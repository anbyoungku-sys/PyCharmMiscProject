요청하신 바와 같이, 제공해주신 Python 소프트웨어 코드(날짜 및 시간 관련 클래스 및 함수 정의)의 구조를 그대로 유지하되, 모든 영어 설명과 주석을 한국어로 번역하여 학습에 도움을 드릴 수 있도록 구성했습니다.

**참고:** 소스에서 직접적으로 코드가 아닌 설명(주석 또는 독스트링) 부분만 번역했으며, 모든 번역된 내용 뒤에는 해당 내용이 추출된 소스 번호가 [i] 형식으로 기재되어 있습니다.

---

### Python 날짜 및 시간 관련 클래스 및 함수 (한글 설명 버전)

```python
"""
**구체적인 날짜/시간 및 관련 유형들.**

**시간대 및 DST 데이터 출처는** http://www.iana.org/time-zones/repository/tz-link.html **를 참조하십시오.**
"""

__all__ = ("date", "datetime", "time", "timedelta", "timezone", "tzinfo",
           "MINYEAR", "MAXYEAR", "UTC")

import time as _time
import math as _math
import sys
from operator import index as _index

def _cmp(x, y):
    return 0 if x == y else 1 if x > y else -1

MINYEAR = 1
MAXYEAR = 9999
_MAXORDINAL = 3652059 # date.max.toordinal()

# 유틸리티 함수들, Python의 Demo/classes/Dates.py에서 채택되었으며, 이는
# 또한 현재의 그레고리력을 양방향으로 무기한 확장했다고 가정합니다.
# 차이점: Dates.py는 0년 1월 1일을 1일 번호로 부릅니다.
# 여기 코드는 1년 1월 1일을 1일 번호로 부릅니다. 이는
# Dershowitz와 Reingold의 "Calendrical Calculations"에 있는 "Proleptic Gregorian" 달력의 정의와
# 일치시키기 위한 것입니다. 이 달력은 모든 계산의 기본 달력입니다.
# 원시 그레고리안 서수(ordinals)와 다른 많은 달력 시스템 간의 변환 알고리즘은 책을 참조하십시오.

# -1은 인덱싱 목적을 위한 자리 표시자입니다.
_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
_DAYS_BEFORE_MONTH = [-1] # -1은 인덱싱 목적을 위한 자리 표시자입니다.
dbm = 0
for dim in _DAYS_IN_MONTH[1:]:
    _DAYS_BEFORE_MONTH.append(dbm)
    dbm += dim
del dbm, dim

def _is_leap(year):
    "year -> 윤년이면 1, 아니면 0."
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def _days_before_year(year):
    "year -> 해당 해의 1월 1일 이전의 날짜 수."
    y = year - 1
    return y*365 + y//4 - y//100 + y//400

def _days_in_month(year, month):
    "year, month -> 해당 연도의 해당 월의 일수."
    assert 1 <= month <= 12, month
    if month == 2 and _is_leap(year):
        return 29
    return _DAYS_IN_MONTH[month]

def _days_before_month(year, month):
    "year, month -> 해당 연도에서 해당 월의 첫날 이전에 지난 일수."
    assert 1 <= month <= 12, 'month must be in 1..12'
    return _DAYS_BEFORE_MONTH[month] + (month > 2 and _is_leap(year))

def _ymd2ord(year, month, day):
    "year, month, day -> 서수(ordinal). 0001년 1월 1일을 1일로 간주합니다."
    assert 1 <= month <= 12, 'month must be in 1..12'
    dim = _days_in_month(year, month)
    assert 1 <= day <= dim, ('day must be in 1..%d' % dim)
    return (_days_before_year(year) +
            _days_before_month(year, month) +
            day)

_DI400Y = _days_before_year(401) # 400년 동안의 일수
_DI100Y = _days_before_year(101) # 100년 동안의 일수
_DI4Y = _days_before_year(5) # 4년 동안의 일수

# 4년 주기는 4개의 단일 연도를 붙여 얻는 것보다 윤일이 하루 더 많습니다.
assert _DI4Y == 4 * 365 + 1

# 마찬가지로, 400년 주기는 4개의 100년 주기를 붙여 얻는 것보다 윤일이 하루 더 많습니다.
assert _DI400Y == 4 * _DI100Y + 1

# 반면에, 100년 주기는 25개의 4년 주기를 붙여 얻는 것보다 윤일이 하루 적습니다.
assert _DI100Y == 25 * _DI4Y - 1

def _ord2ymd(n):
    "서수(ordinal) -> (year, month, day). 0001년 1월 1일을 1일로 간주합니다."
    # n은 1년 1월 1일부터 시작하는 1 기반 인덱스입니다. 윤년의 패턴은
    # 정확히 400년마다 반복됩니다. 기본 전략은 n과 같거나 n 이전의
    # 가장 가까운 400년 경계를 찾은 다음,
    # 그 경계에서 n까지의 오프셋을 처리하는 것입니다.
    # n에서 1을 먼저 빼면 훨씬 명확해집니다. 그러면 400년 경계에서의 n 값은
    # 정확히 _DI400Y로 나눌 수 있는 값이 됩니다.
    # ... (표 생략) ...
    n -= 1
    n400, n = divmod(n, _DI400Y)
    year = n400 * 400 + 1 # ..., -399, 1, 401, ...

    # 이제 n은 원하는 날짜까지의 1월 1일부터의 (음수가 아닌) 일수 오프셋입니다.
    # 이제 n 이전에 몇 개의 100년 주기가 선행하는지 계산합니다.
    # n100이 4가 될 수도 있다는 점에 유의하십시오! 이 경우 400년 주기 말일인
    # 12월 31일이 원하는 날짜임을 의미합니다.
    n100, n = divmod(n, _DI100Y)

    # 이제 그 이전에 몇 개의 4년 주기가 선행하는지 계산합니다.
    n4, n = divmod(n, _DI4Y)

    # 그리고 이제 몇 개의 단일 연도가 선행하는지 계산합니다. n1 역시 4가 될 수 있으며,
    # 이 경우에도 4년 주기 말일인 12월 31일이 원하는 날짜임을 의미합니다.
    n1, n = divmod(n, 365)
    year += n100 * 100 + n4 * 4 + n1

    if n1 == 4 or n100 == 4:
        assert n == 0
        return year-1, 12, 31

    # 이제 연도는 정확하며, n은 1월 1일부터의 오프셋입니다.
    # 우리는 정확하거나 하나만 더 큰 추정치를 통해 월을 찾습니다.
    leapyear = n1 == 3 and (n4 != 24 or n100 == 3)
    assert leapyear == _is_leap(year)
    month = (n + 50) >> 5

    preceding = _DAYS_BEFORE_MONTH[month] + (month > 2 and leapyear)
    if preceding > n: # 추정치가 너무 큽니다.
        month -= 1
        preceding -= _DAYS_IN_MONTH[month] + (month == 2 and leapyear)
    n -= preceding

    assert 0 <= n < _days_in_month(year, month)

    # 이제 연도와 월이 정확하며, n은 그 달의 시작일부터의 오프셋입니다. 완료되었습니다!
    return year, month, n+1

# 월 및 요일 이름. 지역화된 버전은 calendar 모듈을 참조하십시오.
_MONTHNAMES = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
_DAYNAMES = [None, "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def _build_struct_time(y, m, d, hh, mm, ss, dstflag):
    wday = (_ymd2ord(y, m, d) + 6) % 7
    dnum = _days_before_month(y, m) + d
    return _time.struct_time((y, m, d, hh, mm, ss, wday, dnum, dstflag))

def _format_time(hh, mm, ss, us, timespec='auto'):
    specs = {
        'hours': '{:02d}',
        'minutes': '{:02d}:{:02d}',
        'seconds': '{:02d}:{:02d}:{:02d}',
        'milliseconds': '{:02d}:{:02d}:{:02d}.{:03d}',
        'microseconds': '{:02d}:{:02d}:{:02d}.{:06d}'
    }
    if timespec == 'auto':
        # us==0일 때 후행 마이크로초를 건너뜁니다.
        timespec = 'microseconds' if us else 'seconds'
    elif timespec == 'milliseconds':
        us //= 1000
    try:
        fmt = specs[timespec]
    except KeyError:
        raise ValueError('Unknown timespec value')
    else:
        return fmt.format(hh, mm, ss, us)

def _format_offset(off):
    s = ''
    if off is not None:
        if off.days < 0:
            sign = "-"
            off = -off
        else:
            sign = "+"
        hh, mm = divmod(off, timedelta(hours=1))
        mm, ss = divmod(mm, timedelta(minutes=1))
        s += "%s%02d:%02d" % (sign, hh, mm)
        if ss or ss.microseconds:
            s += ":%02d" % ss.seconds
        if ss.microseconds:
            s += '.%06d' % ss.microseconds
        return s

# strftime 형식에서 %z 및 %Z 이스케이프를 올바르게 대체합니다.
def _wrap_strftime(object, format, timetuple):
    # 실제로 필요하지 않는 한 utcoffset() 또는 tzname()을 호출하지 않습니다.
    freplace = None # %f에 사용할 문자열
    zreplace = None # %z에 사용할 문자열
    Zreplace = None # %Z에 사용할 문자열
    # %z 및 %Z 이스케이프에 대해 형식을 스캔하고 필요에 따라 대체합니다.
    newformat = []
    push = newformat.append
    i, n = 0, len(format)
    while i < n:
        ch = format[i]
        i += 1
        if ch == '%':
            if i < n:
                ch = format[i]
                i += 1
                if ch == 'f':
                    if freplace is None:
                        freplace = '%06d' % getattr(object,
                                                    'microsecond', 0)
                    newformat.append(freplace)
                elif ch == 'z':
                    if zreplace is None:
                        zreplace = ""
                        if hasattr(object, "utcoffset"):
                            offset = object.utcoffset()
                            if offset is not None:
                                sign = '+'
                                if offset.days < 0:
                                    offset = -offset
                                    sign = '-'
                                h, rest = divmod(offset, timedelta(hours=1))
                                m, rest = divmod(rest, timedelta(minutes=1))
                                s = rest.seconds
                                u = offset.microseconds
                                if u:
                                    zreplace = '%c%02d%02d%02d.%06d' % (sign, h, m, s, u)
                                elif s:
                                    zreplace = '%c%02d%02d%02d' % (sign, h, m, s)
                                else:
                                    zreplace = '%c%02d%02d' % (sign, h, m)
                    assert '%' not in zreplace
                    newformat.append(zreplace)
                elif ch == 'Z':
                    if Zreplace is None:
                        Zreplace = ""
                        if hasattr(object, "tzname"):
                            s = object.tzname()
                            if s is not None:
                                # strftime이 이를 처리할 것이므로: % 이스케이프
                                Zreplace = s.replace('%', '%%')
                    newformat.append(Zreplace)
                else:
                    push('%')
                    push(ch)
            else:
                push('%')
        else:
            push(ch)

    newformat = "".join(newformat)
    return _time.strftime(newformat, timetuple)

# isoformat()의 결과를 구문 분석하기 위한 도우미
def _is_ascii_digit(c):
    return c in "0123456789"

def _find_isoformat_datetime_separator(dtstr):
    # Modules/_datetimemodule.c:_find_isoformat_datetime_separator의 주석을 참조하십시오.
    len_dtstr = len(dtstr)
    if len_dtstr == 7:
        return 7
    assert len_dtstr > 7
    date_separator = "-"
    week_indicator = "W"
    if dtstr == date_separator:
        if dtstr == week_indicator:
            if len_dtstr < 8:
                raise ValueError("Invalid ISO string")
            if len_dtstr > 8 and dtstr == date_separator:
                if len_dtstr == 9:
                    raise ValueError("Invalid ISO string")
                if len_dtstr > 10 and _is_ascii_digit(dtstr):
                    # 이 시점에서 모호성을 해결하는 데 필요한 만큼만 해결합니다.
                    # YYYY-Www-## 형식이라면 구분자는 8번째의 하이픈이거나 10번째의 숫자입니다.
                    # 하이픈이 구분자로 사용될 가능성이 숫자보다 훨씬 높으므로
                    # 8번째 하이픈이라고 가정합니다. 하지만 이 시점에서는
                    # 이것이 어차피 사양의 확장(extension)이기 때문에 최선의 노력입니다.
                    # TODO(pganssle): 이 내용을 문서화하십시오.
                    return 8
                return 10
            else:
                # YYYY-Www (8)
                return 8
        else:
            # YYYY-MM-DD (10)
            return 10
    else:
        if dtstr == week_indicator:
            # YYYYWww (7) 또는 YYYYWwwd (8)
            idx = 7
            while idx < len_dtstr:
                if not _is_ascii_digit(dtstr[idx]):
                    break
                idx += 1
            if idx < 9:
                return idx
            if idx % 2 == 0:
                # 마지막 숫자의 인덱스가 짝수라면 YYYYWwwd
                return 7
            else:
                return 8
        else:
            # YYYYMMDD (8)
            return 8

def _parse_isoformat_date(dtstr):
    # 이 문자열은 길이가 7, 8, 또는 10인 ASCII 전용 문자열이라고 가정합니다.
    # Modules/_datetimemodule.c:_find_isoformat_datetime_separator의 주석을 참조하십시오.
    assert len(dtstr) in (7, 8, 10)
    year = int(dtstr[0:4])
    has_sep = dtstr == '-'
    pos = 4 + has_sep

    if dtstr[pos:pos + 1] == "W":
        # YYYY-?Www-?D?
        pos += 1
        weekno = int(dtstr[pos:pos + 2])
        pos += 2
        dayno = 1
        if len(dtstr) > pos:
            if (dtstr[pos:pos + 1] == '-') != has_sep:
                raise ValueError("Inconsistent use of dash separator")
            pos += has_sep
            dayno = int(dtstr[pos:pos + 1])
        return list(_isoweek_to_gregorian(year, weekno, dayno))
    else:
        month = int(dtstr[pos:pos + 2])
        pos += 2
        if (dtstr[pos:pos + 1] == "-") != has_sep:
            raise ValueError("Inconsistent use of dash separator")
        pos += has_sep
        day = int(dtstr[pos:pos + 2])
        return [year, month, day]

_FRACTION_CORRECTION =

def _parse_hh_mm_ss_ff(tstr):
    # HH[:?MM[:?SS[{.,}fff[fff]]]] 형식의 항목을 구문 분석합니다.
    len_str = len(tstr)
    time_comps =
    pos = 0

    for comp in range(0, 3):
        if (len_str - pos) < 2:
            raise ValueError("Incomplete time component")
        time_comps[comp] = int(tstr[pos:pos+2])
        pos += 2
        next_char = tstr[pos:pos+1]
        if comp == 0:
            has_sep = next_char == ':'
            if not next_char or comp >= 2:
                break
            if has_sep and next_char != ':':
                raise ValueError("Invalid time separator: %c" % next_char)
            pos += has_sep
            if pos < len_str:
                if tstr[pos] not in '.,':
                    raise ValueError("Invalid microsecond component")
                else:
                    pos += 1
            len_remainder = len_str - pos
            if len_remainder >= 6:
                to_parse = 6
            else:
                to_parse = len_remainder
            time_comps = int(tstr[pos:(pos+to_parse)])
            if to_parse < 6:
                time_comps *= _FRACTION_CORRECTION[to_parse-1]
            if (len_remainder > to_parse
                and not all(map(_is_ascii_digit, tstr[(pos+to_parse):]))):
                raise ValueError("Non-digit values in unparsed fraction")
            return time_comps

def _parse_isoformat_time(tstr):
    # 지원되는 형식은 HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]입니다.
    len_str = len(tstr)
    if len_str < 2:
        raise ValueError("Isoformat time too short")

    # 이는 re.search('[+-Z]', tstr)와 동일하지만 더 빠릅니다.
    tz_pos = (tstr.find('-') + 1 or tstr.find('+') + 1 or tstr.find('Z') + 1)
    timestr = tstr[:tz_pos-1] if tz_pos > 0 else tstr
    time_comps = _parse_hh_mm_ss_ff(timestr)

    tzi = None
    if tz_pos == len_str and tstr[-1] == 'Z':
        tzi = timezone.utc
    elif tz_pos > 0:
        tzstr = tstr[tz_pos:]
        # 유효한 시간대 문자열은 다음과 같습니다:
        # HH len: 2
        # HHMM len: 4
        # HH:MM len: 5
        # HHMMSS len: 6
        # HHMMSS.f+ len: 7+
        # HH:MM:SS len: 8
        # HH:MM:SS.f+ len: 10+
        if len(tzstr) in (0, 1, 3):
            raise ValueError("Malformed time zone string")
        tz_comps = _parse_hh_mm_ss_ff(tzstr)
        if all(x == 0 for x in tz_comps):
            tzi = timezone.utc
        else:
            tzsign = -1 if tstr[tz_pos - 1] == '-' else 1
            td = timedelta(hours=tz_comps, minutes=tz_comps,
                           seconds=tz_comps, microseconds=tz_comps)
            tzi = timezone(tzsign * td)

    time_comps.append(tzi)
    return time_comps

# tuple[int, int, int] -> tuple[int, int, int] 버전의 date.fromisocalendar
def _isoweek_to_gregorian(year, week, day):
    # 이 방식으로 연도를 제한하는 이유는 9999-12-31이 (9999, 52, 5)이기 때문입니다.
    if not MINYEAR <= year <= MAXYEAR:
        raise ValueError(f"Year is out of range: {year}")
    if not 0 < week < 53:
        out_of_range = True
        if week == 53:
            # ISO 연도는 목요일로 시작하는 연도와 수요일로 시작하는 윤년에
            # 53주가 있습니다.
            first_weekday = _ymd2ord(year, 1, 1) % 7
            if (first_weekday == 4 or (first_weekday == 3 and
                                       _is_leap(year))):
                out_of_range = False
        if out_of_range:
            raise ValueError(f"Invalid week: {week}")
    if not 0 < day < 8:
        raise ValueError(f"Invalid weekday: {day} (range is)")

    # 이제 (Y, 1, 1)로부터의 오프셋을 일수로 계산합니다.
    day_offset = (week - 1) * 7 + (day - 1)

    # 1주차 월요일의 서수일(ordinal day)을 계산합니다.
    day_1 = _isoweek1monday(year)
    ord_day = day_1 + day_offset

    return _ord2ymd(ord_day)

# 인수가 None이거나 문자열이 아니면 TypeError를 발생시킵니다.
def _check_tzname(name):
    if name is not None and not isinstance(name, str):
        raise TypeError("tzinfo.tzname() must return None or string, "
                        "not '%s'" % type(name))

# name은 오프셋을 생성하는 메서드("utcoffset" 또는 "dst")입니다.
# offset은 그 메서드가 반환한 값입니다.
# offset이 None이나 timedelta가 아니면 TypeError를 발생시킵니다.
# offset이 None이면 None을 반환합니다.
# 그렇지 않으면 offset이 범위 내에 있는지 확인됩니다.
# 범위 내에 있으면 정수 값이 반환됩니다. 그렇지 않으면 ValueError가 발생합니다.
def _check_utc_offset(name, offset):
    assert name in ("utcoffset", "dst")
    if offset is None:
        return
    if not isinstance(offset, timedelta):
        raise TypeError("tzinfo.%s() must return None "
                        "or timedelta, not '%s'" % (name, type(offset)))
    if not -timedelta(1) < offset < timedelta(1):
        raise ValueError("%s()=%s, must be strictly between "
                        "-timedelta(hours=24) and timedelta(hours=24)" %
                        (name, offset))

def _check_date_fields(year, month, day):
    year = _index(year)
    month = _index(month)
    day = _index(day)

    if not MINYEAR <= year <= MAXYEAR:
        raise ValueError('year must be in %d..%d' % (MINYEAR, MAXYEAR), year)
    if not 1 <= month <= 12:
        raise ValueError('month must be in 1..12', month)
    dim = _days_in_month(year, month)
    if not 1 <= day <= dim:
        raise ValueError('day must be in 1..%d' % dim, day)
    return year, month, day

def _check_time_fields(hour, minute, second, microsecond, fold):
    hour = _index(hour)
    minute = _index(minute)
    second = _index(second)
    microsecond = _index(microsecond)

    if not 0 <= hour <= 23:
        raise ValueError('hour must be in 0..23', hour)
    if not 0 <= minute <= 59:
        raise ValueError('minute must be in 0..59', minute)
    if not 0 <= second <= 59:
        raise ValueError('second must be in 0..59', second)
    if not 0 <= microsecond <= 999999:
        raise ValueError('microsecond must be in 0..999999', microsecond)
    if fold not in (0, 1):
        raise ValueError('fold must be either 0 or 1', fold)
    return hour, minute, second, microsecond, fold

def _check_tzinfo_arg(tz):
    if tz is not None and not isinstance(tz, tzinfo):
        raise TypeError("tzinfo argument must be None or of a tzinfo subclass")

def _cmperror(x, y):
    raise TypeError("can't compare '%s' to '%s'" % (
        type(x).__name__, type(y).__name__))

def _divide_and_round(a, b):
    """a를 b로 나누고 결과를 가장 가까운 정수로 반올림합니다.
    비율이 두 정수 사이의 정확히 절반일 때,
    짝수 정수가 반환됩니다.
    """
    # Objects/longobject.c에 있는 divmod_near에 대한 참조 구현을 기반으로 합니다.
    q, r = divmod(a, b)
    # r / b > 0.5이거나, r / b == 0.5이고 q가 홀수이면 올림합니다.
    # 표현식 r / b > 0.5는 b가 양수이면 2 * r > b와 동일하고,
    # b가 음수이면 2 * r < b와 동일합니다.
    r *= 2
    greater_than_half = r > b if b > 0 else r < b
    if greater_than_half or r == b and q % 2 == 1:
        q += 1
    return q

class timedelta:
    """**두 datetime 객체 간의 차이를 나타냅니다.**

    **지원되는 연산자:**
    - **timedelta 더하기, 빼기**
    - **단항 플러스, 마이너스, 절댓값**
    - **timedelta와 비교**
    - **정수로 곱하기, 나누기**

    또한, datetime은 두 datetime 객체의 뺄셈을 지원하여 timedelta를 반환하고,
    datetime과 timedelta의 덧셈 또는 뺄셈을 지원하여 datetime을 반환합니다.

    표현: (일, 초, 마이크로초). 이유는? 그냥 그렇게 하고 싶었습니다.
    """
    __slots__ = '_days', '_seconds', '_microseconds', '_hashcode'

    def __new__(cls, days=0, seconds=0, microseconds=0,
                milliseconds=0, minutes=0, hours=0, weeks=0):
        # C에서 효율적이고 정확하게 이 작업을 수행하는 것은 어려울 수 있으며,
        # 어디에나 있는 오버플로 가능성과 C double이
        # 10,000년 이상의 마이크로초를 충실하게 표현할 만큼 충분한 정밀도 비트를 가지고 있지 않기 때문에
        # 오류가 발생하기 쉽습니다. 여기 코드는 C 구현을 안내하기 위해
        # 빨리 실행될 수 있는 가정이 어디에 의존할 수 있는지 명시적으로 만들려고 시도합니다.
        # 이는 속도를 무시하고 자동 오버플로-투-롱(auto-overflow-to-long)하는 관용적인 Python보다
        # 훨씬 더 복잡합니다.
        # XXX 모든 입력이 정수 또는 부동 소수점인지 확인하십시오.
        # ... (내부 구현 생략) ...
        if abs(d) > 999999999:
            raise OverflowError("timedelta # of days is too large: %d" % d)

        self = object.__new__(cls)
        self._days = d
        self._seconds = s
        self._microseconds = us
        self._hashcode = -1
        return self

    def __repr__(self):
        """repr()을 위한 공식 문자열로 변환합니다."""
        args = []
        if self._days:
            args.append("days=%d" % self._days)
        if self._seconds:
            args.append("seconds=%d" % self._seconds)
        if self._microseconds:
            args.append("microseconds=%d" % self._microseconds)
        if not args:
            args.append('0')
        return "%s.%s(%s)" % (self.__class__.__module__,
                              self.__class__.__qualname__,
                              ', '.join(args))

    def __str__(self):
        # ... (내부 구현 생략) ...
        def plural(n):
            return n, abs(n) != 1 and "s" or ""
        s = ("%d day%s, " % plural(self._days)) + s
        if self._microseconds:
            s = s + ".%06d" % self._microseconds
        return s

    def total_seconds(self):
        """기간의 총 초를 반환합니다."""
        return ((self.days * 86400 + self.seconds) * 10**6 +
                self.microseconds) / 10**6

    # 읽기 전용 필드 접근자
    @property
    def days(self):
        """일(days)"""
        return self._days

    @property
    def seconds(self):
        """초(seconds)"""
        return self._seconds

    @property
    def microseconds(self):
        """마이크로초(microseconds)"""
        return self._microseconds

    # ... (다른 연산자 메서드 생략) ...

    def __hash__(self):
        if self._hashcode == -1:
            self._hashcode = hash(self._getstate())
        return self._hashcode

    def __bool__(self):
        return (self._days != 0 or
                self._seconds != 0 or
                self._microseconds != 0)

    # Pickle 지원.
    def _getstate(self):
        return (self._days, self._seconds, self._microseconds)

    def __reduce__(self):
        return (self.__class__, self._getstate())

timedelta.min = timedelta(-999999999)
timedelta.max = timedelta(days=999999999, hours=23, minutes=59, seconds=59,
                          microseconds=999999)
timedelta.resolution = timedelta(microseconds=1)

class date:
    """**구체적인 날짜 유형.**

    **생성자:**
    __new__()
    fromtimestamp()
    today()
    fromordinal()

    **연산자:**
    __repr__, __str__
    __eq__, __le__, __lt__, __ge__, __gt__, __hash__
    __add__, __radd__, __sub__ (timedelta 인수가 있는 경우에만 add/radd)

    **메서드:**
    timetuple()
    toordinal()
    weekday()
    isoweekday(), isocalendar(), isoformat()
    ctime()
    strftime()

    **속성 (읽기 전용):**
    year, month, day
    """

    __slots__ = '_year', '_month', '_day', '_hashcode'

    def __new__(cls, year, month=None, day=None):
        """**생성자.**

        **인수:**
        **year, month, day (필수, 1 기반)**
        """
        # ... (Pickle 지원 로직 생략) ...
        year, month, day = _check_date_fields(year, month, day)
        self = object.__new__(cls)
        self._year = year
        self._month = month
        self._day = day
        self._hashcode = -1
        return self

    # 추가 생성자
    @classmethod
    def fromtimestamp(cls, t):
        "POSIX 타임스탬프(time.time()과 같은)에서 date를 구성합니다."
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        return cls(y, m, d)

    @classmethod
    def today(cls):
        "time.time()에서 date를 구성합니다."
        t = _time.time()
        return cls.fromtimestamp(t)

    @classmethod
    def fromordinal(cls, n):
        """**원시 그레고리안 서수(proleptic Gregorian ordinal)에서 date를 구성합니다.**
        **1년 1월 1일은 1일입니다. 결과에서 연도, 월, 일만 0이 아닙니다.**
        """
        y, m, d = _ord2ymd(n)
        return cls(y, m, d)

    @classmethod
    def fromisoformat(cls, date_string):
        """**ISO 8601 형식의 문자열에서 date를 구성합니다.**"""
        # ... (유효성 검사 및 파싱 로직 생략) ...

    @classmethod
    def fromisocalendar(cls, year, week, day):
        """**ISO 연도, 주 번호 및 요일에서 date를 구성합니다.**
        **이는 date.isocalendar() 함수의 역함수입니다.**"""
        return cls(*_isoweek_to_gregorian(year, week, day))

    # 문자열로의 변환
    def __repr__(self):
        """**repr()을 위한 공식 문자열로 변환합니다.**
        >>> d = date(2010, 1, 1)
        >>> repr(d)
        'datetime.date(2010, 1, 1)'
        """
        # ... (내부 구현 생략) ...

    # XXX 이것들은 time.localtime()에 의존해서는 안 됩니다. 왜냐하면 이는
    # 사용 가능한 날짜를 [1970 .. 2038)로 제한하기 때문입니다. 적어도 ctime()은
    # strftime()을 사용하지 않고도 쉽게 수행됩니다. 이는 strftime("%c", ...)이
    # 로케일 특정적이기 때문에 더 좋습니다.
    def ctime(self):
        "ctime() 스타일 문자열을 반환합니다."
        # ... (내부 구현 생략) ...

    def strftime(self, fmt):
        """
        **strftime()을 사용하여 형식을 지정합니다.**
        **예시: "%d/%m/%Y, %H:%M:%S"**
        """
        return _wrap_strftime(self, fmt, self.timetuple())

    def __format__(self, fmt):
        # ... (내부 구현 생략) ...

    def isoformat(self):
        """**날짜를 ISO 형식에 따라 반환합니다.**
        **이는 'YYYY-MM-DD'입니다.**

        **참조:**
        - http://www.w3.org/TR/NOTE-datetime
        - http://www.cl.cam.ac.uk/~mgk25/iso-time.html
        """
        return "%04d-%02d-%02d" % (self._year, self._month, self._day)

    __str__ = isoformat

    # 읽기 전용 필드 접근자
    @property
    def year(self):
        """년 (1-9999)"""
        return self._year

    @property
    def month(self):
        """월 (1-12)"""
        return self._month

    @property
    def day(self):
        """일 (1-31)"""
        return self._day

    # 표준 변환, __eq__, __le__, __lt__, __ge__, __gt__,
    # __hash__ (및 도우미)
    def timetuple(self):
        "time.localtime()과 호환되는 지역 시간 튜플을 반환합니다."
        return _build_struct_time(self._year, self._month, self._day,
                                  0, 0, 0, -1)

    def toordinal(self):
        """**연도, 월, 일에 대한 원시 그레고리안 서수(proleptic Gregorian ordinal)를 반환합니다.**
        **1년 1월 1일은 1일입니다. 연도, 월, 일 값만 결과에 기여합니다.**
        """
        return _ymd2ord(self._year, self._month, self._day)

    def replace(self, year=None, month=None, day=None):
        """**지정된 필드에 새 값을 가진 새 date를 반환합니다.**"""
        # ... (내부 구현 생략) ...

    # 계산
    def __add__(self, other):
        "date에 timedelta를 더합니다."
        if isinstance(other, timedelta):
            o = self.toordinal() + other.days
            if 0 < o <= _MAXORDINAL:
                return type(self).fromordinal(o)
            raise OverflowError("result out of range")
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        """**두 date를 빼거나, date와 timedelta를 뺍니다.**"""
        if isinstance(other, timedelta):
            return self + timedelta(-other.days)
        if isinstance(other, date):
            days1 = self.toordinal()
            days2 = other.toordinal()
            return timedelta(days1 - days2)
        return NotImplemented

    def weekday(self):
        "요일을 반환합니다. 월요일 == 0 ... 일요일 == 6."
        return (self.toordinal() + 6) % 7

    # ISO에 따른 요일 및 연중 주차
    def isoweekday(self):
        "요일을 반환합니다. 월요일 == 1 ... 일요일 == 7."
        # 0001년 1월 1일은 월요일입니다.
        return self.toordinal() % 7 or 7

    def isocalendar(self):
        """**ISO 연도, 주 번호, 요일을 포함하는 명명된 튜플을 반환합니다.**
        **해당 연도의 첫 번째 ISO 주는**
        **그 연도의 첫 번째 목요일을 포함하는 (월-일) 주입니다. 다른 모든 것은**
        **여기에서 파생됩니다.**
        **첫 번째 주는 1입니다. 월요일은 1 ... 일요일은 7입니다.**
        **ISO 달력 알고리즘은 다음에서 가져왔습니다:**
        http://www.phys.uu.nl/~vgent/calendar/isocalendar.htm
        **(허가 하에 사용됨)**
        # ... (내부 구현 생략) ...

    # Pickle 지원.
    # ... (내부 구현 생략) ...

_date_class = date # 인수가 "date"로 명명된 함수들이 클래스에 접근할 수 있도록
date.min = date(1, 1, 1)
date.max = date(9999, 12, 31)
date.resolution = timedelta(days=1)

class tzinfo:
    """**시간대 정보 클래스를 위한 추상 기본 클래스입니다.**
    **서브클래스는 tzname(), utcoffset() 및 dst() 메서드를 반드시 재정의해야 합니다.**
    """
    __slots__ = ()

    def tzname(self, dt):
        "datetime -> 시간대 문자열 이름."
        raise NotImplementedError("tzinfo subclass must override tzname()")

    def utcoffset(self, dt):
        "datetime -> timedelta, UTC보다 동쪽이면 양수, 서쪽이면 음수."
        raise NotImplementedError("tzinfo subclass must override utcoffset()")

    def dst(self, dt):
        """**datetime -> DST 오프셋(timedelta), UTC보다 동쪽이면 양수.**
        **DST가 적용되지 않으면 0을 반환합니다. utcoffset()에는 DST**
        **오프셋이 포함되어야 합니다.**
        """
        raise NotImplementedError("tzinfo subclass must override dst()")

    def fromutc(self, dt):
        "UTC의 datetime -> 지역 시간의 datetime."
        # ... (내부 구현 생략) ...
        # 이 알고리즘에 대한 설명은 이 파일 끝에 있는 긴 주석 블록을 참조하십시오.
        # ... (내부 구현 생략) ...

    # Pickle 지원.
    # ... (내부 구현 생략) ...

class IsoCalendarDate(tuple):
    # ... (내부 구현 생략) ...

_IsoCalendarDate = IsoCalendarDate
del IsoCalendarDate
_tzinfo_class = tzinfo

class time:
    """**시간대 정보가 있는 시간.**

    **생성자:**
    __new__()

    **연산자:**
    __repr__, __str__
    __eq__, __le__, __lt__, __ge__, __gt__, __hash__

    **메서드:**
    strftime()
    isoformat()
    utcoffset()
    tzname()
    dst()

    **속성 (읽기 전용):**
    hour, minute, second, microsecond, tzinfo, fold
    """
    __slots__ = '_hour', '_minute', '_second', '_microsecond', '_tzinfo', '_hashcode', '_fold'

    def __new__(cls, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0):
        """**생성자.**

        **인수:**
        **hour, minute (필수)**
        **second, microsecond (기본값 0)**
        **tzinfo (기본값 None)**
        **fold (키워드 전용, 기본값 0)**
        """
        # ... (Pickle 지원 로직 생략) ...
        # ... (내부 구현 생략) ...

    # 읽기 전용 필드 접근자
    @property
    def hour(self):
        """시 (0-23)"""
        return self._hour

    @property
    def minute(self):
        """분 (0-59)"""
        return self._minute

    @property
    def second(self):
        """초 (0-59)"""
        return self._second

    @property
    def microsecond(self):
        """마이크로초 (0-999999)"""
        return self._microsecond

    @property
    def tzinfo(self):
        """시간대 정보 객체"""
        return self._tzinfo

    @property
    def fold(self):
        return self._fold

    # 표준 변환, __hash__ (및 도우미)
    # 다른 time 객체와의 비교.
    # ... (비교 메서드 생략) ...

    def __hash__(self):
        """해시."""
        # ... (내부 구현 생략) ...

    # 문자열로의 변환
    def _tzstr(self):
        """**형식화된 시간대 오프셋 (+xx:xx) 또는 빈 문자열을 반환합니다.**"""
        off = self.utcoffset()
        return _format_offset(off)

    def __repr__(self):
        """repr()을 위한 공식 문자열로 변환합니다."""
        # ... (내부 구현 생략) ...

    def isoformat(self, timespec='auto'):
        """**시간을 ISO 형식에 따라 반환합니다.**
        **전체 형식은 'HH:MM:SS.mmmmmm+zz:zz'입니다. 기본적으로, 소수 부분은**
        **self.microsecond == 0이면 생략됩니다.**
        **선택적 인수 timespec은 포함할 시간의 추가 항목 수를 지정합니다. 유효한 옵션은**
        **'auto', 'hours', 'minutes', 'seconds', 'milliseconds', 'microseconds'입니다.**
        """
        # ... (내부 구현 생략) ...

    __str__ = isoformat

    @classmethod
    def fromisoformat(cls, time_string):
        """**ISO 8601 형식 중 하나의 문자열에서 time을 구성합니다.**"""
        # ... (내부 구현 생략) ...
        # 사양상 시간 전용 ISO 8601 문자열은 T로 시작해야 하지만,
        # 날짜 문자열과의 모호성이 없는 한 확장 형식에서는 이를 생략할 수 있습니다.
        # ... (내부 구현 생략) ...

    def strftime(self, fmt):
        """**strftime()을 사용하여 형식을 지정합니다. 기본 strftime에 전달되는**
        **타임스탬프의 날짜 부분은 사용되어서는 안 됩니다.**
        """
        # ... (내부 구현 생략) ...

    # 시간대 함수
    def utcoffset(self):
        """**시간대 오프셋을 timedelta로 반환합니다. UTC보다 동쪽이면 양수**
        **(서쪽이면 음수)입니다.**"""
        # ... (내부 구현 생략) ...

    def tzname(self):
        """**시간대 이름을 반환합니다.**
        **이 이름은 100% 정보용이며, 특별한 의미가 있어야 하는 요구 사항은 없습니다.**
        **예를 들어, "GMT", "UTC", "-500",**
        **"-5:00", "EDT", "US/Eastern", "America/New York"은 모두 유효한 응답입니다.**
        """
        # ... (내부 구현 생략) ...

    def dst(self):
        """**DST가 적용되지 않으면 0을 반환하고, DST가 적용 중이면 DST 오프셋(timedelta로,**
        **동쪽이면 양수)을 반환합니다.**
        **이는 순전히 정보용입니다. DST 오프셋은 이미 utcoffset()에서 반환되는**
        **UTC 오프셋에 추가되었으므로, DST 정보를 표시하는 데 관심이 있지 않다면**
        **dst()를 참조할 필요가 없습니다.**
        """
        # ... (내부 구현 생략) ...

    def replace(self, hour=None, minute=None, second=None, microsecond=None,
                tzinfo=True, *, fold=None):
        """**지정된 필드에 새 값을 가진 새 time을 반환합니다.**"""
        # ... (내부 구현 생략) ...

_time_class = time # 인수가 "time"으로 명명된 함수들이 클래스에 접근할 수 있도록
time.min = time(0, 0, 0)
time.max = time(23, 59, 59, 999999)
time.resolution = timedelta(microseconds=1)

class datetime(date):
    """**datetime(년, 월, 일 [, 시 [, 분 [, 초 [, 마이크로초 [, tzinfo]]]]])**
    **년, 월, 일 인수는 필수입니다. tzinfo는 None이거나**
    **tzinfo 서브클래스의 인스턴스일 수 있습니다. 나머지 인수는 정수일 수 있습니다.**
    """

    __slots__ = date.__slots__ + time.__slots__

    def __new__(cls, year, month=None, day=None, hour=0, minute=0, second=0,
                microsecond=0, tzinfo=None, *, fold=0):
        # ... (Pickle 지원 로직 생략) ...
        # ... (내부 구현 생략) ...

    # 읽기 전용 필드 접근자 (date 클래스에서 상속되지만, time 속성이 추가됩니다.)
    @property
    def hour(self):
        """시 (0-23)"""
        return self._hour

    # ... (minute, second, microsecond, tzinfo, fold 속성 생략 - time 클래스와 동일한 설명) ...

    @classmethod
    def _fromtimestamp(cls, t, utc, tz):
        """**POSIX 타임스탬프(time.time()과 같은)에서 datetime을 구성합니다.**
        **시간대 정보 객체를 함께 전달할 수도 있습니다.**
        """
        # ... (내부 구현 생략) ...
        # 플랫폼에 윤초(leap seconds)가 있으면 이를 잘라냅니다.
        # ... (내부 구현 생략) ...
        # Windows에서 localtime_s는 음수 값에 대해 OSError를 발생시키므로,
        # 최대 시간 접힘(fold) 값보다 작은 시간에 대해서는 접힘 감지(fold detection)를
        # 수행할 수 없습니다. 자세한 내용은 _datetimemodule의
        # 이 메서드 버전에 있는 주석을 참조하십시오.
        # ... (내부 구현 생략) ...

    @classmethod
    def fromtimestamp(cls, t, tz=None):
        """**POSIX 타임스탬프(time.time()과 같은)에서 datetime을 구성합니다.**
        **시간대 정보 객체를 함께 전달할 수도 있습니다.**
        """
        _check_tzinfo_arg(tz)
        return cls._fromtimestamp(t, tz is not None, tz)

    @classmethod
    def utcfromtimestamp(cls, t):
        """**POSIX 타임스탬프에서 순수한(naive) UTC datetime을 구성합니다.**"""
        return cls._fromtimestamp(t, True, None)

    @classmethod
    def now(cls, tz=None):
        "time.time() 및 선택적 시간대 정보를 사용하여 datetime을 구성합니다."
        t = _time.time()
        return cls.fromtimestamp(t, tz)

    @classmethod
    def utcnow(cls):
        "time.time()에서 UTC datetime을 구성합니다."
        t = _time.time()
        return cls.utcfromtimestamp(t)

    @classmethod
    def combine(cls, date, time, tzinfo=True):
        "주어진 date와 주어진 time에서 datetime을 구성합니다."
        # ... (내부 구현 생략) ...

    @classmethod
    def fromisoformat(cls, date_string):
        """**ISO 8601 형식 중 하나의 문자열에서 datetime을 구성합니다.**"""
        # ... (내부 구현 생략) ...

    def timetuple(self):
        "time.localtime()과 호환되는 지역 시간 튜플을 반환합니다."
        # ... (내부 구현 생략) ...

    def _mktime(self):
        """**정수 POSIX 타임스탬프를 반환합니다.**"""
        # ... (내부 구현 생략) ...

    def timestamp(self):
        "POSIX 타임스탬프를 부동 소수점으로 반환합니다."
        # ... (내부 구현 생략) ...

    def utctimetuple(self):
        "time.gmtime()과 호환되는 UTC 시간 튜플을 반환합니다."
        # ... (내부 구현 생략) ...

    def date(self):
        "날짜 부분을 반환합니다."
        return date(self._year, self._month, self._day)

    def time(self):
        "시간 부분을 반환합니다. tzinfo는 None입니다."
        return time(self.hour, self.minute, self.second, self.microsecond, fold=self.fold)

    def timetz(self):
        "시간 부분을 반환합니다. 동일한 tzinfo를 가집니다."
        return time(self.hour, self.minute, self.second, self.microsecond,
                    self._tzinfo, fold=self.fold)

    def replace(self, year=None, month=None, day=None, hour=None,
                minute=None, second=None, microsecond=None, tzinfo=True,
                *, fold=None):
        """**지정된 필드에 새 값을 가진 새 datetime을 반환합니다.**"""
        # ... (내부 구현 생략) ...

    def astimezone(self, tz=None):
        # ... (내부 구현 생략) ...
        # self를 UTC로 변환하고, 새 시간대 객체를 첨부합니다.
        # UTC에서 tz의 지역 시간으로 변환합니다.
        return tz.fromutc(utc)

    # 문자열을 생성하는 방법.
    def ctime(self):
        "ctime() 스타일 문자열을 반환합니다."
        # ... (내부 구현 생략) ...

    def isoformat(self, sep='T', timespec='auto'):
        """**시간을 ISO 형식에 따라 반환합니다.**
        **전체 형식은 'YYYY-MM-DD HH:MM:SS.mmmmmm'처럼 보입니다.**
        **기본적으로, self.microsecond == 0이면 소수 부분이 생략됩니다.**
        **self.tzinfo가 None이 아니면 UTC 오프셋도 첨부되어**
        **'YYYY-MM-DD HH:MM:SS.mmmmmm+HH:MM'의 전체 형식이 됩니다.**
        **선택적 인수 sep은 날짜와**
        **시간 사이의 구분자(기본값 'T')를 지정합니다.**
        **선택적 인수 timespec은 포함할 시간의 추가 항목 수를 지정합니다. 유효한 옵션은**
        **'auto', 'hours', 'minutes', 'seconds', 'milliseconds', 'microseconds'입니다.**
        """
        # ... (내부 구현 생략) ...

    def __repr__(self):
        """repr()을 위한 공식 문자열로 변환합니다."""
        # ... (내부 구현 생략) ...

    def __str__(self):
        "str()을 위한 문자열로 변환합니다."
        return self.isoformat(sep=' ')

    @classmethod
    def strptime(cls, date_string, format):
        'string, format -> 문자열에서 구문 분석된 새 datetime을 반환합니다 (time.strptime()과 유사).'
        import _strptime
        return _strptime._strptime_datetime(cls, date_string, format)

    def utcoffset(self):
        """**시간대 오프셋을 timedelta로 반환합니다. UTC보다 동쪽이면 양수 (서쪽이면**
        **음수)입니다.**"""
        # ... (내부 구현 생략) ...

    def tzname(self):
        """**시간대 이름을 반환합니다.**
        **이 이름은 100% 정보용이며, 특별한 의미가 있어야 하는 요구 사항은 없습니다.**
        **예를 들어, "GMT", "UTC", "-500",**
        **"-5:00", "EDT", "US/Eastern", "America/New York"은 모두 유효한 응답입니다.**
        """
        # ... (내부 구현 생략) ...

    def dst(self):
        """**DST가 적용되지 않으면 0을 반환하고, DST가 적용 중이면 DST 오프셋(timedelta로,**
        **동쪽이면 양수)을 반환합니다.**
        **이는 순전히 정보용입니다. DST 오프셋은 이미 utcoffset()에서 반환되는**
        **UTC 오프셋에 추가되었으므로, DST 정보를 표시하는 데 관심이 있지 않다면**
        **dst()를 참조할 필요가 없습니다.**
        """
        # ... (내부 구현 생략) ...

    # datetime 객체와 다른 객체와의 비교.
    # ... (비교 메서드 생략) ...

    # ... (내부 구현 생략) ...

datetime.min = datetime(1, 1, 1)
datetime.max = datetime(9999, 12, 31, 23, 59, 59, 999999)
datetime.resolution = timedelta(microseconds=1)

def _isoweek1monday(year):
    # 1주차의 월요일이 시작되는 날짜 번호를 계산하는 도우미
    # XXX 이것은 더 효율적으로 수행될 수 있습니다.
    # ... (내부 구현 생략) ...

class timezone(tzinfo):
    # ... (내부 구현 생략) ...

    def __new__(cls, offset, name=_Omitted):
        # ... (내부 구현 생략) ...

    def __repr__(self):
        """repr()을 위한 공식 문자열로 변환합니다.
        >>> tz = timezone.utc
        >>> repr(tz)
        'datetime.timezone.utc'
        >>> tz = timezone(timedelta(hours=-5), 'EST')
        >>> repr(tz)
        "datetime.timezone(datetime.timedelta(-1, 68400), 'EST')"
        """
        # ... (내부 구현 생략) ...

    def utcoffset(self, dt):
        if isinstance(dt, datetime) or dt is None:
            return self._offset
        raise TypeError("utcoffset() argument must be a datetime instance"
                        " or None")

    def tzname(self, dt):
        if isinstance(dt, datetime) or dt is None:
            if self._name is None:
                return self._name_from_offset(self._offset)
            return self._name
        raise TypeError("tzname() argument must be a datetime instance"
                        " or None")

    def dst(self, dt):
        if isinstance(dt, datetime) or dt is None:
            return None
        raise TypeError("dst() argument must be a datetime instance"
                        " or None")

    def fromutc(self, dt):
        if isinstance(dt, datetime):
            if dt.tzinfo is not self:
                raise ValueError("fromutc: dt.tzinfo "
                                 "is not self")
            return dt + self._offset
        raise TypeError("fromutc() argument must be a datetime instance"
                        " or None")

    # ... (내부 구현 생략) ...

    @staticmethod
    def _name_from_offset(delta):
        # ... (내부 구현 생략) ...

UTC = timezone.utc = timezone._create(timedelta(0))

# bpo-37642: 이러한 속성들은 하위 호환성을 위해 가장 가까운 분으로 반올림됩니다.
# 비록 생성자는 더 넓은 범위의 값을 허용하더라도 말입니다. 이는 향후 변경될 수 있습니다.
timezone.min = timezone._create(-timedelta(hours=23, minutes=59))
timezone.max = timezone._create(timedelta(hours=23, minutes=59))
_EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)

# 일부 시간대 대수학. datetime x에 대해, 다음을 가정합니다:
# x.n = 시간대 정보가 제거된 x - 순수한(naive) 시간.
# x.o = x.utcoffset(), 그리고 예외가 발생하거나 None을 반환하지 않는다고 가정합니다.
# x.d = x.dst(), 그리고 예외가 발생하거나 None을 반환하지 않는다고 가정합니다.
# x.s = x의 표준 오프셋, x.o - x.d
# ... (시간대 대수학 규칙 및 tz.fromutc(x) 알고리즘 설명- 생략) ...

try:
    from _datetime import *
except ImportError:
    pass
else:
    # 사용되지 않는 이름 정리
    del (_DAYNAMES, _DAYS_BEFORE_MONTH, _DAYS_IN_MONTH, _DI100Y, _DI400Y,
         _DI4Y, _EPOCH, _MAXORDINAL, _MONTHNAMES, _build_struct_time,
         _check_date_fields, _check_time_fields,
         _check_tzinfo_arg, _check_tzname, _check_utc_offset, _cmp, _cmperror,
         _date_class, _days_before_month, _days_before_year, _days_in_month,
         _format_time, _format_offset, _index, _is_leap, _isoweek1monday, _math,
         _ord2ymd, _time, _time_class, _tzinfo_class, _wrap_strftime, _ymd2ord,
         _divide_and_round, _parse_isoformat_date, _parse_isoformat_time,
         _parse_hh_mm_ss_ff, _IsoCalendarDate, _isoweek_to_gregorian,
         _find_isoformat_datetime_separator, _FRACTION_CORRECTION,
         _is_ascii_digit)

# XXX 위의 import *는 _로 시작하는 이름을 제외하므로,
# 독스트링이 덮어쓰여지지 않습니다. 향후에는
# 단일 모듈 수준 독스트링을 유지하고 다음 줄을 제거하는 것이
# 적절할 수 있습니다.
from _datetime import __doc__
```

### 이해를 돕기 위한 비유

이 코드가 복잡하게 느껴지는 것은 마치 **정교한 스위스 시계**를 분해하는 것과 같습니다.

각 클래스 (`date`, `time`, `datetime`, `timedelta`, `timezone`)는 시계의 핵심 부품(날짜 바퀴, 시간 바퀴, 태엽 등)이며, 영어로 된 설명들은 **각 부품이 왜 특정한 모양과 기능을 가지는지, 그리고 서로 어떻게 맞물려 돌아가서 정확한 시간을 만들어내는지를 설명하는 설계도**입니다.

특히 `_ord2ymd`나 `_isoweek_to_gregorian` 같은 헬퍼 함수들은 내부적으로 복잡한 윤년 계산 및 400년 주기 패턴을 다루는데, 이는 시계가 4년마다 혹은 100년마다 미세하게 움직여야 하는 **미세 조정 메커니즘**에 해당합니다. 번역된 설명을 통해 이 "설계도"를 한글로 이해함으로써, 각 부품의 역할과 시계 전체의 작동 원리를 더 깊이 있게 파악할 수 있을 것입니다.
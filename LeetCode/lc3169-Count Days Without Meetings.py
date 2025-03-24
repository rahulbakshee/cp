# sort -> merge intervals -> find unbooked days
# time:O(nlogn), space:O(n), n is the len of meetings
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # 1- sort the intervals
        meetings.sort()

        # 2 - merge intervals
        merged_meetings = []
        for meeting in meetings:
            if not merged_meetings:
                merged_meetings.append(meeting)
                continue
            curr_s, curr_e = meeting
            if curr_s <= merged_meetings[-1][1]:
                merged_meetings[-1][1] = max(curr_e, merged_meetings[-1][1])
            else:
                merged_meetings.append(meeting)

        # 3 - find the unbooked days
        booked = 0
        for meeting in merged_meetings:
            start, end = meeting
            booked += end-start+1

        return days - booked



# line sweep
# time:O(nlogn), space:O(n)
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # 1 - intitalize
        day_map = defaultdict(int)
        prefix_sum = 0
        free_days = 0
        prev_day = days
        has_gap = False

        # 2 - loop over meetings
        for meeting in meetings:
            prev_day = min(prev_day, meeting[0])

            # process start and end of meetings
            day_map[meeting[0]] += 1
            day_map[meeting[1]+1] -= 1

        # 3 - line sweep
        # add all days before the first meeting
        free_days += prev_day - 1
        # sort the day_map based on keys and loop over it
        for curr_day in sorted(day_map.keys()):
            # add current range of days without a meeting
            if prefix_sum == 0:
                free_days += curr_day - prev_day

            prefix_sum += day_map[curr_day]
            prev_day = curr_day


        # add all days after the last day of meeting
        free_days += days - prev_day + 1
        return free_days

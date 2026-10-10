class MemorySimulator:
    @staticmethod
    def fifo(reference_string, num_frames=4):
        frames = []
        history = []
        page_faults = 0
        page_hits = 0

        for page in reference_string:
            if page in frames:
                page_hits += 1
            else:
                page_faults += 1
                if len(frames) < num_frames:
                    frames.append(page)
                else:
                    frames.pop(0)
                    frames.append(page)
            history.append((page, list(frames), "Hit" if page in frames else "Fault"))

        return history, page_hits, page_faults

    @staticmethod
    def lru(reference_string, num_frames=4):
        frames = []
        history = []
        page_faults = 0
        page_hits = 0
        recent_usage = []

        for page in reference_string:
            if page in frames:
                page_hits += 1
                recent_usage.remove(page)
                recent_usage.append(page)
            else:
                page_faults += 1
                if len(frames) < num_frames:
                    frames.append(page)
                    recent_usage.append(page)
                else:
                    lru_page = recent_usage.pop(0)
                    idx = frames.index(lru_page)
                    frames[idx] = page
                    recent_usage.append(page)
            history.append((page, list(frames), "Hit" if page in frames else "Fault"))

        return history, page_hits, page_faults

    @staticmethod
    def optimal(reference_string, num_frames=4):
        frames = []
        history = []
        page_faults = 0
        page_hits = 0
        n = len(reference_string)

        for i, page in enumerate(reference_string):
            if page in frames:
                page_hits += 1
            else:
                page_faults += 1
                if len(frames) < num_frames:
                    frames.append(page)
                else:
                    farthest_use = -1
                    page_to_replace = -1
                    for f in frames:
                        try:
                            next_use = reference_string[i+1:].index(f)
                        except ValueError:
                            next_use = float('inf')
                        
                        if next_use > farthest_use:
                            farthest_use = next_use
                            page_to_replace = f
                    
                    idx = frames.index(page_to_replace)
                    frames[idx] = page
            history.append((page, list(frames), "Hit" if page in frames else "Fault"))

        return history, page_hits, page_faults

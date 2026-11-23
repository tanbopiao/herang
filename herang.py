"""合壤（HERANG）· 冲突消解、基线收敛

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：冲突消解、基线收敛。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Herang:
    """合壤（HERANG）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "HERANG"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "herang",
            "cn": "合壤",
            "code": self.CODE,
            "duty": "冲突消解、基线收敛",
            "mingwen": "会盟归一，异见定宗",
            "anchor": self.ANCHOR,
        }

    def resolve(self, conflicts):
        """对冲突清单出消解方案，会盟归一。"""
        import json
        plan = []
        for c in conflicts:
            versions = c.get("versions", [])
            counts = {}
            for v in versions:
                key = json.dumps(v, sort_keys=True, ensure_ascii=False)
                counts[key] = counts.get(key, 0) + 1
            best_key = max(counts, key=counts.get)
            plan.append({"key": c.get("key"), "resolved": json.loads(best_key),
                         "quorum": counts[best_key] > len(versions) / 2})
        self.events.append({"event": "resolve", "conflicts": len(conflicts)})
        return plan

    def converge(self, baselines):
        """多基线收敛为单一真值基线。"""
        if not baselines:
            raise ValueError("无基线可收敛")
        keys = set()
        for b in baselines:
            keys |= set(b)
        merged = {}
        for k in sorted(keys):
            values = [b[k] for b in baselines if k in b]
            if len(values) > 1 and len({repr(v) for v in values}) > 1:
                merged[k] = self.resolve([{"key": k, "versions": values}])[0]["resolved"]
            else:
                merged[k] = values[0]
        self.events.append({"event": "converge", "keys": len(merged)})
        return merged

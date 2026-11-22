"""合壤（HERANG）· 冲突消解、基线收敛

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：冲突消解、基线收敛。

边界：本件为算子骨架 v0——接口先立、实现随进化轮补齐；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Herang:
    """合壤（HERANG）算子骨架 v0。"""

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
        """对冲突清单出消解方案，会盟归一（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("HERANG.resolve 骨架桩，候进化轮补齐")

    def converge(self, baselines):
        """多基线收敛为单一真值基线（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("HERANG.converge 骨架桩，候进化轮补齐")

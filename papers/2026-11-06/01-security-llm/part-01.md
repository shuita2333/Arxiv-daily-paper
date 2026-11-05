# 🔐 大模型安全相关研究 | 2026年11月06日

> 本类共 **1** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Addition by Subtraction: Toward Mitigating Fragile Safety Alignment in Large Language Models](https://arxiv.org/abs/2611.06553)

**<font color=#1a73e8>作者：</font>** Hamid Dashtbani, Alexandra Dmitrienko  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) undergo safety alignment to prevent harmful generations, yet they remain vulnerable to jailbreak attacks. Recent work reveals a deeper structural weakness: safety alignment can be highly sparse, such that pruning a small number of safety-critical neurons or ablating a single refusal direction can substantially undermine aligned behavior. In this work, we take the first steps toward strengthening safety alignment such that it is less dependent on sparse model components. We propose Addition by Subtraction, which gradually removes identified safety-critical neurons during finetuning and uses preference optimization to re-establish safety-aligned behavior through other parts of the model. Our results show that the resulting models are substantially more robust to pruning-based attacks. Remarkably, these benefits generalize beyond the white-box attacks motivating our design: Addition by Subtraction improves robustness against other sparsity-based interventions, including refusal-direction ablation, as well as a broad range of black-box jailbreak attacks. The finetuned models also exhibit improved truthfulness while largely preserving general capabilities. Comprehensive experiments across four models from three vendors demonstrate consistent improvements in safety robustness, reducing attack success rates by up to 90% for some attacks.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

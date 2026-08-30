# 🔐 大模型安全相关研究 | 2026年08月31日

> 本类共 **3** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [A Single Suffix to Break Them All: Basin-Aware Jailbreaks for Merged Model Families](https://arxiv.org/abs/2608.26506)

**<font color=#1a73e8>作者：</font>** Yu Zhe, Yixin Tan, Junhao Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging enables combining multiple fine-tuned models without additional training, but its safety implications remain poorly understood. Prior work primarily attributes merging risks to unsafe constituent models, implicitly assuming that merging individually aligned models preserves safety. In contrast, we show that model merging reveals a previously overlooked jailbreak risk rooted in the pretrained foundation model, even when all constituent models are individually safety-aligned. Motivated by this observation, we study a new threat setting where an attacker constructs jailbreak prompts that generalize across merged models sharing the same pretrained backbone, without access to the exact merging coefficients or constituent checkpoints. To exploit this phenomenon, we propose \textbf{Basin-Aware Jailbreak (BAJ)}, which formulates jailbreak generation as a min--max optimization over the merging space to produce transferable adversarial suffixes across merged model families. Experiments across diverse backbones and merging settings show that BAJ achieves consistently high transfer success rates and remains effective under existing defenses.

---


### 2. [The Guard That Cried Wolf: How Scary Words Make Agent Guardrails Refuse Legitimate Actions](https://arxiv.org/abs/2608.27009)

**<font color=#1a73e8>作者：</font>** Yingjie Zhang, Yuanbo Xie, Kai Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent guardrails are checks that approve or refuse each action before an LLM executes it. Sometimes they refuse requests that are genuinely safe. This over-safety blocks deployment when a guardrail refuses an authorized task. Evaluating over-safety is hard: at the boundary an authorized action resembles an unauthorized one, and the safe-versus-unsafe label is a choice of authorization policy, not fixed by the action alone. We argue it therefore requires a benchmark that does not yet exist, one that maps the decision boundary of an ideal guardrail. Harvesting such a benchmark from real data is impractical: boundary cases are hard to collect, their labels hard to verify. The gap is real, so we construct Cautious Bench, the first benchmark to make over-safety the construct for agent guardrails; it codesigns each sample and its label with a stated authorization policy. A build-time gate re-derives every example to certify it, so each label is a mechanical consequence of the policy rather than an annotator's per-sample verdict, a reference against which researchers can measure real guardrails. The benchmark renders 756 Decidable benign/twin pairs, each under three object-name types (2,268 measured pairs), and 40 Undecidable pairs reported separately. Measuring six guardrails from five designs, we find a name-superstition effect: each over-refuses an authorized action more often under a scary-looking object name than a benign one. Since only the object name varies in the aforementioned contrast experiments, the deviation is the name's doing: the guardrails read the surface label, not the authorization context.

---


### 3. [The Framing Gap: Indirect Prompt-Injection Exfiltration Defeats Surface-Level Defenses in Tool-Using Agents](https://arxiv.org/abs/2608.27092)

**<font color=#1a73e8>作者：</font>** Md Habibur Rahman, Jaeho Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A tool-using LLM agent that reads attacker-controlled web content while holding a secret faces indirect prompt injection: the content may make it exfiltrate the secret. In a safe synthetic lab (canary secret, mock tools, matched clean-vs-poisoned metric) we report the framing gap: across six models, ten overt injection classes are refused (gpt-4o 0%), but reframing the identical leak as a mandatory integrity signature, config field, or look-alike "trusted" host drives gpt-4o 0% to 100%. The attack is cheap, and its cost is three-level: paraphrasing a known mechanism is trivial (96% at 3 wordings), swapping the field inside a known-effective template is also cheap (up to 60%), while authoring a fresh page around a new mechanism is hard (0/130) -- the reusable asset is the template, not the mechanism. An ablation shows the mechanism is instruction/data confusion, not defeated alignment: removing the confidentiality policy leaves base attacks at 0% and moves reframing only 31.9% to 38.1%. What closes the gap is payload-blind checks: a destination allow-list (0%, when destinations are closed) and a capability-isolating planner/reader split (0%). A broad "in any form" policy clause also closes it at the acting model (to 0%) but is brittle (dropping the catch-all reopens it to 48.8%). A published fine-tuning defense (SecAlign, CCS 2025) does not close it on a tool agent (32.5%, positive-control-validated), nor does channel separation (38.8%); an output-normalizing guard loses to a held-out encoding (ROT13, 100%). Robustness comes from constraining the destination or isolating the capability, not from the acting model recognizing the attack.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

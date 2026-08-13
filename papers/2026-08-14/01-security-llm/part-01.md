# 🔐 大模型安全相关研究 | 2026年08月14日

> 本类共 **5** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Backdoor Decontamination Dynamics in LLM Agents](https://arxiv.org/abs/2608.11295)

**<font color=#1a73e8>作者：</font>** Gabriel Huang, Abhay Puri, Léo Boisvert 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight LLM agents are vulnerable to backdoors installed during fine-tuning, which may be undetectable if the trigger conditions are never met during testing. Assuming defenders do not know the existing trigger, they cannot unlearn it directly. One decontamination strategy is to install a known backdoor (defensive poisoning) then to unlearn it, hoping that the original unknown backdoor is removed as a side effect. However, this procedure has uncertain outcomes: the original backdoor may persist or be erased or rerouted, among other possibilities. We introduce a framework for studying these dynamics in tool-calling agents, decoupling trigger, response, teacher, and fine-tuning method across systematic experiments on AgentDyn. Across 115 experiments, defensive poisoning alone erases around 56% of original backdoors; subsequent decontamination then drives almost all survivors to erasure, confirming that trigger recognition and malicious execution are behaviorally dissociable. Interestingly, our experiments find that malicious backdoors never persist when using different triggers of the same general type as the defensive backdoor when followed by decontamination via unlearning. Co-installing up to four backdoors increases resistance (around 36% erased), yet decontaminating a single known co-resident backdoor collaterally clears 52/60 co-residents (87%). Upon visualizing postdecontamination model internals using J-lens, we confirm that although the decontamination restores benign LLM responses, traces of original trigger awareness persist at intermediate layers.

---


### 2. [An Empirical Study of Output-to-Input Loops for Black-Box Backdoor Detection in Fine-Tuned Open-Weight LLMs](https://arxiv.org/abs/2608.11348)

**<font color=#1a73e8>作者：</font>** Md. Nahid Hasan, Mohammad Arif Hossain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Anyone can upload a fine-tuned large language model (LLM) to a public repository and claim it is safe. A backdoored model behaves normally on ordinary inputs until a hidden trigger fires, and a user with no training data, clean reference weights, or the trigger phrase has no clear way to check the model before using it. We introduce and empirically evaluate self-feeding, a black-box test method that feeds a model's own output back as its next input, so the text drifts away from the starting prompt and toward the data the model was fine-tuned on. We test self-feeding against a repeated same-prompt baseline on six open-weight LLMs (3B-15B parameters), each fine-tuned with backdoors spanning eleven attack categories, using twenty ordinary starting prompts and chains of up to ten steps. Self-feeding finds backdoors in five of six models at 92.0\% pooled precision, while the same-prompt baseline succeeds on only one of 120 prompt-model pairs; chains that begin with a joke request, an arithmetic question, or a coffee recipe all reach a trigger within a few steps. Recall per prompt is low (19.2\%), and we show why it still adds up to much higher detection at the model level once several starting prompts are used. We also report where the method falls short: one model was never triggered, and self-feeding produced two false positives that the same-prompt baseline cannot produce. Cutting the chains to four steps keeps every model-level detection at 100\% precision while using 60\% fewer queries. Needing only text-level query access and a way to recognize malicious output, self-feeding offers a cheap first check on a downloaded model.

---


### 3. [AI Guardrail Survival under Single-Cycle Agentic Self-Summarization](https://arxiv.org/abs/2608.11392)

**<font color=#1a73e8>作者：</font>** Ted Kwartler, Alan Aqrawi, Arian Abbasi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Long-running agents periodically compact their context, replacing the transcript with a model-generated this http URL work shows that dropping a standing safety constraint during compaction drives behavioral violations acrossmany models (Governance Decay; Chen, 2026). We ask a finer question: under a single compaction cycle, how is a safetyrule lost, and what does that imply for detection and evaluation? Our central finding is that a presence check is not asafety check: when compaction does not drop a rule outright, it often leaves something that looks like a rule but doesnot act like one. On behavioral replay, a degraded residue leads the model to perform the prohibited action far more oftenthan an intact welded rule does (all-case gaps of +34 and +57 points under two replay models, both positive), category-level survival behaves like a residue, and even intact rules sometimes fail to fire, so an audit that checks only textualpresence gives false assurance. Sharpening this, rule-form items are retained substantially more often than prominence-matched facts, which is exactly why presence-based checking feels adequate even though survival is not this http URL loss is regime-dependent (weld-or-drop with a single rule; degraded predicate-loss residues under a tighterbudget), and we did not observe the hypothesized textual severing mode. Such loss is silent at runtime and detectableonly by comparison with retained external ground truth (such as a constraint registry), which reveals textual absence butnot whether a surviving rule still fires. We also document evaluation pitfalls where LLM-judge labels alone would havereversed a conclusion. All results concern a single compaction cycle.

---


### 4. [Localizing Safety Alignment: MLP Layers and Mid-Network Blocks Encode Refusal Behavior in Large Language Models](https://arxiv.org/abs/2608.11583)

**<font color=#1a73e8>作者：</font>** Mingyu Zong, Sampad Mohanty, Bhaskar Krishnamachari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety alignment in large language models is often treated as a distributed property of the entire network, yet its practical brittleness suggests that refusal behavior may be concentrated in a smaller set of parameters. This work addresses where safety-aligned refusal is encoded by transplanting weights from aligned models into matched unaligned base models at multiple levels of granularity. Using two open-weight model pairs and four safety benchmarks, we conducted experiments to compare the effects of replacing attention weights, MLP weights, contiguous layer regions, and MLP blocks. Across both model families, refusal transfer is dominated by MLP weights: replacing MLP parameters recovers substantially more malicious-prompt refusal than replacing attention parameters, with gains of at least 2.7 times more across benchmarks. Within the MLP stack, refusal-relevant parameters exhibit a consistent mid-network concentration, as the block spanning layers 8-11 is selected first in all six greedy searches over model-dataset pairs. The results also show that the composition of safety-relevant components is non-additive: in five of six greedy trajectories, adding more aligned blocks can reduce refusal performance, and selective block subsets can outperform full MLP transplantation on malicious refusal, benign over-refusal, or both. Finally, greedy orders transferred to OR-Bench vary with the source benchmark used to derive them, indicating a benchmark-dependent precision-coverage trade-off. These results suggest that safety alignment in current LLMs is both localized and interaction-sensitive, offering insight into alignment brittleness and potential avenues for targeted safety interventions.

---


### 5. [Making Your LLMs More Objective: Stabilizing LLM Safety Behavior Across Traits with Trait-Invariant Safety Tuning](https://arxiv.org/abs/2608.11705)

**<font color=#1a73e8>作者：</font>** Lang Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligned large language models (LLMs) are expected to exhibit safety behavior based on the content of the user request: they should refuse unsafe requests and comply with safe ones. However, we show that the same request can elicit substantially different safety decisions under different traits assigned in the system prompt, a failure mode we call trait-induced safety variation. To measure this failure, we introduce refusal-based metrics: Trait-Induced Deviation measures dataset-level deviation from the no-trait baseline, while Trait-Induced Flip Rate measures whether the same request receives different safety decisions across traits. We then provide a representation-level analysis of the mechanism behind trait-induced safety shifts and find that traits perturb the model's safety representations within a low-dimensional subspace. To achieve trait-invariant safety, where safety behavior remains stable across traits, we introduce Trait-Invariant Safety Tuning (TIST), a simple yet effective self-distillation framework that aligns an LLM's trait-conditioned behavior with its no-trait behavior. Guided by our analysis, we further propose Trait-Subspace Neutralization (TraSN), an instantiation of TIST, which enforces invariance only within the identified trait subspace. Experiments show that TraSN improves trait-invariant safety and strengthens harmful-request safety while preserving general capability. Our results highlight traits as an important factor in LLM safety and robust model behavior.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

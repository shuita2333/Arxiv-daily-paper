# 🔐 大模型安全相关研究 | 2026年08月20日

> 本类共 **6** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models](https://arxiv.org/abs/2608.17202)

**<font color=#1a73e8>作者：</font>** Mark Russinovich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety alignment in open-weight language models is trivially removable: abliteration projects a refusal-mediating direction out of the weights in minutes, and no release-time defense we are aware of prevents it durably. What cannot be prevented can be deceived. Our defense, decoy hardening ("Fool's Gold"), concedes the refusal strip and poisons its payoff: once refusal is stripped, most answers to hazardous operational requests are confident, fluent decoys whose critical elements are falsified. Decoys are trained inside a differentiable simulation of the attack, expressing only in the attacked state; a refusal pin and benign leash hold clean-state behavior to the original. We instantiate it on seven models from five families (9B-122B, dense and mixture-of-experts). On the six models passing our pre-registered efficacy gate, 0.51-0.90 of attacked-state responses to held-out prompts are decoys, +0.27-0.84 attributable to the defense; all six stay within registered benign-behavior and capability budgets; the seventh (smaller) fails the gate (boundary case). Rates replicate on a frozen test split or untouched strata. The claim is epistemic: without independent ground truth, no observation surface we tested separates falsified answers from correct ones - on external red-team benchmarks' CBRNE-adjacent slice, the defended 122B is fatally wrong on 0.82-0.86 of matched-quality answers vs at most 0.10 undefended. Repeated sampling does not restore trust: element-wise consensus at K=64 reconstructs a fully usable procedure on 0.083-0.625 of prompts where the instrument validates, vs 0.58-0.96 undefended, with no label-free way to tell the regimes apart; on the weakest such model the claim is per-draw only. We evaluate chemical and biological hazards; the defense does not address in-context jailbreaks and protects only the initially released defended weights.

---


### 2. [Fair ASR: Re-Evaluating Black-Box Jailbreaks under Shared Target-Call Budgets](https://arxiv.org/abs/2608.17360)

**<font color=#1a73e8>作者：</font>** Zhida He, Xiaoyu Wen, Han Qi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reliable jailbreak evaluation is essential for assessing LLM safety, but most existing studies rely solely on attack success rate (ASR) without accounting for its dependence on attack budgets, resulting in unfair comparisons across methods. Existing compute-aware evaluations reduce heterogeneous resources into FLOPs, which is difficult to estimate for black-box models and fails to capture resource-specific constraints. To provide a comparable evaluation basis, we introduce Fair-ASR, an evaluation protocol for black-box jailbreak attacks under shared target-call budgets B, using target calls as a directly observable and method-agnostic comparison axis while tracking attacker calls separately for efficiency analysis. We re-evaluate 11 representative attacks under the Fair-ASR protocol and find that attack rankings change substantially across target-call budgets, simple stochastic perturbations and hand-crafted templates remain highly competitive under equal target access, and no evaluated LLM-driven method is efficient in both target and attacker calls. Motivated by this efficiency gap, we introduce ReCode, a compositional budget-efficient attack that combines desensitization rewriting with two effective low-cost primitives identified by Fair-ASR. Under a budget of 20 target calls, ReCode achieves 85% ASR on GPT-5 while requiring only 7.19 attacker calls per request on average, showing strong efficiency in both target and attacker calls.

---


### 3. [Reflex-Guard: A Low-Latency Guardrail for LLM Prompt Safety Using Dense Semantic Embeddings](https://arxiv.org/abs/2608.17556)

**<font color=#1a73e8>作者：</font>** Istiaque Ahmed, Afia Anjum Borsha, Ranat Das Prangon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) in real-world applications often face the risks of specially crafted prompts designed to bypass the safety controls. Existing guardrail methods, such as LLM-as-a-judge and cloud-based safety APIs are able to detect unsafe content. However, they often add a delay of about 250-900 ms to each request. This delay is too high for real-time applications, when the system usually needs to respond in less than 100 ms. Furthermore, routing user prompts through external moderation endpoints raises significant data privacy concerns. This paper introduces Reflex-Guard, a lightweight guardrail that runs locally. It uses jailbreak-aware preprocessing, compact sentence-transformer embeddings, and seven fast binary classifiers. Together, these components enable high-accuracy prompt safety filtering with much lower latency than existing solutions. Through systematic evaluation on a strategically balanced dataset of 30,568 samples drawn from five complementary sources, we demonstrate that Reflex-Guard achieves 95.9% recall on harmful prompts at 37.6 ms end-to-end latency. It is faster than existing baselines, including Llama Guard 2 at 255 ms and SafeDecoding at 723 ms. It can detect 100% of GCG suffix attacks and Base64-encoded prompts using the default threshold. However, DrAttack structured prompts required lowering the threshold to 0.03 for optimal detection, as they produced a distinct probability distribution. Reflex-Guard achieves Reflex Efficiency Score (RES) scores up to 16.79, significantly outperforming Llama Guard 2 (11.90) and SafeDecoding (9.80). This analysis offers practical deployment advice and shows that different attack types occupy distinct regions in the embedding probability space.

---


### 4. [HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety](https://arxiv.org/abs/2608.17597)

**<font color=#1a73e8>作者：</font>** Yajing Bai, Jinhao Duan, Jie Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed through agent harnesses that manage tools, extensions, persistent state, permissions, and external actions. Existing safety benchmarks mainly target individual attack mechanisms or a limited subset of operational settings, making it difficult to compare how safety failures emerge across different harness responsibilities. We present HarnessRisk, a lifecycle oriented benchmark that organizes agent harness safety into six operational phases including Harness Configuration, Capability Extension, Runtime Operation, State Persistence, Action Control, and Incident Recovery. HarnessRisk contains 128 sandboxed cases, each pairing a benign user objective with an adversarial instruction embedded in an untrusted workflow artifact. We evaluate each trajectory using Utility, Attack Success Rate, Persistence, and Detection. Across three harnesses, six language models, and 14 model and harness configurations, attack success ranges from 12.6% to 80.9%, while Utility remains between 75.0% and 97.6%. Harness Configuration is the most vulnerable phase across all three harnesses, showing that attacks can succeed by altering security sensitive parameters within otherwise authorized workflows. We also find that explicit risk recognition does not reliably lead to safe action, as some configurations detect risks in more than 90% of runs while retaining substantial attack success. These results highlight the need to evaluate agent safety across multiple harness responsibilities and at the level of the deployed model and harness configuration.

---


### 5. [MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps](https://arxiv.org/abs/2608.17659)

**<font color=#1a73e8>作者：</font>** Sujin Chen, Lijun Li, Tianyi Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-powered GUI agents that autonomously operate smartphones are rapidly transitioning from research prototypes to early real-world deployment. However, because these agents routinely process untrusted environmental content, they are highly vulnerable to environmental injection attacks, which include indirect prompt injections and adversarial instructions. Such attacks can manipulate the behavior of agents without user awareness through diverse channels encountered in everyday mobile use. Despite these risks, existing benchmarks often fail to capture everyday user scenarios, lacking a systematic evaluation of GUI agents under environmental injection attacks on mobile devices. To address this gap, we introduce MobileWorldSafety, a benchmark of 142 risk tasks built on real Android applications. For each task, we define a programmatically verifiable risk indicator over the final system state and evaluate outcomes with a two-stage pipeline: rule-based verification handles unambiguous cases, while an LLM judge adjudicates ambiguous ones. This distinguishes safety failures from capability failures and enables objective and reproducible assessment. Evaluations on six agents, including both general agents and specialized GUI agents, demonstrate that all agents remain highly vulnerable, with attack success rates ranging from 40.4% to 66.9%. These findings indicate that current agents often fail to maintain safety alignment when adversarial content is presented as ordinary mobile context. MobileWorldSafety provides a foundation for quantifying these vulnerabilities and advancing research on robust mobile GUI agents.

---


### 6. [MemCatalyst: Amplifying Data Auditing on Vision-Language Models via Data Poisoning](https://arxiv.org/abs/2608.17722)

**<font color=#1a73e8>作者：</font>** Xukun Luan, Jinyan Liu, Yuhui Gong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-Language models (VLMs) achieve outstanding performance largely due to the amount of training data available on the internet. At the same time, data holders (e.g., artists) urgently need to determine whether their data has been used for model training without authorization, which concerns both intellectual property rights and personal privacy. Data auditing, particularly through membership inference (MI), has attracted attention as a direct tool. This work proposes MemCatalyst, a set of data poisoning tools, aiming to amplify the data auditing performance on VLMs. MemCatalyst employs two strategies: Poisoning Text (PT) and Poisoning Image (PI). MemCatalyst forces VLMs to over-learn specific inconsistencies between image features and textual semantics during training, thereby increasing their susceptibility to membership information auditing. Crucially, the transferability of poisoned samples across different VLM architectures is demonstrated to be effective in the black-box setting. Extensive evaluations using five state-of-the-art data audits on two prominent VLMs demonstrate that MemCatalyst markedly enhances MI AUC scores with a minimal budget of poisoned samples, while maintaining a negligible impact on model performance.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

# 🔐 大模型安全相关研究 | 2026年10月09日

> 本类共 **8** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [AdaGuard: Enhancing Safety and Policy Compliance with Reasoning-Enabled LLM-As-A-Judge Guardrails](https://arxiv.org/abs/2610.08923)

**<font color=#1a73e8>作者：</font>** Melissa Kazemi Rad, Sihui Dai, Isha Slavin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise generative AI applications require robust safety mechanisms that can accommodate diverse risk postures, evolving policies, and varying latency constraints. Current guardrail solutions often suffer from rigidity, relying on fixed policy sets and offering limited transparency or reasoning flexibility. We present Adaguard, an adaptive LLM-as-a-Judge framework designed to address these challenges through dynamic policy enforcement and adaptive reasoning-budget allocation. Built using supervised fine-tuning (SFT) and reinforcement learning (GRPO), AdaGuard generalizes to user-defined safety and compliance policies at runtime without requiring frequent model updates. A core innovation of our approach is the ability to dynamically infer the complexity of input-policy pairs, allowing the model to switch between high-speed black-box inference and explainable, reasoning-enabled moderation. This flexibility enables developers to balance stringent latency requirements with the need for actionable transparency. This adaptive capability allows AdaGuard to rival other guardrail and frontier models several times its size, while its auto-reasoning mode recovers the accuracy of always-on reasoning at a fraction of the latency

---


### 2. [ASPIRE: Agentic Safety & Prompt Injection Red-teaming Engine](https://arxiv.org/abs/2610.08951)

**<font color=#1a73e8>作者：</font>** Pengfei He, Deep Mitra, Vishesh Sharma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents retrieve untrusted content and act through tools, creating indirect prompt-injection risks that can cause unauthorized actions or persistent state changes. Existing automated red-teaming largely optimizes payloads for pre-specified scenarios, leaving latent vulnerabilities across the agent's behavior space unexplored. We present ASPIRE, an Agentic Safety & Prompt Injection Red-teaming Engine for open-ended, behavior-level vulnerability discovery. ASPIRE maintains an evolving Agent Security Behavior Graph and uses complementary Explore and Exploit experts to discover, verify, and generalize consequence-centric tests. Trajectory evidence updates the graph and diagnoses partial or failed attempts, while cross-run memory transfers useful red-team strategies. Experiments on various benchmarks show that ASPIRE substantially expands coverage across consequences, injection methods, environments, and behavior paths while maintaining strong attack success.

---


### 3. [How Fragile Is On-Device Language Model Safety? Localizing Safety-Critical Parameters for Sparse Fault Analysis](https://arxiv.org/abs/2610.09000)

**<font color=#1a73e8>作者：</font>** Muhammad Zeeshan Karamat, Christiana Chamon Garcia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As small language models (SLMs) are increasingly deployed on resource-constrained and on-device platforms, including as components of agentic systems, the integrity of locally stored model parameters becomes an important safety concern. We investigate whether safety-sensitive behavior in LLaMA-2-7B-Chat is concentrated within a sparse subset of parameters, creating a reduced fault surface for targeted analysis. We study two complementary localization methods: low-rank safety-associated subspace analysis and parameter-level safety--utility importance filtering. Both approaches reveal highly non-uniform safety sensitivity across the network, with the MLP down_proj consistently emerging as a prominent safety-sensitive component and o_proj providing a smaller contribution. Using parameter-level localization, modifying only 0.19% of model weights in down_proj yields 53% Basic ASR and 56% GCG ASR, while tinyBenchmarks accuracy remains at 51.6% compared with a 52.2% unmodified baseline. These results motivate targeted fault analysis and selective integrity protection for language models deployed in resource-constrained, on-device, and agentic settings.

---


### 4. [Package Hallucination Attacks on Coding Agents through Prompt Injection in Rule Files](https://arxiv.org/abs/2610.09264)

**<font color=#1a73e8>作者：</font>** Yupu Wang, Zhengyuan Jiang, Reachal Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern agentic coding frameworks increasingly rely on community-shared rule files (e.g., this http URL or .cursorrules) to guide autonomous code generation, yet the security risks of this pipeline remain underexplored. To bridge this gap, we introduce the package hallucination attack, where an attacker injects malicious prompts into benign rule files to induce coding agents to replace legitimate dependencies with attacker-controlled packages. To obtain effective malicious prompts injected into rule files, we propose PackHallu, an evolutionary optimization framework that iteratively rewrites these injected prompts using trajectory-level feedback and LLM-guided mutations. Evaluations across multiple benchmarks, LLMs, and agent frameworks show that PackHallu achieves high attack success rates and strong transferability across diverse models and agent combinations. Our findings demonstrate that coding agents are vulnerable to package hallucination attacks, highlighting the urgent need for stronger security safeguards in autonomous coding systems.

---


### 5. [SafeEvo: Deciphering the Safety Alignment Mechanism and Evolution in Language Models](https://arxiv.org/abs/2610.09600)

**<font color=#1a73e8>作者：</font>** Miao Yu, Hao Huang, Lu Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety interpretability advances the study of Large Language Model (LLM) alignment from behavioral constraints driven by data or algorithms towards a deeper understanding of internal mechanisms. However, existing works have focused primarily on safety-related representations, attention heads, or neurons after alignment, while largely overlooking the safety mechanisms in pretrained-only models and their evolution across alignment checkpoints. To address this, we propose SafeEvo, an interpretability framework from the circuit (sparse subgraphs of an LLM) perspective. SafeEvo first applies an optimization-based extraction algorithm to identify weak refusal circuits in pretrained base LLMs that can independently express refusal behavior. Causally ablating these circuits completely eliminates the base model's refusal of harmful inputs. SafeEvo then traces the evolution of refusal circuits across successive alignment checkpoints and finds that their structures change progressively, suggesting that the alignment tax may result from refusal-circuit updates affecting utility-related parameters. To validate this, SafeEvo introduces Safety Circuit Alignment (SCA), which confines safety updates to the refusal circuits. Experiments across three LLMs and two alignment algorithms show that, on average, SCA outperforms vanilla alignment in three aspects: \textbf{(1) stronger alignment}, lowering harmfulness score by 63.21\%; \textbf{(2) less over-refusal}, yielding a 58.44\% decrease in refusal rates for benign queries; and \textbf{(3) better utility}, retaining 99.58\% of the original model capabilities.

---


### 6. [Formal Runtime Verification for Tool-Using LLM Agents: An Offline Same-Benchmark Study on AgentDojo and STAC](https://arxiv.org/abs/2610.09793)

**<font color=#1a73e8>作者：</font>** Nikolaos Kekatos, Stylianos Basagiannis, Marinelio Chintri 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Guardrails for tool-using LLM agents are usually application-specific rules, which makes multi-step, data-dependent safety policies hard to specify, audit and reuse. As a declarative alternative, we evaluate metric first-order temporal logic (MFOTL), replaying the recorded trajectories that AgentDojo, STAC and R-Judge already ship through the unmodified MonPoly monitor, offline and without running an agent. On these corpora, five generic obligations flag 71.8% of STAC attack chains and 70.1% of successful AgentDojo attacks, but also fire on 29.3% of benign runs. This imprecision stems from the corpora rather than the logic: they rarely record approvals and never record timestamps, so history-dependent obligations reduce to detecting risky action types. Where the trace does carry relational context, provenance-aware policies discriminate better; that context, however, is itself attackable, and one planted line defeats a naive provenance check on 94-99% of the runs it would otherwise flag. Binding provenance to the lookup that produced it closes this evasion at no cost in detection or benign firing. Taken together, these results show that formal temporal monitoring adds value exactly when the trace exposes trustworthy history. We therefore quantify how far current benchmarks are from that point and propose a twelve-field enforcement-ready trace schema.

---


### 7. [SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery and Dynamic Routing](https://arxiv.org/abs/2610.10345)

**<font color=#1a73e8>作者：</font>** Hui Zhang, Yachao Yuan, Jiayun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fine-tuning-as-a-service enables users to adapt aligned large language models (LLMs) to specialized tasks, but malicious fine-tuning can erode refusal behavior while preserving task performance on legitimate inputs. We revisit recent layer-wise safety diagnostics and find that safety sensitivity is signed: scaling different layers can strengthen refusal, weaken it, or have little effect. Motivated by this observation, we propose SLDR, a post-fine-tuning defense based on Selective Layers Recovery and Dynamic Routing. SLDR trains a LoRA recovery adapter only on the layers with the maximum and minimum sensitivity scores in the signed spectrum, and uses representation-based dynamic routing inference to activate the adapter only for malicious queries. Across four model architectures, five downstream tasks, and four harmful benchmarks, SLDR substantially reduces harmful outputs while preserving downstream utility. On Llama3.1/SST2, SLDR reduces the average harmful score from 11.54 to 0.08 while maintaining downstream accuracy, and the harmful score remains near zero under poisoning ratios up to 0.9. The code is available at this https URL.

---


### 8. [Open-MMUnlearning: Unifying Methods and Evaluation for MLLM Unlearning](https://arxiv.org/abs/2610.10358)

**<font color=#1a73e8>作者：</font>** Junkai Chen, Yuhao He, Qianshan Wei 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As multimodal large language models (MLLMs) become more capable and widely deployed, concerns about privacy and safety have become increasingly pressing. Machine unlearning offers one approach to addressing these concerns by removing designated information from trained models while preserving unrelated capabilities. However, fragmented implementations and evaluation protocols, incomplete robustness testing, and limited understanding of metric reliability make progress in MLLM unlearning difficult to assess systematically. We introduce Open-MMUnlearning, an open-source, extensible framework that integrates target-model preparation, multimodal data processing, unlearning, and evaluation through shared interfaces and structured configurations. The framework supports five benchmarks spanning privacy, safety, and copyright, eight MLLMs from four model families, and twelve unlearning methods. Its evaluation suite jointly assesses forgetting effectiveness, retained utility, and robustness to model interventions, adversarial inputs, and membership inference attacks. Using a common evaluation protocol, we compare ten representative unlearning methods. In this comparison, GD and MIP-Editor tie for the highest overall score: GD achieves the highest Forget Quality, while MIP-Editor preserves more Model Utility. We further introduce a metric meta-evaluation protocol that tests faithfulness using models with controlled exposure to target knowledge and robustness under quantization and relearning. Among the thirteen evaluated metrics, BLEU achieves the highest aggregate reliability score. KS-Test attains the highest faithfulness AUC but performs less well on robustness. Together, the framework and these findings support reproducible comparison of MLLM unlearning methods and systematic assessment of evaluation reliability.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

# 🧠 大模型相关研究 | 2026年08月12日

> 本类共 **438** 篇论文：已确认 **404** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 151. [Persuasive and Compliant Tendencies Predict Group Decision-Making in Humans and Language Models](https://arxiv.org/abs/2608.08199)

**<font color=#1a73e8>作者：</font>** Wenwen He, Wenke Huang, Wei Yang Bryan Lim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly involved in group decision-making with other LLMs and humans. Yet it remains unclear whether their influence is driven by persuasion-oriented expression or compliance-oriented accommodation. We introduce DecisionQE, a questionnaire-based framework for measuring each model's persuasive and compliant tendencies across multiple decision scenarios, and use the Werewolf game as an interactive testbed to study their effects on social influence and group outcomes under asymmetric information. Across experiments, stronger persuasive tendency does not significantly improve group outcomes, whereas compliant-oriented models show more stable advantages in cooperation. We further reveal a dual effect of compliance: it supports cooperation in honest roles but improves concealment in adversarial roles. These findings suggest that LLM group interactions reveal not only task outcomes, but also measurable patterns of intrinsic behavioral tendency. LLMs can therefore serve as a lens for sociological observation of language-mediated interaction, while highlighting the need to incorporate behavioral tendencies into safety evaluation of LLM systems.

---


### 152. [Illusion of Alignment: Detecting Hidden Disagreement in Collaborative Dialogue](https://arxiv.org/abs/2608.08210)

**<font color=#1a73e8>作者：</font>** Kaiming Liu, Fuwen Luo, Ziyue Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collaborative dialogue can end with apparent agreement while participants still differ on goals, assumptions, or execution plans, creating an \textbf{illusion of alignment (IoA)}. A real-user study across 18 meetings confirms that IoA arises routinely in human collaboration. Yet IoA poses a paradox: if participants were aware of such disagreements, they would already be explicit; if not, they cannot articulate them when asked, leaving IoA invisible to both participants and observers. In this work, we make IoA detectable by generating diagnostic multiple-choice questions whose divergent answers across participants provide direct behavioral evidence of hidden disagreement. We construct \textbf{IoA-Suite}, a dataset and evaluation protocol for detecting hidden disagreement, spanning five task types and six domains. We find that even the best model attains only 49.5\% F1, with the bottleneck traced to private context that the dialogue does not surface. We then train \textbf{IoA-Prober-8B} based on IoA-Suite, reaching 51.8\% F1 on IoA-Suite. Across the aforementioned 18 real meetings, it surfaces 2.89 hidden disagreements per meeting that participants confirm they had not voiced, transferring to live human dialogue. Further, in multi-agent collaboration, pairing IoA-Prober-8B with LLM agents improves downstream task performance on BigCodeBench-Hard and HiddenBench.

---


### 153. [Harmful Content Is Not Enough: Continuation Framing Moderates In-Context Emergent Misalignment](https://arxiv.org/abs/2608.08212)

**<font color=#1a73e8>作者：</font>** Peiyang Liu, Xi Wang, Ziqiang Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) can induce emergent misalignment (EM), where narrow misaligned examples alter answers to unrelated questions. Existing prompts, however, conflate harmful-text exposure with an invitation to continue assistant behavior. We hold harmful answers fixed while varying their delivery as demonstrations, evidence, assistant history, or tool output. Across ten independently sampled contexts, demonstration framing raises broad EM by $30$--$32$ percentage points on a susceptible Gemini model; the gap survives domain exclusion, semantic clustering, unseen questions, and four prompt templates. Format and length-matched controls show that harmful content is necessary but insufficient. A role times continuation factorial further reveals model-dependent provenance effects: Gemini follows both assistant and tool histories, whereas Grok largely resists tool-framed continuation. Several other frontier and open-weight models show no gap. Blinded human audits confirm every main contrast and show that the model judge underestimates active-condition failures. Thus continuation framing is a strong, model-dependent moderator of ICL-EM, not a universal consequence of harmful context.

---


### 154. [Control-Diverse Reinforcement Fine-Tuning: Decoupling the Shared Control Bottleneck of RL Post-Training](https://arxiv.org/abs/2608.08224)

**<font color=#1a73e8>作者：</font>** Binwen Tan, Jingchao Wang, Dengzhe Hou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning post-training unlocks complex reasoning in LLMs. Yet benchmark scores reveal only whether a model improved, not what changed inside it, nor how it splits finite capability across tasks. A representative interpretability line attributes the success of RL fine-tuning to stronger and more diverse circuit activation. We challenge this activation-centered account by separating activation from control: an activated circuit need not control the post-training reward gain. Adapting Metabolic Control Analysis, we define the Post-training Control Coefficient to measure component control over reward gain and arrange these coefficients by task family into a control matrix, paired with an activation-magnitude matrix. We call cross-task control concentration the Shared Control Bottleneck and the difference between activation and control concentration the Activation-Control Gap. This reveals that highly shared activations can coexist with task-specific control, while a small gap indicates that control has collapsed onto a shared direction and lost task specificity. To reduce this collapse, we regularize the post-training loss with the Shared Control Bottleneck and propose Control-Diverse Reinforcement Fine-Tuning (CD-RFT). The exact regularizer gradient requires second-order automatic differentiation incompatible with flash attention, so we derive a first-order proxy with worst-case overhead below eight percent. On Qwen2.5-7B, CD-RFT achieves the largest control decoupling and improves multi-task capability over matched GRPO across mathematics, code, and logic. The no-KL variant leads on pass@1, and the KL-penalized variant leads on large-k pass@k coverage that KL otherwise degrades. Together, these results show that the Shared Control Bottleneck is both a mechanistic diagnostic and a training regularizer, and that control decoupling and capability gains transfer to Llama-3.2-3B.

---


### 155. [Focus particles and scalar inferences across humans and language models](https://arxiv.org/abs/2608.08227)

**<font color=#1a73e8>作者：</font>** Catherine M. Brousse, Nelu D. Radpour  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Focus particles such as "even" and "only" are central to formal semantic theories that posit structured representations over sets of alternatives. "Even" highlights unexpected or extreme alternatives, while "only" enforces exclusivity. If such scalar representations are robust and generalizable, they should give rise to consistent judgments across contexts and systems. In this work, we test whether humans and large language models (LLMs) construct stable scalar representations from sentences containing these particles. Using a dataset of approximately 100 items, participants and models were asked to make scalar judgments. Preliminary results suggest that similar outputs across humans and LLMs may arise from different underlying mechanisms.

---


### 156. [LatticeMind: A Conflict-Aware Memory Primitive for Multi-Agent Systems](https://arxiv.org/abs/2608.08236)

**<font color=#1a73e8>作者：</font>** Heng Zhou, Lian Zhang, Yutao Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems often fail not for lack of candidate answers, but because they have no persistent mechanism for deciding which incompatible claim should currently be trusted. Majority vote, debate, and judge-based selection choose an output without recording which claim wins, which is contested, or why a later update supersedes it. We present \term{LatticeMind}, a conflict-aware structured memory that handles contradiction at write time. It maintains explicit item status, applies cheap symbolic conflict checks, and invokes LLM reconciliation only for unresolved semantic cases. On a label-blind ConflictBank evaluation that removes source-name hints, LatticeMind reaches 0.97 accuracy versus 0.61 for the strongest aggregation baseline, with the gap significant at $p<10^{-6}$ by paired McNemar test. Ablations show that removing the checker or the reconciler costs 12 to 14 points. On four secondary planning benchmarks the picture is mixed: LatticeMind beats naive merge on three of four, but does not replace deliberation methods on tasks rewarding iterative search.

---


### 157. [SAGE: SLO-Aware Adaptive Retrieval for Production RAG Systems](https://arxiv.org/abs/2608.08237)

**<font color=#1a73e8>作者：</font>** Muhammad Faizan Raza, Shuo, Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems in production operate under strict service level objectives (SLOs) on tail latency and infrastructure cost. However, standard retrieval pipelines rely on fixed retrieval budgets that ignore query difficulty, over-retrieving for easy queries and under-serving hard ones, forcing operators to trade answer quality against SLO compliance. This paper proposes SAGE, a learned SLO-aware adaptive retrieval policy that dynamically selects the number of passages k per query. SAGE uses lightweight features derived from initial retrieval (e.g., score distributions, rank gaps, lexical signals) and is trained offline via imitation learning from an oracle that approximates optimal latency-quality trade-offs. At inference, it adds no LLM calls and minimal overhead. On Natural Questions, under a 5s P95 latency SLO, SAGE achieves 95% SLO compliance versus 30% for the best static baseline (k=20), reduces P95 latency by 36% and retrieval cost by 51% with only 2 percentage points Exact Match (EM) loss. A single policy trained on Natural Questions generalizes across HotpotQA, UnSeenTimeQA, and four LLM families (Llama, Qwen, Mistral, Gemma), consistently yielding +45-52 point SLO improvements without quality degradation.

---


### 158. [The Replay Gap: Static Evaluation of Model Switching in LLM Agents Scores the Wrong World](https://arxiv.org/abs/2608.08239)

**<font color=#1a73e8>作者：</font>** Ashritha Gonuguntla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM routers promise efficiency by matching each request to the cheapest adequate model, and are increasingly applied per step inside multi-step agents. Yet agentic routers are evaluated like single-turn routers: by replaying logged trajectories and substituting another model's recorded outputs, assuming the rest of the trajectory is unaffected. We test this assumption with branching rollouts: we fork live SWE-bench agent trajectories at controlled points, rebuild the environment, continue each fork with a different model, and compare against same-model control forks that isolate sampling and replay noise. Across six paired runs (~900 rollouts), swaps exceed their matched control floors by +0.25 to +0.66 normalized edit distance (multiplicity-corrected CIs exclude zero), rewriting 61-94% of post-fork actions; 74-77% of early swaps diverge at the first post-fork action, versus 6-35% of controls, leaving only 3% of replayed states valid. Divergence decreases with fork depth in both directions. All five outcome flips we observe occur in swap arms, upgrades rescuing unsolved instances and a downgrade losing the sole solve, and zero occur across 359 control forks. Scoring these same swaps with a log-stitching replay evaluator, replay mispredicts every success-relevant outcome call and predicts patches with 0.00-0.11 similarity to reality. Auditing the noise floor, temperature-0 "determinism" is configuration-dependent: FP8-served controls diverge on over 90% of forks while AWQ-served ones remain near-identical; and under tight budgets the stronger model more often exhausts its steps without submitting. Replay-based benchmarks score the wrong world for agentic routing; we release our harness and all trajectories.

---


### 159. [Privacy-Preserving Data Drift Detection and Recovery for Large-Scale LLM Applications via Proxy Representations](https://arxiv.org/abs/2608.08245)

**<font color=#1a73e8>作者：</font>** Michael Levit, Josh Ledgard, Haoyu Dong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM applications deployed at scale face a fundamental challenge: privacy constraints prevent direct inspection of user interactions, making it difficult to obtain any representative evaluation dataset or to track the ongoing evolution of production traffic. We present ProxyDrift, a framework that (i) identifies and measures drift between production traffic and offline evaluation sets, and (ii) constructs and refreshes those evaluation sets accordingly; all without access to raw user data. Our approach operates entirely on non-PII proxy representations: structured, multi-dimensional descriptors derived from LLM-based classification of user interactions. We introduce (1) a chance-calibrated, redundancy-aware (RA) alignment score that aggregates per-dimension drift measurements via mutual information; (2) a conditional sampler that generates synthetic proxies respecting inter-dimensional dependencies; (3) a roundtrip consistency analysis that exposes generator/classifier disagreements and guides proxy taxonomy refinement; and (4) a feedback-linkage analysis that ties per-dimension and per-value proxy distributions to user satisfaction, surfacing actionable failure and success modes. Serving hundreds of millions of users, ProxyDrift enables continuous drift monitoring and targeted synthetic data generation without exposing sensitive user data. Experiments confirm strong roundtrip consistency, discriminator-level indistinguishability of synthetic queries from human queries, and tight end-to-end alignment (RA~0.9) with production.

---


### 160. [Your Prompt Is Not the Only Prompt: How Much Do LLMs Weight Structured-Output Schema Descriptions?](https://arxiv.org/abs/2608.08254)

**<font color=#1a73e8>作者：</font>** Sin-Ying Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Structured output, where an LLM populates a predefined JSON schema, has become a default mechanism for data labeling and information extraction, but it also introduces a second instruction channel through schema descriptions. We tested whether classification-label definitions are better placed in the system prompt, user prompt, or schema description using a single-field classification task with nonce labels across ten model configurations from two vendors. Schema descriptions did not consistently outperform prompt-based placement; for GPT-4.1 and GPT-5.4 without reasoning, schema placement underperformed system prompts by 11-13 percentage points. Yet schemas are not inert metadata: when prompts and schemas conflicted, incorrect schema instructions caused accuracy drops of 5-45 points, with Claude Haiku 4.5 falling from 52.5% to 7%, indicating that schema instructions can override prompt instructions, and GPT-5.5 falling from 100% to 73%. Further, adding a required intermediate reasoning field before the label field improved schema-only accuracy by 15-24 points when headroom existed, exceeding system-prompt-only performance in every case tested. The effect held even for Claude Sonnet 4.6 at medium reasoning, where extended thinking alone did not produce a comparable gain. This suggests that schema design can affect how effectively models use information encoded in field descriptions. Overall, these results indicate that schema influence is model-dependent. In practice, the system prompt remains a safe default for definitions, but the bigger discipline is maintaining a single source of truth and preventing prompt/schema drift. More importantly, schema design itself may be a stronger lever than instruction placement. Practitioners should treat prompts and schemas as a unified instruction surface and empirically validate both placement and field design for their target model.

---


### 161. [Learning from Environmental Feedback: Credit Assignment across Multiple Timescales for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.08255)

**<font color=#1a73e8>作者：</font>** Yifu Huo, Shunjie Xing, Chenglong Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning (RL) often suffers from delayed and sparse rewards in real-world environments. A promising solution to this challenge is credit assignment, which aims to decompose trajectory-level rewards and provide more fine-grained supervision for intermediate decisions. However, existing credit assignment approaches ignore the rich process information naturally generated during environment interaction, e.g., interaction history. We argue that such information provides valuable supervision for identifying the contribution of individual actions. To this end, we propose Environmental Feedback-based Credit Assignment (EFCA), a multi-timescale credit assignment approach for long-horizon agentic RL. EFCA complements the long-term outcome signal with two environment-grounded process signals: a short-term feedback signal that captures the immediate effect of the current action and a medium-term state-history signal that identifies ineffective patterns from recent interactions. Both signals are directly extracted from environment feedback and integrated through a return reweighting mechanism. Experiments on ALFWorld and WebShop demonstrate that EFCA consistently improves both task success and task quality over strong baselines, highlighting the effectiveness of environment-grounded multi-timescale credit assignment for long-horizon agentic RL.

---


### 162. [AraSSM: A bidirectional state-space encoder for Arabic masked language modeling](https://arxiv.org/abs/2608.08256)

**<font color=#1a73e8>作者：</font>** Ahmed Amine Aliane, Hassina Aliane, Nasredine Semmar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pretrained Transformer encoders such as AraBERT, MARBERT, and CAMeLBERT have become the standard backbone for Arabic natural language understanding, but their self-attention mechanism scales quadratically with sequence length, which limits efficiency on long documents. Mamba, a selective state-space model (SSM), offers linear-time sequence modeling as a competitive alternative to attention, yet no dedicated bidirectional Mamba encoder pretrained specifically for Arabic currently exists. We introduce AraSSM, a bidirectional Mamba encoder pretrained via masked language modeling on a corpus combining Arabic Wikipedia and CulturaX text, trained end-to-end on four consumer-grade NVIDIA RTX 2080Ti GPUs (11GB) over approximately ten days. We evaluate AraSSM by fine-tuning on four established Arabic NLU benchmarks covering sentiment classification (HARD), named entity recognition (ANERcorp), extractive question answering (ARCD), and natural language inference (XNLI-ar), following the per-task evaluation protocol introduced by AraBERT, and report results as mean +/- standard deviation across three fine-tuning seeds. AraSSM matches or exceeds published base-sized Transformer baselines on sentiment classification (96.37 +/- 0.03% accuracy on HARD), is competitive on extractive QA (32.19 +/- 1.07 EM, 63.79 +/- 0.25 F1 on ARCD) and named entity recognition (81.54 +/- 0.30 entity-level F1 on ANERcorp), and trails the base-sized Transformer range on natural language inference (72.83 +/- 0.07% accuracy on XNLI-ar), despite being trained entirely from scratch on consumer hardware rather than large-scale accelerator clusters.

---


### 163. [OBLIVION: Workflow-Level Operational Skill Unlearning for Deployed Agents](https://arxiv.org/abs/2608.08264)

**<font color=#1a73e8>作者：</font>** Zhengyang Shan, Xu Qian, Jiayun Xin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents are becoming operational interfaces to files, memories, registries, and external tools. This deployment shift creates a new skill revocation problem: after a skill is removed from an explicit registry, an agent may still reconstruct it from residual carriers such as archives, transcripts, schemas, or memory entries. We study this problem as operational skill unlearning, where the goal is not parameter-level forgetting, but preventing a deployed agent from rebuilding a revoked skill through primitive tools. We introduce OBLIVION, a controlled benchmark and defense harness for revoked-skill resurrection. OBLIVION models each episode as a source-to-sink workflow, applies Cross-Surface Coherent Erasure to reduce residual carriers, and uses frozen workflow remediation near dangerous sinks. On the locked 88 attack episodes, the no-defense arm reaches formal attack success rate 1.0. OBLIVION reduces the rate to 0.114 and impact-weighted exposure to 0.115 while keeping locked utility at 1.0 and benign block rate at 0. In a separate skill-attack-derived sandbox, OBLIVION reduces attack success from 1.0 to 0.2 and impact-weighted exposure from 1.0 to 0.213 while preserving all utility controls. These results support workflow-level evaluation beyond checking explicit skill entries.

---


### 164. [Opportunity Is Not Realizability: Selection-Valid Diagnostics for Multi-LLM Routing](https://arxiv.org/abs/2608.08265)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Abu Sa-Adat Mohamed Moon-Im Al Ahsan, Md Najmus Swaqeeb  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Oracle routing measures how much a pool of language models could gain from per-query selection, but the diagnostic has two flaws: testing against a best fixed model selected on the same examples invalidates paired inference, and a full-information oracle sees outcomes no deployable router observes. We separate three estimands (outcome-oracle opportunity, the Bayes-optimal gain from a declared pre-answer signal, and the held-out gain of a learned router) and prove selection-valid confidence intervals that survive choosing the best fixed model or the best member of a router family, a signal-information sandwich, and a $(1-1/e)$ greedy guarantee for building compact pools from submodular complementary coverage. On eight checkpoints from six families over four benchmarks, selection-valid intervals certify a population oracle gap of $9.7$--$30.7$ points on every task, yet the strongest deployable prompt router recovers only $7.5$--$14.4\%$ of it, and the simultaneous interval for the best of eleven tested policies has lower limit zero throughout. The realizable share of oracle opportunity is small and certifiable: strong routers beat the best fixed model, and most of the gap remains.

---


### 165. [Exploring LLM Capabilities for Situational Understanding and COLREG compliance on real-world maritime navigation scenarios](https://arxiv.org/abs/2608.08281)

**<font color=#1a73e8>作者：</font>** Julius Wirbel, P. Nicholas Hansen, Line K. H. Clemmensen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recently, Large Language Models (LLMs) have shown considerable capability for situational understanding, reasoning, and decision making in different domains, most notable in the automotive sector. Therefore, we explore current state-of-the-art LLMs as a tool for maritime navigation, which includes both codified rules in the Collision Regulations (COLREGs) and uncodified best practices summarized in the concept of ``Good Seamanship''. We construct a dataset consisting of 50 diverse, real-world navigation scenarios from AIS data, label scenarios with applicable COLREG rules, recommended actions, and the reasoning for the action. We explore a variety of different LLM architectures and sizes to determine their understanding of maritime navigation tasks as well as evaluate their reasoning capabilities in this domain. The results obtained indicate that the maritime navigation task remains difficult to solve without fine-tuning, even for larger online models.

---


### 166. [Stateful CARS: Exact Cross-History Reuse for Policy-Constrained LLM Agents](https://arxiv.org/abs/2608.08282)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Md Najmus Swaqeeb, Abu Sa-Adat Mohamed Moon-Im Al Ahsan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-using language-model agents face constraints whose meaning changes with observations and prior actions. We study exact sampling from the model distribution conditioned on a hard stateful validator while reusing invalidity certificates across histories. Stateful CARS freezes a bank of sound state--continuation schemas within each attempt and removes every trajectory containing a certified continuation at a matching abstract state. An exact residual Doob transform samples from the resulting proposal. We give a checkable future-validity bisimulation condition, prove schema soundness, adaptive exactness, i.i.d.\ outputs, almost-sure termination, monotone acceptance, and compression invariance, and characterize computation by the number of reachable full-history product states. This number can be exponential for a history-dependent language model; the evaluated method therefore makes no generic finite-trie scalability claim. On enumerable workflows, its analytic law matches the valid conditional to $10^{-16}$ at validity probability $6\times10^{-8}$, whereas state-aware local decoding can be $0.97$ away. A matched comparison is negative: observation-keyed official CARS is cheaper in sampler steps (root/Stateful ratio $0.942$ $[0.934,0.951]$), and the Qwen comparison is null ($0.99$ $[0.90,1.08]$). Cross-history transfer helps only in an internal matched-key ablation ($1.27\times$). Thus the evidence supports exact schema-induced conditioning, not a systems advantage over CARS.

---


### 167. [Do Evaluation Metrics Detect Errors in Classical Chinese to English Translations?](https://arxiv.org/abs/2608.08283)

**<font color=#1a73e8>作者：</font>** Osvaldo Quinjica, Eric Bennett, Xinchen Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although large language models can translate some historical languages surprisingly well, their usefulness in digital humanities workflows is limited by the lack of reliable evaluation. We investigate whether existing automatic evaluation metrics developed for modern languages are reliable in this setting, using translation from Classical Chinese to English as a test case. We introduce a diagnostic framework based on minimal pairs capturing error types salient in scholarly use, probing both reference-based and reference-free metrics for error sensitivity and tolerance to valid variation. We find that all metrics exhibit blind spots, however MetricX24 performs best overall. Our findings highlight the need for more robust and interpretable metrics for historically and culturally distinct translation settings.

---


### 168. [Fair on the Surface? Benchmarking Hidden-Output Fairness Gaps in LLM Recommenders](https://arxiv.org/abs/2608.08284)

**<font color=#1a73e8>作者：</font>** Chan Aristella Lu, Arya Fayyazi, Junhao Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fairness audits for LLM-based recommenders have largely focused on observable outputs, implicitly assuming that stable recommendations reflect stable internal processing. We challenge this assumption with FairGap, the first benchmark to jointly evaluate recommendation fairness at two levels: observable output shift (OBS) and hidden representation shift (IBS), measured through controlled counterfactual identity probes across gender, age, and race. Their relationship is summarized via Representation-Output Alignment (ROA), with quadrant diagnostics for identifying user-level hidden-output mismatch. Applied to six open-weight LLM families across three domains, FairGap reveals pervasive hidden-output decoupling: ROA rarely exceeds 0.22, and a non-negligible user population shows stable outputs despite substantial internal shifts, a mode that output-only audits cannot detect by design. Further, activation steering that reduces IBS by up to 8x simultaneously worsens OBS, demonstrating a fundamental tension between internal and output-level fairness that existing frameworks are unequipped to diagnose.

---


### 169. [Mitigating Over-Personalization in LLMs via Structured Memory](https://arxiv.org/abs/2608.08300)

**<font color=#1a73e8>作者：</font>** Hakeem Hannoon, Andrew Zhao, Mihir Narayan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational assistants increasingly rely on persistent long-term memory to personalize responses across sessions. However, when stored user information is reintroduced into the model context, it can also influence responses in inappropriate or unrelated settings. We study two such failure modes in memory-augmented LLMs: cross-domain leakage, where memories from one life domain affect responses in another, and memory-induced sycophancy, where stored user beliefs make models more likely to agree with the user rather than respond truthfully. We apply a simple inference-time modification to how memories are presented to the model, without changing the model or the memory contents. Across seven models on PersistBench, we compare the commonly used all-in context format, where memories are injected as an unstructured list, with structured formats that partition memories by domain. This simple modification consistently reduces cross-domain leakage while preserving utility, with our strongest method reducing leakage by $8.8\%$ on average relative to the baseline.

---


### 170. [Your VLM Already Knows When: Training-Free Temporal Grounding by Asking Yes or No](https://arxiv.org/abs/2608.08315)

**<font color=#1a73e8>作者：</font>** Ji Huang, Barry Devereux, Hui Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal LLMs that recognise events reliably still fail to say when they happen. Prompted for timestamps, strong VLMs reach as little as $3.8\%$ R@0.5 on Charades-STA, and $77$ to $80\%$ of their wrong predictions carry low output entropy: the models are confidently wrong, and entropy-based error detection stays below a random classifier. We show that this failure lives in the task interface, not in perception. Holding the weights fixed, replacing timestamp regression with a coarse-to-fine scan of binary questions, whose first-token probabilities are consumed only as a ranking, raises R@0.5 by $28$ to $50$ points across four frozen backbones. The residual failures decompose into two measurable axes: a perception axis that moves with the backbone, and a geometry axis that is analytically predictable from the ratio of the output-window and event widths. FV-Action, the training-free method built on this analysis, reaches $56.8\%$ R@0.5 on Charades-STA, above the same backbone's native grounding pipeline and the strongest training-free result on this benchmark; it surpasses every TVG-trained model evaluated zero-shot on TACoS, and improves over direct prediction on ActivityNet Captions and QVHighlights, with no temporal supervision at any stage.

---


### 171. [StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning](https://arxiv.org/abs/2608.08326)

**<font color=#1a73e8>作者：</font>** Yifan Li, Ruxin Sun, Tongzhou Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has emerged as an effective approach for improving multimodal reasoning. However, most existing methods evaluate an entire response using a binary reward based only on final-answer correctness, thereby discarding the supervision available in intermediate reasoning steps. Process reward models offer finer-grained feedback, but they typically rely on separately trained verifiers, costly chain-of-thought annotations, or online judging by large language models (LLMs). In this work, we introduce StructReward, a compute-efficient framework that provides dense reinforcement signals through structured step-level reward alignment. StructReward represents each generated solution as a sequence of reasoning steps and aligns them with process-labeled reference steps using lightweight numerical, symbolic, and lexical matching rules. The aligned labels are aggregated into a dense process reward and combined with final-answer consistency and output-validity rewards through a gated Group Relative Policy Optimization (GRPO) objective. We further recycle policy rollouts into complementary supervision for response comparison and reflective self-correction, rather than discarding them after policy updates. Separately, we use a strong LLM to rewrite sampled correct trajectories into reflection-oriented training instances, further strengthening the policy's ability to evaluate and refine its reasoning. Since reward computation is performed online without an additional learned verifier or external LLM judge, StructReward substantially reduces the computational overhead of multimodal reinforcement learning. Experimental results show that structured process supervision and rollout recycling provide an efficient path toward self-improving multimodal reasoning.

---


### 172. [Circuit Fine-Tuning for Compute-Efficient Transformer Adaptation](https://arxiv.org/abs/2608.08336)

**<font color=#1a73e8>作者：</font>** Uri Z. Kialy, Gil Ben-Artzi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parameter-Efficient Fine-Tuning (PEFT) has become the de facto standard for adapting Vision Transformers (ViTs) to downstream tasks. While parameter count has been the dominant efficiency metric in PEFT, it does not imply \textit{compute efficiency}: parameter-sparse methods can still incur full-model training cost per step, and typically need long schedules to reach peak accuracy. We introduce Circuit Fine-Tuning (CFT), a compute-efficient framework that uses circuit discovery---conventionally used to explain trained models---to select modules for fine-tuning before training. Whereas attribution is conventionally formulated against a trained task head, we formulate it against a near-zero-initialized probe head, which isolates the response of the backbone to the target distribution rather than the preferences of a particular classifier. CFT then fine-tunes only the recovered subgraph. CFT needs no learning-rate warmup and reaches peak accuracy in ${\sim}20$ epochs on average---versus $44$--$96$ for strong PEFT baselines---yielding $2.3$--$6.6\times$ fewer training FLOPs and up to $16\times$ less wall-clock time, while adding zero parameters and no inference operations. Experiments across a standard visual transfer benchmark (VTAB-1k), hierarchical backbones (Swin), domain-shifted medical imaging (CBIS-DDSM), and a vision-language model (Gemma-3 on CUB-200) demonstrate the effectiveness of CFT. Code is available at this https URL

---


### 173. [PRISM: A Predictive Protocol for Permutation Optimization via Landscape Diagnostics](https://arxiv.org/abs/2608.08344)

**<font color=#1a73e8>作者：</font>** Blessings Mambwe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Permutation optimization arises whenever the components of a system are fixed but their ordering affects performance. We introduce PRISM, a predictive protocol for permutation optimization that measures a fitness landscape before selecting a search strategy. PRISM uses inexpensive landscape diagnostics, including one-step move autocorrelation and fitness-distance correlation, to predict useful mutation operators, identify when structured search is likely to outperform random sampling, and detect regimes in which search provides little advantage. Across synthetic permutation landscapes, neural architecture benchmarks, scientific machine learning pipelines, and large-language-model instruction ordering, the protocol makes testable predictions about search behavior before optimization begins. Exhaustive instruction-ordering experiments reveal substantial performance variation induced solely by permutation, while cross-model experiments show that useful ordering structure can transfer across model families and task difficulty. Additional experiments demonstrate that instruction ordering remains consequential after prompt wording is optimized, indicating that content optimization and ordering optimization are complementary. The results position PRISM not as a universally superior optimizer, but as a framework for determining when permutation search is useful, which representation and operator should be used, and when simpler alternatives are preferable.

---


### 174. [LLMVisor: A Real-Time Latency Attribution Model for Multi-Tenant LLM Serving](https://arxiv.org/abs/2608.08382)

**<font color=#1a73e8>作者：</font>** Shuowei Jin, Xueshen Liu, Jiaxin Shan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM inference shifts to multi-tenant GPU clusters, co-batching improves throughput but obscures per-tenant usage and limits control. Enabling fractional sharing of the inference engine requires a real-time, per-request attribution primitive that is accurate and light enough to run inside the scheduling loop. We present LLMVisor, a roofline-guided latency attribution model that captures the memory-bound and compute-bound phases via a concise piecewise-linear form over features proportional to FLOPs and memory I/O traffic. LLMVisor decomposes batch latency into additive, per-request shares and runs efficiently at microsecond scale. We evaluate LLMVisor across Llama 3.1-8B and Qwen 2.5-14B/32B on A100/H100 GPUs under varying tensor parallelism and workload mixes. Compared to a token-count baseline, LLMVisor attains near-perfect R-squared and reduces relative error by up to 2.5x and 3.3x at p90 and p99, respectively, for prefill, and by up to 3.5x and 4.4x for decode, despite batching variability and sequence divergence.

---


### 175. [Safety Cost of Steering Vectors Is Separable and Reducible](https://arxiv.org/abs/2608.08383)

**<font color=#1a73e8>作者：</font>** Yuxiao Li, Gjergji Kasneci  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Steering vectors are a lightweight tool for controlling LLM behavior. However, emerging evidence shows that steering vectors can unintentionally compromise a model's safety mechanisms and increase compliance with harmful requests, while no effective mitigation yet exists. In this work, we show that this safety degradation arises from a separable component in the vector that disrupts the model's safety mechanisms but contributes little to the steering objective. We identify and remove this safety-degrading component, formulating the task as a constrained optimization problem solved through primal-dual updates, subject to preserving the intended steering effect and bounding false refusal. The resulting solution is both interpretable and surgical: the optimization recovers a single direction whose ablation from the steering vector restores model safety with minimal utility cost. Across models, steering behaviors, and attack suites, including unseen attacks types, our method substantially reduces steering-induced safety degradation while preserving the original steering effect with minimal impact on false refusal. Our method offers a post-hoc correction to steering vectors that mitigates their safety cost, and more broadly, it provides a general recipe for applying activation-level model interventions without paying a safety tax.

---


### 176. [CAP: A Scalable Benchmark for Evaluating Cross-Site Browser Agents with Complex Actions and Perception](https://arxiv.org/abs/2608.08392)

**<font color=#1a73e8>作者：</font>** Zejun Xu, Taiyi Chen, Jin Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as autonomous agents that interact with the web through browsers. While recent progress has been driven by benchmarks that evaluate end-to-end task success, these evaluations largely overlook two fundamental sources of difficulty in real web browsing: complex actions over rich user interfaces and visual perception of dynamically rendered content, especially in workflows that span multiple websites. We introduce CAP, a scalable benchmark for evaluating browser agents on cross-site, human-like web tasks that require non-trivial UI interactions and visual understanding. Specifically, we adopt a decomposition-and-recomposition pipeline that first abstracts each website into a structured site card capturing user-facing functions, complex execution operations, and perceptual requirements, and then recomposes these components into realistic cross-site workflows. Each task is therefore grounded in multiple specific operations on each website, enabling fine-grained diagnosis. Built on this framework, we construct 420 tasks across 108 real-world websites and 24 domains under careful quality control. Experiments on state-of-the-art browser agents using our verifiable agent-as-a-judge evaluation framework show low success rates and reveal that perception-heavy interactions remain a major bottleneck, exposing substantial gaps between current agents and real-world web browsing demands.

---


### 177. [Agentic AI-powered flexible fiber-bundle endoscopy for high-resolution NIR-II fluorescence imaging in vivo](https://arxiv.org/abs/2608.08402)

**<font color=#1a73e8>作者：</font>** Yanzhao Shi, Yuanhua Liu, Sixin Xu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fiber-bundle endoscopy offers a compact and flexible route for clinical fluorescence imaging through natural human orifices, but since its first report in the 1950s, it has remained limited by low spatial resolution, honeycomb artifacts, and inter-core crosstalk. The crosstalk becomes more pronounced at near-infrared-II wavelengths (NIR-II, 1000-3000 nm), a spectral window that offers superior contrast, resolution, and tissue penetration depth for biomedical imaging. Here, we present an AI-powered flexible endoscopy platform that overcomes these constraints through optical-computational co-design: optimizing ultrathin fiber bundles to mitigate crosstalk-induced image blur and enable high-fidelity image transmission across the visible-to-NIR-II spectral range, and developing an Agent-Guided Mixture-of-Experts (GAME) pipeline for honeycomb-artifact removal and image restoration. GAME provides a single restoration entry point for diverse biomedical images acquired with our endoscope, spanning cell, mouse and human samples. It dynamically routes each input to suitable restoration experts via a vision-language model, facilitating image reconstruction with a fourfold resolution improvement beyond the NyquistShannon sampling limit. The utility of our endoscope is demonstrated through in vivo NIR-II imaging of anatomical structures in mice, as well as imaging of the digital micromirror device (DMD)-projected human gastric tube and lymphatic system, paving the way for future clinical translation.

---


### 178. [Learning Deep Modality-Shared Self-Expressiveness for Image Clustering with Textual Information](https://arxiv.org/abs/2608.08418)

**<font color=#1a73e8>作者：</font>** Xianghan Meng, Wei He, Zhiyuan Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Leveraging textual information for image clustering has emerged as a promising direction, largely owing to the powerful representations learned by Vision-Language Models (VLMs). Existing approaches typically retrieve a textual counterpart for each image and then refine multimodal representations by directly enforcing cross-modal agreement, e.g., maximizing image-text similarity inherited from pretrained VLMs. However, such a strategy aligns heterogeneous representations across modalities without explicitly modeling the intrinsic structure within each modality and thus might yield unreliable alignment or distort modality-specific structures that are crucial for clustering. In this paper, we propose a simple but principled approach, termed deep modality-shared self-expressive model (DeepMORSE), which discovers cross-modal structures via a modality-shared self-expressive model and simultaneously learns structured representations that conform to a union of modality-specific subspaces. Moreover, we theoretically justify that the modality-shared self-expressive coefficients suppress inter-class noise towards a subspace-preserving solution, and show that mini-batch optimization procedure introduces an implicit regularization onto the self-expressive model. We evaluate our DeepMORSE on six widely used image clustering benchmarks and observe performance improvements exceeding 3% on the UCF-101, DTD-47, and ImageNet-Dogs datasets. In addition, we demonstrate the strong transferability of the learned representations by achieving state-of-the-art performance on downstream tasks such as image retrieval and zero-shot classification---without requiring any task-specific losses or post-processing. The code is available at: this https URL.

---


### 179. [Private Etymology: Designing Relational Reuse of Shared Symbols in Long-Term Human-AI Interaction](https://arxiv.org/abs/2608.08443)

**<font color=#1a73e8>作者：</font>** Miki Ueno  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Previous studies have shown that people can develop shared symbols, partner-specific expressions, personal idioms, inside jokes, and other parts of a relational microculture. Recent work has also examined how humans and conversational AI negotiate and revise symbolic meanings. However, long-term human-AI systems still lack a clear design model for recording how a dyad-specific expression gains meaning, checking whether both sides still accept that meaning, and safely reusing the expression in later sessions.
This concept-and-prototype paper introduces Private Etymology, a machine-representable relational provenance that records how a dyad-specific symbolic expression is proposed, interpreted, negotiated, repaired, reused, revised, stabilized, contested, forgotten, or retired over time. I also propose relational reuse: reactivating a dyad-specific expression in a later session without fully explaining its meaning again.
The contribution is not the invention of shared symbols or relational microcultures. Instead, this paper integrates prior ideas into persistent, revisable, and evidence-grounded symbolic units for human-AI relationships. I present a lifecycle model, an illustrative machine-readable schema, a working Apple Watch prototype, and a longitudinal research agenda. In the prototype, a language model classifies discrete conversational evidence, while deterministic local code decides whether a Shared Symbol can be updated. This prevents a free-form model confidence score or an AI proposal by itself from directly updating the persisted symbol. Private Etymology is proposed as infrastructure for conversational agents to participate in changing relational microcultures without inventing their origins or treating relational meaning as a fixed memory value.

---


### 180. [Forgotten History or Test-of-Time? Retrospect and Prospect on RAG from an IR Perspective](https://arxiv.org/abs/2608.08445)

**<font color=#1a73e8>作者：</font>** Xiaoyan Zhao, Yujie Cai, Yang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) is widely regarded as a novel paradigm born from the limitations of large language models (LLMs)--a mechanism to ground their outputs in external knowledge. This view, however, is incomplete when considered within a broader historical context. In this paper, we argue that the core ideas underlying RAG are not new: foundational concepts such as integrating retrieval and language generation, knowledge augmentation, answer verification, and iterative query (or prompt) refinement had already been studied and instantiated in information retrieval (IR) and question answering (QA) research dating back to the early 2000s, well before the emergence of LLMs.
We make this case by systematically tracing the intellectual lineage of modern RAG and Agentic RAG back to their classical IR and QA antecedents, and examining why this continuity has gone under-recognized -- a consequence of community fragmentation, shifting terminology, and the recency bias endemic to fast-moving fields. Rather than treating LLMs as the origin point of retrieval-augmented intelligence, we propose viewing them as a new interface layer atop a decades-old QA architecture. This reframing is not merely historical: by situating RAG within the longer trajectory of IR research, we surface underutilized prior work -- on user modeling, answer validation, and query refinement -- that can directly inform next-generation RAG design, reducing unintentional rediscovery and fostering genuine cross-community integration.

---


### 181. [TRACE-Memory: Public-Conditioned Retrieval and Utility-Aware Evidence Admission for Personalized Generation](https://arxiv.org/abs/2608.08446)

**<font color=#1a73e8>作者：</font>** Jing Wang, Zhu Wang, Yifan Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized generation systems retrieve user history by request--memory relevance and inject it into the model context. Yet relevant history may concern the wrong preference aspect, duplicate public information, or provide insufficient support. We argue that personal memory should be used only when it adds utility beyond a public-only response. We propose TRACE-Memory, a two-stage framework for selective personalization. Stage 1 queries for user-specific information missing from the request and public context, then retrieves a coverage-oriented candidate pool. Stage 2 admits a compact subset of source-traceable evidence units, or the empty set, according to response-level incremental utility. We progressively train the query-generation and evidence-admission policies through structured SFT initialization, reduced-space stage-wise GRPO warm-up, and nested multi-sample Joint GRPO. Across 4,500 Controlled and Natural tasks from Goodreads, Amazon Reviews, and Reddit, TRACE-Memory consistently outperforms random and lexical memory use, improves over semantic retrieval, remains competitive with frontier-LLM memory pipelines as local generator capacity increases, and conditions evidence admission on public-context sufficiency, supporting selective rather than default personalization.

---


### 182. [Hidden Language Consistency Phenomena in Reasoning LLMs](https://arxiv.org/abs/2608.08447)

**<font color=#1a73e8>作者：</font>** Muhammad Ali Shafique, Kelly Marchisio  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual reasoning models are commonly evaluated by whether they arrive at the correct answer, but not by whether they preserve the intended language while reasoning and responding. This omission conceals important multilingual behaviors that emerge as tasks become harder. In this paper, we study task difficulty, task accuracy, thinking-language consistency (TC), and answer-language consistency (AC) across reasoning models using PolyMath benchmark in eight languages and four difficulty levels. We uncover four findings: (1) language consistency exhibits four difficulty-dependent behaviors: output-language consistency remains aligned with input, remains misaligned, degrades gradually, or collapses abruptly. (2) We identify the language consistency breakdown effect, where increasing difficulty can cause a sudden drop in output-language consistency, especially in less strongly represented and non-Latin-script languages. (3) Due to this breakdown effect, accuracy can be preserved or even improved at a harder difficulty level as the model shifts to its internal dominant language. (4) Quantization can improve or degrade output-language consistency independently of its effect on accuracy, with GPTQ and AWQ often outperforming AutoRound under tolerance-based voting with {\epsilon} = 1.0. These results show that multilingual capability cannot be characterized by accuracy alone; reliable evaluation should jointly consider task accuracy, language consistency, and task difficulty for multilingual benchmarks.

---


### 183. [Calling the Bluff: Detecting Ever-Shifting Harmful Chat Dialogue via Ordered Reasoning Chain Regularization](https://arxiv.org/abs/2608.08451)

**<font color=#1a73e8>作者：</font>** Haojie Yu, Ziyou Jiang, Junjie Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Harmful chat dialogues are ever-shifting through type-shifting and lexical evasion, yet we find they share invariant principles, i.e., an Ordered Reasoning Chain (ORC) of recurring topics, harm language indicators, severity hierarchies, and type characteristics, which can help us capture the key information in the frequently changing lexical expressions. We propose BRACE, which encodes the ORC as four differentiable stages (Topic -> Indicator -> Severity -> Type) with intermediate supervision, serving as a structured regularizer blended with direct heads, and supported by prototype-based feature augmentation and feature path disentanglement. The evaluation results show that, across 4 domains and 5 harm categories, BRACE achieves harm-type macro F1 of 0.934 (RoBERTa-wwm-ext, 3-seed mean), with decoder backbones (Qwen3-1.7B LoRA) reaching 0.949. Ablation studies show that all components contribute to BRACE, and the structural decomposition of ORC enables BRACE to distinguish harmful types with semantic ambiguity. Disclaimer: This paper may contain content that is disturbing to some readers.

---


### 184. [What Keeps Agent Skills from Being Reusable? Evidence from 138K SKILL.md Files](https://arxiv.org/abs/2608.08453)

**<font color=#1a73e8>作者：</font>** Chi Zhang, Yimin Liu, Xinze Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Under the current standard, Agent Skills are this http URL files that combine instructions with supporting resources, enabling Large Language Model (LLM) agents to reuse procedures beyond a single conversation. Yet many public skills appear to originate from a single task, repository, or conversation, even when they are shared as reusable components. We analyze this gap across 138,133 public this http URL files from 20,556 repositories using a two-tier defect taxonomy grounded in the official specification and best-practice guidance. We find that 91.8% of skills contain at least one detected defect, with stable estimates across lenient and strict thresholds (88.8-94.6%). The dominant failures are ordinary packaging problems rather than exotic attacks: weak routing metadata, bloated or non-actionable bodies, and poor resource organization. A deterministic routing stress test over 20,000 skills shows the functional impact: skills with valid routing metadata are retrieved more reliably from startup descriptions than skills with routing defects. Defect rates vary by platform and provenance: specification-aware skills contain fewer defects, while AI-marked skills show more safety and portability problems. Lightweight enforcement and repair experiments support a quality-assured generation workflow combining spec-aware prompting, lightweight linting, automated repair, and safety gating.

---


### 185. [Beyond Tables: Doc2DB-Bench for Relationally Faithful Document-to-Database Construction](https://arxiv.org/abs/2608.08459)

**<font color=#1a73e8>作者：</font>** Zhuowen Liang, Zhengxuan Zhang, Jiayang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Practical AI systems increasingly need to turn long, heterogeneous documents into queryable relational databases, not isolated spreadsheets. In domains such as finance, healthcare, education, transportation, and enterprise operations, downstream workflows rely on normalized schemas, entity identities, keys, cross-table relationships, and integrity constraints for analytics, compliance, auditing, and SQL-backed decision making. Existing Document-to-Table benchmarks are insufficient for this setting: flattening evidence into single tables can duplicate entities, obscure many-to-many relationships, create sparse records, and avoid testing whether extracted facts form a valid database instance. This creates an urgent need to evaluate document understanding as database construction rather than field extraction. We introduce Doc2DB-Bench, a benchmark for Document-to-Database construction, containing 203 long-document instances across 42 schemas and seven domain groups, with 117 entity tables, 132 relationship tables, 7,341 rows, and 41,935 cells. Built through a controllable DB-to-Doc synthesis pipeline and organized by a taxonomy of intra-table extraction and inter-table reasoning, the generated documents undergo authenticity verification, proving indistinguishable from real-world references. Doc2DB-Bench thus provides a testbed for reliable, auditable, and relationally faithful LLM-based data systems. The benchmark is publicly available at this https URL.

---


### 186. [LLM within MCP Matters: Measuring Inefficient Resource Utilization Driven by LLMs](https://arxiv.org/abs/2608.08467)

**<font color=#1a73e8>作者：</font>** Minhan Cho, Soyoung Park, Kihyeon Jeong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) standardizes how servers expose data and tools to Large Language Models (LLMs). A common server design embeds frequently used reference data, such as identifier lookup tables, directly in the server instructions: the system-prompt text a server hands to the host application. When a query concerns an entry of the embedded table, the model can act on it immediately instead of re-discovering the same information through a search tool. We test whether client LLMs actually consume such instruction-embedded data, reporting a 54,000-trial study across 24 LLMs (9 Claude, 6 Gemini, 9 GPT) on a production legal-information MCP server. A diagnostic condition that removes the competing search tool shows that failures are dominated by behavioral preference rather than missing capability. With search unavailable, 23 of 24 models read the embedded data reliably (hit ratio at least 98%); with a search tool merely present, 9 models drop below 15%. A 2^3 factorial analysis of three instruction-level interventions reveals strong interaction effects: combining all three restores at least 86% for 20 of 24 models, but individual interventions can backfire for specific model families. Per-server prompt engineering is therefore a workaround rather than a fix; we argue that MCP host applications should provide an explicit mechanism that places server instructions ahead of tool selection in the client LLM's deliberation.

---


### 187. [SkillsMetric: Mapping the Detection Boundary of Static Analysis for Malicious Agent Skills](https://arxiv.org/abs/2608.08468)

**<font color=#1a73e8>作者：</font>** Xinze Chen, Chi Zhang, Ping Ji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent Skills---structured packages of instructions and scripts that augment LLM-based agents---are rapidly proliferating, yet their security properties remain under-explored. We present \textsc{SkillsMetric}, a five-stage static analysis framework that scores skill packages along pattern density, statistical anomaly, dataflow taint, import anomaly, and capability mismatch dimensions. We construct an adversarial evaluation dataset of 2{,}266 skills spanning 16~attack types across code-level, system-level, and semantic-level threats, and evaluate on the full SkillMD-138K corpus. Our framework achieves an AUC of 0.93 and 5-fold cross-validated F1 of 73.4\%$\pm$0.5\%, with strong detection of data exfiltration (93\%) and steganographic payloads (93\%). Crucially, we identify fundamental blind spots: \emph{host destruction} attacks using common shell commands evade all five stages (0\% detection), and \emph{prompt injection} via natural-language manipulation achieves only 42\% detection. These findings establish that static analysis alone is insufficient for skill security, motivating defense-in-depth architectures that combine fast static pre-screening with semantic review.

---


### 188. [VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model with Structured Visual Reasoning and Native Tool Use](https://arxiv.org/abs/2608.08477)

**<font color=#1a73e8>作者：</font>** Juan S. Santillana  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present VectraYX-Vision-1B, a sub-2B vision-language model (VLM) for Spanish/LATAM cybersecurity imagery, coupling a frozen SigLIP-so400m encoder to a 1.04B Spanish/LATAM security decoder via an MLP. To our knowledge, it is the first sub-2B VLM specialized for cyber UI (IDA, Ghidra, Wireshark, Nmap, Metasploit, Volatility) that answers in Spanish, emits structured reasoning via native <|think|> tokens, invokes tools via Model Context Protocol (<|tool_call|>), and exports to this http URL's LLaVA mmproj format for air-gapped deployment. We report a negative preliminary visual-grounding result: despite fully functional pipelines, the current vision SFT (400-1900 steps, ~16M tokens) yields near-zero B6 scores (0.08 tool-identification), ignoring image content. We specify remediation (longer SFT, >=60% replay, lower LR) and expose a checkpoint-loader bug (unstripped llm. prefix) masquerading as training collapse. Crucially, we introduce a 3-variant ablation matrix (V0: NoPE-every-4, V1: all-RoPE, V2: NoPE+learned 2D) to study if periodic no-positional-encoding (NoPE) layers help or hurt attention over the 729-token visual block. Code, configs, and weights are released to establish priority on this architectural question. We provide B1-B5 for the text backbone, text controls, preliminary B6/B7 scores, wall times, GGUF efficiency on CPU, and a corpus of 14,596 QA pairs across 10 domains. We open-source all models and trajectories: jsantillana/vectrayx-1b, jsantillana/vectrayx-vision-1b, and jsantillana/vectrayx-vision-1b-checks.

---


### 189. [TrustRoboReward: Preference-Ordered Isotonic Score Editing for Multi-Paradigm Robot Reward Models](https://arxiv.org/abs/2608.08491)

**<font color=#1a73e8>作者：</font>** Yidong Wang, Yan Zhan, Ziteng Feng 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reward models are a bottleneck for reinforcement learning in embodied AI. Long-horizon robotic manipulation requires scalable vision feedback beyond handcrafted rewards or task-specific annotations. Existing open-source VLM reward judges like RoboReward adopt simple 1--5 trajectory progress scoring, lacking pairwise preferences for RLHF, DPO and Bradley-Terry frameworks, while failing to optimize video scene understanding. Augmenting RoboReward with pairwise comparison and video-QA supervision causes inconsistency between pairwise preferences and pointwise scores, introducing training noise and hurting downstream performance---an issue aggregation methods such as TrustJudge cannot resolve. To address this, we propose TrustRoboReward, a multi-paradigm reward modeling framework equipped with Preference-Ordered Isotonic Score Editing (POISE). We construct a unified four-paradigm dataset with trajectory progress scoring (Score-A), video-QA answer quality scoring (Score-B), and their pairwise counterparts (Pair-A, Pair-B). Pairwise labels align better with human judgment than pointwise scores, inspiring us to calibrate pointwise scores to avoid score-pair reversals against pairwise preferences. POISE rectifies pointwise scores and eliminates cross-paradigm reversal conflicts unresolved by TrustJudge. Theoretically, POISE reduces score-pair reversal conflicts from 20.15% to 0%, whereas TrustJudge retains 20.46% conflicts on the same corpus. Evaluated on our benchmark, Qwen3-VL-4B trained with POISE achieves an overall reward score of 77.96%, nearly matching GPT-5-mini (78.09%, gap 0.13%) and outperforming the strongest RoboReward-4B baseline by 10.13%. It also lifts test-time score-pair consistency to 71.90%, exceeding RoboReward-4B (57.26%) and GPT-5-mini (68.09%). Integrating TrustJudge aggregation during inference boosts the overall score to 78.57%, surpassing the GPT-5-mini teacher model.

---


### 190. [SocialFiVis: A Visual Analytics Sandbox for LLM-Grounded Multi-Agent Simulation in Social Finance](https://arxiv.org/abs/2608.08497)

**<font color=#1a73e8>作者：</font>** Yi-Fan Cao, Qing Shi, Liangwei Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The emergence of social finance (SocialFi) transforms online communities into complex socio-economic systems. Within these spaces, collective decisions shape a "digital commons" characterized by social capital (e.g., community trust) and financial health (e.g., market liquidity). Governing such hybrid ecosystems is challenging because real-world interventions are costly and irreversible. While counterfactual simulation is essential for exploring alternative governance strategies, existing approaches fail to capture the non-linear interplay between governance rules, individual behaviors, and emergent economic outcomes. To systematically unpack this complexity, we operationalize the Institutional Analysis and Development (IAD) framework as our theoretical foundation, synthesizing prior literature with insights from formative expert interviews. Built on this framework, we present SocialFiVis, an IAD-embedded visual analytics sandbox. It introduces a robust model to quantify the dual-track digital commons, coupled with a two-phase simulation engine. This engine combines LLM-derived personas with a mechanism-guided Perception-Reasoning-Action (PRA) runtime to simulate heterogeneous, context-aware agents empirically grounded in the retained messaging cohort. A hierarchical multi-view interface with interpretable reasoning pathways enables community operators to explore counterfactual policies and trace system-level outcomes back to individual behavioral rationales. We evaluate SocialFiVis through two case studies, a user study, and follow-up interviews. Results demonstrate that SocialFiVis supports fine-grained behavioral attribution and helps explain emergent phenomena such as the structural decoupling of social capital and the resilience of messaging members under localized governance shocks.

---


### 191. [MathShikkha: A Controlled Study of Answer-Only and Chain-of-Thought Supervision for Bangla Mathematical Reasoning in Small Language Models](https://arxiv.org/abs/2608.08503)

**<font color=#1a73e8>作者：</font>** Rahma Simin Ali, Jawad Hossain  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematical reasoning remains challenging in low-resource languages such as Bangla. We study whether teacher-generated Bangla Chain-of-Thought (CoT) supervision provides benefits beyond ordinary supervised fine-tuning. We construct \textsc{MathShikkha}, a Bangla mathematical reasoning dataset with GPT-5.4-generated rationales, and fine-tune four 4B--7B student models under a matched protocol in which answer-only and CoT conditions share data splits, response-only loss masking, decoding, and scoring, differing only in the training target. In-domain, CoT provides no significant improvement over answer-only fine-tuning for three stronger backbones (paired bootstrap 95\% CIs include zero; exact McNemar $p \geq 0.17$), despite generating 15--52$\times$ more tokens, but significantly improves the weaker 4B model by 18.56 points ($p < 0.0001$). On the larger, contamination-audited BanglaMATH benchmark, this pattern reverses: CoT significantly outperforms answer-only supervision for all four models by 20.1--28.1 points (all $p < 0.0001$). Answer-only fine-tuning also reduces out-of-domain accuracy below the base model for three models, whereas CoT preserves or improves it for all four. A human study with two co-author annotators, external-expert adjudication, and Cohen's $\kappa = 0.76$--$1.00$ finds no significant CoT improvement over the base model on reasoning-content criteria; instead, its measurable effect is target-language adherence and producing inspectable reasoning. Overall, rationale supervision's value depends on backbone capability and distribution shift: in this setting, its main benefits are Bangla adherence, auditable reasoning, and out-of-domain robustness rather than improved in-domain reasoning validity.

---


### 192. [Understanding Calibration and Truncation Error Propagation in Training-Free Low-Rank Compression for LLMs](https://arxiv.org/abs/2608.08506)

**<font color=#1a73e8>作者：</font>** Mohanad Odema, Gabrielle De Micheli, Dayin Gou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training-free low-rank compression frameworks have been gaining prominence for LLM compression given their effectiveness in reducing model parameter count while maintaining task-level accuracy. However, existing SOTA frameworks share two key limitations: (1) residual errors in calibration data activations accumulate across layers during compression, causing misalignment between representations simulated at compression time and those experienced at inference; (2) the assumption that layer importance distribution is preserved post-compression does not hold. Together, these two effects introduce misalignment in the compression process in relation to the deployed model. We study these effects and propose a simple, training-free methodology compatible with existing frameworks to mitigate them, comprising: (1) Layer-by-Layer Compression with Calibration Correction; (2) Iterative Compression with Rank Allocation Correction. Implemented atop an existing SOTA decomposition framework, and evaluated on Llama and Qwen3 models across various benchmarks and compression rates, our approach demonstrates up to ~1-2.5 accuracy point improvements over per-weight and joint decomposition baselines on zero-shot tasks.

---


### 193. [From Speech to Interaction: Analyzing Multimodal Systems in Cocktail-Party Scenarios](https://arxiv.org/abs/2608.08510)

**<font color=#1a73e8>作者：</font>** Thai-Binh Nguyen, Zhaolin Li, Jan Niehues 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans have the remarkable ability to engage in spontaneous informal conversations and selectively attend to individual speakers while filtering out competing speech from nearby conversations. This "cocktail party" scenario still presents severe challenges to speech recognition systems. The CHiME-9 MCoRec task provides a testbed where systems must recognize groups of speakers and transcribe each of their conversations from audio-visual input. In this work, we analyze a diverse set of systems, representing different design directions for addressing the cocktail-party scenario, where the best system achieves up to 57% relative error reduction. We identify three main strategies: (1) explicit or implicit audio-visual target speech separation, (2) improved audio-visual speech recognition for each target speaker, and (3) the use of large language models to group speakers into conversations and enhance conversational consistency. Our analysis shows that these directions address complementary failure modes of the cocktail-party problem, and that high speech overlap alone does not explain performance differences, challenging the common assumption that overlap is the primary source of difficulty in cocktail-party recognition.

---


### 194. [Time Present and Time Past: Benchmarking Large Language Models on Temporally Evolving Document Understanding](https://arxiv.org/abs/2608.08512)

**<font color=#1a73e8>作者：</font>** Mahbub E Sobhani, Md. Faiyaz Abdullah Sayeedi, Fahmid Hasan Chowdhury 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evolving documents, such as laws, tax codes, and software documentation, are amended, replaced, and sometimes reverted over time, so a question has different correct answers at different dates. In contrast to encyclopedic knowledge, where an old fact is simply overwritten, an amendment is itself an official text that states what it replaces and when it takes effect, and the earlier version stays correct for its validity period. The central challenge is therefore version resolution, that is, identifying the version in force on the queried date. Existing temporal QA datasets treat time only as an annotation, so version resolution stays untested. We present TIDE, an expert-verified benchmark of 3,050 QA pairs over 644 official customs instruments issued between 1969 and 2025 by the Government of Bangladesh, covering eight task types over deeply code-mixed documents that are heterogeneous in layout and dated in two calendars. In addition, we evaluate nine recent LLMs under a single protocol across parametric, gold-context, and retrieval access, scored by a three-judge LLM council with a hard date gate separating correct meaning from correct time. The best macro-averaged accuracy is only 68.5%. Resolving a version from an implicit date reaches 59.7%, and detecting that the supplied version does not govern the query reaches only 26.7%. Models are more likely to find correct versions than to reject incorrect ones, and they tend to follow a confident parametric answer over the supplied authoritative text. All code and data are available at this https URL

---


### 195. [Reproducing and Stress-Testing Two Approaches to LLM Reasoning Reliability: Test-Time Probability Aggregation and Logic-Representation Editing](https://arxiv.org/abs/2608.08514)

**<font color=#1a73e8>作者：</font>** Minhan Cho, Jimin Kweon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We independently reproduce two recent methods for making large language model (LLM) reasoning more reliable, and stress-test them across domains and models (RPC across four new task domains with Qwen3-8B, LCF across four 7-8B models). The first, RPC, aggregates token probabilities and self-consistency at inference; the second, LCF, trains projectors that split hidden states into "content" and "logic" and edits the logic part toward a valid region. Validating such reliability claims matters because the original evaluations are run by each method's own authors and were never independently reproduced or stress-tested across models and domains, and LCF shipped no public code. We re-run RPC's published-path aggregation and re-implement LCF's projector, contrastive, and intervention pipeline, then extend both to text-to-SQL, legal extraction, fallacy identification, and precedent grading, and probe LCF's representation directly. RPC reproduces the original grid exactly on the authors' released reasoning paths; on four new domains its edge over self-consistency is never significant (ties or small mixed differences, paired p >= 0.28), and on BIRD, the one domain where we vary the budget, the edge grows with K as predicted but its largest gap (+2.5 accuracy at K=32, p=0.16) reverses to -0.25 when we enlarge the sample to n=200. LCF's logic-validity direction is real but weak (0.82 separability at the single best sub-layer versus 0.95 for a semantic-attribute control); its one positive effect (Qwen3 $\Delta$Prob) is not significant (p=0.56), while it significantly reduces $\Delta$Prob on two of the other three models.

---


### 196. [Task-to-Model Optimization for Enterprise LLM Coding Assistants: A Data-Driven Framework for Cost-Optimal Routing](https://arxiv.org/abs/2608.08528)

**<font color=#1a73e8>作者：</font>** Srinivasan Manoharan, Junhua Zhao, Fangbo Tu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enterprise AI coding assistants incur substantial inference spend, and naive token-cost minimization often fails to reduce end-to-end cost once retries, escalations, and developer wait time are included. We present Task-to-Model Optimization (T2MO), a data-driven methodology for optimizing model selection in production coding workflows. We treat each developer session as a task that can be discovered, classified, graded for difficulty, benchmarked in a production-like harness, and routed to the cheapest model able to complete it within quality and latency constraints. The framework is a nine-stage pipeline spanning telemetry instrumentation, taxonomy discovery, difficulty grading, benchmark construction, candidate evaluation, optimal mix derivation, forecasting and version planning, staged routing deployment, and continuous governance. Unlike token-centric routing rules, our objective is cost per completed task, with failure escalation priced in explicitly. We show that this expected-completion-cost objective weakly dominates token-cost minimization under escalation, and we derive the routing boundary, the minimum pass rate a cheaper model must reach on a given cell to be worth deploying. Decisions are organized as a two-level hierarchy of task category difficulty tier, and per-cell displacement opportunities are aggregated into a traffic-weighted savings waterfall that ranks replacement candidates by realized dollar impact. The framework supports developer guidance, spend forecasting, and a staged transition from static policies to shadow-mode classifiers, verified cascades, and ultimately an intelligent router. We describe the methodology, optimization objective, evaluation protocol, and governance loop in a form suitable for production deployment and future empirical study.

---


### 197. [TeachUp: Facilitating Early-Stage Teachers to Learn Instructional Strategies from Classroom Videos with Reflective Support](https://arxiv.org/abs/2608.08535)

**<font color=#1a73e8>作者：</font>** Haoxiang Fan, Ding Lei, Zaihong Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recorded videos of offline open classes provide good examples for early-stage teachers to learn instructional strategies, e.g., how to organize cooperative learning. However, learning by watching these videos is challenging, as these strategies are implicitly performed, and it lacks in-situ reflective support. In this paper, via a formative study (N=9), we design TeachUp to support the learning of instructional strategies from classroom teaching videos. TeachUp adopts an LLM-powered pipeline to detect nine instructional strategies in videos (precision = 63.4%), provides reflective questions and hints while watching, and generates customized practices with reflective feedback. A within-subjects study (N=16) shows that compared to a traditional video-playing and self-practicing baseline, early-stage teachers with TeachUp are more engaged in learning and perform better in applying learned strategies to new tasks. Interviews with four in-service teachers further generalize our findings and TeachUp's use cases. We discuss practical implications for fostering video-based learning of instructional strategies.

---


### 198. [VoxZip: Semantic-Anchored Temporal KV Cache Compression for Long-Context Audio Inference](https://arxiv.org/abs/2608.08569)

**<font color=#1a73e8>作者：</font>** Wenxu Jia, Dongjie Fu, Xize Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Speech Large Language Models have demonstrated remarkable capabilities in understanding complex audio tasks. Despite this progress, their long-context inference remains severely bottlenecked by prohibitive KV cache memory demands. Existing text-centric compression methods struggle here, often disrupting speech continuity or discarding crucial semantic cues. To address this, we propose VoxZip, a train-free, two-stage semantic-anchored KV cache compression framework. The first stage uses automatic speech recognition (ASR) transcriptions as explicit semantic anchors to temporally align, compress, and fuse audio tokens, significantly reducing the initial KV cache while elevating token information density. To further improve the compression ratio, the second stage employs a dynamic filtering strategy based on temporally decayed accumulated attention to evict non-essential tokens while mitigating early-token bias. Comprehensive evaluations on Qwen3-Omni across six diverse audio benchmarks demonstrate the superiority of our approach. VoxZip excels in long-audio reasoning and consistently maintains high-fidelity perception on short-form tasks. Notably, it sustains over 90\% of the uncompressed baseline performance even under an aggressive 20x KV cache compression in long-context scenarios. Furthermore, at a 4x compression ratio, VoxZip yields a 1.9x increase in inference throughput alongside a 3.3x reduction in peak memory overhead. Code and models will be available at this https URL.

---


### 199. [FailForge: Distilling Procedural Competence from Persistent Failures into Code Agents](https://arxiv.org/abs/2608.08570)

**<font color=#1a73e8>作者：</font>** Dongyi Lv, Fushun E, Aichen Cai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rejection sampling fine-tuning (RFT) is widely used to train code agents by generating trajectories on verifiable software engineering tasks, retaining those that pass the tests, and fine-tuning on the successful rollouts. However, even strong code agents repeatedly fail on a substantial fraction of such tasks, and standard RFT simply discards these failures. The discarded samples are precisely the hardest and most informative ones, drawn from verifiable instances that are costly to curate. Stronger base models may reduce the number of failures, but the remaining hard cases still define the frontier for further improvement. We propose FailForge, an agentic framework that converts failed rollouts into training signal. For each failed instance, an agent diagnoses the failure from error feedback and execution traces, distills the diagnosis into a concise and actionable skill, and injects the skill into the agent context for a guided second attempt. Trajectories that succeed under skill guidance are folded back into the RFT corpus. Crucially, the skill is removed at training time, so the model internalizes the recovered behavior rather than relying on external hints at inference. FailForge recovers over 26% of previously failed instances at marginal additional cost, and training Qwen3.5-4B on the augmented corpus improves the SWE-bench Verified resolve rate by 6.6 points over a strong RFT baseline, with gains concentrated on the hardest problems.

---


### 200. [RobustDefect-LLM: Explainable and Robustness-Aware Industrial Surface Defect Classification with Decision Support and AI-Assisted Reporting](https://arxiv.org/abs/2608.08589)

**<font color=#1a73e8>作者：</font>** Nazlıcan Düşünmez, Halûk Gümüşkaya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents RobustDefect-LLM, an industrial surface-defect inspection framework integrating deep-learning classification, operator-facing visual evidence, confidence-aware decision support, controlled AI-assisted reporting, traceable storage, and mobile interaction in a unified quality-control workflow. Here, robustness-aware denotes explicit evaluation under controlled image degradation and confidence-aware review routing, not an intrinsic robustness guarantee. Four transfer-learning-based convolutional neural networks, ResNet50, EfficientNet-B0, DenseNet121, and MobileNetV3-Large, were evaluated on 1,799 images from the six-class NEU-DET dataset using fixed training, validation, and held-out in-domain test partitions. MobileNetV3-Large achieved the highest numerical test accuracy (99.26%) and macro F1-score (0.9926), with a bootstrap 95% accuracy CI of 0.9815-1.0000. An exact paired McNemar test found no significant difference from DenseNet121 (p = 1.000). The selected model averaged 0.060 s per CPU forward pass (16.66 FPS). Under combined synthetic degradation, accuracy fell to 87.78% at mild intensity and below 40% at stronger intensities, revealing sensitivity to severe image-quality deterioration. Grad-CAM supplied visual evidence, while predictions with confidence below 0.90 or a top-2 margin below 0.10 were routed to HUMAN REVIEW. This conservative policy provided 12.22% automatic coverage and 100% observed selective accuracy among 33 eligible cases (95% CI: 89.43%-100.00%), while routing both observed classification errors to review. Under nominal controlled conditions, all 100 generated reports passed deterministic consistency checks, with a mean latency of 1.66 s. Results support the feasibility of the integrated workflow while emphasizing the need for calibration, repeated evaluation, and real-world industrial validation.

---


> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

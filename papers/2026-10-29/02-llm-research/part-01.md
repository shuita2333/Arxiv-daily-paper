# 🧠 大模型相关研究 | 2026年10月29日

> 本类共 **226** 篇论文：已确认 **214** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-226](./part-05.md)

---

### 1. [Task-Utility IQA: Rethinking Image Quality Assessment in Embodied Tasks](https://arxiv.org/abs/2610.35905)

**<font color=#1a73e8>作者：</font>** Jirong Zha, Yanwei Liao, Yemin Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image quality assessment (IQA) underpins embodied imaging pipelines by judging whether visual quality satisfies downstream tasks, yet most existing methods learn task-agnostic scores aligned with generic human ratings on static benchmarks. This objective mismatches embodied and interactive settings, where image adequacy depends on task goals, context, and action requirements that shape an agent's decisions. We argue that IQA should shift from score regression to goal-conditioned judgment defined by embodied task utility. To this end, we propose an MLLM-based embodied IQA agent framework that reasons about task requirements, grounds quality evidence, and produces decision-facing assessments. A compact VisDrone evidence study shows that conventional perceptual metrics and generic MLLM-based IQA scores are weak proxies for downstream VLM task success, while a task-conditioned utility score better predicts whether visual input supports the target task. These findings support a task-utility-oriented reframing of IQA for embodied, explainable, and decision-aware visual perception.

---


### 2. [Physiognomy Revisited: How Vision-Language Models Encode Sensitive Attributes Through Image Transformation](https://arxiv.org/abs/2610.35910)

**<font color=#1a73e8>作者：</font>** Soumyajit Datta, Arka Dutta, Ashiqur R. KhudaBukhsh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emergent generative AI technologies, while remarkably beneficial across several tasks and domains, can suffer from unforeseen vulnerabilities and difficult-to-anticipate failure modes. Such failure modes can disparately affect vulnerable communities. This paper investigates two well-known vision language models (VLMs) and inspects how these models encode protected identities while generating images. We show that when VLMs are requested to transform human face images to reflect race identities (e.g., Hispanic, Black, White, or Asian) and sexual orientation (e.g., gay or straight), VLMs often comply with such requests. We demonstrate that compliance (and refusal) is non-deterministic, group-sensitive, and generated images are statistically distinguishable, often accentuating deep-seated stereotypes. We further show that representation biases introduced during image generation can re-emerge in textual reasoning and characterization tasks. Finally, we show that this worrisome finding is not limited to racial identity or sexual orientation, image generation can perpetuate bias around criminality, raising concerning possibilities of AI-assisted profiling.

---


### 3. [ReCoPII: A Relation-Grounded Framework for Building Contextual PII Masking Datasets](https://arxiv.org/abs/2610.35925)

**<font color=#1a73e8>作者：</font>** Taehwan Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training contextual masking systems for personally identifiable information (PII) requires examples distinguishing maskable from preservable mentions of one entity type, but privacy restrictions limit access to real data. Author-based augmentation (SPY) labels mentions unrelated to the author as non-PII, presuming a single data subject and overlooking others. We propose ReCoPII (Relation-grounded Contextual PII masking), a framework that builds such data without this premise: it plans ontology-constrained entity relations, writes insertion sentences with placeholders, reconstructs annotations with code, checks the result with a separate LLM, and derives MASK/KEEP labels from entity relations. On Korean documents from six domains, it yields ReCoPII-Ko, a corpus with relation, privacy, and MASK/KEEP annotations, which we validate. Across 300 pairs, four annotators agree with 88.42% of its sampled KEEP labels, against 26.27% for SPY-style augmentation of the same sources. Classifiers trained on it over-mask less than under that reference on a matched test. Contextual masking fine-tuned jointly with a PII detector removes most over-masking of detection alone within a fixed leakage budget; on human-verified entity records, the four detectors meeting it over-mask at most 5.04% with at most 4.18% leakage. The detector is comparable to XLM-R-large on KDPII with about a quarter of its parameters.

---


### 4. [SCOPE: Source Credibility and Outlet Profiling Engine](https://arxiv.org/abs/2610.35929)

**<font color=#1a73e8>作者：</font>** Ilyas Nagiyev, Miras Baisbay, Daniil Orel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We present SCOPE, a multi-agent system for profiling news media outlets with respect to bias, factuality, and credibility. Given an outlet URL, SCOPE coordinates specialized agents for article acquisition, content analysis, external evidence search, scoring, and report generation. The system follows an MBFC-style methodology while making intermediate evidence and agent outputs inspectable through a structured demonstration interface. On a benchmark of 200 media outlets, SCOPE outperforms LLM-only, article-only, search-only, and media-background-check baselines on most metrics, achieving the lowest bias and factuality MAE, perfect failed-fact-check detection, and the lowest factual error rate. These results suggest that decomposed, evidence-grounded agent workflows can support more transparent and reliable media profiling. Our code is available at this https URL, and a live demonstration at this https URL.

---


### 5. [Who Convinced Whom? Tracing How LLMs Change Their Minds in Multi-Agent Systems](https://arxiv.org/abs/2610.35930)

**<font color=#1a73e8>作者：</font>** Arnesh Batra, Aniket Khandelwal, Jashn Khemani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate (MAD) aims to improve language-model decisions through the exchange of arguments, yet agreement after debate need not reflect independent corroboration. We investigate how peer communication influences individual decisions and collective outcomes through behavioral and internal interventions. We introduce MAD Bench, a 2,400-question benchmark spanning knowledge and reasoning, values and moral judgment, and safety and refusal, and evaluate three open-weight models using a round-matched independent-reflection control. Among answer-changing responses, a forced-choice readout before rationale generation matches the eventual answer more often in debate than in reflection (65.4% versus 22.3% on Qwen3.5-9B). Message ablations reveal model-dependent effects of peer answers and reasoning, while attributing identical text to the receiver rather than another agent substantially changes its influence. For the tested source descriptions, stated track record affects answer preferences more strongly than professional-status cues across all three models. Attention masking produces different changes in decision margins across the three checkpoints. On fully parsed, reference-labelled non-numeric questions, debate yields small estimated accuracy improvements over initial majority voting, while increasing the rate of unanimous wrong answers by 3.1-7.4 percentage points relative to reflection. Longer debates show persistent consensus and greater correlation between agents' correctness than reflection. These findings show that stronger consensus can coexist with more shared errors, motivating evaluations that assess dependence and unanimous errors alongside accuracy.

---


### 6. [Counting the Bandages: On measuring the time that AI saves](https://arxiv.org/abs/2610.35942)

**<font color=#1a73e8>作者：</font>** Solomon Shalom Lijo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> I consider what it means for AI assistance to save time. I contrast a stopwatch view, on which time saved is whatever the clock records, with a ledger view, on which it is a counterfactual that has to be read next to the errors the work lets through, and I argue for the latter. The argument has four parts. I define a model-free pair of quantities, time saved and excess escaped defects, and one decision number built from them: the break-even defect cost. I give a baseline model of checking in which, until the model is good enough not to check, a calibrated worker's escaped-defect rate does not depend on how good the model is; checking time grows with the logarithm of the model's error rate; and over-trust buys minutes on the clock at a larger cost in total minutes. I show what randomized studies can and cannot identify, and I replicate METR's developer study from its public data: the same 246 issues support a slowdown of 19% or 24% depending on the estimand (34% without adjusting for a chance imbalance), and AI helped on somewhere between 3% and 82% of them. Finally, I restate the published record, with stated bounds in place of imported point assumptions. In GDPval's own review-every-output workflow, review time alone caps GPT-5's speedup at 3.6x; the consultants outside the frontier were faster, and more often wrong. Last, I test two of the model's predictions in a small pre-specified experiment on AI reviewers checking AI drafts of the same kind of brief, built from SEC filings made after the models' training data were collected. Told the drafter's true error rate, the reviewer checked more as it rose, but all-or-nothing, switching near where its prompt's costs break even. Told that the drafter erred ten times less often than it did, it checked 7 fewer of 9 figures and let a wrong figure through in 22.5% of briefs instead of none: faster and worse, entirely through reduced effort.

---


### 7. [ResCom: Activation Residual Compensation for Large Language Model Quantization](https://arxiv.org/abs/2610.35955)

**<font color=#1a73e8>作者：</font>** Ning Yang, Bohan Cui, Zhuowen Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-bit weight--activation quantization reduces the memory and computation needed to deploy large language models, but activation rounding can still degrade accuracy after calibration. Reconstruction from rounded inputs cannot distinguish activations within the same quantization bin. We propose ResCom, a low-rank correction that uses the activation rounding residual to compensate for the resulting layer-output error. An output-aware calibration procedure selects residual directions by their contribution to output reconstruction and computes the correction in closed form, without gradient training or updates to the calibrated weights. On Llama-3-8B with 4-bit weights and activations, rank-32 attention corrections reduce WikiText-2 perplexity from 7.708 to 7.147, improve MMLU by 2.89 percentage points, and raise five-shot GSM8K accuracy from 23.96 to 36.16 percent. Evaluations on models from 1B to 70B parameters and on held-out C4 test the method beyond this setting. The evaluated FP32 implementation adds 2.25 percent to 4K prefill time; a separate compact-storage implementation retains a 27.7 percent peak-memory reduction relative to FP16.

---


### 8. [Distributed LLM Inference via Communication-Efficient Speculative Decoding](https://arxiv.org/abs/2610.35957)

**<font color=#1a73e8>作者：</font>** Joohyun Shin, Byeonghyeon Park, Keumseo Ryum 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributed speculative decoding has emerged as a promising approach for device--server collaborative large language model (LLM) inference, but its decoding speedup is often limited by the vocabulary-scale communication overhead. In existing distributed speculative decoding methods, exact rejection sampling requires transmitting full token distributions over the LLM vocabulary between the device and the server, which becomes costly in bandwidth-constrained environments. To address this issue, we propose DISCO, a communication-efficient framework for distributed speculative decoding, that eliminates vocabulary-scale distribution transfer while preserving the exact target distribution. DISCO achieves this by introducing a server-side replica of the draft small language model (SLM), which enables the server to locally obtain the draft-side distribution required for rejection sampling. As a result, DISCO exchanges only drafted token indices and scalar probability values between the device and the server. Experimental results on multiple datasets show that DISCO consistently achieves higher decoding speedup than existing distributed speculative decoding methods, particularly under stringent bandwidth constraints.

---


### 9. [AgentBaton: Efficient Model Collaboration in Agentic Tasks](https://arxiv.org/abs/2610.35959)

**<font color=#1a73e8>作者：</font>** Junlong Li, Jindong Jiang, Yonggan Fu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Solving long-horizon agentic tasks requires language agents to interact with their environments over multiple steps, and reliable performance often comes from the expensive capable models available through cloud providers. Meanwhile, alternative efficient models with inferior performance but a much lower cost are emerging, including lower-tier cloud models and smaller open-weights models deployable on local hardware. This raises a natural question that remains less explored than traditional query-level routing: can capable and efficient models collaborate within a single long-horizon agentic task to substantially reduce cost while preserving task accuracy? In this paper, we systematically investigate key design choices for such collaboration through model handoffs, where one model takes over from another, focusing on handoff direction and context transfer. We find that efficient-to-capable handoffs generally underperform capable-only execution with limited or even no cost reduction, whereas capable-to-efficient handoffs at suitable stages of task progress largely preserve or even improve accuracy while substantially reducing cost. These findings suggest that a one-time, simple, well-timed handoff strategy is good enough for cost-effective agent collaboration, motivating AgentBaton, a lightweight detector that learns when to hand off from recurring patterns in task progress. Across 11 model pairs and two representative benchmarks, AgentBaton reduces API costs by 65.9% on average while largely preserving task accuracy, with accuracy gains of up to 8.8 percentage points over capable-only execution. Experiments across various reasoning-effort settings further show that AgentBaton extends the empirical accuracy-cost Pareto frontier.

---


### 10. [h1: A Taste of the Bitter Lesson in Automated Theorem Proving](https://arxiv.org/abs/2610.35962)

**<font color=#1a73e8>作者：</font>** Skander Moalla, Ahmad Rammal, Niket Patel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While progress in informal mathematics has come largely from scaling the chain-of-thought and agentic reasoning of frontier language models, formal theorem proving has increasingly relied on human-designed workflows around these models, such as planning, decomposition, and orchestrating specialized provers. This raises a bitter-lesson question: can a simple agentic loop that scales test-time compute match these workflows? The answer matters as formal verification must scale to keep up with frontier models producing research mathematics, yet new workflows rarely settle it, as their gains are often confounded with stronger models or more compute. We study this question with h1, a simple harness that gives a model an efficient interface to Lean 4 and keeps it working through verifier feedback and self-reflection, without imposing a decomposition or search structure. h1 reaches state-of-the-art results on PutnamBench, FATE-X, and FormalConjectures100-Solved, settles eight open problems in FormalConjectures, and, at matched models, matches or outperforms specialized workflows such as Goedel-Architect and AlphaProof Nexus, surprisingly showing that a single attempt (pass@1) can often scale to solve open problems. Through ablations and matched-model comparisons with Claude Code and AxProverBase, we find that simplicity alone is not enough: an efficient Lean interface largely determines cost and solve rate. We thus recommend that future work evaluate frontier models with efficient execution feedback before prescribing workflows, at the risk of bitter lessons.

---


### 11. [EMMA: Structured Episodic Memory for Multi-Agent Workflow Synthesis](https://arxiv.org/abs/2610.35966)

**<font color=#1a73e8>作者：</font>** Ruijia Niu, Kaiwen Liu, Rose Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Deploying LLM agents in specialized domains often require fine-grained task-specific procedures and knowledge a general model lacks, yet parameter training is costly and non-interpretable, and hand-engineered agent systems shift the cost to expert labor. Episodic memory updates at context level, but single agent adaptation struggles to alleviate cross-task interference, especially with complex tasks such as multi-application navigation or data pool analysis. Although multi-agent evolution alleviates this problem, existing methods lack clear definitions on update rules and rely on the backbone model to decide where and how much the system changes. This ill-scoped evolution makes learning follow the backbone's structural preferences rather than the observed failures: one backbone accumulates skills while another spawns agents. We present EMMA (structured Episodic Memory for Multi-Agent workflow synthesis), which treats the configuration of a multi-agent system (controller routing memory, specialists inheriting a generalist prompt, and per-step procedural skills) as episodic memory. EMMA makes the ownership and admissibility of updates explicit: a reflector assigns each diagnosed failure to the scope owning its correction and proposes one edit within it, and backbone-independent guards keep every accepted edit scoped, incremental and bounded. Across KramaBench, AppWorld and BBEH with five backbones and four baselines (ACE, GEPA, EvoMAS and ADAS), EMMA attains the best overall performance on every benchmark, up to 32.5% over the strongest baseline, maintains consistent improvements across backbones, and uses 17-38% fewer training executions than the most efficient baseline.

---


### 12. [Let the Gate Decide: Per-Lookup Precision for Quantized Conditional Memory in LLMs](https://arxiv.org/abs/2610.35985)

**<font color=#1a73e8>作者：</font>** Tianqi Chen, Xunchao Li, Linchuan Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional memory layers, such as DeepSeek's Engram, attach large hashed n-gram tables to a language model, and removing them from DeepSeek-V4.1-Flash costs 36.8 PopQA points. Low-bit quantization loses long-tail facts first, and the standard remedy, giving more bits to frequently accessed rows, backfires: refining lookups by access frequency is worse than refining them at random. We trace this to the gate that scales each retrieved row. A lookup's quantization error is weighted by its gate, which is small for frequent n-grams, large for the rare n-grams of long-tail entities, and computable from a 1-bit code. GateRQ therefore stores each row as a ladder of 1-bit residual codes, keeps level 1 in GPU memory to compute the gate, and reads deeper levels only for the lookups the gate ranks highest. Without retraining, GateRQ cuts GPU table memory by 7.8x on DeepSeek-V4.1-Flash, which raises vLLM throughput by 11%-31% over FP8 tables, while losing about 1 PopQA point at 1.50 bits read per lookup and 0.2 points at 2.10 bits across two models.

---


### 13. [PolicyMediator: Multi-Regional Policy Learning through Mediation Agents with Evolving Skills in OPC Ecosystems](https://arxiv.org/abs/2610.35997)

**<font color=#1a73e8>作者：</font>** Jie Li, Bin Guo, Georgina Curto 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> One-person companies (OPCs) are emerging enterprises operated by individual entrepreneurs through digital platforms and LLM-based AI agents. These highly skilled entrepreneurs are characterized by being digital nomads, with limited reliance on local ecosystems. Governments in China use distinct regional support policies to attract mobile OPCs, turning local support into a cross-regional coordination problem. OPCs compare regions to maximize their own utility, but imperfect policy perceptions may cause them to reject otherwise suitable locations. Existing policy-learning methods optimize resources under fixed perceptions, while consensus-formation methods aggregate views without feeding cognitive changes back into policy learning. This disconnect produces mismatched location choices and inefficient regional policy adjustment. We introduce PolicyMediator, a cognition-constrained leader-multi-follower Stackelberg framework with bilateral mediation. The mediator explains verified policies to OPCs to build awareness and trust, and reports their needs and unresolved concerns to governments for policy learning. Its self-evolving skills retain, revise, or prune strategies using verification, allocation, capacity, and objective trajectories rather than mediation success alone. Across six-region simulations in China with five OPC types, five scenarios, and three OPC-simulator backbones, PolicyMediator ranks first in all 15 OPC-backbone--scenario combinations. Over the eight-baseline mean, it improves the aggregate government objective, combining economic performance, employment benefit, and policy-access equality, by 42.4% and average OPC utility by 40.9%.

---


### 14. [MedJev: Evaluating Zero-Shot System-One Decision Making in Medicine](https://arxiv.org/abs/2610.36006)

**<font color=#1a73e8>作者：</font>** Simon A. Lee, Jiahang Sha, Moonseong Jeong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> System One decision models such as Jev answer structured questions in a single forward pass without generating text, offering fast and computationally efficient clinical decision support. We evaluate MedJev, an open System One model that runs locally on a laptop, across ten medical benchmarks spanning medical knowledge, diagnosis, and patient level prediction using MIMIC IV and MIMIC IV ED. We compare MedJev against zero shot LLM baselines, published GPT results, and supervised models. MedJev achieves accuracies of 72.5 percent on MedQA, 75.4 percent on USMLE, and 80.1 percent on NEJM, approaching published GPT 4 performance while maintaining well calibrated confidence estimates (ECE 0.028 to 0.063). On patient level tasks, MedJev achieves an AUROC of 0.926 for In Hospital Mortality, exceeding XGBoost (0.902), but underperforms supervised models on operational outcomes such as ED Triage Admission (0.745 vs. 0.809). Patient level predictions also exhibit substantial miscalibration (In Hospital Mortality ECE 0.286). We introduce a lightweight, two parameter recalibration method that adapts predictions to local patient populations using 50 to 200 labeled examples, reducing ECE to 0.007. Our findings establish open System One models as a promising zero shot baseline for medical AI, combining competitive predictive performance with low computational cost and efficient local calibration. We release our code and evaluation harness to support future research.

---


### 15. [DuplexTune: Coupled-State Replay for Memory-Efficient Mixture-of-Experts Adaptation](https://arxiv.org/abs/2610.36009)

**<font color=#1a73e8>作者：</font>** Paul Raj, Simon Caldwell, Daniel Whitmore 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse expert execution does not remove the stored states needed to adapt a mixture-of-experts language model. We present DuplexTune, a framework for replaying coupled hidden states through pretrained attention and expert modules. Trainable width bridges connect two residual streams to the backbone. Bridge warm-up precedes backbone adaptation, with router weights kept frozen. We analyze the implicit state-recovery equation and identify the convergence and replay conditions needed for reconstruction. On Qwen1.5-MoE-A2.7B, the single-H800 evaluation reports 38.8 GB peak memory, versus 64.8 GB for supervised fine-tuning with checkpointing, and throughput of 25.1 versus 19.9 samples/s. DuplexTune achieves 67.2% MMLU, 75.6% GSM8K, and 7.69 MT-Bench, with a weaker multilingual score than the checkpointed baseline. The results characterize a configuration-dependent tradeoff among state storage, throughput, and adaptation quality.

---


### 16. [How Much Does the Hint Matter? Scope Conditions for Hindsight Self-Distillation in Financial Reasoning](https://arxiv.org/abs/2610.36082)

**<font color=#1a73e8>作者：</font>** Johnny Yu, Cyril Gorlla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial institutions operating under data-residency constraints are restricted to open-weight models small enough to locally host, which trail frontier systems on multi-step quantitative reasoning. On-policy distillation narrows such gaps by supervising a student on its own rollouts, but traditional OPD requires a strong external teacher, and on-policy self-distillation (OPSD) conditions on a full reference solution. We ask how much of that signal is necessary. We present Fin-SD, a localized hindsight self-distillation recipe for multi-step reasoning. Given a problem the student fails, the student itself identifies the first incorrect reasoning step and writes a short critique of that step. We truncate the student's trajectory immediately before the error (aiming to obtain a correct prefix), condition a frozen copy of the student on the same prefix plus the hint, and distill that hint-conditioned teacher into the student over a short rollout under reverse KL. No external model contributes a gradient. We apply Fin-SD to GPT-OSS-20B on a custom multi-step financial reasoning benchmark that requires deriving formula inputs from realistic scenarios via accounting conventions. We find: (i) replacing the critique with a generic-feedback control matches Fin-SD's entire 3.03 pp accuracy gain over the base model on the FinanceReasoning Hard subset, suggesting the gain comes from where supervision is applied, not hint content; (ii) the model writing the hint does not need to be stronger than the model receiving it: hints from same-family GPT-OSS-120B, at roughly 6x the parameters, yield no materially greater benefits than self-written hints; and (iii) Fin-SD matches on-policy self-distillation from full reference solutions on accuracy while generating 9.5% fewer tokens. With Fin-SD, general reasoning on MMLU-Pro and a fourteen-metric compliance audit on FinTrust show no material regression.

---


### 17. [FinLLM-KG: Knowledge Graph-Enhanced LLMs for Financial Sentiment Analysis in Algorithmic Trading](https://arxiv.org/abs/2610.36083)

**<font color=#1a73e8>作者：</font>** Giorgos Iacovides, Oliver Hannibal, Wuyang Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in Generative AI have substantially improved financial sentiment analysis through post-trained financial large language models (LLMs). However, existing approaches remain confined to predicting the sentiment of each article in isolation and operate as black boxes, which limits contextual understanding and hinders deployment in high-stakes financial decision-making. To this end, we introduce FinLLM-KG, a model-agnostic framework that combines causal LLMs with a financial knowledge graph, in order to inject temporally grounded, company-level knowledge from SEC 10-K filings at inference time, without updating model weights. Within FinLLM-KG, context is supplied either as a natural-language company profile or as a small set of relevance-ranked factual triples. This enables sentiment predictions to account for broader firm-level information rather than the article alone, at almost zero computational cost and for any causal LLM. In addition, attributing each article-level sentiment score to individual sentences and to the retrieved knowledge-graph facts makes the evidence behind the prediction inspectable, thereby enhancing explainability and supporting human-in-the-loop review. Simulations demonstrate that FinLLM-KG consistently improves portfolio performance over the state-of-the-art baseline.

---


### 18. [Instruction Capacity: Behavior and Degradation of Language Models under Controlled Load](https://arxiv.org/abs/2610.36095)

**<font color=#1a73e8>作者：</font>** Hennadii Kutomanov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quality with which language models follow instructions falls as the load grows, yet there is still no quantity that expresses the limit of a model in units of load with an uncertainty. We propose an instrument in which the load consists of rules that replace single-token words in a text without meaning: such an instruction is atomic, the rules are independent by the construction of the task, and the outcome of every application of a rule is determined by a computable reference answer. Every occurrence of a word to be replaced becomes a Bernoulli trial with a known position in the answer and a known rule number. The statistical model first measures the shape of the dependence of the probability of a right replacement on the text length, the word position, the replacement density, the number of rules and the rule number, then describes it by smooth laws and restores a reference level that does not depend on the choice of the coding. The model yields the instruction capacity - the number of rules held at a given share of right replacements - with an uncertainty. A measurement of GPT-4o mini (2958 requests, 642,430 trials) gave regular laws for every load factor and for the collapse of the answer; the instruction capacity was about 37-38 rules at a share of right replacements of 0.95, and about 18-19 rules at the full replacement density. The code of the instrument, the measurement data and the passport are open, and every number of the passport is recomputed from the published points. The passport of a model serves as the calibration of a future meter of the instruction load of prompts.

---


### 19. [CohortFlow: A Steerable Clinical Cohort Curation Agent with Localized Semantic Correction](https://arxiv.org/abs/2610.36100)

**<font color=#1a73e8>作者：</font>** Neil Chen, Adrian Serapio, Hanxue Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model agents for clinical cohort curation should accommodate evolving eligibility criteria without repeatedly processing unchanged requirements. We introduce CohortFlow, a steerable agent that represents natural language corrections as localized updates to a structured cohort specification and reconciles them with a persistent execution graph. Explicitly recorded semantic dependencies enable affected computations to be selectively invalidated while preserving valid prior results. On 100 scenarios derived from clinical-trial eligibility criteria, comprising 126 correction turns, localized steering achieves 77.0% requirement micro-F1 versus 76.4% for full regeneration using the same 8B model, a small numerical advantage that is not statistically significant ($p=0.493$). It reduces mean correction latency by 64.8% after completion and 44.3% during execution, with 38.1% fewer model calls. In a separate proof-of-concept evaluation over MIMIC, all 13 cohort states execute successfully, while correction trajectories demonstrate selective preservation of unaffected computations and recomputation of changed or dependent nodes. Together, these results show that localized semantic steering can substantially reduce correction latency and model calls while maintaining strong requirement-level accuracy.

---


### 20. [Beyond Update Counts: A Control Map for Evaluating Test-Time Model Updates](https://arxiv.org/abs/2610.36109)

**<font color=#1a73e8>作者：</font>** Zehao Zhao, Shangjian Yin, Rui Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time updating lets a language model change persistent state after training---such as model weights, adapter parameters, or a memory module---before or while answering queries. Existing evaluations often compare systems using update count or frequency and performance measured immediately afterward. These summaries omit what is updated, where, when, and in what order. The same total can therefore hide an important difference: one system may answer after one update while another answers after two. We introduce the Control Map, an evaluation framework that records the committed updates preceding each scored answer and separately evaluates behavioral changes, immediate learning (acquisition), later recall (retention), preservation of unrelated behavior (locality), and performance in new settings. We prove when counts alone determine final state and show, under stated assumptions, how differences between pre-answer histories limit differences in average scores. Using ControlMap, our experiments reveal three insights. First, update scheduling matters: at a 760M-parameter checkpoint, 24 schedules with the same update count yield 19.7%--34.2% accuracy. Second, learning an edit does not guarantee that it lasts or remains contained: all six selected CounterFact LoRA settings learn the new information, while ROME retains edits at all 13 operating points but fails locality at each. Third, no editor performs best consistently across models, benchmarks, and tests. Evaluations should therefore report update histories and assess acquisition, retention, and locality separately.

---


### 21. [Don't Pick a Winner: Knowledge Conflicts Need a Prior, Not a Rule](https://arxiv.org/abs/2610.36169)

**<font color=#1a73e8>作者：</font>** Minh Pham Van, Cong Tran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A retrieval-augmented language model answers from two sources, the retrieved context and its own knowledge, and the two disagree whenever the context is incomplete or wrong. Existing methods settle the disagreement with a rule fixed at design time: follow the context, amplify it in proportion to how far it moves the model, or trust the model's memory. Each rule is confidently wrong in some deployment. In a decision-theoretic model of two sources, the score of any fixed rule is linear in the share of reliable contexts while the best attainable score is convex, so every fixed rule is beaten wherever it is not exactly optimal; and a symmetric divergence between the two sources, the signal adaptive decoding uses, carries no information about which one is right. Resolving a conflict therefore needs two inputs that no existing method keeps: evidence about each source separately, and a prior on how often the context is right. We test these claims on GRACE, a benchmark that intervenes on the knowledge-graph context of a fixed question, so that what the model knows, what the context says and what is true are measured separately. There, every baseline from four families is strong on right contexts or on wrong ones, never on both. We then build the two inputs: the model states its knowledge as notes, a small policy voices each note with a calibrated confidence, a reader answers in two voices, and a selector commits or abstains under a prior $\pi$ applied as an exact prior shift. With $\pi$ set to the true share of right contexts, the system is above the best baseline at every mixture of GRACE contexts, by up to 26 points. Its overall score is 45.3 and 35.0 (Qwen3.5-35B-A3B, Llama-3.1-8B), against 29.4 and 27.5 for the best baseline. On preregistered ClashEval it beats same-backbone CK-PLUG and TCR by 12 and 26 points. Where the model lacks the knowledge, the gains vanish, as the theory predicts.

---


### 22. [3, 7, 14, 17, 42: Instruction Tuning Installs and Sharpens Number-Choice Heuristics in Language Models](https://arxiv.org/abs/2610.36178)

**<font color=#1a73e8>作者：</font>** Samar Ansari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We measure, without sampling error, the probability a language model assigns to each integer from 1 to N when asked for a random number. For a fixed prompt the model defines one probability vector, which we compute by summing over each integer's scored spellings rather than estimate by sampling, removing the noise that limits earlier studies [1, 4]. We evaluate 18 open-weight model lines at five ranges up to N = 100, under 29 decoding configurations, on two inference stacks; 15 of them have matched base and instruction-tuned checkpoints that both give usable answers. Instruction tuning makes the distribution less uniform in all 15 pairs. It installs one heuristic, round-number avoidance, and sharpens another, endpoint avoidance. Base checkpoints do not avoid round numbers once the endpoints are removed from those sets; tuned checkpoints avoid them, multiples of 10 almost completely. Base checkpoints return the endpoints 1 and N at 0.30 to 0.60 of the interior rate; tuned checkpoints almost never return them. A preference for odd numbers is consistent across tuned checkpoints only at N = 100, where base checkpoints also show it weakly. Endpoint avoidance and the odd preference fit the account Kubovy and Psotka [6] proposed for human number choice; round-number avoidance is not part of that account, and the midpoint avoidance it predicts is essentially absent, with one slight exception at N = 100. Tuning does not install a new favourite integer shared across models: above N = 10 no modal integer is shared by more than 42 percent of tuned conditions, and P (17) rises in 10 of 15 pairs and falls in 5. The concentration is present in the model's own distribution: at temperature 1.0, nucleus truncation at top-p 0.95 adds a median of 0.035 to the total variation distance.

---


### 23. [Skill Dreaming: Evolving Repository Skills through Pull Request Streams](https://arxiv.org/abs/2610.36188)

**<font color=#1a73e8>作者：</font>** Xinyuan Song, Hasibul Haque, Jay Somasundaram 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on reusable skills for complex software engineering tasks, making skill libraries essential for repository development and maintenance. However, repository-specific skills must evolve with changing code structures, implementation conventions, and maintenance requirements. Pull requests (PRs) provide a natural source of such knowledge by recording how repositories evolve through implementation and review. Meanwhile, new PRs must follow repository-specific implementation patterns, modify related components consistently, and ensure that existing tests continue to pass while adding coverage for new functionality. This creates a mutually reinforcing cycle: PRs provide knowledge for updating skills, while these skills improve future PRs, maintain repositories, and support further skill evolution. To enable this co-evolution of PRs, repositories, and skills, we propose Skill Dreaming, a framework that learns from PR streams to guide continuous repository development and maintenance. Given a repository and its PR history, Skill Dreaming builds a repository-specific skill library by extracting executable knowledge from validated PRs and continuously refines the skills as new PR information becomes available. These skills guide coding agents not only in implementing requested features but also in maintaining associated tests, documentation, compatibility, and repository conventions. By integrating PR analysis, skill management, code execution, and continuous integration, Skill Dreaming provides an end-to-end workflow for applying learned skills to repository changes and incorporating subsequent PR outcomes into future skill updates.

---


### 24. [LLM Hallucination Detection via Low-rank Multilinear Decomposition](https://arxiv.org/abs/2610.36191)

**<font color=#1a73e8>作者：</font>** Devansh Sharma, Faizul Rakib Sayem, Shahana Ibrahim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) frequently generate fluent yet factually incorrect responses, raising concerns about their reliability. Recent hallucination detectors increasingly exploit internal representations, but extracting informative signals from high-dimensional hidden states remains challenging. Existing approaches often rely on selected activations or pooling-based compression, potentially overlooking discriminative information distributed across Transformer layers, feature modes, and tokens. We propose LOTUS (Low-rank Order-statistic TUcker-based Subspace learning), a multilinear low-rank decomposition framework for hallucination detection that extracts compact representations from LLM hidden states while reducing dependence on labeled data. Our approach first summarizes variable-length token representations using complementary statistical descriptors that capture peak activations, activation distributions, and cross-layer changes. We then leverage low-rank multilinear decomposition to extract compact representations that capture the underlying structure of LLM hidden states, which are subsequently used to train a lightweight hallucination classifier. Experiments across multiple LLMs and question-answering benchmarks demonstrate improved hallucination detection performance over recent state-of-the-art baselines.

---


### 25. [Learning to Read Braille: Benchmarking and Improving Braille Recognition Capabilities of VLMs](https://arxiv.org/abs/2610.36195)

**<font color=#1a73e8>作者：</font>** Kartik Jangra, Atharva Gawane, Siddharth Pulipaka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress in visual understanding and document transcription, modern vision-language models (VLMs) struggle with a fundamental accessibility task: reading Braille from images. We introduce BrailleBench, a manually curated benchmark of 259 real-world Grade-1 and Grade-2 Braille images. We evaluate proprietary, open-weight, OCR-specialized, and tool-assisted multimodal systems and find that standalone general-purpose models perform poorly at directly transcribing Braille images, whereas tool-assisted systems perform much better. We design a synthetic Braille generation pipeline with diverse layouts and image perturbations. A 2B VLM model trained on our synthetic data reaches 87% exact match on Grade-1 and 61% on Grade-2 BrailleBench, outperforming standalone VLMs and achieving the highest Grade-2 exact match score among the evaluated systems. We further show that high accuracy on synthetic validation data does not guarantee high accuracy on real photographs in our experiments: models trained on prior synthetic data reach up to 96% on their synthetic validation set but at most 3.26% on Grade-1 BrailleBench. Our results identify an accessibility-relevant capability gap in multimodal systems and show that targeted synthetic supervision can improve real-world Braille transcription.

---


### 26. [Base Models Can Detect Hidden Intentions that Prompted Classifiers Miss](https://arxiv.org/abs/2610.36202)

**<font color=#1a73e8>作者：</font>** Oz Amram  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Persona Selection Model (PSM) posits that post-training selects a persona the model learned during pre-training. Work on subliminal learning has shown that models can impart covert signals (like "love of owls") into semantically unrelated outputs like strings of numbers, and that students trained on these outputs inherit those traits. In this work I show that by evaluating the likelihood of such outputs under the base pre-trained model with an appropriate header, a method I call persona-header likelihood evaluation (PHLE), one can decode these subliminal signals and classify between them. For example, PHLE distinguishes number sequences generated by a post-trained model prompted with "You love owls" from those prompted with "You love eagles", and distinguishes answers from a model with a secret desire to harm the user, filtered to remove any noticeable misalignment, from those of a model with no system prompt. In both cases prompted classifiers, including the generating model itself, remain near chance. The signal partially persists across model families, with the Qwen base model reading signals generated by Olmo and vice versa. This is evidence for a non-trivial prediction of the PSM, and the method may be practically useful for auditing the hidden objectives of models.

---


### 27. [Diagnosing and Correcting Bias in MLLM for Long Video Understanding](https://arxiv.org/abs/2610.36210)

**<font color=#1a73e8>作者：</font>** Xusheng Liang, Jianqiao Sun, Hao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video question answering is challenging since the answer often hinges on a few decisive moments scattered throughout the video, while memory constraints force Multimodal Large Language Models (MLLMs) to sample frames at extremely low rates, resulting in sparsity that risks omitting key evidence. Though aggressively enlarging the context size is intuitive, we argue that performance remains fundamentally constrained by the bias, \emph{i.e.}, the misleading cues caused by spurious \textit{linguistic} correlations and salient yet irrelevant \textit{visual} observations. In this paper, we first introduce {S-MME}, a benchmark designed to systematically diagnose shortcut-biased behavior in MLLMs. To mitigate this failure, we further propose a training-free framework, Counterfactual Long-video Evidence-Aware Reasoning (CLEAR). By treating the full video-question pair as a complete view, CLEAR estimates bias effects via augmented views by only keeping the question or locally salient visual clips. Then, we intervene hidden states to mitigate the discrepancy at inference such that the correct answer can be predicted confidently. With experimental studies across five benchmarks, we show that our method is generalizable and can be integrated in different MLLMs, yielding consistent gains in prediction and robustness. We hope CLEAR can offer a complementary direction in test-time scaling for long-video understanding.

---


### 28. [EREBOTS 4.0: A framework for conversational assistants with A2A agents and MCP tools](https://arxiv.org/abs/2610.36221)

**<font color=#1a73e8>作者：</font>** Elia Pacioni, Davide Calvaresi, Andrei C. Coman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In recent years, multi-agent systems have shifted from rule-based, symbolic agents to sub-symbolic agents built on language models. However, several limitations remain unresolved. The new frontier is neuro-symbolic agents, which pair language models with deterministic tools and explicit protocols. Without a common framework to standardize and compose them, each study rebuilds the same infrastructure, and results are hard to replicate. This paper presents EREBOTS 4.0, an open-source, hybrid-AI, multi-agent framework that fills this gap for conversational assistants. Language-model agents plan and route requests, while deterministic tools compute exact results over the Model Context Protocol (MCP). An orchestrator selects one or more specialist agents per turn and calls them over the Agent2Agent protocol (A2A). A new agent, local or remote, is added by listing its URL in a configuration file. The framework also manages identity, user context with consent flags, task states and traces. Its A2A server passed 97 tracked requirements in the official A2A Technology Compatibility Kit, with no failures.

---


### 29. [MARQ: A Modular, LLM-Agnostic Requirement Quality Assessor Infused with Systems Engineering Knowledge](https://arxiv.org/abs/2610.36234)

**<font color=#1a73e8>作者：</font>** Jannatul Shefa, Alejandro Salado, Paul Wach 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Requirements engineering (RE) is foundational to systems engineering (SE), as requirement defects can propagate downstream and adversely affect development outcomes. Although large language models (LLMs) are promising for requirement quality assessment, prior work shows that off-the-shelf models miss a large share of expert-identified defects, perform unevenly across quality criteria, and vary across executions. This study investigates whether infusing expert-derived SE knowledge can improve LLM-based requirement quality evaluation beyond off-the-shelf capability. We present MARQ, a modular, LLM-agnostic prototype that supplements LLMs with a criterion-specific knowledge stack operationalizing INCOSE requirement quality criteria and evaluated against off-the-shelf baselines on an expert-labeled NASA requirement set using Claude Opus 5, GPT-5.6 Sol, and the open-weight Gemma 3 12B, with 100 executions per model. MARQ achieves median F1 scores of 0.80 for Claude Opus 5, 0.62 for GPT-5.6 Sol, and 0.53 for Gemma 3 12B, compared with off-the-shelf baselines of 0.55, 0.52, and 0.18, respectively. However, the nature of these gains is model-dependent. Claude Opus 5 improves defect detection and false-alarm control; GPT-5.6 Sol gains detection and better execution-level consistency at the cost of more false alarms; and Gemma 3 12B reaches the performance of off-the-shelf proprietary models, although it remains highly variable. Criterion-level analysis shows gains concentrated in Correctness and Conformance, trade-offs between misses and false alarms within individual criteria, and model-dependent responses across several criteria. These findings position SE knowledge infusion as a promising model-agnostic pathway for strengthening trustworthy LLM-based RE support while underscoring the need for criterion-specific interventions and human-in-the-loop review.

---


### 30. [The Inbox as a Coordination Primitive for LLM Agent Societies](https://arxiv.org/abs/2610.36264)

**<font color=#1a73e8>作者：</font>** Karthik Sreedhar, Leo Yuan, Pradyumna Chari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Language-model agents increasingly coordinate in large groups, and current agent protocols focus on delivering messages. For these agents, however, the scarce resource is not delivery but reading: every message costs tokens, and the context is finite. Current infrastructure works by push: the sender decides when a message enters the recipient's context, so the recipient reads in arrival order and drops the oldest messages once its context is full. We study the alternative, pull, in which messages wait in an inbox outside the context and the recipient's own rules decide what it reads and keeps. We argue that the inbox is a coordination primitive: each agent sets its rules privately, and those rules decide whether other agents' requests reach it. In simulated societies of up to 16,000 agents, with every decision an LLM judgment, we report three findings. First, push fails as an agent takes part in more coordination at once: an agent leading 20 negotiations with a full memory proposes options already rejected 97% of the time, because it has dropped the oldest replies. Second, an inbox is necessary under heavy, noisy traffic. Where first come, first read misses every request, an inbox that first reads messages carrying a refundable deposit still finds about 60% of the agents a request needs, at every size from 1,000 to 16,000. On a real email network, losses compound: when half the agents adopt such an inbox, forwarded search recovers only 5% of full adoption, against 42% for one-hop search. Third, an inbox comprises four decisions (what to read, what to keep, what a sender pays, and what a reply may say), and the best rule for each depends on the traffic and the agent's role. Multi-agent coordination under load requires an inbox layer designed for the traffic each agent receives.

---


### 31. [BUSTA: Teaching Small Language Models to Reason About Binary Execution](https://arxiv.org/abs/2610.36288)

**<font color=#1a73e8>作者：</font>** Ritika Poddar, Aidan Fennelly, Deirdre Murphy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLM) are increasingly applied to Reverse Engineering (RE) workflows. RE, however, differs from common LLM coding tasks as it requires models to reason about low-level program behavior. Furthermore, the deployment of tooling in resource-constrained sandboxed RE environments limits the ability to use frontier-scale solutions. We examine whether a targeted LLM training approach can transfer distinct RE skills to open models via inverse basic-block execution: given an x86-64 basic block and a desired output register state, the model predicts the input register values that produce it. Fine-tuning \texttt{Qwen3-1.7B} and \texttt{Nemotron-3-Nano} with Group Relative Policy Optimization (GRPO) raises knowable-register prediction accuracy from 73.2\% to 85.3\% and from 63.3\% to 95.2\%, respectively. Frontier models still score highest (up to 99.2\%), but our fine-tuned \texttt{Nemotron-3-Nano} comes within four points at a fraction of the parameter count. We release both fine-tuned models and the training dataset.

---


### 32. [Detecting and Mitigating Query-Based System Prompt Leakage Attacks](https://arxiv.org/abs/2610.36295)

**<font color=#1a73e8>作者：</font>** Tushar Nayan, Pratik Poudel, Qian Lou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) rely on proprietary system prompts to enforce task directives, safety policies, and access controls. These prompts are vulnerable to query-based leakage attacks, where black-box adversaries extract confidential instructions through adaptive, multi-turn interactions. Existing defenses often assess queries independently, missing malicious behavior that emerges across interactions.
We present AdvGuard, a model-agnostic framework for detecting and mitigating system prompt leakage. AdvGuard models cross-query relationships using a bounded semantic interaction graph, statistically filters candidate components, and converts them into line graphs for graph convolutional network (GCN) classification. This approach captures multi-hop patterns in query similarity that distinguish coordinated extraction from benign workflows. A lightweight prompt-level detector provides protection before sufficient interaction history accumulates, and the framework supports black-box LLM deployments.
In mixed-query evaluations, AdvGuard improves recall by up to 36% over the strongest baseline while maintaining a false positive rate of at most 3.4%. In multi-turn workloads, it achieves 97.23%-99.1% F1 with 100% recall. Leave-one-attack-family-out tests yield 99.98% mean recall and 99.99% mean F1, with no observed false positives. Integrated into the adaptive PLeak and LeakAgent attack loops, AdvGuard limits exact-match leakage to 0.00-0.01 and substring-match leakage to 0.01-0.09 across evaluated victim models. These results demonstrate robust detection of unseen attack families and substantially reduced prompt reconstruction.

---


### 33. [When Retrieval Is Not Enough: Obsolete Facts in Agent Memory](https://arxiv.org/abs/2610.36308)

**<font color=#1a73e8>作者：</font>** Oleeviya Babu Poikarayil, Tony Basil Babu, Abdulrahman Nahhas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory-agent benchmarks often collapse retrieval and answer generation into one score, making it hard to tell whether a failure comes from missing an update or from not using an update that was already retrieved. We examine this distinction on the single-hop FactConsolidation task of MemoryAgentBench. With Qwen2.5-7B-Instruct on 6K-history BM25 accuracy drops from 45% to 32% when the retrieved evidence budget grows from 64 to 512 tokens, even though a gold-assisted post-hoc audit finds the newest statement in every retrieved set. Most of the errors occur on questions that also contain an obsolete statement version. Under a frozen prompt and equal four-statement evidence size, replacing one unrelated statement with the obsolete competing statement reduces accuracy from 100% to 44.6% for Qwen2.5 and from 100% to 87.8% for Qwen3-14B, with all 50 harmful paired flips classified as stale. A 32K-history replication likewise favors BM25-64 over BM25-512 (69% versus 58%). These results suggest that retrieving the correct fact is not enough. An obsolete competing statement can be more harmful than an unrelated piece of evidence of the same size.

---


### 34. [Ontology-guided multi-agent reasoning for explainable differential diagnosis](https://arxiv.org/abs/2610.36325)

**<font color=#1a73e8>作者：</font>** Roxana Ramona Szomiu, George Ursu, Adrian Groza  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective differential diagnosis depends on well structured and unambiguous patient case descriptions, since incomplete or ambiguous clinical information readily leads to diagnostic errors and inconsistent reasoning. Large Language Models (LLMs) have recently shown promising capabilities in medical question answering and clinical reasoning; however, even when achieving competitive performance on medical benchmarks, they often rely on pattern recognition learned from training data rather than grounded clinical evidence, and can generate plausible yet unsupported diagnostic conclusions. Their reasoning remains largely opaque, making it difficult for clinicians to assess the evidence and rationale behind a given recommendation. To address this gap, we propose an ontology-guided, multiagent differential diagnosis framework that replicates the iterative reasoning process of physicians. The framework grounds diagnostic inference in a structured, expert-curated medical knowledge base, enabling interpretation of symptoms, clinical findings, or disease relationships, while decomposing diagnosis into explicit, auditable reasoning steps. This ontology-based grounding constrains inference to evidence-backed associations, reducing hallucination and improving diagnostic transparency, traceability, and consistency. The system then identifies the most discriminative missing symptoms and generates targeted follow-up questions to reduce uncertainty through a process that mirrors to clinical inquiry. Together, these components improve the reliability, explainability, and diagnostic accuracy of AI-assisted differential diagnosis. The source code is publicly available.

---


### 35. [Training-Free Inference Acceleration for Video Large Language Models: Methods, Trade-offs, and Evaluation](https://arxiv.org/abs/2610.36327)

**<font color=#1a73e8>作者：</font>** Yuqi Li, Chuanyue Yan, Neil Rodrigues 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models (VLMs) have demonstrated strong capabilities in video understanding and reasoning, but processing long visual sequences incurs substantial computational, latency, and memory overhead. This survey examines training-free inference acceleration, focusing on reducing inference costs while preserving task-relevant spatiotemporal evidence. We organize existing methods by their intervention stages in the inference pipeline, covering input, visual encoding, projector, prefill, and decoding. Post-training quantization (PTQ) is discussed separately as a cross-stage extension with varying calibration requirements. We analyze how intervention position affects evidence preservation and computational savings, and why local efficiency improvements may not translate into end-to-end acceleration. We complement this analysis with quantitative evidence from prior studies and our own experiments under a shared evaluation setting to assess accuracy-latency trade-offs.

---


### 36. [How Stable Are LLM-Generated Proofs Under Program Refactoring? A Stress Test for Verifiable Code Generation](https://arxiv.org/abs/2610.36328)

**<font color=#1a73e8>作者：</font>** Aravind Mandiga, Guoming Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmarks for verifiable code generation usually test a proof against one fixed implementation. We ask whether the same proof remains valid after a program refactoring that preserves behavior. We introduce RefactorProof, which derives 458 Lean-certified variants from the 185 VERINA tasks that compile in our pinned environment while holding the specification and evaluated proof fixed byte-for-byte. VERINA supplies reference proofs for 46 tasks, all from its basic split; the primary model-versus-reference comparisons further match on 21-25 short, non-recursive tasks. Structural refactorings expose substantial brittleness across proof sources: task-normalized structural PSR is 4.3% for the supplied references and 13.3-26.8% for the specialized provers. On the matched tasks, specialized prover proofs nevertheless have higher overall unchanged-proof survival than the supplied reference artifacts: +15.6 points for DeepSeek-Prover-V2-7B, +18.8 for Goedel-Prover-V2-32B, and +20.3 for Goedel-Prover-V2-8B; all three 95% CIs exclude zero. The ordering persists after excluding universally survived T1 variants, under family-balanced aggregation, and under alternative deployable valid-proof selection rules. However, unchanged-proof failure is not the same as high repair cost: predefined one-identifier edits repair 51/54 eligible reference structural failures and 58/85 eligible prover failures. RefactorProof therefore measures unchanged-proof stability under program refactoring, not the cost of maintaining a proof after it breaks.

---


### 37. [OA-RAG: Ontology-based Agentic RAG for Faithful LLM Reasoning](https://arxiv.org/abs/2610.36335)

**<font color=#1a73e8>作者：</font>** Hui Yang, Jiaoyan Chen, Yongsheng Gao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) perform well across many real-world tasks but remain prone to hallucination, limiting their reliability in domains such as biomedicine and healthcare, where answers must be grounded in established knowledge. Retrieval-augmented generation (RAG) mitigates this problem by incorporating external information, but often overlooks logical relationships and relies heavily on the LLM's own reasoning, which can compromise answer faithfulness. We propose OA-RAG, an agent that integrates formal reasoning with LLM reasoning, drawing on both the logical structure and informal annotations of domain ontologies. For each answer, OA-RAG reports the ontology observations used as evidence and a model-assessed grounding level (entailed, supported, related, or unrelated) that characterises the strength of that evidence. Across benchmarks derived from three large-scale ontologies and six real-world medical question-answering tasks, OA-RAG achieves the best overall performance among the evaluated ontology-fine-tuned and popular RAG methods, with particularly strong results on reasoning-intensive tasks. The reported grounding levels also offer a useful indication of answer reliability, with stronger grounding generally associated with higher accuracy. Finally, our results demonstrate the value of ontologies as knowledge sources: OA-RAG is competitive with, and sometimes outperforms, domain-specific RAG systems that draw on sources such as textbooks.

---


### 38. [Executable Archaeology of Programs That Model Programming: Reanimating the Heuristic Compiler (1961) and KBEmacs (1984)](https://arxiv.org/abs/2610.36341)

**<font color=#1a73e8>作者：</font>** Jeff Shrager, Kent M. Pitman, Mia Golec  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early AI programs were often also theories of how people think, and programs that wrote programs were, in part, theories of how people program. Here we report on the reanimation of two such programs that offer two seemingly different theories of programming and were developed for quite different purposes. The first, Herbert Simon's Heuristic Compiler (1961), was an experimental model of programming as problem-solving, applying the means-ends analysis methods of the General Problem Solver to investigate the nature of the programming task. The second, KBEmacs (1984), was a working prototype of an intelligent programming assistant developed by MIT's Programmer's Apprentice project, built on the view that expert programmers recognize and combine familiar patterns, or "cliches." It let a programmer build up programs by combining cliches through a stylized English command language. We approach both through the methodology of Executable Archaeology, the study of historical computational systems by running their original code, a process we call "reanimation." Our reanimation of the Heuristic Compiler reproduces the compiled code appearing in Simon's 1963 paper, and our reanimation of KBEmacs reproduces the SQRT sequence of its December 1984 self-test. Examined side by side, the two theories turn out to have much in common: the Heuristic Compiler also works by adapting existing routines, and Simon later argued that search alone requires a large body of programming knowledge. To highlight the reflexivity of this project, we deliberately used a modern AI-assisted programming tool, Anthropic's Claude Code (Opus 5.5), to carry out much of the detailed reanimation work, building on a significant base of existing software. The explicit, executable theories of programming that both systems embodied are largely absent from today's far more capable AI coding assistants.

---


### 39. [Detect Before You Disambiguate: Perturbation-Based Input Ambiguity Detection in LLMs](https://arxiv.org/abs/2610.36353)

**<font color=#1a73e8>作者：</font>** Tiejin Chen, Xiaoou Liu, Michael Clifford 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often answer ambiguous inputs as if they had a single intended meaning. This is problematic because input ambiguity is an upstream source of uncertainty: when a prompt admits multiple valid interpretations, the key question is whether the model should answer directly at all. Existing input uncertainty methods often rely on LLM-generated statements or clarifications, but such transformations may already disambiguate the input before the ambiguity is measured. We propose a label-preserving perturbation framework for input ambiguity detection in which perturbations remain close to the original input while preserving its label. We instantiate this principle with two detectors: a black-box rule-based perturbation library and a white-box importance-guided method using model-internal signals. Experiments across four datasets in open-domain, conversational, and visual QA show that our methods outperform output-side uncertainty baselines and LLM-paraphrase-based perturbation baselines. Our results highlight the importance of detecting ambiguity before attempting to disambiguate it. Our code is available \href{this https URL}{\textcolor{purple}{here}}.

---


### 40. [WAKMan: Workload Aware KVCache Manager](https://arxiv.org/abs/2610.36355)

**<font color=#1a73e8>作者：</font>** Suhas Kumar Morisetty, Vaibhavi Lokegaonkar, Sachin Mathew Varghese 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prefix caching enables a Large Language Model (LLM) servers to reuse the Key-Value (KV) states and accelerate prefill computation stage for requests that share a prefix with earlier prompts, thus reducing latency and serving cost. With limited memory resource, the KV cache eviction policy becomes a decisive factor in determining the overall benefits of prefix caching. Production traffic may have single-turn, multi-turn, agentic, or a mixture of any combination of these request types. Our findings indicate that agentic steps return within seconds and favor recency, while popular prompts and long conversations return after many other requests and favor frequency. Across 20 mixes, no single policy is always best: vLLM's default strategy LRU provides 12% higher cache hits as compared to the frequency-oriented S3FIFO on agentic-heavy mixes but trails it by up to 22% elsewhere, and even a single workload parameter can flip the winner even for any particular mix. We present WAKMan, a workload-aware KV cache manager that picks its eviction policy from live traffic without knowing request types or reading prompts. It improves hit rate over LRU by 5 percentage points on average, with the lowest mean and worst-case optimality gap of all policies.

---


### 41. [BoxWorld: Let World Engines Control and Video Generators Render](https://arxiv.org/abs/2610.36371)

**<font color=#1a73e8>作者：</font>** Zike Wu, Ahmed Hatem, Chintan Trivedi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We tackle the challenge of building real-time interactive video worlds with user-defined behaviors. Such worlds must track object states, apply interaction rules, and render the resulting consequences as users act. Yet existing end-to-end video world models typically learn interaction dynamics within the generator, making it difficult to specify object-level rules and reason about their consequences. In this work, we introduce BoxWorld, which separates interaction reasoning from generative rendering. Given user-specified rules, a coding agent creates a Box World Engine that determines interaction outcomes and exposes the resulting object states through a lightweight interface of layout boxes, persistent object attributes, and dynamic status variables, leaving appearance and physical effects to generative rendering. A Box-State Generative Renderer then renders this evolving state stream into video autoregressively, enabling online control over object motion, state switches, and conditional events. Rendering this state stream is non-trivial: the renderer must respond to object-level state updates in real time while remaining coherent with the generated history. To this end, we introduce a three-stage training strategy that learns object grounding from open-domain videos and state transitions from gameplay videos, both annotated automatically, and finally performs rollout distillation on self-generated histories. We further propose PairedStateBench, a paired benchmark for fine-grained interaction control. BoxWorld substantially outperforms end-to-end world models and remains competitive across multiple public benchmarks. Project page: this https URL.

---


### 42. [Evaluating Federated Vision-Language and Vision-Only Models for Privacy-Aware Breast Cancer Imaging](https://arxiv.org/abs/2610.36379)

**<font color=#1a73e8>作者：</font>** Malithi Mithsara Wanniarachchi Kankanamge, Ning Yang, Sree Bash Debnath 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) shows promise for breast imaging, but limited labeled data, institutional data fragmentation, and privacy concerns hinder centralized training. We investigate a privacy-aware federated learning framework combining pretrained vision-language models (VLMs) with client-level differential privacy. We compare general-purpose CLIP models, biomedical BiomedCLIP, and an ImageNet-pretrained ViT-B/16 baseline on two public breast imaging datasets, with and without differential privacy. We also evaluate a CLIP ViT-B/16 ablation that removes the text pathway. Evaluation includes patient-level ROC-AUC with bootstrap 95% confidence intervals, baseline comparisons, threshold sensitivity, inter-model agreement, and communication cost. Under federated learning, all five models achieve high normal-versus-sick discrimination (ROC-AUC: 0.940-0.990). However, acquisition year alone achieves 0.974 on the same test partition, raising concerns about confounding rather than genuine pathology recognition. Benign-versus-malignant discrimination remains uncertain (ROC-AUC: 0.504-0.637), with all confidence intervals including 0.50. Removing the text pathway preserves classification accuracy while halving communication cost. Differential privacy reduces ROC-AUC by 0.375, attributable to perturbing the full model state rather than only trainable parameters. These findings highlight the importance of evaluating confounding, predictive reliability, privacy implementation, and deployment efficiency when developing federated AI systems for breast imaging.

---


### 43. [From Generation to Scoring: Scaling LLM-Based Semantic Labeling at LinkedIn](https://arxiv.org/abs/2610.36383)

**<font color=#1a73e8>作者：</font>** Jian Sheng, Sriram Vasudevan, Sundara Raman Ramachandran 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For efficiency, industrial large language model (LLM) labelers often pack many candidate labels into one prompt and generate a YES/NO answer for each, even when each decision depends only on the entity and one candidate. Generating these independent decisions as one answer list couples them, spends decoding on the list, and relies on the list being well-formed. In this paper, we present an end-to-end recipe that reformulates the labeler as semantic scoring, fine-tuning it on single-candidate prompts to return each decision as one answer-token score from a prefill-only pass. We also adapt Multiple-Item Scoring (MIS) to score hundreds of candidates in one sequence with attention masked between them. Deployed for profile qualification labeling at LinkedIn, semantic scoring changes at most 0.01% of decisions when candidates are reordered and matches the agreement with reference labels that packed generation reaches only with about 4.7x as many training pairs. The MIS-based stack raises throughput over the deployed stack by 1.24x offline and 1.9x in model serving under a one-second p99 latency target. For offline batch inference, we implement MIS-based scoring as a reusable, model-agnostic Ray Data API proposed for upstream adoption. Model serving uses MIS support contributed to SGLang.

---


### 44. [SOMA: A Benchmark for Fine-Grained Egocentric Behavior and Body-Motion Understanding](https://arxiv.org/abs/2610.36384)

**<font color=#1a73e8>作者：</font>** Matea Tashkovska, Naël Ouerghemi, Haozhe Qi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perceiving human body motion is critical for multimodal systems that understand and assist people. Yet current evaluations of Multimodal Large Language Models (MLLMs) largely focus on objects, scenes, and coarse actions, leaving their ability to reason about the body itself poorly assessed. This is especially challenging from the egocentric perspective, in which the body is only partially visible and motion must be inferred from occluded and temporally distributed cues. We introduce SOMA, a benchmark for fine-grained body-motion understanding from egocentric video, comprising 1,632 human-verified questions across three capability axes: body configuration, motion dynamics, and temporal reasoning. We evaluate 37 leading closed-source, open-source, and specialized egocentric MLLMs, complemented by an extensive human evaluation. We find that humans also find this task difficult from video alone (68.5% accuracy), yet clearly outperform the strongest MLLM (Qwen3.6-27B), which reaches 50.0% zero-shot accuracy. Our error analysis shows that MLLMs often misread the wearer's own body, misjudge events in time, and are prone to biases such as favoring the right hand or under-counting repetitions. To narrow the gap to human performance and support further progress, we introduce a training dataset of aligned video, body motion, and language supervision, and a multimodal baseline that jointly learns from these modalities. By identifying common failure modes and missing capabilities in current MLLMs, we hope SOMA will inspire future research on body-motion understanding and multimodal reasoning. Full benchmark, training data, and code will be released at: this https URL

---


### 45. [MAREval: A Multi-Agent Framework for Evaluating Natural Language Recommendation Explanations](https://arxiv.org/abs/2610.36389)

**<font color=#1a73e8>作者：</font>** Reza Yousefi Maragheh, Jayesh Uddhav Kudase, Aysenur Inan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating natural language explanations in recommender systems is essential for fostering user trust, transparency, and engagement. However, existing evaluation approaches like human evaluations, while accurate, are resource-intensive and impractical at the scale required by modern recommendation platforms. Also, automated methods using single-agent LLMs suffer from prompt sensitivity and inconsistent outputs. To address these challenges, we propose MAREval, a structured multi-agent framework for evaluating recommendation explanations using large language models. MAREval orchestrates (i) a planner agent that uses a novel Chain of Debate (CoD) prompting strategy to coordinate agent roles and enforce logically consistent evaluation plans; (ii) a moderator agent that regulates discussions by mitigating prompt drift; and (iii) an arbitrator agent that aggregates outputs from multiple evaluation rounds and (iv) a Monte Carlo sampling method, improving robustness and alignment with human judgment. We conduct comprehensive evaluations on both public (TopicalChat) and proprietary recommendation datasets, demonstrating that MAREval outperforms state-of-the-art baselines. Comprehensive experiments on a public benchmark and a proprietary e-commerce dataset show that MAREval improves alignment with human judgments over strong singleand multi-agent baselines. Stability analyses indicate substantially lower variability across repeated trials. In a large human-annotation gate, MAREval meets production quality thresholds where prior evaluators fall short, and online A/B testing demonstrates statistically significant improvements in engagement and revenue metrics. These results establish MAREval as a scalable and reliable solution for human-aligned evaluation of recommendation explanations in real-world systems

---


### 46. [kw-bench: Breaking Frontier Harnesses on Real-World Tasks](https://arxiv.org/abs/2610.36405)

**<font color=#1a73e8>作者：</font>** George Juraj Salapa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Each new generation of frontier model pushes the edge of what is possible. Inside a harness -- a loop, a shell, a filesystem, the ability to write and run its own code -- a model can take on increasingly difficult work.
A growing body of work treats the coding-agent harness as infrastructure for knowledge work rather than a coding tool, and a new wave of benchmarks tests it there. Most of them are generative: build a financial model, a memo, a spreadsheet from a brief, judged by a rubric or by another model. Few test the expensive part of knowledge work, which is investigative. In audit, tax, due diligence, regulatory reporting, claims or any dispute over numbers, the answer already exists -- hidden in incomplete and inconsistent evidence spread across systems -- and has to be recovered and defended to the cent.
We introduce kw-bench, a benchmark built from real engagements specialists described to us. Its first task family is a five-year VAT reconstruction across three generations of SAP -- legacy ECC, a partial S/4HANA migration and a consultant's redesign -- delivered as raw system extracts: page headers, local number formats, partial link tables, no documentation of how anything connects. Grading is deterministic, with no LLM judge.
We ran four harnesses -- Claude Code, Codex, OpenCode and micro-cc -- on the same model, DeepSeek v4.1 Flash, for two hours. The two independent, model-agnostic harnesses delivered (OpenCode 0.542, micro-cc 0.528); the two lab harnesses, away from their home model, delivered nothing (0.00 each). What defeated them was inertia: keeping many weak signals alive across a long session. On a frontier model the task collapses. micro-cc and Claude Code on Claude Opus 5.5 scored 0.9986 and 1.000, in 22 and 25 minutes. A weeks-long engagement now costs minutes and a few dollars; below the frontier, the harness decides how far a model gets.

---


### 47. [Verifiable Efficiency Limits of Innate LLM Planning in Sliding Puzzles](https://arxiv.org/abs/2610.36415)

**<font color=#1a73e8>作者：</font>** Yezhou Cheng, Charles Ling  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-assisted planning success can reflect external search and verification, leaving a model's unaided planning ability unresolved. We isolate innate planning through complete plans generated in one response without tools or execution feedback. We propose a verifiable framework that decomposes success-weighted plan efficiency as $\mathrm{SPE}=R\times Q\times E$: execution reliability, planning coordination among legal plans, and action economy among completed plans. Trajectory replay and certified optima verify these factors; the joint score includes unsuccessful attempts. We evaluate 8,400 full-plan outputs from seven model conditions on $4\times4$ sliding puzzles, controlling exact horizon and obstacle count in the primary cohort. Models that complete every trial still become less economical at longer horizons, while higher efficiency among completed plans can coexist with poor goal attainment. SPE separates the overall capability hierarchy, while its factors distinguish coordination failure from inefficient completion. The framework makes long-horizon limitations in unaided planning quantitatively verifiable.

---


### 48. [SO-101 Bench: Accessible Spatial Manipulation](https://arxiv.org/abs/2610.36420)

**<font color=#1a73e8>作者：</font>** Truman Hickok  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-cost arms such as the SO-101 have become the most common entry point to robot learning, yet no released policy performs spatially constrained, language-conditioned tasks on them out of the box, and existing SO-101 benchmarks run only on physical hardware with simple tasks and few held-out objects. We introduce SO-101 Bench, a simulated benchmark for language-conditioned spatial manipulation built on an Isaac Lab digital twin of a real SO-101 setup. It has four tasks scored as five families, 138 objects in seen, unseen-instance and unseen-class splits, 916 evaluation episodes with subsets for held-out appearances, rotate-to-fit planning and occlusion memory, and 3,629 simulated demonstrations on which every learned policy is fine-tuned under an equal compute budget. The twin ranks policies as the real robot does: five policies trained without real data, four VLAs and an LLM agent, keep their exact ranking when the same weights run on the physical arm in an unseen environment with unseen objects (Spearman rho = 1.00, MMRV = 0.000), although simulation overestimates success. Across nine VLAs and world-action models, the best learned policies score near 61%, with spatial placement, unseen object classes and rotate-to-fit planning remaining open. An LLM agent that writes code and hands grasping to a learned policy scores 83.2%, and an ablation shows that this lead comes from the choice of harness and the choice of language model.

---


### 49. [Repulsive Population Policy Gradients for Behaviorally Diverse Reinforcement Learning](https://arxiv.org/abs/2610.36425)

**<font color=#1a73e8>作者：</font>** Saeed Hedayatian, Harsh Shah, Celine Mneimneh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The goal of Quality-Diversity Reinforcement Learning (QD-RL) is to find a population of high-performing policies that solve a decision-making problem in diverse ways. Despite recent progress, QD-RL methods predominantly rely on evolutionary operators--including black-box optimizers, mutations, and crossovers--to facilitate exploration and induce diversity. Scaling these methods becomes increasingly costly as policies and behavior spaces grow larger. Building on the Soft QD view of quality-diversity optimization, we introduce \textbf{Re}pulsive \textbf{P}opulation \textbf{P}olicy \textbf{O}ptimization (\textbf{RePPO}), which adapts PPO to jointly optimize a compact population of diverse, high-quality policies using a population-dependent, dynamically shaped reward. On standard continuous-control tasks, RePPO achieves a strong quality-diversity tradeoff compared with state-of-the-art QD-RL methods. Ablations further characterize this tradeoff by examining how each component affects individual quality and collective diversity. To assess RePPO's scalability, we extend our evaluation to learning from pixels and fine-tuning large language models. In pixel-based tasks, where large policies make most traditional QD-RL methods infeasible, RePPO maintains quality on par with standard PPO while achieving substantially higher diversity. Its successful application to language model fine-tuning further demonstrates, for the first time, that QD-RL methods can scale to this domain. Together, these results show that directly optimizing compact populations with RePPO provides a scalable approach to QD-RL across increasingly complex domains.

---


### 50. [LM-DSB: A Lightweight Multi-agent System for Automated Daily Safety Bulletin Generation in Construction](https://arxiv.org/abs/2610.36433)

**<font color=#1a73e8>作者：</font>** Xianxiang Zhao, Advik Mehta, Falak Sethi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Construction safety management still struggles to produce daily safety bulletins (DSBs), structured daily communications that identify site-specific hazards, convey safety protocols, and set preventive measures for workers. Manual DSB creation takes 2-3 hours daily and yields inconsistent quality, with 25% of crews never conducting pretask planning (Olson et al., 2016), diverting safety personnel from field supervision. This study proposes the Lightweight Multi-Agent DSB System (LM-DSB), which integrates retrieval-augmented generation (RAG) with a locally deployable Large Language Model (LLM) to automate DSB generation on consumer-grade personal computers. LM-DSB coordinates specialized planner, researcher, and writer agents in a hierarchical architecture, enhanced by domain-specific fine-tuning on construction safety documentation and RAG grounding in 37 health, safety, and environment (HSE) documents. A two-phase validation assessed feasibility. Phase 1 comparative evaluation showed the multi-agent RAG system (Llama 3-8B) outperformed all alternative configurations, with strong lexical alignment and coherence (TF-IDF: 0.70, BLEU: 0.39, ROUGE-1: 0.66) and near-complete document generation (length ratio: 1.01 vs. 0.39 for single-agent RAG). Phase 2 expert evaluation (N=40) confirmed practical acceptability (mean scores 3.50-4.20 on a 5-point scale), particularly in regulatory compliance (4.20) and factual accuracy (4.10). The findings show that architectural design enables lightweight models to handle safety-critical documentation on consumer-grade hardware, advancing technology democratization in construction safety management. Limitations include knowledge base scope, language constraints, and lack of field deployment validation; future work should address multimodal integration and workflow adoption.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-226](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

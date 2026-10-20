# 🧠 大模型相关研究 | 2026年10月21日

> 本类共 **548** 篇论文：已确认 **507** 篇，待复核 **41** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

---

### 351. [Can LLM User-Proxies Stand In for Humans in Reliance Measurement? Replicating Rel-A.I. with Simulated Users](https://arxiv.org/abs/2610.25788)

**<font color=#1a73e8>作者：</font>** Shuai Wang, Rui Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can language-model user proxies reproduce human reliance on an AI answer across contexts? Published simulated-user studies do not establish validity for this partial-answer decision, and Rel-A.I.'s released human record omits trial-level choices. We audit its 90 printed questions and 15 domain-by-marker reliance rates using sampled decisions and counterbalanced A/B probabilities from open models through 72B parameters. A matched crossover varies the printed agent specialty within each question, separating question content, label averages, and their interaction. Mistral Small's strong-marker math-minus-law label marginal is -0.4 percentage points, yet matching the agent label to the question domain raises reliance by 13.3 points on average across the five domains. The best A/B proxy has 22.5-point absolute-rate error and 8.3-point domain-effect error against the human table. A two-sample independent-binomial human replication has 3.5-point expected domain-effect error under the stated working model. The interaction is model dependent, and inference layout changes identical-prompt probabilities. This single-study audit does not establish proxy validity for human effect sizes or general directional screening.

---


### 352. [CoMem: Learning to Anticipate Failures from Retrieved Experience](https://arxiv.org/abs/2610.25790)

**<font color=#1a73e8>作者：</font>** Yun Shen, Ming Shen, Tianjun Yao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reflection lets LLM agents improve from their own attempts, but the memory it builds is local to a single task, so an agent reflecting on its own tends to revisit the same explanation for failure. Cross-task reflective memory addresses this in two forms: retrieved memory keeps past experience explicit and looks up related cases, which is specific but bounded by the bank, and parametric memory internalizes experience into parameters, which generalizes but is grounded in nothing beyond the task description. When both are used, existing agents combine them additively, feeding their outputs to the solver side by side, so retrieved experience never changes what the learned memory produces. We introduce CoMem (Compounding Memory), which makes retrieved experience an input to the learned memory itself, at training and at inference. The agent builds a bank of its own successful and failed reflections, learns from retrieved cases to write failure hypotheses, candidate explanations of how an attempt is likely to go wrong, and at test time reasons from newly retrieved cases to guide each attempt. Varying the retrieved cases gives the memory different perspectives, yielding reflective diversity that is not merely sampled but also grounded in retrieved experience. Across two backbones and five benchmarks in math, code, and multi-hop QA, CoMem achieves strong overall performance. Additional evaluations show that it generalizes to out-of-distribution tasks and enables smaller models to provide effective guidance to stronger solvers.

---


### 353. [Towards Architectural-Level Safety Control: Relocating Hazardous Knowledge into Removable Experts in Mixture-of-Experts Models](https://arxiv.org/abs/2610.25791)

**<font color=#1a73e8>作者：</font>** Cheng Jin, Zhongtian Ma, Xiao Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models acquire broad knowledge from web-scale corpora during pretraining, including knowledge that could be hazardous if misused. Removing such knowledge from the model itself without degrading general capability is desirable but difficult, as it is deeply entangled with general capability within the same parameters. Existing safety alignment and unlearning methods typically adjust these shared parameters, tending to suppress the expression of hazardous knowledge rather than remove it. As a result, the knowledge remains in the model and is readily recoverable by subsequent fine-tuning. To address this limitation, we propose REX (Relocating into Removable EXperts), a knowledge relocation method that separates hazardous knowledge from general capability at the architectural level. Exploiting the modular structure of Mixture-of-Experts models, REX expands the model with a set of new, physically removable experts designated to hold hazardous knowledge. Through expert expansion, selective gradient masking and routing differentiation, it relocates hazardous knowledge out of the original experts and concentrates it in the new ones. Excising these new experts yields a model suitable for public release. This removal holds consistently across Intern-S2, Qwen3.5-35B-A3B and Gemma-4-26B-A4B; on Qwen3.5-35B-A3B, for instance, excision lowers WMDP-Bio accuracy by 48.4 points while MMLU changes by less than 3 points. The excised model matches the strongest of nine unlearning baselines in removing hazardous knowledge, and it is the only one that preserves this removal under subsequent fine-tuning. After 250M tokens of standard fine-tuning on Qwen3.5, the best baseline rebounds on WMDP-Bio from 44.1% to 78.3%, whereas REX rises only from 32.4% to 42.8%.

---


### 354. [Communication-Efficient Federated Domain Generalization in Edge Networks via Dynamic Prototype Regulation](https://arxiv.org/abs/2610.25810)

**<font color=#1a73e8>作者：</font>** Yuankun Xia, Hui Wang, Ling Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is a distributed paradigm for Internet of Things (IoT) edge networks. However, deploying Vision-Language Models (VLMs) over wireless edge networks presents distinct challenges: large model parameters increase uplink transmission latency over bandwidth-constrained fading channels, and non-independent and identically distributed (Non-IID) data exacerbates client drift. Existing feature alignment solutions often introduce auxiliary computations that consume time slots allocated for wireless parameter transmission, increasing the likelihood of straggler dropouts under system delay constraints. To address these issues, we propose DPGR-GCAM, a communication-efficient federated domain generalization framework. By employing a dual-parameter-efficient fine-tuning (PEFT) architecture, we design a channel-aware tiered transmission mechanism that adaptively truncates payloads to maximize node survival rates under fading conditions. To mitigate client drift, we introduce the Gradient-Conflict Aware Modulation (GCAM) mechanism. GCAM operates within the low-dimensional feature manifold to dynamically resolve multi-objective optimization conflicts with minimal edge computation latency, thereby reducing computation-induced network outages. Experiments demonstrate that DPGR-GCAM improves cross-domain generalization and sustains convergence under network fading scenarios with a 10\% client participation rate.

---


### 355. [Is it RL or Data? A Controlled Comparison of GRPO and Rejection-Sampling Fine-Tuning](https://arxiv.org/abs/2610.25812)

**<font color=#1a73e8>作者：</font>** Lakshya Chaudhry  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bauer et al. (2026) showed that in low-data reinforcement learning with verifiable rewards, training GRPO on mixed-difficulty prompts gives up to 5x the sample efficiency of easy-only prompts. They did not test whether this benefit is specific to GRPO, or whether another post-training method given the same data would obtain it too. We test this on their procedural counting task with Qwen3-4B-Base and LoRA, comparing GRPO to rejection-sampling fine-tuning (RFT) on the same prompts, verifier and token cap. Six primary arms cross the two methods with three prompt sets (Easy, Mixed, and a Curated subset of prompts the base model sometimes solves, which makes GRPO's implicit filter explicit). We use three seeds per arm. Hypotheses and falsifiers were registered before training. To rule out a poorly tuned baseline, RFT receives a 27-run hyperparameter sweep, while GRPO uses Bauer et al.'s recipe unchanged. GRPO outperforms RFT at every prompt set: by 10.9 points on held-out test problems with curated prompts, and, in post hoc comparisons with matched rollout budgets, by 8.4 and 9.2 points on the easy and mixed prompts. On test the advantage survives the least favorable treatment of truncated completions; out of distribution, truncation prevents a conclusion. Curating prompts does not help RFT (-2.7 points). Mixed-difficulty data helps RFT (+3.7 points), while for GRPO the evidence is inconclusive. A secondary iterated-RFT arm, which resamples from the current policy, recovers 3.2 of the 10.9-point gap (about 30%). These are controlled measurements on one synthetic task family and one base model with three seeds per arm.

---


### 356. [Modal Sense Disambiguation in Language Models: The Role of Context, Training Domain, and Input Frequency](https://arxiv.org/abs/2610.25816)

**<font color=#1a73e8>作者：</font>** Ezgi Başar, Yevgen Matusevych, Annemarie van Dooren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modals such as may and must can take on different senses depending on discourse context, alternating between root interpretations (e.g., permission, obligation) and epistemic interpretations (e.g., knowledge, belief). While modals are known to be notoriously difficult for children to acquire, limited research exists on whether language models (LMs) can reliably distinguish between different modal senses. We evaluate seven LMs that vary in architecture, size, and training data type using vector-based similarity and surprisal measures across four datasets. Specifically, we investigate whether LMs can leverage contextual information to disambiguate modal senses and whether their performance reflects the distribution of modal senses in their training data. We show that larger LMs trained on diverse text successfully leverage additional contextual information when available. In the absence of context, they tend to favor the dominant sense based on corpus statistics. Smaller developmentally plausible LMs, including those trained on child-directed language (CDL), fail to show consistent sensitivity to modal sense distinctions and do not benefit from context to the same degree.

---


### 357. [When to Stop Asking: Factor Coverage Bias and LLM Determinability Judgments with Underspecified Information in Medicine](https://arxiv.org/abs/2610.25819)

**<font color=#1a73e8>作者：</font>** Yusuke Watanabe, Yohei Kobashi, Taisei Tosaki 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical decision-making often begins with underspecified information and requires not only gathering missing information but also knowing when to stop. This calls for judging determinability (whether the available information is sufficient for a decision) by considering whether missing information could change the conclusion, not simply the amount of available decision-relevant information. Reliance on this amount as a cue for determinability, which we term \textit{factor coverage bias}, could undermine the trustworthiness of large language models (LLMs) through premature conclusions or excessive information gathering, such as unnecessary invasive tests. Yet whether LLMs exhibit this bias remains insufficiently studied. To address this gap, we construct a controlled pairwise benchmark in which LLMs identify the determinable case within each determinable--undeterminable pair. We add a decision-relevant factor to either side while keeping each case's determinability unchanged, and similarly add irrelevant text to distinguish this bias from context-length effects. Adding a relevant factor made LLMs more likely to select the augmented case as determinable even when it remained undeterminable, an effect that persisted with increased reasoning effort, while adding irrelevant text made them less likely to select the augmented case, an effect that reasoning substantially reduced. These findings identify factor coverage bias as a failure mode distinct from context-length effects and a potential risk to LLM trustworthiness. Our work provides an evaluation framework for LLM trustworthiness under underspecification.

---


### 358. [When Retrieval Partially Conflicts with Skills: Understanding Procedural Hallucination in Language Models](https://arxiv.org/abs/2610.25827)

**<font color=#1a73e8>作者：</font>** Guanqun Jiang, Pengfei Cao, Kang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models increasingly use skills that provide reusable instructions and procedures for task execution. After a relevant skill has been selected, the model may need to apply its governing procedure together with retrieved task context. When the retrieved context is useful but contains cues that violate the skill, the model must retain compatible information while rejecting the conflicting cues. We study failures in which the model adopts such cues and produces a retrieval-supported but skill-invalid answer, which we call procedural hallucination. We introduce SourceClash, a matched benchmark with 1,271 bundles and 6,355 prompts across ten procedural domains. Each bundle fixes the task, skill specification, and answer space while varying the relation between the skill and retrieval. Across nine models, valid-answer rates average 25.7% under conflicting retrieval, compared with 78.2% and 72.8% under two supportive retrieval settings. Mechanistic analysis of open-weight models shows that the answer-preference difference typically reaches its maximum shortly after generation begins. Residual replacement moves the model toward valid answers, while attention decomposition attributes most of the repair to value vectors. Intervention at the identified value pathway also improves final answer validity. These results characterize how partly conflicting retrieval changes skill-guided generation.

---


### 359. [FrontierRefactor: Benchmarking Multi-Scale Performance-Oriented Codebase Refactoring](https://arxiv.org/abs/2610.25834)

**<font color=#1a73e8>作者：</font>** Shijian Wang, Fanqing Meng, Jiajun Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous codebase refactoring requires coding agents to restructure working software while strictly preserving externally observable behavior and prioritizing execution performance and compute efficiency over stylistic preference. Existing benchmarks: refactoring benchmarks assess functional correctness while overlooking runtime regressions, whereas code performance benchmarks target isolated micro-kernels that ignore codebase-scale complexity. We observe that refactoring scale is governed by the scope of the observable contract, the caller-visible interface fixing behavioral invariants while freeing private implementations for optimization. Building on this insight, we introduce FrontierRefactor, a benchmark of 60 qualified engineering tasks spanning four scales, from computational kernels to full repositories, across in-place optimization and cross-language rewriting. Evaluating frontier coding agents through a reference-free cascaded protocol across 1,080 execution runs reveals that correctness and speedup are largely decoupled: 41.2% of submissions satisfy functional equivalence yet fail to deliver verified performance improvements, with 19.3% suffering performance regressions and 21.9% trapped in measurement noise. Refactoring paradigms reveal orthogonal engineering bottlenecks: while cross-language rewrites gain speedups from native compilation after passing functional checks, agents struggle with contract fidelity, with pass rates dropping from 65.0% on modules to 32.6% at package scale; conversely, in-place optimization reliably preserves behavioral contracts at 86.5% but rarely achieves acceleration without physical performance profiling. Trajectory analysis shows that agents fall victim to uncalibrated micro-benchmarking illusions, an operational blind spot that multi-turn execution-timing feedback directly resolves, raising strict success from 16.0% to 40.0%.

---


### 360. [Diffusion Language Models Change Speed Across Tasks and Languages](https://arxiv.org/abs/2610.25835)

**<font color=#1a73e8>作者：</font>** Mohsen Fayyaz, Ali Modarressi, Daniel Israel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models can write several tokens in one forward pass, and they decide during generation how many passes to spend. Two outputs of the same token length can therefore vary a lot in cost. To understand the underlying factors of this cost variation, we analyze two diffusion models across 10 tasks. We find that the number of forward passes per token depends heavily on the task. Text copied or lightly edited from the input is cheap, while open-ended writing is costly. In DiffusionGemma, generating a token for story writing requires more than three times as many forward passes as for grammar correction. Two output properties explain much of this gap: how much of it is new relative to the input, and how rare its words are within the task. The same holds within a single response when thinking is involved. The final answer is cheap when it repeats the model's reasoning trace and costly when it adds something new. In multilingual generation, we find that highly tokenized languages also require more passes per token, adding to the cost they already pay with more tokens. Finally, cost tracks correctness: on the same math problem, wrong answers take more passes per token than correct ones, and weighting candidate answers by decoding speed beats majority voting by up to 4.2 points at no extra cost. Taken together, our results show that diffusion's computational advantage depends on how much of the output is already determined, while its decoding effort offers a practical signal for making inference more efficient and reliable.

---


### 361. [Where RL Breaks: Localizing and Repairing Failures via Targeted Continued Pretraining](https://arxiv.org/abs/2610.25836)

**<font color=#1a73e8>作者：</font>** Xinyi Wang, Danqi Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is widely used to improve reasoning in language models, yet growing evidence suggests that it mostly sharpens what the base model can already do. This raises a practical question: when RL fails, what is the base model missing? We look inside the RL policy's own rollouts and find that failures are localized: whether a rollout fails is strongly predicted by a small set of characteristic n-grams, ranging from reflection phrases such as "let's recheck" to specific operations such as "the inverse of A". These failures persist throughout RL training, although they are not beyond the model's reach: other sampled answers to the same question are often correct. Building on this observation, we use the failure $n$-grams to retrieve text from the pretraining corpus and continue pretraining the base model on it before RL. The resulting corpus has only 35M tokens, 3--4 orders of magnitude smaller than typical mid-training. We evaluate this approach on OLMo2 and Qwen3 models trained with RL on (1) GSM8K; (2) a mixture of math, commonsense, and knowledge questions; and (3) general math and science reasoning. Despite its size, the corpus yields consistent gains: our approach outperforms continued pretraining on the same amount of text sampled from the pretraining corpus across 10 out of 11 settings, including by $2.0$ points on GSM8K when inserted before mid-training. The retrieved text also transfers across model families: text retrieved for OLMo2-1B's failures improves Qwen3-4B on the mixture by $1.9$ points over the same baseline. Together, our results suggest that where RL fails is a cheap and effective signal for selecting pretraining data.

---


### 362. [Not Every Rollout Needs Distillation: Correctness-Filtered On-Policy Self-Distillation](https://arxiv.org/abs/2610.25842)

**<font color=#1a73e8>作者：</font>** Harrison Zhao, Lei Huang, Fei Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) supervises student-generated trajectories with a reference-conditioned version of the same base model. We ask whether every trajectory supplies distinct supervision that warrants its distillation cost. Gradient measurements on Qwen3-1.7B at initialization reveal that correct and incorrect responses have similar individual gradient magnitudes, but incorrect responses have approximately three times the coherent gradient share. Their estimated population-mean directions also largely overlap. A signal--noise model fitted at a small group size tracks alignment at larger group sizes without refitting. Motivated by these measurements, we introduce correctness-filtered OPSD (C-OPSD), which generates one response per problem and distills only a subset of incorrect responses. Removing unselected rows before both distillation forwards avoids their teacher/student forward and student backward work. Across Qwen3-1.7B, 4B, and 8B on AIME24, AIME25, and HMMT25, C-OPSD achieves on-par performance with full OPSD. In a measured micro-batch-size-four implementation, executed rows decrease by approximately 68%, and with retained rows packed into full micro-batches, training takes about 40% less time while rollout generation remains unchanged. Together, the measurements and training results connect outcome-conditioned supervision redundancy to more compute-efficient distillation.

---


### 363. [A Cue's Hidden Price: Auditing Seller Influence on AI Shoppers](https://arxiv.org/abs/2610.25843)

**<font color=#1a73e8>作者：</font>** Felix Buecheler, Gerardo Berbeglia, Mingyu Guo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly asked to shop on a user's behalf, which lets seller-controlled content such as badges, endorsements, and framing steer what they recommend. That poses the question at the core of generative engine optimization (GEO): not whether seller content shifts an agent's choice, but how much. The usual gauge of that influence, how often a cue wins the choice, has a blind spot: once a cue is strong enough to be picked almost every time, the choice rate can no longer show how much stronger one cue is than another. We introduce price-equivalent (PE) auditing, which removes this ceiling by pricing the cue in money. In a counterbalanced, position-controlled forced choice, we raise the cued product's price until it is chosen only half the time, and report that premium as the cue's price-equivalent: a formally defined, policy-conditioned parity threshold that makes very different cues comparable. Priced this way, cues that look equally strong at equal price differ by a wide margin, so choice-rate audits substantially under-resolve seller influence. We run the audit over 113,472 trials, seven models across families, and two product categories. To our knowledge, we also run the first price-equivalent audit of a decision-native model, Jev, which outputs a choice probability directly instead of generating text; strikingly, its profile is unlike any text model we tested, resisting most cues yet remaining susceptible to the strongest social-proof claims. We release the stimuli, logs, and code as a benchmark that reports each model's cue-price profile rather than a single score, giving developers and auditors a common, reproducible way to measure how content moves AI shopping agents.

---


### 364. [Measurement Validity and Representation Dynamics of Confidence Signals in Large Language Models](https://arxiv.org/abs/2610.25846)

**<font color=#1a73e8>作者：</font>** Debojeet Ghosh, Shreyansh Kumar, Ayushman Garg  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Whether a language model "knows what it knows" matters for trustworthy deployment and for deciding when it should abstain. Prior work usually measures this through one channel: verbalized confidence, a linear probe on hidden states, or agreement among sampled answers (semantic entropy), and often treats these as interchangeable. We compare all three in a pre-registered audit of five Qwen2.5 models (0.5B-7B, including a base/instruct pair at 7B) on factual retrieval (PopQA, SimpleQA) and multi-step reasoning (GSM8K, MATH). First, probes trained on prefill states to predict whether sampled answers will disagree become informative earlier for retrieval (about 7% of layer depth on average) than for reasoning (about 28%). The pre-registered five-layer test supported this only marginally; a finer 21-layer follow-up, designed after those results, supports it more clearly. In most retrieval cells, however, a prompt-only TF-IDF classifier matches the probe, so the early signal may reflect surface features of the question. Second, verbalized confidence is unstable: slightly different prompt templates yield scores that barely correlate. Third, Expected Calibration Error is misleading: verbal confidence looks well calibrated because it clusters near the base rate while discriminating poorly, whereas sampling agreement has worse ECE but about twice the resolution. Of five pre-registered hypotheses, two were falsified, one was partly supported, one was not supported, and one could not be tested because the base model's verbal confidence was degenerate.

---


### 365. [ACE-Trader: Adversarial Co-Evolution for Generator-Critic Trading Systems](https://arxiv.org/abs/2610.25847)

**<font color=#1a73e8>作者：</font>** Chang Zhou, Jiarun Zhou, Xingtong Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generator--critic trading systems pair an LLM-based trader that makes trading decisions with a red team agent that evaluates these decisions and provides feedback for revision. However, improving individual trading decisions does not ensure that both agents learn from experience and improve together over time. This raises an important question: how can the trader and red-Team select useful experience and learn from each other's evolving behavior? On one hand, experience that benefits decisions under one market condition may become ineffective or harmful under another. On the other hand, trading outcomes reflect both agents' actions, making it difficult to derive appropriate experience for each role. In this work, we propose ACE-Trader, an adversarial co-evolution trading framework. Specifically, we first develop separate context-dependent memory selectors that learn to identify useful experience for the current trading decision. Both selectors receive shared feedback from net-return differences between complete memory-assisted and memory-free trading pipelines, with online updates emphasizing recent outcomes. We further design a co-evolution mechanism that links role-specific memories through shared trading records. We use these records to evaluate the Red-Team's risk assessments and the effects of the Trader's revisions against realized market outcomes, then derive experience for their respective memories. By linking this experience to the corresponding records, we enable the Trader to improve its proposals based on prior critiques and the Red-Team to adjust its review focus as the Trader's behavior changes. Experiments on U.S. stock trading show that ACE-Trader outperforms all 22 active baselines in cumulative return and achieves the highest Sharpe ratio and lowest maximum drawdown across both active methods and passive benchmarks.

---


### 366. [Learning Who Talks to Whom: Role-Aware Communication Topology Scheduling for Efficient LLM Multi-Agent Collaboration](https://arxiv.org/abs/2610.25851)

**<font color=#1a73e8>作者：</font>** Haibin Li, Wenya Yu, Xuefeng Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems driven by large language models (LLMs) rely on structured communication topologies to facilitate information exchange and collaborative reasoning. However, effectively scheduling these topologies to dynamically determine who talks to whom and when to communicate remains a fundamental challenge in balancing collective reasoning performance against exponential token overhead. Existing topology scheduling approaches either enforce static communication graphs that cannot adapt to dynamic problem-solving states, or overlook agent role complementarity while failing to explicitly incorporate the synthesized graph structure into team-level decision evaluation. To tackle these limitations, we propose ACTS, a role-aware adaptive communication topology scheduling framework for efficient LLM multi-agent collaboration. Orchestrated within a Centralized Training with Decentralized Execution (CTDE) paradigm, ACTS introduces a novel dual-attention mechanism. Specifically, a Role-conditioned Relational Attention module dynamically selects variable-cardinality interaction partners based on agent roles and evolving execution states, while a Topological Attention Mixer explicitly embeds the directed communication topology into team value decomposition for precise credit assignment. Comprehensive evaluations across 9 challenging benchmarks covering code generation, multi-step reasoning, general knowledge, and competitive mathematics demonstrate that ACTS consistently outperforms state-of-the-art baselines, boosting average accuracy by up to 6.19 percentage points while reducing token consumption by over 15%. The project website is available at this https URL.

---


### 367. [Are Self-Evolving Agents Continual Learners?](https://arxiv.org/abs/2610.25858)

**<font color=#1a73e8>作者：</font>** Xiaoyin Chen, Yizheng Huang, Yinglun Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents are often deployed in environments where new knowledge, tools, and workflows keep arriving. Such an agent is therefore expected to adapt continually, learning new tasks as they arrive without forgetting earlier ones. This resembles the continual learning problem, but at a pace that conventional gradient updates cannot sustain. Nonparametric self-evolving agents are a natural alternative: they adapt by rewriting their own harness, such as prompts, memory, and skills, from task feedback while the model weights stay frozen. We study whether such agents are effective continual learners across four drifting task streams that shift in topic, workflow, or domain (built from BIRD, BFCL, and ScienceWorld). Evaluating three representative methods spanning experience retrieval and self-modification (ReasoningBank, GEPA, and Meta-Harness), we find that although self-evolution improves aggregate performance on most streams, higher plasticity consistently comes at the cost of stability. Specifically, self-modifying methods apply global edits to a shared prompt or workspace, interfering with unseen tasks and overwriting earlier knowledge as the stream shifts. Conversely, similarity-based memory retrieval localizes updates across distant domains, but still retrieves foreign memories on unseen tasks and suffers from retrieval collision when similar queries require conflicting workflows. These findings show that current self-evolving agents remain incomplete continual learners.

---


### 368. [Benefit-Targeted Routing and Bounded Revision for LLM-Based Evidence Screening in Manufacturing Supplier Discovery](https://arxiv.org/abs/2610.25867)

**<font color=#1a73e8>作者：</font>** Yijiashun Qi, Hanzhe Guo, Yuxuan Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An evidence-review system must allocate additional model judgments and control their use. We study these software decisions on 6,164 frozen manufacturing source-task pairs. Benefit-targeted routing learns recovered agreement minus newly introduced disagreement. On the original 300-case test, 60 consultations yield 202/231 agreements with two human references versus 189/218 for a logistic-risk router. An additional 300 cases were independently annotated twice using equal frozen evidence. Without retraining the historical policies, the corresponding counts are 164/190 versus 163/193; the differences do not resolve an advantage. Strict scalar-Ridge controls share preprocessing, regularization and fitting, and remain inconclusive. Quotation and requested-state replacement gates retain rejected cases and budget costs; their joint gate rejects one original and two additional consultations without changing primary outcomes. Evidence ablations, fusion and bounded updates supply further controls. A completed 200-pair identity audit yields 97.45 percent weighted merge precision after eight author adjudications. This audits a provisional map, while prospective company-disjoint performance remains untested.

---


### 369. [DeltaTrace: Efficient Signed Attribution for Reasoning Language Models](https://arxiv.org/abs/2610.25877)

**<font color=#1a73e8>作者：</font>** Chen Liang, Daoping Wu, Donghua Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how words in the context support or oppose a language model's response and present DeltaTrace, a novel attribution framework that explains the effect of input tokens on a fixed model response. DeltaTrace measures how the response's log-probability changes when the context tokens being explained are masked. To distribute this difference among source tokens, it constructs operator-specific local rules for finite changes and composes them backward through the computational graph using effective secant slopes. Each token is assigned a signed attribution as the inner product of its embedding displacement and the corresponding backward-propagated slope. Local conservation makes these contributions sum to the measured score difference and preserves their meaning when aggregated over sentences or passages. DeltaTrace supports both attention and linear-attention models, with auxiliary memory growing linearly with sequence length at fixed model dimensions and chunk size. On the evaluated attention model, DeltaTrace achieves the lowest deletion-faithfulness scores (RISE and MAS) on most retrieval and reasoning tasks and the highest needle-in-a-haystack Recall, exceeding FlashTrace by 5.67-24.33 percentage points. On the evaluated hybrid attention and linear-attention model, DeltaTrace lowers RISE on 9 tasks and MAS on 12 relative to FlashTrace.

---


### 370. [Asynchronous On-Policy Self-Distillation](https://arxiv.org/abs/2610.25880)

**<font color=#1a73e8>作者：</font>** Xidong Wu, Qi Qi, Yuqiong Ji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlike on-policy distillation (OPD), which depends on a separate teacher model, on-policy self-distillation (OPSD) leverages a single language model acting simultaneously as the student and the teacher, with the teacher conditioned on privileged information. Despite this architectural simplicity, synchronous rollout generation dominates overall training time, creating a severe systems bottleneck when scaling OPSD. To address this, we introduce Asynchronous On-Policy Self-Distillation (AsyncOPSD), a framework that decouples rollout generation from learner updates to improve training throughput. Since the teacher and student share parameters, AsyncOPSD eliminates the multi-model coordination overhead inherent to OPD architectures in asynchronous training. As the student policy evolves, buffered trajectories generated by older policies become stale, potentially degrading performance. To mitigate this, we introduce a distillation objective based on staleness-aware policy control and token-level entropy weighting. Across three model sizes and mathematical reasoning benchmarks, AsyncOPSD improves the training throughput by $1.96$--$2.25\times$ over synchronous OPSD while increasing average benchmark accuracy.

---


### 371. [Learn the Interface, Not the Implementation: Output Representation Dominates Training Regime in LLM-Based RTL Generation](https://arxiv.org/abs/2610.25881)

**<font color=#1a73e8>作者：</font>** Siddharth Patel, Vikram Singh, Siddharth Savyasachi Malu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-language-model register-transfer-level (RTL) generation has concentrated on how to train the model: fine-tuning, continued pre-training, and reinforcement learning from a verifier. We argue this is the second-order question. On a bounded, formally specifiable task of generating single-error-correcting, double-error-detecting (SECDED) ECC memory wrappers, we hold the task, data, and correctness oracle fixed and vary two axes independently: the training regime (seven settings) and the output representation (four levels, from fully expanded flat Verilog to an eight-field configuration expanded by a deterministic generator). Because a reference generator exists, correctness is decided by formal equivalence over a design space of approximately ten million points, rather than sampled from a hand-written testbench. Two results follow. First, representation dominates: every representation close to raw RTL reaches a pass rate of at most 0.17, while the configuration reaches 0.83 with no training at all. Once the model emits the configuration, every training regime achieves a pass rate between 0.89 and 1.00. Second, raw RTL hits a hard output-length limit: a 512-bit design requires 44,237 tokens of flat Verilog compared with just 69 tokens for the configuration. Consequently, raw generation becomes infeasible above 32-bit data words rather than merely inaccurate. A model trained from scratch with fewer than 50 million parameters, combined with the verified generator, achieves 0.89 formal equivalence, compared with 1.00 for a 32-billion-parameter fine-tuned model, while using approximately 1600 times less inference energy per correct design. Inference energy also dominates amortized training energy. The lesson is to learn the interface, not the implementation.

---


### 372. [An Analysis of Semantic and Spatio-Temporal Co-evolution for Edge Classification on Dynamic Text-Attributed Graphs](https://arxiv.org/abs/2610.25906)

**<font color=#1a73e8>作者：</font>** Tyler Bonnet, Marek Rei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic edge classification on text-attributed Web graphs, such as review networks, community forums, and news-derived knowledge graphs, requires high quality, adaptive semantic representations in the context of network evolution. Existing dynamic graph architectures typically initialize text feature vectors with pretrained language models and hold them static during training to preserve their semantic structure, forgoing the potential benefits of allowing them to co-evolve with network topology. In this work, we investigate the effects of enabling such co-evolution with a unified text-graph alignment framework that integrates a lightweight Transformer adapter to update token-level text representations via spatio-temporal gradients from a contrastive pretraining objective. To prevent detrimental semantic distortion, a language model maintenance objective anchors the evolving text embeddings to their original semantic structure. Evaluations on the Dynamic Text-Attributed Graph Benchmark demonstrate that this anchored text-graph co-evolution consistently improves upon the edge classification performance of frozen-text baselines across diverse Web-related domains. Representational analyses reveal that the framework reduces anisotropy, improving the linear separability of text embeddings, and effectively encodes structural and temporal information into the semantic space. A computational efficiency analysis confirms that this beneficial semantic and spatio-temporal co-evolution is achieved without incurring the prohibitive computational overhead typical of end-to-end joint training.

---


### 373. [CALM: Consistency-Aware Logit Masking in Decoding Space for Mitigating Overthinking of Large Reasoning Models](https://arxiv.org/abs/2610.25908)

**<font color=#1a73e8>作者：</font>** Shengjing Liu, Feiyang Li, Yuxuan Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) have achieved strong performance on challenging mathematical and scientific tasks through long chain-of-thought reasoning, but they often suffer from overthinking with unnecessary reasoning steps. Existing truncation-based methods typically detect consecutive trial-answer agreement and force early exit, yet such local stopping signals do not necessarily indicate final-answer stability and can disrupt useful subsequent reflection or verification, potentially leading to performance degradation. We propose consistency-aware logit masking (CALM), a training-free decoding intervention for mitigating overthinking in LRMs. CALM first monitors trial answers at step boundaries and then applies logit masking to action transition point (ATP) tokens such as "Wait", "Alternatively", and "Hmm", suppressing redundant transitional reasoning while allowing the model to continue its thought process more naturally. Experiments across four advanced LRMs and five benchmarks show that CALM reduces token consumption by 18.6%-25.0% compared with full CoT reasoning while maintaining performance, and can even improve accuracy by 0.07%-1.48% by reducing redundant reasoning. LLM-as-a-Judge results also demonstrate that CALM provides more coherent and concise results.

---


### 374. [FisherEdit: Fisher Information Guided Knowledge Editing for Large Language Models](https://arxiv.org/abs/2610.25914)

**<font color=#1a73e8>作者：</font>** Yizhou Yang, Jiahong Fu, Zhiwu Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sequential knowledge editing in Large Language Models (LLMs) often leads to a degradation of general capabilities due to cumulative parameter interference. In this paper, we revisit prominent projection-based methods like AlphaEdit and reveal a surprising mismatch: their robustness is primarily driven by update regularization rather than the intended null-space projection. Based on this insight, we propose FisherEdit, a theoretically grounded method built on Fisher geometry, which replaces coarse activation-space projections with importance-aware regularization in parameter space. It penalizes changes to sensitive parameters more strongly while retaining flexibility for new facts, and admits an efficient row-wise closed-form solution. Experiments on Llama-3, Qwen2.5, and Olmo-3 across multiple benchmarks demonstrate that FisherEdit achieves state-of-the-art performance while better preserving model stability and downstream task accuracy.

---


### 375. [LEAPS: Long-context Evaluation of Adaptive Pattern Learning and State Tracking](https://arxiv.org/abs/2610.25919)

**<font color=#1a73e8>作者：</font>** Howard Yen, Nitya Mani, Alex Renda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context language models (LCLMs) power agents that act over long trajectories, from improving a codebase to running research experiments to forecasters that condition on lengthy histories. These applications draw on three distinct long-context capabilities: recall, where the answer is a fact present in the context; state tracking, where the outcome can be computed by performing a series of transformations to a specified state; and pattern learning, where the goal is to make a prediction by sampling from a distribution inferred from many observations. Existing benchmarks primarily focus on the first capability. In this work, we introduce LEAPS (Long-context Evaluation of Adaptive Pattern learning and State tracking), a collection of 12 novel datasets, spanning agentic workflows, behavioral modeling, and forecasting of market and world events. By construction, LEAPS is resistant to data contamination, extends to millions of input tokens, and uses reliable metrics. We evaluate 30 API and open models from 8K to 512K input tokens. LEAPS distinguishes models that perform near perfectly on recall tasks, finding that such models' state tracking and pattern learning abilities can vary significantly and degrade much more dramatically with increasing input lengths--even for pattern learning, where more observations should make learning a theoretically easier task. Moreover, thinking models often underperform their base counterparts, exhausting their generation budget or oversimplifying the task. We hope LEAPS can guide the development of the next generation of LCLMs.

---


### 376. [Maestro: Agentic Formal Proof Development by Coordination](https://arxiv.org/abs/2610.25920)

**<font color=#1a73e8>作者：</font>** Haoyu Li, Zeren Shui, Yuhao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lean is increasingly used to verify mathematical proofs and software produced by LLM agents, but writing formal proofs remains hard. Existing prover systems take a divide-and-conquer approach that recursively decomposes hard proof obligations into easier lemmas and splits again any lemma that resists proof. However, a lemma can resist proof for different reasons, including insufficient guidance, a false statement, or a flaw in the decomposition that produced it. Existing systems cannot tell these apart as a failed attempt reports little beyond its failure, and responses are confined to the failing node without considering the rest of the proof or revising the plan above it. The system may thus keep decomposing obligations along a flawed proof direction until the budget runs out, causing the whole proof attempt to fail. We introduce Maestro, a Lean prover harness that handles failures through global coordination. Provers report why they failed, not just that they failed, and a coordinator that sees the whole proof chooses an appropriate response, such as guiding a stuck prover, correcting a false lemma, or retracting a flawed subtree and replanning it. The same harness extends to verified code synthesis, where a checked counterexample sends the code back for repair. We evaluate Maestro with four frontier LLMs on seven mathematics and three software verification benchmarks. It proves more targets than each model's native coding agent (Claude Code or Codex) on every benchmark the agent has not already saturated, with the largest gains on research-level mathematics. With Claude Opus 5, it discovers its own proofs of 34 of the 48 theorems in the June 2026 release of arXivLean, against 19 for the native agent. It also outperforms all published prover systems on every benchmark they share, solving 669/672 PutnamBench, 59/60 Lean-IMO-Bench, and 6/6 IMO 2026.

---


### 377. [SAPO: Self-Supervised Attention Policy Optimization for Improving Temporal Video Grounding in Vision-Language Models](https://arxiv.org/abs/2610.25923)

**<font color=#1a73e8>作者：</font>** Zixuan Chen, Depeng Wang, Wei Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video vision-language models (VLMs) have strong semantic understanding, yet remain unreliable at precise temporal grounding. Existing gains from explicitly aligning video frames with absolute time suggest that VLMs may already encode accurate temporal locations internally but lose precision when expressing them as timestamps. Our analysis across four VLMs and two grounding datasets confirms this hypothesis: attention intervals outperform predicted intervals on approximately 66% of valid examples. We term this discrepancy the temporal generation gap. Because precise temporal annotations are expensive, this finding motivates closing the gap to improve temporal grounding using only unlabeled video-query pairs. We propose Self-Supervised Attention Policy Optimization (SAPO), which uses internal temporal attention as self-supervision for Group Relative Policy Optimization and applies a ground-truth-free criterion to select high-value samples. SAPO consistently improves temporal grounding across multiple datasets and models spanning weak to strong initial grounding ability. Relative mIoU gains reach 33.7% on Qwen2.5-VL-3B and 5.4% on the strong Time-R1-7B. The improvements transfer across datasets while preserving general video understanding.

---


### 378. [UtilityBench: Measuring Language Model Utility When Errors Have Different Costs](https://arxiv.org/abs/2610.25924)

**<font color=#1a73e8>作者：</font>** Qifeng Lei, Zhiyong Yang, Zitai Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As language models are increasingly deployed in real-world scenarios with important outcomes, the impact of their mistakes often extends far beyond what correctness can capture. In domains like medicine, a single error can lead to serious consequences and put patient safety at risk. However, mainstream evaluation protocols still treat all errors as equal, overlooking the spectrum of real-world costs. To address this, we propose a utility-based evaluation paradigm that explicitly incorporates the varying consequences of errors. Guided by this principle, we develop UtilityBench, a large-scale benchmark of 15,000 instances with verifiable answers, quantifying error severity using Best-Worst Scaling to elicit meaningful, data-driven cost estimates. These quantified utilities shape when a model should answer or abstain, guiding it to make decisions that align with the true importance of each scenario. As another merit, we introduce UtilityAUC, a metric that measures the area under the utility curve determined by a model's response ordering, thereby enabling utility preference alignment beyond error frequency. Our theoretical analysis demonstrates that UtilityAUC can distinguish between models where standard accuracy and AURC fall short. Empirically, evaluating 20 state-of-the-art models, we find that greater accuracy or more advanced architectures do not reliably translate to higher UtilityAUC, highlighting a gap between problem-solving ability and responsible decision-making in language model evaluation.

---


### 379. [MIRA: A Multimodal Illustrated Deep Research Agent for Controllable Reports](https://arxiv.org/abs/2610.25926)

**<font color=#1a73e8>作者：</font>** Hongrui Wu, Kaiwen Tuo, Congcong Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep research agents are increasingly capable of searching the open web and synthesizing evidence, yet they remain poorly suited to controllable report generation in multimodal deep research. This task requires agents to handle interleaved textual and visual inputs, gather multimodal evidence through multi-step web search, and deliver comprehensive illustrated reports under user-specified requirements. Existing systems face two limitations. During reasoning, they often underuse images discovered along the search trajectory; during generation, they tend to produce fixed-form answers with limited control over report granularity, multimodal composition, and evidence grounding. We introduce MIRA, a Multimodal Illustrated Deep Research Agent for controllable reports. MIRA integrates textual and visual evidence throughout research and writing. At its core, MIRA-Harness translates user requirements into generation contracts and connects four stages: evidence collection, report submission, feedback-driven revision, and final delivery. Building on this harness, MIRA-Data constructs high-quality multi-hop multimodal research trajectories, and we post-train foundation models to operate within the workflow. Using Qwen3.6-35B-A3B, MIRA achieves state-of-the-art performance among open agents on 7 representative, established multimodal-search and deep-research-agent benchmarks, while producing user-aligned illustrated reports with traceable textual and visual evidence.

---


### 380. [CondenseVLA: Learnable History Condensation for Efficient Multi-Frame VLA](https://arxiv.org/abs/2610.25927)

**<font color=#1a73e8>作者：</font>** Feiyang Hong, Yujie Wei, Bo Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robot manipulation often depends on short-term cues - such as brief contacts, temporary occlusions, and intermediate object states - that are ambiguous in a single frame and can only be resolved by integrating observations over time. However, injecting historical information solely by enlarging the history window is computationally costly and frequently yields limited gains due to substantial redundancy and task-agnostic, inflexible sampling of observations. We propose CondenseVLA, a multi-frame VLA policy with a learnable decoder-side history condensation module for using short-term visual context in action decoding. Given a sequence of cached per-frame features from the VLM backbone, CondenseVLA distills observation history into a fixed set of slot tokens using learnable queries and multi-head cross-attention. Simple auxiliary regularization penalizes overlap among slot attention maps and decorrelates slot embeddings, encouraging complementary attention and reducing slot redundancy. Across the evaluated tasks, CondenseVLA improves Simpler-WidowX success from 58.7% to 69.8% (+11.1 percentage points), achieves 97.2% on LIBERO, and reaches 52.8% on real-world tasks. It achieves 21.6% success on memory-dependent RMBench tasks. These results support selective condensation of bounded recent visual evidence for action decoding, while harder multi-observation tasks expose the limits of a finite history window. Project page: this https URL

---


### 381. [OmniGround: Strengthening Omni-Modal Temporal Grounding via Attention-Consistency Training](https://arxiv.org/abs/2610.25929)

**<font color=#1a73e8>作者：</font>** Zixuan Chen, Depeng Wang, Hao Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models can jointly understand video, audio, and text, yet they remain weak at temporal grounding, a capability essential for real-world audio-visual applications. To understand this limitation, we look beyond final predictions and examine the model's internal temporal evidence. We identify a temporal generation gap: the internal attention of the model localizes the target moment more accurately than the timestamps it generates. To close this gap, we propose TACG (Temporal Attention-Consistency Grounding), a post-training method that treats internal attention as a reliable temporal pivot and aligns it with both the model prediction and the ground-truth annotation through attention-consistency training. We further build a 580K-sample training dataset by reconstructing temporal QA from dense audio-visual annotations and organizing general omni-modal instruction data. Using TACG and this training dataset, we train OmniGround, a general-purpose omni-modal model with stronger temporal grounding capability, without injecting any additional temporal cues. OmniGround reaches state-of-the-art omni-modal temporal grounding, including 37.5 mIoU on LongVALE and 35.7 mIoU on UnAV-100, while staying competitive on both general audio-visual understanding and vision-only grounding.

---


### 382. [TESS: LLM-guided Translation, Exploration, Simulation, and Search for Embodied Task Planning](https://arxiv.org/abs/2610.25930)

**<font color=#1a73e8>作者：</font>** Peiran Xu, Yixiang Yang, Jinghan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this work we focus on the problem of embodied task planning, which requires an agent to accomplish a complex task by separating it into atomic actions. Recent studies have developed LLM-based methods to address this problem. However, the executability and correctness of the generated plans remain suboptimal in complex environments and tasks. On the other hand, classical search algorithms have the potential to solve the planning problems perfectly, yet they require fully observable environments, known state transitions and goal state, which are often unattainable in general task domains. Therefore, we propose to implement an LLM-guided search algorithm that makes the search process possible and efficient by incorporating LLMs' commonsense knowledge. Our method leverages LLMs to (1) translate natural language instructions into formatted goal conditions, (2) facilitate efficient exploration in partially observable environments, (3) implement a rule-based world simulator, and (4) prune the space of candidate actions to improve search efficiency. Experimental results on VirtualHome and ALFWorld demonstrate its superior performance.

---


### 383. [EvoSkill v2: Fully Agentic Skill Evolution from Benchmark Adaptation to a Stateful Evolver](https://arxiv.org/abs/2610.25931)

**<font color=#1a73e8>作者：</font>** Dastin Huang, Baran Nama, Salaheddin Alzubi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> EvoSkill v2 is a three-agent system that edits the instructions (skills) an agent is given, leaving its model and harness intact. The user starts a run by describing a benchmark and supplying a grader, which a benchmark adaptor turns into a benchmark-specific plugin. A solver attempts the tasks, and an evolver reads the solver's training rollouts and rewrites the skills at each epoch. We implement the evolver as one stateful coding agent with a bash tool for the whole run, unlike the two most common designs among the skill optimizers we surveyed: a sequence of single model calls, as in SkillOpt, and an agent that starts afresh each round, as in SkillBoost. We also measure how much the solver's rollouts vary from one attempt to the next, give the evolver several attempts per training task, and accept every epoch's skills instead of selecting among them on noisy scores. With fine-grained ground truth, EvoSkill v2's skills raised the held-out pass rate above the stronger of SkillOpt and SkillBoost by 7.7 percentage points on SpreadsheetBench v2 and by 5.4 on $\tau^3$-bench banking. In both benchmarks and both feedback settings, EvoSkill v2's evolver cost less per percentage point of held-out pass rate gained than either baseline's optimizer. EvoSkill v2 also enables a less capable model to improve its own skills, demonstrated by a gain of up to 21.5 percentage points in the $\tau^3$-bench banking experiment where Claude Haiku 5.5 powers both solver and evolver.

---


### 384. [Keep the Lineages Alive: Diversity-Preserving SMC for Diffusion LLM Decoding](https://arxiv.org/abs/2610.25932)

**<font color=#1a73e8>作者：</font>** Minoo Ahmadi, Seyedarmin Azizi, Mehdi Kamal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time sequential Monte Carlo (SMC) decoding can improve the reasoning accuracy of masked diffusion language models (diffusion LLMs) without post-training by resampling a population of partial generations according to a reward. Its effectiveness therefore depends on the resampling step, which must concentrate computation on promising candidates while retaining enough diversity to explore alternative reasoning paths. The reward can be internal, the decoder's own confidence on the committed prefix, or external, a process reward model scoring that prefix. Under either reward, multinomial resampling can disrupt this balance by duplicating high-weight particles and discarding lineages that may still reach a correct solution. The effective sample size (ESS) does not register this loss: multinomial resampling resets it to its maximum even as distinct lineages disappear. To retain such lineages, we introduce lineage-preserving SMC (LP-SMC), which combines Chopthin resampling with an input weight floor. Instead of equalizing weights, Chopthin bounds the ratio between the largest and smallest weights it returns and carries the unequal weights forward. The floor limits how far below the maximum a weight may fall before resampling so that lineages with low early weight keep a chance to recover. Across mathematical-reasoning and code-generation benchmarks on two base models, LP-SMC raises oracle coverage, the fraction of problems with at least one correct particle, in every setting, by 1.8 to 25.6 points, and raises end-to-end accuracy under a common reward-model selector in eleven of twelve settings, by up to 7.9 points on LLaDA-1.5 and 18.3 on Dream-7B. The coverage gain persists under the external reward model, which suggests that diversity-preserving resampling and the guidance signal contribute separately to inference-time search.

---


### 385. [The KV-Surgeon: Compensation-Aware Offline KV-Cache Compaction](https://arxiv.org/abs/2610.25933)

**<font color=#1a73e8>作者：</font>** Moritz Wagner, Christophe Roux, Max Zimmer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline compaction of the key--value cache (KV-cache) reduces the cost of repeatedly querying a fixed context by constructing a smaller cache once and reusing it subsequently. The central challenge of compaction is deciding which cache entries to delete and which to retain. Existing methods score each candidate for deletion on its own, with the rest of the cache being held fixed. However, softmax renormalization of the attention operation couples these decisions in a nonlinear manner: removing one entry changes the attention weights of every remaining one. In this work, we introduce KV-Surgeon, which uses calibration data to take interactions into account in a tractable way. We derive a quadratic surrogate that admits closed-form expressions for jointly making the optimal greedy removal decision as well as compensation within the remaining entries. On QuALITY, LongHealth, and Long Code Arena, and at every evaluated compaction ratio, KV-Surgeon substantially advances the cost--accuracy Pareto frontier of dense and mixture-of-experts models from 4B to 30B parameters. At $50\times$ compaction, KV-Surgeon improves question-answering accuracy by up to four points over attention matching (Zweiger et al., 2026), the state of the art, at comparable cost. Lastly, we introduce an even faster variant, which also exceeds the state of the art while requiring only two fifths of its cost.

---


### 386. [MITRA-lexicon: Lexica of attested translations from Sanskrit into English, Tibetan and Chinese](https://arxiv.org/abs/2610.25934)

**<font color=#1a73e8>作者：</font>** Sebastian Nehrdich, Kengo Harimoto, Sven Sellmer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The standard Sanskrit lexica are monumental and indispensable, but they cite their attestations as abbreviated references to editions, without links to the digitized texts now widely available and without a translation of the passage, and they naturally do not reflect translations made after them. To address these gaps, we present MITRA-lexicon, a family of corpus-grounded lexica based on span annotations of translation equivalents with Sanskrit as the pivot: Sanskrit-English, derived from the Mitrasamgraha corpus, as well as Sanskrit-Tibetan and Sanskrit-Chinese, derived from the MITRA-parallel corpus of Buddhist literature. In total, the resource comprises 2.18 million headword entries in six directional lexica. Headwords are lemmas and compounds from silver annotations that follow the Digital Corpus of Sanskrit (DCS). Senses are ranked by frequency, and each of the 10.4 million attestations includes its sentence pair, with character offsets of the word and its equivalent. We propose a multi-step pipeline based on grammatical annotation models, fine-tuned large language models, and a teacher-student setup to produce the alignments. We evaluate the lexica against reference dictionaries and manually corrected gold alignments. We release the lexica and the fine-tuned span annotation model, together with a web interface for looking up headwords and their attested senses.

---


### 387. [Speech LLMs That Breathe: Modeling Non-Verbal Vocalizations in Dialogue](https://arxiv.org/abs/2610.25942)

**<font color=#1a73e8>作者：</font>** Heyang Liu, Lixin Zhang, Jiayi Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The user experience of speech interaction models has improved, benefiting from the modeling of paralinguistic attributes and advances in speech reconstruction paradigms. However, human communication follows extensive norms regarding non-verbal vocalizations (NVVs) spanning respiratory, affective, and discourse. The omission of these events imposes inherent limitations on the naturalness of current approaches. In this work, we cover 13 major types of NVVs and construct a natural dialogue dataset that conforms to human conversational norms through an automated synthesis pipeline. We enhance the ability of speech interaction models to generate contextually appropriate NVV events through multi-stage fine-tuning and NVV-aware GRPO (Group Relative Policy Optimization). Based on distinct modeling paradigms, we substantially improve the expressiveness of VocalNet and VITA-Qinyu in empathy interactions and role-play dialogues, and further discuss the architectural necessity for achieving high-quality natural speech generation.

---


### 388. [OrderGPT: Generation Order as a Learnable Modeling Choice](https://arxiv.org/abs/2610.25949)

**<font color=#1a73e8>作者：</font>** Chenhe Yang, Yuhuan Lyu, Tianyang Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative modeling of discrete data has two popular paradigms: autoregressive models such as GPT, which factorize a sequence in a left-to-right (L2R) order, and masked diffusion models, which are essentially any-order autoregressive modeling. Rather than competing methods, these are the two extreme points of a single axis -- the generation order. For structured discrete domains without a natural traversal, both extremes may be suboptimal, yet the intermediate choice -- a single well-adapted order -- remains largely unexplored. We introduce OrderGPT, which builds on Any-Order GPT to learn a task-level generation order without canonical-order supervision. Our key observation is that predicting variables from randomly sampled reveal prefixes produces recurring attention patterns in the backbone that provide a model-dependent signal of predictive dependencies. We aggregate this signal into a reciprocal dependency graph and use a spectral teacher to derive continuous generation priorities. A lightweight OrderMLP integrated into the GPT backbone learns to predict these priorities from attention, incorporating order learning into the architecture within a single training run. Training gradually shifts toward the learned order, which is then frozen for subsequent autoregressive training and generation. The same mechanism adapts across modalities: adaptively it recovers near-L2R dependency structure in language, learns anatomically organized factorizations on human pose, and discovers a factorization on tabular data that places statistically and semantically related fields nearby, while improving downstream modeling metrics across all domains. The code is available at this https URL.

---


### 389. [AdaExploreBench: Benchmarking LLM Agents for Proactive Exploration and Test-time Adaptation in Evolving Environments](https://arxiv.org/abs/2610.25950)

**<font color=#1a73e8>作者：</font>** Rui Wang, Zishen Lai, Jiayu Liu 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly deployed in unfamiliar and evolving environments, requiring them to proactively explore, understand, and adapt to environmental dynamics. However, existing benchmarks rarely test whether agents can proactively discover how an environment works and adapt as it evolves. To address this gap, we introduce AdaExploreBench, a benchmark for proactive exploration and test-time adaptation in evolving environments. By instantiating environmental dynamics as hidden rules, AdaExploreBench requires agents to actively acquire evidence and infer the rules. Under implicit rule drift, the latent rule changes without announcement, requiring agents to detect from degraded performance that prior knowledge is stale and re-explore. Experiments on eight leading LLMs show that proactive and adaptive exploration remain challenging: GPT-6 Sol achieves only 61.9% calibrated accuracy, while providing sufficient evidence or removing rule drift improves average performance significantly by close to 10%. These results reveal a critical bottleneck in current LLM agents: they can often reason effectively from informative evidence once it is available, but struggle to actively acquire the right evidence and recognize when previously acquired evidence is no longer valid.

---


### 390. [CXBench: A Benchmark for Process-Compliant LLM Agents in Regulated Customer-Experience Workflows](https://arxiv.org/abs/2610.25954)

**<font color=#1a73e8>作者：</font>** Boxi Yu, Yuzhong Zhang, Zhenfeng Su 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using language agents increasingly perform regulated customer-service workflows, where a correct final state is insufficient: agents must also provide disclosures, obtain consent, and follow required procedures. Existing tool-agent benchmarks largely score final business states, accepting trajectories that reach correct outcomes through non-compliant processes.
We introduce cxbench, a benchmark that evaluates outcome and process compliance separately across six regulated domains. Each task combines a customer request, a tool-based environment, and explicit process requirements. Rule cards link cited regulatory obligations to observable trace evidence. A hybrid grader combines deterministic checks for ordering and authority with an LLM judge for semantic requirements. We define a false-pass as an outcome-pass run that fails process checks.
Across seven models and 120 tasks, 55.5% of the 840 retained executions are false-passes, representing 80.1% of outcome-passing runs; only 13.8% pass both checks. Process-inclusive evaluation changes the observed model ordering and exposes differences hidden by outcome-only scoring. cxbench makes these failures inspectable through trace-linked criteria.

---


### 391. [Productive State-Space Exploration for Multi-turn RL in LLM Agents](https://arxiv.org/abs/2610.25957)

**<font color=#1a73e8>作者：</font>** Mohammed Haroon Dupty, Yong Liang Goh, Song Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) for Large Language Model (LLM) agents in multi-turn, long-horizon environments remains challenging due to inefficient action selection and repetitive behavioral patterns. In particular, agents often become trapped in high-confidence yet unproductive behaviors, repeatedly executing invalid actions or entering action loops that hinder task completion. We observe that these frequently violate environment preconditions, revealing a mismatch between the agent's representation of the internal state and the dynamics of the underlying environment. In addition, repetitive high-confidence actions lead to cyclical behaviors that provide little to no progress towards the goal. We argue that addressing these challenges requires more productive task-aligned exploration to improve the agent's understanding of environment dynamics. Motivated by intrinsic curiosity-driven exploration, we propose a conditional state-space exploration framework that balances task completion with intrinsic information-seeking behavior. Specifically, we introduce an intrinsic reward that penalizes actions whose observation duplicates prior state memory. This provides the benefit of reducing redundant behaviors and encouraging state-space coverage without relying on a general information-theoretic measure. Strong experimental results demonstrate that our approach substantially improves policy learning in multi-turn environments, mitigating invalid actions and repetitive loops.

---


### 392. [ABACUS: Program-Guided Multistep Reasoning over Frozen Judgment Models](https://arxiv.org/abs/2610.25963)

**<font color=#1a73e8>作者：</font>** Yuhao Wang, Zelin Zang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Judgment models answer semantic questions by scoring a finite set of candidate outcomes. Can reusable programs turn these local decisions into powerful multistep reasoning? We introduce \method, a framework that jointly constructs judgment schemas and composition programs for frozen judgment models. A generative teacher designs the procedure offline; the judgment model resolves local semantic questions online, and the saved program composes its decisions into an answer. We study three allocations of design effort between humans and the teacher, focusing on construction through a shared interface. We instantiate the framework with Kev. On three selected BIG-Bench Hard tasks, nine independently constructed programs solve all 450 executions of 150 development inputs. A separate deployment study freezes three programs after development-set reference-agreement refinement and evaluates them on 600 held-out questions. These programs achieve near-perfect 99.67\% macro accuracy, versus 64.00\% for direct Kev and 68.80\% for final-answer-only Qwen3.5-4B. They attain comparable observed accuracy to Qwen's unrestricted response policy (99.07\%) with an \textbf{8.43-fold online speedup}: 0.255 versus 2.150 seconds per question. These results show how reusable programs can substantially expand the reasoning capability of a compact judgment model while keeping its parameters fixed.

---


### 393. [Token-Set Choice Confounds POPE: A Systematic Audit of Yes/No Extraction in VLM Hallucination Evaluation](https://arxiv.org/abs/2610.25964)

**<font color=#1a73e8>作者：</font>** Kesav Kumar Jayakumar, Karthigeyan Thilak  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We set out to reproduce a recent hallucination-mitigation result on the POPE benchmark. The LLaVA-1.5-7B baseline we measured, 82.21 F1 on the adversarial split, sat 1.21 to 8.67 points above the adversarial baselines we planned to compare against (81.00, 79.30, and 73.54). We looked at the evaluation code and found a readout choice that moves F1 on its own. A two-token logit readout decides yes versus no by comparing two vocabulary IDs, 3582 ("yes") and 1217 ("no"). Across 9,000 greedy-decode questions spanning all three splits, neither ID is generated even once. The model emits " Yes" (token 3869) and " No" (token 1939), because SentencePiece prepends a space byte after the prompt suffix "ASSISTANT:". Read with an eight-token lookup that covers the space-prefixed surface forms, LLaVA-1.5-7B scores F1 0.8221, 0.8498, and 0.8713 on the adversarial, popular, and random splits. That 6.13-point adversarial shift exceeds the adversarial gain reported by five of the six papers we surveyed. None of them states its readout, and our reference ran under 4-bit NF4 quantization, so we cannot say how much of any reported gain a matched evaluation would keep. That comparison stays unresolved until readout and precision are matched. On the fixed baseline we run nine inference-time corrections of our own (none beat it) and dissect why the adversarial split resists logit-level intervention. In a 3,000-question probe, wrong predictions draw more image attention than correct ones (Cohen's $d=-0.46$, $p=1.4\times10^{-24}$), the opposite of what grounding-based corrections assume. A four-readout audit across four further VLMs from three tokenizer families confirms the confound is protocol-level, not model-specific: porting the LLaVA-1.5 IDs verbatim drops F1 to 0.00 on the two disjoint-vocabulary models, whereas a tokenizer-derived readout holds between 0.80 and 0.92.

---


### 394. [Behavioral Probes for Information Flow in LLM Swarms](https://arxiv.org/abs/2610.25966)

**<font color=#1a73e8>作者：</font>** Junhui Chen, Yu Zhang, Lantian Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Most existing approaches to LLM swarm optimization are utility-driven, focusing on final task utility while leaving the processing, integration, and reliance of information within individual interactions largely implicit. To address this, we study LLM swarm interactions from an information-flow-based view and introduce behavioral probes to quantify information flow patterns. Specifically, we repurpose External Context Score (ECS) and Parametric Knowledge Score (PKS)---originally designed for hallucination analysis---to measure a node's external-context dependence and parametric-knowledge dependence, respectively. Across controlled and realistic swarm settings, we observe consistent patterns: ECS increases with input relevance and distinguishes useful multi-source contributions, while PKS decreases as informative context accumulates. Building on this heuristic interpretation, we demonstrate how these probes can complement utility-driven structure optimization in two controlled applications. Probe-guided node pruning reduces redundant communication and token consumption, and probe-guided reasoning-path search accelerates convergence compared to utility-only baselines. Our empirical results suggest that behavioral probes can make the internal information flow of LLM swarms observable and serve as effective auxiliary signals for structure optimization.

---


### 395. [Correctness-Dependent Asymmetric Target Distributions for Self-Distillation Policy Optimization](https://arxiv.org/abs/2610.25973)

**<font color=#1a73e8>作者：</font>** Suwan Yoon, Seongryong Jung, Changhee Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-distillation policy optimization provides dense token-level supervision for LLM post-training through feedback-conditioned self-teachers. However, directly matching the self-teacher can disrupt successful behaviors on correct rollouts while providing insufficient correction on incorrect ones. We propose Asymmetric Policy Optimization via Self-Distillation (APSD), which constructs correctness-dependent targets by mixing student and self-teacher distributions: interpolation preserves successful behaviors on correct rollouts, while extrapolation beyond the self-teacher strengthens correction on incorrect ones. We analyze APSD through divergence decomposition, reverse-KL barycentric geometry, and gradient analysis, highlighting the importance of gradient flow through student-dependent targets. Experiments under reinforcement learning with verifiable rewards and rich feedback show that APSD achieves strong overall performance against reinforcement-learning and self-distillation baselines and matches SDPO performance with 2.6x fewer training steps on average across Qwen3 model scales.

---


### 396. [GraphEvoResearcher: Graph-Aware Training-Free Self-Reflective Reasoning for Cost-Bounded Multi-Hop Question Answering](https://arxiv.org/abs/2610.25978)

**<font color=#1a73e8>作者：</font>** Suxing Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-hop question answering (QA) requires models to chain intermediate conclusions while remaining cost-aware. Existing training-free self-reflective protocols (generate -> critique -> revise) improve accuracy but operate on a flat token stream: revisions cannot identify which prior step is unreliable, and early stopping cannot exploit structural convergence. We introduce GraphEvoResearcher, a training-free protocol that lifts EvoResearcher's self-reflective meta-reward onto an explicit reasoning graph - nodes are intermediate conclusions/evidence and edges encode support, contradict, and depends_on. A graph-aware meta-reward combines correctness, efficiency, reflection, diversity, and four structural signals (connectivity, acyclicity, branch coverage, path convergence) to decide whether to revise, backtrack, or stop. A graph-convergence early-stop terminates when evidence branches converge on a single conclusion. On a real LLM (DeepSeek), over GSM8K, MATH, and BBH (n=50 each), GraphEvoResearcher reaches 98%, 92%, and 82% respectively, the highest of all baselines, with the largest gains on the hardest set (MATH: +24 pp over single-shot, +12 pp over flat reflection), while keeping construction cost bounded at ~2 steps / 4.5-5 nodes. Our results indicate the structural signal of a reasoning graph is most valuable exactly where single-step reasoning is unreliable.

---


### 397. [ClueFlow: Learning Long-Horizon Search through Attributed Research-State Transitions](https://arxiv.org/abs/2610.25980)

**<font color=#1a73e8>作者：</font>** Yicheng Wang, Wentao Tan, Yidan Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon search requires agents to acquire relevant evidence and integrate it into an evolving research state. Existing methods maintain research states to guide exploration or assign turn-level progress signals, yet grounding these signals in explicit, attributable state changes remains underexplored. We introduce ClueFlow, which learns long-horizon search from attributed research-state transitions. ClueFlow constructs Source-State-Final attribution chains that connect evidence-acquiring browser actions, Evidence and Candidate updates, and the final answer supported by those updates. During search, ClueFlow records typed state changes and potentially supporting browser actions, then applies gold-conditioned semantic validation and source tracing after execution. We use this attribution to guide both supervised fine-tuning and reinforcement learning. During SFT, attribution selects which decisions receive supervision with their original interaction contexts. During Turn-PPO, the same attribution augments outcome-based turn advantages with credit assigned along the Source-State-Final chains. Transition-level validation also recovers useful supervision from gold-consistent state changes in trajectories with incorrect final answers. We evaluate ClueFlow across two Qwen backbones and four search benchmarks spanning live-web and fixed-corpus settings, observing consistent gains from SFT and further improvements from PPO. With Qwen3.5-35B-A3B, ClueFlow achieves 60.0% accuracy on BrowseComp and 72.0% on BrowseComp-Plus. In controlled BrowseComp-Plus experiments, attribution-guided SFT matches all-turn exact-context SFT using about 30% of the training tokens, while attribution-guided PPO outperforms outcome-only PPO by 4.1 pp. These results demonstrate that state-transition attribution enables efficient supervision and effective credit assignment for long-horizon search agents.

---


### 398. [Auditor-Assisted Summary-Channel Verification for Hosted LLM Identity Substitution](https://arxiv.org/abs/2610.25982)

**<font color=#1a73e8>作者：</font>** Ziyi Zhang, Ziyao Wang, Guoheng Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hosted LLM services increasingly expose model identity as a product claim, but external users and auditors often cannot inspect which model configuration served a request. We study an auditor-assisted regime in which a trusted auditor enrolls claimed identities and prepares verification material before deployment, while audit-time verification uses only the claimed identity and released output, without runtime access to model internals, inference logs, routing decisions, or provider metadata. We propose SUMMARK, a summary-channel watermarking framework that uses user-visible reasoning summaries as a keyed audit surface. During setup, SUMMARK constructs identity-specific vocabulary carriers, trains lightweight summary adapters, and calibrates per-identity thresholds. At deployment time, a keyed statistical test assesses whether the released summary is consistent with the claimed identity and, when needed, attributes the most likely enrolled identity. Across model families, scales, and task domains, SUMMARK reliably detects cross-family and cross-scale substitutions at low false-positive rates while preserving task-facing answer quality. We further study FP16->INT8/INT4 precision-consistency diagnostics and robustness under bounded post-processing, rewriting stress tests, and text-only spoofing, revealing both strong performance and clear failure boundaries. Our code is publicly available at this https URL.

---


### 399. [NIOCIS: Typed-Decision Next-Hop Routing with Node-Conditioned Option Spaces for Tool-Use Agents](https://arxiv.org/abs/2610.25985)

**<font color=#1a73e8>作者：</font>** Jin Han, Mingfeng Xin, Feng Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-use agents pay per decision: at each hop a language model re-reads the state and thinks for seconds, though its actions are finite and decisions recur. We present NIOCIS, a routing layer that folds execution logs into a loop-collapsed action graph (forward transitions plus recovery back-edges) answering one typed question: which declared option at a state, plus stop, does the fleet take next? A small model reads a calibrated distribution over them in one pass, emitting no text. On 1,615 production security-operations episodes we measure what the layer replaces, returns and is bounded by. Replaces: the typed encoder matches the logged next hop on 32.2% of the 3,875 held-out decisions (34.9% within the declared options) in 10 ms of encoder time (19.5 ms for the typed-choice form), against 2.2 s per LLM hop; two feature readouts reach 32.8% and 32.3%, an ordering the paired test does not resolve, so the typed layer is chosen for cost, not a separated lead. Tuning: jpt-4b reaches 9.9% zero-shot and 31.9% fine-tuned, a gap an exact paired test does not resolve (p=0.68), at 244 ms. Returns little: the realised hop falls outside the declared options for 7.9% of decisions and outside the model's top twenty for 9.3%; the most confident 15% holds 91.9% accuracy. Bounded: a cross-trace leave-one-out test puts the released state's ceiling at 25.6--44.9% as the state key grows more specific, i.e. repeated states disagree more often than they agree; the option-space ablation attributes the gain to per-node candidate restriction (+3.5 points over a flat catalog) rather than graph traversal (zero within its interval); a gated self-evolution loop lifts every arm above its anchor yet ends below full supervision; a confidence-gated cascade loses agreement when the escalation arm is the zero-shot stand-in; and agreement past a third of the fleet needs a state carrying the plan and the observation.

---


### 400. [Map-Distribution Mixture-of-Experts for Multi-Agent Pathfinding](https://arxiv.org/abs/2610.25991)

**<font color=#1a73e8>作者：</font>** Fumimaro Suzuki, Keisuke Okumura  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing capable neural policies for multi-agent pathfinding (MAPF), which map local observations to action distributions, represents an important challenge in multi-agent learning, with practical relevance to scalable collective automation problems such as warehouse logistics. In contrast to prior studies focusing primarily on individual policy design, this study explores a meta-level Mixture-of-Experts (MoE) approach to learning-based MAPF. Specifically, given a collection of compact yet high-performing experts specialised for different map distributions, our architecture learns a router that selectively fuses their outputs according to each agent's local situation. We instantiate and validate this MoE approach with a commonly used graph neural network-based policy as well as a newly developed recursive action-token refinement model. Combined with supervised and reinforcement learning fine-tuning of the experts, our experiments show that MoE generally improves upon the pretrained policy and outperforms existing leading methods. At the same time, our findings reveal that appropriately trained, parameter-matched monolithic models still outperform MoE, highlighting a nuanced role for map-distribution MoE for MAPF.

---


> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

# 🧠 大模型相关研究 | 2026年11月25日

> 本类共 **486** 篇论文：已确认 **458** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-486](./part-10.md)

---

### 51. [An LLM-Assisted Multi-Objective AutoML Framework for Efficient Network Intrusion Detection](https://arxiv.org/abs/2611.28312)

**<font color=#1a73e8>作者：</font>** Ailin Barzegar, Khalil El-Khatib, Li Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Conventional Machine Learning (ML)-based Intrusion Detection Systems (IDSs) require manual design, optimize only detection performance, and neglect inference latency and model size, which are critical for resource-constrained Internet of Things (IoT) and Electric Vehicle Charging System (EVCS) deployments. Automated ML (AutoML) reduces manual effort but explores broad search spaces inefficiently. Meanwhile, Multi-Objective Optimization (MOO) methods lack guided search initialization, leading to long search times. This paper proposes a Large Language Model-Assisted Multi-Objective Automated ML (LLM-MOO-AutoML) framework for efficient intrusion detection. A local Llama 3.1 8B model analyzes a compact dataset profile and generates a bounded, validated policy for automated data balancing (AutoDP) and feature engineering (AutoFE). This policy narrows the search space for Non-dominated Sorting Genetic Algorithm III (NSGA-III), which jointly optimizes the LightGBM feature-selection threshold and key hyperparameters across three objectives: maximizing weighted F1-score, minimizing 99th-percentile (P99) inference latency ratio, and minimizing model size ratio. Experiments on CICIDS2017, IoTID20, and CICEVSE2024 demonstrate that the proposed framework achieves the highest weighted F1-scores on CICIDS2017 (99.788%), IoTID20 (99.778%), and CICEVSE2024 (99.989%), with feature sets reduced to as few as 10 features, P99 latency as low as 0.00038 ms, and model size as small as 0.1073 MB. The LLM-guided configuration reduced NSGA-III search time relative to unconstrained multi-objective search on all datasets at the largest trial budget and in most comparisons at smaller budgets, indicating that dataset-aware search-space reduction supports efficient, deployment-aware intrusion detection.

---


### 52. [INSEP: Refusal-Direction Inseparability as a Defense Against Abliteration](https://arxiv.org/abs/2611.28314)

**<font color=#1a73e8>作者：</font>** Ivan Brugere, Junqi Jiang, Saumitra Mishra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Abliteration is a widely used white-box attack against the safety alignment of large language models (LLMs). It elicits harmful behavior by estimating a refusal direction in the model's activation space and projecting that direction out of the residual-stream write-out matrices. We propose INSEP, a defense that fine-tunes the model to reduce the separability of harmful and benign activations along the refusal direction. Abliteration estimates this direction as a difference in class means and projects it out. Reducing separability weakens the signal the attack relies on. An adversarial eigendecomposition selects the most separable prompt subsets. A low-rank adapter reduces their separation along that direction. Behavioral losses preserve the base model's refusal and the quality of its benign responses during training. We benchmark INSEP against six published defenses under five attacks, across eight LLMs from 1B to 14B parameters and several model families. Beyond response harm, we measure coherence, directness, over-refusal, and MMLU, to distinguish robust refusal from low harm produced by evasive or degraded responses. INSEP ranks first on the mean composite score across all eight base models while retaining utility, in the largest abliteration-defense evaluation reported to date.

---


### 53. [Selection Policies for Equal-Byte Mixed-Precision Quantization of Small Language Models](https://arxiv.org/abs/2611.28318)

**<font color=#1a73e8>作者：</font>** Smit Anand  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can changing which matrices receive 2, 4, or 8 bits improve a small language model without increasing its parameter storage? I compare two parent-selection rules in the same genetic algorithm: a binary-tournament variant and an Alternis-inspired rule. A separate baseline samples repaired random allocations without crossover or mutation. All three use the same MLX affine quantizer, byte ceiling, initialization and candidate allowance within each study. An exploratory study on Qwen3.5-2B evaluates 90 allocations per run. The main study on Qwen3-1.7B evaluates 500 distinct allocations per run over 10 paired seeds. Against uniform four-bit, tournament reduces held-out next-token negative log-likelihood (NLL) by 0.0616 on AG News and 0.0152 on IMDb on average, improving all 10 seeds on each corpus at identical parameter storage. Alternis improves five seeds and ties five on AG News; on IMDb its mean gain is near zero. Random returns uniform four-bit in every seed. The tournament representative answers 156 of 400 ARC-Challenge questions correctly versus 163 for uniform; no accuracy gain is demonstrated on this subset. The result favors this tournament variant for text prediction under the tested protocol, not for compression ratio or task accuracy.

---


### 54. [MatHarness: Towards Long-Horizon Open-ended AutoResearch for Computational Materials Science](https://arxiv.org/abs/2611.28324)

**<font color=#1a73e8>作者：</font>** Yanlin Fei, Lei Li, Shaolong Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Materials science research is a non-linear, long-horizon process. Existing scientific agents, however, largely rely on specific task execution or predefined workflows, rendering them brittle in open-ended settings. To bridge this gap, we present MatHarness, an agent harness designed for open-ended, long-horizon computational materials research spanning the complete lifecycle from initial ideation to manuscript writing. MatHarness couples three mechanisms: execution robustness through pre-flight verification, expert-distilled skills, and just-in-time auditing; epistemic adaptability through persistent research artifacts and an evolving scientific mental model; and collective intelligence through a heterogeneous multi-agent round table under targeted human oversight. We evaluate MatHarness on adsorbate-induced surface segregation in Cu-Zn alloys, an open question in methanol-synthesis catalysis. Over a multi-week trajectory consuming roughly 10^3 GPU-hours (50 production DFT relaxations prescreened by 171 machine-learning-potential evaluations) the system revised its plan six times, recovered autonomously from failed calculations, and had an independent auditor overturn one of its own over-attributed claims before publication. Within the sampled metallic dilute-limit models, the validated DFT analysis supports an adsorbate-induced tendency toward greater surface Cu exposure at both composition endpoints, with facet- and coverage-dependent exceptions. These results were compiled into a complete manuscript with human involvement concentrated in specification, approval, and strategic steering gates. The code is publicly available at this https URL.

---


### 55. [Decision models for UAVBench and the viability of edge deployment](https://arxiv.org/abs/2611.28331)

**<font color=#1a73e8>作者：</font>** Matthew Michelson, Goran Muric, Adrien Bibal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small language models are often proposed for reasoning onboard a drone. However, a good benchmark score does not tell us whether a model will actually run, and run usefully, on an edge computer. In this paper we study three related questions using the UAV decision benchmark, UAVBench. First, are small structured decision models good candidates for these tasks? Second, can an ordinary local machine (a Mac) screen candidate models before we test them on physical devices? Third, what software and resource limits govern deployment? Our main Mac evaluation covers 24 model configurations on the same 2,000 validated multiple-choice questions from UAVBench. These include 20 size-and-precision configurations of 11 generative models, plus four open-weight structured decision models that received no additional UAVBench-specific training. A structured decision model, H2O Lightning 4B, achieved the highest accuracy we observed, scoring 77.65% on the Mac. This shows that these models are well suited to this kind of task. However, when we tried to deploy the decision models, we ran into conversion and runtime limits on the edge devices we tested, which we describe in detail. To test local screening, we ran matched evaluations of two generative models on both the Mac and a Qualcomm RB3 board. The accuracies did not match exactly, but the ranking did. LFM2 2.6B ranked above Qwen2.5 1.5B on both platforms. This supports using a local machine to shortlist candidates. That said, individual answers still differed between platforms, so testing on the actual hardware remained necessary.

---


### 56. [GlaucomaMarker - Biomarker-Grounded Glaucoma Vision-Language Model](https://arxiv.org/abs/2611.28332)

**<font color=#1a73e8>作者：</font>** Ahammed Sakir Nabil, Sadia Siraz, Nikita Chincholkar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Glaucoma is a leading cause of irreversible blindness. In the current clinical setting, glaucoma diagnosis is generally conducted by assessing optic disc cupping and asymmetry. Vision-language models (VLMs) have been utilized in recent years for glaucoma, mostly trained on fixed templates or AI-generated captions, as no public text describes the biomarkers. Our proposed framework, GlaucomaMarker, hypothesizes that retinal structural biomarkers can ground glaucoma-based VLMs. It converts public segmentation masks into sentences describing eleven biomarkers, to teach retinal foundation models to read them. We applied this framework to RETFound (GlaucomaMarker-R) and FLAIR (GlaucomaMarker-F), training on 9,778 images that yielded 45,190 image-text pairs. On a real-world clinical cohort, GlaucomaMarker-F detects glaucoma with an AUROC of 0.905, against 0.848 for FLAIR, and both read the biomarkers where baselines stay near random guessing. Since the biomarker text is computed from existing masks, it comes at no extra cost.

---


### 57. [Alignment under Hard Negative Re-Pairing: Cross-Modal Similarity, Scale and Retrieval](https://arxiv.org/abs/2611.28336)

**<font color=#1a73e8>作者：</font>** Charles Weng, Alexander Martin, Sandra Arcos-Holzinger 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Do vision and language models represent the world alike? That question hides three: what structure each modality has, whether the two modalities organize images and their captions alike, and whether a model ranks an image's own caption highly. Centered kernel alignment (CKA) and neighborhood agreement answer the second, yet matching and model selection use them as if they identified individual pairs and answered the third. To test this reading, we introduce hard negative re-pairing: every image receives the caption of a similar image, and nothing else changes. Although no image keeps its own caption and annotators judge a majority of the substituted captions wrong, CKA stays higher than under a random re-pairing that keeps 80% of the original pairs. In all 22 image-text models we test, neighborhood agreement loses far less than top-one retrieval, which collapses. The reason is scale: these diagnostics pool over many neighbors, matching and retrieval are decided among the nearest ones, and an exact decomposition shows that near-neighbor pairs contribute almost nothing to CKA. In the matching problems we test, an exact maximizer of CKA would not return the original pairing. On COCO and Flickr30k, the model with the highest diagnostic value retrieves worse on held-out data than the model chosen by validation recall, even where the two correlate positively. What re-pairing removes is the informative part: that share tracks retrieval on both datasets and ranks encoder pairs before alignment training. A diagnostic should be reported with its question and its scale, and tested against hard negative re-pairing.

---


### 58. [When Tools Fail, Agents Fabricate: Silent Failure and Verification-First Oversight in Tool-Using LLM Agents](https://arxiv.org/abs/2611.28341)

**<font color=#1a73e8>作者：</font>** Gün Kaynar, Boshen Yan, Carl Kingsford  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents must recover when a tool call fails, by retrying, switching tools, or revising their plan. We study how agents fail when tools fail, using RetryRealistic, a sandboxed yet realistic testbed for controlled fault injection in which agents operate on a real OS filesystem with genuine permission enforcement, SQLite databases, a deterministic local HTTP server, and a constrained shell, across 8 tools, 9 fault types with controlled persistence, and 30 multi-step tasks. Evaluating four agents over 2,100 faulted runs against ground truth, we find that recovery is unreliable (19-68% correct) and frequently silent: 6-26% of runs end in a confident fabrication, a wrong answer asserted as fact. The failure mode is governed more by the fault type than by the model: faults that return partial data drive fabrication (up to 38%), while hard denials drive honest failure. The mechanism is what we call silent ingestion: the agent accepts faulted data as valid on first contact without retrying or flagging the problem, then builds a fabricated answer on top of it. We show that fabrication is reducible: a verification-first Monitor, grounding checks in structured tool outputs and issuing corrective directives rather than hard blocks, raises correct recovery from 45.6% to 56.3% and cuts fabrication from 17.3% to 10.8%. Removing chain-of-thought increases fabrication (+8.3pp), so deliberation guards against silent ingestion. We release RetryRealistic, the fault-injection toolkit, and all annotated traces at this https URL

---


### 59. [SMAD: A Semantics-Guided Multi-Agent Framework for Unsupervised Time-Series Anomaly Detection](https://arxiv.org/abs/2611.28348)

**<font color=#1a73e8>作者：</font>** Qinghua Liu, Junpeng Wang, Mingzhi Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time-series anomaly detection (TSAD) lacks a one-size-fits-all detector for heterogeneous data and anomaly types. Existing automation is limited by implicit objectives, potentially unreliable historical knowledge, or high computational costs. More fundamentally, it selects how to detect anomalies without explicitly defining what to detect. We propose SMAD, an LLM-based multi-agent framework that translates anomaly intent into executable, testable detection pipelines. Rather than selecting detectors against an implicit target, SMAD establishes a natural-language semantic contract grounded in measurable time-series properties, specifying target event patterns, expected score responses, and validation questions. This contract governs both detector construction and evaluation: LLM agents propose pipelines, while contract-matched synthetic interventions provide label-free evidence from the target series to assess semantic coverage and guide iterative self-refinement. A semantics-aware ensemble integrates validated candidates and attributes each alert to contributing detectors and supporting evidence. On univariate and multivariate TSAD benchmarks, SMAD improves detection performance over the strongest baseline by 11.5% and 9.6%, respectively, while outperforming general-purpose coding agents at 2-5x lower language-model token cost.

---


### 60. [Grammar-as-a-Draft: More Tokens per Speculative Decoding Step on Grammar-Constrained Structured Outputs](https://arxiv.org/abs/2611.28349)

**<font color=#1a73e8>作者：</font>** John Zhang, Silky Arora  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Under structured outputs (JSON schemas, regexes, tool calls), speculative drafters do not see the grammar constraint and repeatedly propose invalid keys, delimiters, and indentation, while the grammar engine already knows which tokens must come next.
We present Grammar-as-a-Draft (GaaD), which treats the grammar as a second drafter. Before each verify step, the scheduler merges the drafter's proposal with grammar-forced tokens into one draft row: matching tokens stay as GRAMMAR, the proposal is cut where it leaves the forced path, and forced tokens fill the rest of a row wider than the drafter's proposal. The verify step accepts GRAMMAR drafts without computing their logits, composing with any drafter with no new kernels or compilation on the critical path. Because grammars fix text rather than tokens, committing canonical forced tokens changes the output distribution relative to grammar-masked target decoding.
We implement GaaD in vllm-torchtpu and an independent Rust serving runtime, evaluating on TPU v7x with MTP, DFlash, and n-gram drafters on a JSON character-profile benchmark. GaaD raises average acceptance length from 2.06 to 5.43 (MTP, Qwen3.5-0.8B), 1.99 to 5.31 (MTP, Qwen3.5-35B-A3B), 1.57 to 4.13 (DFlash, Qwen3-4B), and 1.30 to 3.64 (n-gram, Qwen3-4B), decoding 2.66-2.81x faster at batch size 1 and 1.14-1.70x at batch size 64. In Rust, MTP+GaaD is 2.23x faster on Qwen3.5-0.8B, 2.02x on Qwen3.5-397B-A17B-FP8, and 1.22x at 128 concurrent requests. Under mixed traffic (25-50% structured), GaaD finishes the workload 1.03-1.23x sooner (structured requests 2.2-3.2x sooner) while plain-text TPOT rises 7-42%. We also show grammar-masked greedy decoding can pick non-canonical tokenizations, so GaaD can yield different valid outputs that an fp32 reference finds equally likely.

---


### 61. [Engram: Multi-Stage Memory for Agentic Tuning of Heterogeneous Models](https://arxiv.org/abs/2611.28356)

**<font color=#1a73e8>作者：</font>** Huanran Li, Nhat X.T. Le, Kevin De Angeli 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can now tune neural networks, yet without cross-session memory they spend costly trials rediscovering known lessons. Reuse is difficult because production models differ in architecture, training setup and inference budget. We present Engram, a memory system that links past trial outcomes with the hypotheses and rationale behind them and assesses whether this evidence applies to the current model. An online agent curates evidence at the decision points where it is needed: Initial Guidance supplies validated lessons at the start, Session Retrieval supplies related past sessions before each batch of hypotheses is generated, and Trial Candidate Review checks each trial candidate against matching past trials. Between sessions, an offline agent distills validated lessons, making the memory self-improving. On two ads models, Engram reaches the 32-trial result of a no-memory control with 47% fewer trials and also ends with a better model on average.

---


### 62. [Contrastive On-Policy Distillation via Dual-Branch Supervision](https://arxiv.org/abs/2611.28359)

**<font color=#1a73e8>作者：</font>** Zhibo Hou, Fan Zhao, Yiping Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For on-policy distillation (OPD), more capable models are a natural choice as teachers. However, higher task performance does not necessarily imply greater teachability. A controlled token intervention study suggests that even a model weaker than the student can serve as an informative contrastive reference. Building on this observation, we propose Contrastive On-Policy Distillation (cOPD), which provides dual branch supervision by contrasting strong teacher, weak teacher, and student predictions at student generated prefixes. Our analysis explains how this three way comparison helps select token candidates associated with better or worse reasoning outcomes under an idealized model. We evaluate cOPD across diverse teacher student configurations spanning different training stages, parameter scales, and model families, on tasks including mathematical reasoning, instruction following, and question answering with abstention. cOPD achieves the best or top-tier performance among the evaluated baselines across all three tasks, improving overall Pass@16 on mathematical reasoning by up to 7.51\% over the strongest baseline. Further analyses show that cOPD suppresses undesirable response patterns and suggest that it facilitates exploration.

---


### 63. [Schedule, Rank, Profile: Continuous Evaluation of LLM Agents in Games](https://arxiv.org/abs/2611.28368)

**<font color=#1a73e8>作者：</font>** Martyna Plomecka, Yao Yan, DJ Sterling 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Games are a robust test for large language model agents: they require sequential decisions, adversarial or cooperative interaction, state tracking, reasoning under uncertainty, and long-horizon planning. However, a one-time game benchmark can go stale as models, prompts, environment implementations, and evaluation policies change, and refreshing it is costly: full round-robin evaluation scales poorly in the number of model pairs, and the resulting outcomes live on incompatible per-game scales. We present a framework for continuous evaluation of LLM agents in game settings, organized around three coupled components. First, an adaptive scheduler that maps pairwise Bradley-Terry uncertainty to reduced per-pair match targets, concentrating budget on comparisons that remain unresolved. Second, a Unified Leaderboard (ULB) that reduces heterogeneous outcomes to pairwise evidence and fits a game-balanced Bradley-Terry model by minorization-maximization with bootstrap intervals, so that high-throughput games cannot dominate the aggregate ranking. Third, a game skill-profile methodology that scores each game along diverse skill dimensions, making the capability coverage of the suite explicit and turning game selection into a design decision rather than an artifact of availability. In this paper, we specify the research design and outcome reduction of the current implementation and evaluate the framework on a ten-game suite spanning perfect-information board games, imperfect-information games, and social/language settings, reporting LLM capability profiles, evaluation-cost savings across model-refresh cycles, and an empirical Pareto frontier relating model performance to inference cost. As deployed, the scheduler saved 61.7% of episodes; it counted each episode in the two team games as four records, overstating their savings, and the other eight games save 61.9%.

---


### 64. [CausalNTP: A World-Model Recipe for Causal Next-Token Prediction under Noisy Training-data](https://arxiv.org/abs/2611.28369)

**<font color=#1a73e8>作者：</font>** Devansh Arpit  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper shows that transformer networks trained with next-token prediction (NTP) and gradient descent do not learn to make predictions using only causally-relevant tokens in the left context, irrespective of the causal ordering of tokens during training, and identifies the learning deficiencies responsible. We introduce a causal world-model setup, for which, we characterize the Bayes-optimal predictor under the causal view of the data. We then prove that, a function that distills its predictions to non-causal views of data, when realized under Occam's Razor, recovers the true causal predictor. Based on this analysis we propose CausalNTP, a practical training algorithm that approximates this theoretical recipe and trains transformers to depend only the causally relevant tokens in left-context. Empirically in the world-model setup, CausalNTP achieves out-of-distribution generalization that vanilla NTP cannot due to its theoretical limits, regardless of data and model scale. We show similar gains and behavior in the natural language question-answering setting as a proof-of-concept.

---


### 65. [How a Prediction Dies: A Challenge-Driven, Rule-Bound Self-Refutation in an LLM Agent Society](https://arxiv.org/abs/2611.28371)

**<font color=#1a73e8>作者：</font>** Lei Zhenbing, Lei Chang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Persistent societies of large language model agents now make empirical claims about their own collective behaviour, yet the fate of such claims is rarely observable. We document one claim, from registration to death, on AITRAP, a multi-agent platform whose public, append-only ledger records every action. The claim (0495d171, registered 19 October 2026) asserted that a majority of bridges between problem domains would remain attached to a single exploration lineage. Three community challenges forced its judgment criterion through four versions, from an ambiguous statement to an executable protocol with a fixed threshold, a minimum-frame-size gate, and a baseline calibration gate. When the first frame with at least 20 bridges arrived, support stood at 9 of 79 (11.4%; Wilson 95% CI [6.1%, 20.3%]); the author, bound by the registered clause, refuted the claim and relinquished the associated stake. Three findings emerge. The criterion became executable only under community pressure, which we document version by version. The calibration gate caught a fault in the author's own recalculation that would otherwise have published a spuriously perfect 0/79 result. The failure itself traces to a denominator that grew 8.8-fold in five days while the numerator grew 1.8-fold, coinciding with a change in platform incentives; we report this mechanism as a hypothesis, not a rescuing condition. A claim whose termination is carried out exactly as written carries more evidential weight than one that survives, and this case provides initial empirical grounds for treating voluntary self-refutation as a candidate indicator of epistemic accountability in incentive-coupled agent societies.

---


### 66. [Language models compress human preference geometry while political structure remains prompt-sensitive](https://arxiv.org/abs/2611.28383)

**<font color=#1a73e8>作者：</font>** Adolfo Ignacio Fuentes-Jofre, Cristian Candia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to construct synthetic publics. Prior work has documented errors in individual responses, population heterogeneity, and prompt robustness, but whether these failures reflect a common loss of fidelity or distinct properties of synthetic populations remains unclear. We tested this using matched pairwise policy choices from 1,991 Chilean, 843 French, and 434 Brazilian adults replayed through three open-weight model families. Across a 27-condition Chilean grid and cross-country factorial replications, no condition jointly reproduced individual choices, population heterogeneity, and political organization. The most consistent result was compression of the latent preference space: synthetic participant variance was only 0.4-10.5% of the corresponding human reference in the primary comparisons and remained below human variance in all 270 matched refits. Political structure was much more sensitive to how choices were elicited. Reversing proposal position changed 12.3-31.2% of decoded choices. Explicitly labeling the endpoints of the numeric left-right self-placement scale changed 20.5-28.1% of choices and moved an independent proposal-level measure of left-right cleavage toward the human pattern in all three settings. Yet matched agreement improved by only 3.1-4.2 percentage points and participant geometry remained compressed. In Chile, the same intervention compressed the synthetic population further. These results separate political legibility from population fidelity: language models can recover salient political divisions while failing to preserve the breadth of human preference variation. Synthetic-public fidelity is therefore a property of the checkpoint, prompt, and setting, not of a checkpoint alone, and must be evaluated separately at individual, population, and political-structure levels.

---


### 67. [TOGO: Take One Image Editor, Get One Video Editor for Free](https://arxiv.org/abs/2611.28397)

**<font color=#1a73e8>作者：</font>** Yixuan Luo, Jose Caballero, Yanjing Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based image editors are trained on millions of edit pairs and follow instructions far more reliably than current video editors. We show that this ability can be transferred to video editing without any training. Our key observation is that a growing number of image editors and video generators share the same latent space. Their velocity fields can therefore be combined at sampling time: the difference between the editor's velocity under the instruction and under a neutral prompt, which we call the \emph{edit velocity}, can be added to the sampler of a video model. Added naively, however, it blurs the video, alters the background and flickers. An analysis of the edit velocity explains why. It is small and reliable only at coarse scales and high noise levels, not concentrated on the edited object, and uncorrelated across frames. From these properties, we derive a simple guidance operator that amplifies the edit velocity and restricts it in noise level, space, and time. The video model then turns the incoherent per-frame signal into a temporally coherent edit. Our method, TOGO, combines Qwen-Image-Edit with the Wan2.1 video model without training or fine-tuning. On FiVE-Bench, it raises the edit success rate from 47.0\% (the same video model without the editor) to 65.6\%, above the best published method (59.2\%). At the same time, it maintains the background PSNR and obtains the best LPIPS and SSIM of all methods. Because the video editor is assembled at inference time, it can be upgraded to any newer image editor that shares the latent space with no cost.

---


### 68. [The Effect of Security-Focused Prompts on Reported Findings: A Controlled Experiment on 400 AI-Generated Web Applications](https://arxiv.org/abs/2611.28408)

**<font color=#1a73e8>作者：</font>** Darko Andročec  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic coding tools turn a specification into a running web application, so their defaults for authentication, sessions, input validation, and dependencies become its security posture. This study asks whether appending a fixed block of OWASP-aligned security requirements to the prompt changes what such tools produce, by how much, and with what side effects. Each of 100 frozen specifications was realized four times: two agentic tools (Claude Code, Codex CLI) crossed with two prompts sharing a byte-identical functional core, without (A) and with (B) the security block. A fixed static and dynamic pipeline scanned the 400 applications, yielding 6,721 triaged findings, analyzed with count and logistic mixed models and with a dependency diff. The block cut findings per application by a third (incidence-rate ratio 0.65, 95% CI 0.60-0.71), equally through both tools, and roughly doubled the declared dependency surface, so variant-B applications carried more high-severity dependency advisories. Adjusted for that surface the advisory rate did not rise (flat per application, 18% lower in aggregate), while high-severity findings in first-party source fell by nearly half. Security-focused prompting is therefore an inexpensive and portable improvement, but it enlarges the dependency surface that has to be audited against it, an effect of library selection rather than of the security requirements themselves.

---


### 69. [Diversity over Scale: Recursive Self-Improvement with Ensembles of Small Open-Weight Models](https://arxiv.org/abs/2611.28420)

**<font color=#1a73e8>作者：</font>** Navapat Nananukul, Mayank Kejriwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The advancement of large language models (LLMs) has significantly enhanced the capabilities of agents across various tasks. Recursive self-improvement (RSI) loops, in which a language model repeatedly rewrites a program and builds on its previous version, now perform well in machine-learning tasks, but they rely on frontier models and hundreds of calls per run. Small open-weight models are far cheaper, yet when used alone, their programs often crash and their improvements stall. We propose DiVE (diverse models evolve), an ensemble method for RSI that aims to improve creativity and diversity of generated solutions. DiVE uses three components: a shared memory, a failure log, and best-idea-wins rounds. This allows models to write candidate solutions from the same context and retain the best idea at each iteration. On 22 MLE-bench Lite competitions, an ensemble of five 8-12B open-weight models has 25.4% less test error than its average member and 16.7% less than Llama 3.3 70B, and comes within 7.1% of Qwen 3.5 122B-A10B at 75% of its cost. Diversity among small models can thus stand in for part of the scale that RSI relies on.

---


### 70. [Human-in-the-Loop Runbook Improvement with Agentic Support Automation](https://arxiv.org/abs/2611.28441)

**<font color=#1a73e8>作者：</font>** Rocker D'Antonio, Harry Xie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Operational support is an important component of production software services. Support requests are often emergent and can come in many forms such as customer escalations or unplanned service interruption. Engineers across organizations have been successful in implementing automation to help streamline support processes but many solutions remain in the hands of human operators. A successful strategy to improve operator response times is to maintain up-to-date runbooks which are documents enumerating triage steps and remediation procedures in the face of identified incidents. This paper is an investigation into an operational system which incorporates Agentic AI into a runbook based incident resolution pattern. The bot uses information in the runbook corpus along with some system-specific tooling to guide the manual operator through the mitigation process then evaluate the outcome and suggest edits to the runbook where it found gaps and in its ability to triage the situation. By using the runbook as a medium to bridge humans and automation, the process maintains explainability and can be decoupled from the agent system. This paper demonstrates a collaboration between human operators and Agentic AI with results from an 17 week study involving 232 production incidents. We conclude with lessons on integrating LLMs into DevOps workflows, related work in AI-assisted operations, and guidance for reproducibility.

---


### 71. [Muted Distillation: Sealing Reasoning from Teacher Unlocks Token-Efficient Agents](https://arxiv.org/abs/2611.28445)

**<font color=#1a73e8>作者：</font>** Yuwei Zhang, Ian Miao, Wentao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is commonly adopted as one of the components in post-training of large language models (LLMs), but in multi-turn agentic tasks we find that the student model increases their reasoning lengths after training. Our empirical analysis shows that the reasoning token lengths is affected by how much the student can distract the teacher's scores. We introduce Muted Distillation (MD), a simple variant of OPD that hides the student's reasoning from the teacher, so the teacher judges what the student does without the interference of student's reasonings. MD takes a few lines of code and adds no extra data or hyperparameters. On the knowledge-work benchmarks OfficeQA Pro and SpreadsheetBench, it reduces output tokens per episode by 57\% and 53\% compared with standard OPD, making the student more concise than it was before training. At the same time, it matches OPD's accuracy on OfficeQA Pro and improves pass@1 by 4.8 points on SpreadsheetBench.

---


### 72. [When a Permitted Action Completes a Forbidden Workflow: Designing Consequence-Oriented Approval for LLM Agents](https://arxiv.org/abs/2611.28454)

**<font color=#1a73e8>作者：</font>** S M Asif Hossain, Ruksat Khan Shayoni, Md Kishor Morol 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-using language-model agents increasingly ask people to approve consequential actions, yet an approval prompt shows only the next step. A request to send a file to an approved recipient can look harmless even when that file was assembled, several steps earlier, from data the user said must never leave. We call this a cumulative authorization failure and argue that it is an interaction design problem as much as a security problem. The evidence a reviewer needs is spread across the trajectory, and listing it in time order leaves the reviewer to reconstruct the causal chain. We present the Cumulative Consent Ledger (CCL), an approval interface built on four design principles that restate the user's intent, bind the review to the exact action, compose the cumulative consequence, and keep every claim checkable. A trusted monitor that tracks artifact lineage supplies the evidence. In a between-subjects study with 80 participants and 960 approval decisions, CCL was associated with fewer unsafe approvals than an evidence-matched chronological log (24.2% vs. 32.5%), higher comprehension, and faster decisions, although the adjusted difference in unsafe approvals remained uncertain (-7.9 points, 95% CrI [-19.7, 3.8]). In a system evaluation, the monitor detected 89.2% of 120 violating checkpoints and, used as an execution gate, reduced executed unsafe effects from 43.3% to 5.0% for one agent at a small cost to benign completion. We derive implications for designing consent around consequences rather than individual calls.

---


### 73. [CAMA: Calibrated Anti-Collapse Marginal Alignment for Test-Time Adaptation of Vision-Language Models](https://arxiv.org/abs/2611.28461)

**<font color=#1a73e8>作者：</font>** Jinho Kang, Yunhui Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) updates a model using unlabeled test data to help it handle distribution shifts. However, prior work has found that image corruption causes a vision-language model (VLM) to produce more similar features for different images, a phenomenon known as feature compression. Under compression, entropy minimization, the most common TTA objective, can cause the model to favor a few classes and perform worse than before adaptation. Despite these observations, a detailed analysis of how these failures are connected and an effective strategy for preventing them are still lacking.
In this paper, we first analyze why entropy minimization fails for VLMs. We then propose CAMA, a new test-time adaptation objective that maximizes batch mutual information to encourage confident predictions for individual images while maintaining diverse predictions across the batch. CAMA also estimates a reference class distribution early in the test stream and aligns each batch's average prediction with this reference during adaptation. We prove that feature compression biases the predictions and that entropy minimization amplifies this bias into collapse, whereas CAMA is guaranteed to preserve every class. Across standard corruption benchmarks, we observe collapse on nearly every VLM backbone evaluated. CAMA prevents collapse in every observed case and, in turn, achieves the best accuracy on every backbone. Quantitative and qualitative analyses confirm that CAMA reverses the feature compression behind the collapse, and ablations show that each of its components contributes.

---


### 74. [PAMS: Preconditioned Activation-Metric Subspace for Zeroth-Order LLM Fine-tuning](https://arxiv.org/abs/2611.28476)

**<font color=#1a73e8>作者：</font>** Pradeep Kumar Ragu Chanthar, Saksham Sahai Srivastava, Jaewoo Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) optimization provides a computationally efficient approach to fine-tuning large language models (LLMs), but conventional methods typically rely on isotropic perturbations that ignore the anisotropic structure of neural-network parameter spaces. We introduce Preconditioned Activation-Metric Subspace (PAMS), a ZO optimization framework that uses forward-pass activation statistics to construct structured, layer-wise perturbation geometries without computing gradients or forming dense curvature matrices. PAMS tracks a low-rank approximation of the dominant activation subspace and its associated spectrum online, and uses the spectrum to softly reweight perturbation variance while preserving exploration in directions outside the retained subspace. A trace normalization separates the perturbation geometry from its overall scale, enabling consistent perturbation magnitudes across layers. We show theoretically that the resulting perturbation covariance induces right-side preconditioning of the gradient of the corresponding Gaussian-smoothed objective. We further characterize the estimator's smoothing bias and second moment and derive a nonconvex convergence guarantee that captures the effects of the perturbation geometry and smoothing radius. The proposed low-rank tracking procedure requires $\mathcal{O}(n_l r)$ persistent memory for a layer with input dimension nl and retained rank r, avoiding the $\mathcal{O}(n_l^2)$ memory required by a dense activation covariance. Experiments on transformer-based language-model fine-tuning tasks across GLUE and SuperGLUE demonstrate that PAMS improves the effectiveness and stability of zeroth-order optimization while retaining its gradient-free and objective-evaluation-based advantages.

---


### 75. [ESM-Bench: A Benchmark for Evaluating Whether AI Agents Understand Earth System Model Physics and Code](https://arxiv.org/abs/2611.28477)

**<font color=#1a73e8>作者：</font>** Koutian Wu, Yuxuan Cao, Gengchen Mai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI coding agents that modify Earth System Model (ESM) code must preserve both software interfaces and the physical assumptions encoded in them. We introduce ESM-Bench, a benchmark of 60 developer-commit tasks from 6 repositories: Noah-MP, CLM5, SUMMA, ParFlow, MOM6, and VIC. The v5 corpus contains 17 physics-based bug fixes, 16 process-representation modifications, 13 parameterization-scheme selections, and 14 parameter-optimization tasks. Each task includes a scientific objective, parent-commit source files, a reference diff, and three stored prompt variants. An artifact audit confirms that all 60 reference diffs apply to their supplied starting files. We define an eight-item patch-review rubric and audit five archived patch fixtures against the implemented local checkers. None of the five fixture diffs applies to its supplied starting files, yet three text-pattern checkers return a pass. A ParFlow expression replay disagrees with the reference slopes, and a MOM6 pattern check detects an omitted update. Inspection also identifies a retained VIC reference assignment that overwrites the intended vegetation-specific albedo. These findings expose limits of reference patches and local proxies as correctness evidence. The release provides a reproducible corpus and diagnostic tools; complete expert validation, comparative agent performance, and full-model execution remain unmeasured on v5.

---


### 76. [Digital Knockoffs](https://arxiv.org/abs/2611.28482)

**<font color=#1a73e8>作者：</font>** Niuniu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social simulations often use language model agents to represent people who differ on several measurable traits. However, describing a trait profile in a prompt does not guarantee the agent will express each trait at its intended level. We propose a method that calibrates agents to multidimensional profiles using activation steering: (i) extract steering directions for each trait, (ii) learn a shared mapping from steering strengths to measured trait scores, and (iii) search for a steering intervention for each target. We use Bayesian optimization for this search and evaluate the method on the Big Five personality scores of 500 OpenPsychometrics respondents. In each of five rounds, the assigned interventions yield lower mean absolute error across respondents than the prompting and steering baselines. Further, the model's responses to a given intervention yield the same trait profile regardless of whose target motivated it, so a poor match for one respondent can be the best match for another. When we match each respondent to the closest profile found across all tested interventions, Bayesian optimization yields 16.6% lower mean absolute error than uniform random search at the same evaluation budget. Our method thus offers a way to build social agents whose measured traits dovetail with those of the people they seek to represent. Whether this closer fit translates to improved predictions of downstream behavior remains an open question.

---


### 77. [Don't Train It, Write It: An AI Agent Writes New Capabilities into Language Model Weights](https://arxiv.org/abs/2611.28483)

**<font color=#1a73e8>作者：</font>** Santiago Rivadeneira Quintero  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that an AI agent can write new capabilities into a pretrained language model by adding gated attention heads and MLP neurons inside its existing layers, without backpropagation and without fitting any weight to the answers of task examples. It has a budget of 50 model passes and sees no validation or test instance. Composed in one model, its modules for six BIG-Bench Hard (BBH) subtasks raise the normalized BBH score of Qwen2.5-1.5B-Instruct from 19.95 to 41.05 (Qwen2.5-7B-Instruct: at most 35.01) and that of Gemma-3-1B-it from 10.25 to 32.86. Against the unmodified model at the same precision, both composites leave the next-token distribution on 1,023,000 WikiText tokens unchanged (KL exactly 0), give identical answers on 15,845 items of five other Leaderboard tests and identical scores on the other 18 BBH subtasks. The agent also writes exact multiplication up to 20 digits, running the model only up to 6 (100.0% on the absent lengths of the sealed test in both models; a LoRA with the same budget: at most 2.1%). Sets, rules and report sentences were sealed in git before the first session (manifests timestamped in Bitcoin), with dated amendments listed in Appendix D; a frozen evaluator ran the sealed test once. Verdicts (H5: tracking; H6: composite; H8: one pass vs. chain of thought; H9: fresh and rewritten instances; H10: side effects; H12: multiplication), on the preregistered sealed test, Qwen2.5-1.5B-Instruct: H5 success, H6 success, H8 (web_of_lies) success, H9 success, H10 (composite) success on (i) to (iii), (iv) confirmed, H12 success; Gemma-3-1B-it (H7: H5, H6, H8 and H9 in this model): H5 success, H6 success, H8 (web_of_lies) success, H8 (tracking 3) success, H9 partial, H10 (composite) success on (i) to (iii), (iv) confirmed, H12 success. Not everything worked: 4 of 45 single modules show small side effects and 5 of 50 sessions hit the 12-hour limit without a module.

---


### 78. [PatchLens: Adapting Mechanistic Interpretability Techniques for Non-Expert Audiences](https://arxiv.org/abs/2611.28487)

**<font color=#1a73e8>作者：</font>** Gwenyth Lincroft, Yik Su Chan, Adam Belfki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A chat interface presents a reply as finished text, concealing a model that predicts at every position and reruns. Mechanistic interpretability can show how a large language model produces text, but its tools are built for researchers. We present PatchLens, a browser interface that runs logit lens and activation patching on remotely served research-scale models. Each layer's state appears as the tokens it comes closest to, laid out by layer and input position; an intervention is a drag from one cell onto another. The tokens a learner reads are the tokens they manipulate. In a between-subjects study with 61 non-experts, the comparison against Transformer Explainer was inconclusive on post-test knowledge. PatchLens participants wrote their own prompts (21 of 32 against 1 of 29), reported lower mental demand, and located their difficulty in the interface rather than the material. We read the null as evidence about what such an instrument measures.

---


### 79. [Open Vision Banana: An Open Framework for Unified Visual Perception through Generation in RGB Space](https://arxiv.org/abs/2611.28489)

**<font color=#1a73e8>作者：</font>** Xu Lin, Ruilin Yao, Haoran Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Banana showed that a closed image generator, instruction-tuned to paint perception outputs as RGB images, becomes a generalist vision model. Does this carry over to \emph{open} generators, and if not, what fails? We answer with \textbf{Open Vision Banana (OVB)}, an open framework that adapts the 7B diffusion generator of Qwen-Image-2.1 into one instruction-driven model for metric depth, semantic, instance, and referring segmentation, using a single shared low-rank adapter and public data. Each task is a \emph{task contract} whose RGB encoder, instruction, and decoder share one specification and are checked before training. Studying 42 externally evaluated checkpoints from two 100k-update runs, six exact weight-space merges, and eight controlled shorter runs, we find that the gap to the closed system is specific and measurable. Geometry is learned early while absolute scale is not: median-aligned NYUv2 $\delta_1$ stays at 0.89--0.93 throughout training as unaligned $\delta_1$ wanders between 0.11 and 0.50. The scale is not committed by a single sample: a ten-seed ensemble lifts unaligned $\delta_1$ from 0.348 to 0.516 without retraining. Depth and 2D segmentation compete for the shared adapter, and weight merging moves along this trade-off without escaping it. Finally, lower validation flow loss comes with lower Cityscapes accuracy (Spearman $\rho\approx-0.9$ between loss reduction and mIoU), so the loss cannot select checkpoints. We release code, contracts, training data, and all evaluation outputs.

---


### 80. [SupportChain: Trace-Calibrated Aggregation of Quote-Grounded Reasoning Chains for Multi-Hop RAG with Small Readers](https://arxiv.org/abs/2611.28519)

**<font color=#1a73e8>作者：</font>** Zhexi Gu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Strong results in multi-hop retrieval-augmented question answering come from graph indexes read by models of 70B parameters or more, and building such an index calls a large language model over the whole corpus. We present SupportChain, which splits a question into hops, binds each hop's answer to a sentence quoted from a retrieved passage, estimates how reliable each execution is from its own trace, and merges several executions by the support of their answers, the pooled reliability of the executions that agree, stopping once support is high enough. With a 9B reader under the HippoRAG~2 protocol, SupportChain reaches 63.0 F1 on MuSiQue, above the best earlier result of 59.2, which used a 20B reader. With the same reader and embedder, it is significantly better than HippoRAG~2 on all five datasets, by up to 17.2 F1, and it builds no index. Merging by support is significantly better than majority voting, and than letting the reader choose among the candidates, on three of the five datasets and level with both on the other two. The reliability model needs only 100 answered training questions.

---


### 81. [DisSparse: Pipelined Top-$p$ Sparse Attention for Long-Context LLM Serving](https://arxiv.org/abs/2611.28522)

**<font color=#1a73e8>作者：</font>** Nurlan Nazaraliyev, Elaheh Sadredini, Nael Abu-Ghazaleh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context LLM inference is bottlenecked by the memory demands of the key-value (KV) cache, whose size scales linearly with context length. Dynamic sparse attention reduces this bottleneck by fetching and attending only to a critical subset of tokens. The dominant primitive in dynamic sparse attention research and deployment is fixed-budget top-$k$ selection, which is favored because its deterministic block count aligns with the static memory allocation that systems like vLLM rely on. Top-$k$ uses a fixed budget regardless of how attention mass is distributed across heads, layers, and decode steps, leading to either wasted bandwidth on heads with peaky attention or dropped context on heads with diffuse attention. Top-$p$ (nucleus) selection adapts naturally to this variation but has seen limited adoption in production serving systems due to two system-level challenges: variable block counts that break deterministic block allocation and computationally expensive selection kernels that exceed the cost of attention itself. We present DisSparse, a serving system that integrates top-$p$ sparse attention into vLLM end-to-end. DisSparse decouples block selection from the scheduler's critical path, hides selection latency behind layer computation via a two-stream pipeline, and introduces a single-pass histogram-based top-$p$ kernel. We further observe intra-block sparsity, the inflation of selection budgets caused by mixing high- and low-importance tokens within fixed-size KV cache blocks, and address it with a token relocation kernel guided by accumulated prefill attention scores. Across long- and medium-context benchmarks on multiple models, DisSparse achieves 1.17x to 1.80x speedup in sparsity analysis (block selection) over state-of-the-art top-$p$ methods with negligible accuracy loss and supports up to 8x larger maximum batch sizes than dense vLLM under the same memory budget.

---


### 82. [Information Access and Gain-Loss Framing in Six Large Language Models and Human Decision Makers](https://arxiv.org/abs/2611.28525)

**<font color=#1a73e8>作者：</font>** Aadithya Chandramouli, Jeremy M. Gernand  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A risky choice can be described by what will be saved or what will be lost, and people often choose differently depending on that wording. We test whether six large language models (LLMs) show this gain-loss framing effect, and whether it shrinks when they can first read more about the options. GPT-4.1, GPT-4o, GPT-4o-mini, Gemini 2.5 Flash, Qwen3 235B and Llama 4 Maverick made 11,519 choices across four risk scenarios, each in its original wording, two paraphrases and a mirrored version in the opposite wording. Before choosing, a model could open up to 0, 2, 3 or 4 of seven information cards. With no cards, all six models showed large framing effects: the share choosing the safe option was 27 to 79 percentage points lower under loss than under gain wording. The gap was smaller at 2 cards than with no cards in every model. Against a 10-point threshold set in our analysis plan, GPT-4.1 fell within it at 4 cards and Qwen3 only at 2 cards; in the plan's pooled comparison over all versions, GPT-4.1 was within it from 2 cards and GPT-4o from 3. GPT-4o-mini and Llama 4 Maverick kept gaps of 28 to 66 points with cards, and for GPT-4o-mini and Qwen3 the gap grew again from 2 to 4 cards. Part of the drop from 0 to 2 cards may reflect a change in prompt format, and most card content counted against the risky option, which may favor the safe choice. In an exploratory comparison with 198 students who saw the same scenarios and cards but opened cards one at a time and chose how many, decisions made after opening 0 or 1 cards showed a 19-point difference between the gain scenarios, asked first, and the loss scenarios, asked later, and no clear difference appeared in decisions made after opening more, though this design cannot show that cards reduced framing in people. With these cards, in the balanced comparison 17 of 18 card gaps were below the model's no-card gap, but few were within the threshold.

---


### 83. [Where the Image Sits: Vision-Text Order Bias in Jev](https://arxiv.org/abs/2611.28535)

**<font color=#1a73e8>作者：</font>** Youzhi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Jev-style system-1 decision models read a choice from a single prefill. They restrict the next-token distribution to the supplied option labels and return a distribution over the options, with no generation and no parsing. Recent work shows that generative vision-language models are sensitive to the relative order of image and text tokens. We ask whether that sensitivity reaches this Jev-style readout. The answer is always read at the end of the prompt, so moving the image changes the distance from the visual evidence to the decision, but never the position at which the decision is read. Using four placements---prefix, pre-question, pre-options, and suffix---and holding the option listing fixed, we measure argmax flips, total variation, accuracy, calibration, and label marginals. Suffix placement flips 41.0% of decisions and lowers accuracy by 18.6 points. Averaged over the four slots, the curve is monotone, not U-shaped. That shape differs from prior results on generative vision-language models. The effect survives a battery of controls. We also introduce prefix--question averaging (P+Q), a two-forward readout that averages the prefix and pre-question distributions. It is at least as accurate as prefix and outperforms the prior baselines. Our code and data are publicly available at this https URL.

---


### 84. [BIRD-Persona: A Persona-Aware Benchmark for SQL and pandas Analytics Code Generation](https://arxiv.org/abs/2611.28542)

**<font color=#1a73e8>作者：</font>** Davin Hill, Pawan Chorasiya, Bhawani S. Leelar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Production text-to-code systems use large language models to turn natural-language analytics requests into executable SQL and pandas code. Existing benchmarks cover both tasks but do not isolate when performance diverges between them. We introduce BIRD-Persona, a persona-stratified extension of BIRD-Python that adds novice and expert rewrites to tasks with matched SQL and pandas ground truth, along with schema variants and task-structure annotations. Across 1,534 tasks, nine models, and 245,592 evaluations, SQL outperforms pandas for eight of nine systems. The gap varies by condition: expert, schema-explicit prompts improve both paradigms but help SQL more; schema representations have mixed, model-dependent effects; and selected-column burden widens the gap while subqueries do not. By making user phrasing a controlled benchmark dimension, BIRD-Persona supports persona-aware and paradigm-aware evaluation of natural-language analytics systems. The dataset is available at this https URL.

---


### 85. [X-AQA: Unifying Action Quality Assessment with Multimodal Large Language Models and Multi-Domain Learning](https://arxiv.org/abs/2611.28548)

**<font color=#1a73e8>作者：</font>** Kaili Zheng, Wei Ding, Yuchen Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Action Quality Assessment (AQA) aims to evaluate the quality of human actions, yet existing methods are predominantly developed and evaluated on individual datasets with different task formulations and assessment criteria. We introduce X-AQA, the first unified training and evaluation framework for general-purpose AQA with multimodal large language models (MLLMs). We construct X-AQA-40K, a training corpus comprising 40,163 samples from 22 data sources across four domains: competitive sports, fitness exercises, rehabilitation, and general skills. We convert heterogeneous annotations into a unified question-answering format, incorporating dataset-specific annotation guidelines and official scoring rules when available. Using this corpus, we fine-tune Qwen3.5-9B to develop a single MLLM capable of handling diverse AQA tasks. We further establish X-AQA-Bench, which evaluates both in-distribution (ID) performance on datasets represented during training and out-of-distribution (OOD) generalization on four held-out datasets. The resulting model outperforms all evaluated open-source MLLMs on X-AQA-Bench and achieves competitive performance relative to proprietary MLLMs. Ablation studies further demonstrate that multi-domain joint training and explicitly providing assessment criteria in prompts both improve OOD generalization. X-AQA establishes a unified foundation for advancing general-purpose AQA across diverse real-world domains. Data and models are released at \hyperlink{this https URL}{here}.

---


### 86. [From Reward Engineering to Data-Centric Reinforcement Learning for Effective Agentic Visual Tool Use](https://arxiv.org/abs/2611.28558)

**<font color=#1a73e8>作者：</font>** Jin Cui, Xinyue Long, Jiepeng Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) increasingly use external visual tools to acquire evidence during reasoning, yet learning when to invoke these tools remains challenging. Existing tool-use reinforcement learning (RL) methods often rely on call-contingent rewards to encourage beneficial tool use, but such reward engineering can distort the task objective and lead to degenerate calling behaviors. We argue that effective tool-use learning requires identifying not merely which questions are difficult, but which failures are attributable to missing visual evidence and can therefore be corrected through tool observations. We propose AOVO, a data-centric framework that enables MLLMs to learn effective tool use through perception attribution and policy-adaptive data sampling (PADS), without introducing tool-specific rewards. It counterfactually probes the model's reasoning states to identify observation-sensitive questions, distinguishing them from reasoning-dominated ones. PADS then periodically estimates category-level observation effects from recent policy rollouts and dynamically reallocates the training distribution toward questions where visual observations provide informative learning signals, while optimizing solely for final-answer correctness. Experiments across diverse visual perception and multimodal reasoning benchmarks demonstrate consistent improvements over competitive tool-use MLLMs, with causal analysis further validating the data-centric perspective for learning effective visual tool use.

---


### 87. [Tool-to-Self: Internalizing Visual Tool Capabilities via Scaffolded Reinforcement Learning](https://arxiv.org/abs/2611.28564)

**<font color=#1a73e8>作者：</font>** Jin Cui, Hao Dong, Xinyue Long 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) increasingly rely on external visual tools to access fine-grained visual evidence, but repeated tool execution incurs substantial inference overhead and deployment dependencies. Moreover, conventional tool-use RL can improve visual-task performance, yet the resulting tool gains are often unstable. Motivated by this, we propose Tool-to-Self (T2S), a tool-scaffolded reinforcement learning framework that turns external visual tools into temporary training scaffolds. T2S cold-starts tool-use ability and observation prediction from tool-repairable examples, then progressively anneals tool execution on a per-tool basis during RL. By combining answer-correctness and observation-consistency rewards with privileged on-policy self-distillation from actual tool observations, T2S effectively teaches the model both to reproduce tool outputs and to reason from them. Experiments across diverse visual perception and reasoning benchmarks demonstrate consistent improvements over both explicit tool-use models and implicit zooming models while enabling tool-free inference with reduced latency.

---


### 88. [Beyond Unit Tests: Path-Aware Rubric-Guided LLM Autograding of Notebooks](https://arxiv.org/abs/2611.28565)

**<font color=#1a73e8>作者：</font>** Salman Hajizada, Mohammed Yusuf Ansari, Gianni Di Caro  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Jupyter notebooks support open-ended, multi-step assessments in which students build one logical flow across interdependent steps, combining code, written analysis, and generated outputs such as plots. These reflect authentic scientific practice but are hard to grade consistently, since students may make different yet equally valid choices at each step, so a later answer can only be judged in light of the choices a student made earlier. We present an LLM-based autograder for such flow-structured notebook questions. It generates a rubric from a reference solution, then applies a softening pass that relaxes criteria tied to the reference so legitimate alternative paths are not penalized. Each question group is graded in a single model call, so later answers are judged against the student's own earlier choices, using question-type tags and schema-constrained, low-temperature outputs. Evidence is scored multimodally: code, text, numerical outputs, and figures from code cells. We deployed the tool in a machine-learning course, integrated with Gradescope, with a pre-submission format check and prompt-injection defenses, and evaluate it both in that live course and against archived submissions graded by staff in earlier terms. We report agreement, cross-model variance, cost, student perceptions, and injection resilience. With low-temperature models, agreement with human scores is often strong, including on the open-ended items the design specifically targets, while run-to-run stability depends sharply on the model's temperature support.

---


### 89. [MACE: Memory-Augmented Crop-Disease Evaluation of Frozen Vision-Language Models](https://arxiv.org/abs/2611.28573)

**<font color=#1a73e8>作者：</font>** Tirtho Roy, Shreyan Ganguly, Muhammad Arbab Arshad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In plant phenotyping, crop disease diagnosis has traditionally relied on expert assessment of visible symptoms and on models tailored to specific crops or diseases, and both are difficult to scale across field conditions. Recent methods provide frozen vision-language models with source-grounded knowledge bases that summarize the typical symptoms of each disease but describe little of how symptoms vary across individual cases. We introduce MACE (Memory-Augmented Crop-Disease Evaluation), a training-free method that supplements the knowledge base with a memory of symptom descriptions paired with known disease labels. MACE matches a description of the query image against this memory and retrieves only text descriptions and disease labels, so the query is the only image that the diagnosis model sees. Across ten crops, MACE with Claude Sonnet 5.5 improved accuracy over the knowledge-base baseline from 42.8% to 62.2% in distribution and from 50.7% to 57.0% on held-out image collections. Retrieved disease labels accounted for most of the gain, and adding the corresponding text descriptions improved in-distribution accuracy by about six percentage points.

---


### 90. [EvoViM: Recursively Self-Evolving Visual Agents for Exploration with Deferred Queries](https://arxiv.org/abs/2611.28574)

**<font color=#1a73e8>作者：</font>** Xinyu Cao, Tianjie Ju, Zhuosheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language model (MLLM) agents have shown promising capabilities in task-oriented environments. However, they still struggle when queries are deferred until after exploration, requiring them to retain visual evidence before knowing which details will matter. We introduce EvoViM, a recursively self-evolving framework in which a frozen multimodal model turns its own interaction experience into one visual program for memory and skills. The program retains images and computes directly on pixels, and its operations decide how this evidence is used in each task. During memory evolution, the same model traces failures in its visual trajectories to the operations that lost or misused evidence and revises them. It also rewrites the notes and analysis tools that guide later revisions, which then build on earlier findings and skip changes that have already failed. We evaluate EvoViM with three multimodal models on six tasks covering visual matching, spatial recall, and sequential decision-making, including three tasks with deferred queries. Across the six tasks, EvoViM improves the average score over AutoMem, the strongest baseline in the main comparison, by 31.3-47.6 points on held-out episodes. Programs written once from the initial environment instructions perform substantially worse, highlighting the value of interaction experience in shaping how visual evidence is retained and used. Code and dataset are available at this https URL.

---


### 91. [CLASP: Deciding Structure and Claims Before Decoding for Whole-Slide Pathology Report Generation](https://arxiv.org/abs/2611.28576)

**<font color=#1a73e8>作者：</font>** Ziaullah Khan, Rashadul Islam Sumon, Md Ariful Islam Mozumder 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide pathology report generation has advanced through stronger slide encoders, retrieved knowledge, and, recently, slide-level multimodal LLMs. However, these generators leave every report-level choice to the decoder: how long the report is, how it is organised, and which findings it states and where. On the standard PathText-BRCA benchmark, we find that these choices dominate n-gram overlap, as reports from the query's hospital selected without learning approach the state of the art, while decoders under-generate and fall back to the most frequent findings. We present CLASP, a decide-then-decode generator that makes these choices explicitly, once per slide. Before decoding, an Exemplar Structure Prior (ESP) takes the sentence plan and length from reports of image-similar cases, a Calibrated Claim Decision (CCD) selects the findings from calibrated slide posteriors, and a Claim-to-Sentence Placement (CSP) assigns each finding to a planned sentence. A Plan-Conditioned Decoder (PCD), refined by structure-anchored sequence training, then writes the report under these decisions. With 35M parameters, CLASP outperforms retrained report generators and slide-level LLMs of up to 7B parameters, matches the strongest published results, and generalises to lung cancer from unseen hospitals. Its decisions change what the reports state, not only their length, transfer to an LLM decoder, and can withhold what H&E cannot show: withholding receptor status leaves 23% fewer contradictions with clinical records than the same network without decisions.

---


### 92. [Understanding and Mitigating the Fragility of Self-Rewarding Optimization](https://arxiv.org/abs/2611.28582)

**<font color=#1a73e8>作者：</font>** Rongyi Zhu, Tanqiu Jiang, Fenglong Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-rewarding optimization (SRO) promises to improve language models by enabling them to generate their own reward signals. Yet when and how SRO succeeds or fails remains poorly understood. We reveal that SRO is fundamentally fragile: even seemingly benign perturbations to training prompts can corrupt the self-generated preference signal and trigger iterative collapse. We demonstrate this through two prompt-level attacks that serve as controlled stress tests: a Re-Ranking attack that concentrates training on prompts where self-reward diverges from an oracle, and a Preamble attack that learns short prefixes inflating self-reward without any gain in oracle quality. To explain why these attacks succeed, we introduce self-reward fidelity (SRF), a metric quantifying on-policy agreement between self-evaluated and oracle rewards. We show that SRF can serve as a diagnostic signal of self-supervision reliability, and that controlled SRF perturbations induce a phase-transition region: SRO improves when SRF remains sufficiently high, but collapses once SRF drops below a model- and task-dependent threshold. This analysis motivates Projection Decoupling Defense, which suppresses SRO update components along directions to which the reward generator is locally sensitive, improving SRO robustness under adversarial conditions. This work sheds light on the fragility of SRO and charts promising directions toward making it more robust.

---


### 93. [CLOSE: A Calibrated Label-free Online Self-Evaluating Verifier for Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2611.28589)

**<font color=#1a73e8>作者：</font>** Zhaoxi Wang, Jiahao Lai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models frequently describe objects absent from the image because of language priors. Yet the model itself is already a strong judge of its own output: asked separately whether an object is present, it rejects 44%-62% of its hallucinations, and its yes probability reaches an AUROC of 0.90-0.95 without training. This judgment, however, is not directly usable: (1) its probabilities lack a common scale across models; (2) for the remaining 38%-56%, the model still answers yes with probabilities that overlap those of real objects, so no threshold separates them. We therefore propose CLOSE, a Calibrated Label-free Online Self-Evaluating verifier that enforces this judgment during generation. Its threshold is a quantile of a memory rather than a probability and thus depends only on ranks; the memory is cold-started from unlabeled images and updated online. A scorer self-trained on pseudo-labels from four hidden-state signals is fused with self-asking by rank to separate what self-asking leaves mixed. Refused objects are rolled back and banned through a laddered back-off, and a recognition table intercepts their reappearance under other wordings. On COCO, refusing 20% and 40% of object mentions reduces the CHAIRs of LLaVA-1.5-7B by 42% and 87% (F1 +1.9 and -6.1 points); refusing 20% and 35% reduces the reachable hallucinations of Qwen3-VL-8B (official counts minus CHAIR-script miscounts) by 79% and 96% (F1 +0.5 and -5.3). An external vocabulary further extends the check beyond the official vocabulary.

---


### 94. [When Fog Becomes a Weapon: Atmospheric Attacks on Visible-Infrared Vision-Language Models](https://arxiv.org/abs/2611.28592)

**<font color=#1a73e8>作者：</font>** Chengyin Hu, Dehe Zhao, Dingyi Lu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing adversarial attacks on vision-language models (VLMs) and cross-spectral perception primarily rely on conspicuous, unnatural artifacts, such as vivid adversarial patches or active light beams, that lack physical stealthiness, whereas prior weather attacks largely overlook how one atmosphere simultaneously affects heterogeneous sensors. This raises a key scientific question: can a purely natural, shared fog environment simultaneously disrupt complementary visible and thermal infrared cues without artificial surface modifications? We introduce Fog Manipulation Attack (FMA), a zero-gradient attack that optimizes a common 3D fog state to induce simultaneous semantic failures in visible-infrared VLMs. FMA links shared, depth- and layer-aware atmospheric propagation along scene paths with band-specific imaging physics---visible airlight scattering and thermal path radiance---allowing one realistic fog state to erode both modalities' distinct cues. Experiments show that FMA more than doubles simultaneous failure rates over fidelity-matched random fog, transfers to captioning and VQA, and removes cross-modal compensation, where restoring a clean companion view recovers 64%--74% of lost dual-input VQA answers.

---


### 95. [Bridging Teacher-Student Capability Gaps with Recurrent Computation](https://arxiv.org/abs/2611.28603)

**<font color=#1a73e8>作者：</font>** Zeyi Huang, Jiuxiang Gu, Eli Shechtman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation transfers capabilities from large language models to smaller students, yet stronger teachers do not always yield better students. Recent studies report diminishing or even negative returns from teacher scaling. We hypothesize that these limitations arise in part from insufficient student capacity to absorb the teacher's knowledge. We therefore investigate loop and recurrent computation as a way to expand the student's effective capacity by modifying its computation graph while keeping the backbone parameter count fixed. Under teacher-forced KD during pretraining, weight-shared looping improves performance but retains teacher-size saturation, whereas cross-token recurrence avoids the observed reversal with larger teachers. In mathematical post-training under both teacher-forced KD and on-policy distillation (OPD), recurrent students scale better with increasing teacher size than looped and vanilla LLMs do. Crucially, we show that a pretrained LLM can be readily fine-tuned into a looped or recurrent architecture jointly with OPD, without repeating pretraining. Our recurrent Qwen model improves with larger teachers and consistently outperforms looped and vanilla LLMs. This suggests a new post-training paradigm that integrates architectural conversion into distillation, avoiding a separate conversion stage while substantially improving student performance and maintaining near-vanilla inference latency.

---


### 96. [BitShare: Sensitivity-Aware Binning and Bit Sharing for Compacting LLM Weight Storage](https://arxiv.org/abs/2611.28607)

**<font color=#1a73e8>作者：</font>** Qiuyu Ren, Sudipta Paria, Aritra Dasgupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoding with large language models at small batch sizes is limited by memory bandwidth, so the bits stored per weight largely set its cost. Group-wise integer quantization stores every weight of a group at the same precision, although the input channels of a group differ in sensitivity. We present BITSHARE, a codebook-free weight format that keeps the integer grid and the dequantizer of group-wise quantization but varies precision within each group. Sensitivity-aware binning places the channels of each group into three bins at fixed positions, and static bit sharing with optimal bit-value allocation lets the less sensitive weights share their lower bits, each stored once per group or once per pair of weights. A sharing-aware version of GPTQ chooses every stored value, with no fine-tuning and no codebook. BITSHARE has two modes. BITSHARE-U gives every group the same layout, so its decoder routes bits by fixed wiring, while BITSHARE-N chooses a layout per group within the same bit budget. With calibration on the Pile and at the same storage, both modes have lower perplexity than GPTQ at 3 and 2 bits on WikiText-2 and C4. At 2 bits across Llama-2 and Llama-3 models, BITSHARE-N lowers WikiText-2 perplexity by up to 70% against SliM-LLM and up to 35% against GPTAQ. At the 2-bit perplexity of SliM-LLM, BITSHARE-U stores 13.6-19.4% fewer bits per weight, cutting DRAM weight traffic by the same fraction. A verified hardware decoder implementation synthesized in SkyWater 130 nm reconstructs BITSHARE weights at the throughput of INT-n and SliM-LLM decoders.

---


### 97. [Agent Money Benchmark: Can AI Agents Be Trusted to Spend Money?](https://arxiv.org/abs/2611.28610)

**<font color=#1a73e8>作者：</font>** Zhe Chen, Emma Hsieh, Vicky Fu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Giving an AI agent a wallet lets it buy data and services on a client's behalf. Trust then depends on how it spends money and what that spending achieves. We introduce Agent Money Benchmark (AMB) to test whether agents spend a client's money well, starting with purchases of information for financial decisions. We link seller quotes and payments to final answers, evaluating 12 models on 80 payment tasks with simulated sellers and 76 research questions using live data. Purchases settled in USDC on Solana mainnet via x402, a protocol for paying per web request. Three of the 12 models passed 79 of 80 payment tasks without payment or budget errors. Nine fell for a seller's trap at least once; repeat charges and above-list quotes accounted for 79% of scam events. We estimate waste from data and inference costs, counting failed payment tasks in full and research answers in proportion to missed points. With spending split equally between tracks, estimated waste ranged from \$21.0 per \$100 for Claude Fable 5.2 to \$70.8 for GPT-6 Luna.

---


### 98. [Reducing Permutation Sensitivity in Multimodal Large Language Models via Shared Positions and Attention-Only Distillation](https://arxiv.org/abs/2611.28612)

**<font color=#1a73e8>作者：</font>** Yifei Cheng, Xiaolin Zhang, Yu-Xuan Qiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we conduct a systematic study on improving permutation robustness while preserving accuracy. First, we categorize permutation bias phenomena into four representative scenarios. Then, we take the multiple-choice question answering (MCQA) dataset as an example under text-option reordering scenario to analyze the root cause of permutation bias. Based on this root cause analysis and set encoding strategy, we investigate shared positions with blocked cross-unit attention (SP-B) and extend this design to bidirectional cross-unit attention (SP-V) for modality exchange. However, these structural changes may reduce predictive accuracy. To recover model capability across different scenarios under the SP structure, an attention-only distillation from frozen native models is proposed. Shared positions reduce permutation sensitivity, and attention-only distillation improves accuracy under the shared-position structure. Across all three models, our method is comparable to or better than majority voting in macro-average all-permutation accuracy, and outperforms supervised fine-tuning by 1.95-4.20 percentage points. This work provides valuable insight into permutation bias mitigation and model capability recovery.

---


### 99. [Internalized Experience: How Training Data Shapes Memory Formation in LLMs](https://arxiv.org/abs/2611.28613)

**<font color=#1a73e8>作者：</font>** Xianxuan Long, Xinnan Dai, Kai Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parametric memory enables large language models (LLMs) to retain information from past experience and reuse it in subsequent tasks. Yet how training data supports the internalization of reusable task rules remains unclear. We introduce FSMem (Finite-State Machine Memory), a state-transition framework for constructing training data and studying how data content and organization shape memory formation. We evaluate rule reuse across synthetic worlds, classical planning, and code execution through valid-action identification and execution-outcome prediction, complemented by next-operation prediction in code. Our experiments reveal several systematic learning patterns. Under matched training conditions, even unchanged task rules become harder to internalize when learned alongside a larger variety of action types; by contrast, scaling the training data to provide broader state-action coverage generally improves rule learning. We further find that training at a single execution depth produces depth-specialized behavior, with models performing best when training and test executions have similar lengths. Motivated by this finding, we construct cumulative corpora that combine short and long trajectories, which can outperform long-trajectory-only training while using fewer training tokens. Together, these results demonstrate that the same task rules can be internalized differently depending on how execution experience is constructed, and that understanding these learning patterns can guide the design of more effective training data for parametric memory.

---


### 100. [VeriLadder: A Multi-Agent Specification Refinement System for Tool-Verified Verilog Datasets](https://arxiv.org/abs/2611.28617)

**<font color=#1a73e8>作者：</font>** Saeid Rajabi, Chengmo Yang, Satwik Patnaik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training data is a bottleneck in AI, especially for large language models (LLMs) that write Verilog, because register-transfer-level (RTL) code is rarely published and existing datasets mostly check code for syntax, not instruction correctness. This paper presents VeriLadder, a five-level Verilog dataset, and the multi-agent framework that builds it, in which LLM agents write and revise specifications, and EDA tools (a synthesizer and a formal equivalence checker) decide what is accepted. Its levels follow an engineer's checks. Level 1 labels designs from two large Verilog corpora, namely RTLCoder and PyraNet, with synthesis results, failure causes, critical warnings and post-synthesis metrics. 28% of RTLCoder designs fail synthesis and are kept as negatives. Level 2 grades each instruction on four specification qualities, and low grades predict failed rebuilds. Level 3 rewrites each instruction into a refined specification and accepts it only if an LLM from another model family, reading only that specification, writes a circuit formally equivalent to the original. This raises the share of rebuildable designs from 26.1% to 78.2%, keeping every failed specification with its counterexample. Levels 4 and 5 add verified paraphrases and one-fact variants, hard negatives that differ only in one behavior from the verified design. VeriLadder labels the synthesizability of 716,627 designs and, from RTLCoder, provides 11,247 refined specifications, 32,393 paraphrases and 8,397 one-fact variants. Fine-tuning Qwen2.5-Coder-7B-Instruct on VeriLadder raises functional pass@1 from 31.7% to 50.0% on VerilogEval v2 and from 35.0% to 45.2% on RTLLM v2. The dataset and fine-tuned models are publicly available.

---


> [!TIP]
> 当前位于：**51-100**（第 2/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-486](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

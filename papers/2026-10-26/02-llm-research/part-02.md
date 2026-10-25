# 🧠 大模型相关研究 | 2026年10月26日

> 本类共 **241** 篇论文：已确认 **225** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-241](./part-05.md)

---

### 51. [Model-intrinsic, Weight-level, and Training-free Spectral Fingerprinting for Large Language Models](https://arxiv.org/abs/2610.30626)

**<font color=#1a73e8>作者：</font>** Yanan He, Yanli Chen, Ling Xiong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing release and reuse of Large Language Models (LLMs) as open-weight checkpoints make model fingerprinting important for ownership protection and offline auditing. Existing fingerprinting methods typically construct evidence from query responses, generated outputs, or input-induced activations. Although effective in representation-based settings, they can be affected by prompt selection, decoding configuration, inference environment, and forward-pass implementation, which may limit their applicability. Here we introduce a model-intrinsic weight-level framework that derives compact fingerprints from spectral structures encoded in LLM parameters. Specifically, the framework constructs GATE spectral scalar features from the singular-value distributions of GATE projection weights in gated feed-forward networks (FFNs), and aggregates the resulting layer-wise features through depth-wise segmented pooling to form a model-level fingerprint. Such representation preserves coarse layer-depth organization while reducing dependence on strict layer-to-layer alignment, enabling comparison across LLMs with different depths. The similarity between fingerprints is computed by linear centered kernel alignment. The entire pipeline is training-free and does not require input samples, generated outputs, forward activations, or an auxiliary verifier. Experiments on representative LLM families and post-training variants have demonstrated a clear separation between source-related models and unrelated ones, and stable similarity under instruction tuning, quantization, pruning, and distillation-related modifications, which verify that spectral features are robust evidence for LLM fingerprinting.

---


### 52. [Future of Time Series Anomaly Detection: From Historical Review to Unified Outlook](https://arxiv.org/abs/2610.30628)

**<font color=#1a73e8>作者：</font>** Zhijie Zhong, Zhiwen Yu, Pengyu Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series anomaly detection (TSAD) is a foundational problem in data mining, aiming to identify observations that deviate significantly from nominal temporal patterns. Driven by escalating data volumes and application complexity, recent research has yielded diverse architectures, including diffusion models, state space models, and large language models (LLMs). However, existing surveys provide limited coverage of these emerging designs and lack a unified treatment of multivariate anomalies, cross-domain unified modeling, metric reliability, and contemporary evaluation challenges. To bridge these gaps, this survey delivers three core contributions: (1) We establish a refined anomaly categorization and a structured taxonomy of paradigms reflecting modern advances, comparing detection mechanisms and charting developmental trajectories across paradigms. (2) We provide an extensive analysis of evaluation methodologies and conduct comprehensive experiments to assess metric fidelity, complemented by an open-source benchmark repository encompassing algorithms, datasets, and evaluation tools. (3) We outline key open challenges, offering forward-looking perspectives on dynamic thresholding, model interpretability, zero-shot transfer, multi-modal alignment, and foundational models for time series. By addressing existing theoretical and empirical limitations, this survey establishes a coherent framework to guide future TSAD research and practical deployments.

---


### 53. [Interpreting Model Reasoning through Behavioral Counterfactuals](https://arxiv.org/abs/2610.30630)

**<font color=#1a73e8>作者：</font>** Shawn Im, James Oldfield, Adel Bibi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Faithfully understanding the internal process that occurs as models form their chain of thought is an important problem with the rise in model capabilities. However, this remains challenging due to the variance in sampled responses, making it difficult to isolate the effects of interventions and compare model reasoning systematically. We propose a method for localizing and analyzing how a given intervention affects the model's reasoning through behavioral counterfactuals: given a fixed response, how does introducing an intervention to the prompt change the next-token distributions? We train a module to edit the residual stream such that it minimizes the KL divergence between the output distributions for a fixed response under a source prompt and its counterfactual target prompt. We find that matching the output distributions recovers the counterfactual behavior more effectively than standard activation reconstruction objectives and validate that attribution of the trained module outputs is effective for identifying causally important locations for counterfactual recovery. The attribution maps and visualizations of the downstream effects of model edits provide an interface for generating hypotheses about the original model's computation, which can then be tested with activation patching. In a case study on Gemma-4-E4B-it and DeepSeek-R1-0528-Qwen3-8B, we investigate how a suggestion influences model reasoning even when it is not verbally acknowledged. Our analysis identifies representations at the question statement and filler tokens that mediate a substantial part of the suggestion's influence, with downstream effects such as changing the framing of the justification or even the final answer.

---


### 54. [Large language models show systematic failures in incorporating evolving medical knowledge](https://arxiv.org/abs/2610.30631)

**<font color=#1a73e8>作者：</font>** Min Zeng, Zaifu Zhan, Kai Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical knowledge evolves as clinical guidelines revise recommendations, yet whether large language models (LLMs) faithfully incorporate such changes remains unclear. We introduce ChronoEvo, comprising 1,709 recommendation-level revisions across 12 forms of medical knowledge change, to distinguish recognition of revised guidance from incorporation into clinical recommendations. In the primary model, 90.8% of responses recognized revisions and 80.2% were clinically correct, but only 58.5% fully incorporated guidance, yielding a 32.3-percentage-point recognition-incorporation gap. This dissociation persisted across 14 models and was corroborated by two clinicians' adjudicated assessment of 300 responses, yielding a 40.3-percentage-point gap in the validation sample. Changes in recommendation strength and patient eligibility were associated with retention of outdated guidance. A revision-salience intervention reduced outdated-content retention and improved clinical correctness but did not significantly improve full incorporation. These findings identify faithful incorporation of evolving medical knowledge as a distinct challenge for clinical LLM reliability, even when updated guideline evidence is available.

---


### 55. [FedBST: Bilateral Self-Training for Unsupervised Federated Classification](https://arxiv.org/abs/2610.30634)

**<font color=#1a73e8>作者：</font>** Aijing Yu, Kuangpu Guo, Jian Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised federated learning with Vision-Language Models (e.g., CLIP) offers a promising solution for label-free classification, yet its performance often degrades under severe non-IID shifts. A pioneering method, FedCoPL, typically relies on self-training strategies that exclusively prioritize high-confidence predictions for pseudo-labeling. However, this selective approach neglects the information of ambiguous samples (often referred to as ``waist" samples), leading to the underutilization of data and biased decision boundaries. To address this limitation, we propose FedBST, a bilateral self-training framework that effectively exploits both high-confidence and ambiguous data. Specifically, for local optimization, we introduce uncertainty-aware confidence penalization (UACP). UACP targets ambiguous samples by penalizing overconfident predictions to implicitly promote higher uncertainty, thereby preventing erroneous pseudo-labeling. At inference, we employ a visual-text ensemble strategy. This approach aggregates uncertainty-aware local visual prototypes and ensembles them with textual prototypes, achieving lightweight adaptation to local distributions via prototype-based calibration. Experiments demonstrate that FedBST achieves consistent improvements over existing methods with standard federated aggregation protocols.

---


### 56. [What the Specification Did Not Say: Specification-Oracle Gaps in Test-Graded Coding-Agent Benchmarks](https://arxiv.org/abs/2610.30635)

**<font color=#1a73e8>作者：</font>** Fei Ding  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coding-agent benchmarks often describe a task in natural language but grade it with tests taken from the upstream project. Passing those tests can require information the description never states: a constant's name, a module path, an exact message. We call this a specification-oracle gap: where it exists, a benchmark also measures whether an agent reproduces upstream implementation details. We formalise the gap, including the inconsistencies that chains of dependent tasks add, and build a static audit for five languages that classifies every name-, path- and literal-level dependency of every scored test (held-out precision 89.2%, recall 92.9%). On SWE-Milestone (98 graded milestones, 35 published runs), 25 milestones contain a test that depends on an unstated, non-inferable name or path. Build units with such a dependency fail in 80.6% of runs, against 48.4% for comparable units without one, and withholding a single hidden name from the reference stops its unit's tests from compiling in 126 of 128 cases. The leaderboard's ranking is robust to removing the affected tests, but they shift scores within repositories and favour agents that reproduce upstream names. Across four further benchmarks, prevalence appears to follow construction: a third or more of the tasks are affected where specifications are release notes or LLM summaries, almost none where tasks are screened or written for their tests; how much a gap costs depends on how the harness grades. We release the audit, corrected filter lists and specification addenda.

---


### 57. [Speculative Acceptance Does Not Decay with Position: A Full-Length Diagnostic on Long Chain-of-Thought with Independent Drafts](https://arxiv.org/abs/2610.30644)

**<font color=#1a73e8>作者：</font>** Zhiming Meng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The claim that speculative-decoding acceptance rate decays as a chain-of-thought grows longer has become a de facto industry narrative, motivating draft-model co-design and position-aware training. Nearly all direct evidence comes from trained drafters whose offline training length is far shorter than inference, so a purely positional law has never been isolated. We present the first systematic, full-length measurement of acceptance rate as a function of generation position on MATH-500 (all 500 problems), under greedy and sampling decoding, with two independent drafts against DeepSeek-R1-Distill-Qwen-7B: a same-family draft (DeepSeek-R1-Distill-Qwen-1.5B) and a cross-family draft (Qwen2.5-1.5B-Instruct), yielding about 1.78M verification rounds. Using within-problem paired tests, we find that after isolating a greedy-decoding repetition pathology, acceptance rate does not decay with position in any of the four configurations within the supported ranges (greedy 0-8K, sampling 0-12K); the second half of each trajectory is slightly but significantly higher than the first. A controlled temperature sweep shows that the apparent sampling-mode degradation of high-entropy reflection tokens is a visibility artifact of argmax agreement, not a drop in expected acceptance probability. Rejections concentrate with high precision on reflection trigger tokens such as "wait", "however" and "check", an entropy-selective failure that a lightweight three-arm LoRA trajectory-alignment intervention (uniform, reflection-marked, entropy-weighted) fails to improve in mean accepted length. We thus supply the positional baseline that independent draft-target pairs were missing, and localize the residual failure to decision-point entropy rather than position.

---


### 58. [A Topology-Guided GeoAI Agentic Framework for Urban Flood Screening](https://arxiv.org/abs/2610.30660)

**<font color=#1a73e8>作者：</font>** Yutian Tao, Haoan Feng, Xin Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-world geographic artificial intelligence (GeoAI) agents can transform public geospatial data into accessible decision support for real-world challenges, but must balance autonomous reasoning with reliable spatial analysis and human oversight. We present a topology-guided GeoAI agentic framework for urban flood screening that takes a place name, drawn region, or uploaded boundary and returns ranked candidate basins with an interactive map and report. A deterministic controller retrieves public elevation, rainfall, soil, land-cover, exposure, and infrastructure layers, extracts terrain depressions with discrete Morse theory, and ranks basins with a relative flood-priority score. The language model acts only at recorded decision points: selecting a persistence threshold from a precomputed candidate table, drafting recommendations from computed evidence, and reviewing each recommendation against the same evidence. Three human-in-the-loop checkpoints let users revise the threshold, factor weights, or recommendation. In a College Park, Maryland case study, the selected threshold reduced 278 raw terrain minima to 70 basins, with 77% of these basins' lowest points also identified as sinks by a separately computed eight-direction (D8) flow-routing model. Across four further study areas, agreement ranged from 61% to 83%. By combining open data, explicit spatial reasoning, traceable evidence, and human oversight, the framework enables transparent first-pass flood screening while keeping consequential recommendations inspectable and user-controlled.

---


### 59. [Class-Grounded Batik Captioning under Scarce Text Annotation: Label Retention and Source-Specific Error Propagation](https://arxiv.org/abs/2610.30661)

**<font color=#1a73e8>作者：</font>** Novanto Yudistira, Muhammad Dzaka Aufa Fadhillah, Irawati Nurmala Sari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class labels offer compact supervision for describing cultural-heritage images when expert text annotations are scarce. We investigate a batik-captioning cascade that integrates a LoRA-adapted DINOv2 classifier with Qwen2.5-VL-7B, adapted using LoRA and loaded in 4-bit NF4. A $3\times2$ evaluation combines three captioner conditions with two inference prompts to examine adaptation and predicted-class injection. Across 150 caption-evaluation images, all three injected conditions achieve a ground-truth class-label mention rate of 0.9067. The classifier's separate test yields 96.10% pooled accuracy, with 98.33% on 300 public-source images and 75.76% on 33 local images. Supported-class macro-F1 and balanced accuracy on the local subset are 0.8493 and 0.8302, respectively. The classifier and captioner use separate partitions, and their training--evaluation overlap remains unquantified. Differences in label semantics and training support also affect interpretation of the source-specific accuracy gap. Reference-based caption metrics and image--text compatibility scores produce different model rankings. Qualitative examples show both retention of correctly predicted identities and propagation of classification errors into fluent descriptions. These findings characterize how class conditioning preserves label information and transfers upstream errors into batik captions under scarce text annotation.

---


### 60. [Group Relative Policy Optimisation Improves Multilingual Speech Recognition in Low-Resource Languages](https://arxiv.org/abs/2610.30663)

**<font color=#1a73e8>作者：</font>** Tim Wenjie Hu, Evelyn Nafula Ouma, Benjamin Akera 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoregressive encoder-decoder speech recognition models trained with teacher forcing can suffer from exposure bias, limiting their ability to recover from their own prediction errors at inference time. Recent work has shown that reinforcement learning with Group Relative Policy Optimisation (GRPO) improves speech recognition in major languages with LLM-based models. We extend this line of work to smaller, non-LLM encoder-decoder ASR models, using Whisper-large-v3 as a case study across 51 African languages. The benefits of this approach are most pronounced when training data is scarce or when input audio is noisy or degraded. Our resulting model, SunflowerASR, achieves the best published macro-averaged WER on the AfriVox-v2 (0.227) and SimbaBench (0.372) benchmarks, and is publicly available.

---


### 61. [Compiling Autoregressive LLM Control into Policy-Exact Parallel Inference for Hierarchical RAG](https://arxiv.org/abs/2610.30664)

**<font color=#1a73e8>作者：</font>** Zehao Lin, Qianfeng Shen, Xixuan Hao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly act as controllers in structured decision pipelines, yet their decisions are still executed by autoregressive text decoding. Hierarchical RAG is one such setting: at each frontier of a document tree, an LLM commits to $b$ of $k$ sections under an input-dependent action grammar, executed as either failure-prone free-form JSON or reliable but strictly serial grammar-constrained generation. We show that this serialization is unnecessary for bounded-horizon control: the reachable future forms a shallow action-prefix tree, which we compile --- one root prefill plus one tree-causal probe evaluate every prefix-conditioned action distribution with serial decoding's tokens, positions, and causal ancestry. A prefix-state lemma makes compiled control policy-exact in exact arithmetic: the same policy with a two-forward critical path and zero output tokens. One further probe pass certifies the exact order-marginalized MAP set. Across four document-disjoint splits and two scales on the primary MetaX device, compiled control matches the serial policy on $84$--$89\%$ of questions --- every instrumented divergence a floating-point near-tie --- and cuts control latency by $35$--$47\%$ versus token-wise serial decoding and $6$--$7\%$ versus an idealized chunked engine; an H800 repetition preserves the ordering.

---


### 62. [Your Token Is Gone: A Token-Consumption Countermeasure for Disrupting LLM-Based Scam Systems](https://arxiv.org/abs/2610.30666)

**<font color=#1a73e8>作者：</font>** Fudu Xing, Kailong Wang, Tianlong Yu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based scam systems increasingly combine adaptive dialogue, persistent context, external tools, and multi-agent coordination to automate personalized fraud. These capabilities also create a resource dependency: every reasoning step, model call, and coordination round incurs inference cost. We present TokenTrap, a resource-oriented defense that redirects suspected scam systems toward benign, low-value computation while withholding credentials, payments, and other exploitable information. TokenTrap combines three components: an architecture-specific token-task library, a router that selects among single-agent, hierarchical, and flat multi-agent workflows, and a bounded anti-guardrail strategy that varies task presentation while enforcing token, round, time, and safety limits. Across 50-round traces, TokenTrap amplifies token consumption by $2{,}487.0\times$, $1{,}616.0\times$, and $567.8\times$ relative to a no-token-task baseline for the three workflows. Its router achieves 85.67% accuracy on 300 architecture-labeled prompts. These results demonstrate that short, non-sensitive requests can impose substantial context-processing and coordination costs, motivating resource-aware defense as a complement to scam detection.

---


### 63. [Spectral Smoothing and Spiking Perturbations Reconfigure Capability Profiles and Selective Task Performance in Large Language Models](https://arxiv.org/abs/2610.30676)

**<font color=#1a73e8>作者：</font>** Qince Luan, Jianhui Xu, Yang Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Singular-value spectra encode important structure in transformer feed-forward projections, yet their causal role in downstream behavior remains underexplored. We study post-hoc spectral smoothing and spiking interventions on the up_proj and down_proj matrices. Positive perturbation stretches deviations from the geometric mean, making large singular values larger and small ones smaller (spiking), and vice versa. The intervention preserves singular vectors and the geometric mean of the singular values. Across five open Llama and Qwen instruction models, we evaluate the perturbed systems on capability-labeled subtasks, standard and chain-of-thought reasoning benchmarks, judge-scored truthfulness, hallucination, and safety tasks, and TRAIT personality probes. To interpret score shifts, we fit responses in a three-dimensional capability basis consisting of factual knowledge, language understanding, and deductive reasoning. The induced changes suggest structured rather than purely random sensitivity: large positive perturbations more reliably suppress language and deductive responses, moderate negative perturbations can sometimes improve factual or task-local performance on the evaluated grids, and sensitivity varies strongly by model family, benchmark module, and underlying layerwise spectral inequality. These results position spectral perturbation as a lightweight intervention for probing how capabilities are organized and traded off in large language models.

---


### 64. [WikiOriginQA: Automated Construction of a QA Dataset with Knowledge Origins for Analyzing Cultural Bias](https://arxiv.org/abs/2610.30677)

**<font color=#1a73e8>作者：</font>** Kento Haneda, Yosuke Kishinami, Ryo Fujii 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing datasets on cultural knowledge have been typically created by human annotators familiar with each culture. However, the process requires considerable human effort, presenting a significant challenge to scalability. To address this challenge, we introduce WikiOriginQA, a QA dataset automatically constructed by objectively representing the origins of knowledge through the creation dates of different Wikipedia language editions. Experimental results with the created dataset confirm that LLM performance tends to be biased toward Anglophone cultures. Furthermore, the results suggest the importance of knowledge propagation into the Anglosphere. These findings demonstrate the validity of our automated approach, enabling cultural bias evaluations with superior scalability across diverse languages without extensive manual annotation.

---


### 65. [Scaling Laws for Safety Probes](https://arxiv.org/abs/2610.30678)

**<font color=#1a73e8>作者：</font>** Yuchen Wu, Jerry Wei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety probes trained on a model's activations are a standard tool for monitoring language models in real time. Each time a new model is released or a new harm area needs to be monitored, the probe must be retrained, which requires new labels and a choice of probe architecture. Yet neither the model nor the labels tell us in advance how well the resulting probe will perform. Finding out requires training and comparing many probe configurations. In this paper, we ask whether probe performance can instead be predicted in advance from model size and the number of labels. Existing safety datasets are insufficient for this, as they are either limited in scale or already saturated. We therefore construct six new safety datasets of sufficient size and difficulty. On these datasets, we train two probe architectures on 20 base models from five model families, with 32 to $10^{6}$ labels for each model. We measure performance using probe error, defined as 1 - AUROC, where lower values are better. We find that probe error follows two simple scaling laws. First, the lowest probe error a model can reach falls as a power law in its size. Second, probe error decreases towards its floor as the number of examples increases; the slope increases as the target model size increases. Both laws hold across tasks, model families and probe architectures, and only their fitted constants differ. When fitted on the smallest models of a family, the laws predict the error of the next larger model to within 0.02 in 72% of cases. They also identify whether more labels or a larger model is the cheaper way to reach a target error in 73% of cases. Finally, they choose the probe architecture with an extra error of only 0.006 on average when they pick the worse one. These laws allow safety researchers to determine how to create the best probe for any given model and label budget.

---


### 66. [Zero-Shot Domain Generalization via Domain Prompt Learning](https://arxiv.org/abs/2610.30680)

**<font color=#1a73e8>作者：</font>** Shiming Chen, Shuhuang Chen, Salman Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain generalization (DG) aims to improve
the generalization of the model to any unseen domains. Targeting this goal, existing DG methods mainly focus on learning domain-invariant features or prompts from the given source domains. However, these methods rely on source-domain data, and collecting and annotating large-scale single- or multi-source datasets is often infeasible, limiting the practical applicability of DG. To tackle this challenge, we propose {\underline{Do}}main \underline{P}rompt Learning (DoP), a method built on a large vision-language model (e.g., CLIP) for zero-shot domain generalization, which recognizes unseen classes in unseen target domains without access to source-domain data. DoP essentially learns the target domain knowledge via prompt both in text and visual modalities to overcome the domain shift in text-visual modalities under the test-time adaptation formulation. Specifically, DoP first takes text domain learning (TDL) to simulate various distribution shifts by learning diverse style tokens implicitly in the text space with inter-style diversity loss and intra-style consistency loss. Subsequently, DoP employs visual domain learning (VDL) to further refine the target-domain-relevant style token generated by TDL by making use of the test visual data with self-supervised learning. Extensive experiments on popular DG benchmark datasets (e.g., PACS, VLCS, OfficeHome, and DomainNet) and ImageNet show that our DoP consistently outperforms the state-of-the-art DG approaches. Codes are available at: this https URL.

---


### 67. [Disentangling Robustness and Sycophancy in Multilingual LLMs](https://arxiv.org/abs/2610.30696)

**<font color=#1a73e8>作者：</font>** Rhitabrat Pokharel, Ameeta Agrawal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a multilingual LLM agrees with a user's false premise, is it being sycophantic, or does it simply not know better in that language? Current research does not distinguish these cases: they record only whether the model agreed, not why. We introduce the SC-matrix, that crosses a model's competence (whether it answers correctly under no pressure) with its sycophancy (whether it maintains that answer under pressure). Our results show that (1) identical aggregate sycophancy rates can mask different failure compositions, (2) high competence in a language does not always protect against sycophancy, and (3) reasoning-oriented mitigations outperform directive-based strategies. We find that multilingual sycophancy is not a single phenomenon but a composite of different failures that require distinct diagnosis.

---


### 68. [Governance-State Corruption in Long-Term Memory for LLM Agents: A Cross-Model Stress Test](https://arxiv.org/abs/2610.30698)

**<font color=#1a73e8>作者：</font>** Bowen Liu, Youting Wang, Bonan Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An LLM agent can retrieve a memory correctly yet use it incorrectly after its validity state changes. We study governance-state corruption: faults that alter which retained records enter model-visible context while stored content and tasks remain fixed. Across six providers, 731 benchmark-grounded bases yield 2,080 matched fault pairs. In offline control-plane checks, corruption changes the operative projection in 96.25% of pairs, while oracle-backed enforcement restores it in 100%. For downstream evaluation, a deterministically selected, non-probability LongMemEval/Memora panel resolves 298 of 300 matched triplets (238 distinct bases). Clean-minus-corrupted contrasts are 40.54 percentage points in LongMemEval binary correctness (95% base-cluster interval [30.32, 50.71]) and 30.60 points in rescaled Memora FAMA ([23.31, 37.69]); both sources also show recovery. OAKS Novel native option parity holds for all 6,714 resolved outputs. Full-cohort frozen-scorer corruption/recovery effects (-27.55/+27.51 points) remain descriptive proxies, not validated native semantic population effects. These bounded findings motivate evaluating memory control-state integrity alongside retrieval accuracy.

---


### 69. [ULME: Predictive Coupling for Mutually Reinforcing Embedding and Language Modeling](https://arxiv.org/abs/2610.30705)

**<font color=#1a73e8>作者：</font>** Yang Liu, Zhiqiang Yuan, Shu-Dong Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text embedding and text generation are two of the most useful capabilities of modern large language models, yet they are typically provided by separate specialized models (an embedder and a generator) trained with incompatible objectives and deployed side by side in retrieval-augmented generation and agent systems. Recent unified embedding-generation models such as GritLM share parameters between the two capabilities, but they either switch attention regimes between modes or optimize embedding and language modeling as parallel objectives that never supervise each other. We argue that these designs are only partially unified: the two capabilities coexist on the same weights, but do not shape each other. We propose ULME, a post-training framework that unifies embedding and language modeling on a causal decoder-only LLM through predictive coupling. ULME inserts a chain of learnable slots between the query and the answer, reads a semantic embedding and a reasoning embedding from two designated slots, and trains three objectives on a shared causal backbone: a contrastive loss anchoring the semantic slot to document representations, a language-modeling loss supervising answer generation, and a stop-gradient predictive loss that aligns the reasoning slot with a pooled summary of the answer, so that generation actively shapes what the embedding encodes. Across two model families (Qwen2.5, Qwen3) and eight scales spanning 0.5B-8B parameters, a single ULME checkpoint improves MTEB by 3.3-4.1 points over the strongest open-source baseline, tightens BRIGHT and AdvBench-IR simultaneously, and remains on par with a generation-only fine-tune on standard accuracy benchmarks (MMLU, GSM8K, MMLU-Pro, HumanEval), demonstrating that genuine unification yields mutually reinforcing rather than merely coexisting capabilities.

---


### 70. [Meaning Contracts: Local Semantic Geometry in Large Language Models](https://arxiv.org/abs/2610.30715)

**<font color=#1a73e8>作者：</font>** Andrés Daniel Godoy Ortiz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper studies the local geometry of semantic meaning in large language models. Current representation analyses ask whether meanings are close in embedding space, or whether linear probes separate semantic classes, but they do not characterize the within-concept local geometry: what is invariant across realizations of a single semantic factor, what varies, and what changes when meaning is refined. This paper characterizes that geometry through two controlled probes evaluated on four architecturally diverse decoder-only LLMs (Gemma 4, Llama 3.2, Qwen 2.5, Pythia). A cross-lingual probe uses language as a perturbation to separate exact meaning matches, same-factor realizations, nearby concepts, and out-of-domain contrasts. A refinement probe separates specificity-bearing semantic narrowing from high-probability attributive elaboration and adversarial controls; both probes are validated by blind human judgments. Four findings recur across all models: under mean pooling, once dominant variance directions are removed, sentence pairs order by semantic relatedness (same factor, then same domain, then different domain) without overlap over a band of layers; semantic factors organize around an invariant core surrounded by structured realization-specific variation; refinement produces directed displacement into tighter neighborhoods, including against controls built on the same base noun; and sentence-level and token-local readouts expose complementary geometry (volume contraction at the sentence level, sharper anisotropic endpoints at token-local readout). We interpret these results as evidence that LLM semantics are organized as local anisotropic neighborhoods in which meaning contracts under refinement.

---


### 71. [Faithful Latent Harm Monitors Work No Better Than the Models Own Behaviour at a Matched False Alarm Rate](https://arxiv.org/abs/2610.30727)

**<font color=#1a73e8>作者：</font>** Abhishek Mishra, Sagnik Chatterjee, Suyash Maniyar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have been reported to encode the harmfulness of a request separately from their decision to refuse it, and latent safety monitors such as Latent Guard build on this report by classifying prompts as harmful from the internal activations of the model, with the aim of catching harmful intent even when the model complies. Whether these representations give a signal of harm that survives distribution shift and is independent of model behaviour is unclear. We test this on out-of-distribution prompts made by rewriting existing harmful and benign requests with surface rewording, persuasive framing and jailbreak-style wrappers. Across 15 instruction-tuned LLMs and 38 activation-based readers, we compare harm detection with that of TF-IDF and sentence-embedding classifiers, with independently trained safety classifiers, and with the refusal of each model. Activations are read at the last token of the user instruction, where the model has read the whole request, and at the last chat-template token before the reply, where the planned response can be represented. Because models disagree about which prompts to refuse, we can separate a signal of the harmfulness of the prompt from a signal of the refusal decision of the model. At the end of the instruction, the representation is largely independent of the refusal behaviour of each model but degrades under distribution shift, so that a TF-IDF classifier ranks harm better than the original Latent Guard in every model we test, and linear and MLP probes do about as well as sentence-embedding classifiers trained on the same examples. The representation just before generation detects more, catching 44 percent of harmful prompts at a matched false-alarm rate against 32 percent for the refusal of the model, but that gain follows the refusal decision itself, and part of it comes from refusals that string-matching evaluation misses.

---


### 72. [Federated Graph Retrieval-Augmented Generation](https://arxiv.org/abs/2610.30728)

**<font color=#1a73e8>作者：</font>** Xiaobao Wang, Renda Han, Zhiliang Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Retrieval-Augmented Generation (GraphRAG) leverages centralized knowledge graphs to enhance large language models with structured knowledge retrieval. However, real-world knowledge is inherently distributed across multiple organizations rather than being centrally accessible. Privacy constraints further prohibit sharing entire local knowledge graphs, preventing GraphRAG from effectively retrieving and utilizing distributed knowledge. To this end, we propose Federated GraphRAG (FedGRAG), a unified framework for distributed graph retrieval and knowledge-enhanced generation over multiple clients with knowledge graphs. Specifically, we address two fundamental challenges in federated GraphRAG. First, the absence of a global knowledge graph makes unified retrieval impossible. To address this, we develop a Federated Knowledge Routing mechanism that efficiently identifies relevant clients through lightweight knowledge indices without exposing local graph structures. Second, local graph memory cannot be shared directly because it contains sensitive entities and knowledge information. We therefore propose a controlled-disclosure evidence construction method. It extracts retrieved evidence subgraphs and converts them into an evidence abstract, enabling evidence conversion and reconstruction on the server. Extensive experiments demonstrate that Federated GraphRAG consistently outperforms existing baselines in both retrieval and downstream generation tasks, establishing a new paradigm for deploying GraphRAG in federated environments.

---


### 73. [SmolVLA-MoE: Sparse Mixture-of-Experts for Efficient Multi-Task Robotic Manipulation](https://arxiv.org/abs/2610.30732)

**<font color=#1a73e8>作者：</font>** Shiyang Zhang, Miao Yang, Zhengda Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have shown promising results in multi-task robotic manipulation by leveraging visual and language understanding for action generation. However, existing lightweight VLA models employ a single dense action expert to handle all tasks, which limits their multi-task capability under constrained computational budgets. To address this issue, we propose SmolVLA-MoE, a novel framework that introduces sparse Mixture-of-Experts (MoE) into the FFN layers of the action expert in VLA models. SmolVLA-MoE replaces dense FFN layers with multiple parallel expert FFNs and a token-level router, enabling each token to adaptively select the most suitable expert for action generation. We further introduce a shared expert with a tunable weight parameter to balance the inheritance of pre-trained capabilities and task-specific expert specialization. Through sparse activation, SmolVLA-MoE activates only a single expert FFN during inference, with a total activated parameter count of approximately 500M including the frozen VLM backbone, while benefiting from approximately 800M total stored parameters. We evaluate our method on four task suites of the LIBERO benchmark. SmolVLA-MoE achieves an average success rate of 84.25%, outperforming SmolVLA (82.75%) and OpenVLA-7B (76.5%), while maintaining comparable inference efficiency. Our code is publicly available at this https URL.

---


### 74. [AgentTriage: Replayable Security Diagnosis Across Heterogeneous Agent Runtimes](https://arxiv.org/abs/2610.30738)

**<font color=#1a73e8>作者：</font>** Jie Ying, Xutao Zhang, Ningyuan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When tool-use agents write files, execute code, or send data, their final responses do not explain the resulting security events, and heterogeneous runtimes expose the relevant evidence through incompatible interfaces. We present AgentTriage, an executable contract for replayable security diagnosis across heterogeneous runtimes. The contract admits conclusions whose claims cite canonical runtime events and requires abstention when mandatory evidence is missing. Runtime overlays normalize native observations, while a deterministic pipeline joins invocation and result lifecycles, constructs a typed provenance graph, selects a policy-decisive slice, and binds claims to recorded evidence. Given the same normalized trace, overlay version, and pre-run policy oracle, the diagnosis can be recomputed and its claims re-checked without language-model judgment. Across five runtimes, one contract captures all 159 applicable executions, with an audit of native and synthesized identifiers. On 120 adjudicated cases, AgentTriage achieves 0.858 grounded joint diagnosis, 0.966 required-evidence coverage, and a 0.036 unsupported-claim rate, improving joint diagnosis by 0.175 (95% CI [0.092, 0.258]) over the strongest same-schema baseline. These results quantify the precision of replayable diagnosis and the observation boundaries that require abstention. We release an open-source implementation and selected sanitized evidence at this https URL.

---


### 75. [Where Did the Light Come From? Diagnosing Cast-Shadow Reasoning in VLMs and Borrowing the Missing Shadow Prior from Image Generation Models](https://arxiv.org/abs/2610.30740)

**<font color=#1a73e8>作者：</font>** Ryugo Morita, Shunsuke Kitada, Stanislav Frolov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shadows are observable consequences of latent physical causes, arising from the interaction between illumination, object geometry, and scene structure. A model that understands shadows should be able not only to read a shadow's direction, but also to infer where a shadow should fall when it is absent, and to judge whether a shadow is physically consistent with the scene. We introduce ShadowBench, built from real photographs, which poses these three questions to vision-language models (VLMs). From each scene, we build a correct-shadow, a shadow-removed, and a human-annotated wrong-direction state. Evaluating 19 open VLMs (2B to 78B) and frontier proprietary models, we find that VLMs read a visible shadow's direction well above chance and improve with scale, yet infer the absent direction only weakly and fall to chance at judging physical consistency even under a bias-free two-alternative test that removes the yes-bias of single-image naturalness questions. Only Gemini-3.1-pro exceeds chance on validity, and even then only modestly and far below humans. Chain-of-Thought (CoT) does not help. The missing ingredient is not reasoning but knowledge that image generation models (IGMs) already hold. Routing a VLM through an IGM lifts its inference well above its direct attempt and helps it flag the wrong-direction shadows it otherwise accepts. Cast-shadow direction is a single facet of illumination understanding, but the sharp gap it reveals between VLMs and IGMs suggests image-generation or reconstruction objectives as a route toward illumination-aware VLMs.

---


### 76. [Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought](https://arxiv.org/abs/2610.30755)

**<font color=#1a73e8>作者：</font>** Zhengye Bao, Shengtao Zhang, Haokai Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM memory is widely used in long-term conversation understanding. Agentic memory systems often use mutation, structural organization, learned retrieval strategies, or other complex operations. Is this complexity always necessary? We study Raw-RAG, a naive RAG baseline using dense retrieval and reranking over raw history to supply evidence to a reader LLM. Across LoCoMo, LongMemEval, MEME, and MemoryAgentBench, Raw-RAG ranks first among the compared memory systems in six of seven benchmark-model settings, outperforming the strongest compared agentic memory system by 0.13-5.53 points. We investigate why raw-history retrieval remains competitive. Evidence analysis shows that its higher coverage of necessary evidence can offset lower utilization. Useful evidence includes both answer values and the relations and dependency paths needed to derive them. Even complete access to transformed memory stores leaves an accuracy gap relative to raw evidence, highlighting the importance of preserving raw information. These findings challenge the necessity of complex agentic memory for the evaluated conversation tasks and establish naive RAG as an essential baseline.

---


### 77. [AgentDP: Towards Automated Model Deployment for Heterogeneous Embedded AI Applications](https://arxiv.org/abs/2610.30760)

**<font color=#1a73e8>作者：</font>** Leming Shen, Qiang Yang, Xinyu Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents AgentDP, which aims to deploy pre-trained AI models on heterogeneous embedded devices by fully automating model optimization and adaptation (O&A) with Large Language Model (LLM) agents. AgentDP not only significantly reduces human effort via automation but also enhances model inference efficacy by integrating LLMs with device-specific domain knowledge. To deliver a robust automation framework, AgentDP develops novel solutions to address three key technical challenges: 1) To help users elicit clear requirements, we propose a user requirement standardization module; 2) To mitigate the execution environment mismatch between AI models and heterogeneous embedded devices, we design an operator-aware model partition paradigm that enables different parts of the model to be efficiently executed on distinct inference engines. 3) To avoid re-searching optimization hyperparameters for new tasks, we propose a configuration reuse module that heuristically retrieves previous hyperparameter configurations for efficient reuse. Extensive experiments demonstrate that by fully automating the entire O&A process, AgentDP reduces entire model adaptation time by up to 80% compared with manual O&A while achieving higher task accuracy (more than 13% on average) than the baselines. Additionally, a comprehensive user study also exhibits the robust generalizability of AgentDP in adapting to different user requirements for heterogeneous embedded devices.

---


### 78. [Abstract Priorities, Concrete Rewards: How Stated Preferences Relate to What People Reward in AI Responses](https://arxiv.org/abs/2610.30763)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Lei Nico Zheng, Di Zhu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI assistants built on large language models (LLMs) are trained on human feedback and increasingly personalized to users' stated preferences. Yet how closely these preferences reflect what people reward in responses remains unclear. We compare stated and revealed preferences in the public PRISM dataset, in which 1,396 participants reported how much seven response attributes mattered to them and then rated 29,347 responses from 21 LLMs. Among responses to the same prompt, features the survey never asked about, such as response length, formatting and refusal language, were at least as strongly associated with ratings as text proxies of the surveyed attributes. Whether stated priorities matched ratings depended on how attributes were measured: participants who prioritized an attribute favoured responses from models that others perceived as strong on it, but not responses that scored higher on text proxies for it. Written feedback was more telling: participants who asked for shorter answers, even in earlier conversations, gave length less weight in their ratings, and those asking for longer answers gave it more. Their relative priorities over the surveyed attributes, however, did not predict this weight. Reasons given for choices reflected perceived attributes more than measured features. Participants also differed stably in how much they weighted several concrete features, especially length, but with a median of 6 conversations per participant, these weights were estimated poorly. The largest gain from personal information in predicting held-out choices was 0.13 percentage points, compared with 1.11 for a stronger pooled model. Stated priorities thus track perceived attributes of AI responses but say little about the concrete features that ratings reward, a distinction that matters for preference elicitation and AI personalization.

---


### 79. [Scaling Laws for Generative Reward Models](https://arxiv.org/abs/2610.30765)

**<font color=#1a73e8>作者：</font>** Angel Raychev, Nathan Lile, Rafael Rafailov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study generative reward models (GenRMs) as online preference providers for policy optimization in creative writing. Across Qwen3 reward-model sizes from 0.6B to 14B, Thinking judges trained with GRPO have higher static Gold-label accuracy than Answer-Only judges trained with SFT. This ranking often reverses when the judges train policies through online DPO: Answer-Only rewarders yield higher peak and top-five-average policy Elo in seven of eight matched settings under a fixed, learned 32B Gold evaluator. Intermediate Thinking-judge checkpoints can also outperform later, more statically accurate checkpoints as rewarders. Sweeps over rewarder size, policy size, training duration and DPO regularization show substantial benefits from reward-model capacity, including judges larger than the policy. We analyze trajectories with evaluator-specific Elo arenas, conditional match-resampling intervals and descriptive scaling fits. These results demonstrate an evaluator-rewarder gap in the studied pipelines: fixed-distribution judging accuracy does not determine downstream optimization quality. The comparison changes judge-training objective as well as response format, and the main ranking is conditional on its learned reference rather than a universal human-quality result. A limited follow-up using a different learned judge is inconclusive overall.

---


### 80. [LLM Multi-Agent Systems Are Vulnerable to Herding and Runaway Cascades](https://arxiv.org/abs/2610.30769)

**<font color=#1a73e8>作者：</font>** Farnoosh Hashemi, Shiyu Ji, Joice Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly operate in multi-agent systems where they collaborate by responding to others' choices, creating endogenous feedback loops with vulnerability to social influence, herding behavior and runaway cascades. Following the design of the classic Music Lab experiment, we tested this vulnerability in large populations of LLM agents that recommended unfamiliar songs, with or without exposure to cumulative recommendation counts. Exposure led to runaway cascades that generated extreme and unpredictable collective recommendations increasingly divergent from a song's intrinsic appeal. Compared to humans, LLM populations were generally far more susceptible to herding behavior, and unlike humans, LLM cascades were less able to self-correct. This vulnerability has implications for multi-agent collaboration in recommender systems, automated evaluation, complex problem-solving, and unauthorized conspiracies.

---


### 81. [One Pretrained Decision Model Is Enough for Training-Free Generalist Graph Anomaly Detection](https://arxiv.org/abs/2610.30777)

**<font color=#1a73e8>作者：</font>** Xinyu Zhao, Qingyun Sun, Ziwei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph anomaly detection (GAD) aims to identify irregular entities in graph-structured data, yet heterogeneous anomaly patterns and distributional differences across graphs challenge generalizable detection. Existing training-free approaches avoid task-specific optimization but primarily rely on predefined numerical scoring rules, leaving the semantic interpretation of heterogeneous anomaly evidence largely unexplored. In this paper, we propose Jev-GAD, a training-free generalist graph anomaly detection framework that bridges heterogeneous numerical evidence and pretrained decision mechanisms. To address heterogeneous anomaly patterns, we construct complementary structural, attribute, and neighborhood evidence and transform heterogeneous statistics into graph-relative anomaly percentiles. To move beyond predefined numerical scoring rules, we leverage a single frozen pretrained language model for evidence-conditioned anomaly assessment. To bridge the semantic gap between numerical evidence and pretrained models, we design a semantic Graph-to-State (G2S) transformation that organizes graph context and semantically labeled node evidence into structured decision states for non-generative option-logit readout. The resulting decision scores are integrated with four complementary statistical scores through equal-weight rank-based fusion, without GAD-specific gradient-based optimization. Extensive experiments on seven graph anomaly detection benchmarks spanning citation, social, and co-review networks demonstrate the effectiveness of Jev-GAD, achieving average AUROC and AUPRC scores of 89.18\% and 52.40\%, respectively. Further analyses validate the contributions of pretrained decision readout and semantic evidence grounding.

---


### 82. [ProQuant: Preserving Expert Quality over Quantity in Ultra-Low-Bit Quantization of Mixture-of-Experts Models](https://arxiv.org/abs/2610.30779)

**<font color=#1a73e8>作者：</font>** Jiaqi Chen, Xianglong Yan, Chengzhu Bao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) large language models reduce computation through sparse activation but still incur substantial storage costs. Mixed-precision post-training quantization (PTQ) reduces these costs by quantizing different model components at different bit widths, but existing methods often struggle to preserve generation quality under tight bit budgets. We identify two key challenges: (1) nonlinear quantization errors at extremely low precision are underestimated when cross-layer propagation is ignored; (2) direct router fine-tuning may cause routing drift, and calibration gains may not generalize to downstream tasks. To address these issues, we propose ProQuant, a weight-only PTQ framework for MoE models. Prune-or-Prioritize Mixed-Precision Allocation (PoP) jointly optimizes expert pruning and bit-width assignment. It allows higher-precision experts to substitute for severely degraded ones while improving bit-budget utilization. Routing-Consistent RMSNorm Finetune (RoCo) adapts expert input representations through mathematically equivalent transformations. It compensates for quantization errors to reduce routing drift. Extensive experiments demonstrate that ProQuant outperforms existing methods across diverse generative tasks. Code is available at this https URL.

---


### 83. [ABRA: Agent-Bound UI for Human-Agent Communication beyond Chat with Reusable Views](https://arxiv.org/abs/2610.30780)

**<font color=#1a73e8>作者：</font>** Seon Gyeom Kim, Hannah Kim  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Agents can create rich representations, yet these representations are rarely used as a medium for expressing user intent. We present Agent-Bound UI, an interaction model that separates reusable interaction structures from task-specific meanings. Agents bind task-specific meanings to interactions in reusable views and publish the resulting bindings as shared state, enabling humans and agents to understand and act on shared surfaces whose meanings vary across tasks. We implement ABRA, a framework-agnostic prototype of Agent-Bound UI, in which users and agents collaborate through chat and shared interactive canvases. We demonstrate ABRA through a representative use case and evaluate four LLM-backed agents on canvas authoring, owner-side consequence resolution, and cross-agent invocation. The code and demo video are available at this https URL.

---


### 84. [Invisibilization as a Source of Probability Bias in Language Models](https://arxiv.org/abs/2610.30785)

**<font color=#1a73e8>作者：</font>** Christian Arnold, Ernesto Calvo, Guadalupe Gonzalez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are aligned to avoid using protected attributes such as race, ethnicity, and gender to inform their responses. Therefore, they increasingly refuse or hedge when such attributes appear in a prompt. However, if a system must decide how much to learn from what people tell it, it is costly to refuse valuable information because of its source. In this article, we measure the cost of declining information in a two-urn game with an exact Bayesian answer. We present leading LLM models from two developers (OpenAI and Anthropic) with a prompt that requires them to decide how far to trust an unverifiable report from a participant whose description we randomize across ten configurations (6,600 sessions). We show that leading models often decline to assess the reporter, treating information as worthless at rates set by the description rather than by the evidence. At its widest, models decline a Black-described reporter 46% of the time and a white-described reporter 9%; yet, when they do assess the information, the Black-described reporter receives slightly more trust. The bias is invisible to audits that compare average trust or look only at assessed cases. It grows with reasoning effort, follows words rather than categories (models invoke race for "Black" but not for its Spanish translation negro, and never for "Indigenous"), and worsens under warning instructions a practitioner would try first. We also present a scoring option that reduces the refusal rate bias. When a model's trust is scored against revealed truth over repeated rounds, it credits identical records equally. In four of five configurations from Anthropic and OpenAI, the racial gap in trust falls below 0.02 by the last rounds.

---


### 85. [Agentic Knowledge-Model Co-Evolution via Consistency Regularization](https://arxiv.org/abs/2610.30790)

**<font color=#1a73e8>作者：</font>** Sirui Chen, Zhining Liu, Chao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents can evolve by learning from accumulated experience. Existing approaches extract reusable external knowledge, such as skills and memories, from experience to guide subsequent task solving, with some further internalizing this knowledge through model training. However, different ways of analyzing and transforming the same experience can yield knowledge with substantially different utility, even when the resulting guidance appears reasonable. Inspired by consistency regularization, we identify consistent utility gains across different ways of analyzing the same experience, rather than relying on any single way of analyzing it. We introduce SPLICE, a framework for consistency-regularized knowledge-model co-evolution. It constructs evolution views by perturbing how the same experience is analyzed, producing different knowledge candidates. Knowledge updates are then guided by common gain, which accounts for utility gains and their consistency across views. During model evolution, self-distillation internalizes the evolved knowledge alongside reinforcement learning, using knowledge associated with consistent utility degradation as a contrastive reference. The two processes interleave, with model updates driving further knowledge evolution. Experiments across diverse domains show that SPLICE outperforms knowledge evolution and model training baselines by up to 7.1 and 4.6 points in average accuracy, while its evolved knowledge reduces output tokens per correct solution by up to 44% and transfers across model sizes and families.

---


### 86. [Gandalf: Flash Shall Not Die! Increasing Flash Storage Lifetime for KV Cache Offloading in LLM Serving](https://arxiv.org/abs/2610.30791)

**<font color=#1a73e8>作者：</font>** Maharani A. P. Irawan, Kuntai Du, Jiayi Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV caching reduces the serving cost of large language models (LLMs), but the growing KV cache footprint is increasingly exceeds GPU and host-memory capacity. Therefore, people use SSD to expand the KV cache storage capacity with high I/O bandwidth. However, in production LLM workload, such as multi-round conversation and LLM agents, the total amount of KV cache writes significantly exceeds SSD capacity, shortening SSD lifetime from years to months. To improve SSD lifetime, a natural solution is to reduce the KV cache writes by gating the KV cache writes via historical access patterns. However, that significantly lowers the KV cache hit rate (and increase the LLM serving cost) since KV caches from different attention types might have identical historical access pattern but different future access patterns. Our insight is that, to reduce KV cache writes without hurting KV cache hit rate, one need to not only consider the access pattern, but also application-level information such as the attention type of KV cache. Leveraging this observation, we propose Gandalf , the first SSD KV cache offloading system with SSD life time awareness. Gandalf prioritize the admission of full-attention KV cache into SSD over the cache generated by other types of attention, which significantly increases SSD lifetime without sacrificing cache hit rate. Our evaluation shows that Gandalf extends the SSD lifetime by 7.3X on average, while having negligible impact on cache hit rate across multiple workload traces and wide range of hardware capacity. Gandalf design can be extended to other flash-based storage, such as High Bandwidth Flash (HBF).

---


### 87. [GIFT: Gradient Informed Filtering for Distillation Augmented Reasoning RL](https://arxiv.org/abs/2610.30796)

**<font color=#1a73e8>作者：</font>** Shijie Li, Yilin Gao, Tieyuan Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large language models for complex reasoning tasks relies on two complementary signals: sparse, outcome-grounded reinforcement learning (RL) for correctness, and dense, token-level distillation for guidance. However, complementarity in supervision does not guarantee compatibility in optimization; imitation-focused distillation can conflict with the outcome-driven RL objective, and existing hybrids lack a principled resolution. We propose \textbf{GIFT} (\textbf{G}radient-\textbf{I}nformed \textbf{F}il\textbf{T}ering for Distillation-Augmented Reasoning RL), a novel method that directly addresses the allocation problem of which teacher updates to apply. GIFT performs a token-level geometric analysis, decomposing the distillation gradient into a component \textbf{parallel} to the RL gradient, which measures first-order conflict and provides a \textbf{safety} filter, and a component \textbf{orthogonal} to it, which quantifies novel directional guidance and provides a measure of \textbf{value}. This decomposition yields a principled scoring rule to rank token-level guidance. We combine this with a progressive \textbf{coverage annealing} schedule that shrinks the budget of tokens receiving distillation, ensuring that the most conflicting updates are discarded first while the most complementary ones are retained at full strength. This facilitates a smooth transition from dense, geometrically-filtered guidance to a pure, outcome-grounded objective at convergence. Extensive experiments on mathematical and logical reasoning benchmarks show that GIFT consistently outperforms strong baselines across multiple model scales, achieving relative gains of up to 9.5\% on difficult mathematical reasoning tasks. Code: this https URL

---


### 88. [Amplifying Latency and Cost of LLM Inference via Rowhammer Attack](https://arxiv.org/abs/2610.30798)

**<font color=#1a73e8>作者：</font>** Mrityunjay Shukla, Shubham Roy, Biswabandan Panda  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve high inference efficiency using optimized GPU kernels generated by just-in-time (JIT) compilation frameworks such as Triton. Triton compiles GPU kernels through an MLIR/LLVM-based pipeline. We investigate whether a Rowhammer-induced bit-flip in the CPU's DRAM can degrade GPU-based LLM inference performance while preserving output correctness. We present LLVMhammer, the first Rowhammer attack that causes LLM inference slowdown by inducing a bit-flip in Triton's compilation pipeline. A bit-flip in a performance-critical optimization pass causes Triton to generate a functionally identical but suboptimal GPU kernel. Since Triton caches the generated kernel on disk, a single successful bit-flip causes persistent slowdown across subsequent inference executions. Triton's target-independent stages are shared across GPU vendors, which makes our attack GPU vendor-agnostic. To identify exploitable bit-flip locations without manual inspection, we build Karnage, a tool that isolates useful bit-flip locations in Triton's target-independent compilation pipeline. We evaluate LLVMHammer across a diverse set of LLMs, including Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3, and Deepseek-llm-7B-chat, across NVIDIA RTX 4090 and AMD RX 7900 XTX GPUs. LLVMhammer increases inference latency of an LLM inference server running on a single GPU by 4-16\%, which, in turn, can translate into additional annual operating costs at the scale of multi-GPU deployments. We further show that LLVMhammer can also corrupt LLM outputs across different GPU vendors, reducing BERTScore to as low as 25\%, illustrating the broader security implications of bit-flips in Triton's compilation pipeline.

---


### 89. [DRILL: Training World Models to Improve Policies, Not Predict Pixels](https://arxiv.org/abs/2610.30814)

**<font color=#1a73e8>作者：</font>** Zhaolu Kang, Tailong Luo, Lei Wei 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models are increasingly used to reduce environment interaction when post-training vision-language-action (VLA) policies with reinforcement learning. Yet they are typically trained to predict pixels one step ahead, even though their role here is not merely to render visually faithful videos but to produce learning signals from imagined rollouts that improve the policy. We show that this mismatch is substantial: lower pixel MSE can produce worse policy gradients, and a world model trained for policy utility can yield better downstream policies despite 17% higher pixel MSE on the next frame. We propose the Downstream-Return Imagination Learning Loop (DRILL), a bilevel framework that updates the world model to maximize the policy's return after an inner GRPO update on imagined rollouts. DRILL has two instantiations. DRILL-VWI is a closed-form surrogate, requiring no additional simulator rollouts, that reweights prediction errors by policy visitation, the group-relative GRPO advantage, and model confidence. DRILL-IMG is a full meta-gradient method that differentiates through the inner update using truncated Hessian-vector products. We show that DRILL-VWI recovers the local one-step component of the DRILL-IMG meta-gradient under score-compatibility and small-residual assumptions. Across five manipulation simulators and two VLA backbones, DRILL-IMG raises mean success rate by 13.1 points over WMPO and 7.9 points over RLVR-World, and complements RLVR pretraining rather than competing with it. More broadly, we believe video world models for VLA reinforcement learning can be productively trained by the policy gradients they produce, not only by pixel-level prediction.

---


### 90. [TESSA: A Governance-Oriented Custom GPT for SME Guidance under the EU AI Act: Design, Implementation, and Evaluation](https://arxiv.org/abs/2610.30822)

**<font color=#1a73e8>作者：</font>** Chalisa Veesommai Sillberga, Kai-Kristian Kemella, Pekka Sillberga 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The increasing adoption of generative AI presents new opportunities while raising AI governance and regulatory challenges, particularly for small and medium-sized enterprises (SMEs) navigating the European Union Artificial Intelligence Act (EU AI Act). To support AI governance education, this study developed TESSA, a governance-oriented educational artifact within the OpenAI Custom GPT environment. Following a design science research approach, TESSA was evaluated against baseline ChatGPT using 100 benchmark scenarios through governance alignment assessment, human expert review, and consistency testing. Preliminary LLM-assisted assessment showed governance alignment rates of 90% for TESSA and 83% for baseline ChatGPT, while independent validation by an AI regulation law practitioner yielded 71% and 70%, respectively. Human expert review indicated that both systems provided generally strong governance guidance, while TESSA maintained high consistency across repeated executions. The findings suggest that governance-oriented grounding can support structured, practical, and stable AI-assisted compliance guidance for SMEs. The study contributes (i) a governance-oriented Custom GPT artifact for AI governance education, (ii) a human-validated regulatory update mechanism, and (iii) a multidimensional evaluation framework for governance-oriented AI artifact.

---


### 91. [Neural Spectral Capacity with Residual Context for Heterogeneous Resource Allocation within Transformers](https://arxiv.org/abs/2610.30823)

**<font color=#1a73e8>作者：</font>** Chenyu Zhu, Ruoyu Zhao, Zhichao Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting relative trained performance from architectural specifications can guide design when training costs limit experimentation. Neural Spectral Capacity (NSC) provides such a heuristic, but scores projections independently and assigns identical scores to compatible reorderings of the same layer configurations. We introduce Residual-Aware Neural Spectral Capacity (ResNSC) for Transformers, using a specification-derived statistical reference for accumulated residual updates to determine the input and residual-state statistics in each projection's capacity calculation, while retaining additive evaluation without data or instantiated weights. When residual widths vary, earlier choices affect later scores, so we augment NSC's allocator (NSC-DP) with residual history beyond its layer-and-budget state. ResNSC-DP jointly allocates residual and feed-forward widths under a resource budget, with certified bounds on the best numerically evaluated ResNSC score within a specified finite candidate set. At the 121M and 374M pretraining scales, selected architectures achieve lower mean perplexity than uniform, variable-width, and tapered allocations on FineWeb-Edu, WikiText-2, and LAMBADA at comparable parameter budgets. In inherited-weight LLaMA-7B pruning using the LoNAS supernet, ResNSC-DP improves eight-task average accuracy over NSC by 3.28--5.46 percentage points across eight matched parameter budgets. Paired reversals preserve the projection shapes and NSC scores yet worsen performance in both settings, exposing performance differences hidden by position-independent scoring. The code for this work is available at this https URL.

---


### 92. [Loop to Look Better: Learning Adaptive Depth for Question-Guided Perception in Vision-Language Models](https://arxiv.org/abs/2610.30824)

**<font color=#1a73e8>作者：</font>** Wencheng Ye, Anning Hu, Hongye Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual perception should be iterative and task-directed, with representations refined in response to the question and the need for further processing. While Vision-Language Models (VLMs) increasingly support extended reasoning, their visual tokens are still typically acquired in a single, task-agnostic encoder pass. This creates an evidence-acquisition bottleneck: models may reason longer without refining the visual evidence needed to answer the question. We propose LoopLook, a lightweight encoder-side recurrent perception framework that equips pretrained VLMs with adaptive visual depth. LoopLook recurrently revisits a middle-to-late window of the vision encoder, injecting question representations at each loop to guide visual refinement. A learned stopping mechanism adaptively determines the recurrent depth, while a token-wise Mixture-of-Looks (MoL) combines representations from different loops, allowing each visual token to selectively integrate information acquired across recurrent steps. Across four backbones and eight benchmarks, LoopLook consistently improves performance over the baseline, yielding gains of up to 8.6% on MMStar and 8.1% on HallusionBench. Our analysis shows that LoopLook progressively refines visual attention and adaptively allocates depth according to task difficulty. It also better preserves task-relevant visual information under reduced input resolution, while increasing time to first token (TTFT) by only 5.1-6.5%. By bringing recurrence from reasoning back into perception, LoopLook transforms visual perception from a one-shot glimpse into an adaptive process of recurrent refinement.

---


### 93. [TutorCaseBench: A Case-Grounded Benchmark for Evaluating LLM Tutors in Supporting Students with Challenging Behaviors](https://arxiv.org/abs/2610.30828)

**<font color=#1a73e8>作者：</font>** Yeon Su Park, Chanyoung Park, Tae Soo Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used as AI tutors, yet existing benchmarks overlook the challenging behaviors common among students with learning and behavioral difficulties. We introduce TutorCaseBench, a benchmark that grounds AI-tutor evaluation in qualitative case studies from pedagogy, educational psychology, and special education. Our pipeline converts documented student categories into case-specific scenarios, tutor-student dialogues, and rubrics grounded in source evidence. The benchmark contains 923 dialogues across five challenge types, evaluated through open-ended response generation (1,560 items) and multiple-choice selection (2,537 items). Across 11 state-of-the-art LLMs, even the strongest model satisfies a rubric criterion in only 55.8% of open-ended cases, while models are better at selecting appropriate strategies than generating situated responses. These results reveal a gap between intervention recognition and context-specific adaptation, especially for open-weight models. All data are publicly available at this https URL.

---


### 94. [RECAP: Looking Once Is Not Enough for Vision-Language Reasoning](https://arxiv.org/abs/2610.30834)

**<font color=#1a73e8>作者：</font>** Zhaolu Kang, Tailong Luo, Chenxin Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long chain-of-thought reasoning improves vision-language models (VLMs), but it also exposes a temporal grounding failure: as generation unfolds, models may drift from image evidence while reinforcement learning still provides only a final-answer reward. We study this gap through visual revisit, a temporally localized reactivation of image evidence during reasoning. Across three VLM backbones, revisit peaks are predictive of correctness and causally linked to performance: masking them degrades accuracy more than masking non-peaks, while injecting revisit-like peaks into failed rollouts partially restores correct answers. Control analyses show that this signal is not explained by raw attention strength, uncertainty, logit margin, or hidden-state norm. We propose RECAP, a GRPO-compatible training method that turns detached revisit traces into a credit-assignment signal. RECAP uses revisit-conditioned advantage estimation, dynamic discounting, and gated value prediction to propagate final rewards through visually important reasoning steps, without extra rewards, additional rollouts, or inference-time changes. Across Qwen2.5-VL-7B, InternVL3-8B, and LLaVA-OV-7B, RECAP consistently improves over GRPO and VPPO, yielding $+6.1$--$+6.5$ HallusionBench gains over the SFT base while preserving reasoning and text-only performance. Results on larger LoRA-tuned models, Chinese zero-shot benchmarks, visual perturbations, and human evaluation further demonstrate robust improvements in image-grounded reasoning.

---


### 95. [TRIAD: Benchmarking Omni-Modal Ambiguity in Multimodal Large Language Models](https://arxiv.org/abs/2610.30841)

**<font color=#1a73e8>作者：</font>** Zhaolu Kang, Yidi Wang, Yile Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ambiguity is a central feature of natural communication: a sentence, image, or sound may remain underspecified until evidence from the other channels is considered. Yet current multimodal benchmarks mostly test perception, recognition, or reasoning over already determinate inputs, leaving unclear whether omni-modal large language models can resolve ambiguity distributed across text, vision, and audio. We introduce TRIAD, a benchmark for omni-modal ambiguity resolution. Each item is a text--image--audio triplet paired with a question and a set of answer options, and is constructed so that the full triplet determines a unique answer while removing any one modality makes the set of consistent options non-unique. TRIAD contains $327$ hand-written queries in $86$ scene groups and covers $18$ ambiguity categories across the three modalities. Evaluating $14$ omni-modal systems reveals that strong item-level performance does not translate into robust scene-level disambiguation: the best model still trails humans by over $20$ points in group accuracy. Removing answer options widens the gap further, driving model group accuracy to the single digits while humans remain robust. Leave-one-out and transcript/description counterfactuals further show that current systems often underuse audio cues when text and image are present. TRIAD reframes omni-modal evaluation around disambiguation rather than recognition, and provides a taxonomy, benchmark, and diagnostic protocol for measuring this capability.

---


### 96. [Lean Finder V2: Semantic Search for Mathlib That Disambiguates User Queries](https://arxiv.org/abs/2610.30843)

**<font color=#1a73e8>作者：</font>** Jialin Lu, Xiaoyu Liu, Hengrui Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Lean Finder V2, a semantic search framework for Mathlib that disambiguates user queries through complementary model-level adversarial training and input-level query rewriting. Human mathematicians and coding agents rarely search Mathlib by providing detailed context. In practice, they query short properties, notation, aliases, or hypotheses, leaving much of the intended mathematics implicit. In contrast, existing Mathlib search engines unrealistically assume context-rich queries. The scarcity of real-world short queries paired with ground-truth Mathlib statements makes this ambiguity even more intractable. We argue that this is essentially a data problem. Through adversarial training, we scale up the generation of labeled short and ambiguous queries, and learn to disambiguate user queries at both model-level fine-tuning and input-level query rewriting. On the human-curated MathlibQR benchmark, our Lean Finder V2 sets a new state of the art, with at least 11% relative improvement over the previous best Mathlib semantic search engines. On top of our state-of-the-art retriever, optimized query rewriting further improves MathlibQR retrieval. On unlabeled queries from human and coding-agent interactions, Lean Finder V2 is ranked as the strongest system. Integrated with Claude Code, Lean Finder V2 improves proof success on downstream theorem-proving task. Lean Finder V2 is available at: this https URL

---


### 97. [Reverse-KL Policy Distillation: Statistical Guarantees and Limits](https://arxiv.org/abs/2610.30844)

**<font color=#1a73e8>作者：</font>** Haolin Liu, Chen-Yu Wei, Julian Zimmert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reverse Kullback-Leibler (KL) distillation has shown empirical promise for training language models, but its statistical guarantees and limits remain poorly understood. In particular, the effects of two design choices remain unclear: Does access to the teacher's full action distribution provide an advantage over observing only the probability it assigns to the sampled action? Must training trajectories come from the student (online distillation), or can teacher-generated trajectories (offline distillation) suffice? Our work takes a first step toward understanding the theory underlying these questions.
We study the sample complexity of online reverse-KL distillation under two feedback models: the teacher reveals either its full action distribution or only the probability of the student-generated action. We establish minimax bounds for the former and show that substantially more data may be required for the latter. In contrast, offline reverse-KL distillation can attain the same minimax rate whether the teacher reveals its full distribution or only its probability of the teacher-generated action. The key distinction is that teacher-generated actions themselves reveal the teacher's preferences, while queries at student-selected actions can leave those preferences unobserved. This highlights an additional statistical challenge for online distillation compared to offline distillation.
These statistical guarantees do not follow simply from optimizing standard distillation objectives: our lower bounds show that common online objectives can fail when candidates are evaluated only on past student-generated trajectories. We develop trajectory-loss and importance-ratio truncation techniques together with policy-space learning to achieve optimal online distillation guarantees.

---


### 98. [Joules-to-GDP: How Much Economic Value Do AI Systems Produce per Unit of Energy?](https://arxiv.org/abs/2610.30858)

**<font color=#1a73e8>作者：</font>** Amirreza Zeinali, Jon Saad-Falcon, Avanika Narayan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An AI system can produce more economically valuable work while delivering less value for the energy it consumes. We therefore ask: How much economic value does an AI system create per unit of energy consumed? We formalize economic value in two ways: (1) net dollar value, the output's dollar value minus AI-system execution cost, and (2) time saving, the expert's completion time minus the AI system's completion time. Dividing each by measured end-to-end energy yields Net Value per Joule (NVJ) and Time Saving per Joule (TSJ), reported in USD/MJ and hours/MJ. We study 220 public GDPval tasks across 44 occupations, serving five open-weight models locally and evaluating four accelerator types. First, the occupation groups where AI systems succeed most often, deliver the greatest dollar value, or save the most time do not necessarily provide the greatest economic return per joule. For example, among the tested tasks, engineering work delivers about 10% more net dollar value per task than software development. Yet software development delivers about 27% more net value per joule. Second, GLM 5.2 delivers the highest average net dollar value, at $72.27 per task using 0.430 MJ, equivalent in energy to about four hours of active laptop use. By contrast, Gemma 4 31B delivers 56% of that net dollar value using just 23% of the energy, achieving approximately 2.5 times the NVJ and 2.8 times the TSJ. Third, across four single-accelerator deployments, Qwen3.6-27B's NVJ varies by a factor of 4.32 and TSJ by 9.27, with B200 leading both. Additionally, one and eight H100s deliver similar net dollar value, but eight reduce completion time by 22% at 3.24 times the energy. Our framework makes output value and expert time saving under an energy budget explicit objectives for improving models, accelerators, and software, while offering a new basis for assessing AI's potential economic effect on occupational work.

---


### 99. [Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models](https://arxiv.org/abs/2610.30882)

**<font color=#1a73e8>作者：</font>** Zhizhuo Kou, Sizai Hou, Long Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is credited with teaching reasoning models to write {wait} before reconsidering a step, yet large RL accuracy gains do not require the word. This view can confuse what RL discovers with what a model inherits from its training data. We trace the word through open models' training histories, reading it with label-free indices of frequency, position, form and usage and an injected-error test, all computed from sampled outputs. We find that zero-RL almost never coins the marker: on bases that lack the word, RL raises MATH-500 accuracy substantially while {wait} stays near absent. It arrives with training data: mid-training in OLMo-3, and fine-tuning on reasoning traces installs it in most models whose base lacks it. Where the base already uses it, both released RL-Zero recipes (OLMo-3, MiMo) multiply it, whereas KL-free GRPO from the same base does not; OLMo-3's recipe wears down its form and makes it a more sensitive but more liberal alarm; RL after supervised fine-tuning barely changes it, and our GRPO recipe erases a marker seeded by fine-tuning. Finally, we show that marker frequency alone does not indicate RL-induced reasoning and caution against LLM-as-a-judge revision metrics, as automated judges can reverse human-labelled trends.

---


### 100. [Tracing Subliminal Learning Through Pretraining](https://arxiv.org/abs/2610.30884)

**<font color=#1a73e8>作者：</font>** Angela Tang, Vishesh Anand, Gonçalo Paulo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models trained on data generated by other models can sometimes inherit traits unrelated to that data, a phenomenon called subliminal learning. We study both hard label distillation, where students train on numbers generated by a biased teacher, and on-policy soft label distillation, where students generate the data and the teacher's logits provide the learning signal. Using Pythia, PolyPythia, and DataDecide OLMo models, we find that transfer persists in both settings across differences in weight initialization, pretraining data order, pretraining corpus, model size, and architecture. Across pretraining checkpoints, the ability to transmit a preference and the ability to acquire one develop separately: some checkpoints are more effective teachers but weaker students, and vice versa. Consistent with this distinction, cross-model transfer can be strongly asymmetric in magnitude when teacher and student roles are reversed. To investigate what carries the preference signal, we construct synthetic number sequences that match the teacher's generated number frequencies but have no dependence on the prompt or preceding numbers and find that these still induce substantial transfer in the hard-label setting. In top-$K$ soft-label distillation, removing animal tokens from the loss reduces transfer, although not completely in the same-model setting. In our experiments, soft label distillation produces more consistent transfer with less extensive training than hard label distillation. The growing use of on-policy distillation in model post-training makes this a particularly relevant setting for assessing unintended preference transfer.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-241](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

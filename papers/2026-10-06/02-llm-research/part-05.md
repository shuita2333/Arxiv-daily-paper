# 🧠 大模型相关研究 | 2026年10月06日

> 本类共 **261** 篇论文：已确认 **243** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-261](./part-06.md)

---

### 201. [EVOL: Simulator-Guided Evolutionary Expert Synthesis for Deployment-Free Learning Path Recommendation](https://arxiv.org/abs/2610.03273)

**<font color=#1a73e8>作者：</font>** Geonwoo Bang, Dongho Kim, Moohong Min  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for learning path recommendation (LPR) faces two coupled obstacles. First, the policy must commit to a sequence of L concepts without intermediate feedback, producing a combinatorial search space that grows super-exponentially with L and provides reward only at the final step. Second, expert learning paths would be the natural cure for sparse-reward RL, but they do not exist in educational data, because student logs record what learners did, not what they should have done. We address both obstacles by importing a recipe from simulator-based demonstration learning in robotics: the knowledge tracing simulator is used both to synthesize per-learner expert demonstrations through evolutionary search and to train a deployment-free policy that distills these demonstrations into a feed-forward learner. Our framework, EVOL, instantiates this pipeline with an asymmetric actor-critic where the actor commits to deployment-realistic blind planning while the critic exploits the privileged simulator state during training. Across three datasets (ASSIST15, Junyi, and EdNet; 39-189 concepts) and path lengths L = 5, 10, and 20, EVOL surpasses 8 baselines spanning heuristic, sequential, RL, graph-enhanced RL, and LLM-enhanced methods. We further compare three imitation strategies (BC, AWR, and DAPG) and show that final performance is governed by the quality of evolutionary experts rather than by the particular imitation objective.

---


### 202. [Architecture-Dependent Fusion Pathways in MLLMs](https://arxiv.org/abs/2610.03289)

**<font color=#1a73e8>作者：</font>** Hebao Zhu, Dongxia Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) achieve strong performance across vision-language tasks, yet the internal mechanisms by which visual and textual information are fused across layers remain insufficiently understood. We investigate representative MLLMs from two architectural paradigms: concatenation architectures and native multimodal architectures. We conduct three progressively connected analyses: alignment decoupling identifies which modality changes, attention routing and entropy characterize how cross-modal information is distributed, and intrinsic dimensionality examines how fusion reshapes feature spaces. Separately, we perform causal intervention experiments as a validation of the resulting interpretation. As a supplementary analysis, we use visual CKA to examine the Platonic Representation Hypothesis. Together, these analyses reveal two distinct fusion pathways: concatenation models follow a text-first, vision-later pathway, whereas native models exhibit earlier visual-textual co-adaptation and feature-space reorganization. This work provides a mechanistic perspective for understanding multimodal fusion and supports architecture-aware diagnostics of multimodal representations.

---


### 203. [JOVE: Joint Execution and Verification for Resource-Aware LLM Task Graphs](https://arxiv.org/abs/2610.03296)

**<font color=#1a73e8>作者：</font>** Haoran Zhang, Dongjun Kim, Seohyeon Cha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex reasoning queries can be decomposed into directed acyclic task graphs and distributed across heterogeneous LLMs, reducing latency through parallelism and enabling smaller models to solve complex tasks. In practice, however, the suitability of an LLM for a given subtask may be a priori unknown, and execution alone does not reveal output correctness. We propose JOVE, an online framework that jointly assigns executor LLMs and selects intermediate outputs for paid verification. Verification runs asynchronously and is used to improve future allocations, so the system must balance spending on execution now against learning for later. We study how to optimize this trade-off under a long-term budget and a per-query latency constraint, with stochastic, initially unknown LLM service quality, invocation costs, and execution times. JOVE makes execution and verification decisions by solving a sequence of per-query mixed-integer linear programs. Online learning updates task-dependent estimates of LLM quality based on verification feedback, while an information-gain bonus incorporates the value of learning into allocation decisions. Under a natural set of assumptions, we establish sublinear quality-learning regret for JOVE. Across four reasoning benchmarks, JOVE achieves competitive accuracy against standard inference baselines while reducing average cost and latency by at least 3.17 times.

---


### 204. [Lightweight, Rubric-Guided Trajectory Evaluation for Production AI Agents](https://arxiv.org/abs/2610.03315)

**<font color=#1a73e8>作者：</font>** Linh-An Phan, MingXue Wang, Guangyu Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trajectory evaluation is essential for improving the reliability of LLM-based agents, but production use makes it expensive to run repeatedly. Modern agents generate long traces containing tool calls, observations, retries, and external outputs, while not all raw tokens are equally useful for diagnosis. We present \textit{LiteTrajEval}, a lightweight architecture for budget-bounded trajectory evaluation. LiteTrajEval derives compact domain-specific rule profiles offline, then preprocesses each trajectory online, marks heuristic failure signals, serializes it under a fixed global budget, and invokes a single rubric-guided LLM judge to produce structured diagnostic reports. Evaluated on public Magentic-One-style and $\tau$-bench-style trajectory datasets, LiteTrajEval improves failure-localization alignment with human annotations by roughly 20--35 percentage points on Magentic-One and up to 23 percentage points on $\tau$-retail compared with AgentRx, while reducing cost by about 6$\times$ and evaluation time by more than 8$\times$. This solution has also been deployed in our enterprise agentic platform.

---


### 205. [Multi-Task Evolution for Zero-Shot Cross-Problem Generalization using LLMs](https://arxiv.org/abs/2610.03316)

**<font color=#1a73e8>作者：</font>** Zhouliang Xie, Changliang Zhou, Genghui Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing effective heuristics for diverse combinatorial optimization problems requires substantial expertise and repeated search. Large language models (LLMs) automate heuristic generation and refinement, but heuristic search typically depends on evaluation feedback from the problem being optimized. Generalizing to new problem definitions using only source-task feedback therefore remains a central challenge. We introduce MECo, an LLM-driven multi-task evolutionary framework for zero-shot cross-problem generalization. MECo maintains task-conditioned heuristic populations and uses a transfer gap based on cross-task population performance to guide their interactions. These interactions enable the transfer and recombination of heuristics. A complementary selection criterion then constructs a compact heuristic set by rewarding each member's additional coverage of source combinations. The selected set is applied to target problems without further search or adaptation. Experiments on 32 problem variants across vehicle routing (VRP) and flexible job-shop scheduling (FJSP) show that MECo achieves the lowest mean costs compared with eight automated heuristic design (AHD) baselines under the same budgets. On out-of-domain problems, it outperforms the strongest baseline in each family. Moreover, integrating the framework of MECo with different AHD methods improves their ID and OOD performance in both families, supporting its effectiveness across different methods.

---


### 206. [Defense-in-Depth at the Perception-Reasoning Interface of LLM-Centric Agentic UAV Swarms](https://arxiv.org/abs/2610.03319)

**<font color=#1a73e8>作者：</font>** Mohammadhossein Homaei, Yousef Emami, Sajad Homayoun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) increasingly support Uncrewed Aerial Vehicle (UAV) swarm operations such as data collection scheduling, where the model reads structured sensor reports and decides which sensors to visit. An adversary who quietly manipulates those reports can redirect the swarm without modifying the model weights or the UAV. Defenses for this interface have been proposed architecturally but rarely implemented or evaluated. We implement and evaluate defense-in-depth at the perception-reasoning interface of LLM-Centric Agentic UAV Swarms. Five layers check the provenance of a report, whether its values are physically admissible, whether they agree with what swarm geometry and service history predict, whether the resulting schedule starves any sensor, and, when these fail, hand control to a deterministic scheduler that ignores the suspect input. We test each layer against an adversary strong enough to defeat the layer before it. For each of the three input-side layers, we derive in closed form how far a report can be distorted before that layer reacts, fixing each boundary from deployment parameters before any attack data is collected; across thirty matched simulation runs, predicted and measured boundaries agree. Separating attack detection from response is a well-established principle, and we quantify the cost of neglecting this distinction at the perception-reasoning interface. When the system rejects a report, it replaces it with the most recent accepted report. This prevents the adversary from controlling the UAV schedule, but it also increases cumulative cost by 79% and 74% for the two detectors, respectively, compared with the undefended system. The safety check does not detect any attacks, but it nevertheless reduces the attack-induced cost by 37.5%.

---


### 207. [Refinement Buys Intelligibility, Search Buys Identity: What Test-Time Compute Buys in Masked-Diffusion TTS](https://arxiv.org/abs/2610.03320)

**<font color=#1a73e8>作者：</font>** Nityanand Mathur, Hamees Sayed, Ayush Pratap Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models for text-to-speech combine two forms of computation: model depth (parameters) and refinement steps (inference budget). We ask whether they scale equally across capabilities. We train 15 masked-diffusion codec TTS models varying depth (19-133M parameters, 3 seeds) on 2,000 hours of speech and sweep refinement steps T in [1,16] at inference, measuring zero-shot synthesis via ASR word error rate (intelligibility) and speaker verification (identity) on 174 held-out speakers. Against measured floors, refinement closes 86.2% of the intelligibility range but only 46.4% of the identity range - a 1.86x asymmetry robust across multiple error metrics. Retraining at 3x and 6x schedule attenuates but does not reverse this gap (1.84 to 1.36 to 1.23x), because intelligibility saturates with steps while identity continues improving. Best-of-K search recovers speaker identity where refinement fails, with 64.6-79.0% win rates across four independent encoders. Depth and steps are not interchangeable: separable B(d)B(T) fits significantly better (Delta AICc=+69.3) than substitution models. Analysis shows 62% of remaining identity deficit lies in the codec, not the generator. We conclude that refinement and depth target different bottlenecks and should be optimized separately.

---


### 208. [To Jev or Not? Evaluating the Accuracy and Efficiency of Structured Decision Models for Hate-Speech Moderation](https://arxiv.org/abs/2610.03324)

**<font color=#1a73e8>作者：</font>** Demetris Paschalides, George Pallis, Marios D. Dikaiakos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The scale of online content makes hate-speech moderation challenging, while Large Language Models (LLMs) enable harmful material to be produced and adapted more easily. Moderation therefore requires efficient classifiers that can accommodate different definitions of hate speech. Recent structured decision models accept natural-language criteria and select among specified answers, raising the question of whether they can meet these requirements without task-specific training. We present HATEDECIDE, an evaluation of six decision-model configurations on four hate-speech datasets against specialized moderation, zero-shot, commercial, and supervised baselines. We examine whether supplying a dataset's definition, or decomposing it into multiple questions, improves classification, and we measure their latency and cost. We find that commercial LLMs significantly outperform all decision models on only one dataset. Supplying definitions changes up to 28\% of predictions without consistently improving classification, and decomposition significantly improves performance in only 20\% of the comparisons. On a diagnostic set of test cases, the best hosted decision model comes within 1.6 macro-F1 points of the best commercial LLM at approximately 97\% lower inference cost. These results identify opportunities for inexpensive moderation, while showing that explicit criteria and additional questions do not reliably improve classification.

---


### 209. [Preserving Mathematical Reasoning in Compressed Diffusion Language Models via Trajectory-Aware Low-Rank Approximation](https://arxiv.org/abs/2610.03326)

**<font color=#1a73e8>作者：</font>** Tian Liang, Zishan Shao, Yiran Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language model (dLLM) compression faces a known challenge because calibration is typically performed on clean, fully visible activations, whereas inference traverses partially masked intermediate states. For low-rank compression, this raises two questions. First, can low-rank optimality still be characterized when approximation quality is measured over trajectory-distributed states, and second, does the choice of calibration states affect mathematical reasoning preservation under compression? We address these questions by formulating a trajectory-aware low-rank objective over corruption levels and masking realizations. To estimate this objective efficiently, we propose Traj-MC, which estimates the trajectory second moment through Monte Carlo sampling and yields exact sampled-state optimality and population consistency. Under matched compression budgets, trajectory-aware calibration improves reconstruction over the generation trajectory and preserves substantially more mathematical reasoning than clean calibration on mathematical reasoning benchmarks. Our results connect trajectory-aware low-rank optimality to the reasoning capability retained after dLLM compression. Our code is available at: this https URL.

---


### 210. [SyntaxBench: A Statistical Diagnostic Framework for Character-Level Reasoning in Large Language Models](https://arxiv.org/abs/2610.03329)

**<font color=#1a73e8>作者：</font>** Mohsen Larni, Sobhan Ebrahimi Azar, Pouyan Nahed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used where small syntactic errors matter, yet character-level reasoning is still evaluated mostly through isolated probes and aggregate accuracy. We introduce SyntaxBench, a diagnostic benchmark and statistical evaluation framework for character-level reasoning. It contains five core tasks, character counting, letter containment, palindrome detection, edit distance, and longest-string selection, plus index_to_span, a harder substring-extraction stress test. The five core tasks use paired English and character-length-matched random-string inputs. index_to_span documents share a 200-500 word band and are not character-length matched. All six tasks use zero-, one-, and four-shot prompts.
We evaluate eight open-weight models from 2B to 32B parameters across 11 reasoning-mode configurations. The framework reports exact-match and relaxed accuracy, Cohen's kappa, paired McNemar tests with odds ratios, bootstrap confidence intervals, Kendall's tau, class-conditional metrics, tokenization analysis, and multiple-comparison-corrected tests. Three findings stand out. First, tokenization shapes accuracy: random strings are more character-visible than English strings (1.892 vs. 3.169 characters per token), and character-counting accuracy falls as English words occupy more tokens. Second, reasoning mode is not uniformly helpful: Gemma4-31B is nearly unchanged across modes on the near-saturated tasks, while Qwen3.6-27B is worse with thinking on palindrome detection (0.952 non-thinking vs. 0.886 thinking at four-shot). Third, index_to_span remains largely unsolved; the best four-shot exact-match accuracy is 6.75%.
Character-level evaluation needs controlled inputs, paired tests, and analyses of tokenization and reasoning mode rather than aggregate accuracy alone.

---


### 211. [ReFract: Benchmarking Perspective Awareness in Language Model Agents with Text World Models](https://arxiv.org/abs/2610.03356)

**<font color=#1a73e8>作者：</font>** Hainiu Xu, Vítor N. Lourenço, Mohnish Dubey 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly deployed in high-stakes settings such as industrial maintenance and equipment fault troubleshooting, where workers occupy a variety of roles. A capable agent must therefore act in a way that is calibrated to user's role: taking actions and providing information that respect the role's knowledge and capability boundaries. Unlike coding, where mistakes are usually recoverable, agent responses in these settings are enacted on physical equipment, and can therefore cause irreversible equipment damage, production loss, or personnel harm. Existing benchmarks, however, largely overlook the need for agents to infer what a role intends and acting only through tools that role may legitimately use, a capability which we term Perspective Awareness. To this end, we introduce ReFract, a benchmark of 150 expert-validated entries in which an agent must act differently in response to the same query depending on user's role. Entries of ReFract are grounded in anonymized queries from domain support conversations, against which we construct Text World Models that simulate the agent's operating environments and assemble perspective-aware action trajectories. State-of-the-art LLMs solve at most 69% of the tasks with more than 50% of their trajectories contain attempts of taking perspective-violating actions. ReFract exposes perspective awareness as a distinct, largely unsolved axis of agent evaluation and motivates agents that calibrate not just how to act, but for whom.

---


### 212. [Follow the Winners: Conservative Policy Improvement with the Cross-Entropy Method for Critic-Free RFT](https://arxiv.org/abs/2610.03361)

**<font color=#1a73e8>作者：</font>** Joery Ariën de Vries, Neil David Lawrence, Zhenwen Dai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Critic-free reinforcement fine-tuning (RFT) for agentic large language models is often done through GRPO-style methods, which compute a group baseline over repeated rollouts to reduce target variance. However, this setup is ill-suited to agents acting in stateful environments such as live services or security sandboxes, where repeated rollouts are impractical to obtain and aggressive updates entrench the noise of long, sparsely verified trajectories. We propose \textit{Follow the Winners} (FTW), a critic-free policy-learning algorithm that adapts the cross-entropy method to RFT, replacing group rollouts with an ordinal filter on replay-buffer samples that yields polynomial concentration in the order statistic of returns. We derive FTW through a control-as-inference lens, which also recovers GRPO and DPO as specific modelling choices, identifying GRPO as risk-neutral while DPO and FTW share a bounded risk-seeking offset that FTW controls. We identify this offset as an inherent trade-off of variance reduction through ordinal filters on samples, whereas a critic model induces a different trade-off between bias and variance. Scaled to agentic LLM post-training, FTW matches GRPO and PPO on Sokoban and Search-R1 baselines, showing a viable trade-off from a value model or group rollouts to CPU memory.

---


### 213. [CVE2AP: Automated Generation of PDDL-Encoded Attack Paths via Large Language Models](https://arxiv.org/abs/2610.03383)

**<font color=#1a73e8>作者：</font>** Lin Cui, Vincenzo Scotti, Raffaela Mirandola  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Attack Path (AP) modeling is fundamental to cybersecurity analysis, where the Planning Domain Definition Language (PDDL) has been widely adopted to encode APs into formal and machine-verifiable representations for automated reasoning about vulnerability exploitation, attack progression, and their potential impacts. However, existing AP modeling approaches largely rely on expert-driven manual construction, limiting their scalability and ability to keep pace with rapidly evolving cyber threats. Large language models (LLMs) are promising candidates, as their extensive pre-trained knowledge and reasoning capabilities enable them to interpret and transform threat intelligence into formal representations. In this paper, we propose \textbf{CVE2AP}, an LLM-based approach for automatically generating PDDL-encoded attack paths from natural language CVE (Common Vulnerability Exposure) descriptions. CVE2AP leverages structured prompting and incorporates an error-feedback mechanism that iteratively refines the generated paths using planner-reported syntactic and solvability errors. We conduct a systematic empirical evaluation across multiple LLMs and generation configurations, assessing generation quality across syntactic, solvability and semantic dimensions, together with token consumption and generation time. The results demonstrate that CVE2AP effectively generates high-quality PDDL-encoded attack paths, achieving up to 86.9\% syntax correctness, 78.6\% solvability, and 93.1\% semantic correctness under LLM-as-expert evaluation, while \texttt{GPT-5.5} offers the best quality-cost trade-off and error feedback yields the most consistent quality improvement.

---


### 214. [From Patching to Pruning Visual Computation in Vision Language Models](https://arxiv.org/abs/2610.03389)

**<font color=#1a73e8>作者：</font>** Rahul Chowdhury, Timothy A Rupprecht, Xuan Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision language models (VLMs) incur substantial inference cost because every visual token is processed by the attention and MLP projections of every decoder layer, even when token-specific visual computation is unnecessary at many depths. We introduce Patch-to-Prune (P2P), inspired by Mechanistic Interpretability, a training-free framework that converts activation patching from a diagnostic tool into an inference-time computation bypass. P2P performs validation-guided forward and backward layer sweeps to identify decoder regions whose visual-token projection outputs can be replaced by fixed neutral proxy activation vectors within a user-specified accuracy tolerance. Unlike conventional token-pruning methods, P2P preserves the sequence length, token order, positional information, attention mask, and residual pathways, thereby pruning computation without removing tokens or modifying the pretrained model weights. We evaluate P2P on four VLMs from the Qwen2.5-VL and LLaVA families across seven multi-modal benchmarks using mutually disjoint calibration, validation, and test partitions. P2P at a 3% tolerance retains around 94% of dense accuracy while reducing FLOPs by 55%. Beyond these efficiency gains, our layer-wise analysis suggests that visual processing in VLMs is non-uniformly distributed across decoder depth: early and late layers often require little token-specific visual computation, whereas intermediate layers appear to perform most task-relevant visual integration, enabling later reasoning to rely largely on visual information already embedded in shared residual and textual representations. This makes P2P both an efficient inference framework and a causal lens into visual information processing in VLMs.

---


### 215. [CLIMB: Confidence-Guided Complementary Evidence for Multimodal Retrieval-Augmented Generation](https://arxiv.org/abs/2610.03421)

**<font color=#1a73e8>作者：</font>** Hang Gao, Wujiang Xu, Zhixing Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have shown strong visual reasoning abilities, but knowledge-intensive visual question answering often requires external textual evidence beyond the image and the model's parametric knowledge. Existing multimodal RAG systems commonly rely on Top-$K$ retrieval or reranking, which may return redundant passages and provide limited control over whether an answer update is sufficiently supported by the retrieved evidence. We propose \textit{CLIMB}, a training-free inference-time framework for multimodal RAG. CLIMB first constructs a compact complementary evidence pool using an MMR-style objective that balances query relevance and passage-level redundancy. It then performs confidence-controlled refinement within this fixed pool: an R/E/C critic scores passages by relevance, evidence specificity, and cross-modal alignment, while an evidence-grounded confidence estimator accepts an updated answer only when the estimated confidence increases. This design provides a simple stopping criterion and reduces unnecessary refinement without modifying the underlying retriever or MLLM. Experiments on Encyclopedic-VQA and InfoSeek show that CLIMB consistently improves over retrieval-augmented multimodal baselines. Ablations further indicate that complementary pooling, critic-based scoring, and iterative confidence-controlled refinement each contribute to the final performance.

---


### 216. [Jumping the Line: Exploiting Length Predictions in LLM Scheduling](https://arxiv.org/abs/2610.03430)

**<font color=#1a73e8>作者：</font>** Yuyang Dai, Rana Shahout, Mahmood Sharif  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient request scheduling is increasingly important for reducing completion time in large language model (LLM) serving. Size-based policies such as Shortest Job First prioritize shorter requests, but output lengths are unknown before generation, so practical schedulers rely on predicted lengths. We introduce JIL, an attack on prediction-based LLM schedulers that manipulates the scheduling signal to obtain higher priority and reduce completion time. Using TRAIL as a case study, JIL optimizes an adversarial suffix that causes a lightweight output-length probe to underestimate a request's length. We evaluate JIL on two datasets and four LLMs across varied request profiles and deployment configurations. JIL reduces predicted output lengths by up to 83.4 percent, and adversarial requests complete up to 1.53 times faster on average in end-to-end serving experiments. The reduction in predicted length is substantially larger than the change in actual output length, revealing a mismatch between the scheduler's estimate and the request's realized size. Response utility varies across models and tasks, exposing a trade-off between scheduling advantage and response quality. We also evaluate scheduler-side defenses and find that grouping length predictions into coarse intervals reduces JIL's scheduling advantage and mitigates delays to benign requests.

---


### 217. [OptiSelect: How does the Optimizer Shape Data Curriculum?](https://arxiv.org/abs/2610.03432)

**<font color=#1a73e8>作者：</font>** Simin Fan, Alireza Abdollahpoorrostam, Martin Jaggi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online data selection has demonstrated substantial efficiency gains for LLM pretraining by training on the most valuable candidates within each batch. Since a candidate's value is realized through its effective model update, principled selection should account for the optimizer step, which reshapes the raw gradient before it updates model parameters. We formalize this optimizer-aware selection paradigm as OptiSelect and present the first systematic study of how the optimizer shapes data selection. Our theory establishes a selection gain principle in which the advantage of online selection is governed by the discriminability of the optimizer-induced utility scores. We prove that sign-based and polar-tangential preconditioners of Lion and Muon would suffer from a discriminability collapse which caps attainable gains from OptiSelect, whereas diagonal-adaptive optimizers such as AdamW and Sophia admit strictly better upper bounds. The proposed principle also yields a quantitative derivation of the optimal candidate oversampling ratio. Pretraining experiments on 124M and 720M models are consistent with our theoretical analysis and show that AdamW's diagonal-adaptive scoring geometry remains the strongest scoring geometry even with Muon as optimizer. We further demonstrate that OptiSelect retains its benefits under data rephrasing, a technique used in modern data processing pipelines. Our findings provide theoretical foundations and practical guidance for co-designing optimizers and data selection in LLM pretraining.

---


### 218. [Corrupted but Correct: Why Vision-Language Models Lie to Themselves Internally](https://arxiv.org/abs/2610.03445)

**<font color=#1a73e8>作者：</font>** Arun Josephraj Arokiaraj, Zekun Wu, Adriano Koshiyama  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A targeted adversarial perturbation can drive a vision-language model's (VLM's) teacher-forced training loss for a fixed target caption to near zero, yet the same model, allowed to generate freely, produces the original, correct description with no trace of the target. We call this dissociation the train/inference gap, and give it a precise mechanistic account on Qwen2.5-VL-7B-Instruct using a controlled two-stage PGD attack on 200 held-out COCO images. First, we show that image-level pixel statistics, including a correctly re-implemented, texture-based attackability measure from the CNN robustness literature, have essentially no predictive power over which images are corrupted (best predictor r=-0.050, p=0.484; ridge regression R^2=0.069). Second, using the logit lens, we localise the gap to a single autoregressive step: the rank of the target token, conditioned on the correct first token already being generated, is fixed at exactly 3,488 out of 152,064 vocabulary entries for every image and every condition, with zero variance. Third, tracking target-token rank across all 28 LLM decoder layers reveals that the visual encoder corrupts every image's representation by a comparable margin regardless of eventual outcome, but the language model decoder then differentially arbitrates: amplifying the corrupted signal for susceptible images and actively suppressing it, past its clean-image baseline, for resistant ones (p<0.001, rank-biserial r=0.579). A linear probe on the merger hidden state separates these two outcomes with AUC=0.858, though we flag a circularity concern in this estimate. Together these results argue that adversarial robustness in autoregressive VLMs is substantially a property of the language decoder's prior, not the visual encoder, with direct implications for where faithfulness evaluations and defenses for deployed VLM systems should be targeted.

---


### 219. [A Vision-Language Model (VLM)-based Pipeline for End-to-End Procedural Modeling of Field-Grown Maize from Point Clouds](https://arxiv.org/abs/2610.03468)

**<font color=#1a73e8>作者：</font>** Mozhgan Hadadi, Talukder Z. Jubery, Adarsh Krishnamurthy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Editable 3D models of field-grown crops support high-throughput phenotyping and in silico breeding trials, but building them from scanned point clouds requires organ-level segmentation and fitting. Procedural generators can turn an organ-level parameter set into an analysis-suitable 3D model, but obtaining that set requires hours of manual tuning per plant or segmentation models trained on species-specific labels. We present an automated pipeline that reconstructs procedural maize models from raw 3D point clouds without manual tuning or species-specific training data. A multimodal vision-language model (VLM) annotates leaf midlines in rendered orthographic views. Deterministic geometric algorithms back-project the annotations onto the point cloud, merge them into 3D leaves by cross-view consensus, and grow the midlines to full blades on an orientation-weighted surface graph. Measured organ parameters populate a plant descriptor for a Non-Uniform Rational B-Spline (NURBS)-based procedural model generator. Each leaf surface is then refined against its scan points by differentiable NURBS fitting. The pipeline reached a median whole-plant Chamfer distance of 5.4 mm on 100 genotypically diverse field-grown maize plants from the MaizeField3D dataset. The reconstructions were closer to the scans than those of an earlier semi-automated pipeline based on manual annotations. The pipeline recovered 1,017 of 1,023 (99.4%) curated reference leaves at an intersection-over-union of at least 0.5 without using those labels as input. These results show that VLM annotations become usable organ-level measurements when downstream geometric stages can correct them. This makes automated generation of editable 3D plant assets feasible at the scale of modern phenotyping experiments.

---


### 220. [Metropolis-Hastings Dominates Importance Resampling for Policy Composition](https://arxiv.org/abs/2610.03480)

**<font color=#1a73e8>作者：</font>** Alexey Kurennoy, Ramil Yarullin, Fergal Reid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training a large language model (LLM) often requires exploring trade-offs between multiple rewards, but retraining for each trade-off is expensive. Decoding-time policy composition allows these trade-offs to be adjusted by combining reward-specific policies at inference time. This composition targets a weighted product of the policies' probabilities over complete responses, but standard implementations combine their next-token probabilities, generally introducing sampling bias. We analyze a known iterative correction based on independence Metropolis-Hastings (MH). Our main result shows that, for every rollout budget, MH produces an output distribution at least as close to the target as sampling-importance-resampling (SIR) with the same budget, as measured by every convex f-divergence. We also derive a lower bound on MH's improvement over the uncorrected decoder in a consensus objective measuring agreement with the supplied policies. We further characterize the correction's sampling error in two asymptotic regimes: when the reward-specific policies approach agreement, and when the log ratio between target and uncorrected-decoder probabilities fluctuates increasingly widely, as can happen for long responses. We complement our analysis with experiments in enumerable and LLM-scale settings.

---


### 221. [Single-Pass Uncertainty Heads for Claim-Level Hallucination Detection in Persian Medical Language Models](https://arxiv.org/abs/2610.03482)

**<font color=#1a73e8>作者：</font>** Mehrdad Ghassabi, Pedram Rostami, Hamidreza Baradaran Kashani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination detection is particularly important for medical language models, but repeated-sampling approaches are expensive and existing uncertainty-head resources do not directly transfer to a new backbone and language. We adapt the LLM Uncertainty Head (LUH) framework to Aya-Expanse-8B-based Persian medical models, using Gaokerena-V and Gaokerena-R as two previously developed backbones. We first examine response variability on a 168-question Iranian medical entrance examination and observe substantially lower five-run consistency for Gaokerena-V than for Aya-Expanse-8B, whereas Gaokerena-R is comparable to Aya-Expanse-8B. We then construct two paired claim-level hallucination datasets directly in Persian, containing 1,600 responses for each backbone, and train lightweight claim-level heads on frozen backbone attention maps and token probabilities. On held-out test splits, the heads obtain PR-AUCs of 0.4820 and 0.4652, corresponding to 2.30 and 2.66 times their respective random baselines, and ROC-AUCs of 0.7852 and 0.7810. The heads require neither retrieval nor repeated sampling at inference time. These results provide an initial study of single-pass claim-level uncertainty estimation for Persian medical language models; the test splits are small and the labels are automatically generated.

---


### 222. [Efficient Reasoning Training Does Not Always Harm CoT Faithfulness and Monitorability](https://arxiv.org/abs/2610.03509)

**<font color=#1a73e8>作者：</font>** Samuel Lewis-Lim, Xingwei Tan, Mario Sanger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning allows humans to inspect how large language models reach their answers, and oversee model behaviour. This reasoning comes at an increased inference cost, motivating efficient methods that train models to solve tasks using fewer tokens. However, a common concern is that such training may cause models to skip important reasoning steps, so the CoT no longer faithfully reflects the model's decision. It is unclear whether or when this occurs in practice, since different efficiency methods apply length pressure to models' CoT in distinct ways, and faithfully explaining a model's decision takes more tokens on some tasks than others. To understand these dynamics, we fine-tune a variety of models with three methods that apply length pressure differently, namely a fixed generation budget, a per-example length target, and a group-relative length reward. We evaluate how efficient reasoning affects CoT faithfulness (i.e., how well the CoT reflects model decisions on related inputs) and monitorability (i.e., whether the CoT reveals when input interventions alter the output). We find that it affects faithfulness and monitorability differently. Faithfulness falls in most settings, primarily because the trained models are less consistent. Monitorability is more robust, as models keep acknowledging the influence on their answer even when the CoT is much shorter.

---


### 223. [Weave Forcing: Compositional Memory Routing for Interactive Long Video Generation](https://arxiv.org/abs/2610.03510)

**<font color=#1a73e8>作者：</font>** Ziyi Wang, Junchi Yao, Heqian Qiu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in autoregressive video generation have improved temporal consistency over extended durations, yet interactive storytelling requires more than continuous scene extension: a new shot may combine characters and backgrounds from different historical shots. Whole prompt retrieval can overlook the distinct reference needs of individual components, while directly combining all historical memories may introduce unrelated visual content. To address these problems, we present Weave Forcing, a training-free framework for compositional memory reuse in interactive long video generation. First, we use an LLM for semantic slot routing to decompose user prompts into character and background descriptions and explicitly select suitable historical references for each component. To isolate the required content, masked memory weaving uses contrasting attention maps conditioned on semantic slots to construct refined semantic masks, selectively exposing relevant tokens from compressed historical KV memories to guide the generation of the current shot. We further introduce coverage adaptive RoPE to adjust temporal offsets and memory retention according to no, partial, or full reference coverage, addressing visual artifacts observed when incomplete historical references are positioned close to the current generation. Extensive experiments demonstrate that Weave Forcing improves cross-shot subject and background consistency while maintaining competitive visual quality and text alignment.

---


### 224. [Learning from Repaired Reasoning: Root-Cause-Guided On-Policy Distillation](https://arxiv.org/abs/2610.03515)

**<font color=#1a73e8>作者：</font>** Chenglei Shen, Haoyang Yao, Weijie Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) uses reference solutions as privileged hindsight to supervise student-generated reasoning trajectories. However, reference-based guidance may explain a correct solution without addressing why the student's own reasoning fails. This reasoning mismatch between the guidance provided and the correction needed can encourage the student to borrow correct conclusions while leaving its reasoning errors unresolved. Moreover, applying the same hindsight throughout the trajectory risks a distillation trap, where unnecessary constraints on valid reasoning compete with correction of substantive errors. To address these issues, we propose Root-Cause-Guided On-Policy Distillation (RC-OPD), which uses repairs of the student's own reasoning to provide guidance that addresses its specific errors while building on valid progress. For each failed attempt, RC-OPD locates the earliest substantive error, develops a local correction, and uses the corrected intermediate result as an anchor for the valid prefix. An iterative diagnosis--repair--continuation process tests the repairs through student continuation, identifying further errors within a fixed repair budget. For repair chains that reach a correct answer, root--cause--guided distillation uses failure diagnoses and corrective goals to supervise the erroneous segments, while anchor-guided distillation supports the corresponding valid prefixes with reasoning chains leading to the repaired intermediate results. We evaluate RC-OPD across multiple datasets and model scales. Extensive experiments and analyses show that it mitigates reasoning mismatch and the distillation trap, yielding substantial performance gains.

---


### 225. [PrivDev: Mapping Static-Analysis Data Types to DPV](https://arxiv.org/abs/2610.03518)

**<font color=#1a73e8>作者：</font>** Simon Bernbeck, Ricardo Ramalho, Matheus Amendoeira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Static-analysis scanners can identify personal-data types in source code, but they lack mechanisms to connect these findings to standardized privacy vocabularies. PrivDev maps 122 Bearer CLI data types to Data Privacy Vocabulary Personal Data (DPV-PD) categories and links them to potentially relevant GDPR provisions. Our approach combines deterministic mapping for 43 exact-label matches with a retrieval-grounded Large Language Model (LLM) to resolve the remaining 79 non-trivial mappings. The resulting RDF knowledge graph contains 118 ODRL policy resources that were structurally validated using SHACL. The artifact passed five complementary validation gates that cover structural correctness, query consistency, retrieval quality, LLM-based assessment, and human evaluation. In human evaluation, nine annotators produced 711 judgments, yielding a raw agreement of 0.72, Gwet's AC1 of 0.68, and Gwet's AC2 of 0.88. Our results indicate that the proposed mappings are plausible and reproducible, while also revealing ambiguities in scanner-defined data-type labels and coverage gaps in DPV-PD.

---


### 226. [Reasoning Models Are Accurate but Unsound on Identification](https://arxiv.org/abs/2610.03519)

**<font color=#1a73e8>作者：</font>** Arman Behnam, Binghui Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A reasoning model asked whether a causal effect is recoverable from observational data can fail in two ways: it refuses an identifiable query or answers a nonidentifiable one. The latter is more consequential, as no observational data can validate the claimed formula. Measuring this failure requires queries that are provably non-identifiable, which prior evaluations lack, and grading that accepts correct formulas in any equivalent form, which string matching cannot provide. We build CERTID, a formal identification pipeline that addresses both limitations. CERTID uses the sound and complete causal identification algorithm ID to certify whether an effect is identifiable from a given graph and query, and verifies returned formulas against structural causal models whose interventional distributions are known exactly. CERTID further develops theoretical results to mitigate structural leakage, repair non-identifiable queries, and establish grading guarantees. We evaluate three frontier reasoning models (Gemini Flash, Gemini Pro, and GPT5.5) on 1,200 certified instances spanning 4 to 50 vertices. Accuracy proves a poor proxy for soundness: on identical instances, the false-claim rate on non-identifiable queries varies by seventeen-fold across models. We also find that models decide identifiability with 97-100% accuracy on graphs generated after the strongest model's training snapshot. Instances, the certification procedure, the verifier, and per-instance records are available at this https URL.

---


### 227. [From Benchmarks to Production: A Text-to-SQL System for Complex Financial Data](https://arxiv.org/abs/2610.03524)

**<font color=#1a73e8>作者：</font>** Arijit Sehanobish, Bruno Gomes Coelho, Guillaume Michel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General-purpose Text-to-SQL systems achieve strong performance on academic benchmarks like Spider and BIRD, where schemas are relatively shallow and column values are often human readable. In production financial databases, where concepts are stored as opaque integer keys rather than human-readable strings, these methods fall below 50%, as even simple queries require multiple joins and filter predicates reference opaque IDs. We present Financial LINking Text-to-SQL (FLINT), a domain-specialized Text-to-SQL system that closes this gap through three key components: (1) a lookup agent that dynamically resolves natural-language concepts to question-specific reference table constraints, (2) embedding-based retrieval of structurally similar query templates from a compact, expert-authored bank, and (3) schema linking that prunes a large table schema to the relevant subset by traversing foreign-key chains, rather than relying on name similarity alone. We evaluate on two datasets totaling 359 questions over production financial schemas. FLINT outperforms various state-of-the-art baselines using the same LLM. The system is deployed in production as part of a financial data retrieval service.

---


### 228. [Structured Composition of Verifiable Atomic Insights for Table-to-Report Generation](https://arxiv.org/abs/2610.03525)

**<font color=#1a73e8>作者：</font>** Teng Lin, Xinyu Liu, Nan Tang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Table-to-report generation refers to the task of automatically generating article-level analyt- ical reports from relational tables and is an essential capability for automated data science and decision support. Its central challenge lies in systematically discovering verifiable com- posite insights across tables, attributes, and analytical perspectives, and organizing them into coherent, complete, and traceable evidence chains. Existing methods primarily rely on sequential, reactive data agents or direct Large Language Model(LLM) generation. They suffer from exploration bias: early local observations constrain subsequent actions, causing models to focus prematurely on local analyzes and miss cross-table or cross-dimensional evidence. We propose ComInsight, which reformulates insight discovery as the composition of atomic evidences. We first define an atomic insight as the smallest executable analytical unit conforming to a predefined analysis pattern and enumerate all valid atomic insights from database schema and content. These atoms are then organized into a multi-relational insight graph, where nodes represent verified data facts and edges encode logical, temporal, or hierarchical relations. Finally, a set of composition operators systematically fuses atomic nodes into higher-order composite conclusions. Every composite output is accompanied by executable SQL and fine-grained provenance, ensuring full verifiability. Across three benchmarks InsightBench, DDR-Bench, and T2R-Bench, ComInsight consistently outperforms strong baselines in factual correctness, novelty, and structural completeness. We believe ComInsight offers a reliable, efficient, and explainable path toward table-to-report generation.

---


### 229. [Divergence controls entropy in distillation](https://arxiv.org/abs/2610.03529)

**<font color=#1a73e8>作者：</font>** Nicolas Zucchet, Scott W. Linderman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distillation has become a core primitive of large language model training, but its properties are not yet well understood. We take an entropic perspective, studying how the entropy of the student depends on the data and the divergence that define the distillation objective. We prove that forward KL inflates the entropy of the student above that of the teacher. Since cross-entropy training is a special case, this yields an identity that we verify quantitatively in pretraining and supervised finetuning. Other divergences come with no such guarantee: reverse KL deflates entropy until the gap between student and teacher gets too large, and interpolating between the two changes entropy smoothly early in training but abruptly at convergence. The lower entropy of on-policy distillation comes from token-level reverse KL, not from on-policy sampling. The divergence therefore acts as an implicit entropy regularizer, whose role is clearest in self-distillation: as conditioning on privileged information deflates entropy, the divergence hyperparameters that work best are those that compensate for it.

---


### 230. [Author Representation Strategies for Zero-Shot Authorship Attribution: A Comparative Study of LLM-Based and Embedding-Based Approaches](https://arxiv.org/abs/2610.03531)

**<font color=#1a73e8>作者：</font>** Nudrat Habib, Tosin Adewumi, Sana Sabah Al-Azzawi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Authorship Attribution (AA) requires capturing fine-grained stylistic characteristics, making it particularly challenging in zero-shot (ZS) settings where no task-specific supervision is available. In this work, we investigate the effect of author representations on ZS AA by evaluating a label-only prompting baseline together with three author representation strategies: representative writing samples, LLM-generated descriptions, and style embeddings (LISA). The first three approaches perform attribution using LLM prompting, while the embedding-based approach uses style embeddings with cosine similarity. We investigate the influence of prompt design and propose a two-stage embedding-based attribution framework that combines candidate space reduction with embedding-dimension selection. The results show that label-only ZS AA is ineffective, while incorporating author-specific representations consistently improves attribution performance. Among the evaluated approaches, the proposed two-stage LISA framework achieves the strongest overall performance, whereas LLM-generated style descriptions provide a substantially more compact representation of author style at the cost of some attribution performance. These findings demonstrate the importance of author representation in ZS AA, while indicating that current open-source LLMs remain insufficient for robust attribution without more effective representation learning.

---


### 231. [Objects Without Morphisms: What LLMs for Mathematics Do Not Represent](https://arxiv.org/abs/2610.03551)

**<font color=#1a73e8>作者：</font>** Yanli Wang, Suijin Wang, Xiaopeng Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have reached expert-level performance on competition mathematics largely through the volume of search placed around them: candidate solutions are sampled in quantity and retained only when an external criterion accepts them. Such a procedure improves the outcome that survives it while leaving untouched what the model represents. We examine that question where no external criterion exists: translating statements between the dialects of neighbouring subfields, where fidelity turns on the level of generality at which content is asserted. The source leaves that level implicit in its vocabulary, so a faithful translation must recover it from the relation between the theories. We introduce an instrument that codes truth, content and scope in separate blind queues, with a judge-free measure of whether a rewrite states the hypothesis implicit in its source, and establish its sensitivity with a planted-positive control. Across seven models from four families, translating towards the general framing widens the domain of quantification in 60.6% of rewrites and narrows it in none; translating towards the concrete framing narrows it in 28.3% and widens it in 0.3%. The hypothesis that would prevent it is stated in 21.6% of model rewrites and 4.2% of human statements. Capability does not govern the asymmetry: it appears in every model tested, and the most capable widens least. It replicates on the half of the benchmark held out by a pre-registered rule, and on statements written by mathematicians. Instructing a model to state every hypothesis it requires raises that rate but not its sensitivity to direction. We argue that these systems have acquired an object-level correspondence between subfield vocabularies without the constraint under which a translation between theories carries hypotheses to hypotheses.

---


### 232. [Writerslogic at PAN 2026: Process over Content for Robust Detection under Domain Shift](https://arxiv.org/abs/2610.03565)

**<font color=#1a73e8>作者：</font>** David L. Condrey  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe the Writerslogic systems for three PAN at CLEF 2026 shared tasks (Reasoning Trajectory Detection, Voight-Kampff Generative AI Detection, and Multi-Author Writing Style Analysis), unified by a shared analytical framework: feature robustness under distribution shift is governed by support overlap between training and test distributions, not by training-set effect size. This yields a taxonomy (domain-anchored, domain-portable, domain-invariant) that explains why generator-specific features die under domain shift while vocabulary fingerprints (hapax ratio, Yule's K, Heaps' exponent), compression measures, and character n-grams survive. On Reasoning Trajectory Detection, where training was entirely mathematics and 84 percent of test was unseen domains, the framework guided system design to 1st place in source detection (0.85 macro F1 via Opus-Sonnet agreement) and 3rd place in safety classification (0.66 macro F1 via query-refusal decomposition). For Voight-Kampff, we built a calibrated ensemble of DeBERTa-v2 (ONNX), multi-seed LightGBM with 44 domain-portable stylometric features, and SVM on n-gram TF-IDF, combined via learned stacking with isotonic calibration; the best configuration achieved 0.891 on the PAN 2026 test set with balanced sub-metrics (0.853 to 0.902 across all evaluation dimensions). For Multi-Author Writing Style Analysis, we describe a system fusing spectral clustering over character n-gram similarity graphs, normalized compression distance for local boundary detection, and SmolLM-135M perplexity for neural change-point detection; a platform mix-up meant our run never reached the official evaluation, so we report the design and its a priori predictions. Across all three tasks, features measuring generation process properties are designed to outperform features measuring generated content properties under domain shift.

---


### 233. [Writerslogic at the CLEF 2026 SimpleText Track: Multi-Candidate LLM Simplification and Stacked Complexity Spotting](https://arxiv.org/abs/2610.03567)

**<font color=#1a73e8>作者：</font>** David L. Condrey  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe the Writerslogic team's participation in the CLEF 2026 SimpleText shared task, addressing Task 1 (text simplification) and Task 2 (complexity spotting). For Task 1, we develop a multi-candidate generation pipeline using GPT-4o-mini that produces five simplification candidates per sentence at varying temperatures, then selects the best candidate using a reference-free scoring heuristic that rewards compression, source word retention, Cochrane Plain Language Summary vocabulary usage, and lexical simplicity. On Task 1.1 (sentence-level simplification), our Claude Sonnet 4 submission achieves SARI 47.43 and BLEU 14.21, the top-ranked sentence-level system (3rd on the combined Task 1 leaderboard, behind two document-level submissions). For Task 2, we fine-tune a DeBERTa-v3-large NLI model on 350K labeled (source, sentence) pairs, framing hallucination detection as natural language inference. The model reads the most relevant source sentence as premise and the candidate as hypothesis, directly learning to distinguish grounded from hallucinated content. On Task 2.1 (binary overgeneration identification), our fine-tuned DeBERTa system achieves 0.8081 document-level macro F1 (0.8085 in our best ensemble), the top-ranked entry within the identification track and 2nd among teams overall, behind AIIR Lab (0.8197). On Task 2.2 (multi-class error classification), our best submission reaches 0.804 multiclass accuracy, ranking 2nd among unique teams behind AIIR Lab (0.827). We evaluate both tasks on English and multilingual biomedical text from Cochrane systematic reviews.

---


### 234. [HazardWeaver: Scientific Route Selection for Hazard Analysis Agents](https://arxiv.org/abs/2610.03591)

**<font color=#1a73e8>作者：</font>** Wangshu Zhu, Xueqi Cheng, Liang Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding and assessing natural hazards is essential for disaster preparedness and risk reduction. Recent advances in large language models have spurred growing interest in AI agents for hazard analysis, particularly their ability to integrate scientific data, models, and tools into automated workflows. However, effective automation requires agents to determine which scientific methods are appropriate for a given event and executable with the available data and tools. As new evidence and execution results become available, these conditions can change, requiring agents to reconsider their choices. We formulate this problem as state-dependent scientific route selection and introduce HazardWeaver. Specifically, HazardWeaver first leverages the Hazard Knowledge Compiler to extract evidence-linked conditions governing scientific applicability, then its Hazard Capability Graph represents executable scientific capabilities and checks compatibility between their inputs and outputs. Using these complementary representations, the Hazard Weaver Agent component selects applicable and executable routes, carries out their workflows, and revises its decisions as the analysis state changes. To evaluate both the scientific outputs and the decisions that produce them, we introduce the Hazard Weaver Benchmark, comprising 141 instances across seven single-hazard domains and four multi-hazard interaction classes. The benchmark accommodates multiple valid scientific routes and evaluates output correctness, route validity, and justified abstention. Extensive experiments on this benchmark show that HazardWeaver outperforms existing agent systems, with the largest gains on tasks with multiple eligible scientific routes. Our code is publicly available at this https URL.

---


### 235. [DEPICT: Scoring Text-to-Image Alignment by Answer Agreement](https://arxiv.org/abs/2610.03617)

**<font color=#1a73e8>作者：</font>** Vasco Ramos, Sandra Godinho Silva, Joao Magalhaes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-text alignment is a core problem in computer vision with applications in caption evaluation, hallucination detection, data curation, and the benchmarking of text-to-image (T2I) generators. As T2I models improve, benchmarking has become demanding, requiring metrics capable of finding a series of issues like missing objects, swapped attributes, miscounts, and ignored negations. Recent work addresses this by fine-tuning evaluators on preference data or by prompting a vision-language model, either holistically with the caption or with decomposed verification questions. However, existing approaches fall short: fine-tuned metrics remain bound to one backbone and training distribution; holistic metrics miss fine-grained details; and decomposed metrics rely on a fixed-YES assumption that penalizes faithful images whenever that assumption fails. In contrast, we propose DEPICT, a training-free metric that replaces fixed reference answers with expected agreement between image-based and caption-only answers, weighting questions by how decisively the caption determines them. By replacing fixed references, our agreement rule increases negation accuracy from 19% to 88%. To recover the context lost during decomposition, DEPICT merges this agreement score with a holistic score. We evaluate DEPICT on five benchmarks and eleven backbones from three model families and find that it surpasses all training-free metrics and exceeds fine-tuned evaluators on two out of three human-correlation benchmarks.

---


### 236. [NeutronGym: Physics-Graded Neutron Instrument Design for LLM Agents](https://arxiv.org/abs/2610.03631)

**<font color=#1a73e8>作者：</font>** Lijie Ding, Changwoo Do  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing a scientific instrument tests whether language-model agents can do physics rather than recall it, provided the grading cannot be argued with. We introduce NeutronGym, to our knowledge the first executable environment for neutron instrument design: agents build instruments through validating tools, McStas ray-traces what they build, and a level-resolved ladder grades syntax, runtime, structure and science with no LLM judge. Procedural families supply unlimited instances of a fixed layout whose design parameters the agent must set, with held-out parameter regimes; a curated slice, McStasBench, adds 16 tasks from published instruments behind memorization probes and a sandbox. Seven models reproduce at most 7 of the 16, none retrieves a reference, and none meets an improvement target. The environment also trains. Reinforcement learning on its reward takes Qwen3-8B from 11% to 77% of held-out instances of a family whose targets come from a hidden design (69% at a second seed), past an untrained Qwen3-32B, and the recipe holds, at one seed each, on three further gated families. The analysis says what that gain is. Without the ladder's partial credit it collapses by 60 points. From reward alone the trained model reaches what a classical optimizer reaches, at the agent's simulation budget, only when handed the closed-form physics (77% against 81%, a gap that does not separate at this size), while frontier models still solve 98-99%. Getting a trustworthy result meant failing four task designs that no-model baselines could solve, and we release the probes that found them.

---


### 237. [World Embedding Benchmark](https://arxiv.org/abs/2610.03632)

**<font color=#1a73e8>作者：</font>** Yiqi Liu, Ruifeng Yuan, Yang Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical fidelity has received increasing attention in world models and video generation, yet how video representations encode physical information remains less understood. We introduce the World Embedding Benchmark, comprising 8,000 controlled simulation cases from 80 families spanning fluid mechanics, solid mechanics, dynamics, and optics & electromagnetism. Each case pairs a rendered video with simulation-derived physical annotations, supporting three complementary tasks: text-video retrieval, physical-property regression, and multiple-choice video-description pair classification. We use these tasks to distinguish cross-modal physical alignment from the recoverability of quantitative physical information. Evaluated pre-trained omnimodal embedding models show weak retrieval and near-chance within-family pair classification, while lightweight probes recover useful physical information from frozen video embeddings. Continual contrastive training with physics-specific video-text pairs improves retrieval and pair classification but degrades physical-property regression, revealing a trade-off between alignment and quantitative information recoverability. Finally, we use the embeddings to retrieve reference videos for retrieval-augmented generation with MiniMax-H3. Retrieved references improve the physical fidelity of generated videos, with stronger retrieval models yielding larger gains in our experiments. Together, these findings highlight the need to evaluate physical alignment and property recoverability jointly, and demonstrate the utility of physical representations for improving video generation.

---


### 238. [Do Large Language Models Know Colombian Law? A Reliability Benchmark for the Colombian Legal System](https://arxiv.org/abs/2610.03639)

**<font color=#1a73e8>作者：</font>** Rubén Manrique, Michelle Castellanos, Jorge Morales 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to support legal practice, education, and research, yet their reliability in national legal systems outside the United States remains largely undocumented. We introduce an expert-validated benchmark for evaluating LLM reliability on the Colombian legal system. The benchmark comprises 1,042 items spanning ten areas of law and three question formats (closed multiple-choice, semi-open, and open-ended IRAC), built through a human-in-the-loop pipeline with multi-stage expert review. We evaluate 15 contemporary proprietary and open-weight models with format-appropriate metrics. Accuracy on closed questions ranges widely, from 0.905 (Gemini 3.1 Pro) to 0.577, but on free-text legal answers factual correctness never exceeds 0.45 (on a 0-1 scale) for any model. We find a dissociation between answer relevancy and correctness (Spearman rho = -0.46): models reliably sound responsive while frequently being wrong, a pattern of particular concern for non-expert users. Closed-question accuracy and free-text correctness are strongly rank-correlated (rho = 0.94), so cheap multiple-choice screening predicts model ranking but overstates absolute reliability. An independent rubric-based LLM judge and blind human expert scoring both reproduce the free-text ranking (rho >= 0.88). The judge further reveals that only about half of the norms models cite are correct; the rest are wrong or non-existent. Reliability varies systematically by legal area and follows an inverted-U across question complexity. Our results indicate that current LLMs require expert supervision for Colombian legal tasks, and that grounding answers in authoritative sources is a promising path to higher reliability. We release the benchmark construction pipeline to support reproducible evaluation.

---


### 239. [Pivot-SD: Efficient Self-Distillation for Masked Diffusion Language Models](https://arxiv.org/abs/2610.03665)

**<font color=#1a73e8>作者：</font>** Seo Hyun Kim, Sunwoo Hong, Younwoo Choi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (dLMs) offer a promising parallel alternative to autoregressive models for complex reasoning. However, they face a distinct credit-assignment challenge, since a few commitments during denoising sharply reduce the uncertainty over the remaining masked positions and shape much of the response. Most post-training recipes for dLMs do not use this signal to decide which tokens to train on: they typically train on the final text or assign rewards to whole denoising steps, rather than selecting the individual commitments that shape the response. We introduce Pivot-SD, an efficient offline self-distillation framework that supervises only these high-impact commitments (pivots). Pivot-SD selects pivots using an information-gain metric measuring uncertainty reduction over the remaining masked positions. Pivots from successful trajectories are trained with cross-entropy, and pivots from failed trajectories with targeted unlikelihood, leaving the rest of the failed trajectory untouched. Using only 200 questions and four rollouts each, Pivot-SD improves LLaDA-8B-Instruct over full-sequence SFT and budget-matched diffusion RL baselines across math and code benchmarks.

---


### 240. [Planning to Learn](https://arxiv.org/abs/2610.03667)

**<font color=#1a73e8>作者：</font>** Ian Osband  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy-gradient methods are central to modern reinforcement learning, including LLM post-training. When they struggle, the usual suspects are exploration, credit assignment and action-sampling noise. Classification has none of them. A classifier is a policy whose expected reward, its \emph{expected accuracy}, is the probability it assigns to the correct label, and because that label is known, the policy gradient is exact and smooth. Yet exact policy gradient loses to cross-entropy, even on expected accuracy. The exact gradient is myopic: it values an update only by what it buys now, but each update also sets where the next one starts, so an update's value depends on how much learning remains. Viewed this way, cross-entropy is patient accuracy, the total error an example would pay if its log-odds rose at unit speed forever, while exact policy gradient is the zero-horizon limit. Truncating this total at the learning that remains yields the horizon loss, a one-line change that moves from cross-entropy toward exact policy gradient as training runs out. In a simple allocation model, it provably escapes the trap that catches each endpoint. On MNIST and on ImageNet with ResNet-50, ResNet-101 and ViT-S/16, the horizon loss improves top-1 accuracy over cross-entropy at a flat learning rate, and the gain grows with label noise.

---


### 241. [Language Models that Play Chess and Explain Their Moves](https://arxiv.org/abs/2610.03695)

**<font color=#1a73e8>作者：</font>** Adithya Bhaskar, Jeffrey Cheng, Danqi Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern chess engines are silent experts: they play at a superhuman level, but do not offer explanations for their play. On the other hand, language models (LMs) can generate plausible-sounding explanations, but their weak playing strength limits the utility of their explanations. We introduce Queen, a 4B-parameter chess-language model that can explain its moves and plans while playing at the level of a typical Grandmaster. Our novel framework enables domain-specific reasoning through complementary components: an encoder-decoder architecture and an iterative distillation algorithm. This architecture integrates a silent expert chess encoder with an instruction-tuned LM through cross-attention, which we train via a question-answering curriculum to extract chess concepts from the encoder's representations. Building on this domain-adapted model, we iteratively improve its explanations with a natural-language analog of the Bellman update: the model analyzes the positions after its top candidate moves and consolidates them into an explanation of the current position, which is then distilled back into the model. Over seven iterations, our model gains over 900 Elo points (1782 to 2697), substantially surpassing all frontier models on both playing strength and puzzle accuracy, despite containing three orders of magnitude fewer parameters. Furthermore, LM-based evaluations show that our explanations are fluent and approach GPT-5.6-Sol (high) in coherence. The generality of our architecture and training procedure suggests a recipe for applying language models to domains where silent expert encoders are available, like games, robotics, and computer use.

---


### 242. [LESSER: Post-Training Data Selection with Output-Layer Gradients](https://arxiv.org/abs/2610.03702)

**<font color=#1a73e8>作者：</font>** Lyuxin David Zhang, Eric Wong, Surbhi Goel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The choice of post-training data for large language models substantially affects downstream performance. Gradient-based data selection is a popular approach that ranks training data by how well their gradients align with those of a small validation set. However, ranking with full-parameter gradients requires an expensive backward pass on every sample, making computation intractable for large candidate pools. This raises a natural question: can we approximate full-gradient features at a fraction of the cost? Conveniently, we find that output-layer gradients suffice for effective data selection, yet require only the cheaper forward pass. We implement this as LESSER, a drop-in wrapper for selection methods that reduces the feature-extraction FLOP cost by $9.7\times$ for SFT and $3.0\times$ for RL benchmarks, while tracking full-gradient performance on downstream tasks. Empirically, we find that even when output-layer and full gradients rank individual samples differently, they select batches with aligned gradients.

---


### 243. [What Should World Models Forget? Stratified Retention for Continual Adaptation](https://arxiv.org/abs/2610.03713)

**<font color=#1a73e8>作者：</font>** Nishit Anand, Ramani Duraiswami, Dinesh Manocha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning treats degradation on previously seen data as evidence of failure, a convention inherited from settings with a stationary prediction target, where a correct label remains correct indefinitely. World models do not satisfy this condition. Their prediction target is the environment, which changes, so knowledge that was accurate when acquired may later become false, and discarding it is required behavior rather than a defect. Non-stationary ground truth is well studied in the concept drift literature and in the temporal factuality of language models, but has not been formulated for world models, which are distinctive in that they also encode knowledge that must never be revised. We argue that continual world models require retention stratified by invariance timescale, separating invariants such as physics and object permanence, which must never be revised, from instance-level facts that should be revised as soon as the environment changes. Standard forgetting metrics cannot distinguish a world model that has correctly revised outdated knowledge from one that has suffered catastrophic forgetting, and consequently rank a frozen model highest, while existing physical-reasoning benchmarks evaluate only frozen checkpoints. We propose differential retention, which reports invariant regression testing across the adaptation stream jointly with revision latency, without aggregation.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 244. [SCOPE-4D: Endoscopic 4D Geometry Foundation Models](https://arxiv.org/abs/2610.02343)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chaoyi Zhou, Zhongpai Gao, Anwesa Choudhuri 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometric understanding supports endoscopic navigation and robotic assistance, but learning reliable endoscopic geometry faces two challenges: scarce geometric annotations and ambiguity between camera motion and tissue deformation. We present SCOPE-4D, an endoscopic 4D geometry foundation model that jointly predicts camera parameters, dense geometry, and 3D tissue trajectories from monocular RGB video in a single forward pass. Our curation and annotation pipeline constructs SCOPE-5K, a collection of approximately 5,000 clips spanning real and synthetic gastrointestinal endoscopy and laparoscopy. The collection provides rich geometric supervision and includes newly collected phantom and real-colonoscopy evaluation sets. Geometric supervised fine-tuning on SCOPE-5K learns endoscopic priors that improve camera and depth estimation. Common--Residual Motion (CRM) further constrains local deformation relative to common tissue movement. Together with geometric supervision, CRM and trajectory supervision further improve camera and depth estimation over geometric fine-tuning alone while enabling dense 3D tissue tracking. Evaluations on public and newly collected benchmarks demonstrate strong in-domain and out-of-domain geometry, superior 3D tracking, and more stable long-sequence colon reconstruction. A blinded user study further supports the perceived reconstruction quality on real clinical video. Together, these results demonstrate the value of large-scale endoscopic supervision and motion constraints for joint geometry estimation and tissue tracking.

---


### 245. [From Behavior to Provenance: Attributing Tabular Foundation Models to Synthetic Pretraining Data](https://arxiv.org/abs/2610.02347)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mohamed Bouadi, Nassim Bouarour, Shivam Dubey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training-data attribution aims to identify which training examples shape model behavior, yet validating such claims is difficult because causal training influence is rarely observable. We argue that controlled synthetic pretraining makes attribution experimentally testable. Using O'PRIOR, a provenance-rich synthetic task generator for tabular foundation models, we construct a testbed in which every pretraining task carries explicit lineage over structural mechanisms, missingness, confounding, shortcuts, and distribution shift. We combine behavior-conditioned attribution with counterfactual retraining and provenance-aware interventions to test both task-level faithfulness and mechanism-level consistency. On held-out real tasks, removing the top-attributed 5% of synthetic tasks decreases mean ROC-AUC by 0.013, compared with 0.002$\pm$0.004 under random removal, while removing bottom-attributed tasks improves performance by 0.003. Within shortcut-provenance tasks, targeted removal yields an effect of 0.043 versus 0.016 for matched random removal. Provenance discrimination is more modest by ranking AUROC (0.55-0.62), despite substantial top-k enrichment, revealing that provenance association and interventional faithfulness need not coincide. Our results establish synthetic provenance as a controlled setting for verifiable contributive attribution

---


### 246. [Prompted to Discriminate: Generalizing Malicious-Input Probes in the Wild](https://arxiv.org/abs/2610.02413)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Elad David, Max Fomin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on activation probes as runtime monitors for prompt injection, jailbreaks, and unsafe requests, reading the model's own hidden state to catch a harmful input before the agent acts on it. A cheap, increasingly common move, borrowed from LLM-as-judge prompting, is to append a short classification instruction after the user's turn and read the probe at that point, to sharpen it: the instruction asks the model to represent the incoming request as a class, concentrating the signal the probe must separate, at negligible serving cost. But does the wording of that suffix matter, and does its benefit hold in the wild, on attack types the probe never saw in training, the regime a deployed monitor faces? We test this with a controlled ladder of post-user suffixes under strict leave-one-dataset-out (LODO) evaluation across 13 safety benchmarks (jailbreak, injection, and benign chat) and three open-weight model families (Llama-3.1-8B, Qwen3.5-9B, Gemma-4-12B). On a single-position probe, a classification suffix consistently improves out-of-distribution detection over no suffix (up to ~4 AUC points); yet which suffix matters: prompting the model to classify the input, even into content-free labels, reliably wins; an off-topic or merely-attentive suffix helps little. The gain comes from the classification format, not the named criterion: a content-free suffix matches the real malicious/benign one, with the criterion adding precision only at strict thresholds. This is not an artifact of the single-position read: the benefit carries to the multi-position pooling probes used in production (attention, multi-max, MLP), though the best-performing suffix there is readout-dependent. Served through a KV-cache fork, it is a cheap drop-in for any activation-probe monitor, though not an automatic win: which suffix helps, and by how much, depends on the model and the readout.

---


### 247. [LiteEMG-FM: An Efficient and Deployable Foundation Model for Robust EMG Sensing](https://arxiv.org/abs/2610.02497)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianhao Wu, Xu Wu, Amirmohammad Radmehr 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electromyography (EMG) signals vary substantially across individuals, body regions, recording sessions, and sensing hardware, limiting the generalization of models for assistive devices and human-computer interaction. Existing time-series foundation models are also computationally expensive for real-time wearable deployment and often fail to capture EMG-specific time-frequency characteristics. We present LiteEMG-FM, an efficient hybrid CNN-Transformer foundation model for practical EMG sensing. Pretrained on 16 diverse upper- and lower-limb EMG datasets, LiteEMG-FM learns representations that generalize across users and datasets. For resource-constrained deployment, we implement a hierarchical wake-up architecture in which a lightweight, always-on 1D-CNN filters rest and non-target activity and activates LiteEMG-FM only for valid gestures. We evaluate full inference offloading, split inference, and full on-device processing, characterizing their trade-offs in latency, power consumption, and memory footprint. Across diverse evaluation settings, LiteEMG-FM outperforms state-of-the-art time-series foundation models and supervised baselines, particularly under zero-calibration cross-participant and data-scarce conditions. These results demonstrate that LiteEMG-FM is an effective, efficient, and deployable foundation model for EMG applications.

---


### 248. [Test-time Multi-agent Coordination by Decomposed Value Gradient Flow](https://arxiv.org/abs/2610.02554)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dongsu Lee, Haoran Xu, Amy Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline multi-agent reinforcement learning (MARL) faces a persistent trade-off. Expressive generative policies can represent multi-modal coordination in the data, but cannot distinguish high-value regions, while value-optimized policies exploit the learned Q-function but collapse the multi-modal into a single dominant mode. A single agent's mode collapse can break joint coordination, and simultaneous drift across agents can push the joint policy into unseen regions of the action space. We propose scalable coordination via optimal unified transport (SCOUT), the first offline MARL framework to combine a generative foundation model with a learned value function through test-time action refinement. SCOUT trains two decoupled components: a flow-matching behavioral prior and a decomposed value function. At test-time, it transports behavioral samples toward high-value regions via Stein variational gradient descent. The number of transport steps controls adaptive test-time scaling, replacing a fixed regularization coefficient. Under the individual-global-max (IGM) principle, we prove a single-term KL bound on the joint soft-value gap that vanishes as transport converges, with an irreducible additive residual proportional to the IGM violation. Empirically, SCOUT achieves the best average performance across discrete and continuous offline MARL benchmarks and yields performance improvements in all offline-to-online configurations.

---


### 249. [GRAFT: Growing Agglomerative Foundation Models via Continual Teacher Distillation](https://arxiv.org/abs/2610.02597)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhenghao Zhao, Chi Zhang, Qingshuang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models such as DINOv2, SigLIP2, and MASt3R develop complementary capabilities from different pretraining objectives, yet their knowledge remains distributed across separate, specialized models. Multi-teacher knowledge distillation offers a path toward consolidating these capabilities into a single agglomerative backbone, but existing approaches assume a fixed set of teachers, and incorporating a new teacher requires repeating expensive joint distillation over the entire teacher set. We introduce GRAFT, a continual multi-teacher distillation framework that enables a unified backbone to progressively acquire capabilities from an open-ended sequence of foundation models. When a new teacher arrives, GRAFT treats the previously distilled model as a teacher for preserving learned capabilities, while the current student jointly learns from both the previous model and the incoming teacher. Furthermore, to reconcile the incompatible representation geometries of heterogeneous teachers, we introduce Teacher Specific Readout Tokens, which grant each teacher an independent read-out of the shared encoder, together with Geometry Agnostic Relational Loss that aligns a vision-language teacher by matching image-text similarity structures rather than raw feature values. We provide GRAFT model, which is a single, continually extensible backbone that unifies five domains, including image understanding, 2D dense prediction, 3D human pose estimation, 3D vision, and vision-language, delivering strong performance across all of them while acquiring each new capability at the cost of a single distillation rather than a full re-distillation.

---


### 250. [Prospective Hindsight: Self-Calibrating Reinforcement Learning via Prediction-Reality Gaps](https://arxiv.org/abs/2610.02740)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiaxin Zhang, Xiangyu Peng, Qinglin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for long-horizon agents relies on purely retrospective training signals: credit is assigned only after observing environmental consequences, leaving the agent's belief at action time invisible to the gradient. We introduce Prospective Hindsight (PH), a self-calibrating training principle that augments any retrospective base method with a signal derived from the gap between the agent's prospective prediction (before feedback) and the retrospective evaluation (after feedback). This per-rollout surprise identifies samples where the agent's self-model is most inaccurate and amplifies their gradient contribution through a stop-gradient surprise-weighted advantage. Since the prospective predictor shares parameters with the policy, the two co-evolve, progressively shifting focus to the agent's remaining blind spots. We connect this principle to a privileged-information gap and show that minimizing the surprise residual provides a descent pathway on the agent's miscalibration rate; calibration thus emerges as a byproduct of optimization rather than from an added objective. On single-turn verifiable tasks and a multi-turn personal-agent task (under GRPO, on-policy distillation, and their combination), PH improves both task performance and calibration, with consistent gains across model scales. Notably, the dominant miscalibration mode shifts structurally between regimes, overconfident failures in single-turn, underconfident successes in multi-turn, yet the same training principle addresses both successfully.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-261](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

# 🧠 大模型相关研究 | 2026年10月12日

> 本类共 **288** 篇论文：已确认 **273** 篇，待复核 **15** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-288](./part-06.md)

---

### 51. [NOMOS: Compiling Written Policies into Statically Verified Tool-Call Gates for LLM Agents](https://arxiv.org/abs/2610.11030)

**<font color=#1a73e8>作者：</font>** Min-Young Yu, Tony Kim, Jang Won Choi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents violate the policies they are deployed to enforce, often silently. Prior defenses hand-write rules, query an LLM verifier per action, or compile policies through heavyweight formal machinery. Naive compilation fails: extracted rules block the tool satisfying their own precondition, or read arguments their tool lacks. NOMOS, a four-pass compiler, turns a natural-language policy into a deterministic tool-call gate; static verification with tool-schema-level checks alone (no prover, solver, or LLM) repairs or rejects 37% (airline) and 13% (retail) of candidates, without which most shipped rules are inoperable. Replaying compiled rules over undefended transcripts flags bindings that refuse legitimate work (a development binding refused 95.9% of task-passing calls); no evaluation binding is flagged. On $\tau^2$-bench the gate cuts violations of reference-encoded clauses among state-changing calls from 66.3% to 2.6% (airline) and 30.8% to 6.9% (retail), raising airline task success significantly for $2 \le k \le 4$; a 26B on-premise compilation is not significantly worse than hand-written or frontier-compiled rules. Unlike AgentDojo's shipped defenses, it reaches a zero attack success rate (ASR) on banking, where nine attack families collapse onto three structural rules. On the other three suites its ASR is at most 3.6%, from goals with no tool call to govern and one write admitted by a binding weaker than its clause; a second agent model, Llama-3.3-70B, reproduces the effect on both benchmarks. Decisions take microseconds without an LLM call, at a domain-dependent benign-utility cost; compilation runs on-premise on open-weight gemma-4-26B.

---


### 52. [FedAlphaEdit: Null-Space-Aligned Merging for Collaborative Knowledge Editing](https://arxiv.org/abs/2610.11033)

**<font color=#1a73e8>作者：</font>** Sota Sugawara, Yukihiko Okada  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multiple institutions may each hold their own private knowledge edits and wish to integrate them into a single large language model without sharing raw edit requests. Null-space-constrained editing methods such as AlphaEdit mathematically guarantee that each update leaves unrelated knowledge intact, while collaborative frameworks such as CollabEdit aggregate edits from multiple clients without data sharing. Combining the two appears trivial. However, we show that this naive combination fails structurally, and we identify its cause. Guided by this analysis, we propose FedAlphaEdit. To our knowledge, this is the first collaborative knowledge editing framework that aligns both local editing and the server-side merging rule under a single null-space principle for preserving existing knowledge. FedAlphaEdit builds on null-space-aligned merging, in which clients share projected statistics and the server provably recovers the result of editing everything in one place under a one-shot idealization. Empirically, the proposed method repairs the collapse and brings edit success and preservation simultaneously close to the level of centralized editing across two architecture families. FedAlphaEdit thus lets institutions that cannot share raw edit data, such as hospitals and financial firms, jointly maintain a shared model that closely approximates editing all facts in one place.

---


### 53. [Rendering-Free Lookahead for Question-Guided Active Vision](https://arxiv.org/abs/2610.11039)

**<font color=#1a73e8>作者：</font>** Koya Sakamoto, Daichi Azuma, Shuhei Kurita 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Active robot vision requires controlling the camera to reveal task-relevant information that is hidden from the current viewpoint. For example, determining what is inside a box may require raising the camera and looking down into it. For viewpoint-dependent question answering, the challenge is to select camera motions that expose the visual evidence needed to answer the question. Although vision-language models (VLMs) can interpret observed images, selecting such motions requires anticipating the usefulness of unseen views. We quantify this usefulness as answerability, a VLM's estimate that a view suffices to answer the question, and present Rendering-Free Lookahead (RFL), a viewpoint-selection policy that ranks candidate camera motions by predicted future answerability. RFL transfers visual lookahead from deployment to offline training. At training, a privileged teacher renders candidate future views in 3D Gaussian Splatting (3DGS) scenes and uses a frozen VLM to compute one- and two-step answerability targets. Through two-stage distillation, a student learns to predict these action values from the question, recent visual observations, and a candidate camera motion. At deployment, RFL uses these predicted values to select camera motions without rendering future views. On 377 E3VS-Bench test episodes in unseen environments, RFL improves the mean judge score by 43\% over a direct-action baseline using the same VLM. These results support learning camera-control policies from privileged visual lookahead for viewpoint-dependent question answering.

---


### 54. [AgentHorizon: Evaluating Agentic Judges for Long-Horizon Computer-Use Tasks](https://arxiv.org/abs/2610.11050)

**<font color=#1a73e8>作者：</font>** Xing Han Lù, Dheeraj Vattikonda, Sina Hajimiri 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents are capable of completing complex tasks, increasing the use of automatic judges to determine success, either for training or for evaluation without human involvement. Despite their flexibility, their reliability on long tasks spanning multiple applications remains unclear. A trajectory, composed of long sequences of screenshots and actions, may appear complete, but in reality violates constraints from the instruction or introduces an unwanted side effect. To identify these errors, a judge needs to examine the trajectory with respect to the user's instruction. To this end, we introduce AgentHorizon, a benchmark of 1,373 computer-use tasks (instruction-trajectory pairs) drawn from 166 hours of human-recorded trajectories spanning three operating systems. By recording trajectories for closely related instructions, we can construct negative tasks by swapping the instructions. This paired design evaluates judges on their ability to distinguish a successful trajectory from one that completed a similar (but incompatible) request. We release the benchmark under three splits: a frontier split, AgentHorizon (AH), a simplified split, AgentHorizon-Simple (AH-S), and a development split, AgentHorizon-Development (AH-D). We further evaluate eleven judges by (1) directly passing the full trajectory (with up to 300 screenshots and actions), and (2) using them as coding agents across five agent harnesses. We find that our best agentic judge, GPT-5.5, achieves 80.9% balanced accuracy on the AH subset. We find that tool-use improves certain models but results in worse performance for open-weight models, and that judges differ drastically in their ability to accept a valid trajectory and reject failed ones. Our findings highlight the need for judges that are capable of locating and verifying often hidden evidence that a task was properly completed inside long interaction histories.

---


### 55. [AffordDrive3D: Affordance-Aware World-Action Modeling with Spatial Understanding](https://arxiv.org/abs/2610.11060)

**<font color=#1a73e8>作者：</font>** Tianhui Cai, Xinglong Sun, Chao Fang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-action models have recently improved autonomous driving by jointly learning future scene prediction and trajectory generation. Most existing approaches model the future primarily through RGB appearance, and recent works have begun to incorporate geometric prediction to improve spatial understanding. However, dense geometry describes the spatial layout of the entire scene without indicating which parts are most relevant to the ego vehicle's action. For driving, the model must also identify and anticipate where it can safely move and which regions may pose collision risks. Jointly modeling action-relevant regions and future geometry can provide the policy with both driving-relevant cues and their corresponding spatial structure. We therefore propose AffordDrive3D, an affordance- and geometry-aware world-action model that jointly learns future action-relevant regions and spatial structure. In order to capture the scene semantics and driving context needed for driving affordance prediction, we build AffordDrive3D on a VLM backbone to forecast drivable areas and collision-critical regions that directly affect ego motion, while predicting future geometry from RGB world-model latents. On NAVSIM, AffordDrive3D achieves state-of-the-art performance with 91.3 PDMS and 89.9 EPDMS, demonstrating the effectiveness of jointly modeling future affordances and geometry for trajectory planning.

---


### 56. [Emergent Inverse-Depth Scaling From Nonlinearity In Attention](https://arxiv.org/abs/2610.11063)

**<font color=#1a73e8>作者：</font>** Zirui Peng, Yizhou Liu, Ziming Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws describe power-law improvements in model performance with dataset size and parameter count, yet their underlying mechanisms are not fully understood. To explain the parameter count scaling, existing theory posits power-law scaling with model depth. In linear-attention models, this scaling is tied to a power-law data spectrum: unable to selectively attend to relevant tokens, these models learn according to global spectral strength, with stronger directions learned before weaker ones. Large language models, however, can be strongly nonlinear. Here, we show that nonlinear attention yields inverse-depth decay of loss across all tested data spectra. Nonlinearity enables attention to focus selectively on relevant tokens, allowing strong and weak spectral directions to be learned in parallel. Similar focusing across layers motivates a connection to the central limit theorem: shared error across layers sets the loss plateau, while aggregation turns layer-specific differences into continued gains with depth. Our findings suggest that depth scaling may arise from nonlinearity in attention, which allows large language models to focus locally and may make the global covariance structure less relevant.

---


### 57. [Measuring and Mitigating Solution Mode Collapse in RLVR](https://arxiv.org/abs/2610.11064)

**<font color=#1a73e8>作者：</font>** Liv G. d'Aliberti, Marwa Abdulhai, Sofiia Druchyna 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A language model (LM) can usually answer the same question in more than one way, but reinforcement learning with verifiable rewards (RLVR) is indifferent to which correct answer a model produces. A solution will earn the same reward whether it is the thousandth copy of a familiar answer or one the model has never produced before. Yet, there is potential value in having the model retain multiple correct solutions as it is trained. For instance, multiple modes may give users a choice and provide problem-solving strategies that improve overall model performance. Here, we introduce ModeBench, a benchmark of multi-solution tasks in which the verifier returns both correctness and mode discovered. We then use ModeBench to measure how solution diversity changes under RLVR post-training. We find that RLVR post-training concentrates probability onto fewer correct modes even as accuracy holds or improves, and moreover, that frontier models are already highly concentrated. We then introduce our solution, Re:Max, which stores one verified example per discovered mode in a replay buffer and trains on those stored modes uniformly. A solution found once is, therefore, practiced as often as one found repeatedly. Across three model scales, two RL objectives, and harder task constructions, replay improves both how often a policy succeeds and how many different ways it can succeed.

---


### 58. [Clinician use of language models diverges from how the models are evaluated](https://arxiv.org/abs/2610.11069)

**<font color=#1a73e8>作者：</font>** Krithik Vishwanath, Haitong Lin, Anton Alyakin 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) assistants are being deployed to clinicians across health systems, and judgments about their readiness rest largely on benchmark scores, most of them derived from examination questions or curated cases. A benchmark predicts performance in deployment only to the extent that its items resemble real use, yet whether benchmarks reflect the work these systems receive has rarely been measured. Here we analyze 127,833 queries sent by 6,342 physicians, advanced practice providers and nurses in 35 specialties to an institutional assistant during an eight-month roll-out. We characterize each query with RCQ-Map, a clinician-validated framework grounded in taxonomies of clinical questions and of LLM evaluation, which records its task, intent, answerability, missing information and potential harm. Documentation and administration (36.2%) and knowledge retrieval (28.9%) made up nearly two-thirds of use, and diagnosis 3.7%; more than a third of queries could not be answered well as posed. Applying RCQ-Map to 58 public benchmarks drawn from major evaluation suites and frontier model reports, which we assemble into the Clinical AI Benchmark Atlas, showed that the median benchmark contained no documentation requests and shared 31% of the task mix of real use, less than an even spread across task categories would. Benchmarks in suites designed to resemble clinical practice were individually no closer to real use than those used in frontier model reports. Benchmark scores therefore say little about how clinical AI performs on most of the work it is actually given, and evaluation should be matched to real clinical use.

---


### 59. [Stability-Plasticity Balance via Singular-Vector Selection in LLM Continual Learning](https://arxiv.org/abs/2610.11076)

**<font color=#1a73e8>作者：</font>** Lingxiang Wang, Hainan Zhang, Liang Pang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain-specific continual adaptation of LLMs risks catastrophic forgetting, creating a fundamental tension between acquiring new capabilities and preserving those learned during pretraining. PEFT mitigates this problem by restricting the number of trainable parameters, but existing methods lack a principled unit for deciding where plasticity should be allocated and stability should be preserved. We identify the singular-vector channel as a natural unit for managing this trade-off. Each channel represents an input-output transformation, which can be updated to acquire new knowledge or fixed to preserve pretrained capabilities. Based on this perspective, we introduce SVC, a parameter-efficient continual-learning method that selectively updates Singular-Vector Channels. Before fine-tuning, SVC uses domain-specific data to estimate each channel's adaptation benefit and a fixed public general-domain corpus only as a history activation proxy for estimating forgetting cost. It then adaptively selects trainable channels based on these scores via knee-based cost screening, Pareto-front filtering, and Otsu thresholding. Experimental results across four LLM families and eight downstream tasks show that SVC better preserves pretrained capabilities while achieving strong downstream performance relative to existing PEFT baselines. Further analysis of channel scoring and selection demonstrates that selective plasticity at the singular-vector-channel level enables effective continual LLM adaptation.

---


### 60. [Beyond Imitation: A Framework and Benchmark for LLM-Assisted Peer Review](https://arxiv.org/abs/2610.11087)

**<font color=#1a73e8>作者：</font>** Rachel S.Y. Teo, Yutaro Yamada, Shashank Kotyan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid growth of scientific publishing has strained peer review, particularly in machine learning, raising concerns about declining review quality and increasing reviewer workload. Large language models (LLMs) have been proposed as automated review assistants, yet their evaluation has focused largely on imitating human-written reviews rather than supporting the core functions of peer review. Here, we introduce a verification-centric perspective on LLM-assisted peer review, emphasizing error detection as a critical and resource-intensive task. We present a scalable benchmark that evaluates review systems' ability to identify logical contradictions, constructed through synthetic insertion of errors into conference papers, yielding unambiguous evaluation targets and enabling systematic comparison. We further propose a Multi-Layered Review (MLR) framework that prioritizes detailed manuscript comprehension before review generation, aligning more closely with human reviewing practices while improving token efficiency. Across evaluations, our approach demonstrates strong alignment with human review scores, achieves high error detection performance, and provides complementary perspectives on reviewer focus. These improvements can be attributed to both the choice of the underlying LLM and the design of our system. At the same time, we corroborate persistent vulnerabilities to adversarial manipulation, underscoring the need for robustness in automated review systems. Our findings highlight the importance of rigorous, error-focused evaluation to guide responsible deployment of LLM-based tools in peer review and other critical scientific workflows.

---


### 61. [Lapras: Latent Reasoning for Time Series Language Models](https://arxiv.org/abs/2610.11111)

**<font color=#1a73e8>作者：</font>** Yuliang Chen, Yu Yvonne Wu, Patrick Langer 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Time Series Language Models (TSLMs) offer a promising path toward time series understanding by reasoning over temporal signals and producing natural language answers and explanations. A common approach is Chain-of-Thought (CoT), which generates step-by-step rationales linking relevant signal patterns to final answers. Although these models learn from reference CoT traces during post-training, generating faithful descriptions of input time series at inference remains challenging. Expressing high-dimensional, continuous temporal representations in discrete language tokens may cause the model to neglect task-relevant patterns or describe them inaccurately. Because later reasoning steps build on these descriptions, early errors propagate, leading to incorrect answers with plausible explanations that are inconsistent with the input signal. We propose Lapras (Latent Post-trained Reasoning Across Series), a post-training framework that equips TSLMs with latent reasoning. A model trained with Lapras reasons through a sequence of continuous thoughts in the joint time series-language space, producing text only for the final answer. It learns this through teacher-student self-distillation, where a teacher trained on CoT reference traces reasons explicitly through text. The student aligns its hidden states with the teacher's at the answer stage, transferring the teacher's reasoning ability into its latent computation. We evaluate Lapras across four TSLM backbones on five time series question answering benchmarks. Lapras improves average F1 by up to 10.79% over explicit CoT while generating 23.9x fewer tokens. Lapras's continuous thoughts can also be decoded into readable reasoning traces via standard language decoding, preserving textual explanations. Together, these results highlight Lapras as a promising post-training paradigm for efficient, effective, and interpretable TSLM reasoning.

---


### 62. [DiscoVL: Unveiling Disentangled C ross-Modal Representation Learning via Orthogonal Adversarial Regularization for V ision-Language Models](https://arxiv.org/abs/2610.11113)

**<font color=#1a73e8>作者：</font>** Mengping Dong, Jinbao Li, Fei Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained vision-language models excel across varied perception tasks, but adapting them to novel downstream settings without sacrificing generalization remains non-trivial. Existing parameter-efficient prompt learning method often yields inconsistent representations and fails to account for semantic distribution shifts. In this work, we present DiscoVL, a disentangled cross-modal representation learning framework that couples orthogonal adversarial regularization with structured cross-modal alignment for vision-language models. To address the insufficient cross-modal interaction, our DiscoVL designs a multi-branch low-rank residual aligner that decomposes representations into subspaces and enables bidirectional cross-modal feedback between visual and textual streams at each layer. Furthermore, while conventional triplet constraints overfit features to class centroids, we design an orthogonal regularization for adversarial triplet loss, which prevents centroid collapse and substantially boosts generalization. Evaluations on 15 benchmarks demonstrate that DiscoVL delivers consistent improvements over state-of-the-art methods for base-to-novel generalization, cross-dataset evaluation, and few-shot learning

---


### 63. [Dynamics as Code: On Model Compression via Dynamic System](https://arxiv.org/abs/2610.11115)

**<font color=#1a73e8>作者：</font>** Fan Gao, Wei Su, Juntong Fan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The escalating size of pretrained neural networks has rendered model compression a prerequisite for deployment under stringent memory and compute constraints. With the irrational winding as an example, earlier work introduced a dynamic system (DS) paradigm that reconceptualizes compression as compact weight representation: high-dimensional parameters are encoded by the index of a trajectory produced by a dynamic system, from which the vector is recovered during decompression. This mechanism is fundamentally distinct from pruning, quantization, knowledge distillation, and low-rank decomposition. Along this direction, we prove that under a Diophantine condition, a finite trajectory of \(M = O(\epsilon^{-(d+\nu)})\) states in the irrational winding constitutes an \(\epsilon\)-net over the \(d\)-dimensional weight space, thereby linking state resolution, decompression error, and compression ratio in a predictable manner. Furthermore, we propose a generalized DS-based model compression framework by unifying four DS families---space-filling curves (Hilbert, Peano, Morton/Z-order, Snake), chaotic systems (Lorenz), congruential and pseudo-random generators (LCG, PCG), and low-discrepancy sequences (Halton). Also, we introduce the KD-tree and coordinate-template acceleration to scale to large models as well as outlier identification to control the error. Experiments on ResNet-18 and Qwen2.5-1.5B/Qwen1.5-7B validate that DS-based compression achieves competitive compression ratios without post-hoc retraining, with controllable decompression error and flexible state-space design, establishing it as a principled and practical compression approach.

---


### 64. [OpenProblemBench: Benchmarking AI on Open Problems in the Foundational Theoretical Sciences](https://arxiv.org/abs/2610.11118)

**<font color=#1a73e8>作者：</font>** Zhiyi Li, Sihan Hu, Tianning Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The next frontier for artificial general intelligence is tackling unresolved scientific problems, calling for benchmarks that assess progress beyond established knowledge. We introduce OpenProblemBench, a benchmark of 82 unresolved problems drawn from the mathematics and theoretical physics literature. Each problem supplies the research context, assumptions, and prior progress needed to investigate the question. We select problems whose proposed solutions admit comparatively clear checks of their decisive mathematical or computational claims. Four evaluator models independently assess the correctness, completeness, and degree of progress of each submission without reference solutions. Across seven evaluated configurations, GPT-6-Astra achieves the highest mean judged solve rate of 14.0%, compared with 5.5-6.7% for the evaluated full-size open models and 2.4-3.7% for Flash models. Case comparisons connect stronger outcomes to changes in problem representation, general arguments that extend beyond finite evidence, and proofs of the steps needed to complete a solution. By grounding evaluation in questions arising from the research literature, OpenProblemBench provides a setting for investigating the capabilities and limitations of AI as a contributor to foundational theoretical science.

---


### 65. [When Interfaces Speak: Data-Aware Generative UI Harness for Active Interaction](https://arxiv.org/abs/2610.11123)

**<font color=#1a73e8>作者：</font>** Xiaolong Li, Xiaohan Xu, Jinyang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most human-agent interaction today remains text-based. Natural language can impose cognitive overload, ambiguity, information chaos, and slow input for complex tasks; ephemeral generative UIs can present structured information and guide users toward task completion. We propose GenUI-Harness, a multi-agent harness pairing a Tool Agent for information retrieval and task execution with a GUI Coder Agent that identifies ambiguities and generates front-end code for structured interfaces. Training the coder with reinforcement learning is challenging: verifiable rewards for interactive UI generation require costly execution, while LLM-as-a-Judge rewards are prone to reward hacking. We address the first challenge with Dynamic UX, a lightweight package for dynamic interaction and reward collection in a single sandbox, and the second with Reward Auditor, a meta-reward mechanism that monitors reward distributions and distills diagnostic patterns into a shared rubric and scoring specification. We introduce UI-TAU Bench, a benchmark for active human-agent interaction through generated UI code, built on 10 real-world domain databases constructed from public data sources and based on Tau-Bench tool-use settings, with Lite (300 tasks) and Full (1,000 tasks) splits. GenUI-Harness achieves an average Pass@3 gain of 4.48 percentage points over smolagents on Lite. Training with GenUI-Harness improves a 4B backbone from 9.33% to 58.00% Pass@3, outperforming larger frontier models such as Claude Opus 5 (46.67%). GenUI-Harness also remains robust on ambiguous and non-ambiguous queries. In a reviewer survey comparing communication channels, generated UIs reduce average dialogue rounds from 3.4 to 1.2. These results show that data-aware generative interfaces can support effective task completion and reduce dialogue rounds in evaluated database-backed workflows.

---


### 66. [Balancing Reference Guidance and Free Generation in Trajectory Rollouts for Reasoning RL](https://arxiv.org/abs/2610.11128)

**<font color=#1a73e8>作者：</font>** Hanyu Wang, Nakul Agarwal, Hossein Nourkhiz Mahjoub 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A verified reference solution provides a correct trajectory for training a reasoning model. Alternatively, a prefix of the reference can guide the model in generating a trajectory of its own. How much reference guidance should we provide? We study this question through prefix continuation, where the model continues from a reference prefix and keeps the resulting trajectory if it passes verification, falling back to the reference otherwise. Since both procedures produce correct trajectories, we compare their distributions with the ideal distribution, the model's own distribution conditioned on successful verification. For one continuation, we derive the KL divergence in closed form, which, up to a bounded term, decreases with the product of the probability of generating a different correct trajectory and the reference surprisal, the negative log probability of the reference suffix given the prefix. Since a longer prefix tends to raise the former but lowers the latter, continuation success alone does not determine the preferred amount of guidance. From this analysis, we learn a prefix selector shared across training questions from continuation outcomes, without estimating success probabilities or additional generation. The resulting Adaptive Reference Guidance (ARG) constructs correct trajectories within a fixed generation budget, and we apply it to all-failure groups in Group Relative Policy Optimization (GRPO). Experiments on Qwen3-4B and Qwen3-8B across five mathematical reasoning benchmarks show that ARG achieves the highest aggregate pass@12 among the evaluated methods with competitive average sampled accuracy.

---


### 67. [SFT-as-Context Mitigates Forgetting in Supervised Fine-Tuning](https://arxiv.org/abs/2610.11132)

**<font color=#1a73e8>作者：</font>** Kenan Tang, Andong Hua, Chengxuan Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) equips large language models (LLMs) with specialized capabilities, but often comes at the cost of forgetting the general capabilities of their parent models (i.e., the pretrained models before fine-tuning). This trade-off is especially limiting for queries that require both specialized and general capabilities. We introduce SFT-as-context, a training-free method in which the parent model uses the SFT model's response as context to answer the query. This allows the parent model to acquire fine-tuned capabilities from the SFT response through in-context learning while preserving its own general capabilities. Across 19 parent-SFT model pairs and 11 benchmarks, SFT-as-context remains close to the SFT models on fine-tuned capabilities, with gaps of only 2.2 and 2.1 percentage points on AIME 2024 and LiveCodeBench and 2.0 macro MAE on NutriBench-English, while staying within 2.2 percentage points of the parent models on general capabilities on average. Remarkably, it can solve queries requiring both fine-tuned and general capabilities, even when neither the parent nor SFT model succeeds alone. This approach also extends beyond parent-SFT pairs: responses from a small open-source SFT model can improve a strong closed-source LLM, outperforming either model alone. Furthermore, we use a Bayesian framework to derive theoretical guarantees that bound the error of SFT-as-context relative to the SFT model on fine-tuned capabilities and to the parent model on general capabilities. In addition, we visualize the attention weights and find that the parent model attends more to useful SFT responses and less to irrelevant ones, suggesting that selective attention helps the parent model use the SFT response through in-context learning.

---


### 68. [QUILT: Rethinking Sparse-Attention Prefill through Shared Query Execution](https://arxiv.org/abs/2610.11134)

**<font color=#1a73e8>作者：</font>** Zhenduo Zhao, Qihui Zhou, Mingcong Song 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse attention reduces the cost of long-context attention, but existing kernels typically process queries independently, repeatedly loading and dequantizing KV entries shared across queries. We observe substantial overlap in the KV entries selected by neighboring queries, creating opportunities for cross-query reuse. We present QUILT, a workload-aware sparse-attention execution mechanism that jointly processes neighboring queries and reuses shared KV entries to reduce redundant memory traffic and computation. QUILT introduces Shift-and-Compare Set Decomposition (SCSD), which transforms irregular set operations into regular data-parallel primitives suitable for modern accelerators, and pipelines SCSD with attention computation to hide its overhead. Cascaded sharing captures reuse hierarchically at multiple granularities. A tile-aware execution strategy balances sharing granularity with hardware tile utilization and selectively removes low-importance query-specific tails to eliminate underutilized tiles. We evaluate QUILT on LongBench using GLM-5.3 and DeepSeek-3.2 under both tensor and sequence parallelism. Compared with the state-of-the-art sparse-attention kernel, QUILT reduces average kernel latency by up to 55.1% and processed KV data by up to 55.9%, while reducing time-to-first-token (TTFT) latency by up to 36.8% with negligible accuracy degradation.

---


### 69. [Can a System-One LLM Perform Knowledge Tracing When Few or No Learners Are Logged?](https://arxiv.org/abs/2610.11135)

**<font color=#1a73e8>作者：</font>** Unggi Lee, Haeun Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge tracing (KT) models need many logged learners, so a new course or platform starts without a usable model. In LLM-based KT the LLM generates the answer, which we call System-Two; it is either fine-tuned on the target data or reasons and votes over ten samples, which is slow and gives coarse probabilities. We ask whether an off-the-shelf System-One LLM, which returns a probability for a typed question directly in a single pass, can perform KT when few or no learners are logged. On seven datasets, Jev without any data from the target platform reaches a mean AUC of .706, above the best of 28 deep KT models trained on 8 learners (.689) and above System-Two Thinking-KT on all seven datasets (.650) at about 1/100 of its API cost. Adding examples and a similar-learner statistic from the logged learners (JevKT) raises this to .722; JevKT stays significantly ahead of deep KT up to 16 learners and ahead on average up to 64, and supervised KT catches up between 64 and 128 learners. Among the readers we tested, the gain is specific to Jev, since three other LLMs queried with the byte-identical typed request through the official System-One adapter fall below it on all seven datasets, and reader swaps and contamination checks find no evidence that the input format or memorised data explain the gain. For new learners the advantage holds from their first interactions, whereas on unseen items with all learners logged, deep KT remains ahead.

---


### 70. [The "10th Juror": Open-Set Standpoint Screening for Bureaucratic Bias Detection](https://arxiv.org/abs/2610.11136)

**<font color=#1a73e8>作者：</font>** Yuchen Miao, Zijun Wang, Chang Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Presupposing the boundaries of bias is itself a form of bias. We study closed-loop bias governance for Dutch government documents, where a system must detect biased language, ground decisions in legal and contextual evidence, rewrite problematic sentences when intervention is warranted, and verify that the rewrite mitigates harm without distorting meaning. Existing methods face three challenges: (i) discriminative classifiers capture surface regularities but lack normative grounding; (ii) zero-shot LLMs often adopt generic viewpoints and over-flag ambiguous administrative language; and (iii) fixed taxonomies inherit the Closed-World Assumption, missing emerging local targets. We propose MARS-Gov, a standpoint-aware multi-agent framework that combines legal retrieval, open-set target screening, specialized jurors, conservative routing, and rewrite verification. When screening finds an uncovered group, MARS-Gov instantiates a dynamic "10th juror" to deliberate outside the fixed panel. On DGDB, MARS-Gov sets a new SOTA with 0.880 F1, outperforming the strongest zero-shot LLM detector by 20.2 points (29.8% relative) and the best supervised Dutch encoder by 6.8 points, while reducing unnecessary interventions to 2.5%. Leave-One-Category-Out (LOCO) evaluation recovers held-out categories with 85.1% Correct@1 and 93.8% Correct@3.

---


### 71. [ActiveMedAgent: Cost-Aware Trajectory Learning for Multimodal Medical Diagnosis](https://arxiv.org/abs/2610.11140)

**<font color=#1a73e8>作者：</font>** Weiwei Ma, Xiaobing Yu, Peijie Qiu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical diagnosis is inherently sequential: clinicians escalate from cheap to costly tests only when additional evidence is expected to resolve diagnostic uncertainty. We present ActiveMedAgent, a framework that brings this cost-aware sequential logic to multimodal medical AI. Given a frozen, API-accessed vision-language model, ActiveMedAgent tracks probability distributions over candidate diagnoses and scores each acquisition by its per-step diagnostic utility minus cost. A lightweight MLP controller is then trained offline on these scored trajectories, learning when to request additional evidence and when to commit. Across three commonly used benchmarks, trajectory-based policy learning consistently outperforms both unguided acquisition and full-modality baselines. Notably, we identify an information overload effect. In 175 cases, the agent produces a correct diagnosis with fewer channels while the full-modality baseline fails, showing that learning what to omit can be as important as learning what to acquire.

---


### 72. [Improving Image-Based Nutrition Estimation Through Multimodal Food-Item Verification and Recovery](https://arxiv.org/abs/2610.11144)

**<font color=#1a73e8>作者：</font>** Jingbo Yue, Bruce Coburn, Jinge Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image nutrition estimation can fail silently when visible foods are missed. Even when a food is correctly identified, its proposed region may not support portion estimation. We propose a framework that uses multimodal large language models (MLLMs) to inventory visible foods and separately verify food identity and whether each proposed 2D region supports portion estimation. One whole-image review uses these verification results to identify unresolved gaps and omitted foods, triggering at most one targeted recovery pass. Recovered regions are re-verified without access to the recovery prompt, then reconciled into a final item set for nutrition estimation. The framework requires no task-specific fine-tuning. Matched evaluation on common valid-output samples shows that item-level grounding improves mass accuracy across all tested settings and energy accuracy relative to an adapted retrieval baseline, with item-identity precision and recall also improving, while post-recovery visual coverage is assessed separately at inference time without ground-truth annotations.

---


### 73. [Ranking Prior Alignment for Credit Risk Modeling: When Do External Priors Matter?](https://arxiv.org/abs/2610.11146)

**<font color=#1a73e8>作者：</font>** Qiye Lu, Jiang Ji, Liang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cold-start credit scoring -- deploying models with scarce labeled data, weak features, or minimal capacity -- is a recurring problem in financial machine learning. When a new lending product launches, labeled default data is scarce, feature pipelines are immature, and models must be deployed with minimal capacity to avoid overfitting. Standard defenses operate on the same limited data; what is needed is a source of external regularization grounded in domain knowledge.
We propose Ranking Prior Alignment, a model-agnostic framework that distills external ranking priors (from domain experts, teacher models, or LLMs) into any scoring model via a temperature-scaled KL divergence loss. The framework unifies neural (MIL attention) and tree-based (XGBoost custom objective) architectures through a single formulation: L = L_task + gamma(t) * KL(P_agent || P_model), where gamma(t) follows an exponential decay schedule. The method requires no external model at inference, and its tree-based instantiation tolerates annotation noise up to eta = 0.5.
On an industrial dataset of over 1.5M merchants, MIL alignment achieves 7/7 positive evaluation cells at 3K bags (1 ID + 3 OOT + 3 degradation metrics; peak Delta AUC = +0.020 on OOT-1), and XGBoost ablation achieves 9/9 positive metrics at 300 bags. Cross-dataset validation on public Amex shows 5/5 positive folds (avg Delta AUC = +0.041). Four model families (MIL, XGBoost, LightGBM, Logistic Regression) and four teacher architectures show that the framework is both model-agnostic and prior-source-independent.
We further observe that alignment gains exhibit an inverse-scaling pattern: benefits grow as data abundance N, model capacity C, and feature quality Q decrease, helping practitioners decide when to invest in prior annotation.

---


### 74. [SP-DocReader: Difference-Aware Self-Play for Precise Document OCR](https://arxiv.org/abs/2610.11148)

**<font color=#1a73e8>作者：</font>** Wenjie Liao, Xiaohui Song, Liangjie Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate page transcription remains difficult for vision language models under limited input and training budgets. We present SP-DocReader, a self-play framework for optical character recognition (OCR) that targets residual errors after supervised fine-tuning. Reading Discrepancy Masking aligns reference and generated model tokens through a longest common subsequence, then scores unmatched positions with their full conditioning prefixes. Focused Fidelity Loss adds direct negative log-likelihood supervision at unmatched ground-truth positions. Only the OCR module is trained, while the backbone remains frozen. We derive the combined gradient to distinguish relative score optimization from direct supervision. Compared with SFT-2, SP-DR-3 reduces Vary-600K character error rate on both backbones. On Qwen3-VL-4B, it reduces character error rate by approximately 54 percent and improves DocVQA Average Normalized Levenshtein Similarity (ANLS) by 3.7 points. These results show the value of focusing self-play training on the discrepancies that remain after supervised fine-tuning.

---


### 75. [Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context Reinforcement Learning](https://arxiv.org/abs/2610.11152)

**<font color=#1a73e8>作者：</font>** Minchan Kwon, Seunghee Koh, Sunghyun Baek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly improve at inference time by accumulating experience in context rather than by updating parameters. This process is often described as in-context reinforcement learning (ICRL). Whether in-context learning (ICL) can actually play the role of RL, however, has not been tested. We study this question in its simplest form, direct ICRL, where the model conditions directly on raw trajectory-reward pairs, and ask whether the reward acts as a learning signal. Through controlled experiments on four benchmarks across six models, we find that the reward is read, but its effect is small: flipping, randomizing, or removing the reward leaves the improvement curve almost unchanged, and this holds even under meta-prompts that explicitly instruct the model to explore, exploit, or reason over rewards. Trajectories drive improvement, but not through their semantic content: shuffled or corrupted trajectories work as well as real ones. These patterns closely mirror those known in ICL, suggesting that direct ICRL is better understood as a special case of ICL than as inference-time RL. This reframing has implications for agent memory design: ICL factors such as input distribution and demonstrations may matter more than RL elements such as reward shaping and exploration.

---


### 76. [Local Prototype Reconstruction for Text-Compatible Speech-to-LLM Bridge Pretraining](https://arxiv.org/abs/2610.11159)

**<font color=#1a73e8>作者：</font>** Xinnian Zhao, Chia-Hua Wu, Pu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-to-LLM systems often connect a frozen speech encoder to a frozen large language model (LLM) through a small trainable bridge. The bridge is usually treated as plumbing, but it in fact defines the geometry of the speech-to-LLM interface, and the pretraining objective decides whether that interface provides a reusable initialization for downstream tasks. We study a transferable bridge through two complementary properties: global alignment with the text side, and local lexical manifold compatibility, where bridge embeddings remain close to the frozen LLM's input-embedding neighbourhoods. We make this property measurable with a fixed, head-free, timestamp-free diagnostic that applies to any objective, and show that next-word prediction (NWP) and sentence-level contrastive pretraining do not fully capture token-level lexical compatibility. We then introduce Local Prototype Reconstruction (LPR), a lightweight training-only regularizer that requires each aligned bridge token to be reconstructable from a small neighbourhood of frozen LLM token embeddings, with a hard single-prototype anchor as its limiting case. On multilingual ASR and speech translation, LPR improves transfer, with the largest gains on translation and low-resource adaptation. Crucially, our independent diagnostic correlates with downstream gains across objectives, suggesting that lexical manifold compatibility is predictive of reusability for speech-to-LLM bridges.

---


### 77. [LadderEdit: Edit-Level Residual Compression for Memory-Efficient Lifelong Editing of LLMs](https://arxiv.org/abs/2610.11160)

**<font color=#1a73e8>作者：</font>** Xiaobing Yu, Peijie Qiu, Jin Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lifelong editing of LLMs requires storing thousands of edits after acquisition. A widely used family of approaches attaches one LoRA adapter per edit, which preserves behavior but grows linearly in storage. To address this challenge, we propose LadderEdit, a method that compresses each LoRA adapter after it is acquired. Each edit is first stored at low rank as a cheap sketch. We then check whether this sketch still satisfies the rewrite, generalization, and locality contract on probe prompts. Edits that pass keep the sketch; those that fail are promoted to a higher rank along a ladder until the contract is met. Because every edit retains some representation, coverage is maintained, and only hard edits consume more rank. Across ZsRE, CounterFact, and WikiBigEdit benchmarks on LLaMA-3-8B, Mistral-7B, and Qwen2.5-7B, LadderEdit tracks exact LoRA storage at 5.2x less memory and remains effective at 50,000 sequential edits.

---


### 78. [VGGTWorld-VLA: Intent-Conditioned 3D World Evolution for Autonomous Driving](https://arxiv.org/abs/2610.11161)

**<font color=#1a73e8>作者：</font>** Zhaoyang Liu, Kun Jiang, Ziying Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> VGGT provides a strong foundation for geometry-centric world models by recovering unified 3D scene geometry from visual observations. Although recent extensions enable temporal 3D prediction, their future evolution remains weakly conditioned on driving intentions and actions, limiting their ability to model alternative action-dependent futures. We propose VGGTWorld-VLA, an intention-conditioned extension of VGGT-World for controllable 3D world evolution in autonomous driving. First, we introduce an action--semantic conditioning mechanism that injects complementary driving semantics and ego-motion representations into the future-token stream, enabling different future geometry predictions for the same observed scene under alternative ego actions. Second, we develop a geometry--language--action bridge that adapts historical geometry, VLA semantic features, and maneuver and trajectory representations for joint conditioning of future geometry prediction. We evaluate future geometry prediction on NAVSIM, while conditioning ablations further examine the contributions of semantic and action information. Compared with the baseline, our method demonstrates competitive geometry prediction performance. Ablation studies further support the effectiveness of semantic and action conditioning. These results demonstrate the potential of semantic and action conditioning for controllable VGGT-based world prediction in autonomous driving.

---


### 79. [Characterizing Statistical Separability in TP-CRIV for Probabilistic AI Models](https://arxiv.org/abs/2610.11163)

**<font color=#1a73e8>作者：</font>** Teruki Sano, Minoru Kuribayashi, Masao Sakai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party challenge-response identity verification (TP-CRIV) enables an independent verifier to assess whether a claimant possesses a model identical to a remotely deployed model without directly accessing the reference model. However, for probabilistic AI models, repeated executions of the same query may produce different outputs and therefore different verification observations. This raises the question of how such stochastic evidence should be accumulated and how much evidence is required for reliable verification.
In this work, we characterize statistical separability in TP-CRIV of probabilistic AI models. Specifically, we relate challenge-wise behavior of matching and non-matching provers to verification-level separability. The characterization explicitly describes how the numbers of independent challenges and repeated responses affect detection performance and enables the verification budget required for a target AUC to be estimated. We instantiate the proposed characterization for LLMs using open-ended challenges. The experiments demonstrate matching-non-matching separation, close agreement between theoretical and empirical AUCs, and consistent estimates of the minimum verification budgets. These results provide a statistical basis for relating probabilistic model behavior to verification-level separability and the evidence required for third-party verification.

---


### 80. [PIVOT: Perplexity-Informed KD-to-RL Transition Scheduling for Vertical-Domain Few-Shot Distillation](https://arxiv.org/abs/2610.11167)

**<font color=#1a73e8>作者：</font>** Heng Li, Yong Zhang, Ning Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vertical-domain few-shot classification remains challenging for small language models, as limited supervision makes it difficult to acquire domain-specific decision knowledge. On-Policy Distillation (OPD) can improve teacher-guided adaptation by supervising student-generated rollouts, while GRPO-based reinforcement learning can further refine downstream predictions. However, existing KD-to-RL pipelines typically rely on globally fixed transition schedules, ignoring that different samples may require different amounts of teacher-guided acquisition before reward-driven refinement. We propose PIVOT (Perplexity-Informed Transition Optimization), a dynamic transition framework that routes samples between OPD and GRPO according to teacher-evaluated sequence perplexity. PIVOT moves low-perplexity samples to GRPO for reward-driven refinement while keeping high-perplexity samples under OPD for continued domain knowledge acquisition. Experiments on Banking77 and HWU64 show that PIVOT consistently outperforms continued OPD and globally synchronized OPD$\rightarrow$GRPO baselines under the same number of post-warm-up student optimization steps, achieving stronger downstream performance and more stable training dynamics.

---


### 81. [RAG-Stress: Probing the Limits of Evidence Reliance in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.11183)

**<font color=#1a73e8>作者：</font>** Shunyuan Zhou, Hao Chen, Tianyu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Following retrieved evidence does not guarantee factual correctness: misleading evidence can induce a model to replace an answer it previously gave correctly. Standard accuracy measures obscure this behavior by combining answer replacement with preexisting errors. We introduce RAG-Stress, a controlled diagnostic protocol for examining the limits of evidence reliance in retrieval-augmented generation. The protocol holds the question and reference answer fixed, edits one assertion to support a designated incorrect answer, and crosses two source priority policies with three positions of the answer span within the evidence text. We measure misleading rate (MR) on each model's subset of questions answered correctly without retrieval, alongside clean accuracy on the full evaluation set. We evaluate fifteen systems spanning API models, open models, and search agents trained with reinforcement learning on TriviaQA-RC, HotpotQA, and SearchQA, with additional English and Chinese MedQA evaluations. Instructions that prioritize documents consistently produce higher MR than those permitting reliance on prior knowledge. Averaged over models and positions, the gap ranges from 10.9 to 13.5 percentage points across the three QA datasets. Mean MR follows End $>$ Beginning $>$ Middle under both policies, although individual models do not uniformly follow this ordering. A separate paired audit of 500 questions and two checkpoints supports increased harmful override without establishing a corresponding improvement in beneficial correction. These findings distinguish evidence adherence from factual reliability and motivate evaluating whether retrieved evidence preserves, replaces, or corrects a model's answers.

---


### 82. [What to Admit and How to Present: Governing Persistent Memory in LLM Agents](https://arxiv.org/abs/2610.11188)

**<font color=#1a73e8>作者：</font>** Chang Liu, Deliang Ding  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent memory can improve personalization in LLM agents but can also induce sycophancy and cross-domain leakage. We distinguish two governance decisions: admission, which determines what recalled information enters the working context, and presentation, which determines how admitted information is expressed. We implement two inference-time designs without retraining: factor-compiled admission (FC), which assesses whole memory entries, and permission-semantic admission (PS), which decomposes entries into typed units; both translate adjudicated attributes into eligibility decisions via deterministic policies. We evaluate on a four-backbone development suite and an external benchmark with four tasks of 300 samples each. Relative to verbatim injection, FC and PS reduce pooled judge-assessed failure rates on the external benchmark by 6.7 and 8.8 percentage points (p = 2.7e-7 and 4.1e-12), and development-set cross-domain leakage falls by up to 29.5 percentage points. A query-conditioned gating baseline shows no significant change in objective-fact failure or pooled failure. Under matched admission budgets, PS outperforms random and relevance-based selection on external objective-fact judgment after Holm correction. Holding presentation fixed, tightening admission cuts cross-domain failure by a further 17.5 percentage points (p = 1.6e-4); in contrast, no comparison between two renderings of identical adjudicated outputs survives multiple-comparison correction. Both designs increase personalization failures, and PS misses the preregistered improvement and personalization-preservation criteria. These results support evaluating admission and presentation separately: selection quality provides task-specific safety gains, while preserving beneficial memory use remains unresolved.

---


### 83. [Bridging KV-Cache Quantization and Linear Attention: From Theory to Pretrained Weight Migration](https://arxiv.org/abs/2610.11214)

**<font color=#1a73e8>作者：</font>** Kaicheng Xiao, Liran Dong, Haotian Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV-cache quantization and linear attention are two representative approaches to tackling the storage and computational costs of Transformers. KV-cache quantization compresses individual KV entries into discrete codes but retains all entries, whereas linear attention recurrently aggregates multiple historical KV contributions into a fixed-size continuous state but can introduce interference. This contrast raises the question of whether per-KV compression and multi-KV aggregation can be bridged within a single mechanism for efficient attention. We identify RAM-Net as such a bridge through soft assignments over a discrete address space. These assignments determine recurrent updates to the continuous slot state associated with each address. Under a restricted RAM-Net construction, we prove that soft address assignments extend hard quantized matching to a separable read-write overlap that locally approximates full-attention similarity and supports recurrent aggregation. These connections further enable Transformer-to-RAM-Net weight migration through a new path based on a soft-quantized intermediate construction. Across nine pretrained Transformer models from 0.3B to 7B parameters, RAM-Net recovers an average of 87.1% of the teachers' accuracy gains over random guessing across six commonsense and knowledge tasks using only a 500M-token budget per model.

---


### 84. [When Lower Reconstruction Loss Hurts: Distributionally Robust Refinement for Low-Bit LLM Quantization](https://arxiv.org/abs/2610.11226)

**<font color=#1a73e8>作者：</font>** Yanlong Zhao, Xiaoyuan Cheng, Huihang Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Weight-only post-training quantization (PTQ) relies heavily on reconstruction loss minimization to preserve model quality at low precision. We show that the weights favored by minimizing this loss need not yield better model performance on new tasks. In fact, we find that lower reconstruction loss can even degrade model performance on the same calibration data. Our analysis further shows that weights with lower reconstruction loss on calibration data can have higher loss than other weights when the distribution of input activations changes. Motivated by these observations and our analysis, we propose Distributionally Robust Quantization (DRQ), a post-hoc refinement process that minimizes worst-case reconstruction loss over a constrained set of input activation distributions. DRQ refines the integer codes representing quantized weights within the existing quantization grid, keeping quantization parameters and inference operators unchanged. Extensive experiments show that DRQ improves models quantized by six representative PTQ methods, including AWQ, GPTQ, and ParoQuant, and delivers gains across both dense and mixture-of-experts large language models. These results establish DRQ as a general post-hoc refinement framework for weight-only PTQ, achieving better downstream performance without adding inference overhead.

---


### 85. [Multimodal Graph Retrieval-Augmented Sequential Recommendation via Collaborative Filtering Paths](https://arxiv.org/abs/2610.11228)

**<font color=#1a73e8>作者：</font>** Jason Marcell Setiadi, Xin Cao, Lina Yao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated strong potential for sequential recommendation through their ability to reason over complex multimodal data. However, existing approaches either rely solely on the target user's own interaction history, neglecting collaborative signals from neighboring users, or incur substantial computational overhead through repeated MLLM inference over long interaction histories. To address these challenges, we propose MGRASRec, a multimodal graph retrieval-augmented framework for sequential recommendation. MGRASRec injects collaborative filtering signals conditioned on the candidate item directly into the MLLM prompt by retrieving structured paths from a user-item interaction graph, extended via multimodal similarity to increase coverage beyond exact co-interaction overlap. This retrieval also surfaces the history items most relevant to the candidate at no additional cost, removing the need for recurrent summarization and keeping inference to a single forward pass per candidate. All components are unified into an augmented prompt for parameter-efficient fine-tuning of an MLLM. Extensive evaluations across three publicly available datasets validate the effectiveness of MGRASRec, achieving the best performance on all metrics with particularly strong gains in ranking quality.

---


### 86. [Harness Compilation: Which Decisions Should a Small Vision-Language Model Keep?](https://arxiv.org/abs/2610.11231)

**<font color=#1a73e8>作者：</font>** Minhao Fan, Yinyi Liu, Jiayu Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small vision-language models may be able to read external evidence yet struggle to obtain it. We introduce Harness Compilation (HC), an offline procedure that adapts the division of work between a frozen small VLM and its external harness. A large teacher uses student execution traces to revise reusable content and control, while a separate validation set selects the deployed harness. Deployment requires neither weight updates nor teacher calls. Across seven visual question-answering settings with students of at most 9B parameters, HC improves scores over bare students by 9.9-23.9 points, averaged over three independent builds per setting. Interventions on five runtime decision types (invocation, selection, argument generation, evidence integration and abstention) show why this allocation matters: requesting evidence and generating open queries can be costly, whereas bounded choices and reading supplied text can remain useful student work. Fact cards benefit all ten evaluated students, but decision policies transfer unevenly. Recompilation for a new student model helps when the transferred interface no longer fits the student. With 100 practice items, HC exceeds answer-only LoRA on three tasks. Larger training budgets can match or surpass a fixed harness, while combining the two improves SlideVQA beyond either alone. These findings support allocating work from measured student behavior rather than uniformly removing decisions.

---


### 87. [MiniVer-V: Identifying Minimal Sufficient Evidence for Short Video Verification](https://arxiv.org/abs/2610.11233)

**<font color=#1a73e8>作者：</font>** Leran Chen, Lingnan Kong, Zile Cai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A core challenge in short-video fact-checking is identifying which evidence is sufficient to support a verification conclusion. Existing approaches either give the verifier all available evidence, introducing noise, or select evidence by topical relevance, which conflates relatedness with sufficiency. We identify evidential sufficiency as the selection criterion: whether a subset of evidence is adequate to support a confident verdict without redundancy. We introduce MiniVer-V, a benchmark of 195 short videos with three-way verdict annotations (supported, refuted, insufficient) and 5,510 multimodal evidence units spanning visual keyframes, speech transcripts, and web-retrieved external sources. We propose a two-layer verification framework that separates claim-video consistency, assessed from internal evidence, from factual verdict determination, which additionally requires external corroboration. On top of it, a sufficiency-driven greedy search assembles evidence until a sufficiency threshold is met and outputs insufficient when the candidate pool is exhausted, rather than forcing a verdict. With Claude Sonnet 4, the method reaches a Macro-F1 of 0.510 using 4.5 evidence units on average (16% of the full evidence set), statistically indistinguishable from the full-evidence baseline (0.518 with 27.7 units), while significantly improving recognition of insufficient cases over the same search without abstention. The efficiency result replicates with GPT-5.5 and holds only partially with an open-weight Qwen2.5-72B verifier. Ablations show that external evidence is indispensable for factual determination, while internal video evidence grounds the verdict in claim-video consistency. These findings suggest that evidence-efficient verification is achievable, and that explicit abstention is needed when evidence is genuinely inadequate.

---


### 88. [Read What Matters: Query-Adaptive Quantization for KV Caches](https://arxiv.org/abs/2610.11245)

**<font color=#1a73e8>作者：</font>** Siddharth Bhandari, Lucas Gretta, Krishna Balasubramanian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV-cache entries are stored before their future queries are known, but each decoding query needs precision in different places. We study this mismatch using separate budgets for retained bits and bits fetched per query. ReadKV stores each key and value in a progressive code whose prefixes support different reconstruction precisions. For each query, it allocates key-channel prefixes using the query, computes attention from the reconstructed keys, and then allocates value-token prefixes using that attention. Stored entries remain unchanged. Each stage optimizes a calibrated distortion objective under a fixed budget; we prove exact allocation under diminishing refinement gains and relate these objectives to attention-output error. We also exhibit a finite-dimensional attention family where query-dependent access strictly outperforms every query-independent reader at the same read budget, even with unrestricted competing encoders and decoders.
Across six base models, reading four bits on average from an eight-bit cache increases C4 perplexity by at most 0.66%, using about one quarter of the logical reads and half the retained capacity of a 16-bit cache. It is consistently more accurate than storing and fully reading four bits at the same payload-read budget. Retaining more bits than each query fetches is aimed at long-context decoding, where the cache bytes moved per step, rather than the weights, dominate cost. Long-context question answering and retrieval on two instruction-tuned models provide additional quality evidence. On the tested 8K-token, batch-one, single-layer workload on an NVIDIA A10G, a restricted eight-bit ReadKV reader with a two-bit mean payload-read budget has 39% lower latency than the tested TurboQuant codec.

---


### 89. [Why On-Policy Distillation Sometimes Fails: Vanishing Learning Signals](https://arxiv.org/abs/2610.11247)

**<font color=#1a73e8>作者：</font>** Lei Zhao, Qichao Zhao, Bowen Zuo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) enables effective capability transfer between language models, yet the mechanisms underlying its failures are not fully understood. Across code generation and mathematical reasoning, OPD with larger-scale teachers exhibits early loss plateaus, with an average final loss reduction of 25.1% after 200 updates, compared with 96.2% for self-RL teachers, obtained by further reinforcement learning (RL) training of the initial student. To understand this difference, we analyze OPD as an idealized continuous-time dynamical system in the small-learning-rate limit. Our training-log diagnostics associate these plateaus with an early decline in a gradient-based learning-signal proxy while substantial loss remains; these measurements do not establish why the underlying gradient weakens. We further prove a local recovery guarantee for teachers sufficiently close to the initial student in a shared parameterization under regularity conditions, offering a conditional explanation for the success of self-RL teachers in our experiments. Across runs with and without loss plateaus, we observe small relative parameter changes (0.025-0.098%) and high similarity between the student's representations before and after OPD (linear CKA $>0.98$ across layers). These observations suggest that limited representation adaptation may contribute to learning-signal collapse, a hypothesis that remains to be tested. Code is available at this https URL.

---


### 90. [V-CoLA: Vision Token Compression with Linear Attention](https://arxiv.org/abs/2610.11251)

**<font color=#1a73e8>作者：</font>** Hao Jiang, Yiru Mao, Tianpeng Bu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have demonstrated impressive capabilities but suffer from substantial computational overhead, as vision tokens dominate the input sequence. This motivates vision token compression as a key direction to alleviate the burden. However, with the emergence of hybrid architectures incorporating linear attention (\eg, Qwen3.5), prior methods designed for softmax attention struggle to generalize. Our analysis reveals that both attention- and similarity-based approaches suffer notable performance degradation, underscoring the urgent need for compression methods tailored to this regime. To this end, we propose \textbf{V-CoLA}, an efficient training-free token compression framework specifically designed for linear attention. V-CoLA introduces a novel \textit{uniqueness-aware importance criterion} for identifying critical vision tokens, coupled with an \textit{adaptive token merging strategy} that performs compression. All components are optimized at the implementation level to remain compatible with the chunk-wise parallelism of linear attention, ensuring strong practical value. Extensive experiments across multiple benchmarks demonstrate the superiority of V-CoLA: it achieves 99.5\% of the original performance with only 50.0\% of vision tokens, and over 88.0\% with as few as 12.5\%, while delivering a 1.86$\times$ to 6.15$\times$ prefill speedup.

---


### 91. [LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models](https://arxiv.org/abs/2610.11253)

**<font color=#1a73e8>作者：</font>** Surya Shetty, Ulisses Braga-Neto  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents are being increasingly deployed as autonomous scientists, designing experiments and inferring mechanistic world models with minimal human oversight. Yet identifiability is often overlooked: when a plateau is reached, the agent needs to know whether it is not yet capable enough or the model simply is not identifiable from the data, in which case no amount of further experimentation of the same kind can help. We propose the Identifiability-Driven Experimental Agent (LLM-IDEA) for closed-loop discovery with an identifiability engine that returns a three-way plateau verdict: capability limit, resolvable within the design class, or certified exhausted. On ODEBench, 60 of the 62 systems with free constants are identifiable at round 0; the RC circuit is certified exhausted for every experiment that protocol can run, and a harvesting model is resolvable by one added initial condition. The identifiability engine reproduces known verdicts on Lotka-Volterra, Van der Pol, Lorenz, and a pharmacokinetic model, where it recommends the intravenous arm pharmacologists use, and it ranks the depth scorer of our own benchmark last among four observation designs. On the DiscoverPhysics benchmark, it finds two public worlds whose explanation rubric rewards a distinction no legal experiment can make, and every model there with accurate trajectories failed the explanation grade (15 of 15, against 5 of 9 in identifiable worlds, p = 0.012). On the Alien Universe, a two-body testbed we propose in which a force law switches between a provably non-identifiable and an identifiable protocol, LLM-IDEA on the identifiable protocol reaches discovery depth at least three on 8/8 seeds versus 1/8 without it. An autonomous discovery agent can thus compute, rather than guess, whether a plateau calls for more search, a better experiment of the same kind, or a different kind of experiment.

---


### 92. [Gated Memory: Admission-Controlled Memory Formation for Conversational AI](https://arxiv.org/abs/2610.11270)

**<font color=#1a73e8>作者：</font>** Preeti Saraswat, Divya Neelagiri, Ajay Manoj  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized conversational AI relies on long-term memory systems that extract facts from user utterances and store them in persistent vector stores. Despite progress in retrieval, deduplication, and lifecycle management, the formation stage, the moment a fact is first written to storage has received almost no principled attention. We identify this as the binding constraint on memory quality in production systems. Critical contextual signals, such as the distinction between a permanent user attribute and a transient situation, exist only in the original utterance and are irreversibly lost the moment extraction produces a subject-relation-object triple. No downstream process can recover them. We propose Gated Memory, a lightweight, modular formation framework that interposes two decision checkpoints between conversation and storage: an admission gate that evaluates every candidate fact against the full utterance context before extraction runs, and a conditional enrichment stage that grounds admitted facts through an entity scope taxonomy with privacy constraints. The gate evaluates only the current exchange while using prior turns as read-only reference context, and produces a structured formation record. Admitted content is decomposed into atomic facts, each categorized, tagged with provenance (directly stated versus inferred), scoped to its condition of applicability, and grounded in resolved time and place, subject to a constraint that no entity absent from the context may be asserted. On the LoCoMo-10 benchmark with atypical emotional density in utterance data, Gated Memory achieves an overall +2.6% relative improvement in LLM-judge accuracy over a strong baseline with identical retrieval and generation, establishing formation quality as a measurable constraint on memory performance.

---


### 93. [How to post-train on a surrogate: Envelope sampling mitigates reward hacking](https://arxiv.org/abs/2610.11281)

**<font color=#1a73e8>作者：</font>** Sanjit Dandapanthula, Shuvom Sadhuka, Samir Khan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are commonly post-trained against LLM judges and other cheap surrogates because the true reward, such as human preference, is too expensive to query at scale. This practice often leads to reward hacking, where reinforcement learning against a miscalibrated surrogate leads to undesirable side effects. In this work, we study a setting in which a small number $n$ of model outputs are annotated with ground-truth labels (e.g., from expert review) and used to recalibrate the LLM judge before optimizing against it. Prior approaches to judge recalibration are costly or heuristic, and it is known that on-policy sampling fails when the surrogate is miscalibrated on a rare set of outputs. In this work, we propose envelope sampling, a theoretically-grounded method for judge recalibration that seeks to minimize an upper bound on the regret of the post-trained model under the assumption that the human reward and re-calibrated reward lie in an $L^2$ ball around the judge. We give practical algorithms to sample from the envelope by rejection or by fine-tuning against a modified reward, and experiments on clinical note generation and on a controlled sycophancy task show that recalibrating on envelope samples mitigates reward hacking where recalibrating on base-model samples does not.

---


### 94. [When Scene Text Hijacks the Scene: Uncovering, Exploiting, and Mitigating Rendered-Text Semantic Leakage in Image Generation Models](https://arxiv.org/abs/2610.11286)

**<font color=#1a73e8>作者：</font>** Feifei Li, Runjie Wang, Xiaohan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The reliability and accountability of image generative models (IGMs) are essential for building responsible and trustworthy AI systems. Recent IGMs, such as Nano Banana and GPT-Image, now support complex instruction following, realistic image synthesis, and controllable scene-text rendering. As these capabilities expand, safety analysis must also account for new control channels introduced by complex prompts. In this work, we study rendered-text semantic leakage, a largely overlooked phenomenon in open-domain text rendering. Although rendered text is intended to serve as a local visual constraint that should be reproduced verbatim in the generated image, it also carries linguistic semantics that may be interpreted by the model as part of the input instruction. This makes rendered text a potential semantic control channel whose safety implications remain insufficiently understood. We systematically characterize this phenomenon by decoupling the main visual prompt from the rendered text and measuring their individual and compositional effects on generated images. We quantify semantic leakage and rendering fidelity, and further analyze how leakage emerges from intermediate model evidence. We then show that harmful semantics embedded in scene text can persist through LLM-based prompt enhancement pipelines and steer non-text image regions, even when the main visual prompt remains benign. Finally, we propose a preliminary mitigation approach that reduces unsafe semantic transfer from rendered text to non-text regions while preserving the intended text-rendering behavior on FLUX-2-dev. Our findings reveal rendered text as a dual-use carrier of visible data and latent semantics, exposing a text-centric cross-modal attack surface in modern IGMs.

---


### 95. [REMORY: Learning Residual Memory for Context Compaction](https://arxiv.org/abs/2610.11287)

**<font color=#1a73e8>作者：</font>** Hanchen Xia, Baoyou Chen, Yutang Ge 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents compact their history to continue within a finite context window, but a textual summary alone may not support every subsequent decision. We introduce REMORY, a neural memory network that supplements the summary with a bounded sequence of soft memory tokens. Given the history and summary, the network learns to generate tokens that help a frozen LLM approximate the continuation it would produce with the full history. The tokens are conditioned on the summary and appended after it, forming an analogue of a residual connection along the sequence dimension. On SummHay, REMORY improves source attribution at nearly unchanged insight coverage and approaches the full-context joint score using only 5.2% of the input positions. Across long-horizon agent benchmarks, Qwen3.8-27B and GLM-5.3-Flash show consistent gains with residual memory. Both models also exhibit substantially fewer repeated tool outputs and tool errors on BrowseComp and Terminal-Bench 2.1.

---


### 96. [Open-ended Scientific Discovery with Possibilistic Reasoning](https://arxiv.org/abs/2610.11289)

**<font color=#1a73e8>作者：</font>** Anita Yang, Siu Lun Chau, Tomoya Wakayama 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous scientific discovery with LLMs requires generating and testing hypotheses adaptively as evidence accumulates while maintaining statistical validity. Existing anytime-valid methods can handle data-dependent hypotheses, but open-ended discovery poses a deeper challenge: the best discovered hypothesis may still be the best of a bad lot, with better explanations yet undiscovered, while even background knowledge such as physical laws may require revision in light of new findings. In response, we formalize the problem as Abductive Autonomous Scientific Discovery (AASD) using possibility theory. We introduce abductive utility, a computable measure of discovery progress, and possibility frontier search, the first algorithm for AASD, which maintains anytime validity and achieves $\varepsilon$-optimal abductive utility asymptotically under suitable conditions. Experiments on synthetic and real-world scientific-discovery tasks show strong performance.

---


### 97. [When Do We Need On-Policy Distillation? Distilling on Offline Student Rollouts Is Often Better](https://arxiv.org/abs/2610.11291)

**<font color=#1a73e8>作者：</font>** Siyan Zhao, Yonggan Fu, Jindong Jiang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has become increasingly popular for transferring teacher capabilities to student models. In this work, we ask a critical research question: Is on-policy sampling always beneficial for distilling arbitrary teacher-student pairs? We show that a simple alternative, Semi-OPD, which distills from offline rollouts generated by the initial student, can often outperform OPD in both accuracy and training efficiency. Across 17 teacher-student pairs ranging from 1.5B to 235B parameters, Semi-OPD outperforms OPD in 14 cases, with up to +13.6% accuracy and 11.4x training speedup. We further find that the choice between OPD and Semi-OPD depends on the alignment between the initial teacher and student, quantified by an output-token overlap ratio: OPD is beneficial only when the two are highly aligned with high overlap ratios. Our deeper investigation suggests that effective distillation requires on-policyness w.r.t. both the student and the teacher. For misaligned pairs, student rollouts can become increasingly off-policy w.r.t. the teacher as context length grows, weakening the distillation signal. In contrast, Semi-OPD is often more stable, as it distills on shorter contexts while covering full trajectories and exposing the student to more teacher-preferred tokens. Beyond proposing Semi-OPD as an efficient alternative, our work motivates the community to rethink when to use OPD and to study stronger OPD variants with meaningful teacher-student pairs.

---


### 98. [DuplexAgent-RSI: Recursive Harness Improvement for Full-Duplex Voice Agent Collaboration](https://arxiv.org/abs/2610.11299)

**<font color=#1a73e8>作者：</font>** Yingda Shen, Yuxiang Wang, Kunyu Feng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Voice agents are converging on a collaboration pattern: a full-duplex interaction model stays on the live channel as the entry to the conversation, while search, reasoning, and coding are handled through asynchronous delegation. A duplex model supports continuous listening and speaking, but complex reasoning and tool use may exceed its capabilities. A coding agent can plan and execute extended tasks, but its sequential interface is a poor fit for live conversation. Combining them requires a harness that coordinates task acceptance, progress, cancellation, replacement, and result delivery while keeping the conversation responsive. Existing harnesses often rely on coupled heuristics, making them difficult to improve systematically from evidence. We present DuplexAgent, a full-duplex collaboration system whose harness expresses this workflow as six editable modules, and Duplex-Harness-RSI, a closed loop that revises them from interaction traces. A simulator automatically generates timed test conversations, runs the system, and produces failure traces that identify the collaboration modules requiring repair. Reasoning LLMs and coding agents in the delegation pool also serve the improvement loop: the Exam Planner selects the next tests from observed weaknesses and the repair archive, and the Harness Editor proposes targeted module changes. The capabilities that serve the user thus also improve the system's coordination. Experiments on intelligence, agentic, and duplex benchmarks show that DuplexAgent combines continuous interaction with difficult reasoning and complex task execution, achieving stronger spoken-knowledge and executable-tool scores than the compared delegated systems while maintaining strong interruption response. A harness ablation further shows that this modular, verifiable loop outperforms the initial harness and repeated editing that lacks its diagnosis and repair archive.

---


### 99. [Efficient Multi-Granularity Knowledge Transfer for Radiology Report Generation](https://arxiv.org/abs/2610.11303)

**<font color=#1a73e8>作者：</font>** Xubin Zhong, Zheyu Zhang, Wenjian Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology report generation can automatically generate clinical descriptions from X-ray images, thereby significantly improving the efficiency of radiologists. This task is challenging because it requires medical knowledge to accurately identify diseases and describe them in a professional manner. However, existing methods often overlook the importance of enhancing medical knowledge in describing pivotal areas, a capability that requires models to effectively extract and aggregate knowledge at multiple levels of granularity. Accordingly, we herein propose a novel and compact Efficient Multi-Granularity Knowledge Transfer (\textbf{EMGKT}) method to address the above issues. First, we encode global knowledge embeddings using a medical vision-language model, which provides contextual medical knowledge. Moreover, we devise a novel Fine-Grained Knowledge Distillation (FGKD) training task which efficiently extract fine-grained knowledge. Specifically, the FGKD training task contains teacher embeddings and student embeddings. Teacher embeddings are encoded using extra priors; while student embeddings are learned from the teacher embeddings through knowledge distillation. During inference, the student embeddings are used to enhance fine-grained knowledge while the teacher embeddings are discarded, resulting in negligible computational costs and no need for extra priors. Finally, we further develop a mixture of disease diagnosis expert classifiers to enhance knowledge extraction. The classifiers are initialized using disease embeddings and are modeled as different experts to address various granularity features. Notably, \textbf{EMGKT} can be efficiently applied to most existing methods. Extensive experiments are conducted on two widely-used public datasets and various baselines, which demonstrates the effectiveness and transferability of \textbf{EMGKT}.

---


### 100. [BeliefScope: Diagnosing Evidence-Driven Revision and Pressure-Induced Shifts in Large Language Models](https://arxiv.org/abs/2610.11305)

**<font color=#1a73e8>作者：</font>** Shuai Guo, Yidong Cui  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language model may revise the same proposition after receiving genuinely relevant evidence or after receiving directional user pressure that adds no relevant fact. The observable response shift alone therefore does not reveal which source drove the change. We introduce BeliefScope, a controlled black-box framework for separating these two sources of influence around a fixed target proposition. BeliefScope crosses Evidence and Pressure with factor-specific local controls and measures response changes through probability reports, categorical judgments, and action recommendations on channel-appropriate scales. To determine when these observable contrasts support reliable attribution, we evaluate the observation design under controlled synthetic conditions. Known-truth recovery and targeted ablations establish where Evidence- and Pressure-related effects can be separated, while semi-synthetic stress tests map how that recoverability changes as the observation process becomes noisier and more heterogeneous. Across a 36-family Qwen/Llama study, with targeted 12-family checks that also include Gemma3-12B, the resulting profiles show substantial evaluation-context dependence: broad model-level differences can change under matched controls, decoding, or response interfaces, while some narrower within-model patterns remain stable. Instruction interventions further show that reduced target-aligned Pressure following can reflect either stable resistance or movement in the opposite direction. BeliefScope summarizes these measurements as a conditional belief-response profile that keeps diagnostic effects tied to the evaluation conditions under which they are observed, together with explicit validity boundaries for that diagnosis.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-288](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

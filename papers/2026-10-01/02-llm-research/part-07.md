# 🧠 大模型相关研究 | 2026年10月01日

> 本类共 **515** 篇论文：已确认 **473** 篇，待复核 **42** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 301. [Foundations of Proactive Agents: Principles, Technical Layers, and Proactivity-Gym](https://arxiv.org/abs/2609.37267)

**<font color=#1a73e8>作者：</font>** Jio Oh, Seunghyun Do, Young-Jun Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proactive LLM agents can turn idle compute into useful support before users ask. Yet even correct work can misread user context, impose review costs, or undermine trust. This work proposes foundations for designing, realizing, and evaluating proactive LLM agents around three joint principles (3T): Task Capability, anticipating relevant needs and correctly performing useful work; Temporal Allocation, allocating compute according to resource availability and when results are needed; and Trust, sustaining users' confidence and appropriate reliance on the agent. We connect these objectives to a design space organized around five dimensions: task scope, anticipation horizon, activation trigger, processing timing, and intervention depth, and specify the situation and system modeling needed to support its choices, including user and environment representations, backbone LLMs, and agent harnesses. Lastly, we propose PROACTIVITY-GYM, a simulation-based evaluation testbed including multi-day scenarios, stateful environments, and persona-conditioned simulated users that can evaluate the consequences of proactive assistance across interactions. Evaluations across 23 model-harness configurations uncover substantial performance gaps across 3T and reveal that LLM judges often conflate task capability and trust. A human study with 30 participants demonstrates the importance of the joint 3T optimization: participants show sharp trust declines after intervention misalignment despite correct outcomes, and prefer sleep-time assistance, even when imperfect, to preserve ongoing focus. Together, these findings support designing and evaluating proactive agents through the joint consideration of useful work, compute allocation, and evolving user trust.

---


### 302. [SAM Meets VLM: Parameter-Decoupled Full-Parameter Training for Unified Medical Reasoning and Segmentation](https://arxiv.org/abs/2609.37283)

**<font color=#1a73e8>作者：</font>** Xuyang Cao, Enyou Liu, Jun Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical multimodal large language models (MLLMs) are increasingly expected not only to answer clinical questions, but also to localize the visual evidence behind their predictions. A common strategy connects a vision--language model (VLM) with SAM-style segmentation through a special <SEG> token, yet full-parameter training of this unified architecture is difficult because image-level reasoning and pixel-level segmentation impose different requirements on the shared representation space. To address this issue, we propose a parameter-decoupled training framework for unified medical reasoning and segmentation. The framework treats the <SEG> hidden state as a semantic-to-spatial prompt for the mask decoder and encourages it to become separable from generic language states, reducing ambiguous segmentation prompts and potential disruption to reasoning representations. It first performs medical shallow alignment to adapt visual features to clinical language without disturbing the LLM; then controlled instruction tuning shapes separable <SEG> prompt states, monitored by the Davies--Bouldin Index (DBI), while scaling segmentation gradients entering the language backbone; finally, the SAM branch is specialized with the VLM frozen to improve mask precision without altering reasoning parameters. Experiments on medical referring segmentation, grounding, visual QA, and textual QA benchmarks show that our framework achieves strong language-conditioned segmentation while preserving competitive reasoning ability. Ablations show that two-phase instruction tuning, gradient scaling, and segmentation specialization all contribute to the model.

---


### 303. [Scaling Full Conformal Image Classifiers](https://arxiv.org/abs/2609.37298)

**<font color=#1a73e8>作者：</font>** Julio Silva-Rodríguez, Ender Konukoglu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction provides set-valued predictions with distribution-free coverage guarantees, making it attractive for high-stakes image classification. However, split conformal prediction is data-inefficient, while full conformal prediction (FCP), despite its stronger statistical efficiency, is computationally prohibitive at scale because it requires candidate-specific model refits at test time. We address this limitation by leveraging zero-shot vision-language models (VLMs) to guide scalable FCP in large label spaces. We introduce Targeted Full Conformal Prediction (T-FCP), which uses a lightweight inductive conformal predictor to prune unlikely labels and applies FCP only to the remaining candidates, reducing computation while retaining the formal guarantee of the combined conformal procedure. We further propose Stabilized Online LDA (SO-LDA), an efficient VLM adaptation solver based on rank-one inverse-covariance updates. Across multiple benchmarks, including ImageNet, T-FCP enables practical full-conformal image classification with modest test-time overhead, yielding efficient prediction sets and more stable empirical coverage than split conformal alternatives.

---


### 304. [MetaCtrl: Your Large Language Models Can Reason Better and More Concisely with a Metacognitive Controller](https://arxiv.org/abs/2609.37304)

**<font color=#1a73e8>作者：</font>** Zhibin Wen, Tao Han, Lei Bai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models improve performance on challenging problems by allocating additional computation before answering, but longer reasoning does not always lead to better results and can introduce substantial redundant reasoning on simple problems. Conversely, aggressively shortening reasoning can degrade performance on difficult ones. Effective reasoning therefore requires dynamically deciding when additional computation is useful based on the reasoner's capabilities and evolving solution state. Existing approaches often rely on predefined budgets or intervention rules, retrain the target reasoner, or require additional supervision. We introduce MetaCtrl, a lightweight controller that adaptively regulates a frozen reasoner without predefined token budgets or reasoner retraining. We formulate reasoning regulation as a sequential metacognitive control problem: MetaCtrl observes the evolving reasoning trace and decides whether to continue, simplify, skip redundant steps, or conclude reasoning. It is trained directly with reinforcement learning using a reward that prioritizes correctness while favoring shorter trajectories among correct solutions, requiring neither supervised intervention trajectories nor problem-specific budgets. Across seven benchmarks spanning mathematics, science, and code, MetaCtrl consistently improves the accuracy of LRMs while reducing their reasoning length. On DeepSeek-R1-Distill-Qwen-7B, it improves average accuracy by 4.7 points while reducing generation length by 53.3%. Without further training, the same controller transfers to an unseen reasoner (e.g., Qwen3-14B), improving average accuracy by 2.9 points and reducing generation length by 50.3%. These results establish MetaCtrl as a plug-and-play controller for improving reasoning accuracy while substantially reducing inference-time generation. The code is available at this https URL.

---


### 305. [AutoMark: Enabling Autoresearch to Discover Better LLM Watermarks](https://arxiv.org/abs/2609.37310)

**<font color=#1a73e8>作者：</font>** Thibaud Gloaguen, Robin Staab, Martin Vechev  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With LLM watermarking being deployed commercially and now required by regulations, improving its reliability and effectiveness has become crucial. Yet, recent progress in the field of LLM watermarking has increasingly been driven by improving details of existing methods, an effort fundamentally limited by the pace of human researchers. In this work, we enable for the first time the autonomous discovery of new distortion-free state-of-the-art watermarking schemes. To enable this, we (i) establish strict criteria to ensure that watermarks are reliable (e.g., they do not have an unexpectedly high false positive rate), (ii) propose rigorous statistical tests to automatically evaluate whether a watermarking scheme satisfies our criteria, and (iii) design an evaluation suite to rank watermarks along three key dimensions: detectability, quality, and robustness. By running our framework with 3 frontier models (GPT-6 Astra, Opus 5, Gemini-3.8 Flash), we discover over 50 different watermarking schemes, including several that outperform prior works along all key dimensions. We complement this by a manual study of the discovered schemes, distilling the key ideas into smaller components, and individually studying the impact of each component across dimensions (detectability, quality, robustness) to better understand how the proposed schemes operate. Importantly, we find that the agents, on top of improving existing ideas, also discover fundamentally new ideas (e.g., aligning watermark scores with random per-request direction). Overall, our work establishes the first steps of fully autonomous watermarking research, enabling the discovery of more reliable and effective watermarks. Our code is available at this https URL, and a blogpost to visualize our results at this https URL.

---


### 306. [Hidden Reasoning Must Leak, but Need Not Be Readable: Fundamental Opportunities and Limits for Chain-of-Thought Monitoring](https://arxiv.org/abs/2609.37312)

**<font color=#1a73e8>作者：</font>** Mohammadali Mohammadkhani, Madhava Krishna, Yash Sarrof 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can reasoning models trick chain of thought (CoT) monitors and perform hidden computation without revealing it in their thinking traces? We show that the answer depends on the underlying task difficulty and the model size. Simple computations can be performed covertly; however, beyond a threshold depending on model size, successfully solving the task necessarily leaks a near-linear amount of information about the covert task input into the CoT. Therefore, sufficiently complex hidden computation always leaves an information-theoretic footprint. However, concerningly, this leakage need not be readable: Under plausible cryptographic assumptions, even a one-layer Transformer can encrypt its reasoning online so that no polynomial-time monitor can extract information about the hidden computation. Overall, our theoretical and empirical results provide a holistic view of both the opportunities and the limitations of CoT monitoring.

---


### 307. [FLASH: A "Generate Once, Synthesize Many" Framework for Synthetic Anomaly Generation in Industrial Anomaly Detection](https://arxiv.org/abs/2609.37314)

**<font color=#1a73e8>作者：</font>** Abhay Kumar Das, Rajesh Gangireddy, Ashwin Vaidya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic anomaly generation helps expand industrial anomaly datasets when real defects are scarce or unavailable. Existing approaches lie at two extremes: procedural approaches are fast but struggle to represent complex anomalies, while generative approaches produce diverse defects but require costly per-sample generation. We present FLASH, a framework that decouples defect generation from anomaly synthesis under a ``generate once, synthesize many'' paradigm. Given only normal images, FLASH uses Vision-Language Model (VLM) guidance and an image-generation model to produce a small set of defect images, from which it extracts, validates, and banks reusable defect patches. For synthesis of anomalous images, Object Boundary Suppression (OBS) first identifies the probable foreground object-aware region of the host image, while Multi-Resolution Spectral Pyramid (MRSP) noise generates diverse, size-controllable masks that determine the defect location and spatial extent. It then composes a large and diverse synthetic anomalous image set by localizing the defect region, sampling size-controllable placement masks and seamlessly blending retrieved defects onto new defect-free images without further need for image generation. Experiments on the MVTec AD 2 dataset show that FLASH-generated anomalies nearly close the calibration gap on real defects, reaching 78.1% image-level F1 against an 83.6% real-anomaly upper bound and providing the most consistent calibration transfer across detectors among procedural and generative alternatives. Moreover, FLASH synthesizes anomalies more than 11.95x faster than per-sample generative approaches.

---


### 308. [What Comes Next? Omni-StoryBench for Evaluating Story-Grounded Omnimodal Generation](https://arxiv.org/abs/2609.37317)

**<font color=#1a73e8>作者：</font>** Sieun Hyeon, Yejoon Lee, Mintaek Lim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnimodal evaluation should go beyond independent text, image, and speech production: individually plausible outputs may not express a coherent shared event. We introduce Omni-StoryBench, a story-grounded omnimodal benchmark evaluating whether models can coherently continue stories across image, narration, and speech. Each instance provides a current storybook page and structured next-page conditions, requiring models to generate the next illustration, narration, and spoken character utterance. Omni-StoryBench contains 900 rigorously validated story transitions from openly licensed children's books, with ground-truth next-page references and speech metadata. We evaluate systems with modality-specific metrics and consistency-centered LLM-as-a-judge rubrics for context preservation, condition following, reference consistency, and cross-modal coherence. Across 32 baseline configurations spanning orchestration, semi-orchestration, and native any-to-any paradigms, we find orchestration with strong VLM planning most reliable, while current native omnimodal models often struggle with output completeness and controllability. Our analysis shows text-side performance is associated with image and speech quality, but image generation and visual continuity form the clearest observed bottleneck among the evaluated configurations. These results position Omni-StoryBench as a system-level benchmark measuring coherent omnimodal generation beyond isolated modality quality.

---


### 309. [Mubric: Mutation Testing-Guided Rubric Generation for LLM Evaluation](https://arxiv.org/abs/2609.37322)

**<font color=#1a73e8>作者：</font>** Jiayuxuan Yang, Jie M. Zhang, Yiling Lou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rubric-based evaluation is widely used to assess LLM-based systems by decomposing response quality into task-specific scoring criteria. However, automatically generating rubrics that reliably capture task-specific quality requirements remains challenging. We introduce Mubric, a mutation testing-guided approach to rubric generation. Mutation testing, a classic software testing methodology, evaluates a test suite by injecting faults into programs and checking whether the tests detect them. We draw an analogy between test suites and rubrics: if a rubric captures an important quality requirement, introducing a corresponding defect into an otherwise high-quality response should reduce its score. Mubric first mines common defects from real pairs of preferred and dispreferred responses and abstracts these defects into reusable mutation operators, each specifying how to introduce a particular type of response defect. For a new task, it applies relevant operators to a reference response, checks whether the injected defects reduce response quality, and uses insufficiently penalized defects to refine the rubric. We evaluate Mubric on 703 tasks across four representative domains against six advanced rubric generation methods. Mubric achieves the highest overall evaluation accuracy, outperforming the strongest baseline by 7.48 percentage points.

---


### 310. [VISTA: Value-Informed Event Appraisal for Multimodal Emotion Conflict](https://arxiv.org/abs/2609.37324)

**<font color=#1a73e8>作者：</font>** Jiale Dai, Liuxian Ma, Xiaoke Niu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conflicting emotional cues can be individually valid: a subdued voice may reflect a blocked goal while a smile satisfies a social obligation. Their interpretation depends on what the event means to the person. We introduce VISTA (Value-Informed Semantic Trust Arbitration), a learned seven-field appraisal interface that conditions modality arbitration on concerns, event relations, and expression conditions while retaining a joint-evidence residual. A log-odds decomposition separates emotion expectation from cue diagnosticity, motivating an interface that lets appraisal change how evidence is interpreted. With a shared Qwen2.5-Omni-7B backbone and matched training examples and steps, VISTA reaches 64.5% conflict accuracy on CA-MER, improving on modality gating by 2.5 percentage points on conflict and 0.2 on consistency. Shuffling appraisal across scenes or removing its decision connection reduces this benefit. A common frozen-backbone probe reaches 0.600 macro CCC for appraisal readout, compared with 0.505 for emotion-only fine-tuning. Evaluations across five benchmarks connect recognition under increasing conflict with appraisal readout and downstream decision use. Together, the analyses and experiments support scene-specific appraisal as an intermediate representation that helps interpret conflicting emotional evidence.

---


### 311. [Solving Without Stopping: On-Policy Distillation at Small Scale](https://arxiv.org/abs/2609.37326)

**<font color=#1a73e8>作者：</font>** Hongyang Li, Yiming Zhu, Xiao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation, where a student learns from a stronger teacher's feedback on its own outputs, is a common way to pass reasoning to smaller models. We analyze what it transfers at small scale, distilling Qwen3-8B into Qwen3 4B, 1.7B and 0.6B students, in thinking mode (reason at length, then end the reasoning and answer) and, for comparison, in non-thinking mode (no separate reasoning phase). Long reasoning needs two abilities, solving a problem and knowing when it is solved, and we find that distillation transfers the first, but in thinking mode not the second. Solving improves at every size, up to two ceilings, which we measure comprehensively across both modes and all student sizes: a student's single attempt never exceeds what it could already reach in many attempts before training, and the smaller the student, the further it stays below the teacher. Stopping is where the modes part. In non-thinking mode every student keeps stopping; in thinking mode students stop ending their reasoning early in training, and the smaller the student, the less of this ability survives: the teacher signals a stop almost only where a student already ends its reasoning, so distillation teaches no new stops; it only keeps the student's existing stops that land on a right answer, and a weak student has few such stops. The smallest students often reach the right value but do not commit to it: they either rarely mark it or mark it and write past it. Together, these results describe how small students behave under on-policy distillation, and a diagnostic that separates answer marking, correctness and stopping.

---


### 312. [When to Retrieve, When to Stay: Uncertainty-Aware Temporal Evidence Allocation for Streaming Video-LLMs](https://arxiv.org/abs/2609.37345)

**<font color=#1a73e8>作者：</font>** Xiang Hu, Jiazuo Yu, Lu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding requires Video Large Language Models (Video-LLMs) to reason over continuous visual streams under causal constraints. As the visual history grows, a bounded visual?processing budget requires evidence selection that balances temporal recency with query relevance. Recent-only selection excludes potentially relevant historical evidence, whereas Semantic-only retrieval can displace useful recent context when relevance scores are ambiguous. We introduce WRWS (When to Retrieve, When to Stay), a training-free framework for uncertainty-adaptive evidence allocation. A lightweight external vision-language encoder scores query relevance across the observed history, while an adaptive allocation module uses the normalized entropy of the similarity distribution as a proxy for retrieval uncertainty. WRWS favors semantic retrieval when relevance cues are reliable and strengthens the recency prior under uncertainty. Following a retrieve-first, encode-later pipeline, WRWS selects evidence before target-model visual encoding, such that only the selected observations are processed by the costly target Video-LLM. Experiments across four Video-LLM families and multiple model scales demonstrate competitive accuracy on StreamingBench and OVO-Bench. In our efficiency evaluation, WRWS reduces average vision-to-answer time to 47.93% of the state-of-the-art method. Code will be released.

---


### 313. [TAEC: Trajectory-Aware Evidence Coordination for Multi-Step Visual RAG](https://arxiv.org/abs/2609.37349)

**<font color=#1a73e8>作者：</font>** Yalun Wu, Bingzhou Wang, Boyang Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-step visual retrieval-augmented generation (RAG) answers complex questions by repeatedly retrieving visual evidence, updating an intermediate state, and deciding whether to continue searching or answer. Yet retrieving relevant evidence does not ensure its effective use throughout the reasoning trajectory. As multi-step reasoning progresses, redundant sources occupy context capacity needed for missing evidence, observations tied to resolved requirements or unproductive searches linger in context, and visual sources are revisited with insufficient detail for fine-grained reading. We term this loss of usable evidence over a reasoning trajectory trajectory-level evidence utilization degradation. To address it, we propose Trajectory-Aware Evidence Coordination (TAEC), a training-free framework that coordinates evidence use around unresolved answer requirements. TAEC tracks these requirements in a shared trajectory state to guide which evidence enters the context, how accumulated memory is retained, and at what level of detail visual evidence is examined. Under a unified evaluation protocol on ViDoSeek, SlideVQA, and MMLongBench-Doc, TAEC achieves the best overall performance against leading training-free visual RAG baselines, with the highest average accuracy across multiple proprietary vision-language models. These results demonstrate that aligning evidence with evolving reasoning needs improves evidence use throughout multi-step visual RAG.

---


### 314. [Port-Hamiltonian Latent Deliberation: Mitigating the Deliberation Drift Cliff in Test-Time Compute Scaling](https://arxiv.org/abs/2609.37351)

**<font color=#1a73e8>作者：</font>** Zeyu Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time compute scaling has emerged as a cornerstone of advanced machine reasoning, yet performing iterative deliberation directly within continuous latent representation spaces reveals a catastrophic pathology: the Deliberation Drift Cliff. While unconstrained recurrent latent models achieve initial reasoning gains at short horizons (K <= 4), their reasoning collapses when extrapolated to deeper thinking steps (K >= 16), dropping by 22% to 62% across standard logical benchmarks. We resolve the trilemma among expressivity, Lyapunov stability, and computational efficiency in test-time latent reasoning through a 22-round empirical and theoretical investigation. We demonstrate that strictly conservative scalar potential gradient flows suppress long-range drift (cliff 3.40%) but bottleneck peak reasoning accuracy at 32.73%, whereas unconstrained rotational flows achieve high symbolic expressivity (82.33%) but suffer a severe 36.87% drift cliff. To resolve this geometric duality, we establish Port-Hamiltonian Latent Deliberation (PH-LD) and propose the Direct-Gradient Pure-Tensor Helmholtz-Hodge Decomposition (DG-HHD). DG-HHD parameterizes the attracting flow as a tangent projection tensor network while orthogonally decoupling non-zero circulation (Hodge machine error 1.65e-17, contraction error 5.55e-17), eliminating runtime autograd dependencies to achieve 1.84x vector field and 2.09x RK45 rollout speedups. In a 15-arm symmetrical Pareto benchmark, DG-HHD achieves 58.67% peak accuracy (+25.94% absolute gain over conservative HHD) and retains 35.27% at K=32. Transferred to small language model (SLM) multi-hop causal reasoning, DG-HHD delivers monotonic compute scaling (49.33% to 51.56%) and suppresses out-of-distribution drift (cliff -0.66%). All 30 Level 0 deterministic invariants are certified.

---


### 315. [Seek Before You Move: Evidence Seeking for Progress Grounding in Vision-Language Navigation](https://arxiv.org/abs/2609.37353)

**<font color=#1a73e8>作者：</font>** Zhimin Wang, Meiyuan Zhu, Duo Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Navigation (VLN) requires agents to continuously ground task progress from long-horizon instructions and partial egocentric observations. Existing VLM-based navigation agents typically reason only over available observations and may remain confident even when task-relevant evidence is missing. For example, an agent may confidently proceed forward and get lost even though the landmark indicating the next turn lies outside its current field of view. We term this failure mode Progress Myopia: the agent fails to recognize unreliable progress grounding and continues acting on insufficient evidence. To address it, we propose SeekVLN, an evidence-seeking framework that couples semantic progress reasoning with active acquisition of task-relevant observations. SeekVLN is trained in two stages: First, Future-guided Reverse Generation (FRG) uses future expert actions to augment offline expert trajectories with supplementary views and evidence annotations. Supervised fine-tuning on these trajectories establishes a prior for evidence seeking and progress reasoning without additional expert interaction. However, imitation alone does not reveal whether seeking improves subsequent navigation. We therefore introduce Counterfactual Contrastive Policy Optimization (C2PO) for reinforcement fine-tuning. By comparing each evidence-seeking branch with a counterfactual direct-navigation branch from the same state, C2PO uses a contrastive reward to assign credit to seeking decisions based on subsequent navigation benefit. Experiments on simulated benchmarks show that SeekVLN achieves state-of-the-art performance, improving success rate by 12.7% and 7.5% over the base model on R2R-CE and RxR-CE, respectively. Both simulated and real-world evaluations exhibit human-like evidence-seeking behaviors for more reliable progress grounding.

---


### 316. [Teaching LLMs to Generate Challenging MILP Instances via Solver Feedback](https://arxiv.org/abs/2609.37356)

**<font color=#1a73e8>作者：</font>** Jitin Singla, Parikshit Pareek, Pratik Jawanpuria 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating optimization instances that are both feasible and computationally challenging is crucial for benchmarking solvers and training learning-based optimization algorithms. Existing non-LLM generators rely on seed instances or parameter tuning, resulting in high test-time computational cost, while existing LLM generators lack explicit hardness measures. Recent reinforcement learning methods with verifier feedback evaluate only binary correctness, which is misaligned with generating challenging problems. We note that an optimization solver reports the cost of solving at several stages of its pipeline, and leverage this to design a reward that scores both the solvability and the hardness of generated problems, measured by branch-and-bound nodes and post-cut relaxation gaps. Our key idea is a challenger-solver asymmetric self-play approach, where an LLM challenger generates progressively harder instances and the solver verifies feasibility and hardness, so no seed or training MILP instances are required. We fine-tune Gemma-4-12B and Qwen3.5-4B with GRPO and a size curriculum into OptiScribe-12B and OptiScribe-4B, which generate feasible yet challenging MILP problems from natural language instructions. On capacitated facility location and max-cut, OptiScribe-12B raises median SCIP search nodes by 1.7-5x and post-cut gaps by 1.1-1.7x over its base model and improves the feasibility rate on facility location by 9-19 points, while OptiScribe-4B raises median nodes by up to 15.6x. The problems cover a wider difficulty range than public benchmarks of the same size, follow instructions on density and difficulty, and can tune solver settings for families that public libraries lack. These results indicate that optimization-specific rewards, used in self-play mode, can teach LLMs to generate high-difficulty optimization benchmarks. We will release our code and models publicly on acceptance.

---


### 317. [SemOPT: Fixing Semantic Errors in LLM-based Optimization Modeling via Reward-Guided Search](https://arxiv.org/abs/2609.37361)

**<font color=#1a73e8>作者：</font>** Zetong Zhou, Wentao Zhang, Jingyuan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Operations research supports decision-making in domains such as energy, economics, and healthcare. Solving operations research problems typically begins with optimization modeling, which translates a natural-language problem description into executable solver code. LLMs offer a promising way to automate this process, but they remain prone to errors. In practice, these errors can be divided into two categories: syntactic errors refer to solver code that fails to run successfully or is judged infeasible by the solver; semantic errors refer to solver code that successfully returns an objective value but violates the intent of the original problem. Since semantic errors do not trigger runtime failures, they are difficult to detect and rectify. To address this problem, we introduce SemOPT, a semantic-guided framework for correcting LLM-based optimization models. SemOPT combines a semantic reward model that distinguishes faithful math models from plausible but incorrect ones with an adaptive correction system that applies hierarchical reward-guided search over the modeling space. Experiments on seven optimization modeling benchmarks show that SemOPT establishes a new state of the art and achieves an average 7.6% accuracy improvement over the strongest baseline on complex datasets.

---


### 318. [Pretrain Once, Route Anywhere: Towards a Foundation Model for LLM Routing](https://arxiv.org/abs/2609.37362)

**<font color=#1a73e8>作者：</font>** Guannan Lai, Han-Jia Ye  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) routing aims to assign each query to the most suitable model from a heterogeneous candidate pool, improving the quality--efficiency trade-off of LLM inference. Existing routers are typically learned through local fitting: a router is optimized for a particular query workload and candidate pool, and often requires additional supervision or retraining as the routing environment changes. We ask whether LLM routing can instead be approached from a foundation-model perspective, learning a reusable routing capability that generalizes across tasks, candidate models, and deployment conditions. To this end, we introduce RouteFM, which learns to characterize anonymous candidate models from behavioral context and infer their target-specific capabilities, rather than binding routing decisions to fixed model identities or a single environment. Through episodic pretraining across heterogeneous routing environments, this capability can be reused by a frozen router and adapted to new environments through context alone. Experiments demonstrate transfer across changes in domains, modalities, candidate pools, and context budgets, with the largest gains when behavioral evidence is limited. On MMR-Bench, which is excluded from pretraining, RouteFM outperforms the strongest baseline by 2.23 quality points with only eight observations per candidate. These results support moving LLM routing from repeated local fitting toward a pretrain once, route anywhere paradigm. Our code is publicly available at this https URL.

---


### 319. [Shaping Opinion: Quantifying the Psychological Impact of Autonomous Multi-Agent LLM Interactions](https://arxiv.org/abs/2609.37369)

**<font color=#1a73e8>作者：</font>** Marcos Rodriguez-Vega, Afonso Ferreira, Iru Exposito-Luis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Natural-sounding multi-agent conversational AI is increasingly deployed, fundamentally altering human-machine interaction and human information processing. While prior work largely focuses on algorithmic failure, this study investigates the cognitive ergonomics and socio-cognitive impact of algorithmic competence. We present and evaluate FORMS (Framework for Opinion and Rhetoric in Multi-agent Simulations), a low-latency architecture for spatially mediated human-machine dialogue, driven by distinct LLM-based personas and real-time concurrency resolution. To conduct a system test and evaluation of its psychological impact, we exposed an adolescent cohort (n=120) and an adult pilot group (n=25) to a live, moderated synthetic debate. Our findings reveal that exposure to highly competent multi-agent systems triggers "Cognitive Destabilization," fragmenting users' prior strategic consensus. Concurrently, we observe a "Regulatory Awakening" driven by the "Normality Paradox": fluid human-machine interactions inherently increase the baseline demand for external regulation. Furthermore, our pilot study suggests the presence of a "Truthfulness Paradox": despite understanding the risks of generative AI, participants in the adult cohort rated the synthetic debate as significantly more sincere than equivalent human discourse (Cohen's d=2.04). Supported by robust statistical effect sizes, this paper contributes the FORMS architecture and a replicable evaluation protocol, illustrating how high-fidelity conversational systems can reshape human information processing.

---


### 320. [Compiling Learning Problems into Adaptation Programs for Language Models](https://arxiv.org/abs/2609.37371)

**<font color=#1a73e8>作者：</font>** Rebecca Ramnauth, Brian Scassellati  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model adaptation is typically governed by a fixed recipe, even though different update programs can produce substantially different behavioral outcomes. We introduce adaptation compilation, which reframes where, how, and to what extent a model should adapt as a joint prediction and decision problem. Rather than searching over candidate programs anew for each learning episode, a compiler learns from prior adaptations to predict a vector-valued counterfactual response surface over candidate programs---their expected effects on acquisition, transfer, boundedness, and preservation---and selects a program before adaptation begins. Because this predicted geometry captures multiple behavioral consequences rather than a single winner or scalar score, it can be reused under different downstream priorities without retraining. Across five learning types, preferred programs vary meaningfully across episodes, and this variation is predictable from pre-adaptation information. On Llama-3.1-8B, compiler-selected programs approach exhaustive search while outperforming global and objective-specific defaults. Replication on Gemma-2-9B preserves program heterogeneity and selection headroom, but shows that exploiting this headroom requires accounting for uncertainty when departing from strong defaults. Together, these results show that adaptation search can be amortized across related learning problems, turning prior adaptation experience into a basis for deciding how future learning should occur.

---


### 321. [Beyond Prompt Count: How Data Shapes Transfer in On-Policy Distillation](https://arxiv.org/abs/2609.37377)

**<font color=#1a73e8>作者：</font>** Jiaxuan Wang, Jiafei Lyu, Yuchen Cai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains students using teacher feedback on their own sampled responses, yet how prompt choice shapes transfer across teacher-student pairs remains poorly understood. We systematically study prompt quantity, source, and selection across RL- and SFT-continuation pairs and cross-model settings. We find that OPD can be highly prompt-efficient: a few prompts can approach large-pool performance, with four DAPO prompts matching the observed mathematics score of 3,840 DeepMath prompts. However, prompt utility is relational rather than intrinsic: changing only the teacher can reverse the relative effectiveness of mathematics and code prompts. To characterize these transfer differences, we analyze parameter and functional changes across prompt supports and model pairs. Functional alignment with the teacher varies across supports and target tasks; in continuation pairs, teacher-aligned prediction changes can coexist with weak parameter alignment. Continued OPD on effective supports can restore performance after unfavorable transfer. Finally, targeted selection does not consistently outperform uniform random sampling, and filtering out a source that performs poorly alone yields no consistent gain across three paired support draws. Overall, our results distinguish prompt efficiency from prompt interchangeability and show that effective data choice depends on the teacher-student pair and target capability, with random sampling providing a competitive baseline in the studied settings.

---


### 322. [Rethinking Soft Tokens for Parallel Decoding in Diffusion Language Models](https://arxiv.org/abs/2609.37391)

**<font color=#1a73e8>作者：</font>** Kodai Kawamura, Kenji Kawaguchi, Anji Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) enable parallel generation by predicting and committing multiple tokens at each denoising step, yet they can generate individually plausible but mutually inconsistent tokens. Recent work shows that \emph{soft tokens} can mitigate this issue by representing uncertain positions with continuous embeddings built from the model's predictive distribution at the previous decoding step. However, although soft tokens are commonly understood as preserving predictive uncertainty, how soft-token feedback improves parallel decoding has not been systematically examined. In this paper, we investigate this question in frozen pretrained DLMs to examine soft-token feedback without the effects of additional training. To construct soft-token inputs in a training-free setting, we identify a geometric mismatch between conventional soft-token construction and the pretrained embedding space. Based on this observation, we propose a training-free, geometry-aware construction of soft tokens. Our analysis of soft-token feedback suggests that uncertainty preservation alone does not fully explain how it reshapes subsequent predictions. To better explain how soft-token feedback improves parallel decoding, we provide empirical evidence that it favors coherent token sequences. Across four pretrained DLMs and four math and code benchmarks, our method outperforms standard parallel decoding and a training-free Euclidean soft-token baseline. Code: this https URL

---


### 323. [Confidence-Guided Protocol IR for LLM-Aided Security Protocol Modeling](https://arxiv.org/abs/2609.37396)

**<font color=#1a73e8>作者：</font>** Siqi Li, Yufan Cai, Hongshu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models offer a promising interface for translating natural-language protocol descriptions into formal security models, but their outputs remain difficult to trust without expert validation. In this paper, we present a human-in-the-loop framework for generating Tamarin-verifiable formal models of security protocols. Our key observation is that the main correctness bottleneck is the semantic accuracy rather than the syntactic validity of the intermediate protocol representation. To address this problem, we introduce a protocol intermediate representation (IR) that serves as a human-auditable semantic checkpoint between natural-language parsing and formal model generation. The IR explicitly captures protocol participants, message flows, value provenance, cryptographic operations, proof targets, and compromise assumptions. We further design an interactive interface that highlights uncertain fields and guides users to inspect the most critical semantic decisions based on model confidence before model generation. Rather than replacing formal-methods experts, our approach uses LLMs to produce auditable semantic drafts while leveraging verification tools to check the resulting formal models. Code and verification artifacts are available at this https URL.

---


### 324. [Routing Should Pay for Itself: Sparse Supervision for Economical LLM Routing](https://arxiv.org/abs/2609.37402)

**<font color=#1a73e8>作者：</font>** Guannan Lai, Gelin Bian, Hao-Xuan Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) routing reduces serving cost by assigning each query to an appropriate model while preserving response quality. Learning such a router, however, often requires executing multiple candidate models on historical queries to collect query--model quality feedback, creating a nontrivial supervision cost before deployment. Existing work largely focuses on serving-time efficiency, overlooking whether the resulting savings are sufficient to recover this upfront expenditure. We further observe that routing quality often saturates well before all query--model feedback is collected, suggesting that dense supervision can be economically over-provisioned. We propose SaveRouter, a sparse-supervision routing framework that selectively acquires informative model feedback and shares capability information across related queries, while retaining query-level refinement for fine-grained routing. We evaluate routing by jointly accounting for supervision expenditure and subsequent serving-time savings. Across four routing benchmarks, the main setting uses only about 33--41% of available training feedback while maintaining competitive or better routing quality, and reduces the break-even deployment volume by approximately 1.9--9.5 times compared with the fastest conventional router. Further analysis shows that acquiring more supervision is not always economically preferable: the supervision level that minimizes serving cost can differ from the one that achieves the earliest payback. Our code is publicly available at this https URL.

---


### 325. [Complementary Retrieval-Augmented Prompting for Consistent Long-Form Video Generation](https://arxiv.org/abs/2609.37407)

**<font color=#1a73e8>作者：</font>** Xianghan Wei, Xiaoda Yang, Zhi Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent video foundation models excel at generating high-quality short videos, long-form video generation remains a critical challenge, where a major bottleneck lies in conditioning independently generated shots to preserve consistent characters, scenes, and objects throughout a story. Existing training-free approaches typically condition target shots using retrieved historical visuals. However, these references often suffer from severe informational mismatch, either introducing irrelevant contextual redundancy or failing to provide the full combination of required elements for the target shot. To resolve this, we present Complementary Retrieval-Augmented Prompting, an agentic framework that strategically aggregates a compact set of mutually supportive historical references to achieve complete and targeted conditioning for long-form video generation without retraining or modifying the underlying generator. Specifically, our framework explicitly models the visual elements required by each target shot by parsing the narrative script into a text-grounded visual element registry that tracks characters, objects, scenes, and their shot-level states. A VLM-annotated keyframe library further maps these elements to past visual observations. Guided by the required elements, our agent retrieves complementary references that maximize target-element coverage while minimizing historical noise. Finally, the retrieved references, structured element states, and grounding instructions are assembled into a unified prompt for the frozen video generator. This element-aware process provides comprehensive conditioning while remaining fully interpretable. Quantitative and qualitative evaluations on multi-shot story generation demonstrate that our method consistently outperforms recent-frame, memory-based, and entity-level retrieval baselines in cross-shot consistency and text-controllability.

---


### 326. [Look What You Made Us Cluster: Hate Narrative Extraction from Reddit Discourse](https://arxiv.org/abs/2609.37408)

**<font color=#1a73e8>作者：</font>** Annabelle K. L. Chua, Forster J. Khoo, Joel C. R. Tan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Narrative extraction allows us to identify online hate narratives, supporting the construction of rigorous detection systems. Existing computational approaches, however, are limited in precision as they rely on semantic representations, which tend to capture only surface-level meaning. To detect more precise and interpretable narratives, we present an extraction pipeline that represents narratives as entity-evaluation pairs. Narratives are extracted using a Large Language Model (LLM) reasoning process that extends Aspect-Based Sentiment Analysis, identifying the aspect, classifying its judgement type as the basis for evaluation, and deriving the evaluation accordingly. Extracted narratives are then clustered using Leiden, following which clusters are resolved to an intended level of granularity through an LLM-guided refinement process. We illustrate this narrative pipeline with English Reddit comments from 2024 that criticize Taylor Swift, analyzing a representative cluster that exhibits hate speech patterns to demonstrate its interpretive value.

---


### 327. [Scale Sensitivity in Low-Bit Post-Training Quantization: Curvature of the Quantization Error Landscape](https://arxiv.org/abs/2609.37416)

**<font color=#1a73e8>作者：</font>** Jonas von Berg, Massimiliano Datres, Carlo Kneißl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) methods in the GPTQ family minimize a layer-wise reconstruction error on a uniform grid whose scale must be chosen; the common max-based choice degrades sharply at low bit-widths. We study how sensitive this objective is to the scale. For a layer with i.i.d. Gaussian weights and calibration activations of sufficiently large effective rank, we prove that, as the width grows, the normalized round-to-nearest loss converges with high probability, uniformly over all scales, to the mean-squared error of a uniform quantizer applied to a standard Gaussian; we verify the effective-rank condition for wide, randomly initialized MLPs with odd Lipschitz activations and isotropic Gaussian calibration data. The limiting objective has a unique nondegenerate minimizer, whose scale decreases strictly with the number of levels and whose curvature with respect to relative scale errors decays approximately exponentially with the bit-width. GPTQ experiments on five LLMs show the same trend: the scale rule changes perplexity substantially at 2--3 bits and negligibly from 6 bits on, and a local measure of GPTQ scale sensitivity decreases with bit-width in line with the Gaussian curvature. The Gaussian-optimal scale fails on raw weights; after Hadamard incoherence processing it matches the best searched rule at 3 bits and above without any search, but remains clearly worse at 2 bits.

---


### 328. [LazySloth: Bounded LLM-based Lazy Tree Search for Fast Long Video Comprehension](https://arxiv.org/abs/2609.37426)

**<font color=#1a73e8>作者：</font>** Arka Mukherjee, Kaleen Shrestha, Larissa Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern vision-language models (VLMs) have shown promising results in long-video understanding due to the rich semantic information they can capture. However, most methods focus on coarse captioning of extracted image frames that are computationally inefficient and require models with large context windows. While past work has explored efficient methods through multimodal retrieval-augmented generation (RAG), they rely on lossy embeddings that lose temporal context and fine-grained detail. Few works to date have investigated how VLM-based query-relevant information retrieval can be optimized. We introduce LazySloth, an efficient tree-based search method that speeds up video comprehension and retrieval tasks 2.9-8.3x (compared to existing agentic methods) through bounded captioning of portions of the video considered irrelevant by a VLM of the video. Compared to contemporary specialized video-understanding VLMs and RAG-based methods, LazySloth achieved similar or better final task accuracy across two recent open-source base VLMs--Gemma 4 31B and Qwen3.6 27B--across four benchmarks. LazySloth reduced the gap between the base open-source model and a closed-source model, GPT-4o. Ablations showed that replacing VLM scene understanding with CLIP-based retrieval cost 8.8-19.9% in accuracy, while lazy tree construction matches eager construction at a fraction of the captioning cost. With LazySloth, we demonstrate the possibility of faster long-video comprehension without substantial loss in performance.

---


### 329. [Looped Actor: Depth-Recurrent Reasoning Models for Reinforcement Learning](https://arxiv.org/abs/2609.37432)

**<font color=#1a73e8>作者：</font>** T. Konstantin Rusch, Tim Seyde, Jared Boyer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped reasoning models repeatedly apply a shared set of parameters, enabling more computation without increasing the model size. These models also support input-dependent computation by dynamically deciding when to stop looping. Motivated by the recent success of looped transformers in language modeling and reasoning, we investigate whether dynamic looping can similarly benefit sequential decision-making. We provide a complexity-theoretic motivation for this approach by showing that there exist Markov decision processes in which a state-adaptive policy achieves the optimal return with asymptotically less expected computation than any optimal fixed-runtime policy. To learn compute-adaptive policies in practice, we introduce Looped Actor, a transformer-based policy that repeatedly refines a latent representation toward a fixed point using a shared computational block. This allows the model to allocate computation adaptively by varying the number of loops based on the current state. We evaluate Looped Actor on 22 tasks across six environments, ranging from combinatorial puzzles to robotic manipulation and spanning online and offline reinforcement learning (RL) with discrete and continuous actions. Looped Actor matches or exceeds the performance of an untied baseline with 16$\times$ more parameters, with the largest gains in environments where action selection requires substantial multistep planning. For the Boxoban environment, we find that the computation allocation is structured: the number of loops increases with the number of remaining pushes and future optimal pushes become increasingly predictable from the latent state over successive loops. Together, these results highlight actor looping as a simple and efficient way to equip RL agents with adaptive computation and improve their planning capabilities. Code is available at this https URL

---


### 330. [Learning to Retrieve Missing Evidence for Long-Term Memory QA](https://arxiv.org/abs/2609.37443)

**<font color=#1a73e8>作者：</font>** Yi-Xuan Deng, Yi Zhang, Wei Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables language models to use past interactions in future conversations. However, evidence needed to answer a question may be scattered across distant turns, while the question itself omits clues needed to locate it. Retrieved facts can reveal these clues, motivating retrieval decisions conditioned on evidence already found. We introduce MERA (Missing-Evidence Retrieval Augmentation), which separates globally searchable memory from a question-specific evidence state. Verified evidence guides subsequent retrieval without restricting access to the global memory. We train a lightweight planner through reinforcement learning, rewarding queries that recover previously missing evidence. MERA achieves strong answer accuracy across Qwen3-30B and GPT-4o-mini backbones. With Qwen3-30B for evidence processing and answer generation, the trained 0.6B planner achieves 77.40% accuracy on LoCoMo and 71.29% on LongMemEval-S, exceeding a 30B planner without retrieval-grounded training by 4.10% and 3.96%, respectively. On LoCoMo, later retrieval rounds increase cumulative evidence recall from 55.5% to 80.5%.

---


### 331. [Commitment Hierarchies under Intent Revision: A Belief-Revision Account of Salvage in Tool-Use Agents](https://arxiv.org/abs/2609.37453)

**<font color=#1a73e8>作者：</font>** Spandan Ghose Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a user changes their mind partway through a task, an agent that has already split the task into sub-goals and paid for tool calls must decide, per cached sub-result, whether to keep, patch, or discard it (salvage), restarting wastes valid work and continuing unchanged answers the old question. Our main finding is that salvage quality is a matter of role design rather than model capability: a language model asked the keep/patch/discard question one node at a time is unreliable, but asked to classify the revision once, with a deterministic layer propagating the decision, it reaches the cost-optimal oracle on all three models tested, from two vendors. Modeling the plan as a commitment hierarchy and the intent change as a belief-revision operator with AGM style postulates, we prove that no policy observing only a node's local view can be both safe and cost optimal, while the single classification design is both. Across three environments the policy recovers the full achievable savings, 43% cheaper than restart, at 100% correctness.

---


### 332. [Governing the Edge: Automating Commercial Property and Casualty Insurance Underwriting via a Hybrid Local-Cloud Multi-Agent Framework](https://arxiv.org/abs/2609.37454)

**<font color=#1a73e8>作者：</font>** Vivek Kumar Singh, Gautam Bhowmick  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Underwriters in commercial Property and Casualty (P&C) insurance spend 30 to 40% of their time on administrative work rather than risk judgment, and a single submission takes about 40 minutes by hand. We present Governing the Edge, a multi-agent framework for that layer, organized around a data-residency constraint: sensitive submission data must not leave the perimeter. Eleven agents and two deterministic control nodes, one a human-escalation interrupt, form a 13-node LangGraph workflow across two tiers. Agents touching raw submissions run locally on Gemma 2, each bound through a tool interface logging every invocation (synthetic stubs in the current prototype); only anonymized scores and non-identifying fields cross to Claude Sonnet in the cloud. Compliance rules are encoded as conditions on graph edges, so a non-compliant submission never reaches pricing. We walk through one full scenario end to end, a commercial auto submission whose principal driver carries serious violations, showing every agent call, every tool invocation, and the resulting routing decision. The framework processes a 40-minute manual submission in a few minutes on a single edge device, dominated by serialized on-device inference. On the hard-stop violation tier the framework enforces every rule correctly and reproducibly, since hard stops are deterministic predicates over fields extracted at temperature 0; overall compliance accuracy across the 20-scenario benchmark is 70%, with the remaining gap concentrated in softer, judgment-based tiers. It keeps a complete audit trail and respects the privacy boundary throughout. We release all code, compliance rules, tool stubs, and synthetic datasets.

---


### 333. [VeriWeave Govern: Evidence-Gated Deterministic Runtime Governance for Enterprise AI Agents](https://arxiv.org/abs/2609.37457)

**<font color=#1a73e8>作者：</font>** Kabeh Mohsenzadegan, Vahid Tavakkoli, Kyandoghere Kyamakya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise artificial-intelligence agents increasingly call tools, modify infrastructure, and process protected data, creating a need to separate action generation from action authorization. This article presents VeriWeave Govern, a deterministic runtime governance layer that evaluates structured agent actions against versioned policies, validates typed evidence, applies fixed deny > review > allow precedence, routes consequential actions to accountable human review, and records replayable tamper-evident audit state. GovernBench evaluates the design over 30 independent seeds and 60,000 oracle-labelled cases spanning five enterprise domains, adversarial evidence, out-of-distribution actions, and temporal policy evolution. VeriWeave achieves 0.9888 mean accuracy, 0.9836 macro-F1, zero observed aggregate false allows, and zero observed Governance Attack Success Rate on the evaluated cases. Six ablations show that evidence gating, deny precedence, out-of-distribution fail-safe behavior, human review, contradiction handling, and temporal replay contribute complementary safety. The deployed API additionally passes 12/12 end-to-end scenarios and a 40,040-request concurrency matrix with zero failures. A separate 150-case EU/Austria regulation-grounded evaluation uses frozen predictions and two independent blinded human annotators, who agree on all decisions. On this set, deterministic engines remain conservative, while a Gemma 4 31B comparator aligns more closely with the human consensus. The results expose a measurable safety--utility trade-off and motivate evidence-aware, replayable governance as an independent control plane for enterprise agent execution.

---


### 334. [CRASM-Gate: Deterministic-First Constraint- and Role-Aware Semantic Mapping with Selective Model Assistance Across Heterogeneous Industrial Standards](https://arxiv.org/abs/2609.37458)

**<font color=#1a73e8>作者：</font>** Kabeh Mohsenzadegan, Vahid Tavakkoli, Kyandoghere Kyamakya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial standards often encode the same engineering concept through incompatible hierarchies, identifiers, roles, and structural constraints, so the nearest lexical or embedding match can still be technically inadmissible. This article presents CRASM, a deterministic constraint- and role-aware semantic mapping method, and CRASM-Gate, its selectively model-assisted extension. The framework separates standard-specific canonicalization, bounded retrieval, deterministic rules, destination-versus-origin role interpretation, semantic and structural ranking, ambiguity refusal, and target validation. CRASM-Gate adds a confidence/disagreement gate that may invoke a candidate-constrained large language model, while final authority remains with deterministic validation. A controlled artifact covers six directed industrial-standard pairs, three difficulty levels, and ten configurations, yielding 14,400 sample-level decisions. With a fixed local model endpoint, CRASM-Gate reaches mean F1 0.9938 and an implemented structural-validity rate of 1.0000; deterministic CRASM reaches 0.9931 without generative-model calls; and the model-only baseline reaches 0.5347. Relative to the model-only baseline, CRASM reduces top-1 errors from 670 to 10 while exhibiting 0.0688 s/sample rather than 24.5263 s/sample observed latency. CRASM-Gate improves CRASM by one additional correct decision out of 1,440, with observed latency increasing to 15.7666 s/sample. The results support a deterministic-first interoperability architecture in which model assistance is optional, measurable, candidate-bounded, and unable to bypass structural validation.

---


### 335. [Relevance Is Not Sufficient Evidence: Detecting Evidence Gaps Before Generation in RAG](https://arxiv.org/abs/2609.37469)

**<font color=#1a73e8>作者：</font>** Suting Chen, Peichun Hua, Yunming Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) grounds large language models in external sources, but retrieved passages often name the right entities without providing the facts needed to answer. Even when instructed to abstain, 12 generators answer 40.0-99.3% of insufficient-evidence questions. Training generators to abstain ties the decision to model weights, may reward answers recalled from parametric knowledge, and still requires a full generator call. Can sufficiency be judged from the question and evidence alone, before any answer exists? We identify pitfalls in constructing insufficient-evidence tests: removing relevant evidence or pairing evidence with unrelated questions can reveal labels through lexical overlap or evidence position. We build a paired benchmark using substitution, deletion, and question-swap constructions that vary answer support while controlling selected surface features, such as word use. Sufficiency can be judged without generating an answer, but no single signal works across all datasets. We introduce RINSE (Relevance Is Not Sufficient Evidence), which combines three signals: whether every part of the question is covered, whether any passage offers an answer, and whether a small language model reading the passages together judges them sufficient. Across six datasets, RINSE ranks sufficient above insufficient evidence with a score of 0.837 (chance 0.5), exceeding the best of 10 prior methods (0.746) and a frontier model queried through an API (0.784). Its weakest dataset scores higher than any other method's weakest (0.684 vs. 0.676). RINSE runs locally before generation, taking 36.5 ms per question on a single GPU.

---


### 336. [Probability Contracts: Accuracy, Coherence, and Decisions Across LLM Interfaces](https://arxiv.org/abs/2609.37470)

**<font color=#1a73e8>作者：</font>** Han Chen, Yingrui Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A probability used for a decision should refer to the same event across equivalent requests. We introduce probability contracts, a benchmark connecting exact finite-world posteriors, validated event transformations, and failure-aware decision evaluation. Four model-interface configurations are evaluated on 1,000 worlds. Their assessments differ across accuracy, coherence, and decision loss: Kev has lower aggregate canonical posterior error than Jev, but larger complement and coarsening residuals, with accuracy ordering varying by stratum. Jev's Event and Choice interfaces induce different binary actions on 32.8% of valid pairs at defer cost 0.10. A post-hoc analysis finds that disagreement certifies only 11-52% of mean binary pair error across configurations. An elementary action-region characterization explains when averaging changes decision loss relative to randomly selecting one interface. Although averaging cannot worsen that baseline's expected Brier score, its decision effect depends on the cost and crossed boundaries; the observed same-baseline penalties occur in configurations already worse than always deferring. The benchmark makes these distinctions measurable without treating consistency as accuracy or a score improvement as a decision guarantee.

---


### 337. [Authority Before Utility: Non-Compensatory Control for Persistent LLM Memory](https://arxiv.org/abs/2609.37474)

**<font color=#1a73e8>作者：</font>** Wesley Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent memory creates a control problem that retrieval relevance alone does not solve: a memory can remain highly useful after an update, deletion, or revocation makes it inadmissible for the current answer. We formalize this as a separation between utility and authority. A fixed finite penalty applied to an unnormalized utility score cannot guarantee exclusion under arbitrary positive-affine reparameterization of that score; by contrast, rank-normalized compensation is scale-invariant and therefore forms a stronger empirical comparator.
Our prospectively frozen TIDE/LongMemEval primary was quarantined before a valid HELDOUT comparison because the materialized TIDE adapter conflated historical age with query-relative inadmissibility and the aligned LongMemEval split left no DEV set for the predeclared penalty selection. We therefore report a post-primary replacement diagnostic on Memora Remembering, where update/delete operations provide item-level forgetting state.
On Qwen3-8B, DEV selected lambda = 0.6 from a ten-point normalized SOFT family. Across 185 HELDOUT units in 28 dependency clusters, HARD exclusion yields 4.04% balanced construct error versus 19.66% for locked SOFT, a paired difference of 15.61 points with a 20,000-replicate cluster-bootstrap 95% interval of [13.07, 18.76].
The effect is driven primarily by forgotten-value leakage while current-value recall is preserved. This is same-Q operator-comparison evidence, not a universal claim that scalar control fails, not an evaluation of learned authority inference, and not an independent downstream-harm endpoint.

---


### 338. [Boundary-State Control for Tool-Using Language-Model Agents: Commit-Time Consistency under State Drift](https://arxiv.org/abs/2609.37475)

**<font color=#1a73e8>作者：</font>** Wesley Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using language-model agents can decide that an action is permissible and execute it only after security-relevant state has changed. We study this proposal-to-commit gap and introduce BSC-R, a deterministic effect-boundary mechanism that binds a single-use commit authorization to the exact action and to a semantic projection of the authorization state that justified it. On 2,847 attacked AgentDojo episodes, the boundary kernel preserves the unprotected agent's behavior exactly (80.576% utility; 1.616% attack success). On 10,302 frozen proposals, it accepts every unchanged commit and rejects every instance of ten prospectively specified changed or replayed classes. In an independently generated boundary-drift experiment, full joint binding commits 0/4,403 invalid contexts while retaining 5,899/5,899 valid contexts. A prospective external evaluation on the 3,460-scenario CONTINUITY suite retains all 700 benign cases, prevents 1,200/1,200 represented non-replay invalid effects, handles 160/160 replay lifecycles correctly, and withholds 200/200 ambiguous no-release cases. The broader external suite also exposes the method's limit: across all 2,560 attacks, BSC-R has a 25% invalid-effect commit rate versus 0% for CONTINUITY. The result is therefore a scoped commit-time consistency mechanism, not a universal agent-safety claim.

---


### 339. [PoE-Fuse: Precision-Weighted Expert Fusion for Bi-Temporal Change Understanding](https://arxiv.org/abs/2609.37485)

**<font color=#1a73e8>作者：</font>** Haruki Watase, Shunya Nagashima, Takayuki Nishimura  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bi-temporal change understanding, which localizes and characterizes what changed between two satellite images, is central to disaster response and environmental monitoring, spanning change detection, building localization, and damage assessment. Strong vision-language models address these tasks, but adapting them typically requires full fine-tuning or reinforcement learning, which is costly and unstable. We propose PoE-Fuse, a parameter-efficient framework that instead composes frozen foundation experts for geometry, grounding, and language, resampling their features onto a shared spatial grid and training only a lightweight fusion trunk. PoE-Fuse treats the aligned features as Gaussian observations of a latent scene state and fuses them by learned per-cell precision. This product-of-experts estimator strictly generalizes uniform summation and scalar gating, and extends to change fields by composing the precisions of the two timestamps. A single shared trunk solves the three tasks at once, reaching a mean F1 of 59.2%, compared with 40.7% for an instruction-tuned temporal vision-language assistant, and surpassing dedicated change-detection models retrained under the same protocol and training budget.

---


### 340. [FORUM: Frozen Outputs Reconciled Using Model Agreement for Visual Grounding](https://arxiv.org/abs/2609.37488)

**<font color=#1a73e8>作者：</font>** Taiyo Sato, Takamasa Sanda, Keisuke Maeda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen multimodal large language models (MLLMs) now solve standard referring expression comprehension with a single prompted call, yet on adversarial benchmarks with same-category distractors and negation, even the largest models are confidently wrong, and resampling repeats the error. Models built from different data and architectures rarely fall for the same confounder, so their agreement is a strong label-free signal of the correct target. We present FORUM, a training-free test-time fusion of frozen MLLMs guided by two fixed geometric rules: agreement-based selection keeps the region supported by the most distinct models, and medoid localization returns an actual member box instead of a coordinate average, so one loose prediction cannot shift the answer. Fusing three open MLLMs, FORUM surpasses the 397B-parameter published reference by a relative 5% in mean accuracy on the adversarial Ref-Adv-s benchmark, and a plain averaging ensemble by 15%. The gains transfer to standard RefCOCO+, and a balanced lineup with no dominant member still surpasses the 397B model by 5%.

---


### 341. [Regime Boundary Alignment for Evidence-Gated Question Answering](https://arxiv.org/abs/2609.37491)

**<font color=#1a73e8>作者：</font>** Zeyan Li, Qirong Guo, SIyuan Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented language models are expected to answer from the retrieved evidence, but in practice they often keep answering when that evidence is missing. We trace this behavior to the training signal: answer-focused fine-tuning assigns no target to unsupported contexts, so it cannot distinguish a reader that abstains from one that guesses, and unsupported answering stays near 100% even as supported accuracy improves. We introduce Regime Boundary Alignment (RBA), which trains a single reader on matched variants of the same question and gold answer. The reader is trained to produce the gold answer when the context supports it, including when conflicting evidence is also present, and to abstain when the correct support is removed; inference is ordinary decoding, with no verifier, threshold, or regime label. On three multi-hop QA datasets across three seeds, RBA reduces the unsupported-answer rate by more than sixty percentage points relative to conflict-focused training while matching its supported accuracy. On a held-out TriviaQA retrieval-miss slice, the same reader reduces unsupported answering from 100% to below 1% while also improving supported accuracy. These results indicate that evidence-gated answering must be learned on both sides of the support boundary.

---


### 342. [Risk-Controlled Selective LLM Answering by Pricing Label-Free Checks](https://arxiv.org/abs/2609.37493)

**<font color=#1a73e8>作者：</font>** Dongyub Jude Lee, Jungseob Lee, Chanjun Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Serving an answer from a large language model requires deciding when to abstain, yet a verifier's ranking accuracy alone does not determine the error rate among served answers. We introduce PriceCheck, which builds a compact family of decision rules from label-free checks such as re-solving a problem. Each check has a price: its agreement rates on correct and incorrect answers and its cost per run. Prices fitted on a small, class-enriched labelled set compose into predictions of a schedule's coverage and cost, guiding which checks to run and when to stop. A calibration test then selects a schedule at a stated selective-risk target. In mathematics, the selected schedules serve 76.1% of answers on average and keep held-out selective risk below 1.5% on all 15 splits. Under the shared testing protocol, PriceCheck serves more answers at that target than reward models, a prompted judge, the generator's confidence and a trained correctness classifier. At matched coverage, it keeps the fewest wrong answers among these scorers. Across 118 diagnostic schedules, price-based coverage predictions have a rank correlation of 0.97 with observed coverage. These results show that choosing how checks are combined and stopped matters alongside how well a verifier ranks answers. Code is available at this https URL.

---


### 343. [Larry Caused the Car to Stop, But the Model Didn't Notice: Transformer Blindness to the M-Heuristic](https://arxiv.org/abs/2609.37497)

**<font color=#1a73e8>作者：</font>** Stefania Butnaru, Claudiu Creanga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern transformer models excel at capturing semantic relationships through sentence embeddings, yet their ability to perform pragmatic reasoning remains understudied. This paper investigates whether encoder-based transformers such as DeBERTa employ the M-Heuristic (the neo-Gricean principle that marked linguistic forms implicate marked meanings). We test this hypothesis by contrasting lexical causatives (e.g., ``Larry stopped the car'') with periphrastic causatives (e.g., ``Larry caused the car to stop'') using a Natural Language Inference framework. Our experiments across 188 conditions with 15 ambitransitive verbs reveal that DeBERTa, RoBERTa, and BART show no evidence of capturing the pragmatic distinction between these forms, with DeBERTa predicting ``Neutral'' for 100% of cases. Probing analysis initially suggested a representation-use dissociation, but control experiments reveal the probe was tracking syntactic complexity, not causative pragmatics. Semantic similarity over 30 triplets places periphrastic causatives closer to unmediated manner descriptions in 29/30 cases, opposite to M-Heuristic predictions in the embedding space. Under explicit metalinguistic framing, Gemini Flash-Lite reaches 100% with item-specific traces, so the principle is available under instruction yet unused in default NLI.

---


### 344. [The Rashomon Wikipedia: A Data-Perspectivist Analysis of Divergent Historical Narratives](https://arxiv.org/abs/2609.37498)

**<font color=#1a73e8>作者：</font>** Claudiu Creanga, Liviu P. Dinu, Anca Dinu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Wikipedia aims to provide a unified, neutral record of history, yet its independent language editions often function as distinct epistemic communities, creating divergent narratives around contested events. This paper investigates cross-lingual historiographical bias by analyzing Wikipedia articles across five languages (Romanian, Hungarian, Russian, Turkish, and English) focusing on three contentious events in Romanian history: the Battle of Posada (1330), the Soviet occupation of Bessarabia (1940), and the Night Attack at Targoviste (1462). Using human annotators and Large Language Models (LLMs) to classify citation stance and quantify narrative evolution from 2005 to 2024, we identify a phenomenon of "citation isolation". In the case of the Battle of Posada, only 2 out of 119 citations were shared between language editions, with the Romanian edition exhibiting a 91% pro-national bias compared to the balanced Hungarian edition. Longitudinal analysis reveals that these narratives are volatile and responsive to contemporary geopolitics, evidenced by a significant shift in the Russian framing of Bessarabia in 2024. Finally, we propose a "Peace-Maker" pipeline to automate conflict reconciliation. We demonstrate that while standard prompting leads models to hallucinate consensus, "adversarial" prompting, which explicitly instructs the model to preserve and attribute disagreement, achieves near-perfect neutrality scores.

---


### 345. [Who Warmed the Archives? LLMs Overestimate Historical Warmth](https://arxiv.org/abs/2609.37499)

**<font color=#1a73e8>作者：</font>** Claudiu Creanga, Liviu P. Dinu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Historical archives are an under-used source for extending the instrumental climate record backward in time, and LLMs offer a way to extract the indices climatologists derive by hand. Beyond measuring how well systems extract this signal, we check whether their errors are safe to use for cross-century comparison, since a good correlation score does not rule out systematic, era-linked bias. Comparing lexical baselines, fine-tuned historical transformers, and LLM prompting on the Pfister temperature index across five centuries of German text, lexical methods beat every fine-tuned transformer we test, including one pretrained from scratch on historical German (r=-0.016). All six LLMs we test (Gemini 2.5 Flash, GPT-5-mini, DeepSeek v4 Flash, Claude Sonnet 4.6, Qwen3.7-Plus, Kimi-K2.6-Fast) show a warm bias that grows with calendar year, with the same sign in every model (slopes +0.13 to +0.34/century, p<0.01). The effect is modest in size (r-squared approx equal to 0.01 to 0.05) but consistent across six independently developed models. The best-correlated of the six, Gemini 2.5 Flash, matches the best lexical correlation (r=0.32) at double the error. An ablation stripping explicit dates and calendar-era markers from the quotes leaves this trend essentially unchanged, favoring an anachronistic present-day prior over the model correctly inferring the quote's era. Correlation alone is thus insufficient for vetting an LLM as a historical-climate-index oracle.

---


### 346. [REVO: Rollout-Efficient Off-Policy Distillation via Variance-Guided Reuse](https://arxiv.org/abs/2609.37500)

**<font color=#1a73e8>作者：</font>** Yuxiao Yang, Shangzhe Li, Tianrun Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains language models using dense token-level teacher supervision on student-generated trajectories. However, its reliance on frequently refreshed student rollouts often incurs substantial generation cost. We introduce REVO, an off-policy distillation framework that improves rollout efficiency by reusing each student rollout for multi-step learner updates. REVO addresses prefix-level and current-token policy mismatch through stabilized prefix weighting and one-step resampling from the current student, which enables repeated updates without regenerating full trajectories. To prioritize informative token positions within reused rollouts, REVO uses the variance of the student-teacher log-probability ratio to quantify the remaining token-level learning signal and guide repeated optimization. Across multiple student-teacher scales, REVO with only 50 rollout iterations matches or exceeds OPD baselines trained for 200 iterations on both in-domain and cross-domain reasoning benchmarks.

---


### 347. [Evaluating Bounded Autonomy in Regulated Agentic AI: A Diagnostic Harness with Constitutional Rewards, Escalation Labels, and Runtime Governance](https://arxiv.org/abs/2609.37501)

**<font color=#1a73e8>作者：</font>** Dipankar Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose RegLLM, a diagnostic harness for bounded autonomy in regulated agentic workflows. It instruments six trustworthiness signals: citation validity, source grounding, schema compliance, escalation correctness, constitutional alignment, and unsafe-action rate. Signals are distinguished by their source of supervision: programmatic verifiers, task-level escalation labels, or AI-judge scores. A deterministic runtime supervisor blocks ungrounded answers and forces escalation, logging interventions. The same domain constitution informs evaluation, training rewards, and serving guardrails. Task-level should-escalate labels make the act-versus-defer decision a measurable training signal. We demonstrate the harness at smoke scale. An offline reference run (n=12) lifts escalation recall from 0 to 0.67 and reduces unsafe-action rate from 0.33 to 0.08 when governance is enabled. Two single-GPU Qwen2.5-3B LoRA/DPO pilots (n=8, same seed and evaluation split) expose substantial variation: nominally identical RL-base configurations yield task success of 0.25 versus 0.12 and escalation recall of 1.0 versus 0.5. An answer-quality adapter changes recall from 1.0 to 0.5 in Run A, but from 0.5 to 1.0 in Run B. An escalation-aware variant produces no measurable change in Run B. These small pilots do not establish reliable adapter effects or production readiness. Their contribution is diagnostic: configuration variance can overwhelm apparent tuning effects on bounded-autonomy metrics, motivating larger evaluation sets and repeated runs.

---


### 348. [From Dissonance to Orchestration: Teacher Intervention in On-Policy Distillation](https://arxiv.org/abs/2609.37510)

**<font color=#1a73e8>作者：</font>** Yuhao Wang, Ruiyang Ren, Yinan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own reasoning trajectories using feedback from a stronger teacher. Teacher interventions can improve these trajectories, but also change the distribution on which the student learns. Our controlled studies show that rollout quality alone is an incomplete criterion for allocating teacher guidance. Deeper intervention yields diminishing gains in rollout accuracy while increasing off-policy load. In a training probe with a restricted rollout horizon, peak student accuracy and performance retention favor different intervention strengths. The preferred intervention depth and placement also vary across benchmarks. These findings motivate MAESTRO, which uses local policy disagreement to jointly adapt when the teacher takes over and how long it generates. Its {policy disagreement score} combines teacher-weighted candidate coverage with local distribution similarity and is aggregated within reasoning paragraphs. Across eight mathematical reasoning benchmarks, MAESTRO achieves the highest macro-average accuracy among the compared methods for both 0.6B and 1.7B Qwen3 students, with the 1.7B student leading on every benchmark. MAESTRO also reduces average training response length by 67.3\% relative to standard OPD. The code is available at this https URL.

---


### 349. [Hierarchical Compression of Vision-Language Model Benchmarks](https://arxiv.org/abs/2609.37515)

**<font color=#1a73e8>作者：</font>** Hyunjong Ok, Seunggu Kang, Jaeho Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Thorough evaluation of vision-language models (VLMs) has become prohibitively expensive, as benchmarks span an ever-broader spectrum of capabilities and new models arrive at a relentless pace. Benchmark compression methods that preserve model rankings at a fraction of the cost are well studied for language models, but for VLMs the question remains under-explored. We present PRIMEBench (Pruning Redundant Items for Multimodal Evaluation), a vision-aware hierarchical benchmark compression framework that substantially reduces evaluation cost while preserving model rankings. This hierarchical framework operates in four stages: data cleaning to remove items answerable without the image and all-correct items, category representative selection to pick one benchmark per capability category, item pruning with Vision-Aware Variance (VAW), and category-count pruning. VAW combines inter-model variance with a vision-dependence score computed from multimodal embeddings alone, while encouraging coverage of diverse items within each benchmark. On models held out from item selection, it has the highest mean fidelity at the released 5% retention. The hierarchical design lets practitioners stop at any stage to match their compute budget; the released suite removes over 97% of items while preserving model rankings. Beyond compression, our analyses show how VLM evaluation behaves as model panels grow and evolve, providing guidance for designing future benchmarks that are more efficient, robust to model turnover, and explicit about the limits of evaluation-side pruning.

---


### 350. [Graph-Conditioned On-Policy Agent Distillation from Off-the-Shelf Teachers](https://arxiv.org/abs/2609.37522)

**<font color=#1a73e8>作者：</font>** Xiaohan Yi, Wen Luo, Yani Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains compact language agents with teacher feedback on student-generated trajectories. In multi-turn tasks, compounding errors can move students beyond the teacher's effective supervision. We introduce Graph-Conditioned On-Policy Agent Distillation (GC-OPD), which enriches an off-the-shelf teacher's scoring context with execution evidence. A graph indexes repeated teacher executions by shared states while preserving complete successful and failed histories. After each student episode, GC-OPD retrieves current-state references or historical alternatives and combines them with student hindsight to score the original thought-action tokens. Using the same original teachers, GC-OPD improves mean success over vanilla OPD from 24.70% to 48.78% on ScienceWorld (4B student), from 53.36% to 85.26% on ALFWorld Unseen, and from 29.10% to 37.65% on WebShop. At matched student sizes, it also achieves higher mean success than every evaluated OPD baseline using GRPO-trained teachers on ScienceWorld and ALFWorld; the strongest such ScienceWorld 4B baseline reaches 46.66%. GC-OPD requires no task-specific teacher optimization.

---


> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

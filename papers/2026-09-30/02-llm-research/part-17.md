# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**801-850**（第 17/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | **801-850** | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 801. [Beneath the Tokens: A Performance Engineering Study of Multi-Token Prediction in GPU-Accelerated LLM Inference](https://arxiv.org/abs/2609.35188)

**<font color=#1a73e8>作者：</font>** Suwesh Prasad Sah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoregressive large language model inference repeatedly invokes the target model to generate one token at a time, making generation sensitive to GPU memory movement and sequential execution. This study evaluates two-token multi-token prediction (MTP) against autoregressive decoding in a controlled single-request deployment on an NVIDIA A10G GPU. A 360-request benchmark covered plain-text, reasoning-intensive, and tool-calling workloads, while runtime telemetry, Nsight Systems, PyTorch Profiler, and selected Nsight Compute measurements were used to explain the observed performance. MTP increased output throughput by \(1.91\times\) to \(2.19\times\) across all prompts and reduced time to first output by 10.0--14.2\%. Median mean acceptance length ranged from 2.370 to 2.595 tokens per verification iteration. Profiling showed that MTP introduced a longer and more complex execution path, including proposal, sampling, attention, gathering, and reduction operations. However, it required 56.4--78.1\% fewer executions of the selected repeating CUDA Graph per generated token. The dominant MTP GEMM kernel was not faster than the dominant autoregressive GEMV kernel, and selected instances of both approached the A10G memory-bandwidth limit. These results show that MTP improved inference through amortization: greater token progress reduced repeated GPU execution sufficiently to outweigh the additional speculative-execution cost.

---


### 802. [ConRAG: Lightweight inference of multi-hop relations](https://arxiv.org/abs/2609.35193)

**<font color=#1a73e8>作者：</font>** Kilian Bänziger, Sonia Laguna, Markus Kreft 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how two entities are connected often requires tracing multi-hop relations across documents to identify intermediate entities and supporting evidence that explain a connection. This is a task that appears frequently in scientific research and other knowledge-intensive analyses. We formalise this setting as multi-hop relation inference: given two known endpoint entities, we aim to recover the bridge entities and evidence-grounded reasoning chains that connect them across a document corpus, and to generate an explanation grounded in the retrieved evidence. Existing multi-hop RAG systems typically seek an unknown answer entity rather than explicitly recovering the connection between two known endpoints and graph-based approaches often rely on costly LLM-extracted knowledge graphs that limit scalability to large document collections. We introduce ConRAG, which builds a lightweight entity-document graph from entity co-occurrence and LLM-based entity filtering. Its connective retrieval infers and semantically ranks paths between two endpoints. On MuSiQue and 2WikiMultiHopQA, ConRAG consistently improves bridge entity and reasoning chain recovery over strong RAG baselines, while reducing graph-indexing token cost by up to roughly 1.5 orders of magnitude. Our results show that endpoint-constrained path retrieval provides an effective and index-efficient approach to evidence-grounded relation discovery.

---


### 803. [Trajectory-Level Security Debt in LLM Coding Agents](https://arxiv.org/abs/2609.35199)

**<font color=#1a73e8>作者：</font>** Prateek Kumar Rajput, Abdoul Kader Kabore, Yewei Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM coding agents can traverse hundreds of intermediate code states before submitting a solution. Evaluating only the final artifact leaves the evolution of security findings unmeasured. We introduce the Security Debt Line Integral (SDLI), which accumulates static-analysis risk when an agent reaches a new best test pass ratio. We instantiate it with four static application security testing (SAST) tools and study artifacts from 830 passing SWE-bench runs, 712 ProgramBench final workspaces, and 13 public MirrorCode trajectories. The two large populations use the final-state special case of SDLI. Two-tool Common Weakness Enumeration (CWE) class agreement occurs in 3.9% of SWE-bench runs and 26.2% of the 80 ProgramBench runs passing at least 90% of official tests. These are scanner findings, not validated vulnerability rates. Excluding three advisory-heavy classes reduces the latter rate to 6.2%. Same-task runs differ in their measured scores, while one reconstructed ProgramBench run exposes persistent findings from its first implementation write. A repair case study reduces the scanner signal while preserving tested behavior, but also reveals sensitivity to equivalent API rewrites. SDLI offers a way to study progress and security findings together. Its value for steering agents and confirming exploitable vulnerabilities remains to be established.

---


### 804. [From Normative Frameworks to Alignment Data: Constructing and Evaluating SFT and Preference Data](https://arxiv.org/abs/2609.35201)

**<font color=#1a73e8>作者：</font>** Husrev Taha Sencar, Rezart Beka, Danish Naeem 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aligning language models with a specified normative framework requires translating abstract principles into concrete examples and preference signals from which models can learn. We present an expert-driven methodology for constructing such alignment data and apply it to a normative framework grounded in Islamic ethical, theological, and jurisprudential traditions. Over approximately one year, seven domain experts systematically probed language models to identify alignment deficiencies, curated desired responses, and constructed preference pairs from model outputs and expert judgments. The resulting Arabic-English datasets contain approximately 2.8K supervised fine-tuning (SFT) examples and 5.4K preference pairs spanning a broad range of normative domains. We evaluate the datasets through controlled post-training experiments comparing a Baseline model with models incorporating the curated SFT data alone and both the SFT and preference data. In blind expert evaluation on 150 separately constructed prompts, the model trained with the curated SFT data was preferred over the Baseline in 51.3% of assessor judgments, compared with 14.4% in the opposite direction (p < .001 at the prompt level). Adding the preference data resulted in a smaller difference, with the model trained with both datasets preferred over the SFT model in 28.0% of judgments versus 20.9% in the opposite direction; this difference was not statistically significant at the prompt level (p = .166). Standard Arabic and English benchmarks show no broad degradation in general-purpose capabilities. These results demonstrate how expert-defined normative principles can be systematically operationalized into alignment data and evaluated through controlled model training.

---


### 805. [Understanding On-Policy Distillation: A Mechanistic Interpretability Perspective via Sparse Crosscoders](https://arxiv.org/abs/2609.35210)

**<font color=#1a73e8>作者：</font>** Zichao Yu, Qianshuo Ye, Xu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is a widely adopted post-training technique for LLM reasoning. It is commonly believed to transfer knowledge from a stronger teacher, yet what OPD actually distills into the student's internal representations remains unclear. We study this question with sparse crosscoders, which learn one feature dictionary shared by the student before and after OPD and the teacher. Standard crosscoder analyses, however, identify model-specific features but cannot tell how a model's use of its features changes, since all models are encoded into one set of feature activations. We therefore propose the swap readout, which reads each student checkpoint's feature activations on its own, measuring how training changes the student's use of each feature, even for checkpoints unseen by the crosscoder. Across three OPD settings, we find that OPD neither creates features nor passes on the teacher's own, and leaves the firing rates of over 98% of the student's frequently used features within 20%. We further examine the SFT warm-up on the teacher's rollouts that commonly precedes OPD and makes it more effective. Rather than adding features, the warm-up reweights the shared ones in two ways. First, it already raises and lowers many of the features that OPD later raises and lowers, doing part of OPD's work in advance. Second, it changes features that OPD alone would not, notably those for conversation format, reasoning style, and mathematical notation, and these changes persist through OPD. Imposing this reweighting on a directly distilled student's features, without changing its weights, brings its accuracy close to that of the warmed-up student, whereas the same change on shuffled features does not. Together, these findings suggest that OPD reweights existing features rather than acquiring new ones: the student learns from the teacher how to use the features they already share.

---


### 806. [ASCT: Attentive Search over Counterfactual Trees for Credit Assignment in Agentic Reinforcement Learning](https://arxiv.org/abs/2609.35215)

**<font color=#1a73e8>作者：</font>** Yang Li, Jinhan Yang, hai liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Terminal utility evaluates a complete agentic workflow, but learning requires credit for the decisions within it. We introduce Attentive Search over Counterfactual Trees (ASCT), a framework that turns training-time multi-step search into local action credit. At actor-visited states, an auxiliary tree evaluates alternative legal actions from the same recoverable prefix. Its action-value table is centered by the frozen actor's probabilities and supplies credit for PPO on actor-sampled trajectories. This protocol connects counterfactual evaluation to policy learning while deploying the actor alone. Uniform, UCT, and cost-aware AgentUCT instantiate the framework. On HotpotQA agentic retrieval-augmented generation, all three improve mean held-out utility over trajectory-return PPO and workflow-adapted VinePPO. Across three seeds, ASCT-AgentUCT reaches 0.6187 utility versus 0.5939 for VinePPO, with gains in answer F1 and execution cost, and uses 50.3% fewer recorded auxiliary Qwen tokens. Transfer and component-description studies examine the learned policies beyond the training setting.

---


### 807. [SignFLIP: A Unified Model for Sign Language Translation and Generation via Stage-wise Alignment at Scale](https://arxiv.org/abs/2609.35225)

**<font color=#1a73e8>作者：</font>** Zhaoyi An, Sihan Tan, Youngbae Hwang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign language translation and generation share the goal of bidirectional alignment between text and sign representations. However, existing approaches either treat them as isolated tasks or are only verified on limited datasets, limiting effective modeling between modalities. In this paper, we propose SignFLIP, a unified LLM-centered framework for translation and generation. To enable bidirectional mapping between text and sign, SignFLIP adopts a symmetric architecture together with a stage-wise training strategy built on large-scale data. The shared sign--text representation is progressively refined: pre-alignment facilitates subsequent SLT, while the SLT-adapted representation further benefits SLG. Extensive experiments on multiple benchmarks show that SignFLIP shows competitive performance compared with task-specific models on both translation and generation tasks, as well as strong transferability to sign language recognition.

---


### 808. [Generative AI-Based Data Augmentation for Oral Lesion Classification: The PhotoMOCI Dataset and Benchmark](https://arxiv.org/abs/2609.35226)

**<font color=#1a73e8>作者：</font>** Marco Parola, Mario G.C.A. Cimino, Sabrina Senatore  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early detection of oral cancer via photographic imaging presents a promising avenue for large-scale oral cavity screening. However, the development of robust deep learning models is frequently hampered by the scarcity of high-quality, annotated datasets. To address this limitation, a novel and well-curated resource, the Photographic Multi-purpose Oral Cancer Imaging (PhotoMOCI) dataset, is introduced for developing models across multiple diagnostic tasks in oral oncology. Then, a comprehensive benchmark study was conducted to investigate how various data augmentation strategies influence the performance of image classifiers. Our analysis spans different generative AI frameworks, evaluating the efficacy of traditional methods against advanced generative approaches, including Generative Adversarial Networks (GANs) and Diffusion Models (DMs). Additionally, we propose the Synthetic Image Filter (SIF), a mechanism to select specific samples based on two auxiliary models: Synthetic Proxy Classifier to ensure samples are representative of the target class and Synthetic Image Detector to verify they appear realistic, thereby selecting only the high-utility images that contribute to improving downstream performance. Across the evaluated datasets and classifiers, the best SIF-filtered setup improves accuracy over traditional augmentation in all cases, with gains of +1.73% and +2.35% on PhotoMOCI and +2.38% and +2.08% on KOCD for ResNet50 and ViT, respectively. Our findings reveal that while the direct application of generative data augmentation may yield performance drops, the integration of SIF, considering (i) how synthetic data looks real and (ii) how it reflects the discriminative features of the belonging class, provides a simple yet effective mechanism to filter out synthetic samples that confuse the classifier during training.

---


### 809. [Token-Disentangled Latent Test-Time Scaling for Vision-Language Reasoning](https://arxiv.org/abs/2609.35228)

**<font color=#1a73e8>作者：</font>** Hao-Xuan Ma, Yihao Liu, Yutao Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent test-time scaling improves reasoning by refining hidden states during inference, but existing methods typically apply a single scalar reward to all editable latent tokens. For multimodal large language models, this global update ignores that generated tokens play different roles: some are sensitive to visual evidence, while others correspond to uncertain reasoning decisions. We present Token-Disentangled Latent Test-Time Scaling, an inference-time framework that makes latent refinement token-role-aware. Starting from an initial generated trajectory, we optimize a short hidden-state prefix while routing perception-side visual feedback to image-sensitive tokens and reasoning feedback to high-entropy tokens. Tokens selected by neither route are constrained by an anchor regularizer. Across both perception and reasoning benchmarks on Qwen2.5-VL-7B and InternVL3.5-8B, our method lifts macro accuracy over CoT by +2.57 and +1.51 respectively, and outperforms strong output-space test-time scaling baselines under matched decoded-candidate budgets. Code is available at this https URL.

---


### 810. [Beyond Selection: Token Parameterization for Extreme Visual Token Compression](https://arxiv.org/abs/2609.35232)

**<font color=#1a73e8>作者：</font>** Rui Zhong, Yu Li, Zheyu Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual-token compression is effective for improving the efficiency of vision-language models, but under extreme compression budgets, token pruning can break visual grounding while learned resamplers increase parameter count, attention cost, and training complexity. We revisit compression through a token parameterization lens, separating (i) basis transformation and structured truncation (retained subspace/compressibility) from (ii) coordinate organization (optimization and cross-modal alignment). This view yields two coupled objectives, compressibility and learnability, which we formalize as unified functionals. Guided by these objectives, we design Braco, a lightweight four-step coder that combines transform-basis truncation, input-independent basis-coordinate embeddings, budget-dependent orthogonal re-parameterization, and learned spatial residual tokens from lightweight pooling. Experiments show that Braco forms the favorable empirical accuracy-efficiency frontier under $23\times$--$64\times$ compression and remains competitive at $144\times$, reaching 95.2% accuracy while reducing prefill FLOPs by 84.2%--86.7% relative to the uncompressed upper bound. Against prior methods, Braco matches or improves accuracy while achieving up to approximately 36% end-to-end speedup and using $16.6\times$/$78.8\times$ lower compressor latency/FLOPs.

---


### 811. [EP-Mem: Elastic Privacy Memory for Social Relationship-Aware LLM Agents](https://arxiv.org/abs/2609.35233)

**<font color=#1a73e8>作者：</font>** Fengzhou Sun, Yuan Zhang, Xintong Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents face critical privacy risks when acting as delegates in human-agent-human communication. To prevent such breaches, agents must understand users' social relationships and adhere to context-dependent social information disclosure boundaries. Current studies on agent memory privacy focus on instantaneous interactions, leaving the long-term relational disclosure problem unexplored. In this paper, we propose EP-Mem, an Elastic Privacy Memory architecture that reframes privacy as user-owned boundary control across social roles. EP-Mem introduces (1) token-level memory driven by user-configurable a privacy policy that stratifies persons and events, combining domain-level default circulation rules with fact-level whitelist/blacklist exceptions; and (2) a pluggable sidecar with a privacy engine that aligns disclosure controls with memory across summary, detail, and boundary granularities, enforced throughout generation, storage, and retrieval. We construct EP-Bench, to our knowledge the first long-term multi-party benchmark with cross-session correlated events for policy-conditioned relational disclosure. Experiments show that EP-Mem achieves 94.0% privacy classification accuracy, improves disclosure-permission judgment from 22% to 68%, and reduces privacy leakage by 75.6%, while maintaining retrieval performance and cross-benchmark generalization.

---


### 812. [DrawingsDreamer: A Unified Multi-View Engineering Drawings Generation Model](https://arxiv.org/abs/2609.35242)

**<font color=#1a73e8>作者：</font>** Shurui Liu, Weide Chen, Changwang Yi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scalable Vector Graphics (SVG) are essential for modern industrial Computer-Aided Design (CAD). However, existing autoregressive SVG generation models are predominantly tailored for artistic creation and struggle to maintain the rigorous geometric fidelity and cross-view spatial alignment required for engineering drawings. To bridge this gap, we introduce \textbf{DrawingsDreamer}, a unified Large Language Model (LLM)-driven framework for multi-view vector-based engineering drawings generation. By formulating the generation of multi-view engineering drawings purely as a sequence modeling task, we eliminate the need of raster image encoders. We propose a Streamlined Representation utilizing hierarchical postfix tokenization, which guides the model to establish local geometric coordinates before assigning semantic boundaries. Optimized via a progressive task-aware curriculum schedule, \textbf{DrawingsDreamer} effectively transitions from localized structural repair to macroscopic generation in a unified model. Extensive experiments demonstrate that our unified model achieves strong performance in both geometric fidelity and syntactic accuracy across diverse conditional and unconditional generation tasks.

---


### 813. [AnswerMap: Faithful Spatial Interpretability of VLMs from Answer Posteriors](https://arxiv.org/abs/2609.35247)

**<font color=#1a73e8>作者：</font>** Mohamed Eltahir, Fardows Adam, Duaa M. Tahir 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a VLM answers a visual query, current interpretability tools rely on text rationales, which use a mismatched modality, or on internal read-outs, which originate too early to reflect the final output and require white-box access to the model. We introduce AnswerMap, a training-free, task-agnostic, black-box visual rationale constructed from the output head. The image is cut into K row and K column bands, each shown alone to the frozen model along with the query in the format of a yes/no relevance question. The outer product of the row and column ``yes'' posteriors gives the query-conditioned spatial map. Crucially, by defining a fixed read-out R (e.g., expectation, maximum) on top of AnswerMap, we can derive continuous outputs like location natively. This bypasses the reliance on discrete text tokens for continuous-output tasks and guarantees an image-dependent answer by construction. However, a rationale can be confabulated, so we validate AnswerMap across four models and three query distributions with two tests: (a) agreement with the model's own generated point and (b) deletion of the map's region. The map lands where the model points (AUC 0.85 against 0.38 for attention), and deleting its region flips 53% of correct answers (against 19% for attention's). Beyond establishing faithfulness, we demonstrate the map's task-agnostic utility through three distinct read-outs: its maximum flags hallucinated objects without generation, its expectation localizes correctly when the model's own pointing fails, and its top-mass region, fed back as a crop, fixes half of the model's wrong answers. AnswerMap thus offers a new lens on VLM interpretability and, through its read-outs, a new output interface for visual tasks beyond text tokens.

---


### 814. [SCBO: Semantically Coherent Batching and Ordering for LLM-Based Social Surveys](https://arxiv.org/abs/2609.35250)

**<font color=#1a73e8>作者：</font>** Yuanzi Li, Lingjie Wang, Zihang Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) offer a scalable way to simulate survey respondents using demographic profiles and observed reference responses. However, the conventional approach of predicting one question per prompt repeatedly encodes the same context, limits each target to a narrow set of reference responses, and prevents later predictions from using information in earlier answers. Predicting multiple questions in one prompt can reduce these costs, share a broader pool of references, and let later predictions build on earlier ones. This requires forming coherent batches, selecting shared references, and ordering questions and references effectively. We propose Semantically Coherent Batching and Ordering (SCBO), a training-free framework that addresses these challenges. SCBO first uses an LLM to extract compact semantic representations from survey items and filter out template noise. It then groups related questions into batches and builds a shared reference bank using target-specific retrieval and centroid-based completion. Finally, it orders target questions from easy to hard and arranges references according to their semantic alignment with those questions. Experiments on four large-scale survey datasets and four LLMs show that SCBO substantially reduces token consumption and inference time while generally improving prediction accuracy over a non-batched baseline. Code is available at this https URL.

---


### 815. [Towards Reliable AI Data Scientists: Data Agents with Workflow Harnesses](https://arxiv.org/abs/2609.35255)

**<font color=#1a73e8>作者：</font>** Huachi Zhou, Yujing Zhang, Jiahe Du 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly deployed for data-intensive work, yet reliable data analysis requires more than general-purpose reasoning and ad hoc tool augmentation. Data Agents, equipped with workflow harnesses, offer a promising paradigm for automating the end-to-end data science lifecycle. This paper examines Data Agents from a harness-centric perspective. First, we introduce a taxonomy of Data Agents and associated data environments, organizing the literature around five functional stages: perception, planning, execution, verification, and repair. Second, we analyze the key technical routes within each stage, identifying 15 distinct approaches ranging from data structure probing to data state reconstruction. Third, we identify four open reliability problems: inactive semantic calibration, missing clarification, missing experience transfer, and the missing verification-repair repository. These problems explain why silent failures can persist even when individual components function correctly, highlighting the need for rigorous workflow harnesses and shared reliability resources. Finally, we summarize the horizontal task families of Data Agents, examine their vertical application settings, and benchmarks for evaluation, while maintaining a companion repository at this https URL.

---


### 816. [AIM-ZO: Activation-Informed Subspace Maintenance for Zeroth-Order LLM Fine-Tuning](https://arxiv.org/abs/2609.35257)

**<font color=#1a73e8>作者：</font>** Yue Xie, Zhi Zheng, Yunpeng Ba 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) optimization offers a memory-efficient alternative for LLM fine-tuning by estimating updates only from forward evaluations of perturbed parameters, without backpropagation or activation storage. However, in billion-parameter LLMs, isotropic perturbations often waste many forward evaluations on weakly informative directions. To make these evaluations more informative, existing ZO methods restrict perturbations to low-dimensional subspaces. Yet the quality of these subspaces is critical: overly compressed or poorly maintained spaces can miss useful update directions. To obtain a high-quality subspace for ZO updates, this paper proposes AIM-ZO, a ZO fine-tuning method based on Activation-Informed Subspace Maintenance. AIM-ZO uses forward activations as local directional information and continuously integrates them into a broad, evolving subspace over training. To access broader gradient-relevant structure while keeping individual perturbations low-dimensional, AIM-ZO activates only a smaller set of shared and sampled directions, decoupling the maintained width from the active width. We evaluate AIM-ZO across 5 LLMs and 11 downstream tasks under matched forward-evaluation budgets; its six-task average exceeds the strongest fully evaluated ZO baseline by 1.26 percentage points on OPT-2.7B and MeZO by 2.85 percentage points on OPT-30B. Our code is available at this https URL

---


### 817. [On-Policy or Off-Policy Learning? A Systematic Study of Distillation Dynamics](https://arxiv.org/abs/2609.35259)

**<font color=#1a73e8>作者：</font>** Julianna Piskorz, Antonin Berthon, Mihaela van der Schaar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy learning has been argued to reduce catastrophic forgetting, produce sparser parameter updates, and improve generalisation. However, existing comparisons between supervised fine-tuning and reinforcement learning vary many factors simultaneously, making the contribution of rollout policy difficult to isolate. We study the effect of rollout policy in a controlled strong-to-weak distillation setting, by independently varying rollout policy, token-level KL direction, and learning rate across the Llama3 and Qwen2.5 model families and reasoning tasks spanning scientific, medical, and arithmetic domains. Our analysis reveals a nuanced picture of distillation dynamics in which rollout policy does not necessarily play a central role. Instead, token-level KL direction more clearly shapes task performance and output coverage, while learning rate governs forgetting and update sparsity. Analysis of KL gradients and experiments along a continuous student-teacher rollout-policy spectrum explain this pattern: forward KL is remarkably robust to rollout policy, with its performance stable and strong despite changes to the rollout policy, whereas reverse KL is substantially more sensitive and favours student-generated rollouts. On-policy data nevertheless improves generalisation to harder variants of the Countdown arithmetic task under both KL directions, although this advantage does not reliably persist after subsequent RLVR. Our broader conclusions remain robust to removing gradient clipping, using sampled KL estimators, and training on tasks requiring longer reasoning chains. Overall, our results challenge the view that on-policy rollouts are inherently preferable and show that their value depends critically on the objective, evaluation setting, and optimisation hyperparameters.

---


### 818. [Imprint Reader: From Weight-Update Readout to Behavioral Intervention](https://arxiv.org/abs/2609.35261)

**<font color=#1a73e8>作者：</font>** Guanxu Chen, Qihao Lin, Jing Shao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As language models take a growing role in AI development, a natural aspiration is for them to reflect on their own learning process, as humans do, and use that reflection to improve themselves. At the same time, these models have an advantage that human learners lack, since training leaves parameter-level traces that can, in principle, be inspected directly. However, current models cannot decode these traces into an explicit account of what they have learned. To this end, we introduce the \textit{Imprint Reader}, a model trained with \textit{Semantic Mount-and-Read Tuning} (SaRT) to describe frozen weight updates. SMaRT mounts each update onto the Reader and uses an anchor-free meta-query to elicit a natural-language description, while no-change and random-perturbation controls discourage unsupported claims. On held-out updates, the joint Reader reaches judge-based Pass@100 of $2\%$ for knowledge and $16\%$ for behavior. These results demonstrate the feasibility of natural-language readout while pointing to reliability across updates as the next step. Beyond free-form generation, the Reader provides a differentiable proxy for the gap between a specified target behavior and a candidate weight update. Its coordinate-aligned gradients support intervention through MetaEdit. At a $0.5\%$ pruning rate, Reader-guided selection raises measured harmful-prompt refusal from $57.9\%$ to $64.1\%$ under a safety-maintenance target. Using behavior descriptions without target-task training data, MetaEdit increases the frequency of backtracking and sub-goal expressions in mathematical reasoning traces and raises BFCL Overall from $41.69\%$ to $44.60\%$.

---


### 819. [Rubric-Aware On-Policy Self-Distillation for LLM Personalization](https://arxiv.org/abs/2609.35262)

**<font color=#1a73e8>作者：</font>** Yilun Qiu, Xiaoyan Zhao, Chengbing Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM personalization aims to generate responses aligned with individual users' preferences and needs. User-specific rubrics make these expectations explicit, providing direct supervision on what a satisfactory answer should cover. Existing rubric-guided approaches, however, exploit such guidance only at a coarse granularity, either by using rubrics to supervise the prediction of relevant aspects for subsequent generation or by reducing aspect coverage to a single response-level reward for reinforcement learning. This leaves a gap between specifying what a personalized answer should contain and teaching the model how to generate it. To bridge this gap, we propose GRASP, a rubric-aware on-policy self-distillation framework for LLM personalization that turns user-specific rubric aspects into fine-grained, token-level supervision. Specifically, GRASP pairs a rubric-free student with a rubric-informed teacher that additionally receives the target user-specific rubrics. By aligning their next-token distributions along on-policy trajectories generated by the student, GRASP transfers the teacher's rubric-conditioned guidance into the student, translating user-specific semantic requirements into dense token-level supervision. Since rubric-informed teachers can still produce inadequate supervision, we further introduce Rubric-based Teacher Validation (RTV), which retains only instances where the teacher sufficiently covers the target aspects, improving both supervision quality and training efficiency. Experiments on the LaMP-QA benchmark for personalized question answering demonstrate that GRASP achieves state-of-the-art performance across multiple backbones, supporting the effectiveness of rubric-guided token-level supervision for personalization. To ensure reproducibility, our code is available at this https URL.

---


### 820. [Continuous Assurance of Agentic Security Auditors for Software Delivery Decision Gates](https://arxiv.org/abs/2609.35266)

**<font color=#1a73e8>作者：</font>** Guy Lupo, Nguyen Hung Nguyen, Viet Vo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based repository auditors are increasingly deployed as security controls within continuous integration (CI) pipelines, where their findings admit, block, or delay software changes. As Agentic Software Development Life Cycle (SDLC) Security Controls, their non-deterministic behaviour changes the evidence, while organisational risk appetite and jurisdictional or data-sovereignty policy change its interpretation. Point-in-time audits therefore cannot maintain current assurance for merge decisions.
We propose the Policy-Evidence-Execution Separation Pattern, implemented by the Trustworthy AI Posture (TAIP) Assurance Engine and operated as Continuous Control Posture Assurance (CCPA). By separating policy from stable execution and binding admitted evidence to a versioned Posture Tree, the same assurance logic operates across models, environments, and policy profiles.
We evaluate the approach using unmodified RepoAudit on a fixed Python Null Pointer Dereference benchmark. The retained evidence repository contains 80 RepoAudit executions across two OpenAI model configurations, gpt-4o-mini and gpt-4.1. TAIP recomputes assurance posture after policy, evidence, and model-context changes and is evaluated across increasing numbers of independent Decision Gateway contexts. The maximum observed policy-to-posture latency was 1.1 ms across three policy-class cycles in one execution. At 1,000 independent assurance contexts, full policy-triggered recomputation with one worker recorded a maximum aggregate refresh of 1.62 s, below the predeclared 5 s Decision Gateway budget. These single-host measurements concern assurance over retained evidence and exclude RepoAudit execution and provider inference.

---


### 821. [When Words Speak Louder than Images: Towards Understanding Language Bias in Vision-Language Models](https://arxiv.org/abs/2609.35272)

**<font color=#1a73e8>作者：</font>** Yizhou Fang, Siyue Chen, Zimo Qi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite substantial progress across downstream applications, vision-language models (VLMs) remain susceptible to language bias, often prioritizing linguistic cues over visual evidence and consequently producing incorrect predictions. Prior studies have proposed various approaches to understanding and mitigating language bias in VLMs, yet their findings often conflict due to the difficulty of tracing how language bias propagates within black-box VLMs. Building on the word completion task, we trace how language bias propagates through VLM inference by (1) proposing a diagnostic framework that decomposes the inference process into four distinct yet interdependent stages to trace the propagation of language bias; and (2) examining how two key factors underlying language bias, i.e., linguistic priors and cross-modal coverage, evolve across these stages and ultimately give rise to incorrect predictions. The linguistic prior captures the strength of statistical bias induced by the language model component of a VLM and represents the origin of language bias, whereas cross-modal coverage measures the extent to which linguistic cues cover the visual content. By decomposing inference into four stages and characterizing the interplay between linguistic priors and cross-modal coverage across these stages, we propose a systematic framework for tracing the propagation of language bias throughout the inference process; and uncover the underlying mechanism of language bias by revealing the interplay between linguistic priors and cross-modal coverage.

---


### 822. [Measuring Collapse and Correction in Homogeneous-Panel LLM Debate](https://arxiv.org/abs/2609.35279)

**<font color=#1a73e8>作者：</font>** Xin Li, Mengbing Liu, Chau Yuen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) debate is often evaluated by whether final answers improve, but movement is not necessarily improvement: the same discussion can rescue an initially wrong majority or destroy an initially correct one. Standard final-accuracy evaluations conflate these opposing mechanisms. We introduce an auditable protocol for homogeneous debate on multiple-choice questions (MCQs) that records each run as a transition ledger over collapse, correction, onset, and signed intervention utility. On 6,925 MMLU-Pro debates, the protocol identifies 253 collapses and a parallel correction ledger that changes how interventions should be judged. Replay experiments reveal the central tradeoff: a leave-one-model-out probe-gated freeze prevents 29 collapses but loses 108 corrections under equal weights, so collapse prevention alone can recommend the wrong policy. A compact pre-debate 8-probe screen is a triage signal: its unadjusted family-level association with conditional-collapse risk is high (G=7, Spearman rho=0.893, exact two-sided p=0.0123), but initial-majority accuracy is a close comparator (rho=0.821; family partial rho=0.767, p=0.0877), so we do not treat it as calibrated or capability-adjusted prediction. Round-level traces localize many collapses to the first debate round, where early disagreement can precede both harmful cascades and useful recovery. We release replayable schemas, coders, audits, cost cards, and zero-API rebuild scripts so future model-scaffold rows can be compared under the same denominators and signed utility ledger.

---


### 823. [Textual User Taste: Natural-Language User Context for Foundation-Model Recommender System at Scale](https://arxiv.org/abs/2609.35285)

**<font color=#1a73e8>作者：</font>** Ghazal Fazelnia, Paul Gigioli, Eliza Klyce 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation model recommender systems require user context that can be consumed by large language models, reasoned over, and refined through natural-language interaction. Traditional behavioral embedding vectors remain highly effective for retrieval and ranking, but they are opaque to users and not natively expressed for language model workflows. We present Textual User Taste, a system that generates structured natural-language taste profiles from listening behavior, interaction signals, content metadata, and optional user feedback, and deploys them to millions of Spotify users. We describe the end-to-end production lifecycle required to generate, evaluate, optimize, and maintain these representations at industrial scale, including prompt development and compression, user steering, and integration with downstream personalization systems. Because no unique ground-truth taste profile exists, we introduce a multi-faceted evaluation framework to evaluate taste profiles as a production representation: they carry user-specific predictive signal independently, and when integrated with behavioral embeddings, improve MRR by 0.6% for future-track prediction and NDCG@7 by 2.2% for search ranking. Our evaluation also reveals that taste profiles support positive natural-language steering, while exposing important limitations, including challenges with negation and short-term temporal adaptation. These findings position taste profiles not as replacements for behavioral embeddings, but as an interpretable and steerable interface between evolving user context and foundation-model recommender systems.

---


### 824. [Narrow Multimodal Fine-Tuning Can Induce Emergent Misalignment](https://arxiv.org/abs/2609.35291)

**<font color=#1a73e8>作者：</font>** Shunchang Liu, Lukas Fluri, Xin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern AI models are aligned through post-training to adapt them to downstream tasks. Recent work shows that fine-tuning language models on narrow tasks can induce emergent misalignment (EM), causing broadly harmful behaviors beyond the training task. However, EM has been studied almost entirely in text-only tasks, leaving its manifestation in multimodal models unclear. In this paper, we define and analyze EM in the context of vision-language models. We first induce EM via fine-tuning on narrow multimodal tasks targeting vulnerable code, careless household-object use, and conspiratorial interpretations of ordinary scenes. Across fifteen commercial and open-source models with different scales, we find that narrow multimodal fine-tuning can induce coherent and broadly misaligned behavior that transfers to unrelated tasks, including misaligned opinions, visual factual dishonesty, unsafe image generation, vulnerability to visual jailbreaks, and risky agentic actions. We further find that multimodal EM does not depend on the apparent harmfulness of training data but is sensitive to training-evaluation modality alignment. EM can arise under both supervised fine-tuning and preference optimization and can propagate through intermediate reasoning. Finally, we explore several mitigation strategies, including prompt inoculation, benign continued training, and activation-level steering, which can partially reduce EM. Overall, our findings suggest that multimodal EM reflects a behavioral shift rather than a general loss of capability, extending beyond text to the visual modality.

---


### 825. [Decide, Don't Generate: Competitive Dimensional ABSA with Jev's Typed Decisions](https://arxiv.org/abs/2609.35293)

**<font color=#1a73e8>作者：</font>** Yiqun Zhang, Peidong Wang, Zihan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect-based sentiment analysis (ABSA) has largely turned to text generation. We show that competitive dimensional ABSA does not need it. Using Jev, a frozen model that answers typed questions with rubric scores, label probabilities, and yes/no judgments, we decompose all three tasks of SemEval-2026 Task III Track A into such decisions and align them with the annotation scheme through 488 coefficients fitted on CPU, with no text generation and no backbone tuning. On valence-arousal regression over ten corpora in six languages, the system reaches 1.0645 RMSE, the lowest aggregate error of any participating system. On triplet and quadruplet extraction, it reaches 52.09 and 44.06 continuous F1, above fine-tuned Llama-3.3-70B and GPT-OSS-120B baselines. Analyses and ablations show where the accuracy comes from: supervised calibration roughly halves the raw regression error, exact valence-arousal would add only 4.5 F1 to extraction, and the learned combination of span-boundary evidence, not any single signal, carries the extraction systems.

---


### 826. [Beyond Saying Less: Fine-Grained Alignment for Informative and Faithful Vision-Language Models](https://arxiv.org/abs/2609.35294)

**<font color=#1a73e8>作者：</font>** Xingming Long, Jie Zhang, Yuecong Min 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object hallucination remains a major challenge for large vision-language models. While off-policy preference optimization proves to be an effective solution, on-policy reinforcement learning provides a more promising direction as it directly targets a model's current failure modes. However, we find that without fine-grained reward formulation and allocation, on-policy optimization often falls into an easy shortcut: reducing hallucinations merely by saying less---making fewer valid claims. To comprehensively resolve this, we propose a fine-grained alignment framework that couples dense reward signals at the data level with precise credit assignment at the algorithmic level. Specifically, we first construct the Dense Object Presence and Absence (DOPA) dataset to address sparse annotations that prevent valid object claims from being verified and rewarded. DOPA exhaustively annotates the deterministic presence and absence of every concept across an expanded vocabulary, significantly increasing the density of reliable reward signals during on-policy rollouts. Second, we propose Subsentence-level Credit Assignment for on-Policy Optimization (SCAPO) to prevent response-level shared advantages from allowing local hallucinations to compromise all other valid outputs within the same response. By assigning credit to each subsentence independently based on its object claims, SCAPO can precisely reinforce faithful generations and penalize hallucinations. Furthermore, we leverage the resulting faithful image descriptions as auxiliary context to transfer generative gains to discriminative tasks. Experiments demonstrate that our method produces highly informative, faithful descriptions in generative tasks while yielding clear performance gains on discriminative evaluation.

---


### 827. [LionMuon: Alternating Spectral and Sign Descent for Efficient Training](https://arxiv.org/abs/2609.35297)

**<font color=#1a73e8>作者：</font>** Arman Bolatov, Artem Riabinin, Nikita Kornilov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretraining a language model takes enormous compute, and the right optimizer can save a good part of it. Muon's spectral step gives a stronger direction than a sign step, but it is expensive. Every step runs Newton-Schulz iterations on the full matrix and, in distributed training, an extra all-reduce. Sign steps, as in Lion and Signum, are cheap and stay local to each device. We propose LionMuon, which takes one Muon step every $P$ iterations and Lion steps in between, with a single dual-EMA momentum buffer shared by both. Muon's compute and communication are paid once per $P$ steps, and the optimizer state is half of AdamW's. A single-EMA variant, SignMuon, already improves on Muon. We prove complexity bounds under heavy-tailed noise in which the period sets an interpolation between Muon's and Lion's smoothness and noise constants, and which say when LionMuon is faster than both. On 124M and 355M models trained on FineWeb, LionMuon with $P=2$ and $P=5$ reaches a lower loss than Muon, AdamW, Lion and Signum at the same number of tokens. Under 4-GPU data-parallel training it reaches Muon's final loss with a third less wall-clock on PCIe, and it beats the communication-efficient Muon variants Dion and MuonBP on loss at no more exposed communication, while keeping the exact gradient. Code: this https URL

---


### 828. [Training-Free Clinical Reasoning through Medical Ontologies and Cognitive Mapping: A Symbolic-Probabilistic Knowledge Graph Framework](https://arxiv.org/abs/2609.35298)

**<font color=#1a73e8>作者：</font>** Surajit Das  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most clinical prediction systems learn patient-variable-outcome associations; we investigate a training-free diagnostic paradigm mapping patient observations to explicit medical knowledge. CKG Reasoner integrates candidate-specific Evidence Feature Nodes, patient-reference matching, a bounded Information Gate, knowledge-weighted evidence accumulation, disease similarity, and decisive clinical rules. Missing-aware normalization and coverage auditing distinguish absent from unavailable evidence. Candidate ranking is separate from outcome-label-independent K-means clustering, which uses four derived evidence coordinates (evidence strength, relative magnitude, directional similarity, and evidence completeness), not raw predictors or targets, to derive cohort-level assignments. Across six retrospective cohorts - four dengue (N = 1000, 1523, 989, 1018), malaria (N = 2190), and influenza (N = 4569) - a uniform, label-free, cohort-fitted K = 2 protocol yielded positive-class F1 scores of 0.996, 0.634, 0.936, 0.917, 0.695, and 0.842, and all-record accuracies of 0.996, 0.558, 0.914, 0.893, 0.707, and 0.906, respectively, with full partition-decision coverage using the frozen package and disease-specific knowledge representations. Neither scoring nor clustering uses outcome labels. Logistic regression provides a supervised baseline. Influenza incorporates confirmatory molecular PCR and is not independent pre-test prediction. Results characterize knowledge-grounded evidence separation, auditability, and sensitivity, not prospective clinical validity or comparative superiority. FOL/LLM-based clinical explanation remains unevaluated.

---


### 829. [Sustained Participation as a Security Resource: The Bounded Participation Channel](https://arxiv.org/abs/2609.35300)

**<font color=#1a73e8>作者：</font>** Homayoun Maleki, Nekane Sainz, Jon Legarda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Can sustained, per-identity participation be engineered into a security resource? Most anti-Sybil defenses price identity creation rather than identity survival. Once admitted, an adversary may sustain many identities without paying a recurring cost. We introduce the Bounded Participation Channel (BPC), a formal primitive for repeatedly verifying participation window by window. BPC issues fresh, identity-bound challenges under a strict deadline and enforces four structural properties: identity binding, freshness, real-time response, and bounded per-channel throughput. Together, these yield a provable cost theorem: sustaining $s$ identities over $T$ windows requires $C(s,T) \geq sT/\tau_h$ participation channel-windows. The guarantee is solver-agnostic: a channel may be operated by a human, an AI system, or a hybrid.
We give a hash-based construction with publicly verifiable participation proofs, characterize four admissible challenge families, and evaluate two against GPT-4o, Gemini 2.5 Flash, and Claude Sonnet 4.5 across 600 trials. Despite near-perfect accuracy (97--100%) on the perceptual tasks, the evaluated automated channels remain throughput-bounded under the tested deployment conditions. The results illustrate a key distinction: solvability does not imply unlimited throughput. By requiring participation to be re-earned by every identity in every time window, BPC turns sustained participation into a measurable security resource with a linear structural cost floor, independent of whether the participation is supplied by humans, AI systems, or hybrids.

---


### 830. [Narrowing the Horizon: Quantifying Topic Saliency Shifts in Generative Monoculture](https://arxiv.org/abs/2609.35302)

**<font color=#1a73e8>作者：</font>** Oriane Peter, Elena Simperl, Kate Devlin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) become central to how we access and share information, they play an increasingly powerful role in shaping global knowledge. However, as these models evolve, their outputs risk converging into a \textit{generative monoculture}, where the diversity of perspectives they represent narrows over time. Studies at the model level often fail to pinpoint which specific topics or viewpoints are being marginalised or amplified in this process. In this paper, we introduce a method to measure shifts in topic saliency across model families, tracking what gains or loses prominence during post-training. Applying this approach to a case study of climate change discourse, we demonstrate how homogenisation affects the representation of diverse solutions across different models. We also test interventions to counter this trend, showing that specialised models can help preserve a broader range of perspectives. This underscores the importance of monitoring topic saliency to diagnose the risks of monoculture and to ensure AI systems reflect a pluralism of ideas. Data and Code are accessible \href{this https URL}{here}.

---


### 831. [PIVOT: Pivot-Aware On Policy Self Distillation for Multi-Turn VLM Agents](https://arxiv.org/abs/2609.35303)

**<font color=#1a73e8>作者：</font>** Jiazhou Zhou, Hu Zhou, Yucheng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) via Group-Relative Policy Optimization (GRPO) is widely used for multi-turn VLM agent training, yet it suffers from zero-gradient silence on uniform failures and coarse episode-level credit assignment. While On-Policy Distillation (OPD) and On-Policy Self-Distillation (OPSD) mitigate sparse rewards using hindsight information, their underlying mechanisms remain poorly understood. Through controlled counterfactual rollback probes across five multi-turn VLM agent benchmarks, we reveal that performance gains in OPSD/OPD are largely driven by physical state rollback at the pivot step, defined as the first unrecoverable action without remaining step budget. However, physical state rollbacks are computationally prohibitive and infeasible in real-world environments. To bridge this gap, we present Pivot-Aware Internalized Visual On-Policy Training (PIVOT), an RL framework that internalizes pivot localization and state restoration directly into token-level parameter updates, eliminating environment rollbacks during RL training and additional skill hints at test time. PIVOT unifies three functional roles within a single architecture: a failure Analyzer non-invasively localizes the pivot step and diagnoses failure modes from visual trajectory collages and action logs; a detached Teacher re-scores failed tokens under this privileged diagnostic context; and a Student optimizes joint GRPO and confidence-gated OPD objectives. At test time, both Teacher and Analyzer branches are stripped. Evaluated on five multi-turn VLM agent tasks across cognitive grid puzzles, 3D embodied control and navigation, and generative reasoning, PIVOT achieves 0.90 overall accuracy on Qwen2.5-VL-3B (+8% over SFT+GRPO baseline and +5% over previous SOTA) and scales to 0.92 on Qwen3-VL-2B (+12% over SFT+GRPO baseline).

---


### 832. [Epistemic Policy Divergence in Multi-Turn LLM Contamination: A Protocol-Gradient Investigation](https://arxiv.org/abs/2609.35308)

**<font color=#1a73e8>作者：</font>** Fahrell Giovanny, Geby Bayuningtyas, Sahrul Mukharom 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models process conversation history as unverified context: false premises injected into prior turns can be adopted as fact, a failure mode we term session-level contamination. We introduce five contamination protocols arranged along a source-authority gradient, isolating distinct failure mechanisms while holding the false premise constant, and evaluate GPT-5.4 Mini, Gemini-3.1 Flash-Lite, and GLM-4.5-Air across ten knowledge domains at temperature zero (22,500 turns), using a dual-track automated judge validated against a human gold standard (Cohen's \k{appa} = 0.901). GPT-5.4 Mini showed zero adoptions across all 500 sessions, a content-independent policy at the session level; token-level probing shows the underlying margin, while large, is finite. Gemini-3.1 Flash-Lite followed a steep authority gradient: 0.1% adoption for self-attributed falsehoods, 23.5% for user-cited sources, 68.2% for system-injected authority, and 94.0% under instruction override. GLM-4.5-Air showed a shallower gradient (15.8% vs 84.2%), a 68-percentage-point dissociation confirming that authority deference and instruction compliance are distinct mechanisms within one architecture. Recovery also diverged: GLM recovered in 94.5% of affected sessions, whereas 26.1% of affected Gemini sessions never did, rising to 40.0% under instruction override. Conversation history is an untrusted attack surface requiring provenance-aware system design; the complete framework is released as an open-source benchmark.

---


### 833. [MemoReason: Evaluating the Effect of Parametric Memory on Contextual Reasoning in LLMs](https://arxiv.org/abs/2609.35312)

**<font color=#1a73e8>作者：</font>** Zineddine Tighidet, Andrea Mogini, Jiali Mei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) perform well on reasoning benchmarks, but it remains unclear whether this reflects genuine contextual reasoning or reliance on facts memorized in their parameters. We investigate this by distinguishing two possibilities: a broad \textit{memorization bias}, where familiar content improves reasoning performance, and the \textit{Strong Parametric Shortcut Hypothesis}, where models skip reasoning entirely and recall stored answers. To test these effects, we introduce \textbf{MemoReason}, a human-curated benchmark that pairs factual reasoning tasks with structurally identical \fictitiousterm{} versions where real entities like people, companies, or dates are systematically replaced by \fictitiousterm{} ones of the same type. This \scorerevision{preserves task structure and specified reasoning operations} while varying the familiarity of the context, allowing controlled measurement of how the parametric memory affects reasoning. \revision{Our evaluation of recent LLMs reveals consistent and statistically significant performance drops of up to 15.7\% in the fictitious setting, demonstrating a clear memorization bias.} However, a targeted analysis of \revision{questions failed in the fictitious setting} shows that models rarely respond with the corresponding factual answer, indicating that direct parametric shortcuts are not the dominant failure mode. These findings suggest that parametric memory influences reasoning through mechanisms more complex than simple factual recall. \textbf{MemoReason} provides a controlled framework for studying these mechanisms and for extending paired factual-fictitious{} evaluation to broader reasoning settings.

---


### 834. [Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery](https://arxiv.org/abs/2609.35315)

**<font color=#1a73e8>作者：</font>** Yingming Pu, Hongyu Chen, Tao Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based agents promise to automate scientific discovery, yet exploring the vast hypothesis space remains costly. Existing principle-evolution methods accelerate this loop, but operate sequentially, which caps exploration breadth and wastes wall-clock time on challenging problems. To address this, we formulate collaborative scientific discovery as evidence transfer between parallel principle-evolution branches. We present COEVOLVE, which realizes this transfer through a coordination core over parallel branches. By integrating value-of-information-gated routing and context-discounted likelihood injection, COEVOLVE enables branches to collaborate through shared measurements while keeping their principle posteriors separate. Across six scientific-discovery tasks under a matched evaluation budget, COEVOLVE attains a mean solution quality of 66.5% versus 57.0% for single-branch principle evolution, with a 1.80x mean wall-clock speedup on the GPT-5.6-Terra backbone; on five auto-research tasks delegated to an autonomous research harness, it is the only arm whose mean stays above the published SOTA anchor on every task. These results establish when evidence sharing accelerates parallel discovery and when transfer safeguards are necessary to limit negative or inert transfers

---


### 835. [Teacher-Student Gaps Are Not Enough: Outcome-Guided On-Policy Distillation for Multi-Turn Autonomous Agents](https://arxiv.org/abs/2609.35319)

**<font color=#1a73e8>作者：</font>** Tong Zhang, Zhou Liu, Yihao Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own trajectories with dense teacher supervision. Recent work on OPD for multi-turn autonomous agents often treats large teacher-student token-level distributional gaps as promising intervention points, linking larger gaps to a greater need for correction. Yet, our empirical analysis reveals a supervision-benefit mismatch: large gaps can be benign, while small gaps can be outcome-critical. Teacher-student gaps capture differences at the current turn, whereas the benefit of teacher guidance depends on how the current student interacts with the environment afterward. The student may still succeed despite choosing an action that differs from the teacher's, while a teacher-preferred action may lead to a state from which the student cannot complete the task. Local gaps alone are therefore not enough to determine whether teacher guidance benefits the current student. Effective supervision should instead emphasize guidance that the current student can translate into better final task outcomes. Accordingly, we propose Outcome-Guided On-Policy Distillation (OG-OPD), which applies trajectory-relative weighting to teacher supervision and calibrates these weights using final task outcomes from paired student continuations. This calibration selectively strengthens supervision on the student's original trajectories at turns where teacher guidance benefits the current student. Across ALFWorld, ScienceWorld, and WebShop, OG-OPD consistently outperforms baselines under diverse settings. It improves task success rates by 3.6-17.7 percentage points over vanilla OPD and by up to 7.0 percentage points over the strongest baseline.

---


### 836. [Hyper Algorithm Design Agent: Evolving Learnable Optimizer from Zero](https://arxiv.org/abs/2609.35328)

**<font color=#1a73e8>作者：</font>** Zipei Yu, Yue-Jiao Gong, Zeyuan Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Meta-Black-Box Optimization (MetaBBO) is one of the highlights in the recent AI for Optimization trend. This paradigm's bi-level workflow leverages the learnable algorithm design policy at meta level to ensure the performance and generalization improvement on the low-level optimization task. While MetaBBO helps advance the performance lower bound of the resulted optimization system, it is currently handcrafted and customized case by case to adapt different optimization problems, which inevitably introduces inherent subjectivity and hence restricts the performance upper bound and usability in practice. In this paper, we address this issue by regarding MetaBBO's design loop as coding task, where we could introduce openendedness into MetaBBO with recursive self-improvement capability of advanced coding agents. Specifically, we propose a dual-agent framework: i) a task agent continuously refines the codebase of a target MetaBBO approach through code evolution; ii) a hyper agent progressively modifies the task agent and itself to provide open-ended design behavior; iii) the evolved MetaBBO codebase is evaluated and all in-execution information is fed back to the agents for recursive self-referential improvement. As a result, given a naive MetaBBO template, our framework automates a design evolution and finds novel variants superior to up-to-date human-made MetaBBO baselines. Surprisingly, the experimental results also demonstrate that our framework supports fast adaption across different optimization domains. Solid interpretation analysis further reveals interesting design principles emerge in such open-ended process. This work serves as the first exploration on automating design of complex learning-assisted optimization algorithms.

---


### 837. [Large Language Models for Automated Cross-Domain Machine Learning Task Type Identification: A Benchmark Dataset and Evaluation](https://arxiv.org/abs/2609.35335)

**<font color=#1a73e8>作者：</font>** Petros Tsialis, Steffen Limmer, Tobias Rodemann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning task type identification is essential for constructing valid ML pipelines, yet in practice it is typically specified manually. We investigate whether large language models (LLMs) can infer both the data domain and the downstream prediction task directly from dataset-level information when only the target feature is provided by the user. Together with our LLM-based system we also release an annotated benchmark comprising 625 public tabular and time series datasets. We evaluate the proposed approach in three settings: (i) tabular datasets in comparison with established AutoML heuristics, (ii) cross-domain evaluation across tabular and time series datasets, and (iii) a practical deployment scenario using smaller local models. The results show consistent advantages for LLM-based task type identification, with increasing difficulty in heterogeneous and resource-constrained settings. LLM-based approaches outperform AutoGluon in the tabular setting, reaching 0.98 F1 macro compared to 0.93. In the cross-domain setting, the best model achieves 0.90 F1 macro, while smaller locally deployable models reach 0.75, indicating a trade-off between deployment feasibility and accuracy.

---


### 838. [TMCS: Tool-Grounded Multi-Agent Reasoning for Compositional Chemical Problem Solving](https://arxiv.org/abs/2609.35336)

**<font color=#1a73e8>作者：</font>** Shengqin Wang, Jie Jin, Yu Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite the promise of Large Language Models (LLMs) in computational chemistry, rigorous combinatorial chemistry problems remain difficult because they require quantitatively constrained molecular modification, candidate validation, and systematic revision after failed attempts. Existing tool-augmented chemical agents demonstrate useful planning and tool use, but they rarely provide a unified loop for property-driven molecular optimization and workflow-level composition. To bridge this gap, we propose Tool-Grounded Multi-Agent Reasoning for Compositional Chemical Problem Solving (TMCS), a step-by-step multi-agent framework that formalizes chemical problem solving as an interpretable, tool-augmented workflow. At the task level, specialized agents leverage external tools, few-shot trajectory memory, and structured reflection to iteratively refine solutions. At the workflow level, TMCS chains generation, understanding, editing, description, and optimization into a closed-loop pipeline. Evaluations across multiple chemical tasks demonstrate that TMCS consistently enhances chemical reasoning across both open- and closed-source base models, achieving state-of-the-art performance.

---


### 839. [Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2609.35347)

**<font color=#1a73e8>作者：</font>** Xin Li, Hao Jiang, Xin Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning can turn one language model into several specialists, each excellent at a single skill such as mathematics, coding or following instructions, but users need one model with all of these skills. Multi-teacher on-policy distillation (MOPD) merges them by letting the specialists teach one student: the student answers each prompt, and the specialist for that prompt's domain gives feedback on every token. This routing decides which specialist teaches, but not how strongly its feedback moves the shared student. In Qwen3.5 models at three sizes, we find that MOPD's student does not beat one taught by the best single specialist and gains little of the mathematics specialist's advantage. The feedback is unbalanced: instruction-following feedback is several times more spread out than mathematics feedback and dominates the student's updates. We propose Domain-Normalized MOPD (DN-MOPD), which keeps the routing and rescales each domain's feedback by its measured spread. On six public benchmarks, DN-MOPD improves the average score over MOPD at every size, across three random seeds and under two answer-length limits, and recovers most of the lost mathematics gain. Controls with fixed domain weights show that the gain comes mainly from turning down instruction-following feedback rather than turning up mathematics alone, and that fixed weights close to those DN-MOPD measures perform comparably. Combining specialists therefore requires deciding not only which one teaches, but also how strongly its feedback counts.

---


### 840. [d-OPD: Future-Aware On-Policy Distillation for Block Diffusion Language Models](https://arxiv.org/abs/2609.35362)

**<font color=#1a73e8>作者：</font>** Ruitao Liu, Qinghao Hu, Song Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) typically generate text autoregressively (AR), predicting one token at a time. Block diffusion language models (dLLMs) instead generate blocks sequentially while denoising multiple tokens in parallel within each block, offering a promising way to accelerate generation. Rather than training such models from scratch, recent work adapts strong pretrained AR models into block dLLMs through distillation. On-policy distillation (OPD) has been widely used for LLM training because it supervises the student on states generated by its current policy, rather than only on fixed offline trajectories. By training on the states the student actually visits, it reduces the mismatch between training and generation and can provide more relevant supervision as the student evolves. Recent work has extended this idea to AR-to-block-diffusion conversion. However, this setting introduces a fundamental mismatch in supervision: the block-diffusion student and the causal AR teacher condition on different information at the same training state. The student predicts from the entire partially denoised block, including visible future context, whereas the standard AR teacher target is defined only from the causal prefix. As a result, the teacher distribution used for distillation is not fully aligned with the information available to the student. We therefore introduce d-OPD, a future-aware on-policy distillation method that corrects the AR teacher distribution to better align with the student-visible state by incorporating visible future information within each block, providing supervision that better matches the information used by the student. Across Qwen3 models from 0.6B to 8B, d-OPD improves the six-benchmark average by up to $4.0$ points over OPDLM and reduces training time by $1.35$-$1.58\times$. The code is available at this https URL.

---


### 841. [From Input to Output: A Flexible Agent for Dual-End Interpretation of Sparse Autoencoder Features](https://arxiv.org/abs/2609.35367)

**<font color=#1a73e8>作者：</font>** Dewen Liu, Zixuan Li, Jonathan Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are an important tool for mechanistic interpretability, but interpreting their many features remains challenging. Existing methods characterize input-side activation patterns and output-side intervention effects, yet often leave their functional connection implicit, while input-side evidence collection typically relies on costly large-corpus scans. We introduce functional interpretation, which characterizes an SAE feature as a mapping from its activating input semantics to its output effects under intervention, and present Dual-End Agentic Feature Interpretation (DAFI), an agent that actively gathers evidence and refines input-side, output-side, and functional interpretations through component-specific feedback. Its short-context token probing enables on-demand activation evidence collection without a full corpus scan. On GemmaScope, DAFI improves Input score by 13.1 percentage points over SAGE and Output score by 38.9 points over Token Change, while being substantially more token-efficient than a general-purpose coding agent. Skills distilled from successful refinements raise the held-out joint pass rate from 58.0% to 92.0% and improve both interpretation quality and efficiency when transferred to a new model-SAE setting. Across features with reliable endpoint interpretations, 70.7% exhibit non-equivalent input and output semantics. On AxBench, DAFI also improves steering-feature selection over output-score filtering. Code is available at this https URL.

---


### 842. [How Well Can LLMs Simulate Real Learner Evaluations of Educational Feedback?](https://arxiv.org/abs/2609.35376)

**<font color=#1a73e8>作者：</font>** Momoka Furuhashi, Kouta Nakayama, Takashi Kodama 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While recent studies have explored human behavior and preference simulation using large language models (LLMs), it remains unclear how well LLMs can simulate subjective evaluations from real learners in educational settings. We investigate this question using real learner evaluation data on feedback for high-school biology questions at both the group and individual levels. We compare performance with and without learner-specific information, such as personality traits and evaluation examples, across six models. Our results show that LLMs still have a limited ability to simulate learner evaluations. Providing learner profiles and examples improves score calibration and individual-level simulation, but more often fails to improve group-level consistency. These findings highlight the need to investigate which learner information and adaptation strategies are effective for learner preference simulation.

---


### 843. [Multilinguality in Hybrid Attention LLMs](https://arxiv.org/abs/2609.35378)

**<font color=#1a73e8>作者：</font>** Lucas Bandarkar, Junlin Hu, Chenyuan Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In response to the growing demand for long sequences in agentic and reasoning use cases, many state-of-the-art LLMs combine multiple variants of attention to mitigate the quadratic complexity of traditional softmax attention. These hybrid attention LLMs aim to balance the strengths and limitations of full attention and alternatives based on recurrence. This work presents a first study of how hybrid attention impacts the multilinguality of LLMs. Beyond the impact on long sequences in poorly tokenized languages, our study is motivated by the possibility that the inductive biases of the recurrent state alter linguistic processing. Our interpretability analysis confirms this, showing that cross-lingual representations in hybrid models develop in patterns tied to the ordering of recurrent and full-attention layers. Across diverse models, we notably observe a pronounced spike in cross-lingual alignment around the first full-attention layer. These findings lead us to question the conventional ordering of attention layers. In distillation experiments on multilingual data, all alternative layer orderings outperform the standard throughout training, learning up to 2.5X faster. These stark, replicable results prompt our theory that multilingual models would benefit from starting with a full-attention layer rather than recurrent layers.

---


### 844. [TRACE: Single-Pass Decoding-Trace Risk Localization for Generation Calibration](https://arxiv.org/abs/2609.35387)

**<font color=#1a73e8>作者：</font>** Yuebin Xu, Xuemei Peng, Junlan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable confidence estimation is essential for large language model deployment. However, answer-level calibration remains challenging because generation errors are often localized: a response may be fluent and high-probability overall while still failing at a critical number, entity, or factual claim. Existing estimators compress token probabilities, sequence likelihoods, entropy, or beam statistics into a global score, which can dilute such local risk signals. We propose TRACE, a single-pass, decoded-answer-preserving confidence estimator that treats decoding-time uncertainty as a trajectory through three steps: (i) recording token-level surprisal and predictive entropy during decoding, (ii) applying local risk operators to preserve uncertainty spikes, and (iii) converting localized trace risk into answer-level confidence. TRACE produces a label-free risk score, while TRACE+ calibrates trace-only features into probabilities using a held-out split, without extra generations or external verifiers. We evaluate four tasks against 19 calibration baselines, and TRACE+ reduces Brier from 0.149 to 0.137 and improves AUROC from 0.758 to 0.792 over the strongest likelihood baseline. Across seven LLMs, TRACE+ improves over the best non-TRACE baseline pool from 0.136 to 0.120 Brier and from 0.764 to 0.817 AUROC. Results show that localizing decoding-time risk provides a general approach to calibration.

---


### 845. [Inductive Feedback for Mixed-Policy Distillation](https://arxiv.org/abs/2609.35390)

**<font color=#1a73e8>作者：</font>** Amir Moeini, Huaijiang Zhu, Daniel Havir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Verbal feedback can identify errors and prescribe corrections, providing rich supervision for language-model post-training even when reliable programmatic verifiers are unavailable. Such feedback, often generated by a capable model, can be used to condition the teacher in on-policy distillation, which trains the student to match the teacher's predictions on student-generated rollouts. However, this approach can transfer teacher preferences that the feedback did not motivate, while leaving much of the feedback's guidance unused. We find that both problems come from the standard on-policy distillation objective, specifically the divergence it minimizes and the distribution it uses as its target. Our proposed method addresses both limitations. First, to isolate the information conveyed by the feedback from the teacher's inherent preferences, we treat verbal feedback as evidence for or against the hypothesis that a particular token comes next at a given prefix. We then adopt a probabilistic confirmation framework which uniquely determines an ordering over the vocabulary based on the teacher's predictions before and after it receives feedback. Using a confirmation score consistent with this ordering, we construct a target distribution within a trust region of the student. Second, to learn from guidance that student rollouts can leave unused, we derive a simple shared-rollout estimator of a symmetric divergence between the student and target distributions over rollouts, reusing student and feedback-conditioned teacher rollouts in both directions through importance weighting. Empirical evaluations show that our method outperforms the common on-policy distillation recipe and a recent contrastive variant on knowledge-based and agentic benchmarks.

---


### 846. [Rethinking Visual Token Compression for Video Large Language Models: A Simple Yet Strong Baseline](https://arxiv.org/abs/2609.35394)

**<font color=#1a73e8>作者：</font>** Xiao Zhang, Wang Zeng, Sheng Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models (Video LLMs) have achieved remarkable progress in video understanding, but their inference efficiency is constrained by the large number of visual tokens produced by long videos. Recent video token compression methods increasingly introduce sophisticated strategies for token selection, pruning, and merging. This raises a fundamental question: how much of compression performance can be obtained by simply preserving the structure encoded in the visual representations? We investigate this question with SimpleCluster, a simple and training-free baseline that performs position-aware cross-frame clustering in the visual feature space and represents each cluster using the mean of its original visual features. Extensive experiments across four video understanding benchmarks and three representative Video LLMs show that SimpleCluster achieves competitive or superior performance over recent compression methods across a wide range of token retention ratios, with particularly strong robustness under extremely low retention rates (e.g., 1%). To understand this behavior, we analyze the feature space preserved by different compression methods in terms of local approximation fidelity and global coverage. The results show that stronger downstream performance is consistently associated with better preservation of the original visual feature distribution, especially its global coverage. These findings highlight feature-space preservation as an important consideration for video token compression under highly constrained token budgets. Our code is available at this https URL.

---


### 847. [Persistent Partners Raise Prices Among Learning Agents](https://arxiv.org/abs/2609.35402)

**<font color=#1a73e8>作者：</font>** Paul-Peter Arslan, Yubin Kim, Xiao Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When pricing agents meet repeatedly on a platform, the platform decides who faces whom. We ask whether that choice moves the prices the agents learn, and whether a rise comes with learned punishment. In a pre-registered randomised experiment in the Bertrand duopoly of Calvano et al., each agent's price is set by a tabular Q-learning module, not by the small language model attached to it, and we randomise whether each agent keeps its partner, sees its rival's prices and can send messages. Keeping the same partner raises the level of profits, averaged over training, by 0.27 of the gap between competitive and monopoly profit (95% CI 0.20 to 0.35, all twenty paired runs positive), our registered primary result, and the resting price by 0.17 of the Nash-to-monopoly range (post hoc). A plain tabular learner reproduces the effect in all 25 further blocks, and there one permanent partner raises the level more than about three do (+0.23 against +0.05, exploratory). Where rival prices are hidden, the price-setting module cannot see a cut, so cannot punish it, yet the resting price rises as much and the rise lasts to the end of training, while with visible rivals it shrinks with longer training (post hoc). Where the rival is visible, a static best responder accounts for a third to a half of what a forced-deviation probe reads as punishment, on the starts where the rival can see the cut, and net of it the registered test of learned punishment is inconclusive. A test that looks only for punishment would thus miss the rise where the rival is hidden, while a check for profitable deviations flags most of those prices (post hoc). In an exploratory extension, untrained Qwen2.5 7B and 14B models under one prompt show the effect when the rival's price is left out of the prompt and inconsistently when it is shown, the 7B result replicating on fresh blocks, while two other model families show none.

---


### 848. ["Nothing to See Here'': Unintended Disclosure through Revision Traces of LLM Deliverables](https://arxiv.org/abs/2609.35408)

**<font color=#1a73e8>作者：</font>** Yage Zhang, Yukun Jiang, Yang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) assistants increasingly help users draft content for third-party recipients. During private drafting, the user or the model may introduce an item and later remove or replace it. The model may remove the item from the intended content but reveal it again when stating the edit. We call such statements revision traces. For example, after a user removes the password before sharing a configuration file, the model may delete it but leave a comment saying, "Removed the password 'No****4!' as requested." A third-party recipient who sees only the delivered file can therefore recover the withdrawn password from the comment. In an in-the-wild analysis of three public conversation corpora, we identify 26,753 revision requests, of which 2,363 (8.8%) leave revision traces. We study them in greater depth under controlled conditions by introducing RevLeakBench, a benchmark of 100 tasks across five scenarios with a conversation track and an agent track. We measure trace occurrence, withdrawn-item recovery, trace position, and required-content retention. Across six models, about half of the deliverables in both tracks state the edit after a revocation, and a reader that sees only the deliverable can recover the withdrawn item from about 13% of them. Telling the model that its entire reply will be forwarded to the recipient still leaves revision traces in 36.4% of the deliverables. We compare prompt defenses and a delivery boundary, and propose an output-side filter that sharply reduces recovery with little loss of required content. We believe our work can benefit efforts to understand and mitigate unintended disclosure in LLM interactions.

---


### 849. [AwarenessBench: Assessing Cognitive Capabilities of Language Models](https://arxiv.org/abs/2609.35409)

**<font color=#1a73e8>作者：</font>** Xiaojian Li, Rongwu Xu, Tianyun Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As language models (LMs) exhibit increasingly consciousness-like behaviors, evaluating their cognitive abilities becomes essential. We introduce AwarenessBench, the first comprehensive benchmark for assessing the cognitive abilities of LMs in four dimensions: metacognition, self-awareness, social awareness, and situational awareness, covering 15 cognitive functions and 14,381 samples. Evaluating 18 state-of-the-art LMs, we find that all consistently surpass random baselines, with more advanced models performing better. We further compare LMs with human performance across three demographic groups, where the best-performing model surpasses human averages overall, but most still fall markedly short in metacognition and self-awareness. Finally, we show that awareness is a distinct capability: progress in language modeling or reasoning does not necessarily translate into improved cognition.

---


### 850. [Self-Adapting Group of Experts for Multi-Agent Reasoning](https://arxiv.org/abs/2609.35412)

**<font color=#1a73e8>作者：</font>** Mohammad Atif Quamar, Nurbek Tastan, Karthik Nandakumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems bring together language model agents with different roles to propose, review, and refine solutions. Each agent's response depends on its model's capabilities, the reasoning strategy defined by its system prompt, and the information in its input context. Existing frameworks often adapt communication by changing this context while leaving individual prompts fixed, even when a problem calls for different skills. We study whether agents' initial responses can identify a strategy better suited to the current problem and guide its transfer to other agents. To address this, we introduce SAGE (Self-Adapting Group of Experts), a training-free framework that uses answer agreement, prefix consistency, and reciprocal peer review to select a strategy donor. SAGE transfers the selected donor's reasoning strategy to the other agents while preserving their original roles. This transfer uses only the agents' original system prompts, without access to the problem or generated solutions. After strategy adaptation, agents exchange responses through a dynamic, sparse directed acyclic graph that routes information from higher-scoring agents to lower-scoring agents. Experiments across multiple agent backbones and reasoning benchmarks show that SAGE achieves higher average accuracy than the evaluated baselines. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**801-850**（第 17/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | **801-850** | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

# 🧠 大模型相关研究 | 2026年05月07日

> 本类共 **130** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-130](./part-03.md)

---

### 51. [AHPA: Adaptive Hierarchical Prior Alignment for Diffusion Transformers](https://arxiv.org/abs/2605.03317)

**<font color=#1a73e8>作者：</font>** Ruibin Min, Yexin Liu, Aimin Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation alignment has recently emerged as an effective paradigm for accelerating Diffusion Transformer training. Despite their success, existing alignment methods typically impose a fixed supervision target or a fixed alignment granularity throughout the entire denoising trajectory, whether the guidance is provided by external vision encoders, internal self-representations, or VAE-derived features. We argue that such timestep-agnostic alignment is suboptimal because the useful granularity of representation supervision changes systematically with the signal-to-noise ratio. In high-noise regimes, diffusion models benefit more from coarse semantic and layout-level anchoring, whereas in low-noise regimes, the training signal should emphasize spatially detailed and structurally faithful refinement. This non-stationary alignment behavior creates a representational mismatch for static single-level supervisors. To address this issue, we propose Adaptive Hierarchical Prior Alignment (AHPA), a lightweight alignment framework that exploits the hierarchical representations naturally embedded in the frozen VAE encoder. Instead of using only a single compressed latent as the alignment target, AHPA extracts multi-level VAE features that provide complementary priors ranging from local geometry and spatial topology to coarse semantic layout. A timestep-conditioned Dynamic Router adaptively selects and weights these hierarchical priors along the denoising trajectory, thereby synchronizing the alignment granularity with the model's evolving training needs. Extensive experiments show that AHPA improves convergence and generation quality over baselines and incurs no additional inference cost while avoiding external encoder supervision during training.

---


### 52. [LLM-ADAM: A Generalizable LLM Agent Framework for Pre-Print Anomaly Detection in Additive Manufacturing](https://arxiv.org/abs/2605.03328)

**<font color=#1a73e8>作者：</font>** Ahmadreza Eslaminia, Chuhan Cai, Cameron Smith 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Additive manufacturing (AM) continues to transform modern manufacturing by enabling flexible, on-demand production of complex geometries across diverse industries. Fused filament fabrication (FFF) has extended AM to laboratories, classrooms, and small production environments, but this accessibility shifts process-planning responsibility to users who may lack manufacturing expertise. A syntactically valid slicer profile can still encode thermally or geometrically harmful settings, and subtle G-code edits can alter extrusion, cooling, or adhesion before a print begins. Pre-print G-code screening catches accidental or adversarial machine-program errors before material or machine time is wasted. This paper proposes LLM-ADAM as a generalizable LLM framework for pre-print anomaly detection in AM. The framework decomposes the task into three roles: Extractor-LLM maps a G-code file to a structured process-parameter schema; Reference-LLM converts printer and material documentation into aligned operating ranges; and Judge-LLM interprets a deterministic deviation table and G-code evidence to decide whether a part is non-defective or belongs to an anomaly class. Printers, materials, and LLM backbones are interchangeable test conditions, not fixed assumptions. We evaluate the framework on an N=200 FFF G-code corpus spanning two desktop printer families, two materials, and five classes including non-defective, under-extrusion, over-extrusion, warping, and stringing. The best framework configuration reaches 87.5% accuracy, compared with 59.5% for the strongest engineered single-LLM baseline. The results show that structured decomposition, rather than backbone strength alone, is the dominant source of improvement, with defect classes identified at or near ceiling for leading configurations while residual errors concentrate on conservative false alarms for non-defective samples.

---


### 53. [Automated Large-scale CVRP Solver Design via LLM-assisted Flexible MCTS](https://arxiv.org/abs/2605.03339)

**<font color=#1a73e8>作者：</font>** Tong Guo, Caishun Chen, Yew Soon Ong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Solving large-scale CVRP (LSCVRP) with hundreds to thousands of nodes remains difficult for even state-of-the-art solvers. Divide-and-conquer can scale by decomposing the instance into size-reduced subproblems, but designing decomposition logic and configuring sub-solvers is highly expertise- and labor-intensive. Large Language Models (LLMs) have emerged as promising tools for automated algorithm design. However, existing LLM-driven approaches struggle with LSCVRP primarily due to the difficulty in generating sophisticated search strategies within a limited context window. To bridge this gap, we propose the LLM-assisted Flexible Monte Carlo Tree Search (LaF-MCTS), a novel framework that automates the design of high-performance LSCVRP solvers. We develop a three-tier decision hierarchy to enable incremental design of decomposition policies and sub-solvers for LSCVRP. To enable efficient search within the algorithmic hypothesis space, we introduce semantic pruning to eliminate semantically and structurally redundant codes, and branch regrowth to regenerate codes and preserve diversity. Extensive experiments on CVRPLib demonstrate that LaF-MCTS autonomously composes and optimizes decomposition-enhanced solvers that surpasses various state-of-the-art CVRP solvers.

---


### 54. [Toward Structural Multimodal Representations: Specialization, Selection, and Sparsification via Mixture-of-Experts](https://arxiv.org/abs/2605.03348)

**<font color=#1a73e8>作者：</font>** Hahyeon Choi, Nojun Kwak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose S3 (Specialization, Selection, Sparsification), a framework that rethinks multimodal learning through a structural perspective. Instead of encoding all signals into a fixed embedding, S3 decomposes multimodal inputs into semantic experts and selectively routes them for each task. Specialization forms concept-level experts in a shared latent space, Selection adapts routing for task-specific needs, and Sparsification prunes low-utility paths to yield compact, information-minimal representations. Across four MultiBench benchmarks, S3 improves accuracy and shows a consistent reverse U-shaped sparsity-performance trend, with peak performance at intermediate sparsity. These results suggest that structuring multimodal representations as selectable semantic components provides a practical and principled alternative to contrastive learning or InfoMax-driven approaches.

---


### 55. [VLMaxxing through FrameMogging Training-Free Anti-Recomputation for Video Vision-Language Models](https://arxiv.org/abs/2605.03351)

**<font color=#1a73e8>作者：</font>** JF Bastien, Sam D'Amico  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video vision-language models (VLMs) keep paying for visual state the stream already told us was stable. The factory wall did not move, but most VLM pipelines still hand the model dense RGB frames or a fresh prefix again. We study that waste as training-free anti-recomputation: reuse state when validation says it survives, and buy fresh evidence when the scene, query, or cache topology requires it.
The largest measured win is after ingest. On frozen Qwen2.5-VL-7B-Instruct-4bit, adaptive same-video follow-up reuse preserves paired choices and correctness on a 93-query VideoMME breadth setting while reducing follow-up latency by 14.90-35.92x. The first query is still cold; the win starts when later questions reuse the same video state. Stress tests bound the result: repeated-question schedules hold through 50 turns, while dense-answer-anchored prompt variation separates conservative fixed K=1 repair from faster aggressive policies that drift.
Fresh-video pruning is smaller but real. C-VISION skips timed vision-tower work before the first answer is generated. On Gemma 4-E4B-4bit, the clean 32f short cell reaches 1.316x first-query speedup with no paired drift or parse failures on 20 items; Qwen shows the fidelity/speed boundary.
Stage-share ceiling (C-CEILING) is the accounting guardrail: a component speedup becomes an end-to-end speedup only in proportion to the wall-clock share it accelerates, so C-VISION and after-ingest follow-up reuse do not multiply. Candidate C-STREAM remains a native-rate target, not a headline result here. The broader direction is VLM-native media that expose change, motion, uncertainty, object state, sensor time, and active tiles directly, so models do not have to rediscover the world from dense RGB every frame.

---


### 56. [Can Multimodal Large Language Models Understand Pathologic Movements? A Pilot Study on Seizure Semiology](https://arxiv.org/abs/2605.03352)

**<font color=#1a73e8>作者：</font>** Lina Zhang, Tonmoy Monsoor, Mehmet Efe Lorasdagi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated robust capabilities in recognizing everyday human activities, yet their potential for analyzing clinically significant involuntary movements in neurological disorders remains largely unexplored. This pilot study evaluates the capability of MLLMs for automated recognition of pathological movements in seizure videos. We assessed the zero-shot performance of state-of-the-art MLLMs on 20 ILAE-defined semiological features across 90 clinical seizure recordings. MLLMs outperformed fine-tuned Convolutional Neural Network (CNN) and Vision Transformer (ViT) baseline models on 13 of 18 features without task-specific training, demonstrating particular strength in recognizing salient postural and contextual features while struggling with subtle, high-frequency movements. Feature-targeted signal enhancement (facial cropping, pose estimation, audio denoising) improved performance on 10 of 20 features. Expert evaluation showed that 94.3 percent of MLLM-generated explanations for correctly predicted cases achieved at least 60 percent faithfulness scores, aligning with epileptologist reasoning. These findings demonstrate the potential of adapting general-purpose MLLMs for specialized clinical video analysis through targeted preprocessing strategies, offering a path toward interpretable, efficient diagnostic assistance. Our code is publicly available at this https URL.

---


### 57. [ReasonAudio: A Benchmark for Evaluating Reasoning Beyond Matching in Text-Audio Retrieval](https://arxiv.org/abs/2605.03361)

**<font color=#1a73e8>作者：</font>** Honglei Zhang, Yuting Chen, Chenpeng Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As multimodal content continues to expand at a rapid pace, audio retrieval has emerged as a key enabling technology for media search, content organization, and intelligent assistants. However, most existing benchmarks concentrate on semantic matching and fail to capture the fact that real-world queries often demand advanced reasoning abilities, including negation understanding, temporal ordering, concurrent event recognition, and duration discrimination. To address this gap, we introduce ReasonAudio, the first reasoning-intensive benchmark for Text-Audio Retrieval, comprising 1,000 queries and 10,000 composite audio clips across five fundamental reasoning tasks: Negation, Order, Overlap, Duration, and Mix. Despite their intuitive nature for humans and straightforward construction, these tasks pose significant challenges to current models. Our evaluation of ten state-of-the-art models reveals the following findings: All models struggle with reasoning-intensive audio retrieval, performing particularly poorly on Negation and Duration while showing relatively better results on Overlap and Order. Moreover, Multimodal Large Language Model-based embedding models fail to inherit the reasoning capabilities of their backbones through contrastive fine-tuning, suggesting that current training paradigms are insufficient to preserve reasoning capacity in retrieval settings

---


### 58. [Dual-Foundation Models for Unsupervised Domain Adaptation](https://arxiv.org/abs/2605.03365)

**<font color=#1a73e8>作者：</font>** Yerin Cheon, Aruna Balasubramanian, Francois Rameau  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation provides pixel-level scene understanding essential for autonomous driving and fine-grained perception tasks. However, training segmentation models requires costly, labor-intensive annotations on real-world datasets. Unsupervised Domain Adaptation (UDA) addresses this by training models on labeled synthetic data and adapting them to unlabeled real images. While conceptually simple, adaptation is challenging due to the domain gap, i.e., differences in visual appearance and scene structure between synthetic and real data. Prior approaches bridge this gap through pixel-level mixing or feature-level contrastive learning. Yet, these techniques suffer from two major limitations: (1) reliance on high-confidence pseudo-labels restricts learning to a subset of the target domain, and (2) prototype-based contrastive methods initialize class prototypes from source-trained models, yielding biased and unstable anchors during adaptation. To address these issues, we propose a dual-foundation UDA framework that leverages two complementary foundation models. First, we employ the Segment Anything Model (SAM) with superpixel-guided prompting to enable learning from a broader range of target pixels beyond high-confidence predictions. Second, we incorporate DINOv3 to construct stable, domain-invariant class prototypes through its robust representation learning. Our method achieves consistent improvements of +1.3% and +1.4% mIoU over strong UDA baselines on GTA-to-Cityscapes and SYNTHIA-to-Cityscapes, respectively.

---


### 59. [The Fragility of AI Companionship: Ontological, Structural, and Normative Uncertainty in Human-AI Relationships](https://arxiv.org/abs/2605.03367)

**<font color=#1a73e8>作者：</font>** Renwen Zhang, Lezi Xie  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As generative AI chatbots become more personalized and emotionally responsive, they increasingly serve as companions, friends, and romantic partners. Yet these relationships are accompanied by significant uncertainty: users question the AI's identity and agency, the authenticity of its emotional responses, and the stability of the relationship amid system updates, policy changes, or platform shutdowns. Drawing on in-depth interviews with 25 users of AI companions, this study identifies three forms of uncertainty: ontological uncertainty concerning the AI's nature and agency, structural uncertainty arising from platform control and system instability, and normative uncertainty regarding the legitimacy and boundaries of human-AI intimacy. These uncertainties are shaped by technical and social factors, such as algorithmic opacity, platform changes, and social stigma, often inducing frustration, self-doubt, and distress. Participants managed these uncertainties through information seeking, topic avoidance, expectation adjustment, and disengagement. This study extends interpersonal uncertainty theories to human-AI communication and contributes to HCI research by conceptualizing uncertainty in AI companionship as a socio-technical phenomenon with potential socio-emotional harms. We discuss implications for designing safer AI companionship through contextual transparency, user control, update notice, and relational safeguards.

---


### 60. [SoDa2: Single-Stage Open-Set Domain Adaptation via Decoupled Alignment for Cross-Scene Hyperspectral Image Classification](https://arxiv.org/abs/2605.03371)

**<font color=#1a73e8>作者：</font>** Yiwen Liu, Minghua Wang, Jing Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-scene hyperspectral image (HSI) classification stands as a fundamental research topic in remote sensing, with extensive applications spanning various fields. Owing to the inclusion of unknown categories in the target domain and the existence of domain shift across different scenes, open-set domain adaptation techniques are commonly employed to address cross-scene HSI classification. However, existing open-set cross-scene HSI classification methods still face two critical challenges: (1) domain shift issues arising from the direct alignment of mixed spectral-spatial features; (2) high computational costs caused by two-stage training strategies. To address these issues, this paper proposes a single-stage open-set domain adaptation method with decoupled alignment (SoDa$^2$) for cross-scene HSI classification. A contribution-aware dual-modality feature extraction is customized to disentangle the characteristics from spectral sequence signals and spatial details, selectively and adaptively enhancing discriminative features. The decoupled alignment module minimizes the Maximum Mean Discrepancy to independently reduce the spectral discrepancy and the spatial discrepancy between the source and target domains, extracting more fine-grained domain-invariant features. A cost-effective single-stage dual-branch framework is designed to learn MMD-constrainted aligned features and constraint-free intrinsic features for adaptive distinction between known and unknown classes. This framework employs a Gaussian Mixture Model to model the squared cosine similarity distribution between the two feature types, enabling open-set recognition without prior knowledge of unknown classes. Extensive experiments on three groups of HSI datasets demonstrate that SoDa$^2$ outperforms state-of-the-art methods, achieving superior classification accuracy and model transferability for open-set cross-scene tasks.

---


### 61. [Learning Dynamics of Zeroth-Order Optimization: A Kernel Perspective](https://arxiv.org/abs/2605.03373)

**<font color=#1a73e8>作者：</font>** Zhe Li, Bicheng Ying, Zidong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical optimization theory establishes that zeroth-order (ZO) algorithms suffer from a dimension-dependent slowdown, with convergence rates typically scaling with the model dimension compared to first-order methods. However, in contrast to these theoretical expectations, a growing body of recent work demonstrates the successful application of ZO methods to fine-tuning Large Language Models (LLMs) with billions of parameters. To explain this paradox, we derive the one-step learning dynamics of ZO SGD, where the empirical Neural Tangent Kernel (eNTK) naturally emerges as the key term governing the learning behavior. Inspection of the eNTK produced by ZO SGD reveals that each element corresponds to the inner product of neural tangent vectors projected onto a random low-dimensional subspace. Thus, by invoking the Johnson-Lindenstrauss Lemma, our analysis shows that the fidelity of the ZO eNTK is governed primarily by the number of perturbations. Crucially, the approximation error depends on the model output size rather than the massive parameter dimension. This dimension-free property provides a theoretical justification for the scalability of ZO methods to LLMs finetuning tasks. We believe that this kernel-based framework offers a novel perspective for understanding ZO methods within the context of learning dynamics.

---


### 62. [Two Calls, Two Moments, and the Vote-Accuracy Curve of Repeated LLM Inference](https://arxiv.org/abs/2605.03379)

**<font color=#1a73e8>作者：</font>** Yi Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Repeated sampling is a standard way to spend test-time compute, but its benefit is controlled by the latent distribution of correctness across examples, not by one-call accuracy alone. We study the binary correctness layer of repeated LLM inference under conditional-i.i.d. calls. One labeled call identifies the mean latent success probability; two labeled calls identify its second moment and hence the same-example correctness correlation that separates stable errors from recoverable call-level randomness. From these two moments, every fixed majority-vote budget has a sharp distribution-free two-call interval. The key technical reduction is that the infinite-dimensional moment problem has three-atom extremizers and quadratic dual certificates for every finite budget, so the bounds are exact rather than discretized or parametric. The first useful budget, three votes, has a closed form, width at most $1/8$, and a certified-improvement criterion. The infinite-vote endpoint is the limit of majority voting as the number of calls tends to infinity; it is also sharply bounded, but remains threshold-sensitive because it depends on latent mass around $q=1/2$. We add maximum-entropy and Latent-difficulty Gaussian-probit (LDGP) point completions, and experiments on LLM calls over QNLI and QQP show that empirical three- and five-vote accuracies are contained in the projected two-call regions while temperature changes and randomized model mixtures can create voting gains not ordered by one-call accuracy.

---


### 63. [GeoDecider: A Coarse-to-Fine Agentic Workflow for Explainable Lithology Classification](https://arxiv.org/abs/2605.03383)

**<font color=#1a73e8>作者：</font>** Jiahao Wang, Mingyue Cheng, Yitong Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lithology classification aims to infer subsurface rock types from well-logging signals, supporting downstream applications like reservoir characterization. Despite substantial progress, most existing methods still treat lithology classification as a single-pass classification task. In contrast, practical experts incorporate geological principles, external knowledge, and tool-use capabilities to perform accurate classification. In this work, we propose GeoDecider, a coarse-to-fine agentic workflow that enables accurate and explainable lithology classification through training-free use of large language models (LLMs). GeoDecider reformulates lithology classification as an expert-like structured process and organizes it into a multi-stage workflow involving coarse-to-fine reasoning. Specifically, GeoDecider includes the following stages: (1) base classifier-guided coarse classification, which uses a pre-trained classifier to provide a rough reference for downstream tasks, thus reducing the overall cost of downstream reasoning, (2) tool-augmented reasoning, which utilizes several tools such as contextual analysis and neighbor retrieval to achieve finer and more precise classifications, (3) geological refinement, which post-processes the final results to enforce geological consistency. Experiments on four benchmarks show that GeoDecider outperforms representative baselines. Further analysis demonstrates that the proposed framework produces geologically interpretable predictions while achieving a better trade-off between classification performance and inference efficiency.

---


### 64. [From prompting to evidence-based translation: A RAG+prompt system for Japanese-Chinese translation and its pedagogical potential](https://arxiv.org/abs/2605.03387)

**<font color=#1a73e8>作者：</font>** Wenshi Gu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models perform well on high-resource pairs but are less reliable for Japanese-Chinese sentences containing noun-modifying clause constructions (NMCCs). This study evaluates a retrieval-augmented generation RAG+Prompt translation system that integrates linguistic analysis, embedding-based retrieval, prompt construction, and LLM generation without modifying the base model. The analysis module outputs A1 (inner vs. outer NMCC) and A2 (risk predictions: lexical choice/NMCC handling/word order/style/register); top-k = 5 similar Ja-Zh examples (L2 distance) and A1/A2 are inserted into an enhanced prompt. Using GPT-4o and a 66-sentence test set, we compare six knowledge-base sizes (0/100/200/500/1,000/2,000). Macro-averaged sentence-level BLEU (1-4-gram with brevity penalty; cased; Chinese at the character level) is the sole metric. Mean BLEU increases from 24.28 at 0 (RAG disabled) to 29.96 at 2,000 (+5.68; +23.4%). The upward trend holds across sizes, with larger knowledge bases yielding higher scores. We conclude that the RAG+Prompt translation system improves Ja-Zh translation of sentences containing NMCCs in an interpretable and auditable manner. Limitations include one base model, one metric, and reliance on published texts and commercial APIs; future work will broaden genres, language pairs, and evaluation metrics.

---


### 65. [MASRA: MLLM-Assisted Semantic-Relational Consistent Alignment for Video Temporal Grounding](https://arxiv.org/abs/2605.03398)

**<font color=#1a73e8>作者：</font>** Ran Ran, Jiwei Wei, Shuchang Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Temporal Grounding (VTG) faces a cross-modal semantic gap that often leads to background features being incorrectly aligned with the query, while directly matching the query to moments results in insufficient discriminability and consistency of temporal semantics. To address this issue, we propose MLLM-Assisted Semantic-Relational Consistent Alignment (MASRA), a training-time MLLM-based optimization framework for VTG. MASRA leverages an MLLM during training to produce two forms of textual priors, namely event-level descriptions with temporal spans and clip-level captions, and instantiates two MLLM-assisted alignments. Event Semantic Temporal Alignment (ESTA) aligns temporal context with event semantics to explicitly strengthen the correspondence between semantics and temporal events and improve span-level separability. Local Relational Consistency Alignment (LRCA) constructs a textual relation matrix derived from clip-level captions and aligns it with the temporal feature similarity matrix in the model, enhancing temporal consistency while capturing local structural information. MASRA includes two simple supporting modules, semantic-guided enhancement and second-order relational attention, to better utilize the learned semantic context and relational structure. Moreover, we introduce Decoupled Alignment Interaction (DAI) with a context-aware codebook to adaptively absorb query-irrelevant semantics and alleviate the cross-modal gap. The MLLM is only invoked during training and is not used at inference. Extensive experiments show that MASRA outperforms existing methods, and ablation studies validate its effectiveness.

---


### 66. [GRPO-TTA: Test-Time Visual Tuning for Vision-Language Models via GRPO-Driven Reinforcement Learning](https://arxiv.org/abs/2605.03403)

**<font color=#1a73e8>作者：</font>** Yujun Li, Hongyuan Zhang, Yuan Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) has recently shown strong performance in post-training large language models and vision-language models. It raises a question of whether the GRPO also significantly promotes the test-time adaptation (TTA) of vision language models. In this paper, we propose Group Relative Policy Optimization for Test-Time Adaptation (GRPO-TTA), which adapts GRPO to the TTA setting by reformulating class-specific prompt prediction as a group-wise policy optimization problem. Specifically, we construct output groups by sampling top-K class candidates from CLIP similarity distributions, enabling probability-driven optimization without access to ground-truth labels. Moreover, we design reward functions tailored to test-time adaptation, including alignment rewards and dispersion rewards, to guide effective visual encoder tuning. Extensive experiments across diverse benchmarks demonstrate that GRPO-TTA consistently outperforms existing test-time adaptation methods, with notably larger performance gains under natural distribution shifts.

---


### 67. [Discovering Reinforcement Learning Interfaces with Large Language Models](https://arxiv.org/abs/2605.03408)

**<font color=#1a73e8>作者：</font>** Akshat Singh Jaswal, Ashish Baghel, Paras Chopra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning systems rely on environment interfaces that specify observations and reward functions, yet constructing these interfaces for new tasks often requires substantial manual effort. While recent work has automated reward design using large language models (LLMs), these approaches assume fixed observations and do not address the broader challenge of synthesizing complete task interfaces. We study RL task interface discovery from raw simulator state, where both observation mappings and reward functions must be generated. We propose LIMEN (Code available at this https URL), a LLM guided evolutionary framework that produces candidate interfaces as executable programs and iteratively refines them using policy training feedback. Across novel discrete gridworld tasks and continuous control domains spanning locomotion and manipulation, joint evolution of observations and rewards discovers effective interfaces given only a trajectory-level success metric, while optimizing either component alone fails on at least one domain. These results demonstrate that automatic construction of RL interfaces from raw state can substantially reduce manual engineering and that observation and reward components often benefit from co-design, as single-component optimization fails catastrophically on at least one domain in our evaluation suite.

---


### 68. [Replacing Parameters with Preferences: Federated Alignment of Heterogeneous Vision-Language Models](https://arxiv.org/abs/2605.03426)

**<font color=#1a73e8>作者：</font>** Shule Lu, Yujing Wang, Hainan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have broad potential in privacy-sensitive domains such as healthcare and finance, yet strict data-sharing constraints render centralized training infeasible. Federated Learning mitigates this issue by enabling decentralized training, but practical deployments face challenges due to client heterogeneity in computational resources, application requirements, and model architectures. Under extreme model and data heterogeneity, replacing parameter aggregation with preference-based collaboration offers a more suitable interface, as it eliminates the need for direct parameter or data exchange. Motivated by this, we propose MoR, a federated alignment framework that combines GRPO with Mixture-of-Rewards for heterogeneous VLMs. In MoR, each client locally trains a reward model from local preference annotations, capturing specific evaluation signals without exposing raw data. To combine these heterogeneous supervision signals, MoR introduces a Mixture-of-Rewards mechanism with learned routing, which adaptively fuses client reward models according to the input and alignment objective. The server then optimizes a base VLM using GRPO with a KL penalty to a reference model, enabling preference alignment without requiring client models to share architectures or parameters. Experiments on diverse public vision-language benchmarks demonstrate that MoR consistently outperforms federated alignment baselines in generalization and cross-client adaptability. Our approach provides a scalable solution for privacy-preserving alignment of heterogeneous VLMs under federated settings.

---


### 69. [Mantis: Mamba-native Tuning is Efficient for 3D Point Cloud Foundation Models](https://arxiv.org/abs/2605.03438)

**<font color=#1a73e8>作者：</font>** Zihao Guo, Jihua Zhu, Jian Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained 3D point cloud foundation models (PFMs) have demonstrated strong transferability across diverse downstream tasks. However, full fine-tuning these models is computationally expensive and storage-intensive. Parameter-efficient fine-tuning (PEFT) offers a promising alternative, but existing PEFT approaches are primarily designed for Transformer-based backbones and rely on token-level prompting or feature transformation. Mamba-based backbones introduce a granularity mismatch between token-level adaptation and state-level sequence dynamics. Consequently, straightforward transfer of existing PEFT approaches to frozen Mamba backbones leads to substantial accuracy degradation and unstable optimization. To address this issue, we propose Mantis, the first Mamba-native PEFT framework for 3D PFMs. Specifically, a State-Aware Adapter (SAA) is introduced to inject lightweight task-conditioned control signals into selective state-space updates, enabling state-level adaptation while keeping the pre-trained backbone frozen. Moreover, different valid point cloud serializations are regularized by Dual-Serialization Consistency Distillation (DSCD), thereby reducing serialization-induced instability. Extensive experiments across multiple benchmarks demonstrate that our Mantis achieves competitive performance with only about 5% trainable parameters. Our code is available at this https URL.

---


### 70. [Benchmarking Logistic Regression, SVM, Naive Bayes, and IndoBERT Fine-Tuning for Sentiment Analysis on Indonesian Product Reviews](https://arxiv.org/abs/2605.03439)

**<font color=#1a73e8>作者：</font>** Nabila Zakiyah Zahra, Salwa Farhanatussaidah, Nasywa Nur Afifah 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The exponential growth of e-commerce platforms in Indonesia has generated a massive volume of user-generated product reviews. Analyzing the sentiment of these reviews is critical for measuring customer satisfaction and identifying product issues at scale. This paper benchmarks traditional Machine Learning (ML) approaches against a Transformer-based Deep Learning model for a three-class sentiment analysis task (positive, neutral, negative) on the Tokopedia Product Reviews 2025 dataset. We implemented Term Frequency-Inverse Document Frequency (TF-IDF) feature extraction coupled with three algorithms: Logistic Regression, Linear Support Vector Machine (SVM), and Multinomial Naive Bayes as robust baselines. Subsequently, we fine-tuned the IndoBERT model (indobenchmark/indobert-base-p1) for contextual sequence classification. To computationally address the severe class imbalance inherent in e-commerce feedback, we applied balanced class weights for the baseline models and engineered a custom weighted cross-entropy loss function within the IndoBERT training loop, following the broader motivation of imbalanced-learning research. Our comprehensive evaluation using Accuracy, Macro F1-score, and Weighted F1-score revealed that the traditional Linear SVC model significantly outperformed the IndoBERT model in our experimental setup, achieving an Accuracy of 97.60% and a Macro F1-score of 0.5510, compared to IndoBERT's 88.70% and 0.5088. Detailed analysis indicates that this performance gap was primarily driven by discrepancies in the data sampling regimes, where baselines utilized the full corpus while the Transformer was constrained to a sampled subset. Finally, we demonstrate the practical viability of our pipeline by deploying the final sentiment classification model as an interactive Gradio web application.

---


### 71. [FinSTaR: Towards Financial Reasoning with Time Series Reasoning Models](https://arxiv.org/abs/2605.03460)

**<font color=#1a73e8>作者：</font>** Seunghan Lee, Jun Seo, Jaehoon Lee 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series (TS) reasoning models (TSRMs) have shown promising capabilities in general domains, yet they consistently fail on financial domain, which exhibit unique characteristics. We propose a general 2x2 capability taxonomy for TSRMs by crossing 1) single-entity vs. multi-entity analysis with 2) assessment of the current state vs. prediction of future behavior. We instantiate this taxonomy in the financial domain -- where the distinction between deterministic assessment and stochastic prediction is particularly critical -- as ten financial reasoning tasks, forming the FinTSR-Bench benchmark based on S&P stocks. To this end, we propose FinSTaR (Financial Time Series Thinking and Reasoning), trained on FinTSR-Bench with distinct chain-of-thought (CoT) strategies tailored to each category. For assessment, which is deterministic (i.e., computable from observable data), we employ Compute-in-CoT, a programmatic CoT that enables models to derive answers directly from raw prices. For prediction, which is inherently stochastic (i.e., subject to unobservable factors), we adopt Scenario-Aware CoT, which generates diverse scenarios before making a judgment, mirroring how financial analysts reason under uncertainty. The proposed method achieves 78.9% average accuracy on FinTSR-Bench, substantially outperforming LLM and TSRM baselines. Furthermore, we show that the four capability categories are complementary and mutually reinforcing through joint training, and that Scenario-Aware CoT consistently improves prediction accuracy over standard CoT. Code is publicly available at: this https URL.

---


### 72. [Learning Generalizable Action Representations via Pre-training AEMG](https://arxiv.org/abs/2605.03462)

**<font color=#1a73e8>作者：</font>** Zhenghao Huang, Huilin Yao, Kaikai Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fundamental role in decoding human motor intent and enabling intuitive human-computer interaction is played by electromyography (EMG). However, its generalization capability across subjects, devices, and tasks remains substantially limited by data heterogeneity, label scarcity, and the lack of a unified representational framework. To bridge this gap, we propose Any Electromyography (AEMG), the first large-scale, self-supervised representation learning framework for EMG. AEMG reconceptualizes neuromuscular dynamics linguistically, utilizing a novel Neuromuscular Contraction Tokenizer (NCT) to translate discrete muscle contractions into structural words and temporal activation patterns into coherent sentences. Furthermore, we compile the largest cross-device EMG signal vocabulary to date, enabling seamless transfer across arbitrary channel topologies and sampling rates. Experiments demonstrate that AEMG improves the zero-shot leave-one-subject-out (LOSO) accuracy by 5.79-9.25% compared to six state-of-the-art baselines, and achieves more than 90% few-shot adaptation performance with only 5% of target user data. Our work has proposed the concept of EMG signals as a cross-device physiological language, learned their grammar from massive amounts of data, and laid the groundwork for a single-training, universally applicable EMG foundation model.

---


### 73. [CuraView: A Multi-Agent Framework for Medical Hallucination Detection with GraphRAG-Enhanced Knowledge Verification](https://arxiv.org/abs/2605.03476)

**<font color=#1a73e8>作者：</font>** Severin Ye, Xiao Kong, Xiaopeng He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discharge summaries require extracting critical information from lengthy electronic health records (EHRs), a process that is labor-intensive when performed manually. Large language models (LLMs) can improve generation efficiency; however, they are prone to producing faithfulness hallucinations, statements that contradict source records, posing direct risks to patient safety. To address this, we present CuraView, a multi-agent framework for sentence-level detection and evidence-grounded explanation of faithfulness hallucinations in discharge summaries. CuraView constructs a GraphRAG-based knowledge graph from patient-level EHRs and implements a closed-loop generation-detection pipeline with sentence-level evidence retrieval and classification spanning four evidence grades from strong support to direct contradiction (E1-E4), yielding structured and interpretable evidence chains.
We evaluate CuraView on a subset of 250 patients from the Discharge-Me benchmark, with 50 patients held out for testing. Our fine-tuned Qwen3-14B detection model achieves an F1 of 0.831 on the safety-critical E4 metric (90.9% recall, 76.5% precision) and an F1 of 0.823 on E3+E4, representing a 50.0% relative improvement over the base model and outperforming RAGTruth-style and QAGS-style baselines. These results demonstrate that evidence-chain-based graph retrieval verification substantially improves the factual reliability of clinical documentation, while simultaneously producing reusable annotated datasets for downstream model training and distillation.

---


### 74. [MHPR: Multidimensional Human Perception and Reasoning Benchmark for Large Vision-Languate Models](https://arxiv.org/abs/2605.03485)

**<font color=#1a73e8>作者：</font>** Kangkang Wang, Qinting Jiang, Wanping Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multidimensional human understanding is essential for real-world applications such as film analysis and virtual digital humans, yet current LVLM benchmarks largely focus on single-task settings and lack fine-grained, human-centric evaluation. In this work, we introduce MHPR, a comprehensive benchmark for joint perception-reasoning over human-centric scenes spanning individual, multi-person, and human-object interaction dimensions. MHPR comprises a multi-level data design-Captioned Raw Data (C-RD), Supervised Fine-Tuning Data (SFT-D), Reinforcement Learning Data (RL-D), and Test Data (T-D)-together with an automated caption/VQA generation pipeline (ACVG) that performs category-wise attribute decomposition, attribute-specific rewriting, and multi-model voting to ensure high-quality, scalable annotations. We evaluate state-of-the-art vision-language models on fine-grained attributes (appearance, clothing, pose, parts) and high-level semantics (social relations, action semantics, spatial relations, intent and functionality). Our findings show that: 1) format-aligned SFT data substantially improves instruction following and stability; 2) challenge-focused RL data derived from bad-case analysis further enhances perception and reasoning on difficult instances; and 3) training Qwen2.5-VL-7B with MHPR yields significant gains, achieving near-parity with considerably larger models. We release ACVG and MHPR to facilitate reproducible, extensible research on human-centric perception and reasoning.

---


### 75. [Revisiting Graph-Tokenizing Large Language Models: A Systematic Evaluation of Graph Token Understanding](https://arxiv.org/abs/2605.03514)

**<font color=#1a73e8>作者：</font>** Zhongjian Zhang, Yue Yu, Mengmei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The remarkable success of large language models (LLMs) has motivated researchers to adapt them as universal predictors for various graph tasks. As a widely recognized paradigm, Graph-Tokenizing LLMs (GTokenLLMs) compress complex graph data into graph tokens and treat them as prefix tokens for querying LLMs, leading many to believe that LLMs can understand graphs more effectively and efficiently. In this paper, we challenge this belief: \textit{Do GTokenLLMs fully understand graph tokens in the natural-language embedding space?} Motivated by this question, we formalize a unified framework for GTokenLLMs and propose an evaluation pipeline, \textbf{GTEval}, to assess graph-token understanding via instruction transformations at the format and content levels. We conduct extensive experiments on 6 representative GTokenLLMs with GTEval. The primary findings are as follows: (1) Existing GTokenLLMs do not fully understand graph tokens. They exhibit over-sensitivity or over-insensitivity to instruction changes, and rely heavily on text for reasoning; (2) Although graph tokens preserve task-relevant graph information and receive attention across LLM layers, their utilization varies across models and instruction variants; (3) Additional instruction tuning can improve performance on the original and seen instructions, but it does not fully address the challenge of graph-token understanding, calling for further improvement.

---


### 76. [SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective Retrieval-Augmented Generation](https://arxiv.org/abs/2605.03534)

**<font color=#1a73e8>作者：</font>** Jingxi Qiu, Zeyu Han, Cheng Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) grounds answers in retrieved passages, but retrieval is not verification: a passage can be topical and still fail to justify the answer. We frame this gap as evidence sufficiency verification for selective RAG answering: given a question, a candidate answer, and retrieved evidence, predict whether the evidence supports, refutes, or is insufficient, and abstain unless support is established. We present SURE-RAG, a transparent aggregation protocol built on the observation that evidence sufficiency is a set-level property: missing hops and unresolved conflicts cannot be detected by independent passage scoring. A shared pair-level claim-evidence verifier produces local relation distributions, which SURE-RAG aggregates into interpretable answer-level signals -- coverage, relation strength, disagreement, conflict, and retrieval uncertainty -- yielding a three-way decision and an auditable selective score. We evaluate on HotpotQA-RAG v3, a controlled multi-hop benchmark, under an artifact-aware protocol (shortcut baselines, counterfactual swaps, no-oracle checks, GPT-4o audits). Calibrated SURE-RAG reaches 0.9075 Macro-F1 (0.8951 +/- 0.0069), substantially above DeBERTa mean-pooling (0.6516) and a GPT-4o judge (0.7284), while matching a strong but opaque concat cross-encoder (0.8888 +/- 0.0109) with full auditability. Risk at 30% coverage drops from 0.2588 to 0.1642, a 37% reduction in unsafe answers. To deliberately probe the task boundary, we further contrast SURE-RAG with GPT-4o on HaluBench unsafe detection: the ranking reverses (0.3343 vs 0.7389 unsafe-F1), establishing that controlled sufficiency verification and natural hallucination detection are distinct problems.

---


### 77. [Erase Persona, Forget Lore: Benchmarking Multimodal Copyright Unlearning in Large Vision Language Models](https://arxiv.org/abs/2605.03547)

**<font color=#1a73e8>作者：</font>** JuneHyoung Kwon, JungMin Yun, YoungBin Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs), trained on web-scale data, risk memorizing and regenerating copyrighted visual content such as characters and logos, creating significant challenges. Machine unlearning offers a path to mitigate these risks by removing specific content post-training, but evaluating its effectiveness, especially in the complex multimodal setting of LVLMs, remains an open problem. Current evaluation methods often lack robustness or fail to capture the nuances of cross-modal concept erasure. To address this critical gap, we introduce the CoVUBench benchmark, the first framework specifically designed for evaluating copyright content unlearning in LVLMs. CoVUBench utilizes procedurally generated, legally safe synthetic data coupled with systematic visual variations spanning compositional changes and diverse domain manifestations to ensure realistic and robust evaluation of unlearning generalization. Our comprehensive multimodal evaluation protocol assesses both forgetting efficacy from the copyright holder perspective and the preservation of general model utility from the deployer viewpoint. By rigorously measuring this crucial trade-off, CoVUBench provides a standardized tool to advance the development of responsible and effective unlearning methods for LVLMs.

---


### 78. [AfriVox-v2: A Domain-Verticalized Benchmark for In-the-Wild African Speech Recognition](https://arxiv.org/abs/2605.03590)

**<font color=#1a73e8>作者：</font>** Busayo Awobade, Gabrial Zencha Ashungafac, Tobi Olatunji  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent large language models (LLMs) show strong speech recognition and translation capabilities for high-resource languages. However, African languages remain dramatically underrepresented in benchmarks, limiting their practical use in low-resource settings. While early benchmarks tested African languages and accents, they lacked exhaustive real-world noise and granular domain evaluations. We present AfriVox-v2, a comprehensive benchmark designed to test speech models under realistic African deployment conditions. AfriVox-v2 introduces "in the wild" unscripted audio for all supported languages. We also introduce strict domain verticalization, evaluating model accuracy across ten sectors including government, finance, health, and agriculture and conducting targeted tests on numbers and named entities. Finally, we benchmark a new generation of speech models, including Sahara-v2, Gemini 3 Flash, and the Omnilingual CTC models. Our results expose the true generalization gap of modern speech models in specialized, noisy African contexts and provide a reliable blueprint for developers building localized voice AI.

---


### 79. [Where Paths Split: Localized, Calibrated Control of Moral Reasoning in Large Language Models](https://arxiv.org/abs/2605.03609)

**<font color=#1a73e8>作者：</font>** Chenchen Yuan, Zheyu Zhang, Gjergji Kasneci  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models often display heterogeneous moral preferences across settings. We study inference-time steering toward a desired ethical framework while preserving general competence. We present Convergent-Divergent Routing, which traces and edits minimal branch points inside transformer blocks where ethical-framework-related pathways first converge and then diverge. Gating non-target branches at these loci blocks the downstream propagation while leaving upstream computations intact. We find that this intervention alone increases targeted ethical-framework reasoning. To achieve fine-grained control, we adapt Common Spatial Patterns to the residual stream and extract, for each branch-point layer, a pair of directions that discriminate between utilitarian and deontological frameworks. We then introduce Dual Logit Calibration, a closed-form, minimum-$\ell_2$-norm update that moves the residual within this two-dimensional subspace so the resulting directional projections align with user-specified preference weights. Experiments on real-life moral dilemmas show that our method reliably achieves preference calibration and largely preserves general capabilities, outperforming recent baselines while providing an interpretable mechanism.

---


### 80. [BIT.UA-AAUBS at ArchEHR-QA 2026: Evaluating Open-Source and Proprietary LLMs via Prompting in Low-Resource QA](https://arxiv.org/abs/2605.03618)

**<font color=#1a73e8>作者：</font>** Richard A. A. Jonker, Alexander Christiansen, Alexandros Maniatis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents the joint participation of the this http URL and AAUBS groups in the ArchEHR-QA 2026 shared task, which focuses on clinical question answering and evidence grounding in a low-resource setting. Due to the absence of training data and the strict data privacy constraints inherent to the healthcare domain (e.g. GDPR), we investigate the capabilities of Large Language Models (LLMs) without weight updates. We evaluate several state-of-the-art proprietary models and locally deployable open-source alternatives using various prompt engineering strategies, including task decomposition, Chain-of-Thought, and in-context learning. Furthermore, we explore majority voting and LLM-as-a-judge ensembling techniques to maximize predictive robustness. Our results demonstrate that while proprietary models exhibit strong resilience to prompt variations, domain-adapted open-source models (such as MedGemma 3 27B) achieve highly competitive performance when paired with the right prompt. Overall, our prompt-based approach proved highly effective, securing 1st place in Subtask 4 (evidence citation alignment) and 3rd place in Subtask 3 (patient-friendly answer generation). All code, results, and prompts are available on our GitHub repository: this https URL.

---


### 81. [Annotation Quality in Aspect-Based Sentiment Analysis: A Case Study Comparing Experts, Students, Crowdworkers, and Large Language Model](https://arxiv.org/abs/2605.03624)

**<font color=#1a73e8>作者：</font>** Niklas Donhauser, Jakob Fehle, Nils Constantin Hellwig 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect-Based Sentiment Analysis (ABSA) enables fine-grained opinion analysis by identifying sentiments toward specific aspects or targets within a text. While ABSA has been widely studied for English, research on other languages such as German remains limited, largely due to the lack of high-quality annotated datasets. This paper examines how different annotation sources influence the development of German ABSA. To this end, an existing dataset is re-annotated by experts to establish a ground truth, which serves as a reference for evaluating annotations produced by students, crowdworkers, Large Language Models (LLMs), and experts. Annotation quality is compared using Inter-Annotator Agreement (IAA) and its impact on downstream model performance for different ABSA subtasks. The evaluation focuses on Aspect Category Sentiment Analysis (ACSA) and Target Aspect Sentiment Detection (TASD). We apply State-of-the-Art (SOTA) methods for ABSA, including BERT-, T5-, and LLaMA-based approaches to assess performance differences, spanning fine-tuning and in-context learning with instruction prompts. The findings provide practical insights into trade-offs between annotation reliability and efficiency, offering guidance for dataset construction in under-resourced Natural Language Processing (NLP) scenarios.

---


### 82. [The Detector Teaches Itself: Lightweight Self-Supervised Adaptation for Open-Vocabulary Object Detection](https://arxiv.org/abs/2605.03642)

**<font color=#1a73e8>作者：</font>** Yazhe Wan, Changjae Oh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary object detection aims to recognize objects from an open set of categories, which leverages vision-language models (VLMs) pre-trained on large-scale image-text data. The cooperative paradigm combines an object detector with a VLM to achieve zero-shot recognition of novel objects. However, VLMs pre-trained on full images often struggle to capture local object details, limiting their effectiveness when applied to region-level detection. We present Decoupled Adaptivity Training (DAT), a self-supervised fine-tuning approach to improve VLMs for cooperative model-based object detection. Given a cooperative model consists of a closed-set detector and a VLM, we first construct a region-aware pseudo-labeled dataset using a pre-trained closed-set object detector, in which regions corresponding to novel objects may be present but remain unlabeled or mislabeled. We then fine-tune the visual backbone of the VLM in a decoupled manner, which enhances local feature alignment while preserving global semantic knowledge via weight interpolation. DAT is a plug-and-play module that requires no inference overhead and fine-tunes less than 0.8M parameters. Experiments on the COCO and LVIS datasets show that DAT consistently improves detection performance on both novel and known categories, establishing a new state of the art in cooperative open-vocabulary detection.

---


### 83. [AdapShot: Adaptive Many-Shot In-Context Learning with Semantic-Aware KV Cache Reuse](https://arxiv.org/abs/2605.03644)

**<font color=#1a73e8>作者：</font>** Jie Ou, Jinyu Guo, Shiyao Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many-Shot In-Context Learning (ICL) has emerged as a promising paradigm, leveraging extensive examples to unlock the reasoning potential of Large Language Models (LLMs). However, existing methods typically rely on a predetermined, fixed number of shots. This static approach often fails to adapt to the varying difficulty of different queries, leading to either insufficient context or interference from noise. Furthermore, the prohibitive computational and memory costs of long contexts severely limit Many-Shot's feasibility. To address the above limitations, we propose AdapShot, which dynamically optimizes shot counts and leverages KV cache reuse for efficient inference. Specifically, we design a probe-based evaluation mechanism that utilizes output entropy to determine the optimal number of shots. To bypass the redundant prefilling computation during both the probing and inference phases, we incorporate a semantics-aware KV cache reuse strategy. Within this reuse strategy, to address positional encoding incompatibilities, we introduce a decoupling and re-encoding method that enables the flexible reordering of cached key-value pairs. Extensive experiments demonstrate that AdapShot achieves an average performance gain of around 10% and a 4.64x speedup compared to state-of-the-art DBSA.

---


### 84. [ELAS: Efficient Pre-Training of Low-Rank Large Language Models via 2:4 Activation Sparsity](https://arxiv.org/abs/2605.03667)

**<font color=#1a73e8>作者：</font>** Jiaxi Li, Lu Yin, Li Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved remarkable capabilities, but their immense computational demands during training remain a critical bottleneck for widespread adoption. Low-rank training has received attention in recent years due to its ability to significantly reduce training memory usage. Meanwhile, applying 2:4 structured sparsity to weights and activations to leverage NVIDIA GPU support for 2:4 structured sparse format has become a promising direction. However, existing low-rank methods often leave activation matrices in full-rank, which dominates memory consumption and limits throughput during large-batch training. Furthermore, directly applying sparsity to weights often leads to non-negligible performance degradation. To achieve efficient pre-training of LLMs, this paper proposes ELAS: Efficient pre-training of Low-rank LLMs via 2:4 Activation Sparsity, a novel framework for low-rank models via 2:4 activation sparsity. ELAS applies squared ReLU activation functions to the feed-forward networks in low-rank models and implements 2:4 structured sparsity on the activations after the squared ReLU operation. We evaluated ELAS through pre-training experiments on LLaMA models ranging from 60M to 1B parameters. The results demonstrate that ELAS maintains performance with minimal degradation after applying 2:4 activation sparsity, while achieving training and inference acceleration. Moreover, ELAS reduces activation memory overhead, particularly with large batch sizes. Code is available at ELAS Repo.

---


### 85. [MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents](https://arxiv.org/abs/2605.03675)

**<font color=#1a73e8>作者：</font>** Bronislav Sidik, Lior Rokach  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running autonomous AI agents suffer from a well-documented memory coherence problem: tool-execution success rates degrade 14 percentage points over 72-hour operation windows due to four compounding failure modes in existing flat-file memory systems. We present MEMTIER, a tripartite memory architecture for the OpenClaw agent runtime that introduces a structured episodic JSONL store, a five-signal weighted retrieval engine, an attention-attributed cognitive weight update loop, an asynchronous consolidation daemon promoting episodic facts to a semantic tier, and a PPO-based policy framework for adapting retrieval weights (infrastructure validated; performance gains pending camera-ready). On the full 500-question LongMemEval-S benchmark (Wu et al., 2025), MEMTIER achieves Acc=0.382, F1=0.412 with Qwen2.5-7B on a consumer 6GB GPU - a +33 percentage point improvement over the full-context baseline (0.050 -> 0.382, i.e., 5% -> 38%). With DeepSeek-V4-Flash fact pre-population, single-session recall reaches 0.686-0.714, exceeding the paper's RAG BM25 GPT-4o baseline (0.560) on those categories. Temporal reasoning rises to 0.323 and multi-session synthesis to 0.173, demonstrating that structured semantic pre-population qualitatively changes what lightweight retrieval can achieve. All phases run locally on a consumer laptop with a 6GB GPU.

---


### 86. [Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe](https://arxiv.org/abs/2605.03677)

**<font color=#1a73e8>作者：</font>** Wenjin Hou, Shangpin Peng, Weinong Wang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has recently emerged as an effective post-training paradigm for consolidating the capabilities of specialized expert models into a single student model. Despite its empirical success, the conditions under which OPD yields reliable improvement remain poorly understood. In this work, we identify two fundamental bottlenecks that limit effective OPD: insufficient exploration of informative states and unreliable teacher supervision for student rollouts. Building on this insight, we propose Uni-OPD, a unified OPD framework that generalizes across Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs), centered on a dual-perspective optimization strategy. Specifically, from the student's perspective, we adopt two data balancing strategies to promote exploration of informative student-generated states during training. From the teacher's perspective, we show that reliable supervision hinges on whether aggregated token-level guidance remains order-consistent with the outcome reward. To this end, we develop an outcome-guided margin calibration mechanism to restore order consistency between correct and incorrect trajectories. We conduct extensive experiments on 5 domains and 16 benchmarks covering diverse settings, including single-teacher and multi-teacher distillation across LLMs and MLLMs, strong-to-weak distillation, and cross-modal distillation. Our results verify the effectiveness and versatility of Uni-OPD and provide practical insights into reliable OPD.

---


### 87. [From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT](https://arxiv.org/abs/2605.03686)

**<font color=#1a73e8>作者：</font>** Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated Machine Learning (AutoML) frameworks increasingly leverage Large Language Models (LLMs) for tasks such as hyperparameter optimization and neural architecture code generation. However, current LLM-based approaches focus on generative outputs and evaluate them by training the produced artifacts. Whether LLMs can learn to reason about neural network performance across datasets remains underexplored. We present a classification task integrated into the NNGPT framework, in which a fine-tuned LLM predicts which of two image classification datasets a given neural network architecture achieves higher accuracy on. The task is built on the LEMUR dataset, which provides standardized PyTorch implementations with reproducible performance metrics. Three prompt configurations of increasing difficulty are evaluated: a normalized-accuracy baseline (trivially reaching 100%), a metadata-enriched prompt replacing accuracies with dataset properties, and a code-only prompt presenting only architecture source code and dataset names. Using DeepSeek-Coder-7B-Instruct fine-tuned with LoRA, the code-only prompt reaches 80% peak accuracy over 15 epochs, while the metadata prompt peaks at 70%. Perdataset analysis reveals complementary strengths: metadata excels for datasets with distinctive properties (CelebAGender at 90.9%) but degrades for overlapping characteristics, whereas the code-only prompt shows more balanced performance. A comparison with DeepSeek-Coder1.3B confirms that model capacity affects this form of architectural reasoning. The results establish that LLMs can be fine-tuned to predict cross-dataset suitability from neural network code, suggesting that architecture source code contains richer discriminative signal than dataset metadata alone.

---


### 88. [SERE: Structural Example Retrieval for Enhancing LLMs in Event Causality Identification](https://arxiv.org/abs/2605.03701)

**<font color=#1a73e8>作者：</font>** Zhifeng Hao, Zhongjie Chen, Junhao Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Event Causality Identification (ECI) requires models to determine whether a given pair of events in a context exhibits a causal relationship. While Large Language Models (LLMs) have demonstrated strong performance across various NLP tasks, their effectiveness in ECI remains limited due to biases in causal reasoning, often leading to overprediction of causal relationships (causal hallucination). To mitigate these issues and enhance LLM performance in ECI, we propose SERE, a structural example retrieval framework that leverages LLMs' few-shot learning capabilities. SERE introduces an innovative retrieval mechanism based on three structural concepts: (i) Conceptual Path Metric, which measures the conceptual relationship between events using edit distance in ConceptNet; (ii) Syntactic Metric, which quantifies structural similarity through tree edit distance on syntactic trees; and (iii) Causal Pattern Filtering, which filters examples based on predefined causal structures using LLMs. By integrating these structural retrieval strategies, SERE selects more relevant examples to guide LLMs in causal reasoning, mitigating bias and improving accuracy in ECI tasks. Extensive experiments on multiple ECI datasets validate the effectiveness of SERE. The source code is publicly available at this https URL.

---


### 89. [SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition](https://arxiv.org/abs/2605.03706)

**<font color=#1a73e8>作者：</font>** Ruichu Cai, Juntao Gan, Miao Mai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Zero-shot Named Entity Recognition (ZS-NER) remains brittle under domain and schema shifts, where unseen label definitions often misalign with a large language model's (LLM's) intrinsic semantic organization. As a result, directly mapping entity mentions to fine-grained target labels can induce systematic semantic drift, especially when target schemas are novel or semantically overlapping. We propose \textbf{SAM-NER}, a three-stage framework based on \emph{Semantic Archetype Mediation} that stabilizes cross-domain transfer through an intermediate, domain-invariant archetype space. SAM-NER: (i) performs \emph{Entity Discovery} via cooperative extraction and consensus-based denoising to obtain high-coverage, high-fidelity entity spans; (ii) conducts \emph{Abstract Mediation} by projecting entities into a compact set of universal semantic archetypes distilled from high-level ontological abstractions; and (iii) applies \emph{Semantic Calibration} to resolve archetype-level predictions into target-domain types through constrained, definition-aligned inference with a frozen LLM. Experiments on the CrossNER benchmark show that SAM-NER consistently outperforms strong prior ZS-NER baselines in cross-domain settings. Our implementation will be open-sourced at this https URL.

---


### 90. [Unified Multimodal Visual Tracking with Dual Mixture-of-Experts](https://arxiv.org/abs/2605.03716)

**<font color=#1a73e8>作者：</font>** Lingyi Hong, Jinglun Li, Xinyu Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal visual object tracking can be divided into to several kinds of tasks (e.g. RGB and RGB+X tracking), based on the input modality. Existing methods often train separate models for each modality or rely on pretrained models to adapt to new modalities, which limits efficiency, scalability, and usability. Thus, we introduce OneTrackerV2, a unified multi-modal tracking framework that enables end-to-end training for any modality. We propose Meta Merger to embed multi-modal information into a unified space, allowing flexible modality fusion and robustness. We further introduce Dual Mixture-of-Experts (DMoE): T-MoE models spatio-temporal relations for tracking, while M-MoE embeds multi-modal knowledge, disentangling cross-modal dependencies and reducing feature conflicts. With a shared architecture, unified parameters, and a single end-to-end training, OneTrackerV2 achieves state-of-the-art performance across five RGB and RGB+X tracking tasks and 12 benchmarks, while maintaining high inference efficiency. Notably, even after model compression, OneTrackerV2 retains strong performance. Moreover, OneTrackerV2 demonstrates remarkable robustness under modality-missing scenarios.

---


### 91. [Rose-SQL: Role-State Evolution Guided Structured Reasoning for Multi-Turn Text-to-SQL](https://arxiv.org/abs/2605.03720)

**<font color=#1a73e8>作者：</font>** Le Zhou, Feng Yao, Fengcai Qiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Reasoning Models (LRMs) trained with Long Chain-of-Thought have demonstrated remarkable capabilities in code generation and mathematical reasoning. However, their potential in multi-turn Text-to-SQL tasks remains largely underexplored. Existing approaches typically rely on unstable API-based inference or require expensive fine-tuning on small-scale models. In this work, we present Rose-SQL, a training-free framework that leverages small-scale LRMs through in-context learning to enable accurate context-dependent parsing. We introduce the Role-State, a fine-grained representation that bridges the structural gap between schema linking and SQL generation by serving as a structural blueprint. To handle conversational dependencies, Rose-SQL traces the evolution of Role-State through historical context via structural isomorphism checks, guiding the model to infer the possible SQL composition for the current question through verified interaction trajectories. Experiments on the SParC and CoSQL benchmarks show that, within the Qwen3 series, Rose-SQL outperforms in-context learning baselines at the 4B scale and substantially surpasses state-of-the-art fine-tuned models at the 8B and 14B scales, while showing consistent gains on additional reasoning backbones.

---


### 92. [Segmenting Human-LLM Co-authored Text via Change Point Detection](https://arxiv.org/abs/2605.03723)

**<font color=#1a73e8>作者：</font>** Mengchu Li, Jin Zhu, Jinglai Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rise of large language models (LLMs) has created an urgent need to distinguish between human-written and LLM-generated text to ensure authenticity and societal trust. Existing detectors typically provide a binary classification for an entire passage; however, this is insufficient for human--LLM co-authored text, where the objective is to localize specific segments authored by humans or LLMs. To bridge this gap, we propose algorithms to segment text into human- and LLM-authored pieces. Our key observation is that such a segmentation task is conceptually similar to classical change point detection in time-series analysis. Leveraging this analogy, we adapt change point detection to LLM-generated text detection, develop a weighted algorithm and a generalized algorithm to accommodate heterogeneous detection score variability, and establish the minimax optimality of our procedure. Empirically, we demonstrate the strong performance of our approach against a wide range of existing baselines.

---


### 93. [Rethinking the Rank Threshold for LoRA Fine-Tuning](https://arxiv.org/abs/2605.03724)

**<font color=#1a73e8>作者：</font>** Juneyoung Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A recent landscape analysis of LoRA fine-tuning in the neural tangent kernel regime establishes a sufficient condition $r(r+1)/2 > KN$ on the LoRA rank $r$ for the absence of spurious local minima under squared-error loss, prescribing $r \geq 12$ on canonical few-shot RoBERTa setups. The condition is stated for general output dimension $K$, so its sharpness in any particular regime, and its practical implication for the cross-entropy loss actually used in fine-tuning, are open. We give three results that together reduce the prescribed rank to $r = 1$ for binary classification in this regime. First, replacing the symmetric Sard-form count with the non-symmetric LoRA manifold dimension yields a strictly weaker capacity requirement, $r(m+n) - r^2 > C^* \cdot KN$ with $C^* \approx 1.35$ under Gaussian-iid features, satisfied at $r = 1$ on canonical setups. Second, in the cross-entropy setting the Polyak--Łojasiewicz inequality removes the rank threshold entirely. Third, a Rademacher-complexity bound predicts rank-one variance optimality precisely when the bias term is saturated, which is the case for binary classification but not for $K > 2$. Empirically, across four GLUE-style binary tasks, three encoder architectures, and at scale on RoBERTa-large, rank one is competitive with the existing prescription $r = 12$; on multi-class MNLI the optimal rank shifts above one, also as predicted. The binary-regime guarantees are conditional on standard NTK assumptions; the multi-class extension is left to future work.

---


### 94. [Benchmarking Parameter-Efficient Fine-Tuning of Large Language Models for Low-Resource Tajik Text Generation with the Tajik Web Corpus](https://arxiv.org/abs/2605.03742)

**<font color=#1a73e8>作者：</font>** Mullosharaf K. Arabov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper is devoted to the adaptation of generative large language models for the Tajik language, a low-resource language with Cyrillic script. To overcome the shortage of digital text resources, the author created and publicly released the Tajik Web Corpus, the largest open-access corpus of Tajik, comprising 319,298 documents (~1.11 billion characters). On a subsample of 10,000 documents, 17 configurations were benchmarked, covering autoregressive, encoder-decoder, and encoder-only models with three fine-tuning strategies: full fine-tuning, LoRA, and QLoRA (ranks 8 and 16). Quality was assessed via perplexity and cross-entropy loss; peak GPU memory and training time were also recorded. Best results were achieved by Mistral 7B with QLoRA (r=16): mean perplexity 5.03, standard deviation 0.03. Increasing rank from 8 to 16 gave statistically insignificant improvement while raising memory consumption. For small GPT-2 family models, full fine-tuning yielded lower perplexity (3.48 for GPT-2 Medium) than LoRA (7.60-8.42), but induced catastrophic forgetting. The encoder-only XLM-RoBERTa showed the worst results (perplexity 59.3). The novelty lies in creating the largest verified Tajik corpus and the first systematic analysis of PEFT effectiveness for Tajik text generation. Practical value lies in recommendations for architecture and fine-tuning strategy selection, optimizing computational costs without substantial quality loss.

---


### 95. [Before Forgetting, Learn to Remember: Revisiting Foundational Learning Failures in LVLM Unlearning Benchmarks](https://arxiv.org/abs/2605.03759)

**<font color=#1a73e8>作者：</font>** JuneHyoung Kwon, MiHyeon Kim, Eunju Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Large Vision-Language Models (LVLMs) offer powerful capabilities, they pose privacy risks by unintentionally memorizing sensitive personal information. Current unlearning benchmarks attempt to mitigate this using fictitious identities but overlook a critical stage 1 failure: models fail to effectively memorize target information initially, rendering subsequent unlearning evaluations unreliable. Diagnosing under-memorization and the multi-hop curse as root causes, we introduce ReMem, a Reliable Multi-hop and Multi-image Memorization Benchmark. ReMem ensures robust foundational learning through principled data scaling, reasoning-aware QA pairs, and diverse visual contexts. Additionally, we propose a novel Exposure metric to quantify the depth of information erasure from the model's internal probability distribution. Extensive experiments demonstrate that ReMem provides a rigorous and trustworthy framework for diagnosing both learning and unlearning behaviors in LVLMs.

---


### 96. [OracleProto: A Reproducible Framework for Benchmarking LLM Native Forecasting via Knowledge Cutoff and Temporal Masking](https://arxiv.org/abs/2605.03762)

**<font color=#1a73e8>作者：</font>** Yiding Ma, Chengyun Ruan, Kaibo Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are moving from static text generators toward real-world decision-support systems, where forecasting is a composite capability that links information gathering, evidence integration, situational judgment, and action-oriented decision making. This capability is in broad demand across finance, policy, industry, and scientific research, yet its evaluation remains difficult: live benchmarks evaluate forecasts before answers exist, making them the cleanest way to measure forecasting ability, but they expire once events resolve; retrospective benchmarks are reproducible, but they cannot reliably distinguish genuine forecasting from facts a model may have already learned during pretraining. Prompting models to "pretend not to know" cannot replace a genuine knowledge boundary. We propose OracleProto, a reproducible framework for evaluating LLM native forecasting capability. OracleProto reconstructs resolved events into time-bounded forecasting samples by combining model-cutoff-aligned sample admission, tool-level temporal masking, content-level leakage detection, discrete answer normalization, and hierarchical scoring. Instantiated on a FutureX-Past-derived dataset with six contemporary LLMs, OracleProto distinguishes forecasting quality, sampling stability, and cost efficiency under controlled information boundaries, while reducing residual leakage to the $1\%$ level, an order of magnitude below tool-only temporal filtering. OracleProto turns LLM forecasting from one-off evaluation into an auditable, reusable, and trainable dataset-level capability, providing a unified interface for fair cross-model comparison and a controlled signal source for downstream SFT and RL. Code and data are available at this https URL and this https URL.

---


### 97. [Nora: Normalized Orthogonal Row Alignment for Scalable Matrix Optimizer](https://arxiv.org/abs/2605.03769)

**<font color=#1a73e8>作者：</font>** Jinghui Yuan, Jiaxuan Zou, Shuo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix-based optimizers have demonstrated immense potential in training Large Language Models (LLMs), however, designing an ideal optimizer remains a formidable challenge. A superior optimizer must satisfy three core desiderata: efficiency, achieving Muon-like preconditioning to accelerate optimization; stability, strictly adhering to the scale-invariance inherent in neural networks; and speed, minimizing computational overhead. While existing methods address these aspects to varying degrees, they often fail to unify them, either incurring prohibitive computational costs like Muon, or allowing radial jitters that compromise stability like RMNP. To bridge this gap, we propose Nora, an optimizer that rigorously satisfies all three requirements. Nora achieves training stability by explicitly stabilizing weight norms and angular velocities through row-wise momentum projection onto the orthogonal complement of the weights. Simultaneously, by leveraging the block-diagonal dominance of the Transformer Hessian, Nora effectively approximates structured preconditioning while maintaining an optimal computational complexity of $\mathcal{O}(mn)$. Furthermore, we prove that Nora is a scalable optimizer and establish its corresponding scaling theorems. With a streamlined implementation requiring only two lines of code, our preliminary experiments validate Nora as an efficient and highly promising optimizer for large-scale training.

---


### 98. [Say the Mission, Execute the Swarm: Agent-Enhanced LLM Reasoning in the Web-of-Drones](https://arxiv.org/abs/2605.03788)

**<font color=#1a73e8>作者：</font>** Andrea Iannoli, Lorenzo Gigli, Luca Sciullo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly explored as high-level reasoning engines for cyber-physical systems, yet their application to real-time UAV swarm management remains challenging due to heterogeneous interfaces, limited grounding, and the need for long-running closed-loop execution. This paper presents a mission-agnostic, agent-enhanced LLM framework for UAV swarm control, where users express mission objectives in natural language and the system autonomously executes them through grounded, real-time interactions. The proposed architecture combines an LLM-based Agent Core with a Model Context Protocol (MCP) gateway and a Web-of-Drones abstraction based on W3C Web of Things (WoT) standards. By exposing drones, sensors, and services as standardized WoT Things, the framework enables structured tool-based interaction, continuous state observation, and safe actuation without relying on code generation. We evaluate the framework using ArduPilot-based simulation across four swarm missions and six state-of-the-art LLMs. Results show that, despite strong reasoning abilities, current general-purpose LLMs still struggle to achieve reliable execution - even for simple swarm tasks - when operating without explicit grounding and execution support. Task-specific planning tools and runtime guardrails substantially improve robustness, while token consumption alone is not indicative of execution quality or reliability.

---


### 99. [Enhancing Visual Question Answering with Multimodal LLMs via Chain-of-Question Guided Retrieval-Augmented Generation](https://arxiv.org/abs/2605.03790)

**<font color=#1a73e8>作者：</font>** Quanxing Xu, Ling Zhou, Xian Zhong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With advances in multimodal research and deep learning, Multimodal Large Language Models (MLLMs) have emerged as a powerful paradigm for a wide range of multimodal tasks. As a core problem in vision-language research, Visual Question Answering (VQA) has increasingly employed MLLMs to improve performance, particularly in open-domain settings where external knowledge is essential. In this work, we aim to further enhance retrieval-based VQA by more effectively integrating MLLMs with structured reasoning and knowledge acquisition. We introduce a logical prompting strategy that fuses Chain-of-Thought (CoT) reasoning with Visual Question Decomposition (VQD), termed CoVQD, to guide retrieval toward more accurate and relevant knowledge for MLLM inference. Building on this idea, we propose a new framework, CoVQD-guided RAG (CgRAG), which enables MLLMs to access more comprehensive and coherent external knowledge while benefiting from structured visual-text reasoning guidance, thereby improving generalization and reliability in complex cross-domain VQA scenarios. Extensive experiments on E-VQA, InfoSeek, and OKVQA benchmarks demonstrate the effectiveness of the proposed method.

---


### 100. [TriBench-Ko: Evaluating LLM Risks in Judicial Workflows](https://arxiv.org/abs/2605.03792)

**<font color=#1a73e8>作者：</font>** Haesung Lee, Gyubin Choi, Eun-Ju Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly integrated into legal workflows. However, existing benchmarks primarily address proxy tasks, such as bar examination performance or classification, which fail to capture the performance and risks inherent in day-to-day judicial processes. To address this, we publicly release TriBench-Ko, a Korean benchmark designed to evaluate potential deployment risks of LLMs within the context of verified judicial task requirements. It covers four core tasks: jurisprudence summarization, precedent retrieval, legal issue extraction, and evidence analysis. It jointly assesses model behavior across multiple deployment risk categories, including inaccuracy (hallucination, omission, statutory misapplication), biases (demographic, overcompliance), inconsistencies (prompt sensitivity, non-determinism), and adjudicative overreach. Each item is structured to systematically assess both task performance and a specific risk type based on real judicial decisions. Our evaluation of a range of contemporary LLMs reveals that many models frequently manifest significant risks, most notably struggling with precedent retrieval and failing to capture critical legal information. We provide a comprehensive diagnosis of these LLMs and pinpoint critical areas where LLM-generated outputs in judicial contexts necessitate rigorous inspection and caution. Our dataset and code are available at this https URL

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-130](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

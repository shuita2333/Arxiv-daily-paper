# 📦 其他研究 | 2026年07月03日

> 本类共 **236** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-236](./part-05.md)

---

### 101. [AI, Trust, and Teaming: The Humans-as-Handlers Approach for Autonomous and Opaque AI Systems](https://arxiv.org/abs/2607.00523)

**<font color=#1a73e8>作者：</font>** Nathan G. Wood  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) is becoming ubiquitous, and across domains, increasingly autonomous systems are carrying out tasks which raise significant ethical and legal challenges which demonstrate a need for strong human-machine teams rooted in trust. In this article, I argue that within highly impactful areas (such as medicine or warfighting) there are grounds for us initially treating autonomous and opaque systems as relevantly analogous to dogs (or other animals with which we have close relationships). Under this analogy, humans making use of these systems are not to be viewed as "users" or "deployers" of these systems, but instead take the role of "handlers". This recasting of roles shifts the way we view humans, AI-enabled and autonomous systems, and the relations between them, and moreover clarifies the clear and traceable lines of responsibility humans have for the outcomes brought about when using these systems. In developing this point, I clarify that the machine-animal analogy does admit disanalogous elements, but that its touch-points ground it as a starting point. I then explore how we can divest the humans-as-handlers approach of those aspects of our relationships with animals which are unfitting for how we engage with and make use of autonomous and AI-enabled systems. I conclude by arguing that the trajectory of human-machine teamings for autonomous and AI-enabled systems should be a state where we authentically view these not as artifacts which we simply make use of, but as collaborators with which we pursue complex goals and carry out complex tasks.

---


### 102. [SPECSIA: Stylization Dataset for Novel-View Enhancement in Drawing-based 3D Animation](https://arxiv.org/abs/2607.00525)

**<font color=#1a73e8>作者：</font>** Kyuwon Kim, Sunjae Yoon, Chang D. Yoo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating animation from a single 2D drawing is challenging because the output must preserve character appearance while remaining plausible and temporally coherent under motion. Existing drawing-based 3D animation pipelines often use sample-wise 2D refinement to align animated renderings with the input image, but such optimization tends to overfit to the observed view and fails to correct projection-induced artifacts in novel views. To address this limitation, we introduce SPECSIA-15K, a paired stylization dataset containing 14,980 artifact-corrupted projection/refinement-target pairs from 1,498 3DBiCar characters. We further present DraViE (Drawing-based View Enhancement), a lightweight plug-and-play module trained with data-level priors to remove novel-view artifacts while preserving style and motion plausibility. Experiments show consistent gains in novel-view fidelity and temporal coherence with lower per-character adaptation cost than sample-wise fine-tuning.

---


### 103. [AI Native Games: A Survey and Roadmap](https://arxiv.org/abs/2607.00527)

**<font color=#1a73e8>作者：</font>** Zhiyue Xu, Fandi Meng, Kaijie Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI now enables games to produce dialogue, quests, characters, images, and worlds at runtime. Yet generation alone does not make a game AI-native, nor does it guarantee playability. This paper defines AI-native games by whether runtime generative AI is constitutive of the core loop: if the AI component were removed or trivially replaced, the central form of play would collapse or become fundamentally different. This counterfactual criterion separates AI-native games from AI-augmented games, boundary artifacts, chatbots, tavern-style role-play, procedural content generation, and AI-assisted production. Using this definition, we screen candidate artifacts and analyze 53 publicly available AI-native games and prototypes. We introduce a dual-axis G/N taxonomy: the G-axis captures player-facing game type, while the N-axis captures the dominant AI mechanic that makes generative AI indispensable to play. The corpus is concentrated around language-forward designs, especially narrative adventure, epistemic interaction, and generative narrative, while categories such as semantic adjudication, multi-agent simulation, generative construction, and relationship/companion play remain less represented. We argue that the central design problem is organizing semantic openness into stable gameplay. AI-native design depends on mechanical invariants: goals, rules, state, feedback, pacing, and player agency that make open-ended AI outputs interpretable and consequential. We conclude with a roadmap for controllable generation, AI-as-mechanic design, multimodal and multi-agent systems, inference economics, evaluation, safety, and regulation.

---


### 104. [NoPA: Non-Parametric Online 3D Scene Graph Generation](https://arxiv.org/abs/2607.00529)

**<font color=#1a73e8>作者：</font>** Qi Xun Yeo, Seungjun Lee, Yan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classic 3D scene graph generation approaches fail to work in real-time due to the heavy computational cost of environment mapping and the need to generate intermediate point-cloud representations. To alleviate this issue, a recent work eschews point clouds in favor of a lightweight Gaussian distribution for each object. This approximation drastically speeds up inference and enables real-time 3D scene graph generation. However, the representation has two key weaknesses. \textbf{1)} Each object is approximated by a single 3D Gaussian, which causes a severe loss of 3D geometric detail. \textbf{2)} The discrepancy between this approximation and the true object geometry exacerbates the inaccurate merging of object candidates during online inference. To address these issues, we propose \textbf{NoPA}, which represents each object as a separate non-parametric distribution. This formulation retains 3D geometric information while preserving real-time inference of the parametric Gaussian formulation. To build upon our novel object representation, we propose a tailored merging strategy to recover coherent object instances. Specifically, we leverage maximum mean discrepancy on kernel density estimates to enable robust merging of object candidates during online exploration while minimizing added computational complexity. The key is to maintain a fixed particle set per object. Furthermore, to rectify the relation loss caused by misclassified objects, NoPA propagates relationships between objects with high affinity. Experiments show that NoPA substantially outperforms current methods without sacrificing real-time inference speed.

---


### 105. [You Shall Not Pass! Where and Why Developers Draw The Line on AI Autonomy](https://arxiv.org/abs/2607.00533)

**<font color=#1a73e8>作者：</font>** Rudrajit Choudhuri, Christian Bird, Carmen Badea 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI takes on more software work, the line between human and AI effort is shifting. Where developers draw that line around AI autonomy bears on how we design tools and roles that preserve meaningful work. Drawing on cognitive appraisal theory, work design, and automation research, we conducted a mixed-methods study of 448 professional developers at Microsoft to investigate their accepted levels of AI autonomy across software engineering work. Most developers accepted AI producing work under their oversight, although accepted autonomy varied substantively across tasks and individuals. Acceptance was lowest for identity-defining, human-facing, and design-oriented work, and higher among developers with more AI experience and risk tolerance. Task accountability was associated with lower odds of allowing AI to act on developers' behalf, whereas task identity was associated with lower odds of granting AI decision-making autonomy. Task demands had the opposite effect, increasing willingness to delegate decision-making to AI. Our findings suggest that preferences for AI autonomy reflect how developers cognitively experience their work, highlighting important considerations for designing meaningful work.

---


### 106. [Flow-Map GRPO: Reinforcement Learning for Few-Step Flow-Map Generators via Anchored Stochastic Composition](https://arxiv.org/abs/2607.00535)

**<font color=#1a73e8>作者：</font>** Zhiqi Li, Wen Zhang, Bo Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Few-step flow-map generators, such as consistency models and MeanFlow, accelerate sampling by directly learning long-range transport maps between noise and data. However, these models are typically deterministic, which makes them difficult to optimize with reinforcement learning (RL) post-training methods that require stochastic trajectories and well-defined likelihood ratios. Existing SDE-based stochasticization techniques are designed for velocity-based samplers with infinitesimal or finely discretized transitions, and therefore do not directly apply to long-range flow maps. In this work, we propose Flow-Map GRPO, an online RL post-training framework for deterministic few-step flow-map generators. The key component is Anchored Stochastic Flow Map Composition (ASFMC), a path-preserving stochasticization mechanism that introduces randomness through anchor-based conditional resampling while preserving the original marginal probability path of the deterministic flow map. We derive GRPO objectives for both single-time and two-time flow-map parameterizations. Experiments on few-step FLUX-based text-to-image generators, including MeanFlow and sCM, show that Flow-Map GRPO improves pretrained deterministic flow-map models across reward-based, perceptual, and task-level evaluation metrics. Our results demonstrate that deterministic few-step flow-map generators can be effectively aligned with RL post-training without modifying their original model parameterization or retraining them as native stochastic models.

---


### 107. [AI-Centered Grand Challenges in Visual Analytics for Healthcare: Synthesizing the VAHC 2025 Community Experience](https://arxiv.org/abs/2607.00542)

**<font color=#1a73e8>作者：</font>** Jürgen Bernard, David Gotz, Robert S Laramee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The intersection of AI, healthcare, and visualization is evolving rapidly, posing challenges that cut across disciplinary boundaries and resist easy resolution. The Visual Analytics in Healthcare workshop (VAHC), co-located every other year at the IEEE VIS conference and the AMIA (American Medical Informatics Association) annual conference, has served as a forum to connect the visualization and medical informatics community since 2010. In 2025, to celebrate the 16th edition, we used the workshop as an opportunity to consolidate the community's collective experience (and expertise) and identify Grand Challenges where the field should prioritize going forward. We combined thematic coding of the 15 accepted VAHC workshop papers with structured group discussions among more than 40 participants, organized around three major themes: "Technical innovation vs. clinical reality", "Human-centered and scalable VAHC", and "From foundations to actionable insights", followed by post-workshop reflexive analysis. Across all three groups, AI emerged as the most consistently recurring concern. In this paper, we report our AI-centered insights from the VAHC 2025 group activity, contextualize them against the broader literature along five Grand Challenges themes, and distill them into five challenge clusters, each concluded with recommendations for future research directions that cross disciplinary boundaries: (1) trust and bias, (2) data and infrastructure, (3) explainability and communication, (4) human-AI interaction, and (5) model reliability and validation. We share these challenges and their associated research directions as a starting point for discussion and collaboration across the healthcare, AI, and visualization communities. All supplemental materials are available at this https URL.

---


### 108. [GEAR-Seg: A Grounded Explainable Agent for Reasoning Segmentation and Data Engine](https://arxiv.org/abs/2607.00544)

**<font color=#1a73e8>作者：</font>** Yanan Wang, Wen Li, Yibin Ying 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning segmentation requires localizing targets based on complex, implicit queries. Current end-to-end models typically entangle perception and deduction into an opaque black box, severely limiting interpretability and scalability. To address this, we propose GEAR-Seg (Grounded Explainable Agent for Reasoning Segmentation), an explicitly decoupled agent that shifts the paradigm by translating visual pixels into dense, attribute-rich text. By decoupling class-agnostic segmentation, semantic description, and Large Language Model (LLM) deduction, GEAR-Seg transforms implicit reasoning into an explicit, trackable logic chain. As a zero-shot inference framework, it achieves highly competitive performance across diverse reasoning and fine-grained referring segmentation benchmarks. Furthermore, GEAR-Seg inherently functions as a highly scalable data engine. Utilizing this engine, we construct GEAR-131K, a massive benchmark (over 38k images, 656k QA-mask pairs) introducing a multifaceted taxonomy tailored for complex real-world manipulation-oriented reasoning. Finally, distillation experiments demonstrate that lightweight models supervised exclusively by our automated pipeline closely match the upper-bound performance of costly human-annotated baselines.

---


### 109. [EgoGapBench: Benchmarking Egocentric Action Selection in Multi-Agent Scenes](https://arxiv.org/abs/2607.00547)

**<font color=#1a73e8>作者：</font>** Jihyeok Jung, Jeewu Lee, Sanghyeop Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing egocentric benchmarks have primarily constructed the egocentric setting from first-person-view data, which makes it difficult to evaluate egocentric perspective itself in isolation. However, understanding first-person-view input and taking an egocentric perspective are separable abilities, especially when first-person body cues are absent or when other agents are present. To isolate egocentric perspective understanding, we introduce EgoGapBench, a diagnostic benchmark for measuring action selection in multi-agent egocentric scenes. We define the ability measured by this benchmark as Egocentric Action Selection (EAS): selecting an appropriate action from the agent's perspective in the presence of other agents. On EgoGapBench, humans answer reliably, whereas both open-source and proprietary MLLMs perform substantially worse and systematically select actions performed by other visible agents. Fine-tuning on existing egocentric data fails to close this gap and can even be detrimental. In contrast, fine-tuning on EgoGapBench training data improves accuracy but does not reach human performance. These results show that EAS is difficult to acquire from first-person-view data alone, and that MLLMs should be evaluated and trained not only for scene understanding but also for egocentric action selection.

---


### 110. [Cross-Domain Generalization Failure in Lightweight Intrusion Detection Models for IIoT Networks](https://arxiv.org/abs/2607.00553)

**<font color=#1a73e8>作者：</font>** MD Azizul Hakim, Md Shihab Uddin, Talha Ibne Anis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Lightweight machine learning models are increasingly proposed for intrusion detection in Industrial Internet of Things (IIoT) networks due to their suitability for resource-constrained edge deployment. Most reported results evaluate these models only within their training network, leaving behavior on unseen networks unverified. This study trains four lightweight architectures on one IIoT dataset and evaluates them, without retraining, on two structurally distinct IIoT datasets using a feature representation restricted to attributes available across all three sources. Explainability analysis across two top-performing models shows both rely overwhelmingly on coarse port-category features; the most influential category occurs in source-domain attack traffic at 96 to 435 times the rate in the two target domains, indicating that coarsening port resolution relocates rather than removes a documented shortcut. Evaluation under naturally imbalanced class distributions reveals a further effect: the evaluation protocol used can reverse which target network appears to pose the greater generalization challenge. Adversarial robustness and recovery through limited target-domain exposure are also assessed; robustness to adversarial perturbation is unrelated to cross-network generalization, and recovery through adaptation varies considerably by architecture. These findings suggest deployment readiness should be assessed using cross-network evaluation under realistic class distributions, rather than within-domain accuracy alone.

---


### 111. [Group-Equivariant Poincaré Convolutional Networks](https://arxiv.org/abs/2607.00556)

**<font color=#1a73e8>作者：</font>** Aiden Durrant, Rahul Baburajan, Georgios Leontidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While recent advancements like the Poincaré ResNet have demonstrated the potential of learning visual representations directly in hyperbolic space, their optimisation remains hampered by the computationally intensive nature of Riemannian gradients and the strict boundaries of the manifold. Furthermore, standard hyperbolic networks treat spatial transformations of the same object as distinct hierarchical concepts, leading to redundant parameter usage and vanishing signals. We propose Equivariant Poincaré ResNets, combining hyperbolic geometry with discrete symmetry groups ($C_4$ and $D_4$). We identify critical roadblocks in applying Euclidean equivariance to hyperbolic space and propose geometrically safe tensor reshaping, left-regular permutations for hyperbolic group convolutions, and joint-orientation Poincaré Midpoint Batch normalisation. Empirically, embedding equivariance drastically reduces the optimisation space, accelerating convergence while accelerating convergence while respecting the boundary constraints of the Poincaré ball and preserving spatial-group equivariance.

---


### 112. [Safe Alone, Unsafe Together: Safeguarding Against Implicit Toxicity When Benign Images Combine](https://arxiv.org/abs/2607.00576)

**<font color=#1a73e8>作者：</font>** Jiaxian Lv, Shiyao Cui, Yingkang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-image content has become an increasingly prevalent form of visual communication in social media, giving rise to a new safety issue, multi-image implicit toxicity (MIIT), where each image appears benign in isolation, but harmful semantics emerge when the images are interpreted jointly. MIIT is particularly challenging for existing commercial moderation APIs and models due to the lack of explicit risky cues in each image. This paper aims to study how to identify MIIT. We first provide a formal definition of MIIT and analyze three key challenges for its detection. To alleviate the scarcity of data in this area, we construct MIIT-dataset, an image-only multi-image safety dataset covering seven representative risk categories through an automatic generation pipeline. Finally, we train MiShield with progressively distilled reasoning supervision, enabling it to produce safety judgments accompanied by explicit analyses of the correlated entities that result in the hazards. Experiments show that MiShield-8B models outperform representative moderation services and even larger-scale models, revealing its effectiveness and practical value for this widely used visual format. Warning: This paper contains potentially sensitive content.

---


### 113. [Caption Bottleneck Models](https://arxiv.org/abs/2607.00578)

**<font color=#1a73e8>作者：</font>** Seref Baris Cagliyan, Umut Ozdemir, Merve Tapli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs) provide interpretability by routing predictions through a layer of human-understandable concepts. However, defining an optimal concept set for a specific dataset remains an open challenge. Existing approaches rely on expensive expert annotations or LLM-generated lists based solely on class names. Even "open-vocabulary" variants typically depend on static concept sets, which restrict discovery and introduce label bias. Furthermore, traditional CBMs often suffer from information leakage, where unmodeled visual features bypass the bottleneck and compromise the integrity of the explanations. To overcome these limitations, we propose Caption Bottleneck Models (CaBM), a framework that circumvents the need for predefined concept sets by replacing rigid concept layers with free-form natural language. By representing images via LMM-generated captions and training a classifier strictly on this text, CaBM ensures a leakage-free architecture by construction. Additionally, by analyzing the text classifier post-training, CaBM autonomously discovers high-quality, dataset-specific concepts. Our results across fine- and coarse-grained benchmarks demonstrate that CaBM achieves competitive accuracy while preserving interpretability without the constraints of external dictionaries or manual labeling.

---


### 114. [Active Spatial Guidance: Eliminating Injected Positional Mechanisms in Vision Transformers](https://arxiv.org/abs/2607.00580)

**<font color=#1a73e8>作者：</font>** Cong Liu, Xiaofang Li, Simon X. Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) commonly rely on injected positional mechanisms to address self-attention's permutation invariance. Motivated by the spatial regularities of natural images, we ask whether spatial organization can be induced from data rather than explicitly injected. Under controlled, matched from-scratch training, we propose Active Spatial Guidance (Guidance), a training-only objective that disables positional injection and applies an auxiliary 2D coordinate-regression loss to the final-layer patch tokens. The guidance head is used only during training and removed for inference; the deployed model consists of a positional-injection-free ViT encoder and the task-specific prediction module. Using DINOv3 ViT backbones, Guidance consistently improves performance on ImageNet-100 classification, ADE20K semantic segmentation, and Hypersim monocular depth estimation, outperforming strong injected baselines such as learned absolute positional embeddings and rotary positional embeddings under identical training protocols. On ImageNet-100, broader comparisons against representative injected positional designs further support Guidance's effectiveness. Guidance also improves robustness under resolution transfer, and multi-resolution training further strengthens accuracy across input sizes. Overall, our results suggest that spatial inductive bias in ViTs need not be architecturally injected, but can be shaped through training-time supervision. The code used for training and evaluation is publicly available in this https URL.

---


### 115. [Decision-focused Sparse Tangent Portfolio Optimization](https://arxiv.org/abs/2607.00581)

**<font color=#1a73e8>作者：</font>** Haeun Jeon, Seunghoon Choi, Hyunglip Bae 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse tangent portfolio optimization aims to learn an interpretable, low-cardinality portfolio in the tangency direction of the mean-variance frontier. However, the associated cardinality-constrained formulation is NP-hard, and standard predict-then-optimize pipelines often misalign forecasting accuracy with downstream portfolio quality. We propose an end-to-end decision-focused learning framework that reformulates Sharpe ratio maximization as a Disciplined Parametrized Programming (DPP)-compliant convex programming layer and replaces discrete selection with a smooth top-$k$ operator enforcing an exact cardinality $k$. This enables gradient flow through prediction, asset selection, and re-optimization, allowing the predictive model to directly optimize portfolio performance. Across four major equity markets, our method achieves competitive and often superior out-of-sample Sharpe ratios compared with historical and prediction-focused baselines, with particularly strong gains in larger asset universes. Our \href{this https URL}{code} is publicly available.

---


### 116. [Low Perplexity is Repetition: A One-Dimensional Self-Conditioning Attractor in Continuous Diffusion LMs](https://arxiv.org/abs/2607.00588)

**<font color=#1a73e8>作者：</font>** Shuai Zhang, Zijie Chen, Hongliang He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion language models such as ELF report record-low generative perplexity (Gen-PPL). We find a catch: these models repeat far more than human text, and Gen-PPL rewards rather than penalizes that repetition, so its low scores overstate quality. Strip the repetition and ELF-B's Gen-PPL rises from $19.5$ to $27.7$; the smallest model even posts the best Gen-PPL because it repeats most. We trace the repetition to its source: a contractive attractor along a \emph{single direction} in the self-conditioning feedback loop, the loop that feeds each step's clean estimate into the next. Because the failure is one-dimensional, a one-dimensional fix suffices, and we propose one. \textbf{ACE} (Attractor-Contrast-Escape) subtracts that single, label-free direction from the feedback at each step. Estimated once on the $105$M model, the direction cuts repetition to near the human level while keeping quality competitive, and transfers near-unchanged to the $342$M and $652$M models and across samplers; the same recipe recovers useful directions on other architectures. Since Gen-PPL itself rewards repetition, we instead measure the compute each fix needs to produce human-clean text, where ACE is $1.5$--$5\times$ cheaper.

---


### 117. [GADA: Geometry-Aware Deformable Aggregation for Image-Based Gaussian Splatting](https://arxiv.org/abs/2607.00595)

**<font color=#1a73e8>作者：</font>** Siwoo Lim, Sunjae Yoon, Gwanhyeong Koo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian Splatting has achieved significant improvements by incorporating warping-based techniques. However, such methods suffer from pixel-level inaccuracies due to uncertain geometry. This uncertainty leads to spatial misalignments in the warped images, which disrupt residual learning used in warping-based methods and fundamentally limit the gains of correction, particularly on thin structures and high-frequency details. Driven by our insight that useful visual cues are not lost but locally preserved under slight displacement, we propose Geometry-Aware Deformable Aggregation (GADA). This method introduces an iterative refinement module with deformable offsets to actively correct spatial misalignments and recover these displaced cues. Furthermore, to address the limitations of standard pipelines where visibility checks (i.e., thresholding) often discard valid pixels and multi-view warped image fusion relies on naive mean aggregation, our module is coupled with an implicit confidence weighting mechanism that selectively suppresses unreliable evidence. Consequently, our approach outperforms prior warping-based Gaussian Splatting, preserving high-frequency quality while achieving 2.13 times faster FPS.

---


### 118. [Diffusion-Based Multi-Class Normality for OOD Detection: An Application to CDP Authentication](https://arxiv.org/abs/2607.00609)

**<font color=#1a73e8>作者：</font>** Bolutife Atoki, Iuliia Tkachenko, Bertrand Kerautret 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstruction-based generative models offer a natural framework for unsupervised out-of-distribution (OOD) detection, but multi-class normality modelling requires a single detector to capture multiple in-distribution manifolds and produce comparable anomaly scores across classes. We study this problem in copy detection pattern (CDP) authentication, where authentic and counterfeit samples are visually similar but differ in subtle printing-and-digitisation (P\&D) signatures. We propose a diffusion based multi-class normality framework in which a single class-conditional ControlNet is trained exclusively on authentic CDPs from multiple P\&D classes and detects counterfeits through reconstruction error under authentic-class conditioning. We further introduce dual template masking, which hides complementary regions of the input template and scores only withheld pixels, reducing reliance on visible binary structure. On the Indigo 1 x 1 Base dataset, the proposed method outperforms traditional and adapted generative baselines under multi-class authentic-versus-counterfeit evaluation, without using counterfeit samples for training or threshold calibration.

---


### 119. [Identifying Latent Concepts and Structures for Generalized Category Discovery](https://arxiv.org/abs/2607.00620)

**<font color=#1a73e8>作者：</font>** Boyang Dai, Chaoqi Chen, Yizhou Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized Category Discovery (GCD) aims to recognize known classes while autonomously discovering novel ones in open-world settings. However, current approaches primarily focus on designing clustering objectives, often overlooking a critical bottleneck: standard vision backbones yield high-rank, entangled token representations that are ill-suited for unsupervised discovery of latent concepts and structures. In this paper, we propose Compositional Primitive Fields (CPF-GCD), a novel representation learning framework that reshapes the feature space to make such latent structure identifiable by enforcing a low-rank compositional organization. Our core hypothesis is that all categories, whether known or novel, can be expressed as compositions and spatial arrangements of a finite set of learnable visual primitives that capture reusable concepts. CPF instantiates this geometric constraint via a spatial field mechanism. Inserted between the backbone and the head, it rewrites noisy patch tokens through low-rank primitive mixtures, effectively decomposing images into reusable atomic parts and their spatial layouts. By explicitly modeling the spatial distribution of primitives, CPF enables novel categories to emerge naturally as new activation patterns over a shared vocabulary. This shifts the focus of representation from merely partitioning global embeddings to constructing a structured and separable primitive field. Extensive experiments demonstrate that CPF serves as a generic, plug-and-play module that consistently boosts performance across diverse GCD baselines, validating that identifying and leveraging low-rank compositional structure is a crucial inductive bias for open-world recognition.

---


### 120. [Learning to Watch: Active Video Anomaly Understanding via Interleaved Policy Optimization](https://arxiv.org/abs/2607.00622)

**<font color=#1a73e8>作者：</font>** Mengjingcheng Mo, Jiaxu Leng, Xinbo Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly understanding (VAU) relies on sparse, context-dependent cues. However, existing passive paradigms suffer from observational aliasing, where static sampling fails to disambiguate semantically distinct events. To overcome this, we propose $Anom\text{-}\pi$, a closed-loop framework that reconceptualizes video understanding as an active sequential decision-making process within a dynamic environment. Inspired by human video-reviewing behavior, this framework unifies internal cognitive reasoning and strategic evidence acquisition into an interleaved policy, utilizing temporal atomic operators such as local backtracking, temporal expansion, and fine-grained sampling to endow the model with perceptual proactivity. To learn such complex interaction strategies under video-level weak supervision, we design Interactive Direct Preference Optimization (iDPO) to achieve trajectory-level policy alignment, guided by an Active Evidence Inquiry (AEI) utility that balances task success, informative evidence acquisition, and interaction cost. This approach enables the agent to learn to actively disambiguate hypotheses while suppressing redundant exploration. Extensive experiments demonstrate that our framework, with only 2B parameters, achieves highly competitive performance, significantly outperforming state-of-the-art large-scale VAU models in complex scenarios.

---


### 121. [Loss Smoothing for Stable Adaptation Under Distribution Shift](https://arxiv.org/abs/2607.00634)

**<font color=#1a73e8>作者：</font>** Darshan Patil, Ekaterina Lobacheva, Razvan Pascanu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In settings such as fine-tuning and reinforcement learning, neural networks are often adapted under distribution shift. Standard adaptation methods typically optimize the target objective directly, inducing an abrupt change from the source training objective. This abrupt transition can distort learned representations, including features that may still be useful for the new task. We investigate whether a more gradual transition can improve adaptation. We propose loss smoothing, a simple approach that interpolates between the source and target training objectives at the start of adaptation. This smooth transition helps to preserve useful features from the source distribution while still enabling the model to specialize to the target distribution. Across controlled supervised shifts, pretrained vision adaptation, offline-to-online and online reinforcement learning, and language model fine-tuning, we find that loss smoothing consistently improves performance, suggesting that smoother objective transitions are a broadly useful tool for model adaptation.

---


### 122. [Uncertainty-aware tree height change regression](https://arxiv.org/abs/2607.00638)

**<font color=#1a73e8>作者：</font>** Max Gaber, Dimitri Gominski, Jaime C. Revenga 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monitoring canopy height change is essential for understanding carbon sinks and forest dynamics. Remote sensing enables consistent, large-scale observations of such changes, increasingly integrated with deep learning architectures such as Geospatial Foundation Models (GFMs). However, existing methods and datasets frame the problem as binary change detection, which overlooks both the continuous nature of change, especially for vegetation, and the inherent uncertainty in labels. We present the Canopy Height Change (CHC) dataset, providing 3 $\mathrm{m}$ resolution continuous canopy height differences and associated spatially resolved uncertainties across 10598 $\mathrm{km}^2$ of northern and western Spain. The dataset is paired with a co-located time series of PlanetScope satellite imagery. Based on the dataset, we introduce the task of uncertainty-aware change regression, associated metrics and strategies for fine-tuning GFMs. Furthermore, we evaluate state-of-the-art GFMs and highlight promising directions and remaining challenges for advancing continuous canopy height change estimation.

---


### 123. [Coachable agents for interactive gameplay](https://arxiv.org/abs/2607.00642)

**<font color=#1a73e8>作者：</font>** Roberto Capobianco, Harm van Seijen, Nolan D. Bard 等 41 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has proven to be a valuable tool in the creation of advanced AI and robotic systems, contributing to everything from game playing to robotics to foundation models. Through trial-and-error, these AI systems typically learn one, near-optimal behavior to solve their tasks. However, there are many use cases in which one would like to assert some level of control, preferably in real time, over how the task is solved. We refer to these modifications of a core task as styles. We combine universal value function approximators (UVFAs) with carefully selected training scenarios, learning algorithms, and data augmentation to create a framework for coaching agents that exhibit styles in complex domains. We demonstrate the framework's application in the AAA video games Horizon Forbidden West and Gran Turismo, and in an open-source humanoid test domain. Despite the different nature of the domains -- car racing, stylized game combat, and humanoid walking -- each agent shows strong coherence to the style requests while still satisfying the main task in its domain. Importantly, the techniques outlined in this paper allow an end user to choose the final behavior at run time, giving them flexible control over the final executed performance.

---


### 124. [Not All Prediction Targets Keep Training-Free Diffusion Guidance on the Manifold](https://arxiv.org/abs/2607.00647)

**<font color=#1a73e8>作者：</font>** Yunsung Lee, Hyeongmin Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free guidance (TFG) steers a pretrained diffusion model toward a desired attribute at inference. To be effective, this guidance must be applied from the earliest, high-noise steps of sampling. Because its objective (a classifier or energy) is defined on clean images, $\epsilon$- and $v$-prediction models must first estimate the clean image $\hat{x}$ from the noisy state at each step, and the accuracy of that estimate determines how easily guidance drifts off the data manifold. $x$-prediction, a recent alternative, outputs the clean image directly, removing this source of error even at high noise. This is our motivation. We provide a theoretical analysis of how each prediction target shapes this accuracy, and introduce guided-class FID (Child FID), a metric that exposes the manifold damage standard evaluation misses. Experiments on a new fine-grained bird benchmark and on style transfer confirm that $x$-prediction keeps guided samples on the manifold most reliably, making it the strongest foundation for training-free guidance. Code is available at this https URL

---


### 125. [Faithful by Definition: Emotion Analysis via Natural Semantic Metalanguage Explications](https://arxiv.org/abs/2607.00661)

**<font color=#1a73e8>作者：</font>** Frank Xing, Erik Cambria  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Explanations for emotion classifiers are usually produced post hoc, with no guarantee that they reflect the computation behind the label. We present an explication interface for event-based emotion analysis. A parser maps the input text to an explication, a short script in the closed vocabulary of Natural Semantic Metalanguage organized into twelve typed slots, and a fixed decision list of rules transcribed from published semantic definitions computes the label from the explication alone. The faithfulness guarantee is therefore causal and definitional, while all empirical risk lives in the learned parser, which the per-line entailment interface makes auditable against the input. On crowd-sourced event descriptions, our fine-tuned parser reaches 0.33 accuracy and 0.48 selective accuracy on a small held-out set, suggesting that the interface trades insignificant accuracy difference to a black-box model for a verifiable, inspectable decision basis for first-person event-based emotion analysis. We also release EmoExpl-1200 with per-line verification metadata and the full rule set.

---


### 126. [Multi-Label Node Classification with Label Influence Propagation](https://arxiv.org/abs/2607.00671)

**<font color=#1a73e8>作者：</font>** Yifei Sun, Zemin Liu, Bryan Hooi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graphs are a complex and versatile data structure used across various domains, with possibly multi-label nodes playing a particularly crucial role. Examples include proteins in PPI networks with multiple functions and users in social or e-commerce networks exhibiting diverse interests. Tackling multi-label node classification (MLNC) on graphs has led to the development of various approaches. Some methods leverage graph neural networks (GNNs) to exploit label co-occurrence correlations, while others incorporate label embeddings to capture label proximity. However, these approaches fail to account for the intricate influences between labels in non-Euclidean graph data. To address this issue, we decompose the message passing process in GNNs into two operations: propagation and transformation. We then conduct a comprehensive analysis and quantification of the influence correlations between labels in each operation. Building on these insights, we propose a novel model, Label Influence Propagation (LIP). Specifically, we construct a label influence graph based on the integrated label correlations. Then, we propagate high-order influences through this graph, dynamically adjusting the learning process by amplifying labels with positive contributions and mitigating those with negative influence. Finally, our framework is evaluated on comprehensive benchmark datasets, consistently outperforming SOTA methods across various settings, demonstrating its effectiveness on MLNC tasks.

---


### 127. [DART: Difficulty-Adaptive Routing for Zero-Shot Video Temporal Grounding](https://arxiv.org/abs/2607.00672)

**<font color=#1a73e8>作者：</font>** Zhengbo Zhang, Mark He Huang, Zhigang Tu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot video temporal grounding (VTG) localizes events in untrimmed videos from natural language queries without task-specific training. Existing methods rely on frame-query feature matching, which suffices for simple events but struggles with complex multi-stage queries that require understanding temporal ordering and causal structure -- a disparity we call the reasoning gap. We propose DART (Difficulty-Adaptive Routing for Temporal Grounding), which bridges this gap by coupling difficulty-aware routing with structured reasoning in large vision-language models. A query-conditioned Determinantal Point Process (DPP) serves a dual role: selecting diverse, query-relevant keyframes as temporal evidence, and providing spectral entropy as a difficulty indicator. Simple queries are routed to a Fast path for direct prediction, while complex queries follow a Slow path with Temporal Markup Prompting, which decomposes localization into global event analysis, per-frame temporal role annotation, and boundary extraction. On Charades-STA and ActivityNet Captions, DART achieves state-of-the-art zero-shot performance across both identically distributed and multiple out-of-distribution settings, improving mIoU by up to 3.5 points over the strongest baseline while using over 7 times fewer frames. The project homepage is available at this https URL.

---


### 128. [ABot-M0.5: Unified Mobility-and-Manipulation World Action Model](https://arxiv.org/abs/2607.00678)

**<font color=#1a73e8>作者：</font>** Ronghan Chen, Yandan Yang, Zuojin Tang 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation: they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under supervision that does not match autoregressive inference. As a result, they often miss fine-grained contact dynamics, suffer from action-distribution conflicts, and accumulate errors over long-horizon rollouts. We propose ABot-M0.5, a new WAM built on the insight that mobile manipulation requires alignment at three levels: temporal granularity, action space, and train-test consistency. To align temporal granularity, we introduce intermediate latent actions that capture local visual state transitions and serve as an bridging action space between video latents and embodiment-specific controls. To align action space, we design a dual-level Mixture-of-Transformers architecture that disentangles both modality representations and heterogeneous action subspaces such as base movement and arm manipulation. To align inference conditions, we propose the dream-forcing training strategy that progressively trains inverse dynamics on model-predicted videos, improving train-test alignment and robustness during autoregressive prediction. Experiments on challenging mobile and fine-grained manipulation benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and finegrained control accuracy. These results highlight the critical importance of granularity-aligned, action-disentangled, and inference-consistent world-action modeling.

---


### 129. [Distributed Online Bandit Submodular Maximization with Bounded Sampling Violations](https://arxiv.org/abs/2607.00680)

**<font color=#1a73e8>作者：</font>** Bin Du, Chang Liu, Dingqi Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study distributed online submodular maximization under partition matroid constraints, in which multiple agents select a limited number of actions from their own subsets sequentially to maximize the cumulative value of a sequence of objective functions. We develop a unified algorithmic framework that accommodates full-information and bandit feedback models. For both feedback models, we prove that the proposed algorithms achieve sublinear $(1-1/e)$-regret guarantees, which are comparable to those achieved by existing centralized counterparts. Furthermore, to tackle the sampling violation issue caused by continuous relaxation and rounding, we develop a bounded stochastic pipage rounding scheme and show that the probability of sampling violation vanishes asymptotically. As a result, the cumulative sampling violation remains sublinear in $T$, which is further shown to be not improvable under certain conditions. Numerical results validate the theoretical findings in this paper.

---


### 130. [LUMA: Benchmarking Segmentation via a Lightweight Universal Mask Adapter](https://arxiv.org/abs/2607.00687)

**<font color=#1a73e8>作者：</font>** Tobias Christian Nauen, Anosh Billimoria, Federico Raue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Comparing transformer backbones for image segmentation is confounded: each is paired with a different decoder, recipe, and pretraining, so reported differences rarely reflect the backbone itself. We introduce the Lightweight Universal Mask Adapter (LUMA), a lightweight, backbone-agnostic mask-transformer head that treats any backbone as a black-box feature extractor, letting a set of queries read from its features through cheap cross-attention. LUMA matches the accuracy of EoMT, the state-of-the-art efficient ViT-segmenter, at lower cost, while attaching unchanged to isotropic, hierarchical, convolutional, and mixture-of-experts backbones alike. Holding this head fixed, we benchmark 20 backbones, 11 pretraining schemes and a range of resolutions on ADE20K and Cityscapes under one modern recipe. We find that ``efficient'' token mixers fail to deliver efficiency even at the high resolutions that motivate them, with plain ViT holding the throughput Pareto-front at every resolution. Additionally, the pretraining objective, not the architecture, the lever the field has tuned hardest, governs segmentation quality.

---


### 131. [Generative Refinement for Low-Budget Black-Box Optimization](https://arxiv.org/abs/2607.00691)

**<font color=#1a73e8>作者：</font>** Edouard R. Dufour, Pascal Fua  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Black-box optimization is a fundamental science and engineering tool that makes it possible to optimize objectives without gradient information. Unfortunately, as it often requires many function evaluations, it can be challenging when each one is costly. This is especially true when the evaluation function is noisy or failure-prone, and when high-performing solutions are confined to thin, curved, or disconnected regions of the search space. Existing methods leveraging generative models to navigate these subspaces are built to sample from reward-aligned distributions. As a result, they require a large number of evaluations to align their sampler effectively, making them impractical in low-budget settings. We propose SPARROW, an algorithm that completely decouples the generative prior from the reward signal. SPARROW can use any sampler with a known corruption process and trained on unevaluated data, as a fixed, structured proposal operator. Optimization proceeds by rank-based guidance over an archive of evaluated candidates. SPARROW can navigate complex geometries, handle unreliable reward signals, and perform effective optimization under very low evaluation budgets. We provide asymptotic convergence guarantees over the sampler support and demonstrate strong empirical performance on problems with unreliable rewards and geometrically complex landscapes.

---


### 132. [The Rise and Fall of Google's Privacy Sandbox](https://arxiv.org/abs/2607.00693)

**<font color=#1a73e8>作者：</font>** Rachid Youssef Grib, Alberto Verna, Nikhil Jha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> On October 17th, 2025, Google announced the retirement of most Privacy Sandbox APIs, concluding nearly five years of experimentation with its alternative to privacy-invasive data collection on the Web. Designed to balance privacy with advertising functionality and cross-site tracking, the initiative faced repeated redesigns and limited ecosystem support.
In this work, we present the first longitudinal, consent-aware measurement of the Privacy Sandbox's deployment across the Web. Using a custom call listener and weekly crawls of the top-10,000 websites, we monitor the usage of all major APIs in the months preceding their retirement. Adoption had already stagnated well before Google's announcement: most APIs were used by only a handful of actors, whose activity declined steadily throughout our study. Even the APIs that Google plans to maintain show no sign of growth. The sole exception is Cookies Having Independent Partitioned State (CHIPS). Overall, the demise of the Privacy Sandbox leaves unresolved the challenge of enabling privacy-preserving interest-based advertising.

---


### 133. [Know Thy Neighbor: Cross-TEE Mutual Attestation](https://arxiv.org/abs/2607.00695)

**<font color=#1a73e8>作者：</font>** Daniel Andrade, João N. Silva, Miguel P. Correia  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud services are composed of multiple heterogeneous distributed components and instances that communicate with one another. This occurs both in applications and services running in traditional execution environments and in trusted applications (TAs) running in trusted execution environments (TEEs). TA instances use attestation before exchanging information to ensure all parties meet the expected security conditions. The straightforward solution to mutually attesting two TA instances that are willing to communicate is employing remote attestation mechanisms in both directions. This is typically the case when the two TA instances are running on TEEs of the same type. In order to support cross-TEE attestation, such an approach, that is, using remote attestation in both directions, would require each TEE type (e.g., SGX, TrustZone) to support the attestation software stack of all other TEE types with which it needs to interact. A dedicated cross-TEE mutual attestation solution has multiple benefits in terms of efficiency and security. This paper presents the Heterogeneous Mutual Attestation (Hema) protocol, a formally-verified protocol for the mutual attestation of TA instances running on the same TEE type or on different TEE types.

---


### 134. [Imprint: Online Memory Compression for Long-Horizon Egocentric QA](https://arxiv.org/abs/2607.00696)

**<font color=#1a73e8>作者：</font>** Kousik Das, Debaditya Roy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon egocentric question answering involves answering about events that have occurred hours or days in the past. This requires memory representations that remain both retrieval-effective and scalable over days or weeks of recording. Existing long-horizon egocentric QA methods construct memory as hierarchical textual summaries of observations. While effective for reducing memory size, summarization optimizes for descriptive compression rather than retrieval: repeated interactions are absorbed into coarse textual descriptions instead of being preserved as explicit, recurring memory units, making long-horizon evidence aggregation difficult. We propose Imprint, an interaction-centric memory framework that formulates long-horizon egocentric memory as an online memory compression problem rather than summarization. Incoming observations are first represented as structured Interaction Records and continuously organized into recurring interaction patterns. Using human memory consolidation signals of recurrence, recency, and distinctiveness, Imprint selectively retains and compresses interactions into a compact retrieval-oriented memory. We evaluate Imprint on EgoLifeQA, a seven-day egocentric benchmark containing questions that require reasoning over interactions occurring hours to days before the query. With the same LLM, Imprint improves QA accuracy from 31.0% to 35.8%, increases evidence-grounded answers by $6\times$ compared with EgoRAG, reduces memory footprint by $2.3\times$, and decreases retrieval latency by $11.8\times$. These results demonstrate that memory compression provides a scalable and retrieval-effective foundation for long-horizon egocentric question answering.

---


### 135. [Creating Impactful Autonomous Driving Datasets: A Strategic Guide from Research Gap to Benchmark](https://arxiv.org/abs/2607.00710)

**<font color=#1a73e8>作者：</font>** Richard Schwarzkopf, Jonas Merkert, Frank Bieder 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Well-designed autonomous driving datasets have fundamentally shaped research progress, yet existing literature primarily describes what datasets contain rather than how to strategically design impactful ones. This is especially limiting for small and medium-sized labs and startups that cannot afford to misallocate scarce resources. We argue that impactful dataset creation begins with a diagnosis: whether a research question is blocked by a data problem or an evaluation problem, and proceeds by selecting the minimal data operator(s) that closes the resulting gap, recording new data only when no cheaper operator(s) suffices. We analyze the evolution of major autonomous driving (AD) datasets through this lens and distill a strategic framework spanning gap identification, operator choice, sensor suite design, and annotation strategy. We ground the framework in a running case study of our KITScenes dataset family. The datasets are available at: this https URL

---


### 136. [Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption](https://arxiv.org/abs/2607.00712)

**<font color=#1a73e8>作者：</font>** Xiaomeng Fu, Jia Li, Yiming Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) streaming models have emerged as a powerful paradigm for long video generation. However, the linearly growing Key-Value (KV) cache poses a significant bottleneck, leading to memory overload and degraded inference throughput. A common compression method is to drop redundant KV tokens, which often breaks long-range dependencies, resulting in temporal flickering and identity loss. In this paper, we propose Instance-Specific Parametric Absorption (ISPA), a novel framework that shifts the KV cache compression from discarding to distilling. The core idea is to transit a subset of layers from Full-Attention (F-Layers) to memory-efficient Local-Attention (L-Layers) by "absorbing" historical context into the model's weights. Specifically, during a brief warmup phase, ISPA monitors the output discrepancy between global and local attention. At the transition point, we solve a closed-form least-squares problem to compute an instance-specific weight modulation that compensates for the missing history. Experiments across architectures (1.3B to 14B) demonstrate that ISPA can remove up to 50\% of the KV cache with near-lossless visual quality. We hope this perspective encourages future work to explore parametric memory consolidation beyond external token-level cache management for streaming generative models.

---


### 137. [Partial Skeleton Visibility for Action Recognition: A Constrained Field-of-View Approach](https://arxiv.org/abs/2607.00716)

**<font color=#1a73e8>作者：</font>** Yingjie Dai, Tianyang Xu, Yanglin Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton-based action recognition has achieved remarkable success by exploiting joint coordinates and their topological connections, yet prevailing methods overwhelmingly assume complete and clean skeleton inputs. In real-world deployments, such as egocentric vision, crowded surveillance, wearable devices, or edge robotics, limited field-of-view (FoV) frequently causes substantial joint visibility dropout, leading to severe performance degradation that existing models are largely unprepared to handle. To bridge this critical yet underexplored gap, we introduce PartialVisGraph, a novel hypergraph framework tailored for robust skeleton action recognition under constrained FoV. We first construct highly expressive hypergraphs by introducing learnable virtual hyperedges that form a soft incidence matrix, capturing flexible high-order dependencies beyond conventional pairwise graphs. We then propose the Single-Head Sample-Adaptive Transformer, which adaptively aggregates joint features onto hyperedges while explicitly incorporating a visibility prior. This prior selectively gates information flow, preventing occluded or out-of-view joints from corrupting reliable feature propagation. We further establish rigorous evaluation protocols with realistic FoV simulation benchmarks on NTU RGB+D 60 and 120. Extensive experiments demonstrate that PartialVisGraph consistently achieves state-of-the-art accuracy under partial visibility, with gains of up to 68.8\% on subsets with severe FoV restrictions compared to recent strong baselines, while remaining superior on full-visibility settings. Our approach offers a principled and practical pathway toward deployable skeleton-based action understanding in unconstrained environments.

---


### 138. [Detecting the Undetectable: Enhancing Unsupervised time series Anomaly Detection via Active Learning](https://arxiv.org/abs/2607.00720)

**<font color=#1a73e8>作者：</font>** Seung Hun Han, Hyeongwon Kang, Jinwoo Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the increasing sophistication of industrial AI systems, the ability to reliably detect subtle and noisy anomalies in complex time series data remains a critical yet unresolved challenge. In large-scale industrial applications, labeling time series data is often prohibitively expensive and time-consuming, making unsupervised learning a practical and widely adopted approach. However, existing unsupervised methods frequently struggle to distinguish near-normal anomalies from normal patterns and are vulnerable to noise contamination within normal samples. To address these limitations, we propose a novel framework that leverages active learning to iteratively enhance the performance of unsupervised models. Our framework's core contributions are (1) a masked time-series reconstruction feedback strategy that forces the model to learn robust temporal dependencies, and (2) a minimax learning strategy that promotes robustness by differentially treating normal and abnormal samples. This process encourages the model to better capture the dynamics of subtle and noisy patterns. The proposed framework is evaluated across 28 test cases involving four multivariate time-series datasets and seven unsupervised backbone models. Experimental results demonstrate a 12.39% improvement in AUC compared to the original models, confirming that our method can be readily integrated into existing unsupervised reconstruction-based anomaly detection systems to significantly enhance their performance.

---


### 139. [MSQA: A Natively Sourced Multilingual and Multicultural SimpleQA Benchmark](https://arxiv.org/abs/2607.00724)

**<font color=#1a73e8>作者：</font>** Xianru Chen, Yukai Huang, Mingxiang Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual fluency often invites a stronger assumption: a model that can speak a user's language must also understand the culture encoded by that language. We call this the Illusion of Cultural Alignment. To test this assumption directly, we introduce MSQA, a benchmark of 1,064 natively sourced questions across 11 language groups, five cultural dimensions, and three difficulty tiers. Unlike translated benchmarks, MSQA targets locally grounded knowledge and reduces shortcuts from English-centric cross-lingual transfer. Evaluating 18 LLMs, we find substantial cultural degradation and a pronounced Locality Effect: cultural competence tracks pre-training exposure more closely than general reasoning ability. We further show that common inference-time remedies do not dissolve the illusion. Models remain overconfident on unfamiliar cultural questions, repeated sampling yields unstable rather than reliable correctness, and retrieval augmentation helps unevenly on long-tail facts. These findings indicate that cultural alignment cannot be inferred from multilingual ability alone and requires deeper intervention than calibration, sampling, or retrieval at inference time

---


### 140. [AV-SyncBench: Decoupled Benchmarking of Temporal and Semantic Audio-Visual Synchronization](https://arxiv.org/abs/2607.00726)

**<font color=#1a73e8>作者：</font>** Tianhong Zhou, Mingyang Han, Boyu Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual feature extraction is a fundamental component of multimodal understanding and generation tasks. However, existing evaluation protocols for feature extraction models exhibit dimensional bias, typically focusing on either semantic matching or temporal offset detection. Moreover, their data construction remains coupled, preventing independent assessment of temporal and semantic consistency. We propose AV-SyncBench, the first benchmark to fully separate temporal and semantic evaluation for audio-visual synchronization. Built from in-the-wild videos, it spans Voice, Music, and Sound across 10 scenarios and 5 challenge tasks. Data are automatically filtered and manually verified to ensure on-screen sound sources. The benchmark contains 3,269 videos and 38,390 samples, and we evaluate five representative models to quantify feature quality for alignment and downstream tasks. The code and dataset are available at: this https URL.

---


### 141. [ConRTF: Edge-Constrained Boundary Distribution Refinement for Realtime TransFormer Table Structure Recognition](https://arxiv.org/abs/2607.00734)

**<font color=#1a73e8>作者：</font>** Eliott Thomas, Tri-Cong Pham, Mickael Coustaty 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Table Structure Recognition (TSR) aims to recover the row and column layout of tables from document images, a key step in document understanding pipelines. Accurate TSR depends on precise boundary localization: small errors in row or column boundaries can propagate into incorrect cell assignments and structural inconsistencies. Yet detection-based approaches treat table elements as generic objects, ignoring a fundamental property of table layout: rows and columns play structurally distinct roles and their boundaries carry unequal importance. We propose an Edge-constrained Fine-grained Localization loss (EFL) that formalizes this structural asymmetry by encoding table-specific geometric priors into the training objective: row-like elements are supervised with emphasis on their horizontal boundaries, while column-like elements prioritize vertical boundaries. Implemented within a real-time detector with distribution-based boundary refinement (D-FINE), EFL operates during training only and guides boundary refinement toward structurally meaningful adjustments with no change to the inference pipeline. The proposed approach, ConRTF, is also data-efficient, maintaining robust accuracy with as few as 2k--3k annotated tables. Experiments on PubTables-1M and two private datasets show consistent improvements over the optimized baseline and several real-time detectors including RT-DETRv2 and YOLOv10-11, with gains of up to +1.6 GriTS points at equal inference speed.

---


### 142. [Towards Robust Driving Perception: A Flexible Scale-Driven Family for Self-Supervised Monocular Depth Estimation](https://arxiv.org/abs/2607.00736)

**<font color=#1a73e8>作者：</font>** Zhaowen Zhu, Li Zhang, Yujie Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-Supervised Monocular Depth Estimation (MDE) has garnered attention in recent years due to its independence from ground truth. However, most existing models are limited to a single scale and exhibit considerable performance degradation in complex driving environments. Networks specifically designed to handle dynamic traffic participants tend to be overly complex, hindering their deployment on resource-constrained automotive edge devices. To address these limitations and move towards robust driving perception, we propose FlexDepth, a scale-driven and flexible family of self-supervised MDE models tailored for challenging road scenarios. FlexDepth employs a two-stage static-dynamic decoupled training strategy, enabling the independent assessment of confidence for both static backgrounds and dynamic road objects. Furthermore, it introduces a meticulously designed Scale-Driven Decoder (SDD) to dynamically select components based on scale size, facilitating efficient feature fusion and the output of high-precision depth maps. Extensive experiments on standard driving benchmarks demonstrate that without any auxiliary information, our model achieves state-of-the-art performance across arbitrary scales with minimal computational overhead. Our smallest model, Flex-Nano, requires only 0.7 GFLOPs and achieves 37.6 FPS on mobile platforms, ensuring reliable real-time perception while maintaining excellent zero-shot this http URL source code is avalible: this https URL

---


### 143. [Prototype Memory-Guided Training-Free Anomaly Classification and Localization in Prenatal Ultrasound](https://arxiv.org/abs/2607.00744)

**<font color=#1a73e8>作者：</font>** Huanwen Liang, Yuhao Huang, Xiliang Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prenatal anomaly classification and localization is of critical importance for fetal health and pregnancy management. Although ultrasound (US) is the primary modality for prenatal screening, accurate diagnosis remains challenging due to the low prevalence and high heterogeneity of anomalies. Existing deep learning methods for prenatal tasks rely on large-scale annotated datasets, which are difficult to obtain in practice. Although few-shot learning alleviates data scarcity, it typically requires fine-tuning for new categories, limiting its practicality in resource-limited clinical settings. To address these challenges, we propose a training-free framework for multi-class prenatal US anomaly classification and localization that operates with only a few reference images per class, representing the first exploration of this setting. Our framework comprises three key components: (1) a memory bank with multi-granular prototypes that explicitly models both class-level semantics and anomaly characteristics; (2) a prototype-driven soft merging mechanism that aggregates discriminative features to detect the anomaly region; and (3) a class-aware refinement strategy that leverages prototype consistency to improve category prediction. Extensively validated on a multi-center prenatal US dataset containing 1,149 cases, with a total of 2,357 images and 9 categories, our proposed method outperforms the competitors.

---


### 144. [GaussianFusion: Unified 3D Gaussian Representation for Multi-Modal Fusion Perception](https://arxiv.org/abs/2607.00746)

**<font color=#1a73e8>作者：</font>** Xiao Zhao, Chang Liu, Mingxu Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The bird's-eye view (BEV) representation enables multi-sensor features to be fused within a unified space, serving as the primary approach for achieving comprehensive 3D perception. However, the discrete grid representation of BEV leads to significant detail loss and limits feature alignment and cross-modal information interaction in multimodal fusion perception. In this work, we break from the conventional BEV paradigm and propose a new universal framework for multi-modal fusion based on 3D Gaussian representation. This approach naturally unifies multi-modal features within a shared and continuous 3D Gaussian space, effectively preserving edge and fine texture details. To achieve this, we design a novel forward-projection-based multi-modal Gaussian initialization module and a shared cross-modal Gaussian encoder that iteratively updates Gaussian properties based on an attention mechanism. GaussianFusion is inherently a task-agnostic model, with its unified Gaussian representation naturally supporting various 3D perception tasks. Extensive experiments demonstrate the generality and robustness of GaussianFusion. On the nuScenes dataset, it outperforms the 3D object detection baseline BEVFusion by 2.6 NDS. Its variant surpasses GaussFormer on 3D semantic occupancy with 1.55 mIoU improvement while using only 30% of the Gaussians and achieving a 450% speedup.

---


### 145. [FrameONE: Hierarchical Motion Modeling for Universal Multi-View Echocardiographic Keyframe Detection](https://arxiv.org/abs/2607.00748)

**<font color=#1a73e8>作者：</font>** Rusi Chen, Yuhao Huang, Hongyuan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate detection of end-systole (ES) and end-diastole (ED) frames is fundamental to echocardiographic assessment. Existing methods are typically developed in a view-specific manner, depend on auxiliary annotations or intensive visual modeling, which limits their generalizability. In multi-view modeling, keyframe detection is driven by shared cardiac motion, yet large appearance differences and motion patterns make unified modeling challenging. To address these issues, we propose FrameONE, a unified end-to-end framework for multi-view echocardiographic keyframe detection. FrameONE introduces a Hierarchical Motion Modeling strategy: an intra-view multi-task learning reduces appearance bias and promotes motion-focused representations within each view; an inter-view general motion learning module further separates view-agnostic dynamics from view-specific patterns, enabling shared yet flexible motion representation learning across views. Extensive experiments on 25,872 videos spanning four standard views demonstrate that FrameONE achieves state-of-the-art keyframe detection accuracy with strong cross-view generalization. Code is available at this https URL.

---


### 146. [GKDT: General Keypoint Detection Transformer](https://arxiv.org/abs/2607.00752)

**<font color=#1a73e8>作者：</font>** Changsheng Lu, Yuxin Chen, Haokun Gui 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the emergence of various pre-trained vision and language models, computer vision is shifting from narrow-domain to open-domain recognition. The construction of a more powerful yet general keypoint detection (GKD) model to support diverse tasks has become increasingly important in the field. To this end, we firstly present a large-scale unified keypoint dataset called MegaKPT. The dataset is composed of over 1.3 million diverse object instances from twenty-nine existing datasets, and enjoys high-quality unified annotations with keypoint text descriptions. Based on MegaKPT, we develop GKDT, a simple, flexible and powerful DINOv3 based Transformer model for General Keypoint Detection. Our GKDT supports visual prompts, text prompts, or both. To enhance model training, we also propose a suite of useful strategies such as mix-modal prompted training and dynamic importance sampling. By testing over 22 test sets with seen or unseen objects, our single GKDT model shows strong performance and generality in detecting keypoints on broad categories, with most categories over 90\% PCK@0.1 accuracy, offering high practical applicability to real-world problems. The dataset, models, and codes will be released at this https URL.

---


### 147. [Forensic-Oriented Intrusion Detection Using Synthetic Network Traffic Data and Explainable Artificial Intelligence](https://arxiv.org/abs/2607.00763)

**<font color=#1a73e8>作者：</font>** Jose Luis Vela Alonso, Carmen Pellicer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital forensic investigations of network intrusions require analytical outputs that are traceable, reproducible, and court-defensible - requirements existing machine learning pipelines do not satisfy, since they treat original evidence as training data and produce opaque classifications without instance-level justification. This paper presents a forensic-oriented intrusion detection framework resolving both problems simultaneously, integrating synthetic data generation, binary classification, and explainability within a single pipeline governed by ISO/IEC 27037, 27041, 27042, and NIST SP 800-86.
The framework operationalises the ISO/IEC 27037 requirement for strict separation between original digital evidence and derived analytical artefacts. Original datasets are treated as immutable, hash-verified artefacts; all training operates on parameterized synthetic derivatives via SDV + CTGAN. XGBoost binary classification provides high-performance detection on tabular network flow data, and SHAP TreeExplainer produces instance-level feature attributions mapping statistical predictions to observable network behaviour for forensic reporting.
Train-on-Synthetic, Test-on-Real (TSTR) evaluation on CICIDS2017 achieves F1-macro = 0.96, within cross-validation variance of the real-data baseline (0.97). Kolmogorov-Smirnov testing confirms synthetic privacy preservation (mean |KS| = 0.38) alongside operational utility. Cross-dataset validation on UNSW-NB15 and Kitsune identifies feature space dimensionality as the primary determinant of synthetic training effectiveness, establishing a practical deployment boundary of approximately 30 numeric flow-level features. SHAP attributions for Brute Force, Port Scan, and DoS attacks are consistent across real and synthetic instances, confirming synthetic training preserves forensically relevant attack fingerprints required for expert witness testimony.

---


### 148. [Decoupled Guidance: Disentangling Subject and Context Pathways in Text-to-Image Personalization](https://arxiv.org/abs/2607.00766)

**<font color=#1a73e8>作者：</font>** Seongmin Kim, Kyucheol Shin, Heesun Jung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image personalization aims to generate a user-provided subject in novel scenes described by text. However, most existing methods encode subject identity (fidelity) and context (editability) through the same conditioning pathway, forcing the two to compete for attention-map resources. We refer to this phenomenon as conditioning entanglement and show that it induces a fidelity-editability trade-off. We further provide causal evidence by replacing the target subject token with a generic subject token, which produces shifts in attention allocation and corresponding changes in context adherence. To this end, we propose Decoupled Guidance (DeGu), a plug-and-play framework that routes subject identity and scene context through two independent guidance streams. We further introduce a spatial mixing mechanism that dynamically fuses these streams, ensuring each operates within its semantically relevant region without interference. Furthermore, DeGu can be readily applied to existing personalization methods without modifying the underlying backbone models, consistently improving the overall personalization performance while enabling inference-time control over the fidelity-editability balance, across diverse methods and backbones, including flow-matching Diffusion Transformers (DiTs).

---


### 149. [No Country for Old Privacy: The Evolving Challenges of Anonymity in Bitcoin](https://arxiv.org/abs/2607.00772)

**<font color=#1a73e8>作者：</font>** Ben Hawkins, Joshua Levett, Siamak F. Shahandashti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a longitudinal measurement study on the adoption of detectable, second-generation anonymisation protocols in the Bitcoin network, including CoinJoin, CoinSwap, CoinShuffle and Stealth Addresses. By implementing and refining a suite of heuristic filters, we identify over 5.94 million CoinJoin and 23.3 million CoinSwap transactions. Besides, the use of CoinShuffle was unexpectedly found to be closely aligned with the Wasabi wallet operation period. Our analysis reveals consistently low adoption rates, with these protocols constituting less than 1% of network transactions, and a sharp decline in detectable usage following key regulatory events. Furthermore, we find no evidence of standardised Stealth Address adoption, indicating a failure to converge on a common privacy standard. This study provides a comprehensive picture of a niche ecosystem whose on-chain visibility has been largely suppressed, strongly suggesting the migration of privacy-seeking users to less transparent and less detectable methods.

---


### 150. [Accelerating Discrete Diffusion Models with Parallel-In-Time Sampling](https://arxiv.org/abs/2607.00773)

**<font color=#1a73e8>作者：</font>** Yu Yao, Huanjian Zhou, Andi Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models are widely used for learning and generating discrete distributions. As the generation process is inherently sequential, the acceleration of sampling is of significant importance. In this work, we parallelize the mainstream $\tau$-leaping algorithm for absorbing discrete diffusion in a Continuous-Time Markov Chain (CTMC) framework. By leveraging the continuous-time stochastic integral form of the $\tau$-leaping algorithm and the Picard iteration method, we achieve parallel-in-time sampling acceleration and provide a proof of exponential-factorial convergence for our algorithm. We improve the overall time complexity of $\tau$-leaping under absorbing settings from ${\mathcal{O}}(d \log S)$ to ${\mathcal{O}}(\log (d\log S)\cdot \log d)$ with respect to NFE. Empirically, our method shows consistent acceleration across synthetic and real-data settings. The new sampler achieves at most $7$--$9\times$ runtime speedup for synthetic distribution, and maintains the same quality with $50\%$ fewer NFE and $1.45$--$1.86\times$ runtime speedups in image/text tasks on a single GPU. Our research expands the potential of discrete diffusion models for efficient parallel inference, with broader implications for applications such as molecular structure and language generation.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-236](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

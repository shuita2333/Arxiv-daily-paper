# 📦 其他研究 | 2026年04月30日

> 本类共 **190** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-190](./part-04.md)

---

### 101. [VAE-Inf: A statistically interpretable generative paradigm for imbalanced classification](https://arxiv.org/abs/2604.25334)

**<font color=#1a73e8>作者：</font>** Hongfei Wu, Ruijian Han, Yancheng Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imbalanced classification remains a pervasive challenge in machine learning, particularly when minority samples are too scarce to provide a robust discriminative boundary. In such extreme scenarios, conventional models often suffer from unstable decision boundaries and a lack of reliable error control. To bridge the gap between generative modeling and discriminative classification, we propose a two-stage framework \textbf{VAE-Inf} that integrates deep representation learning with statistically interpretable hypothesis testing. In the first stage, we adopt a one-class modeling perspective by training a variational autoencoder (VAE) exclusively on majority-class data to capture the underlying reference distribution. The resulting latent posteriors are aggregated via a Wasserstein barycenter to construct a global Gaussian reference model, providing a geometrically principled baseline for the majority class. In the second stage, we transform this generative foundation into a discriminative classifier by fine-tuning the encoder with limited minority samples. This is achieved through a novel distribution-aware loss that enforces probabilistic separation between classes based on variance-normalized projection statistics. For inference, we introduce a projection-based score that admits a natural hypothesis testing interpretation, allowing for a distribution-free calibration procedure. This approach yields exact finite-sample control of the Type-I error (false positive rate) without relying on restrictive parametric assumptions. Extensive experiments on diverse real-world benchmarks demonstrate that our framework achieves competitive performance against other approaches. The codes are available upon request.

---


### 102. [Benchmarking Layout-Guided Diffusion Models through Unified Semantic-Spatial Evaluation in Closed and Open Settings](https://arxiv.org/abs/2604.25358)

**<font color=#1a73e8>作者：</font>** Luca Parolari, Nicla Faccioli, Lamberto Ballan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating layout-guided text-to-image generative models requires assessing both semantic alignment with textual prompts and spatial fidelity to prescribed layouts. Assessing layout alignment requires collecting fine-grained annotations, which is costly and labor-intensive. Consequently, current benchmarks rarely provide comprehensive layout evaluation and often remain limited in scale or coverage, making model comparison, ranking, and interpretation difficult. In this work, we introduce a closed-set benchmark (C-Bench) designed to isolate key generative capabilities while providing varying levels of complexity in both prompt structure and layout. To complement this controlled setting, we propose an open-set benchmark (O-Bench) that evaluates models using real-world prompts and layouts, offering a measure of semantic and spatial alignment in the wild. We further develop a unified evaluation protocol that combines semantic and spatial accuracy into a single score, ensuring consistent model ranking. Using our benchmarks, we conduct a large-scale evaluation of six state-of-the-art layout-guided diffusion models, totaling 319,086 generated and evaluated images. We establish a model ranking based on their overall performance and provide detailed breakdowns for text and layout alignment to enhance interpretability. Fine-grained analyses across scenarios and prompt complexities highlight the strengths and limitations of current models. Code is available at this https URL.

---


### 103. [HuM-Eval: A Coarse-to-Fine Framework for Human-Centric Video Evaluation](https://arxiv.org/abs/2604.25361)

**<font color=#1a73e8>作者：</font>** Bingzi Zhang, Kaisi Guan, Ruihua Song  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models have developed rapidly in recent years, where generating natural human motion plays a pivotal role. However, accurately evaluating the quality of generated human motion video remains a significant challenge. Existing evaluation metrics primarily focus on global scene statistics, often overlooking fine-grained human details and consequently failing to align with human subjective preference. To bridge this gap, we propose HuM-Eval, a novel human-centric evaluation framework that adopts a coarse-to-fine strategy. Specifically, our framework first utilizes a Vision Language Model to perform a coarse assessment of global video quality. It then proceeds to a fine-grained analysis, using 2D pose to verify anatomical correctness and 3D human motion to evaluate motion stability. Extensive experiments demonstrate that HuM-Eval achieves an average human correlation of 58.2%, outperforming state-of-the-art baselines. Furthermore, we introduce HuM-Bench, a comprehensive benchmark comprising 1,000 diverse prompts, and conduct a detailed evaluation of existing text-to-video models, paving the way for next-generation human motion generation.

---


### 104. [Self-DACE++: Robust Low-Light Enhancement via Efficient Adaptive Curve Estimation](https://arxiv.org/abs/2604.25367)

**<font color=#1a73e8>作者：</font>** Jianyu Wen, Jun Xie, Feng Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we present Self-DACE++, an improved unsupervised and lightweight framework for Low-Light Image Enhancement (LLIE), building upon our previous Self-Reference Deep Adaptive Curve Estimation (Self-DACE). To better address the trade-off between computational efficiency and restoration quality, Self-DACE++ introduces enhanced Adaptive Adjustment Curves (AACs). These curves, governed by minimal trainable parameters, flexibly adjust the dynamic range while preserving the color fidelity, structural integrity, and naturalness of the enhanced images. To achieve an extremely lightweight architecture without sacrificing performance, we propose a randomized order training strategy coupled with a network fusion mechanism, which compresses the model into an efficient iterative inference structure. Furthermore, we formulate a physics-grounded objective function based on Retinex theory and incorporate a dedicated denoising module to effectively estimate and suppress latent noise in dark regions. Extensive qualitative and quantitative evaluations on multiple real-world benchmark datasets demonstrate that Self-DACE++ outperforms existing state-of-the-art methods, delivering superior enhancement quality with real-time inference capability. The code is available at this https URL.

---


### 105. [Multi-action Tangled Program Graphs for Multi-task Reinforcement Learning with Continuous Control](https://arxiv.org/abs/2604.25369)

**<font color=#1a73e8>作者：</font>** Quentin Vacher, Nicolas Beuve, Mickaël Dardaillon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Over the past few decades, machine learning has been widely used to learn complex tasks. Reinforcement Learning (RL), inspired by human behavior, is a great example, as it involves developing specific behaviours for specific tasks. To further challenge algorithms, Multi-Task RL (MTRL) environments have been introduced, requiring a single model to learn multiple behaviors. The Tangled Program Graph (TPG) algorithm is a Genetic Programming (GP) algorithm designed for discrete MTRL environments. Recently, the MAPLE algorithm has been proposed, as another GP algorithm that achieves high results in single task continuous RL environments. A variation of the TPG is proposed alongside MAPLE, named Multi-Action TPG (MATPG) that aggregates MAPLE agents, and creates a control flow to activate them. Initially tested on single task RL environments only, MATPG achieved similar results to MAPLE. In this work, we present a new benchmark based on the MuJoCo Half Cheetah from Gymnasium. This benchmark features five distinct obstacles that are randomly positioned in front of the agent, each of which demands a unique behavior. This benchmark serves as a use case for MATPG, to prove its ability as a GP solution for continuous MTRL environments. Our experiments demonstrate its superiority in this multi-task use case when combined with lexicase selection. Furthermore, we examine the interpretability of the evolved graph, revealing that the decision flow of the model is fully interpretable.

---


### 106. [Language corpora for the Dutch medical domain](https://arxiv.org/abs/2604.25374)

**<font color=#1a73e8>作者：</font>** B. van Es  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> \textbf{Background:} Dutch medical corpora are scarce, limiting NLP development. \\ \textbf{Methods:} We translated English datasets, identified medical text in generic corpora, and extracted open Dutch medical resources. \\ \textbf{Results:} The resulting corpus comprises $\pm$ 35 billion tokens across the medical domain in about 100 million documents, freely available on Hugging Face. \\ \textbf{Conclusion:} This work establishes the first large-scale Dutch medical language corpus for pre-training and downstream NLP tasks.

---


### 107. [CoRE: Concept-Reasoning Expansion for Continual Brain Lesion Segmentation](https://arxiv.org/abs/2604.25376)

**<font color=#1a73e8>作者：</font>** Qianqian Chen, Anglin Liu, Jingyang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate brain lesion segmentation in MRI is vital for effective clinical diagnosis and treatment planning. Due to high annotation costs and strict data privacy regulations, universal models require employing Continual Learning (CL) to adapt to evolving clinical tasks without losing previously acquired knowledge. However, existing CL paradigms often suffer from capacity limits or redundant parameter growth, and even advanced dynamic methods rely mostly on image-perception strategies that struggle to handle the substantial pathological and multimodal heterogeneity inherent in brain imaging. To address this issue, we propose Concept-Reasoning Expansion (CoRE) framework, which establishes a joint decision-making mechanism by integrating visual features with structured concepts. Through the alignment of image tokens with a hierarchical concept library, CoRE simulates clinical reasoning to guide both interpretable expert routing and demand-based model growth. This collaborative process ensures model evolution is grounded in clinical priors, preventing redundant parameter expansion while maximizing knowledge reuse. Extensive evaluations across 12 sequential brain lesion MRI tasks demonstrate that CoRE achieves state-of-the-art performance and provides a high knowledge starting point for efficient future adaptation. Its superior few-shot transferability and clinical interpretability further validate its effectiveness in managing non-stationary clinical data streams. Our code will be released soon.

---


### 108. [Safe-Support Q-Learning: Learning without Unsafe Exploration](https://arxiv.org/abs/2604.25379)

**<font color=#1a73e8>作者：</font>** Yeeun Lim, Narim Jeong, Donghwan Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensuring safety during reinforcement learning (RL) training is critical in real-world applications where unsafe exploration can lead to devastating outcomes. While most safe RL methods mitigate risk through constraints or penalization, they still allow exploration of unsafe states during training. In this work, we adopt a stricter safety requirement that eliminates unsafe state visitation during training. To achieve this goal, we propose a Q-learning-based safe RL framework that leverages a behavior policy supported on a safe set. Under the assumption that the induced trajectories remain within the safe set, this policy enables sufficient exploration within the safe region without requiring near-optimality. We adopt a two-stage framework in which the Q-function and policy are trained separately. Specifically, we introduce a KL-regularized Bellman target that constrains the Q-function to remain close to the behavior policy. We then derive the policy induced from the trained Q-values and propose a parametric policy extraction method to approximate the optimal policy. Our approach provides a unified framework that can be adapted to different action spaces and types of behavior policies. Experimental results demonstrate that the proposed method achieves stable learning and well-calibrated value estimates and yields safer behavior with comparable or better performance than existing baselines.

---


### 109. [Benchmarking and Improving GUI Agents in High-Dynamic Environments](https://arxiv.org/abs/2604.25380)

**<font color=#1a73e8>作者：</font>** Enqi Liu, Liyuan Pan, Zhi Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Graphical User Interface (GUI) agents have predominantly focused on training paradigms like supervised fine-tuning (SFT) and reinforcement learning (RL). However, the challenge of high-dynamic GUI environments remains largely underexplored. Existing agents typically rely on a single screenshot after each action for decision-making, leading to a partially observable (or even unobservable) Markov decision process, where the key GUI state including important information for actions is often inadequately captured. To systematically explore this challenge, we introduce DynamicGUIBench, a comprehensive online GUI benchmark spanning ten applications and diverse interaction scenarios characterized by important interface changes between actions. Furthermore, we present DynamicUI, an agent designed for dynamic interfaces, which takes screen-recording videos of the interaction process as input and consists of three components: a dynamic perceiver, a refinement strategy, and a reflection. Specifically, the dynamic perceiver clusters frames of the GUI video, generates captions for the centroids, and iteratively selects the most informative frames as the salient dynamic context. Considering that there may be inconsistencies and noise between the selected frames and the textual context of the agent, the refinement strategy employs an action-conditioned filtering to refine thoughts to mitigate thought-action inconsistency and redundancy. Based on the refined agent trajectories, the reflection module provides effective and accurate guidance for further actions. Experiments on DynamicGUIBench demonstrate that DynamicUI significantly improves the performance in dynamic GUI environments, while maintaining competitive performance on other public benchmarks.

---


### 110. [Wiki Dumps to Training Corpora: South Slavic Case](https://arxiv.org/abs/2604.25384)

**<font color=#1a73e8>作者：</font>** Mihailo Škorić  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a methodology for transforming raw Wikimedia dumps into quality textual corpora for seven South Slavic languages. The work is divided into two major phases. The first involves extracting and cleaning text from raw dumps of Wikipedia, Wikisource, Wikibooks, Wikinews, and Wikiquote, where available. This step requires careful handling of raw wiki markup to isolate, first of all, textual articles, and then usable natural language text within them. The second phase addresses the challenge of suspicious or low-quality articles, which are often generated from databases or structured knowledge bases. These articles are characterised by repetitive patterns, generic phrasing, and minimal to no original content. To mitigate their impact, a n-gram-based filtering strategy was employed to detect high levels of textual redundancy between articles and then remove such articles from the corpora entirely. The resulting datasets aim to provide linguistically rich texts suitable for training language models or conducting comparative research across South Slavic languages. By combining systematic extraction with quality control, this work contributes to the creation of reliable, high-information corpora that reflect authentic language use and cultural context. While focused on the South Slavic case in the paper, the approach is mostly language-agnostic and can be generalised to other languages and language families.

---


### 111. [COMPASS: COmpact Multi-channel Prior-map And Scene Signature for Floor-Plan-Based Visual Localization](https://arxiv.org/abs/2604.25388)

**<font color=#1a73e8>作者：</font>** Muhammad Shaheer, Miguel Fernandez-Cortizas, Asier Bikandi-Noya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Architectural floor plans are widely available priors which contain not only geometry but also the semantic information of the environment, yet existing localization methods largely ignore this semantic information. To address this, we present COMPASS, an algorithm that exploits both geometric and semantic priors from floor plans to estimate the pose of a robot equipped with dual fisheye cameras. Inspired by scan context descriptor from LiDAR-based place recognition, we design a multi-channel radial descriptor that encodes the geometric layout surrounding a position. From the floor plan, rays are cast in 360 azimuth bins and the results are encoded into five channels: normalized range, structural hit type (wall, window, or opening), range gradient, inverse range, and local range variance. From the image side, the same descriptor structure is populated by detecting structural elements in the fisheye imagery. As a first step toward full cross-modal matching, we present a window detection algorithm for fisheye images that uses a line segment detector to identify window frames via vertical edge clustering and brightness verification. Detected windows are projected to azimuthal bearings through the fisheye camera model, producing the hit-type channel of the visual descriptor. As a proof of concept, we generate both descriptors at a single known pose from the Hilti-Trimble SLAM Challenge 2026 dataset and demonstrate that the wall-window pattern extracted from the first frame of each camera closely matches the floor plan descriptor, validating the feasibility of cross-modal structural matching.

---


### 112. [Co-Writing with AI: An Empirical Study of Diverse Academic Writing Workflows](https://arxiv.org/abs/2604.25389)

**<font color=#1a73e8>作者：</font>** Silvia Bodei, Duncan P. Brumby, Katie Fisher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite AI tools becoming increasingly embedded in academic practice, little is known about how university students integrate them into their writing processes. We examine how students engage with AI across different writing tasks, and how this engagement is shaped by individual factors including AI literacy, writing confidence, trust, authorship concerns, and motivation. Study~1 surveys 107 UK university students to map task-specific and co-occurring patterns of AI use across five writing stages (ideation, sourcing, planning, drafting, and reviewing) and their associations with individual factors. Study~2 complements this by exploring how these patterns can be assembled in practice, through interviews with 12 postgraduates reflecting on their established use of AI in assessed writing. Together, the studies suggest that AI integration is selective and heterogeneous, forming three recurring and value-oriented configurations: (1) early-stage (learning-oriented), where tools support exploration and understanding; (2) late-stage (quality-oriented), where tools support drafting and refinement; and (3) peripheral (productivity-oriented), where tools are used to reduce friction and sustain momentum across the process. We offer a workflow-level account of AI-supported academic writing, showing how students navigate competing priorities of learning, quality, productivity, and authorship, and how they evaluate and take responsibility for AI-generated outputs.

---


### 113. [Beyond Fidelity: Semantic Similarity Assessment in Low-Level Image Processing](https://arxiv.org/abs/2604.25408)

**<font color=#1a73e8>作者：</font>** Runjie Wang, Weiling Chen, Tiesong Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-level image processing has long been evaluated mainly from the perspective of visual fidelity. However, with the rise of deep learning and generative models, processed images may preserve perceptual quality while altering semantic content, making conventional Image Quality Assessment (IQA) insufficient for semantic-level assessment. In this paper, we formalize \textit{Semantic Similarity} as a new evaluation task for low-level image processing, aimed at measuring whether semantic content is preserved after processing. We further present a structured formulation of image semantics based on semantic entities and their relations, and discuss the desired properties and constraints of a valid semantic similarity index. Based on this formulation, we propose Triplet-based Semantic Similarity Score (T3S), which models image semantics through foreground entities, background entities, and relations. T3S combines semantic entity extraction, foreground-background disentanglement, and open-world class/relation modeling. Experiments on COCO and SPA-Data show that T3S consistently outperforms existing fidelity-oriented metrics and representative semantic-level baselines, while better reflecting progressive semantic changes under diverse degradations. These results highlight the importance of semantic assessment in modern low-level vision.

---


### 114. [Scaling Probabilistic Transformer via Efficient Cross-Scale Hyperparameter Transfer](https://arxiv.org/abs/2604.25409)

**<font color=#1a73e8>作者：</font>** Penghao Kuang, Haoyi Wu, Kewei Tu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Probabilistic Transformer (PT), a white-box probabilistic model for contextual word representation, has demonstrated substantial similarity to standard Transformers in both computational structure and downstream task performance on small models and small to medium sized datasets. However, PT is less robust to hyperparameter choices than standard Transformers, making it harder to scale efficiently. In this work, we follow Maximal Update Parametrization (muP) to rescale PT's parameters, so that hyperparameters optimized on small models can be transferred to larger models without additional tuning. With this approach, we successfully scale PT to models with up to 0.4B parameters. Experiments show that PT consistently outperforms standard transformer under the same parameter budget on Masked Language Modeling (MLM) tasks. We hope this work will contribute to the practical deployment of probabilistic models at substantially larger scales in the future.

---


### 115. [Biased Dreams: Limitations to Epistemic Uncertainty Quantification in Latent Space Models](https://arxiv.org/abs/2604.25416)

**<font color=#1a73e8>作者：</font>** Julia Berger, Bernd Frauenknecht, Sebastian Trimpe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-Based Reinforcement Learning distinguishes between physical dynamics models operating on proprioceptive inputs and latent dynamics models operating on high-dimensional image observations. A prominent latent approach is the Recurrent State Space Model used in the Dreamer family. While epistemic uncertainty quantification to inform exploration and mitigate model exploitation is well established for physical dynamics models, its transfer to latent dynamics models has received limited scrutiny. We empirically demonstrate that latent transitions are biased toward well-represented regions of latent space, exhibiting an attractor behavior that can deviate from true environment dynamics. As a result, discrepancies in environment dynamics may not manifest in latent space, undermining the reliability of epistemic uncertainty estimates. Because these attractors often lie in high-reward regions, latent rollouts systematically overestimate predicted rewards. Our findings highlight key limitations of epistemic uncertainty estimation in latent dynamics models and motivate more critical evaluation of this method.

---


### 116. [JURY-RL: Votes Propose, Proofs Dispose for Label-Free RLVR](https://arxiv.org/abs/2604.25419)

**<font color=#1a73e8>作者：</font>** Xinjie Chen, Biao Fu, Jing Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) enhances the reasoning of large language models (LLMs), but standard RLVR often depends on human-annotated answers or carefully curated reward specifications. In machine-checkable domains, label-free alternatives such as majority voting or LLM-as-a-judge remove annotation cost but can introduce false positives that destabilize training. We introduce JURY-RL, a label-free RLVR framework that decouples answer proposal from reward disposal: votes from model rollouts propose a candidate answer, and a formal verifier determines whether that candidate can receive positive reward. Concretely, only rollouts matching the plurality-voted answer are rewarded when that answer is successfully verified in Lean. When verification is inconclusive, we invoke ResZero (Residual-Zero), a fallback reward that discards the unverified plurality proposal and redistributes a zero-mean, variance-preserving signal over the residual answers. This design maintains a stable optimization gradient without reinforcing unverifiable consensus. Across three backbone models trained on mathematical data, JURY-RL consistently outperforms other label-free baselines on mathematical reasoning benchmarks and transfers competitively to code generation and general benchmarks. It attains pass@1 performance comparable to supervised ground-truth training, with superior generalization demonstrated by higher pass@k and response diversity.

---


### 117. [SARU: A Shadow-Aware and Removal Unified Framework for Remote Sensing Images with New Benchmarks](https://arxiv.org/abs/2604.25432)

**<font color=#1a73e8>作者：</font>** Zi-Yang Bo, Wei Lu, Hongruixuan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shadows are a prevalent problem in remote sensing imagery (RSI), degrading visual quality and severely limiting the performance of downstream tasks like object detection and semantic segmentation. Most prior works treat shadow detection and removal as separate, cascaded tasks, which can lead to cumbersome process and error accumulation. Furthermore, many deep learning methods rely on paired shadow and non-shadow images for training, which are often unavailable in practice. To address these challenges, we propose Shadow-Aware and Removal Unified (SARU) Framework , a cohesive two-stage framework. First, its dual-branch detection module (DBCSF-Net) fuses multi-color space and semantic features to generate high-fidelity shadow masks, effectively distinguishing shadows from dark objects. Then, leveraging these masks, a novel, training-free physical algorithm (N$^2$SGSR) restores illumination by transferring properties from adjacent non-shadow regions within the single input image. To facilitate rigorous evaluation and foster future work, we also introduce two new benchmark datasets: the RSI Shadow Detection (RSISD) dataset and the Single-image Shadow Removal Benchmark (SiSRB). Extensive experiments demonstrate that SARU achieves state-of-the-art performance on both the public AISD dataset and our newly introduced benchmarks. By holistically integrating shadow detection and removal to mitigate error propagation and eliminating the dependency on paired training data, SARU establishes a robust, practical framework for real-world RSI analysis. The source code and datasets are publicly available at: this https URL.

---


### 118. [PI-TTA: Physics-Informed Source-Free Test-Time Adaptation for Robust Human Activity Recognition on Mobile Devices](https://arxiv.org/abs/2604.25435)

**<font color=#1a73e8>作者：</font>** Changyu Li, Lu Wang, Ming Lei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Source-free test-time adaptation (TTA) is appealing for mobile and wearable sensing because it enables on-device personalization from unlabeled test streams without centralizing private data. However, sensor-based human activity recognition (HAR) poses challenges that are less pronounced in standard vision benchmarks: behavioral inertial streams are temporally correlated and often exhibit within-session shifts caused by sensor rotation, placement change, and sampling-rate drift. Under this streaming non-i.i.d. setting, widely used vision-style TTA objectives can become unstable, leading to overconfident errors, representation collapse, and catastrophic forgetting. We propose PI-TTA, a lightweight source-free adaptation framework that stabilizes online updates through three physics-consistent constraints: gravity consistency, short-horizon temporal continuity, and spectral stability. PI-TTA updates the same small parameter subset as strong source-free baselines and incurs only modest overhead, making it suitable for on-device deployment. Experiments on USCHAD, PAMAP2, and mHealth under long-sequence stress tests and factorized shift protocols show that PI-TTA mitigates the severe degradation observed in confidence-driven baselines and preserves stable adaptation under sustained streaming conditions. It improves long-sequence accuracy by up to 9.13% and reduces physical-violation rates by 27.5%, 24.1%, and 45.4% on USCHAD, PAMAP2, and mHealth, respectively. These results demonstrate that physics-informed adaptation can improve accuracy, stability, and deployment reliability for real-world mobile sensing systems.

---


### 119. [Rewiring Perceived Doability in VR: Hand Redirection as a Subtle Cross-Sensory Support for Sustained Practice](https://arxiv.org/abs/2604.25443)

**<font color=#1a73e8>作者：</font>** Isidro Butaslac, Yota Nagaya, Almira Princess Redoble 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In everyday life, physical effort is often minimized and convenience is prioritized, making it difficult for many people to sustain light exercise and stretching despite well-known long-term benefits. This challenge often arises not from objective movement limitations, but from whether an action feels doable in the moment and, therefore worth continuing. This position paper argues that subtle VR hand redirection (HR) can be reframed as a form of cross-sensory support for sustained practice by targeting perceived doability: a moment-to-moment cognitive appraisal that an action is within one's capability while requiring manageable effort. We propose that conservative HR, applied within known perceptual limits, can create repeated micro-success experiences (e.g., reaching a virtual goal earlier with similar physical movement). These micro-successes may increase continuation intention and early re-engagement without relying on overt pressure or intensive coaching. At the same time, such support raises questions about autonomy and authenticity. We therefore articulate two research questions: (RQ1) how HR shifts perceived doability to support sustained practice and positive behavior change; and (RQ2) when HR functions as acceptable support versus becoming counterproductive by undermining authenticity, agency, trust, or fostering dependence. We present an initial sit-and-reach VR prototype, outline a research plan, and identify key design tensions to spark community discussions on autonomy-preserving cross-sensory futures in HCI.

---


### 120. [Benchmarking Logistic Regression, SVM, and LightGBM Against BiLSTM with Attention for Sentiment Analysis on Indonesian Product Reviews](https://arxiv.org/abs/2604.25452)

**<font color=#1a73e8>作者：</font>** Razin Hafid Hamdi, Ivana Margareth Hutabarat, Hanna Gresia Sinaga 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentiment analysis of product reviews on e-commerce platforms plays a critical role in automatically understanding customer satisfaction and providing actionable insights for sellers seeking to improve product quality. This paper presents a comprehensive benchmarking study comparing a Machine Learning (ML) approach via the PyCaret AutoML framework against a Deep Learning (DL) approach based on a Bidirectional Long Short-Term Memory (BiLSTM) architecture with an Attention mechanism for binary sentiment classification on Indonesian product reviews. The dataset comprises 19,728 samples balanced equally between positive and negative reviews. For the ML approach, three prominent algorithms were evaluated via 10-fold stratified cross-validation: Logistic Regression (LR), Support Vector Machine (SVM) with a linear kernel, and Light Gradient Boosting Machine (LightGBM). Logistic Regression achieved the best ML performance with an accuracy of 97.26\% and an F1-score of 97.26\%. The BiLSTM with Attention model, evaluated on 3,946 held-out test samples, achieved an accuracy of 97.24\% and an F1-score of 97.24\%. These comparative results demonstrate that traditional ML algorithms with proper preprocessing and feature extraction can compete closely with, and even marginally outperform, more complex sequential DL architectures on high-dimensional datasets, while simultaneously offering greater computational efficiency.

---


### 121. [Generative UI as an Accessibility Bridge: Lessons from C2C E-Commerce](https://arxiv.org/abs/2604.25455)

**<font color=#1a73e8>作者：</font>** Bektur Ryskeldiev  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Web accessibility rests on static standards and developer compliance. That model frays in platforms where content is user-generated: photos arrive blurry or off-frame, descriptions skip size and condition, and page structure shifts from listing to listing. Drawing on six studies conducted between 2022 and 2025 with blind, low-vision, and older adult users of customer-to-customer (C2C) marketplaces, I argue that generative UI can produce adapted interfaces at the point of use, addressing barriers that static design cannot anticipate. Three interventions from this program -- HTML regeneration for screen readers, conversational guidance for older sellers, and audio-guided photo framing for blind sellers -- demonstrate how runtime generation can bridge gaps that standards leave open. I outline what these findings imply for HCI practice: generative UI extends beyond the screen, complements rather than replaces ability-based design, and shifts the designer's role from specifying layouts to specifying policies. This is an expanded arXiv version of a position paper accepted at the CHI 2026 workshop "What does Generative UI mean for HCI Practice?"

---


### 122. [GramSR: Visual Feature Conditioning for Diffusion-Based Super-Resolution](https://arxiv.org/abs/2604.25457)

**<font color=#1a73e8>作者：</font>** Fabio D'Oronzio, Federico Putamorsi, Leonardo Zini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent advances, single-image super-resolution (SR) remains challenging, especially in real-world scenarios with complex degradations. Diffusion-based SR methods, particularly those built on Stable Diffusion, leverage strong generative priors but commonly rely on text conditioning derived from semantic captioning. Such textual descriptions provide only high-level semantics and lack the spatially aligned visual information required for faithful restoration, leading to a representation gap between abstract semantics and spatially aligned visual details. To address this limitation, we propose GramSR, a one-step diffusion-based SR framework that replaces text conditioning with dense visual features extracted from the low-resolution input using a pre-trained DINOv3 encoder. GramSR adopts a three-stage LoRA architecture, where pixel-level, semantic-level, and texture-level LoRA modules are trained sequentially. The pixel-level module focuses on degradation removal using $\ell_2$ loss, the semantic-level module enhances perceptual details via LPIPS and CSD losses, and the texture-level module enforces feature correlation consistency through a Gram matrix loss computed from DINOv3 features. At inference, independent guidance scales enable flexible control over degradation removal, semantic enhancement, and texture preservation. Extensive experiments on standard SR benchmarks demonstrate that GramSR consistently outperforms existing one-step diffusion-based methods, achieving superior structural fidelity and texture realism. The code for this work is available at: this https URL.

---


### 123. [Image Compression with Bubble-Aware Frame Rate Adaptation for Energy-Efficient Video Capsule Endoscopy](https://arxiv.org/abs/2604.25464)

**<font color=#1a73e8>作者：</font>** Oliver Bause, Jörg Gammerdinger, Julia Werner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Capsule Endoscopy (VCE) is a promising method for improving the medical examination of the small intestine in the gastrointestinal tract. A key challenge is their limited size, resulting in a short battery lifetime which conflicts with high energy consumption for image capturing and transmission to an on-body device. Thus, we propose an image compression pipeline that substantially reduces the transmitted data while preserving diagnostic image quality. Furthermore, we exploit characteristics of the compression process to identify frames with low diagnostic value mainly caused by bubbles, without requiring additional image analysis. For low-visibility frames, a dynamic bubble-aware frame rate adaptation strategy reduces image acquisition and transmission during these phases while preserving sensitivity to potential anomalies. The proposed compression and frame rate adaptation are evaluated on a RISC-V platform using the Kvasir-Capsule and Galar datasets. The compression method achieves a compression ratio of 5.748 (82.6%) at a peak signal-to-noise ratio of 40.3 dB, indicating negligible loss of visual quality. The compression accomplished a mean energy reduction of the whole system by 20.58%. Additionally, the proposed bubble-aware frame rate adaptation reduced the energy consumption by up to 40%. These results demonstrate the potential of our method to increase the applicability of VCE.

---


### 124. [Generalizable Human Gaussian Splatting via Multi-view Semantic Consistency](https://arxiv.org/abs/2604.25466)

**<font color=#1a73e8>作者：</font>** Jingi Kim, Wonjun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, generalizable human Gaussian splatting from sparse-view inputs has been actively studied for the photorealistic human rendering. Most existing methods rely on explicit geometric constraints or predefined structural representations to accurately position 3D Gaussians. Although these approaches have shown the remarkable progress in this field, they still suffer from inconsistent feature representations across multi-view inputs due to complex articulations of the human body and limited overlaps between different views. To address this problem, we propose a novel method to accurately localize 3D Gaussians and ultimately improve the quality of human rendering. The key idea is to unproject latent embeddings encoded from each viewpoint into a shared 3D space through predicted depth maps and recalibrate them belonging to the same body part based on cross-view attention. This helps the model resolve the spatial ambiguity occurring in highly textured regions as well as occluded body parts, thus leading to the accurate localization of 3D Gaussians. Experimental results on benchmark datasets show that the proposed method efficiently improves the performance of generalizable human Gaussian splatting from sparse-view inputs.

---


### 125. [Subspace Optimization for Efficient Federated Learning under Heterogeneous Data](https://arxiv.org/abs/2604.25467)

**<font color=#1a73e8>作者：</font>** Shuchen Zhu, Zhengyang Huang, Yuqi Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning increasingly operates in a large-model regime where communication, memory, and computation are all scarce. Typically, non-IID client data induce drift that degrades the stability and performance of local training. Existing remedies such as SCAFFOLD introduce heterogeneity-correction mechanisms to address this challenge, but they incur substantial extra communication and memory overhead. This paper proposes a subspace optimization method for federated learning (SSF), which performs heterogeneity-corrected optimization in a low-dimensional subspace using only projected quantities, while preserving full-dimensional control information through a backfill-style update that retains residual components whenever the active subspace changes. Under standard smoothness and bounded-variance assumptions, SSF attains a non-asymptotic rate of order $\widetilde{\mathcal{O}}(1/T+1/\sqrt{NKT})$. Experiments show favorable accuracy--efficiency trade-offs under heterogeneous data.

---


### 126. [DDA-Thinker: Decoupled Dual-Atomic Reinforcement Learning for Reasoning-Driven Image Editing](https://arxiv.org/abs/2604.25477)

**<font color=#1a73e8>作者：</font>** Hanqing Yang, Qiang Zhou, Yongchao Du 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent image editing models have achieved strong visual fidelity but often struggle with tasks requiring complex reasoning. To investigate and enhance the reasoning-grounded planning for image editing, we propose DDA-Thinker, a Thinker-centric framework designed for the independent optimization of a planning module (Thinker) over a fixed generative model (Editor). This decoupled Thinker-centric paradigm facilitates a controlled analysis of the planning module and makes its contribution under a fixed Editor easier to assess. To effectively guide this Thinker, we introduce a dual-atomic reinforcement learning framework. This framework decomposes feedback into two distinct atomic rewards implemented through verifiable checklists: a cognitive-atomic reward to directly assess the quality of the Thinker's executable plan, which serves as the actionable outcome of the Thinker's reasoning, and a visual-atomic reward to assess the final image quality. To improve checklist quality, our checklist synthesis is grounded not only in the source image and user instruction but also in a rational reference description of the ideal post-edit scene. To support this training, we further develop a two-stage data curation pipeline that first synthesizes a diverse and reasoning-focused dataset, then applies difficulty-aware refinement to curate an effective training curriculum for reinforcement learning. Extensive experiments on reasoning-driven image editing benchmarks, including RISE-Bench and KRIS-Bench, demonstrate that our approach substantially improves overall performance. Our method enables a community model to achieve results competitive with strong proprietary models, highlighting the practical potential of Thinker-centric optimization under a fixed-editor setting.

---


### 127. [From World-Gen to Quest-Line: A Dependency-Driven Prompt Pipeline for Coherent RPG Generation](https://arxiv.org/abs/2604.25482)

**<font color=#1a73e8>作者：</font>** Dominik Borawski, Marta Szulc, Robert Chudy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong potential for narrative generation, but their use in complex, multi-layered role-playing game (RPG) worlds is still limited by issues of coherence, controllability, and structural consistency. This paper explores a dependency-aware, multi-stage prompt pipeline for procedural RPG content generation that models narrative dependencies through structured intermediate representations. The approach decomposes generation into sequential stages: world building, non-player character creation, player character creation, campaign-level quest planning, and quest expansion. Each stage conditions on structured JSON outputs from previous stages. By enforcing schemas and explicit data flow, the pipeline reduces narrative drift, limits hallucinations, and supports scalable creation of interconnected narrative elements. The system is evaluated qualitatively through human-centered analysis across multiple independent runs. Outputs are assessed using criteria such as structural completeness, internal consistency, narrative coherence, diversity, and actionability. Results show that the pipeline consistently generates logically sound and structurally valid RPG content, without quality degradation as complexity increases. Separating high-level campaign planning from detailed quest expansion improves both global structure and local storytelling. These findings suggest that dependency-aware prompt pipelines with structured intermediate representations are an effective design pattern for LLM-based procedural content generation. This approach may also generalize to other domains requiring sequential reasoning over evolving contextual states.

---


### 128. [ReTokSync: Self-Synchronizing Tokenization Disambiguation for Generative Linguistic Steganography](https://arxiv.org/abs/2604.25486)

**<font color=#1a73e8>作者：</font>** Yaofei Wang, Rui Wang, Weilong Pang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative linguistic steganography (GLS) enables covert communication by embedding secret messages into the natural language generation process. In practical deployment, however, GLS is vulnerable to tokenization ambiguity: the same surface text may be re-tokenized into a different token sequence at the receiver, breaking the shared decoding state between the communicating parties so that a single local mismatch can propagate into complete extraction failure. Existing solutions either remove ambiguous tokens -- distorting the generation distribution and compromising security -- or preserve the distribution at the cost of substantially reduced embedding capacity or prohibitive runtime overhead. To address this issue, we propose ReTokSync (Re-Tokenization Synchronization), a self-synchronizing disambiguation framework that monitors the receiver-view tokenization during generation and triggers a corrective reset only when ambiguity actually occurs. By confining the effect of tokenization ambiguity to sparse residual bit errors rather than global desynchronization, ReTokSync leaves ambiguity-free positions entirely untouched and remains compatible with the underlying steganographic algorithm. Experiments on both English and Chinese settings show that ReTokSync stays closest to the steganographic baseline in distributional security (zero KL divergence), text quality, embedding capacity, and runtime, while achieving extraction accuracy above 99.7\%. Building on this property, we further develop a two-channel covert communication mechanism in which ReTokSync serves as the primary channel and a reliable auxiliary channel corrects the remaining errors, achieving 100\% end-to-end recovery across all evaluated configurations.

---


### 129. [The Forensic Cost of Watermark Removal](https://arxiv.org/abs/2604.25491)

**<font color=#1a73e8>作者：</font>** Gautier Evennou, Ewa Kijak  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current watermark removal methods are evaluated on two axes: attack success rate and perceptual quality. We show this is insufficient. While state-of-the-art attacks successfully degrade the watermark signal without visible distortion, they leave distinct statistical artifacts that betray the removal attempt. We name this overlooked axis Watermark Removal Detection (WRD) and demonstrate that a modern classifier trained on these artifacts achieves state-of-the-art detection rates at $10^{-3}$ FPR across every removal method tested. No existing attack accounts for this forensic leakage. We benchmark leading watermarking schemes against standard removal pipelines under the extended evaluation triple of attack success, perceptual quality, and forensic detectability, and find that no current method balances all three. Our results establish forensic stealthiness as a necessary requirement for watermark removal.

---


### 130. [Improving Zero-Shot Offline RL via Behavioral Task Sampling](https://arxiv.org/abs/2604.25496)

**<font color=#1a73e8>作者：</font>** Nazim Bendib, Nicolas Perrin-Gilbert, Olivier Sigaud  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Offline zero-shot reinforcement learning (RL) aims to learn agents that optimize unseen reward functions without additional environment interaction. The standard approach to this problem trains task-conditioned policies by sampling task vectors that define linear reward functions over learned state representations. In most existing algorithms, these task vectors are randomly sampled, implicitly assuming this adequately captures the structure of the task space. We argue that doing so leads to suboptimal zero-shot generalization. To address this limitation, we propose extracting task vectors directly from the offline dataset and using them to define the task distribution used for policy training. We introduce a simple and general reward function extraction procedure that integrates into existing offline zero-shot RL algorithms. Across multiple benchmark environments and baselines, our approach improves zero-shot performance by an average of 20%, highlighting the importance of principled task sampling in offline zero-shot RL.

---


### 131. [EvoTSC: Evolving Feature Learning Models for Time Series Classification via Genetic Programming](https://arxiv.org/abs/2604.25499)

**<font color=#1a73e8>作者：</font>** Xuanhao Yang, Bing Xue, Mengjie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series classification is an important analytical task across diverse domains. However, its practical application is often hindered by the scarcity of labeled data and the requirement for substantial computational resources. To address these challenges, this paper proposes EvoTSC, a novel genetic programming approach designed to automatically evolve lightweight feature learning models for time series classification. The core of EvoTSC is a carefully designed multi-layer program structure that strategically embeds diverse forms of prior expert knowledge into the evolutionary process, effectively guiding the search toward operations known to be highly effective for time series analysis. To mitigate the common overfitting problem in time series classification, a tailored Pareto tournament selection strategy is proposed to favor models that perform consistently well across varying training data subsets, promoting the discovery of highly generalizable models. Extensive experiments conducted on univariate time series classification datasets demonstrate that EvoTSC significantly outperforms eleven benchmark methods in most comparisons. Further analyses verify the contribution of each component and the resource efficiency of the evolved models.

---


### 132. [Making the Invisible Visible: Toward Micro-Expression Visualization for Empathy in Social Interaction](https://arxiv.org/abs/2604.25505)

**<font color=#1a73e8>作者：</font>** Feiyang Yin, Isidro Butaslac, Patrick Gebhard 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Micro-expressions are brief and subtle facial movements that convey nuanced affective information but often remain imperceptible during natural social interaction. Although prior research has primarily focused on computational recognition and spotting of micro-expressions, their application in human-centered contexts remains limited. From the perspective of social augmentation, this work proposes a conceptual framework for micro-expression visualization that transforms otherwise imperceptible micro-expressions into perceptible affective cues, with the aim of exploring their potential influence on empathic experience. Furthermore, we outline a planned pilot study to preliminarily assess the feasibility of this framework under controlled conditions.

---


### 133. [Dyna-Style Safety Augmented Reinforcement Learning: Staying Safe in the Face of Uncertainty](https://arxiv.org/abs/2604.25508)

**<font color=#1a73e8>作者：</font>** Artur Eisele, Bernd Frauenknecht, Friedrich Solowjow 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety remains an open problem in reinforcement learning (RL), especially during training. While safety filters are promising to address safe exploration, they are generally poorly suited for high-dimensional systems with unknown dynamics. We propose Dyna-style Safety Augmented Reinforcement Learning (Dyna-SAuR), a novel algorithm that learns both a scalable safety filter and a control policy using a learned uncertainty-aware dynamics model, while requiring minimal domain knowledge. The filter avoids failures and high uncertainty regions. Thus, better models expand the set of safe and certain states, reducing filter conservatism. We present the effectiveness of Dyna-SAuR on goal-reaching CartPole as well as MuJoCo Walker, reducing failures compared to state-of-the-art methods by 2 orders of magnitude.

---


### 134. [PHISHREV: A Hybrid Machine Learning and Post-Hoc Non-monotonic Reasoning Framework for Context-Aware Phishing Website Classification](https://arxiv.org/abs/2604.25512)

**<font color=#1a73e8>作者：</font>** Mainak Sen, Kumar Sankar Ray, Amlan Chakrabarti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Phishing detection systems are predominantly rely on statistical machine learning models, which often lack contextual reasoning and are vulnerable to adversarial manipulation. In this work, we propose a hybrid framework that integrates machine learning classifiers with non-monotonic reasoning using Answer Set Programming (ASP) to enable context-aware decision refinement. The proposed post-hoc reasoning layer incorporates expert knowledge to revise classifier predictions through formal belief revisions. Experimental results indicate that the reasoning module modifies 5.08\% of classifier outputs, leading to improved decision consistency. A key advantage is that new domain knowledge can be incorporated into the reasoning layer in $\mathcal{O}(n)$ time, eliminating the need for model retraining.

---


### 135. [Automated Adversarial Collaboration for Advancing Theory Building in the Cognitive Sciences](https://arxiv.org/abs/2604.25521)

**<font color=#1a73e8>作者：</font>** Suyog Chandramouli, George Kachergis, Akshay Jagadish  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cognitive science often evaluates theories through narrow paradigms and local model comparisons, limiting the integration of evidence across tasks and realizations. We introduce an automated adversarial collaboration framework for adjudicating among competing theories even when the candidate models and experiments must be discovered during the adjudication process. The system combines LLM-based theory agents, program synthesis, and information-theoretic experimental design in a closed loop. In a simulation study spanning three classic categorization theories, the framework recovered the ground-truth theory across noise settings with weaker reliability in the hardest settings. Together, the framework and findings provide a concrete proof of concept for closed-loop, in-silico theory adjudication in cognitive science.

---


### 136. [The Surprising Effectiveness of Canonical Knowledge Distillation for Semantic Segmentation](https://arxiv.org/abs/2604.25530)

**<font color=#1a73e8>作者：</font>** Muhammad Ali, Kevin Alexander Laube, Madan Ravi Ganesh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent knowledge distillation (KD) methods for semantic segmentation introduce increasingly complex hand-crafted objectives, yet are typically evaluated under fixed iteration schedules. These objectives substantially increase per-iteration cost, meaning equal iteration counts do not correspond to equal training budgets. It is therefore unclear whether reported gains reflect stronger distillation signals or simply greater compute. We show that iteration-based comparisons are misleading: when wall-clock compute is matched, \textit{canonical} logit- and feature-based KD outperform recent segmentation-specific methods. Under extended training, feature-based distillation achieves state-of-the-art ResNet-18 performance on Cityscapes and ADE20K. A PSPNet ResNet-18 student closely approaches its ResNet-101 teacher despite using only one quarter of the parameters, reaching 99\% of the teacher's mIoU on Cityscapes (79.0 vs.\ 79.8) and 92\% on ADE20K. Our results challenge the prevailing assumption that KD for segmentation requires task-specific mechanisms and suggest that scaling, rather than complex hand-crafted objectives, should guide future method design.

---


### 137. [DualGeo: A Dual-View Framework for Worldwide Image Geo-localization](https://arxiv.org/abs/2604.25533)

**<font color=#1a73e8>作者：</font>** Junchao Cui, Wenqi Shi, Shaoyong Du 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Worldwide image geo-localization aims to infer the geographic location of an image captured anywhere on Earth, spanning street, city, regional, national, and continental scales. Existing methods rely on visual features that are sensitive to environmental variations (e.g., lighting, season, and weather) and lack effective post-processing to filter outlier candidates, limiting localization accuracy. To address these limitations, we propose DualGeo, a two-stage framework for worldwide image geo-localization. First, it establishes a geo-representational foundation by fusing image and semantic segmentation features via bidirectional cross-attention. The fused features are then aligned with GPS coordinates through dual-view contrastive learning to build a global retrieval database. Second, it performs geo-cognitive refinement by re-ranking retrieved candidates using geographic clustering. It then feeds them into large multimodal models (LMMs) for final coordinate prediction. Experiments on IM2GPS, IM2GPS3k, and YFCC4k show that DualGeo outperforms state-of-the-art methods, improving street-level (<1 km) and city-level (<25 km) localization accuracy by 3.6%-16.58% and 1.29%-8.77%, respectively. Our code and datasets are available : this https URL.

---


### 138. [Sample-efficient Neuro-symbolic Proximal Policy Optimization](https://arxiv.org/abs/2604.25534)

**<font color=#1a73e8>作者：</font>** Simone Murari, Celeste Veronese, Daniele Meli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep Reinforcement Learning (DRL) algorithms often require a large amount of data and struggle in sparse-reward domains with long planning horizons and multiple sub-goals. In this paper, we propose a neuro-symbolic extension of Proximal Policy Optimization (PPO) that transfers partial logical policy specifications learned in easier instances to guide learning in more challenging settings. We introduce two integrations of symbolic guidance: (i) H-PPO-Product, which biases the action distribution at sampling time, and (ii) H-PPO-SymLoss, which augments the PPO loss with a symbolic regularization term. We evaluate our methods on three benchmarks (OfficeWorld, WaterWorld, and DoorKey), showing consistently faster learning and higher return at convergence than PPO and a Reward Machine baseline, also under imperfect symbolic knowledge.

---


### 139. [TopoMamba: Topology-Aware Scanning and Fusion for Segmenting Heterogeneous Medical Visual Media](https://arxiv.org/abs/2604.25545)

**<font color=#1a73e8>作者：</font>** Fuchen Zheng, Chengpei Xu, Long Ma 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual state-space models (SSMs) have shown strong potential for medical image segmentation, yet their effectiveness is often limited by two practical issues: axis-biased scan ordering weakens the modeling of oblique and curved structures, and naive multi-branch fusion tends to amplify redundant responses. We present TopoMamba, a topology-aware scan-and-fuse framework for segmenting heterogeneous medical visual media. The method combines a diagonal/anti-diagonal TopoA-Scan branch with the standard Cross-Scan branch to provide complementary structural priors, and introduces ScanCache, a device-aware caching mechanism that amortizes explicit scan-index construction across recurring resolutions. To fuse heterogeneous scan features efficiently, we further propose a lightweight HSIC Gate that regulates branch interaction using a dependence-aware scalar gating rule. We also instantiate a volumetric TopoMamba-3D for practical 3D clinical segmentation. Experiments on Synapse CT, ISIC 2017 dermoscopy, and CVC-ClinicDB endoscopy show that TopoMamba consistently improves segmentation quality over strong CNN, Transformer, and SSM baselines, with particularly clear gains on thin or curved targets such as the pancreas and gallbladder, while maintaining favorable deployment efficiency under dynamic input resolutions. These results suggest that topology-aware scan ordering and lightweight dependence-aware fusion form an effective and practical design for medical multimedia segmentation. The code will be made publicly available.

---


### 140. [Enhancing SignSGD: Small-Batch Convergence Analysis and a Hybrid Switching Strategy](https://arxiv.org/abs/2604.25550)

**<font color=#1a73e8>作者：</font>** Haoran Chen, Wentao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> SignSGD compresses each stochastic gradient coordinate to a single bit, offering substantial memory and communication savings, but its 1-bit quantization removes magnitude information and is known to leave a generalization gap relative to well-tuned SGD. We revisit SignSGD from a 1-bit quantization and dithering perspective and contribute three improvements. First, we derive a small-batch convergence rate for SignSGD under unimodal symmetric gradient noise using a signal-to-noise weighted stationarity measure, removing the large-batch assumption of prior analyses. Second, we inject annealed Gaussian noise before the sign operator, which acts as a classical dithering mechanism and probabilistically restores magnitude information lost to hard thresholding. Third, we adapt the SWATS strategy to sign-based updates with a projection-based learning-rate calibration that smoothly transitions from SignSGD to SGD. Single-worker experiments on ResNet-18 isolate optimizer effects from communication aspects: pre-sign dithering surpasses Adam on CIFAR-100, and the calibrated switch reaches 92.18% test accuracy on CIFAR-10, outperforming both pure SGD 91.38% and pure SignSGD with momentum 90.82%.

---


### 141. [On Halting vs Converging in Recurrent Graph Neural Networks](https://arxiv.org/abs/2604.25551)

**<font color=#1a73e8>作者：</font>** Jeroen Bollen, Stijn Vansummeren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent Graph Neural Networks (RGNNs) extend standard GNNs by iterating message-passing until some stopping condition is met. Various RGNN models have been proposed in the literature. In this paper, we study three such models: converging RGNNs, where all vertex representations must stabilise; output-converging RGNNs, where only the output classifications must stabilise; and halting RGNNs, where a per-vertex halting classifier determines when to stop. We establish expressiveness relationships between these models: over undirected graphs, converging RGNNs are equally expressive as graded-bisimulation-invariant halting RGNNs, while output-converging RGNNs are at least as expressive. Combined with prior results on halting RGNNs, this shows that, relative to the classifiers expressible in monadic second-order logic (MSO), converging RGNNs express exactly the graded modal $\mu$-calculus ($\mu$GML), and output-converging RGNNs express at least $\mu$GML. These results hold even when restricting to ReLU networks with sum aggregation. The main technical challenge is simulating halting RGNNs by converging ones: without a global halting classifier, vertices may locally decide to halt at different times, causing desynchronisation. We develop a "traffic-light" protocol that enables vertices to coordinate despite this asynchrony. Our results answer an open question from Bollen et al. (2025) and show that the RGNN model of Pflueger et al. (2024) retains full $\mu$GML expressiveness even when convergence is guaranteed.

---


### 142. [Should I Replan? Learning to Spot the Right Time in Robust MAPF Execution](https://arxiv.org/abs/2604.25567)

**<font color=#1a73e8>作者：</font>** David Zahrádka, David Woller, Denisa Mužíková 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> During the execution of Multi-Agent Path Finding (MAPF) plans in real-life applications, the MAPF assumption that the fleet's movement is perfectly synchronized does not apply. Since one or more of the agents may become delayed due to internal or external factors, it is often necessary to use a robust execution method to avoid collisions caused by desynchronization. Robust execution methods - such as the Action Dependency Graph (ADG) - synchronize the execution of risky actions, but often at the expense of increased plan execution cost, because it may require some agents to wait for the delayed agents. In such cases, the execution's cost can be reduced while still preserving safety by finding a new plan either by rescheduling (reordering the agents at crossroads) or the more general replanning capable of finding new paths. However, these operations may be costly, and the new plan may not even lead to lower execution cost than the original plan: for example, the two plans may be the exact same. Therefore, we estimate the benefit that can be achieved by single replanning in scenarios with delayed agents given an immediate state of the execution with a fully connected feed-forward neural network. The input to the neural network is a set of newly designed ADG-based features describing the robust execution's state and the impact of potential delays, and the output is an estimated benefit achievable by replanning. We train and test the network on a new labeled dataset containing 12,000 experiments, and we show that our proposed method is capable of reducing the impact of delays by up to 94.6% of the achievable reduction.

---


### 143. [Vision SmolMamba: Spike-Guided Token Pruning for Energy-Efficient Spiking State-Space Vision Models](https://arxiv.org/abs/2604.25570)

**<font color=#1a73e8>作者：</font>** Dewei Bai, Hongxiang Peng, Yunyun Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spiking Transformers have shown strong potential for long-range visual modeling through spike-driven self-attention. However, their quadratic token interactions remain fundamentally misaligned with the sparse and event-driven nature of spiking neural computation. To address this limitation, we propose Vision SmolMamba, an energy-efficient spiking state-space architecture that integrates spike-driven dynamics with linear-time selective recurrence. The key idea is a Spike-Guided Spatio-Temporal Token Pruner (SST-TP), which estimates token importance using both spike activation strength and first-spike latency. This mechanism progressively removes redundant tokens while preserving salient spatio-temporal information, enabling efficient scaling with token sparsity. Based on this mechanism, the proposed SmolMamba block incorporates spike events directly into bidirectional state-space recurrence, forming a spiking state-space vision backbone for efficient long-range modeling. Extensive experiments on both static and event-based benchmarks, including ImageNet-1K, CIFAR10/100, CIFAR10-DVS, and DVS128 Gesture, demonstrate that Vision SmolMamba consistently achieves superior accuracy-efficiency trade-offs. In particular, it reduces the estimated energy cost by at least 1.5x compared with prior spiking Transformer baselines and a Spiking Mamba variant while maintaining competitive or improved accuracy. These results demonstrate that combining spike-guided token sparsity with state-space modeling offers a scalable and energy-efficient paradigm for spiking vision systems.

---


### 144. [Control Your Queries: Heterogeneous Query Interaction for Camera-Radar Fusion](https://arxiv.org/abs/2604.25574)

**<font color=#1a73e8>作者：</font>** Jialong Wu, Yihan Wang, Matthias Rottmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In autonomous driving, camera-radar fusion offers complementary sensing and low deployment cost. Existing methods perform fusion through input mixing, feature map mixing, or query-based feature sampling. We propose a new fusion paradigm, termed heterogeneous query interaction, and present ConFusion, a camera-radar 3D object detector. ConFusion combines image queries, radar queries, and learnable world queries distributed in 3D space to improve query initialization and object coverage. To encourage cross-type interaction among heterogeneous queries, we introduce heterogeneous query mixing (QMix), which performs dedicated cross-type attention after feature sampling to consolidate complementary object evidence. We further propose interactive query swap sampling (QSwap), which improves feature sampling by allowing related queries to exchange informative feature tokens under attention and geometric constraints. Experiments on the nuScenes dataset show that ConFusion achieves state-of-the-art performance, reaching 59.1 mAP and 65.6 NDS on the validation set, and 61.6 mAP and 67.9 NDS on the test set.

---


### 145. [OxyGent: Making Multi-Agent Systems Modular, Observable, and Evolvable via Oxy Abstraction](https://arxiv.org/abs/2604.25602)

**<font color=#1a73e8>作者：</font>** Junxing Hu, Tianlong Li, Lei Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying production-ready multi-agent systems (MAS) in complex industrial environments remains challenging due to limitations in scalability, observability, and autonomous evolution. We present OxyGent, an open-source framework that enables modular, observable, and evolvable MAS via a unified Oxy abstraction, in which agents, tools, LLMs, and reasoning flows are encapsulated as pluggable atomic components. This Lego-like assembly paradigm supports scalable system composition and non-intrusive monitoring. To enhance observability, OxyGent introduces permission-driven dynamic planning that replaces rigid workflows with execution graphs generated at runtime, which provide adaptive visualizations. To support continuous evolution, the framework integrates OxyBank, an AI asset management platform that supports automated data backflow, annotation, and joint evolution. Empirical evaluations and real-world case studies show that OxyGent provides a robust and scalable foundation for MAS. OxyGent is publicly available at this https URL.

---


### 146. [WhisperPipe: A Resource-Efficient Streaming Architecture for Real-Time Automatic Speech Recognition](https://arxiv.org/abs/2604.25611)

**<font color=#1a73e8>作者：</font>** Erfan Ramezani, Mohammad Mahdi Giahi, Mohammad Erfan Zarabadipour 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-time automatic speech recognition (ASR) systems face a fundamental trade-off between transcription accuracy and computational efficiency, particularly when deploying large-scale transformer models like Whisper. Existing streaming approaches either sacrifice accuracy through aggressive chunking or incur prohibitive memory costs through unbounded context accumulation. We present WhisperPipe, a novel streaming architecture that achieves bounded memory consumption while maintaining transcription quality through three key innovations a hybrid Voice Activity Detection (VAD) pipeline combining Silero VAD with energy-based filtering to reduce false activations by 34%, a dynamic buffering mechanism with overlapping context windows that prevents information loss at segment boundaries, and an adaptive processing strategy that balances latency and accuracy based on speech characteristics. Evaluated on 2.5 hours of diverse audio data, WhisperPipe demonstrates a median end-to-end latency of 89ms (90th percentile: 142ms) while consuming 48% less peak GPU memory and 80.9% lower average GPU utilization compared to baseline Whisper implementations. The system maintains stable memory usage over extended sessions, with zero growth rate across 150-minute continuous operation. Comparative analysis against related work shows that WhisperPipe achieves competitive accuracy (WER within 2% of offline Whisper) while operating at 3-5x lower latency than existing streaming solutions. The architecture's modular design enables deployment across resource-constrained environments, from edge devices to cloud infrastructure. Our results demonstrate that careful architectural design can reconcile the competing demands of real-time responsiveness and model sophistication in production ASR systems.

---


### 147. [The Nonverbal Syntax Framework: An Evidence-Based Tiered System for Inferring Learner States from Observable Behavioral Cues](https://arxiv.org/abs/2604.25612)

**<font color=#1a73e8>作者：</font>** Sherzod Turaev, Mary John, Jaloliddin Rustamov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding learners' cognitive and affective states underpins adaptive educational systems and effective teaching. Although research links nonverbal cues to internal states, no framework calibrates them to evidence. We present the Nonverbal Syntax Framework, drawn from a systematic review of 908 studies and 17,043 cue-state mappings (Turaev et al., 2026). The framework addresses three challenges: terminological fragmentation (behaviors described inconsistently), evidence heterogeneity (single observations to replicated findings), and state ambiguity (similar patterns indicating multiple states). Normalization consolidated 5,537 state labels into 2,010 canonical states (63.7%) and 11,521 cues into 6,434 normalized cues (44.2%) across nine behavioral channels. Dual-evidence assessment separately evaluates Component Evidence (coverage of cues and states) and Relationship Evidence (independent studies per cue-state link). 52% of "Very High" relationships rest on one paper, so separation enables calibrated rather than overconfident inference from preliminary findings. The framework's four levels comprise a Cue Vocabulary of 6,434 indicators classified as observable/instrumental; State Clusters linking 2,010 states to indicative cues; State Profiles with multimodal behavioral signatures and actionable specifications; and Discriminative Analysis distinguishing 1,215 confusable state pairs. We identify 480 actionable R1-R4 relationships (three or more independent papers), the replicated core of six decades of research, covering 35.5% of mappings across 47 key learning states and 111 distinct indicators. The remaining 91.5% (9,653 single-paper findings) form exploratory hypotheses for replication. The framework gives researchers an empirical foundation for identifying gaps, practitioners evidence-based tools for state inference, and technologists validated features for multimodal detection.

---


### 148. [HotComment: A Benchmark for Evaluating Popularity of Online Comments](https://arxiv.org/abs/2604.25614)

**<font color=#1a73e8>作者：</font>** Yafeng Wu, Yunyao Zhang, Liliang Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online comments play a crucial role in shaping public sentiment and opinion dynamics on social media. However, evaluating their popularity remains challenging, not only because it depends on linguistic quality, originality, and emotional resonance, but also because stylistic preferences vary widely across platforms and user groups, causing the same comment to resonate differently in different communities. In this work, we present HotComment, a multimodal benchmark integrating video and text modalities that comprehensively quantifies popularity from three enhanced aspects: (1) Content Quality, which evaluates semantic similarity with ground-truth human comments and extends quality assessment through four interpretable dimensions; (2) Popularity Prediction, based on trends from models trained on real-world interaction data; and (3) User Behavior Simulation, which models the distribution of platform users and approximates \textbf{engagement scores} through an agent-based framework. Furthermore, we propose StyleCmt, inspired by social ripple effects, where multiple stylistic dimensions align to amplify socially resonant expressions and suppress incongruent ones.

---


### 149. [SAMe: A Semantic Anatomy Mapping Engine for Robotic Ultrasound](https://arxiv.org/abs/2604.25646)

**<font color=#1a73e8>作者：</font>** Jing Zhang, Duojie Chen, Wentao Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic ultrasound has advanced local image-driven control, contact regulation, and view optimization, yet current systems lack the anatomical understanding needed to determine what to scan, where to begin, and how to adapt to individual patient anatomy. These gaps make systems still reliant on expert intervention to initiate scanning. Here we present SAMe, a semantic anatomy mapping engine that provides robotic ultrasound with an explicit anatomical prior layer. SAMe addresses scan initiation as a target-to-anatomy-to-action process: it grounds under-specified clinical complaints into structured target organs, instantiates a patient-specific anatomical representation for the grounded targets from a single external body image, and translates this representation into control-facing 6-DoF probe initialization states without any additional registration using preoperative CT or MRI. The anatomical representation maintained by SAMe is explicit, lightweight (single-organ inference in 0.08s), and compatible with downstream control by design. Across semantic grounding, anatomical instantiation, and real-robot evaluation, SAMe shows strong performance across the full initialization pipeline. In real-robot experiments, SAMe achieved overall organ-hit rates of 97.3% for liver initialization and 81.7% for kidney initialization across the evaluated target sets. Even when restricted to the centroid target, SAMe outperformed the surface-heuristic baseline for both liver and kidney initialization. These results establish an explicit anatomical prior layer that addresses scan initialization and is designed to support broader downstream autonomous scanning pipelines, providing the anatomical foundation for complaint-driven, anatomically informed robotic ultrasonography.

---


### 150. [Towards interpretable AI with quantum annealing feature selection](https://arxiv.org/abs/2604.25649)

**<font color=#1a73e8>作者：</font>** Francesco Aldo Venturelli, Emanuele Costa, Sikha O K 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models are used in critical applications, in which mistakes can have serious consequences. Therefore, it is crucial to understand how and why models generate predictions. This understanding provides useful information to check whether the model is learning the right patterns, detect biases in the data, improve model design, and build systems that can be trusted. This work proposes a new method for interpreting Convolutional Neural Networks in image classification tasks. The approach works by selecting the most important feature maps that contribute to each prediction. To solve this combinatorial problem, we encode it into a quantum constrained optimization problem and propose to solve it using quantum annealing. We evaluate our method against the state-of-the-art explainable AI techniques, specifically GradCAM and GradCAM++, and observe an improved class disentanglement, i.e. the model's decision boundaries become more distinct and its reasoning more transparent. This demonstrates that our approach enhances the quality of explanations, making it easier to understand which features the model relies on for specific predictions. In addition, we study the computational behavior of the quantum annealing algorithm. Specifically, we analyze the minimum energy gap of the system during computation and the probability that the algorithm finds the correct solution. These analyses provide theoretical insight into why the method works effectively in practice.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-190](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

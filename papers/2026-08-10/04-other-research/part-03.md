# 📦 其他研究 | 2026年08月10日

> 本类共 **221** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-221](./part-05.md)

---

### 101. [SkillEval: Decomposing Agent Skill Quality into Interpretable Signals](https://arxiv.org/abs/2608.06891)

**<font color=#1a73e8>作者：</font>** Jiahui Han, Qinuo Li, Ziheng Peng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills provide reusable procedural knowledge that helps agents solve specialized tasks. As their use expands, evaluating skill quality becomes increasingly important. Existing evaluations often measure skill quality by testing whether a skill improves performance on specific downstream tasks. However, a reusable skill may apply to multiple task scenarios. Downstream evaluation mainly reflects the compatibility between a skill and the evaluated task, provides only a partial view of skill quality, and does not identify which aspect of the skill should be improved. We find that general properties of the \texttt{this http URL} document play an important role in skill quality. To evaluate these properties, we propose \textbf{SkillEval}, an interpretable framework for document-level skill evaluation. SkillEval evaluates each property using a fixed and inspectable scoring direction, producing interpretable scores. It further measures and reduces the influence of unrelated document features, such as length and formatting, so that each score captures its intended semantic property more specifically. Specifically, SkillEval learns an interpretable direction for each quality property from controlled positive--negative skill pairs in the hidden representation space of the model, and scores a new skill by projecting its representation onto these fixed directions. We use SkillEval to evaluate skills in controlled quality tests and show that SkillEval reliably distinguishes skills of different quality. In addition, SkillEval scores closely reflect downstream task performance, providing an early indication of whether a skill is likely to help an agent complete a task. We further explore SkillEval for diagnosing weaknesses in skill documents and guiding targeted revisions. The revised skills improve the targeted properties and achieve higher pass rates on downstream tasks.

---


### 102. [PRISM: Principled Reference Identification for Schrodinger Bridge Model](https://arxiv.org/abs/2608.06893)

**<font color=#1a73e8>作者：</font>** Forouzan Fallah, Yezhou Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Schrödinger bridge models restore a clean signal from a degraded observation by following the conditional bridges of a reference process, yet this reference is chosen heuristically, typically white noise with a hand-tuned schedule. We develop PRISM, a theory of bridge reference design. We characterize the time-varying Gaussian references that remain exactly tractable with per-mode schedules: precisely those whose instantaneous covariances commute. We then prove an invisibility principle: with the exact drift and unlimited solver steps, every admissible reference recovers the true posterior. The choice of reference therefore matters only under finite computational resources. For a fixed step budget, we derive the finite-step objective in closed form and prove that every optimal noise spectrum is proportional to Pk, the spectrum of information destroyed by the sensor, with a mode-independent constant x*(T) = (2 ln T)^-1/2 (1 + o(1)). The analysis shows that noise color and temporal scheduling are interchangeable, and regularization provably shifts the optimal reference toward white noise. Experiments in Gaussian settings confirm the predicted orderings and the closed-form loss floors. On FFHQ, the distortion-- perception trade-off and spectral localization transfer, but white noise outperforms the matched reference; a pre-registered study that changes the training regime refutes ridge whitening as the explanation. A 2x2 mechanism study then traces the inversion to the non-Gaussian per-mode statistics of real images. PRISM turns reference design from a hyperparameter sweep into a calculation in the Gaussian regime, and locates exactly where real images break it.

---


### 103. [From Points to Edges: Edge-Conditioned Spectral Operators for Physics-Sensitive PDE Learning](https://arxiv.org/abs/2608.06894)

**<font color=#1a73e8>作者：</font>** Zhentao Tan, Ruijie Quan, Yi Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural operators have become a central tool for solving partial differential equations (PDEs), with spectral operators offering efficient global mixing across spatial locations. However, many PDEs contain physics-sensitive local structures that are critical to the underlying physical behavior. For example, in Darcy flow, local material interfaces are often reflected by sharp changes in the permeability field and can strongly influence the solution. Existing spectral operators primarily adapt modal mixing based on center-point representations, making them insufficiently responsive to such localized structural variations. We propose the Edge-Conditioned Spectral Operator (ESO), a novel spectral operator framework that modulates global spectral mixing using local edge-wise variations. By incorporating the Pairwise-Variation Modal Mixer (PVMM) to inject local edge information into spectral mode selection, ESO preserves the global approximation capability of spectral neural operators while enabling the learned kernel to adapt to physics-sensitive local structures. Furthermore, we introduce a task-adaptive Physics-Aware Reweighting (PAR) that emphasizes physically important regions, identified by taskspecific physical quantities. Across nine PDE benchmarks, ESO consistently achieves state-of-the-art performance. Visual and region-wise analyses further demonstrate that ESO reduces solution errors near coefficient jumps, high-gradient flow structures, and other physically sensitive regions. The code is available at this https URL.

---


### 104. [Recent advances in weakly supervised learning: New supervision paradigms, assumption relaxations, and practical solutions](https://arxiv.org/abs/2608.06896)

**<font color=#1a73e8>作者：</font>** Wei Wang, Gang Niu, Masashi Sugiyama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has achieved great success in recent years thanks to the availability of high-quality, well-annotated training data. However, this requirement is often not met in real-world applications. Weakly supervised learning aims to train an accurate model with incomplete, inexact, or inaccurate supervision. In this chapter, we will discuss recent advances in this field, including new supervision paradigms, relaxed assumptions, and practical solutions. First, we introduce a new weakly supervised binary classification problem called confidence-difference classification and propose consistent approaches to solve it. Next, we investigate complementary-label learning, a weakly supervised multi-class classification problem. Our proposed approaches are based on more relaxed assumptions about the data generation process than existing consistent approaches. Lastly, we present an evaluation framework for partial-label learning, another popular multi-class weakly supervised learning problem, in order to promote fair and realistic evaluation of algorithms in this field.

---


### 105. [The Nocturnity Scale: Measuring the Sense of Being at Night in Virtual Urban Environments](https://arxiv.org/abs/2608.06904)

**<font color=#1a73e8>作者：</font>** Anthony Le Gourri{é}rec, Etienne Peillard, Nicolas Houel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Nighttime environments are increasingly used in virtual urban studies, yet darkness alone does not fully recreate the subjective sense of being at night. Prior work suggests that this experience depends not only on the absence of daylight, but also on lighting structure, low-light perception, human activity, soundscape, and self-related states. However, no existing tool directly assesses this scene-dependent subjective experience. This work introduces nocturnity as the feeling of being at night elicited by a scene and proposes a theory-driven framework structured into three subscales: perceptual, activity, and inner-state nocturnity. Based on this framework, we develop a first candidate questionnaire for virtual urban environments. Developed through a literature-informed process and reviewed by two urban lighting experts, the scale comprises 42 Likert-type items, including three diagnostic subscales and complementary global and time-related items. This work provides a first operational basis for comparing virtual urban scenes according to their perceived nocturnity and supports future empirical validation.

---


### 106. [Calibrating WEAT Against Anisotropy: ZCA Whitening as a Geometric Pre-Processing Step for Embedding Association Tests](https://arxiv.org/abs/2608.06908)

**<font color=#1a73e8>作者：</font>** Seitaro Ono, Senna Ross, Jun Saiki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose Zero-phase Component Analysis (ZCA) whitening as a geometric pre-processing step for the Word Embedding Association Test (WEAT). WEAT is a bias measurement method widely used in both computational social science and AI fairness research. It relies on cosine similarity as a measure of semantic association, which assumes that the embedding space is approximately isotropic. However, prior work has reported that many widely used language models do not satisfy this assumption, raising concerns about the reliability of bias measurements. ZCA whitening transforms the covariance of the embedding space into the identity matrix while minimizing perturbation to the original vectors. This transformation restores the isotropy condition on which WEAT relies. We evaluate our approach on ten standard WEAT test suites and seven models spanning three architectural families, yielding 70 model-task combinations. The results show that ZCA whitening substantially reduces the anisotropy of the embedding spaces across all models. Particularly for highly anisotropic models, we further observe improvements on standard semantic similarity benchmarks, indicating that the calibrated space better captures semantic associations. After calibration, over 30% of WEAT results change significance status, and effect sizes shift in both directions depending on bias category. These shifts suggest that uncalibrated measurements may both overestimate and underestimate the associations encoded in the embedding space. These findings indicate that previously reported bias measurements in anisotropic embedding spaces should be interpreted with caution and may benefit from re-evaluation with calibrated methods. Our approach contributes to restoring the measurement foundation of WEAT across both computational social science and AI fairness research.

---


### 107. [Fast LapSum: Exact Differentiable Top-k at Million Scale](https://arxiv.org/abs/2608.06912)

**<font color=#1a73e8>作者：</font>** Łukasz Struski, Joanna Wojciechowicz, Jakub Antczak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The top-$k$ operation is a fundamental building block of modern sparse computation, enabling token routing, expert activation, memory selection, and attention pruning. Yet standard hard top-$k$ blocks gradients, while existing continuous (soft) relaxations remain too costly for large-scale models. We introduce Fast LapSum, an exact-budget soft top-$k$ primitive whose GPU solver runs in linear time after sorting. Unlike prior linear-time methods such as DFTopK, which relax the normalization constraint, Fast LapSum is, to our knowledge, the first method to preserve an exact selection mass of $k$ while remaining fully differentiable end-to-end. Our solver combines a linear-time threshold computation with an analytical vector--Jacobian product, and for extreme scales employs probabilistic bracketing to sort only the uncertain middle band of kernel-noised scores. The resulting overhead is almost negligible: the solver processes $10^6$, $10^7$, and $10^8$ scores in $0.41$, $1.15$, and $5.23$\,ms, respectively. This makes exact soft top-$k$ practical for sparse routing, retrieval, and large-scale optimization. We demonstrate Fast LapSum on two demanding applications operating over millions of coordinates inside the training loop: generating megapixel sparse adversarial examples with an exact soft budget of ${\sim}0.02\%$ of an image's pixels, achieving an order-of-magnitude speedup over state-of-the-art methods, and training a fully differentiable sparse image coder from scratch.

---


### 108. [RibAssist 3D: Biplanar Rib-Fracture Detection, Addressing, and Selective 3D Localization from CT-Derived Projections](https://arxiv.org/abs/2608.06914)

**<font color=#1a73e8>作者：</font>** Kabila Haile Soboka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rib fractures are common, clinically significant, and time-consuming to localize on computed tomography (CT). We ask whether fractures detected in two orthogonal projections (anteroposterior, AP, and lateral) can be paired across views and triangulated into reliable 3D fracture points at a controlled rate of false 3D outputs. We answer this with a staged diagnostic study. Biplanar geometry is exact: detector-predicted centers reconstruct to median 4.0 mm 3D error when correspondence is correct. On the sealed cohort, dual-view availability reaches 61.1% and the candidate graph contains a correct pair for 58.4% of fractures. The binding limitation is not geometry or localization but confidence-limited cross-view correspondence. Lateral-detector retraining lifts dual-view availability (0.52 to 0.76 in development) and moves the frontier from 0% to 2.44% recall at 10 mm. When the policy commits a correct pair, the emitted point is geometrically accurate (sealed median 1.49 mm, rib-exact 93%). A pre-specified pass on the untouched 55-case cohort promotes 15 of 601 fractures to correct 3D localizations at 0.436 false 3D points per case, yielding 2.50% end-to-end commitment yield. The contribution is validated biplanar reconstruction geometry with high conditional localization fidelity, a staged identification of cross-view correspondence confidence as the effective bottleneck, and a selective assistive workflow that preserves uncertain findings rather than a standalone automatic reconstructor.

---


### 109. [MiCoPro: End-to-End Mixed Precision HW/SW Co-design with HW-aware Proxy Model](https://arxiv.org/abs/2608.06916)

**<font color=#1a73e8>作者：</font>** Zijun Jiang, Yangdi Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantized Neural Networks~(QNN) with low-bitwidth data have proven promising in efficient storage and computation on edge devices. To mitigate accuracy degradation while maximizing speedup, layer-wise mixed-precision quantization~(MPQ) becomes a popular solution. However, existing algorithms for exploring MPQ schemes are limited in flexibility and efficiency. Comprehending the complex impacts of different MPQ schemes on post-training quantization and quantization-aware training results is a challenge for conventional methods. Furthermore, an end-to-end framework for the optimization and deployment of MPQ models is missing in existing work.
To address these challenges, we propose the MiCo framework, a holistic MPQ exploration and deployment framework for edge AI applications. The framework adopts a novel optimization algorithm to search for accuracy-optimal quantization configurations under strict latency constraints. We further extended the framework to MiCoPro, which introduces a robust Hardware-Aware Proxy (HAP) model to enhance prediction accuracy and hardware versatility. By leveraging target-specific latency modeling, MiCoPro enables rapid exploration and direct deployment from PyTorch models to bare-metal C code. We demonstrate the versatility of our framework on both the BitFusion accelerator and SIMD-extended RISC-V processors, achieving up to 40\% of latency reduction with less than 3\% of accuracy drop.

---


### 110. [ReGraph: Learning to Generate Recipe Graphs from Food Images](https://arxiv.org/abs/2608.06917)

**<font color=#1a73e8>作者：</font>** Guoshan Liu, Bin Zhu, Pengkun Jiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent Large Multimodal Models (LMMs) have achieved impressive performance in recipe generation from food this http URL, cooking is a structured transformation process in which ingredients undergo state changes through ordered actions,while free-form recipe language leaves the corresponding entities, intermediate states, and dependencies largely implicit and entangled.A graph representation makes this procedural knowledge explicit and compositional, providing a structured basis for assessing whether model outputs encode process-level knowledge rather than merely presenting plausible textual descriptions. To address this limitation, we present ReGraph, a large-scale recipe graph dataset that represents ingredients, cooking actions, and tools as entities, uses entity attributes to describe ingredient state changes, and employs typed relations to encode manipulation targets, destinations, and procedural ordering. ReGraph further incorporates explicit Recipe Reasoning Chain-of-Thought (RR-CoT) traces, providing auxiliary supervision for procedural decomposition and structured graph generation. Building on ReGraph, we propose Recipe Graph Learning (RGL), a two-stage framework that enables LMMs to generate a plausible fine-grained cooking workflow from a food image in the form of a structured recipe graph. Under a deterministic, schema-aware matching protocol, our experiments reveal a substantial gap between text-generation quality and recoverable procedural structure: recipes produced by existing approaches achieve competitive text-generation scores yet yield limited reference-aligned entity and relation structure under the ReGraph schema. In contrast, across two representative LMM backbones, RGL consistently improves the generation of cooking entities and procedural relations, while our analysis further shows that fine-grained ingredient-state capture remains the most challenging dimension.

---


### 111. [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919)

**<font color=#1a73e8>作者：</font>** Oliver Lemke, Alexander Liniger, Abel Gawel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR serves as a primary sensing modality for robots operating in outdoor environments. However, the performance of deep learning models in this domain is severely limited by the scarcity of labeled data, a direct result of the high cost of 3D annotation. Self-supervised learning addresses this scarcity by learning general-purpose features from unlabeled data. In this work, we present a multi-modal, multi-teacher distillation framework for self-supervised learning on outdoor LiDAR point clouds. Building upon the Sonata architecture, we introduce Vernata, consisting of three extensions: sparse view augmentation to improve robustness against varying point densities, a memory bank mechanism to stabilize resource-constrained training, and cross-modal distillation utilizing dense, high-resolution 2D image features to enable fine-grained semantic guidance. We evaluate our method on the GrandTour, TartanGround, and Waymo datasets, as well as data collected from our own robotic platforms. Our experiments demonstrate a significant performance improvement over Sonata baselines, yielding mIoU scores of 54.7 on TartanGround (+5.9 points, +12.1%) and 57.1 on Waymo (+7.3 points, +14.7%). Finally, we show that the self-supervised approach maintains strong performance even in reduced-modality settings (lacking color or normals), achieving competitive mIoU scores of 49.4 and 50.2 on the respective datasets.

---


### 112. [Deal Me Maybe: The Role of Emotions in Multi-Agent Negotiation](https://arxiv.org/abs/2608.06922)

**<font color=#1a73e8>作者：</font>** Massimiliano Luca, Apoorva Singh, Bruno Lepri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Negotiation is a demanding social task for LLM agents, requiring strategic reasoning, persuasion, and interpersonal adaptation. Yet existing benchmarks often treat agents as emotionally neutral, overlooking a key driver of human bargaining behavior. We study how prompt-conditioned emotions affect LLM-based price negotiation. In a controlled framework, buyer and seller agents are independently assigned one of six emotional states and negotiate over 350 real consumer products under two budget conditions. Across 36 emotion-pair settings and five widely used LLMs, we find that emotions strongly shape outcomes. Angry buyers almost never reach agreement (0.39% deal rate), while happy buyers agree most often (28.91%), but obtain worse prices than fearful buyers. Emotion effects are role-dependent: buyer emotion mainly drives acceptance and rejection, whereas seller emotion shapes concession dynamics. These effects influence not only language, but also termination behavior and price trajectories, raising concerns for emotion-conditioned agents in commerce.

---


### 113. [TRIBE: Predicting Team Performance via Communication Behavior Ensembles](https://arxiv.org/abs/2608.06926)

**<font color=#1a73e8>作者：</font>** Ali Jalal-Kamali, Nikolos Gurney, David V. Pynadath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing autonomous agents that effectively assist human teams hinges on understanding team dynamics, often without task specific knowledge. We present TRIBE, a domain independent approach that reveals team behavioral dynamics invisible to traditional performance metrics. We show that communication patterns can categorize teams into performance predictive behavioral tribes, as early as 10% into the task, enabling timely interventions. We test TRIBE on four diverse datasets and demonstrate that communication patterns predict team performance while the prediction strength varies by the degree a task structure allows for behavioral freedom. Our temporal analysis reveals that AI agents significantly alter team behavioral trajectories while human advisors align with natural dynamics, and that teams maintain behavioral flexibility throughout collaboration. Further, we compare TRIBE to Llama and optimize the pipeline, achieving significant speedup with performance improvement.

---


### 114. [MaskFlow: Precise, Consistent and Seamless Regional Image Editing](https://arxiv.org/abs/2608.06929)

**<font color=#1a73e8>作者：</font>** Rui Xu, Yang Yong, Shunzi Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Regional image editing has attracted considerable attention for its spatial controllability. Although instruction-based and mask-reference-based editing methods can achieve strong semantic alignment, reliable regional control remains challenging, where an edit must be accurately localized and naturally integrated with the preserved context. We propose \textbf{MaskFlow}, a training framework for precise localization, consistent background preservation, and seamless boundary transitions. MaskFlow incorporates the mask into the probability path and flow-matching objective, coordinating generation within the editable region with source preservation outside it. The proposed Soft-Poisson de-seaming module further refines the predicted vector field during both training and sampling to improve the smooth integration of the edited foreground with the preserved background. We also design a data synthesis pipeline to construct MEData, a mask-based image editing dataset for training regional image editing models and facilitating further research. Experiments on natural scenes and infographic images demonstrate consistent improvements over competing methods in both quantitative and qualitative evaluations.

---


### 115. [AVCap: Reinforcing Audio-Video Joint Caption with Detail-Aware Reward](https://arxiv.org/abs/2608.06930)

**<font color=#1a73e8>作者：</font>** Mingyang Wu, Kaituo Feng, Bohao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detailed audio-video joint captioning is essential for multimodal video understanding and generation. However, prior works are constrained by three main limitations: (1) the scarcity of high-quality public datasets with fine-grained audio-visual joint captions; (2) reinforcement-learning methods that rely on coarse reward signals; and (3) the lack of a benchmark and metric for evaluating detailed audiovisual captions at the atomic level. To address these challenges, we propose: (1) AVCap-100K, a high-quality dataset of 100K temporally aligned, detail-rich audio-video captions; (2) AVCap, a model optimized via Detail-Aware GRPO (Da-GRPO) that achieves state-of-the-art performance among open-source models and matches or surpasses proprietary models on several evaluations; and (3) AVCap-Bench and AVCap-Score, a specialized benchmark and metric for evaluating atomic-level details in audiovisual captions. Our code, models, and datasets are available at this https URL.

---


### 116. [Ask-E: An Environment for Calibrated Question Generation](https://arxiv.org/abs/2608.06933)

**<font color=#1a73e8>作者：</font>** Sarah Pratt, Jae Sung Park, Scott Geng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Today, we improve models by training and evaluating them on problems at the frontier of their abilities. Creating such problems is itself a demanding task, requiring the ability to probe model limits and generalize beyond existing question distributions. It also means placing problems at a precise difficulty level, which requires understanding what it takes to solve them. In short, generating problems calibrated to a model's current frontier demands capability beyond it, an increasingly burdensome constraint as models improve. Our key insight is that we can leverage this constraint to our advantage: a model that can generate problems consistently calibrated to a given frontier must possess capability beyond it. Accordingly, we present Ask-E, an environment that benchmarks and trains models on their ability to write questions at a given skill level, rather than answer them. Concretely, we define target skill levels as ranges bounded by the capabilities of two existing language models. A generated question is successfully calibrated if exactly one of the two models can solve it, placing it precisely within the target range and differentiating the capabilities of these models. Ask-E serves both as a benchmark and a training environment, where models generate problems calibrated to a variety of skill levels. We find that even frontier models achieve below 50% calibration on the benchmark, leaving significant headroom to measure future progress. We also show that training on this environment leads to improvements across a number of downstream math benchmarks even with no new math data, no interaction with stronger models, and no correctness-based reward.

---


### 117. [Blind to the Pivotal Vote: Aggregate Independence Metrics Miss Where Verification Actually Helps](https://arxiv.org/abs/2608.06940)

**<font color=#1a73e8>作者：</font>** Yang Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM judge panels are a standard evaluation tool, but prior work reports highly correlated panel errors: nine judges provide roughly the effective information of two independent ones, and aggregation closes only a small fraction of the gap. A natural remedy--a signal from a different evidence source, e.g., executing a test suite--produced no distinguishable change in the panel's effective-vote count at scale (-0.04, 95\% CI [-0.10, +0.02]). Aggregate dependence and conditional decision utility are different questions. Elementary majority arithmetic fixes the affected set for single-ballot substitution: only decisions with a one-vote margin can change. The empirical question is whether panel error rates rise and useful substitutions concentrate there. They do: the entire accuracy gain concentrates on these pivotal queries, where it is large (+10.4 to +23.3 percentage points across three headline configurations), and is exactly zero elsewhere. We confirm the pattern across three code benchmarks and four panel sizes (a 9-judge extension and 56 dependent subsampling checks, gain +6.5 to +16.1 percentage points). On HumanEval+/MBPP+, a majority-side replacement rule raises overall accuracy from 82.44\% to 85.62\% while invoking the signal on 16.2\% of queries; signal-only remains stronger at 87.60\%. Thus population-level dependence diagnostics and margin-stratified utility are complementary, and the affected-set characterization yields a call-reduction rule for any specified single-ballot substitution policy.

---


### 118. [ELMZip: Onboard Satellite Image Compression via Extreme Learning Machines for Efficient Downlink](https://arxiv.org/abs/2608.06942)

**<font color=#1a73e8>作者：</font>** Woojin Cho, Junghwan Park, Sangcheol Sim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The acquisition of multispectral imagery via small satellites (e.g., CubeSats) presents significant data downlink challenges due to high data volumes and restricted communication windows. While onboard image compression is critical to address this bottleneck, traditional methods often struggle to adapt to the nonlinear statistics of multi-band, multi-resolution data. To overcome these limitations, we propose ELMZip, a novel framework based on Extreme Learning Machines (ELM) and domain decomposition strategies for efficient, resolution-free onboard neural representation. ELMZip formulates the fitting process as a convex least-squares problem using random-feature single-layer networks, thereby eliminating the need for computationally expensive backpropagation. By adopting an asymmetric transmission protocol that sends only the compact output weights, the proposed method significantly reduces the downlink payload. Unlike previous neural representation approaches that rely on iterative optimization and require transmitting full network parameters, ELMZip achieves significant compression efficiency while maintaining high reconstruction fidelity. This capability enables immediate image reconstruction for analysis, allowing resource-constrained platforms to maximize data return and advancing real-time AI-powered Earth observation.

---


### 119. [Dual-Space Modality Consistency Learning for Universal Cross-Modal Re-Identification](https://arxiv.org/abs/2608.06943)

**<font color=#1a73e8>作者：</font>** Yujian Zhao, Yukang Zhao, Hankun Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal Re-Identification (ReID) aims to retrieve the same identity across heterogeneous imaging modalities and has been widely studied in visible-infrared person ReID and cross-modal ship ReID. Existing methods have achieved promising performance by learning modality consistency in the spatial embedding space, yet often overlook frequency-domain modality discrepancy, particularly in high-frequency representations that are both highly discriminative and modality-sensitive. In addition, most approaches are tailored to specific modality settings, limiting their applicability across diverse cross-modal scenarios. To address these challenges, we propose a Dual-Space Modality Consistency Learning (DSMCL) framework for universal cross-modal ReID. Specifically, DSMCL jointly models spatial feature distribution consistency and frequency-domain discriminative consistency. A Spatial Modality Consistency Learning (SMCL) branch performs Gaussian-based feature alignment, while a Frequency-aware Discriminative Consistency Learning (FDCL) strategy regularizes high-frequency representations through identity-aware cross-modal contrastive learning. By jointly capturing modality-specific characteristics and modality-shared identity cues, DSMCL learns robust representations and establishes a unified framework capable of accommodating diverse heterogeneous modality settings. Moreover, DSMCL is a plug-and-play framework that can be readily integrated into existing cross-modal ReID architectures. Extensive experiments on SYSU-MM01, RegDB, LLCM, HOSS-ReID, and CMShipReID across seventeen evaluation protocols show that DSMCL consistently improves multiple representative baselines.

---


### 120. [LMM Modality Transfer: A Pre-requisite for Autonomous GIS Agents](https://arxiv.org/abs/2608.06948)

**<font color=#1a73e8>作者：</font>** Ivan Majic, Zexian Huang, Franziska Hübl 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI models are becoming increasingly adept at understanding and processing spatial information, thereby facilitating agentic problem-solving in spatial tasks and workflows. However, most of the research on their spatial capabilities (e.g., spatial reasoning) has focused on the textual modality as input and output. This contrasts with the human approach to GIS workflows, where text and visual modalities are often used together, interchangeably, and in a complementary manner. Thus, to truly achieve an automated GIS analysis pipeline or carry out human-designed GIS workflows, AI models --- Large Multimodal Models (LMMs) in particular --- need to be able to seamlessly transition between image- and text-based modalities that are traditionally used in such workflows. We present a modality transfer task that (1) asks an LMM to first describe an input image of colored squares in a regular grid, and (2) asks a new LMM instance to re-generate an image of the original spatial scene using the textual description output by the former model. This task quantifies the ability of LMMs to transfer spatial information between image and text modalities. Ultimately, by examining the modality transfer capability of LMMs through the lens of spatial information theory, this work highlights a critical bottleneck: achieving strong and robust geospatial understanding in LMMs requires rigorous, multi-modal alignment. Our results indicate that recent LMMs (here from OpenAI) still struggle with modality transfer, when tasked with re-generating an image of a simple spatial grid of color squares.

---


### 121. [A Rate Separation for Agnostic Direct Sums](https://arxiv.org/abs/2608.06951)

**<font color=#1a73e8>作者：</font>** Mihir More, Aritra Das, Debayan Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hanneke, Moran, and Waknine \cite{HannekeMoranWaknine2024} asked how the agnostic PAC learning curve of the direct sum $C^r$ depends on the single-instance learning curve $\epsagn(n\mid C)$ and on $r$. We show that the single-instance learning rate does not determine the direct-sum rate. Let $\F$ be the class of the two constant binary functions and let $\G$ consist of the zero function and the identity function. Both classes have agnostic learning curve of order $n^{-1/2}$.

---


### 122. [Casting the Net! Revisiting MasterFace Impersonation Attacks](https://arxiv.org/abs/2608.06952)

**<font color=#1a73e8>作者：</font>** Seunghun Paik, Sunpill Kim, Chanwoo Hwang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Impersonation is a fundamental security threat in face recognition systems (FRSs). While the security of FRSs has been challenged by various attack vectors, under realistic adversarial capabilities, e.g., a limited number of decision-only authentication trials and no internal system knowledge, most attack techniques become infeasible. As a result, impersonation by zero-effort impostors, characterized by false match rate (FMR), is commonly regarded as a standalone baseline. A few years ago, impersonation attacks based on MasterFaces emerged as a notable security threat that could break the barrier of the FMR-based baseline under such realistic constraints. However, they were believed not to yield impersonation above the standard FMR in modern FRSs, as discussed by multiple follow-up studies. In this paper, we demonstrate that even legitimate access to public commercial APIs allows an adversary to amplify impersonation rates through MasterFaces, resulting in a non-trivial impersonation attack beyond FMR on downstream applications built on top of these APIs. We observe that several real-world FRS deployments are implemented using commercial APIs, and that the backend service provider is publicly disclosed or trivially inferable. As a result, the adversary can purchase these pay-as-you-go API services without requiring any additional privilege over the target FRS. From this observation, we formalize the MasterFaces attack as a maximum coverage problem over the biometric representation space, which we call a NET, and show that the adversary can construct an API-tailored NET by leveraging the geometric structure of the representation space. We demonstrate that our attack amplifies the impersonation rates of several open-source and commercial API-based FRSs by up to 9.5$\times$ within at most 30 authentication trials, compared to those expected from the standard FMR.

---


### 123. [Explicit, Not Longer: What Makes Epistemic Stance Survive Memory Compression](https://arxiv.org/abs/2608.06953)

**<font color=#1a73e8>作者：</font>** Alex Kwon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent memory systems compress what they store, and compression is built to drop qualifiers, so a claim's epistemic standing tends not to survive being written to memory. We ask what governs whether it does. Matched notes carry the identical claim and identical stance and differ only in where that stance sits; one model compresses both under the same budget among the same filler notes, and a blind reader that never sees the condition scores the result. Across 60 claims in seven registers, writing the stance as a labelled field rather than a bracketed aside raises retention by about 15 points on two models (37 claims to 2 on one, 30 to 8 on the other; permutation p=0.00005), and a pre-registered replication on Haiku, its prediction and decision rule committed before the run, gives +15.6 points, 38 claims to 1. Ablating the format on both models gives the same net effect from different parts: labels help on both (+9.7 and +12.8) and length helps on neither, but wording the stance as a full sentence is the largest component on one model (+12.5) and worth nothing on the other (+0.6). Either model alone would have licensed a confident and different mechanism, so we claim only the intersection: make the stance explicit, not merely longer, and expect the best way of being explicit to depend on the model. A deterministic readout with no model reproduces the two-cell direction and five of seven ablation contrasts, but not length or labels, which we therefore do not claim on one instrument. Fifty hand labels (kappa=0.75) agree on direction; we print their seven disagreements in full. We also report nine withdrawn claims, three of them former title claims of this paper.

---


### 124. [How Molecular Generative Models Organize Molecular Identity](https://arxiv.org/abs/2608.06956)

**<font color=#1a73e8>作者：</font>** Raul Ortega-Ochoa, Tejs Vegge, Jens S. Bakander 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models for matter are often evaluated as samplers over output representations, and their latent spaces are commonly used as proxies for navigating chemical space. Much less is known about how these models internally arrange discrete chemical identities within those representations. We study this arrangement by making molecular identity explicit and pulling it back through the generative process. Through these pullbacks we probe the regions that generate the same object, exposing the trained model's internal repertoire: a fixed partition that determines which objects (novel or not) the model can produce.
Across three molecular generative architectures, we find that this repertoire is arranged into piecewise-constant regions separated by recurring coarse-to-fine boundaries. Its organization depends on the representation probed, the identity convention, decoder stochasticity, and the metric used to compare coordinates. During training, local chemical organization stabilizes while the number of distinct molecular identities represented within each neighborhood continues to change. Internal organization must therefore be characterized, rather than assumed, before a generative space can be treated as chemically navigable.

---


### 125. [Summarize First, Download Later: Onboard VLMs for Bandwidth-Efficient Earth Observation](https://arxiv.org/abs/2608.06959)

**<font color=#1a73e8>作者：</font>** Junghwan Park, Sangcheol Sim, Woojin Cho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern Earth observation (EO) satellites carry increasingly advanced sensors that produce vast volumes of high-resolution, multispectral data, yet downlink capacity remains a critical bottleneck -- often causing significant latency or the loss of valuable observations within limited contact windows. We propose a "Summarize First, Download Later" paradigm that exploits recent advances in onboard edge computing and Vision-Language Models (VLMs). Rather than indiscriminately downlinking raw imagery, the system follows a three-phase interaction protocol: the satellite first transmits concise natural language summaries generated by a quantized onboard VLM; ground operators then issue targeted Visual Question Answering (VQA) queries to verify scene relevance (e.g., wildfires or maritime anomalies); and full-resolution images are downloaded only when critical information is confirmed. This transforms the downlink from passive bulk transfer into an active, semantics-aware dialogue. We implement and evaluate the system on a resource-constrained NVIDIA Jetson platform, and experiments on diverse remote sensing scenes show that the proposed strategy substantially reduces bandwidth consumption while accelerating time-to-insight for time-sensitive missions.

---


### 126. [Learning in Deep Networks under Dale's Constraint](https://arxiv.org/abs/2608.06963)

**<font color=#1a73e8>作者：</font>** Roy Abel, Shimon Ullman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biologically plausible learning models aim to explain how neural circuits can implement effective learning under the constraints of real neurons. Although significant progress has been made, a major remaining challenge is that existing models often allow neurons or synapses to represent mixed-sign values, both positive and negative, in violation of a basic aspect of cortical circuitry -- Dale's constraint: biological neurons are either excitatory or inhibitory, but not both, and synapses cannot change sign. In this work, we address this discrepancy by introducing a biologically motivated neural architecture in which both neural activations and learning signals are represented by non-negative activity, and synapses have fixed sign, while still supporting backpropagation-like learning. Our approach uses two complementary interacting non-negative channels to represent positive and negative contributions, inspired by evidence of on-off representations in the brain. These channels are implemented through a simple neural circuit motif, which is repeated throughout the network in both bottom-up and top-down pathways. Combined with a local Hebbian learning rule, the resulting model propagates learning signals and updates weights using only local interactions between neurons. We show theoretically that our learning scheme can exactly recover the backpropagation update despite relying solely on non-negative error signals. Empirically, beyond satisfying stronger biological constraints, the on-off architecture learns efficient representations, yielding substantial gains over comparable vanilla networks on the Tiny ImageNet benchmark. These results demonstrate that effective learning can emerge from biologically plausible mechanisms without requiring mixed-sign signals, providing a step toward more realistic models of neural computation.

---


### 127. [Finding Usable Weight Mechanisms with Tiled SVD](https://arxiv.org/abs/2608.06969)

**<font color=#1a73e8>作者：</font>** Ash Manvi, Samreena Tajreen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The dominant approach to mechanistic interpretability trains proxy dictionaries such as sparse autoencoders and labels features from max-activating text. The best such atlases identify con- cepts, but that identity lives in the learned dictionary rather than in the network weights them- selves. We propose extracting mechanism mounts directly from linear sites by column-tiled SVD: each mount is a triple (v,u,{\sigma}) read as trigger, write, and strength. Identity is the weight rule. We evaluate mounts with a pre-registered suite judged on full-write energy lift rather than tile-local lift. On Gemma-2-2B with WikiText-2 (16,384-token subsample), all seven linear maps are scored: residual writes (this http URL, attn.o) receive full A/B/C with steer after post-sublayer RMSNorm and pass 52/52 site-layers; other maps receive A/B only (this http URL this http URL 26/26 each). Aggregate: 182/182 GO. We release library code, the corpus builder, the experiment entrypoint, and unit tests.

---


### 128. [Generative Embedding Benchmark: How Much Information Survives in a Dense Embedding?](https://arxiv.org/abs/2608.06972)

**<font color=#1a73e8>作者：</font>** Yun Li, Biao Yang, Peixi Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embeddings have emerged as a standard representational interface linking foundation models with downstream systems. Most embedding benchmarks assess representations through discriminative tasks or geometric criteria centered on separability in embedding space. However, strong performance on such evaluations does not establish whether content compressed into an embedding remains accessible to a downstream generator. To address this gap, we introduce the Generative Embedding Benchmark (GEB), in which a decoder answers questions using only a frozen embedding and question text, without access to the original image or intermediate visual features. Answer quality under this readout measures generative information: the answer-relevant content recoverable from an embedding. GEB includes a curated visual-question-answering dataset with a 1,800-item development split and a held-out 900-item test split covering natural images, scene text, and visual documents. Using a common decoder and training recipe, we evaluate seven public embedding models in visual-only and vision-language joint modes. On the test set, visual-only scores range from 28.25 to 33.21; with image-question joint encoding, all five VLM-based embedding models score higher, and the best reaches 65.56. Matched embeddings also outperform text-only inputs, zero embeddings, and shuffled embeddings. Natural-image information is much easier to recover than scene text or visual-document information, while a Qwen3-VL-2B reference with access to the original image reaches 84.30. Together, these results show that generative readout exposes information bottlenecks that separability-based evaluation does not capture.

---


### 129. [PHASE-Tree: Modeling Character-State Evolution in Long-Horizon Role-Playing Dialogue](https://arxiv.org/abs/2608.06975)

**<font color=#1a73e8>作者：</font>** Bo Tang, Jianan Yang, Junyi Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon role-playing demands that characters remain recognizable as they evolve with the narrative. Yet existing work falls short on two fronts: representations are typically static profiles that cannot be updated locally without destabilizing unchanged traits, and benchmarks mainly test persona preservation and memory recall rather than whether a model speaks from a character's currently evolved state. We address both. PHASE-Tree is a multi-timescale character-state tree with an immutable identity root and mutable persona, session, and moment layers, making each mutable field an addressable target for localized within- and cross-episode updates. It conditions generation through explicit textual provision or implicit parametric adaptation. To measure evolved-state generation, we introduce LongEvoRoleBench, which pairs four long-dialogue corpora for cross-episode evolution with four short-dialogue corpora as within-scene state-tracking checks, under a unified next-utterance protocol. On the long-dialogue core, textual PHASE-Tree ranks first in 11 of 12 dataset-metric cells against internal variants and all 12 cells against external textual baselines, improving character-level, semantic, and embedding scores by 19.7%, 12.4%, and 15.1% respectively. In a blinded 200-response study, human ratings correlate with the GPT-4.1 judge (Pearson r= 0.65); on descriptive n= 10 PT and NR prompt subsets, the Overall difference is +0.20. The long-dialogue Sem advantage persists across LLM judges and generation backbones.

---


### 130. [Social Facilitation of Creative Reflection: AI-agents and Humans](https://arxiv.org/abs/2608.06980)

**<font color=#1a73e8>作者：</font>** Olga Sutskova, Corey Ford  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social collaboration can support people's reflection and is a crucial component of creativity. Creative technologies have been designed to support more collaborative ways of working, including using AI to simulate social partners. As human-AI creative collaborations increase, further investigation is needed into how different social interactions influence creative reflection and at which stage a social intervention is crucial to improve creative outcomes. Considering that non-verbal communication is the bedrock of human cognition and influence, non-verbal social dynamics should be examined in detail in the age of AI-companionship. For example, during social interaction, the social facilitation effect describes how the mere presence or observation of others influences how a person behaves and feels in the context. Whether changes in technology-mediated social environments influence how people reflect on their creative work needs further exploration, as does whether social AI-companionship elicits similar effects as humans. This paper discusses how theoretical mechanisms relating to social facilitation could influence creative practice and reflection, proposing ways of further testing these effects.

---


### 131. [Local Epistemic Uncertainty Guided Active Sampling for Plug-and-play Diffusive Image Restoration](https://arxiv.org/abs/2608.06981)

**<font color=#1a73e8>作者：</font>** Jiaqi Zhang, Zheng Pang, Rongrong Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have demonstrated remarkable effectiveness in image restoration tasks. However, when guiding image reconstruction, existing Diffusion Model-based Image Restoration (DMIR) methods typically rely on fixed data constraints and uniform step sizes, thereby overlooking the dynamic nature of the generative process. Such rigid designs render the models vulnerable to spatially non-uniform degradations, thus resulting in structural distortions and loss of fine details. Meanwhile, uniform step sizes introduce computational redundancy, whereas naïve step reduction strategies tend to accumulate approximation errors. To address these limitations, we propose a Local Epistemic Uncertainty Guided Active Sampling framework (LEADer). In the spatial domain, LEADer leverages pixel-wise uncertainty to dynamically modulate the prior strength within the null space, which effectively balances detail preservation and artifact suppression. In the temporal domain, it quantifies sampling stability via the uncertainty trace to enable adaptive trajectory pruning, thereby accelerating convergence. Theoretical proofs demonstrate that our framework achieves strict data consistency, while the trajectory pruning strategy admits a deterministic error bound, thereby guaranteeing stable convergence under skip sampling. Notably, our plug-and-play method can be seamlessly integrated into various DMIR baselines. Extensive experiments show that LEADer improves the performance of multiple state-of-the-art DMIR methods, while significantly reducing sampling time with negligible memory overhead. Code is available at this https URL.

---


### 132. [HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses](https://arxiv.org/abs/2608.06984)

**<font color=#1a73e8>作者：</font>** Xiao Zhang, Yusheng Wang, Yuhao Fei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern agent harnesses persist state across tasks and sessions through persistent carriers like memory, skills, tools, and shared artifacts. However, this capability creates delayed safety risks: attacker-influenced content can cross system boundaries and later affect the execution of a benign request. Existing benchmarks typically focus on a few carriers or harnesses, while end-to-end attack-success rates reveal little about how risks propagate. To this end, we present HarnessSafe, a benchmark comprising 328 executable cases across seven persistent-carrier families and evaluated on most mainstream agent harnesses. Each case is specified as a Persistent-Risk Lifecycle that traces attacker influence from its initial entry, through persistence across carriers and system boundaries, to a later benign trigger and an observable violation. We further introduce a multi-stage, trace-based evaluation that uses observable execution evidence to determine how far each attack chain progresses and where it is stopped. Experiments show that containment is carrier-specific and strongly depends on the harness-model configuration. Both the harness and model backend substantially shape containment outcomes, while attack success rates cannot reflect distinct lifecycle progression patterns.

---


### 133. [Switched Reading: Toward Seamless Visual-Auditory Switching When Reading Text in Augmented/Mixed Reality](https://arxiv.org/abs/2608.06985)

**<font color=#1a73e8>作者：</font>** Kazuyuki Fujita, Yuto Matsui, Ikuru Sato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Augmented/mixed reality (AR/MR) wearable glasses now permit information interaction anywhere, but visual displays can be inappropriate when real-world awareness is essential. We propose Switched Reading, a novel interaction framework for reading text in AR/MR that supports switching between visual and auditory modalities as needed. Specifically, we explore two key interaction techniques within this framework: (1) gaze-based voice playback and (2) a correspondence-aware transition effect. We implemented them on an MR headset through a parameter-tuning user test. Next, we conducted a user study (N=16) to investigate the impact of the two techniques on reading performance and overall user experience with simulated modality switching in virtual reality. The results show that the condition combining both techniques was the most preferred among four conditions. Moreover, we found that the gaze-based voice playback reduced gaze offsets when switching modalities and improved reading speed over the baseline condition using scroll position. Finally, we implemented a Switched Reading application for reading while walking and collected user feedback, yielding further design implications for practical use.

---


### 134. [Density-aware Hierarchical Clustering Based on Element-Categorized Connection Subgraphs](https://arxiv.org/abs/2608.06990)

**<font color=#1a73e8>作者：</font>** Yuning Yu, José Rodríguez-Piñeiro, Xuefeng Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clustering is a fundamental data mining technique for pattern recognition through unsupervised learning. Among various clustering methods, hierarchical clustering, density-based clustering, and graph clustering stand out as representative approaches. For hierarchical clustering, it can be categorized into agglomerative and divisive modes to construct clusters in a recursive manner. The key aspect of both modes is the calculation of inter-cluster similarity, which determines whether to merge the sub-clusters into one cluster or divide a current cluster into sub-clusters. Traditionally, the similarity is derived from pairwise distances, often overlooking density variations and structural connectivity in graphs. To address this, we propose a density-aware hierarchical clustering method based on element-categorized connection subgraphs (DHC-ECS), which effectively integrates the hierarchical clustering, density-based clustering, and graph clustering. Particularly, a novel inter-cluster similarity metric is introduced that considers not only distances but also the element categorization in the KNN connection subgraphs, kernel density estimation, and local connectivity within sub-clusters. Extensive evaluations on heterogeneous benchmark datasets demonstrate that DHC-ECS exhibits superior overall performance in terms of clustering accuracy and parameter robustness compared with the baseline methods (including AChameleon, RNN-DBSCAN, McDPC, and G-RMS). The work indicates the great potential of the proposed clustering algorithm for low-dimensional datasets by leveraging local density and graph-structured connectivity (i.e., the duality of vertices and edges), as well as the possibility to determine an intrinsic threshold, reducing the reliance on manual parameter tuning.

---


### 135. [HRDiT: Training-Free High-Resolution Image Generation with Off-the-Shelf Diffusion Transformer Models](https://arxiv.org/abs/2608.07003)

**<font color=#1a73e8>作者：</font>** Yu Xue, Haoxuan Qu, Zhuoling Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free text-to-high-resolution image generation has recently attracted growing research attention. However, existing studies on this task primarily focus on adapting off-the-shelf U-Net-based diffusion models to high resolutions, with limited progress on adapting off-the-shelf Diffusion Transformer (DiT) models despite their strong text-to-image generation capabilities at limited resolutions. In this work, we find two key challenges particularly hindering the application of off-the-shelf DiT models for high-resolution image synthesis in a training-free manner, namely, spatial disorder and long generation time. To address these challenges, we propose a novel method tailored to adapt off-the-shelf DiT models for high-resolution image synthesis. Extensive experiments show the efficacy of our method. Our code is available at: this https URL.

---


### 136. [FedLBW: A Loss-Based Weighting Strategy for Federated Learning on Non-IID Data in Wireless Networks](https://arxiv.org/abs/2608.07007)

**<font color=#1a73e8>作者：</font>** Majid Kundroo, Tinku Singh, Taehong Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative machine learning (ML) across distributed clients while preserving privacy. However, efficient model convergence in FL remains challenging, especially in wireless networks where non-independent and identically distributed (non-IID) data and frequent client dropouts are common. Traditional FL algorithms, such as FedAvg, rely solely on dataset size to weight client updates. This introduces biases towards clients with larger datasets and makes the process sensitive to non-IID data, outliers, and client dropouts. To address these challenges, we propose Federated Learning with Loss-Based Weighting (FedLBW), a novel aggregation method that assigns each client's update a weight proportional to the inverse of its validation loss, computed using a small proxy dataset on the server, rather than its dataset size. This ensures that lower-loss models exert greater influence during aggregation, prioritizing the most reliable updates and boosting overall performance. Through extensive experiments across multiple datasets, including FashionMNIST (CNN), CIFAR-10 (ResNet-18), and CIFAR-100 (ResNet-34), we demonstrate that FedLBW achieves higher accuracy and faster convergence compared to baseline algorithms such as FedAvg, FedAvgM, FedProx, FedNova, FedLAW and FedDkw, with notable improvements of up to 7.6 % higher accuracy on CIFAR-10 in extreme non-IID cases. Moreover, FedLBW showcases exceptional resilience to increasing dropout probabilities, consistently maintaining significantly higher accuracy even in challenging conditions. These results establish FedLBW as an effective and resilient solution for FL in wireless network environments, offering marked improvements in model accuracy, convergence speed, and robustness to non-IID data and client dropouts.

---


### 137. [Scenix: Sparse-View 3D Scene Reconstruction via Executable Scene Programs](https://arxiv.org/abs/2608.07012)

**<font color=#1a73e8>作者：</font>** Kai Li, Lutao Jiang, Zhenyang Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing a structured and editable 3D indoor scene from a few uncalibrated RGB views requires more than generating high-quality individual assets: a system must infer the room structure, associate objects across incomplete observations, and recover a globally consistent spatial configuration. Previous methods mainly focus on 3D scene generation with text input or require continuous visual inputs with additional priors, \ e.g., human-annotated masks or accurate 3D layouts, which makes these methods labor demanding and hard to apply in general cases. We present \textsc{Scenix}, a sparse-view 3D scene reconstruction framework via executable scene programs, a structured representation that can be directly instantiated into editable 3D scenes. Given sparse views, \textsc{Scenix} predicts executable scene programs through perception-grounded asset instantiation and closed-loop spatial refinement. % We present \method, a framework that predicts an executable scene representation from sparse views and realizes it through perception-grounded asset instantiation and closed-loop spatial refinement. To support this task, we construct \dataset, a dataset of approximately 110,000 synthetic and real indoor scenes with multiview imagery, room structures, object-centric descriptions, and metric spatial annotations. We further introduce observation-consistent supervision that aligns each target scene with the visual evidence available in its input views. Experiments on held-out \textsc{XScene} scenes, real indoor images, and out-of-distribution SpatialGen cases evaluate structured scene prediction, object grounding, and spatial refinement.

---


### 138. [Understand Before Detect: Vision--Language Learning for Omni-Domain Infrared Small Target Detection](https://arxiv.org/abs/2608.07015)

**<font color=#1a73e8>作者：</font>** Haoyang Yuan, Boyang Li, Yingqian Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-domain infrared small target (IRST) detection is crucial for infrared surveillance, yet remains challenging due to heterogeneous imaging domains and inconsistent target characteristics. Previous deep learning-based methods have been developed for visual-only paradigms and achieved promising performance on domain-specific tasks. However, existing methods follow the task-specific supervised learning paradigm. This paradigm simplifies the full-scene infrared observations to sparse target supervision, discarding the semantics that remain invariant across heterogeneous domains. Consequently, detection performance suffers substantially under domain shifts. To handle this issue, we introduce \textbf{``understand before detect''}, a paradigm that formulates omni-domain IRST detection as an understanding-driven process, where holistic infrared target understanding precedes precise detection. Building on this paradigm, we propose \textbf{JinSight}, which first develops holistic IRST understanding through language supervision and then transfers the learned cross-domain representations to precise small-target detection. By grounding infrared representations in language semantics, JinSight enables a single model to generalize across heterogeneous infrared domains. We then introduce Latent Semantic Interaction (LSI), which exchanges language-aligned global semantics with fine-grained spatial features in a compact low-rank space. To address the lack of multimodal omni-domain IRST benchmarks, we build \textbf{OmniIRST-VL}, the first large-scale, highly diverse vision--language dataset for omni-domain IRST detection. It comprises over 39k annotations across six complementary instruction tasks covering both scene-level understanding and target-centric reasoning.

---


### 139. [Effects of parental controls in the context of Digital Forensics](https://arxiv.org/abs/2608.07016)

**<font color=#1a73e8>作者：</font>** Selina Märchya, Mauro Vignatia, Frank Breitinger  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Parental control systems are designed to protect minors online, but can inadvertently obstruct digital forensic investigations. When enabled, these systems restrict administrative privileges, disable debugging options, and alter data accessibility, complicating evidence acquisition and analysis. This study empirically examines the impact of Microsoft, Google, and Apple parental controls on forensic processes across fifteen Windows, Android, and iOS devices. Through controlled experiments, we evaluate their impact on evidence accessibility and identify forensically sound methods to overcome these limitations. The findings provide practical guidance for investigators and contribute to improving forensic readiness in environments governed by parental control systems.

---


### 140. [Hyperbolic Graph Embedders for Link Prediction and Topology Reconstruction](https://arxiv.org/abs/2608.07029)

**<font color=#1a73e8>作者：</font>** Robert Jankowski, Maksim Kitsak, Dorota Celińska-Kopczyńska  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperbolic embeddings provide compact geometric representations of complex networks in hyperbolic spaces, but systematic comparisons of methods developed in machine learning, network science, and algorithmics remain rare. We benchmark 13 unsupervised hyperbolic graph embedders under a unified protocol for link prediction and topology reconstruction on synthetic and empirical networks. The protocol captures both missing-link recovery and the preservation of local and global network structure. Maximum-likelihood and representation-learning-based approaches, including hybrid variants, achieve the strongest overall performance, although no method dominates across all tasks and structural regimes. Performance is more strongly associated with embedding paradigm than with disciplinary origin. We identify the network regimes in which different paradigms succeed or fail and provide practical guidance for method selection in downstream applications.

---


### 141. [Accounting Graph Transformer for Short-History Multi-KPI Forecasting in Small Businesses](https://arxiv.org/abs/2608.07037)

**<font color=#1a73e8>作者：</font>** Shrutendra Harsola, Vignesh Subrahmaniam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small businesses often have only 12-24 months of accounting history, yet planning and risk workflows require coordinated forecasts across financial statements. We study joint 12-month forecasting of 13 income-statement, balance-sheet, cash-flow, and working-capital key performance indicators (KPIs) from 71 monthly ledger series. We introduce the Accounting Graph Transformer (AGT), which represents each ledger series as a masked token, exchanges information through typed attention on a fixed accounting-relation graph, pools target-specific context, and fuses it with a gated three-month recency path. Across 11,993 forecast origins from 1,060 unseen companies, AGT achieves sample-weighted KPI-macro mean absolute error (MAE) $0.6990 \pm 0.0013$ over three independent seeds, compared with $0.7378 \pm 0.0014$ for the strongest baseline, LightGBM. At the pre-specified seed 42, a paired company-clustered bootstrap gives a LightGBM-minus-AGT difference of 0.0395 with 95% confidence interval (CI) $[0.0350,0.0439]$. AGT is best on all 13 KPIs against LightGBM, TimeMixer, and SOFTS in the matched seed-42 comparison, while final-architecture ablations show that relational attention, accounting topology, and the recency path each improve validation and test accuracy. On 7,094 additional unseen companies with origins sampled from January-May 2025, AGT obtains 0.7548 MAE versus 0.7694 for SOFTS. A single 5.3M-parameter model produces 156 aligned forecasts without company-specific fitting, providing one forecasting layer for integrated planning, liquidity, and working-capital analysis.

---


### 142. [Not All Problems Are Best Modeled as MILP: A DSL-Centric Framework for Flexible and Accurate Optimization Modeling](https://arxiv.org/abs/2608.07040)

**<font color=#1a73e8>作者：</font>** Shaofeng Zhang, Hongyuan Su, Qingwen Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Solving combinatorial optimization problems (COPs) requires not only efficient algorithms but also carefully crafted formulations. While recent works have leveraged LLMs to automate optimization modeling, current frameworks predominantly rely on a rigid mixed-integer linear programming (MILP) paradigm. In this paper, we argue that not all problems are best modeled as MILP, as forcing complex domains into linear constraints can induce prohibitive modeling complexity and severely restrict solver flexibility. To address this, we propose OptiDSL, a framework that shifts the focus from rigid MILP formulations to domain-specific language (DSL) representations. By utilizing LLMs to map natural language onto standardized, domain-accepted structures, OptiDSL decouples problem formulation from execution. This paradigm enables seamless integration with a diverse library of specialized solvers, ranging from traditional heuristics to modern learning-based methods. Experimental results on the comprehensive benchmark of 44 COP types show that OptiDSL significantly surpasses MILP-based pipelines, yielding a 51.66% gain in formulation accuracy and a 91.71% decrease in modeling time. Notably, it also outperforms MILP-based pipelines on the existing benchmark, achieving a 23.09% higher formulation accuracy. Our code is available at this https URL.

---


### 143. [BONSAI: Evolvability-Guided Tree Search over Skills](https://arxiv.org/abs/2608.07056)

**<font color=#1a73e8>作者：</font>** Yash Priya Shastri, Anand Eswaran, Adnan Qidwai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A skill is a naturallanguage document that steers a frozen agent whose weights cannot be updated so any capability the agent lacks must be supplied in prose Optimising a skill is therefore optimising text against a score and the standard recipe which keeps any edit that raises a heldout score is blind in a specific way a single score cannot tell a document perched on a narrow overfit spike from one resting on a broad plateau even though only the second can still be improved We introduce BONSAI a novel skilloptimisation framework that steers instead by evolvability the capacity of a region of documentspace to keep producing viable variation under further mutation a property biology treats as separate from present fitness BONSAI grows skills as a MonteCarlo search tree in which every child document is a mutation of its parent and descends it under an upperconfidence selection rule whose exploitation term blends a skills own fitness with the fitness of its mutational neighbourhood Because every child is a mutation the mean score recorded beneath a node estimates that neighbourhoods evolvability at no extra cost so the rule concentrates budget on regions that keep improving while its exploration term keeps a currently weak branch in contention BONSAI ships the single bestscoring document it finds at no cost beyond the acceptifbetter loop it replaces With a frozen 30B agent and averaged over three benchmarks BONSAI lifts heldout accuracy over the skillfree agent by 2313 points and improves on two budgetmatched baselines GEPA and SkillOpt by 387 and 397 points respectively

---


### 144. [KnifeHunter: Structured Local Representation Learning for Fine-Grained Knife Image Retrieval in Law Enforcement](https://arxiv.org/abs/2608.07057)

**<font color=#1a73e8>作者：</font>** Syed Sameed Husain, Eng-Jon Ong, Stephen Simpson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knife-enabled violence presents a major public safety challenge, and law enforcement agencies require scalable tools for catalogue-level knife identification, intelligence analysis, and source attribution. Manual visual comparison is specialist, time-consuming, and difficult to scale under operational imaging conditions. We introduce KnifeHunter, an end-to-end forensic knife image retrieval system developed with UK law enforcement. The work contributes the KnifeHunter dataset, comprising 25,843 images across 543 knife classes from police evidence, retail catalogues, and border-force seizures, with structured metadata, Medium/Hard evaluation protocols, and large-scale distractor evaluation. We further propose CoRe-Net, a compact single-descriptor retrieval architecture that combines global context with spatially localised discriminative evidence. CoRe-Net introduces Structured Complementary Representation Learning (SCRL) to organise local evidence into complementary prototype-based representations, and Bi-Directional Reciprocal Fusion (BDRF) to integrate global and local evidence through residual projection and gated local-to-global injection. Using an EVA02-Base backbone and cosine-similarity retrieval, CoRe-Net achieves 88.0% mAP and 86.7% mP@10 on the Medium protocol, and 85.1% mAP and 83.8% mP@10 under distractor conditions. KnifeHunter was deployed by UK police forces during Operation Sceptre deployments from 2023 to 2025, achieving 99.2% mP@1 on field queries. These results demonstrate a practical and effective multimedia retrieval framework for fine-grained forensic knife matching in operational law-enforcement settings.

---


### 145. [Explanation Stability of Test-Time Adaptation in Computational Pathology: A Large-Scale Benchmark](https://arxiv.org/abs/2608.07062)

**<font color=#1a73e8>作者：</font>** R. G. Bahumanya, Harshith V. M., Shreyank N. Gowda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) has become a practical way to adapt deployed models to unlabeled target data, a setting that is especially relevant in computational pathology where staining, scanner, and cohort shifts are routine. While most TTA methods are evaluated by their effect on accuracy, clinical use also depends on whether the model's explanations remain reliable after adaptation. In this paper, we take a closer look at this largely unmeasured effect. We study explanation stability under TTA across two histopathology benchmarks, Camelyon17 and NCT CRC-HE, using five architectures ranging from convolutional networks to vision transformers and a pathology foundation model, seventeen TTA methods, and four attribution families. Across 2,958 adaptation runs, we observe a clear and systematic pattern: TTA methods differ sharply in how much they move model explanations, with frozen-backbone methods leaving attributions almost unchanged and continual methods such as CoTTA and RoTTA causing the largest drift. This effect is not uniform. Convolutional networks are substantially more sensitive than transformer and foundation-model backbones, and explanation drift increases with adaptation strength while remaining largely insensitive to batch size. Surprisingly, explanation stability is only weakly coupled to adaptation quality. Some methods preserve explanations almost perfectly while degrading calibration or accuracy, producing silent failures that would be missed by accuracy-only or explanation-only evaluation. These findings show that explanation stability is a distinct reliability axis for TTA in computational pathology. We release the metric, protocol, and full benchmark to support future work on adaptation methods that are not only accurate, but also stable and clinically auditable. Code: this https URL

---


### 146. [Soft Redaction of Image Provenance via Zero-Knowledge Proofs](https://arxiv.org/abs/2608.07063)

**<font color=#1a73e8>作者：</font>** Muhammad Awan, John Collomosse  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Content provenance standards, such as C2PA, are increasingly used to attach signed records of origin, editing history, and rights to digital images. However, provenance transparency can conflict with privacy -- assertions that strengthen trust in an image may also reveal sensitive information about the creator or capture context. We propose soft redaction for image provenance: a mechanism that replaces sensitive provenance assertions with zero-knowledge proofs (ZKPs) of selected properties over hidden data. Our work focuses on distance proofs. We first show how location assertions can support proofs of proximity to a public reference point, using Chebyshev polynomial approximations within the ZKP proof circuit. We then extend the approach to L2 distance proofs over biometric embeddings, enabling privacy-preserving claims related to likeness to help enforce personality rights with images. Finally, we apply the same distance-proof construction to perceptual hashes (visual fingerprints), supporting an anti-spoofing use case in watermark-based recovery of stripped provenance metadata. Our results demonstrate that ZKPs over image provenance can provide practical soft-redaction capabilities, compatible with C2PA, that may be constructed in seconds and verified in milliseconds.

---


### 147. [XGait: A Multi-Modality Wireless Sensing Dataset for Indoor Human Tracking and Identification](https://arxiv.org/abs/2608.07064)

**<font color=#1a73e8>作者：</font>** Wei Xu, Zhu Wang, Yifan Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wireless sensing has emerged as a promising approach for tracking and identification using commodity Internet of Things devices. However, the features derived from a single wireless modality are often fragile to variations in environmental layouts and walking trajectories. Furthermore, most existing studies are based on datasets collected in specific scenarios with limited trajectory diversity and sensing modalities, preventing a robust evaluation of system generalization. \textcolor{blue}{To address this gap, we introduce \textbf{XGait}, a multi-modality wireless sensing dataset that synchronously captures human walking using Wi-Fi and acoustic transceivers across three indoor scenarios, with vision-based measurements serving as ground truth. Specifically, XGait contains more than 22K walking samples from 27 participants, covering diverse directions and trajectories to support both indoor tracking and identity recognition. To bridge the heterogeneity of wireless sensing modalities, we propose a unified Doppler spectrogram representation that maps Wi-Fi and acoustic signals into a shared time--frequency space, along with a standardized benchmark pipeline for pre-processing, temporal alignment, and feature construction, enabling reproducible evaluation and systematic cross-modal analysis. Extensive evaluations demonstrate that Wi-Fi and acoustic sensing exhibit complementary strengths, particularly under complex trajectories and challenging propagation conditions, thereby paving the way for novel research in the field of multi-modality wireless sensing.} The dataset and code are available at this https URL.

---


### 148. [DocMemo: Dynamic Evidence Discovery via Probabilistic Memory-Guided Retrieval for Multi-Modal Document Understanding](https://arxiv.org/abs/2608.07067)

**<font color=#1a73e8>作者：</font>** Hanshu Yao, Janfeng Zhong, Niu Lian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-document understanding requires locating sparse and heterogeneous evidence across hundreds of pages, yet existing systems remain limited by static retrieval and fragile cross-round memory. Mainstream single-round methods commit to a fixed top-$k$ page set at the outset and struggle to recover from early retrieval errors; recent iterative approaches allow multi-round evidence acquisition, but they do not investigate the propagation mechanism of cross-round states, making it difficult to track the dynamic changes in page relevance. To address these limitations, we propose DocMemo, a memory-guided framework that formulates long-document reasoning as dynamic evidence exploration. DocMemo maintains a tri-level retrieval state consisting of Document Schema Memory, Page Belief Memory, and Question Episodic Memory, which respectively capture structural priors, dynamic relevance estimation, and query-specific reasoning trajectories. During reasoning, DocMemo continuously refines cross-round page selection through Bayesian page belief updating with Thompson sampling, spatial proximity propagation, and structure-aware adaptive-granularity evidence access, while supplementing page-level evidence with fine-grained visual regions. Experiments on 3 benchmarks show that DocMemo achieves state-of-the-art performance and validate the efficacy of structured memory and dynamic page belief updating. Code is available at this https URL.

---


### 149. [Beyond Isolation: Unlocking Reinforcement Learning Component Synergy for Sample-Efficient Continuous Control](https://arxiv.org/abs/2608.07086)

**<font color=#1a73e8>作者：</font>** Qi Zhao, Guozheng Ma, Yilun Kong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning systems are significantly more complex than other machine learning paradigms due to inherent properties, causing RL system design to jointly account for many tightly coupled factors. Despite advances in individual algorithmic components, their functional interdependencies remain underexplored: do they exhibit mutual synergy or counterproductive interference? To bridge this gap, we conduct a systematic investigation and find that the efficacy of different components exhibits significant task-dependency, and naively stacking state-of-the-art techniques does not necessarily yield performance gains; instead, it often triggers emergent challenges, such as compounded non-stationarity. Building upon these findings, we distill a suite of actionable insights into the principled coordination of these components. Guided by these insights, we propose ROSER, an RL framework that coordinates three critical dimensions: Model-based Representation, Optimization Stability, and Experience Replay. Across diverse continuous-control benchmarks, ROSER consistently outperforms vanilla baselines and achieves 17.60% gains over naive stack. Our findings underscore the necessity of a holistic perspective in RL system design and paves the way for developing sample-efficient agents.

---


### 150. [UncertaintyVis: Preserving Linguistic Uncertainty in Automated Text-to-Chart Generation](https://arxiv.org/abs/2608.07093)

**<font color=#1a73e8>作者：</font>** Songheng Zhang, Emily Aurelia, Anthony Tang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Data-rich documents pair narrative text with quantitative claims, and authors routinely qualify those claims with linguistic uncertainty markers such as "nearly," "approximately," or "at least." Automated text-to-chart systems discard these markers, producing visualizations that appear definitive even when the source text expresses hedged or incomplete knowledge. Readers may then over-interpret precision and misjudge author intent. We present UncertaintyVis, a system that preserves linguistic uncertainty during automated chart generation. A formative corpus analysis of 211 uncertainty expressions across 12 documents and 8 domains yielded a four-category taxonomy: Surface Form Normalization, Precision Boundaries, Inferential Derivation, and Non-Inferable Gaps. We mapped each category to chart-specific visual encodings that signal uncertainty without disturbing the spatial integrity readers rely on, and implemented an end-to-end pipeline pairing large language model text analysis with uncertainty-aware rendering. In a two-part study with 12 participants, readers matched charts to source text with 85% accuracy and text to charts with 76%. Uncertainty-aware visualizations trended toward lower cognitive demand (effect sizes 0.460 and 0.769 for mental demand and effort), and 75% of participants preferred them to plain text, describing explicit uncertainty encodings as a basis for verifying data claims. Encoding effectiveness varied by chart type: bar and pie encodings performed consistently, while line chart encodings require redesign.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-221](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

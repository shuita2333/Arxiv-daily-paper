# 📦 其他研究 | 2026年06月10日

> 本类共 **527** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-527](./part-11.md)

---

### 401. [SOMA: From Surface Observations to Muscle Anatomy](https://arxiv.org/abs/2606.09246)

**<font color=#1a73e8>作者：</font>** Eduardo Alvarado, Emily Kim, Gerrit Nolte 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the growing demand for realistic virtual humans, parametric body models have become a cornerstone of modern medicine, sports, and entertainment applications. However, most of these models are inherently limited: they only capture the 3D surface of the skin, offering no insight into the complex bio-mechanical structures that generate motion. As more applications expand towards biomechanics, the need for virtual human models that go beyond the skin has become increasingly evident. Traditional soft-tissue simulations, such as FEM, are accurate but non-scalable and too computationally expensive for most common applications. Alternatively, existing biomechanical tools can simulate muscular forces and activations, but do not model changes in external shape, restricting how activations correlate with actual observable anatomy. This motivates a novel inverse research problem: recovering muscle deformations directly from visible surface observations - i.e., from the skin, and thus the pose. In this work, we present SOMA (from Surface Observations to Muscle Anatomy), a person-specific model that infers spatio-temporal muscle behavior from surface signals obtained using RGB cameras, and SKIM, a subject-specific soft-tissue deformation dataset. To the best of our knowledge, this is the first method that attempts to recover muscle deformations from multi-view RGB data. We show how our method provides anatomically grounded animations without the complexity of traditional simulations, leading to a scalable and cost-effective solution. Data and code are available.

---


### 402. [LiteVSR: Lightweight Adaptation of Frozen Diffusion Transformers for Video Super-Resolution](https://arxiv.org/abs/2606.09250)

**<font color=#1a73e8>作者：</font>** Yu Cao, Ziquan Liu, Zhensong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting large-scale pre-trained video generators for Video Super-Resolution (VSR) in novel domains remains computationally prohibitive. Methods that reformulate generation as direct Low-Quality to High-Quality mappings deviate from the original generative formulation, demanding extensive fine-tuning. ControlNet-style adapters lose their efficiency under modern Diffusion Transformers since the absence of encoder-decoder hierarchy forces duplication of the entire backbone. We observe that flow matching offers a principled alternative for cross-domain VSR adaptation. By predicting a constant velocity field across all timesteps, the adaptation task reduces to learning a fixed injection pattern rather than time-varying transformations. Building on this insight, we propose LiteVSR, a minimalist framework that performs VSR using a completely frozen Diffusion Transformer with a lightweight State-Aware Adapter. The adapter employs a dual-stream architecture that extracts static structural cues from the LQ input and dynamic cues from intermediate denoising states, aligning them through time-dependent cross-attention to enable adaptive transition from structural alignment to texture refinement as denoising proceeds. LiteVSR achieves competitive restoration quality with only 11.25% trainable parameters and 12 GPU-hours of training on a single A100, while maintaining fast sampling (down to a single step) compatibility.

---


### 403. [TruthSplit: Operationalizing Conditional Validity in Arguments Through Multi-Perspective Reasoning](https://arxiv.org/abs/2606.09251)

**<font color=#1a73e8>作者：</font>** Benjamin Stieger, Maximilian Terberger, Thomas Huber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present TruthSplit, an interactive system for multi-perspective argument analysis. Existing argumentation tools typically analyze properties of the argument itself, such as structure, quality, stance, or persuasiveness, while leaving perspective-specific background knowledge implicit. TruthSplit addresses this gap by supporting an exploratory analysis of how the same claim can lead to different conclusions when interpreted through worldview-specific values, assumptions, and conceptual definitions. We refer to this perspective-dependent analysis as conditional validity. Given an input argumentative text, TruthSplit extracts claims and premises, applies a three-layer natural language inference (NLI) approach to assess both logical and worldview-specific normative consistency, and conditions large language model (LLM) reasoning on structured worldview profiles that encode core values and decision principles. The system then generates perspective-specific interpretations, identifies value conflicts and assumption gaps, and visualizes divergence through interactive analytical interfaces.

---


### 404. [A practical probabilistic framework for deformable image registration uncertainty in radiotherapy dose propagation](https://arxiv.org/abs/2606.09253)

**<font color=#1a73e8>作者：</font>** Stefan Heldmann, Sven Kuckertz, Nasim Givehchi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deformable image registration (DIR) is widely used in radiotherapy for dose propagation and accumulation, but uncertainty in the underlying deformation can substantially affect clinically relevant dose estimates. We present a practical probabilistic framework for propagating DIR uncertainty to voxel-wise dose statistics and dose-volume histograms (DVHs). The method models the mapped correspondence at each voxel as a random variable governed by a transparent local certainty map that can be defined by simple safety margins, structure-boundary mismatch, or structure-wise conservative uncertainty values. This yields interpretable quantities such as dose probabilities, expected dose, confidence bounds, and induced DVH envelopes.
The framework is designed to remain lightweight and interpretable: it avoids complex biomechanical or ensemble-based uncertainty models and instead emphasizes simple parameterization, computational feasibility, and transparent dose metrics. We further introduce a structure-guided in/out strategy as an optional refinement that restricts mapping probabilities to anatomically plausible target regions. The approach is demonstrated on a prostate radiotherapy case study and used to compare different certainty-map strategies and probability kernels. The experiments show that the certainty-map design has a stronger effect on resulting dose and DVH uncertainty bounds than the specific kernel choice, while the additional benefit of the in/out strategy is case-dependent and modest in the present example. Overall, the proposed framework provides a transparent way to incorporate DIR uncertainty into radiotherapy dose assessment and to study how modelling choices affect propagated dose metrics.

---


### 405. [BSTabDiff: Block-Subunit Diffusion Priors for High-Dimensional Tabular Data Generation](https://arxiv.org/abs/2606.09257)

**<font color=#1a73e8>作者：</font>** Al Zadid Sultan Bin Habib, Md Younus Ahamed, Prashnna Gyawali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-Dimensional Low-Sample Size (HDLSS) tabular domains (e.g., omics) are characterized by $n \ll m$, where $n$ = number of samples, and $m$ = number of features. Such domains often exhibit strong local correlation groups, sparse cross-group dependencies, heavy-tailed non-Gaussian marginals, heteroscedastic noise, and structured missingness, making direct density learning in $\mathbb{R}^m$ ill-conditioned since $n \ll m$. We propose BSTabDiff, a block-subunit generative framework that partitions the $m$ observed features into $M$ latent blocks ($M \ll m$) and generates each block via a shared low-dimensional subunit variable, concentrating global dependence learning in the compact block-latent space $\mathbb{R}^M$ while decoding to the full feature space with copula-driven dependence, flexible per-feature marginals, and explicit missingness mechanisms. BSTabDiff supports modern deep priors on block latents, including diffusion and normalizing flows, enabling stable synthesis and controllable benchmark generation in the HDLSS regime. Empirically, BSTabDiff produces more realistic and stable high-dimensional synthetic data when compared with unstructured tabular generators on HDLSS data.

---


### 406. [Self-supervised Learning Matters: A Simple Ensemble Solution for Micro-Gesture Recognition](https://arxiv.org/abs/2606.09261)

**<font color=#1a73e8>作者：</font>** Tingyi Liu, Kun Li, Fei Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we present XInsight Lab's solution to the micro-gesture classification track of the 4th MiGA Challenge at IJCAI 2026, in which our solution ranked first and achieved a new state-of-the-art result. We propose a multimodal ensemble framework that integrates a self-supervised RGB-based model with supervised multi-stream models from previous solutions. The self-supervised RGB model is pretrained on 120K unlabeled clips via masked video modeling and then fine-tuned on iMiGUE. This simple yet effective RGB baseline achieves 69.224% top-1 accuracy on the iMiGUE test set, demonstrating the benefit of learning transferable representations from unlabeled in-domain videos. By incorporating this model as a complementary branch, the final ensemble reaches 74.419% top-1 accuracy, surpassing the previous state of the art by 1.206 percentage points. Experimental results on iMiGUE, including ablation studies on the ensemble strategy, validate the effectiveness of self-supervised RGB representation learning for micro-gesture recognition.

---


### 407. [See More, Match Better: Multi-Source Feature Fusion for Two-View Correspondence Learning](https://arxiv.org/abs/2606.09262)

**<font color=#1a73e8>作者：</font>** Xiaojie Li, Xin Jiang, Luanyuan Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Two-view correspondence learning aims to distinguish true correspondences (inliers) from false ones (outliers) in image pairs by leveraging their underlying differences. Existing methods mainly rely on coordinate-based geometric consistency. However, they often struggle with pseudo-consistent outliers in scenes containing repetitive structures, textureless regions, or locally similar geometric patterns. To address this limitation, we propose TriMatch, a multi-source feature fusion framework for two-view correspondence learning, which consists of two parts: feature extraction and feature refinement. In feature extraction, TriMatch jointly extracts geometric, texture semantic, and structural semantic features to provide complementary evidence for correspondence discrimination. To bridge the gap between semantic and geometric features, texture and structural semantic features are aligned with geometric features through dedicated Texture-Geometric Alignment and Structural-Geometric Alignment modules, respectively. We further introduce a Semantic-Guided Correspondence Modulation module, which modulates geometric features using semantic information to suppress geometrically plausible but semantically inconsistent correspondences. In feature refinement, a Hierarchical Semantic-Enhanced Correspondence Refinement strategy progressively models correspondence dependencies and recalibrates multi-context feature responses, enabling more reliable inlier-outlier discrimination. Extensive experiments demonstrate the effectiveness, robustness, and generalization capability of TriMatch.

---


### 408. [EditSSC: Toward Editable Semantic Occupancy Scenes with Unconditional Diffusion Models](https://arxiv.org/abs/2606.09273)

**<font color=#1a73e8>作者：</font>** Fatima Balde, Raoul de Charette, Alexandre Boulch  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D semantic scene generation is crucial for autonomous driving applications, yet most methods rely on complex 3D-specific architectures such as triplane encoders and adapted diffusion networks, limiting both their simplicity and their editing capabilities. We propose EditSSC, an editing-ready method for 3D semantic scene generation using 2D Bird's Eye View (BEV) representations and off-the-shelf latent diffusion network. Our approach reshapes 3D semantic occupancy grids into multi-channel BEV images and leverages the quantized autoencoder and UNet from Stable Diffusion with minimal modifications. We perform diffusion on the latents after quantization, which enables training-free editing capabilities. By exploiting class-to-code correspondences in the codebook, our method supports sketch-guided generation, inpainting, and outpainting without any retraining. On SemanticKITTI, EditSSC outperforms existing 3D-specific baselines on unconditional generation, demonstrating that well-established 2D architectures can be effectively repurposed for 3D scene generation and editing.

---


### 409. [ERBench: A Benchmark and Testsuite for Equation Discovery Algorithms](https://arxiv.org/abs/2606.09276)

**<font color=#1a73e8>作者：</font>** Paul Kahlmeyer, Henrik Voigt, Michael Habeck 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equation discovery aims to automate the discovery of scientific models in the form of mathematical equations from data. Technically, equation discovery is implemented by symbolic regression algorithms. Performance of symbolic regression for equation discovery is measured along two dimensions: Prediction accuracy on test data, and recovery of known groundtruth formulas. For standard regression, accuracy is typically measured on in-domain test data, for instance, by splitting a data set randomly into training and test data. While this makes sense for in-domain interpolation, which is the common goal in ordinary regression, it can be a misleading proxy for true model discovery and generalization. The obvious alternative is to measure out-of-domain accuracy. However, obtaining challenging out-of-domain test data is a non-trivial problem. Therefore, we focus on equation recovery for evaluating symbolic regression algorithms for equation discovery. The rationale is that symbolic regression algorithms that perform well in recovering known groundtruth formulas are good candidates to perform well in unknown equation discovery. Existing benchmarks for symbolic regression include equation recovery tasks, however, with only a small number of groundtruth formulas that are publicly known. Moreover, these benchmarks place less emphasis on evaluating the robustness of algorithms in terms of their behavior under changing dimensionality, sampling size, sampling distribution and sampling domain. This, however, is of central importance to practitioners wanting to discover equations for modeling natural phenomena, since data is almost certainly noisy and comes from diverse domains, distributions, and sample sizes. To fill this gap, we introduce the Equation Recovery Benchmark (ERBench), a new evaluation framework designed to rigorously assess algorithms explicitly targeting the task of equation discovery.

---


### 410. [Internalizing Geometric Law: Learning from Solver Residuals for Precision-Critical Generation](https://arxiv.org/abs/2606.09278)

**<font color=#1a73e8>作者：</font>** Rafael Cabral, Pang Zixi, Ziyi Shou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models frequently hallucinate in precision-critical domains such as technical diagramming and mechanical design, where outputs must satisfy strict geometric constraints. We study open-ended geometric synthesis from natural language: translating free-form descriptions into precise constructions whose entities must simultaneously satisfy dozens of interacting constraints. To make this tractable, we release PyGeoX, a programmable geometric DSL that compiles declarative constraints into a differentiable loss, and PyGeoX-Bench, a stratified suite of 300 problems with per-constraint verifiable rewards. Using PyGeoX as a verifier, we identify a failure mode we call Outlier Gradient Masking: under global-norm rewards (any scheme that aggregates residuals through a single norm, for example, $\exp(-\mathrm{MSE})$), a single outlier constraint can nullify the learning signal across all others. To address this, we propose Saturating Additive Rewards (SAR), which decompose the reward into bounded per-constraint terms, preserving partial progress and ensuring consistent gradients even under severe violations. Against MSE-based rewards, the natural baseline for geometry solvers, SAR improves the hard-tier solving rate by $2.3\times$, and the resulting 8B model is competitive with much larger frontier systems on this benchmark. We release the engine, benchmark, and data at this https URL.

---


### 411. [Trajectory Geometry of Transformer Representations Across Layers](https://arxiv.org/abs/2606.09287)

**<font color=#1a73e8>作者：</font>** Vishal Pandey, Gopal Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how transformer representations evolve across layers, not merely what they encode, remains an open problem in mechanistic interpretability. We recast the transformer forward pass as a discrete population trajectory through a high-dimensional representation manifold, drawing on geometric tools from computational neuroscience. Rather than probing for pre-specified features, we characterize trajectory geometry using five metrics computed directly in the ambient space: trajectory length, curvature, a semantic convergence index, layerwise cosine similarity, and representational stability. Across three model families (GPT-2, TinyLlama, Qwen2.5) and five controlled prompt families, we report four findings. First, semantically related prompts converge significantly in middle-to-late layers (peak CI 0.41--0.58, p<0.001, Mann-Whitney U), consistent with attractor-like dynamics. Second, reasoning tasks produce trajectories of greater curvature than lexical variations (0.71--0.83 rad vs. 0.27--0.31 rad), suggesting curvature encodes computational complexity. Third, ambiguous tokens exhibit trajectory bifurcation with up to 5.6x representational separation by the final layer, absent in unambiguous controls. Fourth, layerwise cosine similarity reveals a universal three-phase structure: encoding, elaboration, and output preparation, consistent across all three architectures. All four effects vanish under shuffled-layer and random-embedding controls. We release a fully open-source, model-agnostic pipeline and argue that trajectory geometry constitutes a principled, probe-free lens for mechanistic interpretability.

---


### 412. [Intention Driven Identification of In-Possession Match Phases in Association Football through Temporal Graph Learning](https://arxiv.org/abs/2606.09289)

**<font color=#1a73e8>作者：</font>** Yuesen Li, Daniel Link  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding tactical organisation of association football, hereafter referred to as football, requires identifying distinct match phases. Yet in-possession phases are rarely directly observable and are shaped by evolving tactical intentions, rather than spatial patterns alone. This study proposes a data-driven framework for identifying in-possession match phases from spatiotemporal tracking data. Seven German Bundesliga matches recorded at 25 Hz with TRACAB were analysed. A hierarchical phase model was defined with three tactical intentions (Invade Opponent Space, Keep Possession, Scoring) and six phases (Build Up, Progression, Counter Attack, Maintenance, Sustained Threat, Finishing). A Temporal Graph Attention Network (T-GAN) was developed to combine frame-level player-interaction graphs, contextual features, and Transformer-based temporal modelling. Performance was evaluated using frame-level F1 and a sequence-aware Intersection over Truth-Dominance (IoT-D) metric. T-GAN achieved macro-average frame-level F1 scores of 0.87 at the intention level, 0.76 for invasion-related phases, and 0.79 for scoring phases. At the sequence level, mean diagonal IoT-D F1 increased from 0.68 to 0.79 for intentions and from 0.61 to 0.71 for phases after post-processing, indicating improved temporal coherence. Model comparisons showed that sequence modelling was the main driver of segmentation quality, while graph-based relational modelling was particularly beneficial for Counter Attack recognition. Exploratory player attention analysis further suggested that wide and midfield positional groups contributed strongly to phase discrimination. Overall, the framework translates continuous tracking data into tactically interpretable in-possession phase representations, with potential applications in automated match annotation, tactical analysis, and playing-style profiling.

---


### 413. [Visual Para-Thinker++: A Single-Policy Multi-Agent Framework for Visual Reasoning](https://arxiv.org/abs/2606.09290)

**<font color=#1a73e8>作者：</font>** Haoran Xu, Hongyu Wang, Yifei Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual reasoning requires integrating evidence distributed across regions, attributes, and relations, making single-chain reasoning prone to early perceptual commitment and hallucination. We propose Visual Para-Thinker++, a single-policy multi-agent framework in which one shared MLLM policy is instantiated as role-conditioned Main, Worker, and Summary Agents. The Main Agent decomposes the task with fixed allocation patterns; Worker Agents reason in parallel under context isolation; and the Summary Agent reconciles full Worker reasoning traces rather than majority-voting on final labels. The shared policy is trained by Multi-Agent Capability Injection and Role-Decoupled Multi-Agent Optimization, which assign role-specific rewards and advantages to corresponding token segments to reduce gradient conflict among collaborative roles. A native inference engine enables efficient multi-agent rollout through shared visual prefix and KV cache reuse. Across V*, CountBench, the RefCOCO family, and HallusionBench, Visual Para-Thinker++ consistently outperforms single-trajectory and inference-time parallel baselines, with especially strong gains on hallucination-sensitive visual reasoning.

---


### 414. [One Model, Multiple Goals: Adaptive Multi-Objective Learning for E-commerce Dialogue Systems](https://arxiv.org/abs/2606.09293)

**<font color=#1a73e8>作者：</font>** Mingzhe Li, Jing Xiang, Enguo Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dialogue systems in e-commerce scenarios often need to satisfy multiple objectives: accurately reasoning over user profiles (e.g., eligibility, credit limit) to ensure correct decision-making and user state interpretation, while also generating natural and faithful responses. These goals are complementary but not identical. In this work, we propose MORE, an adaptive Multi-Objective REinforcement learning framework that jointly optimizes reasoning accuracy and linguistic naturalness. Our preliminary experiments show that directly mixing rewards with diverging optimization dynamics can cause oscillations and unstable learning. Thus, instead of optimizing a single mixed reward, we treat reasoning functions as constraints that guide policy optimization. At inference time, the system directly generates responses without explicit reasoning steps, while still benefiting from reasoning-enhanced scaffold and avoiding additional inference overhead. To better balance linguistic objectives during response generation, we introduce an adaptive multi-reward mechanism that aggregates signals such as fluency and naturalness and dynamically reweighs them via gradient feedback. We evaluate MORE on two real-world dialogue systems at ByteDance and the MultiWOZ 2.2 benchmark, where it consistently outperforms strong baselines. In 14-day online experiments on ByteDance production traffic, MORE improves overall and reached conversion by 16.53% and 30.09%, while increasing user satisfaction and reducing handoff rates. Notably, in a human-machine comparison, MORE recovers about 60% of the incremental conversion lift achieved by human agents.

---


### 415. [Virtual-point-based Solutions to Handle Generalized Absolute Pose Problem](https://arxiv.org/abs/2606.09294)

**<font color=#1a73e8>作者：</font>** Bin Li, Banglei Guan, Shunkun Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-camera systems are increasingly adopted in robotics and autonomous navigation for their wide field of view, flexibility, and fault tolerance. Nevertheless, existing PnP solvers fail to handle multiple projection centers. This paper introduces a virtual point formulation that bridges the standard PnP and generalized pose problems, enabling a unified pipeline that transforms existing PnP solvers into generalized pose solvers. Based on this framework, we derive three Virtual-point-based Generalized Pose solvers, namely VGPc, VGPq, and VGPr, leveraging Cayley, quaternion, and rotation-matrix parameterizations, respectively. Extensive experiments demonstrate that the proposed solvers inherit the accuracy and efficiency of original PnP algorithms while significantly outperforming existing generalized solvers. Specifically, VGPc achieves higher estimation accuracy under heteroscedastic noise conditions, VGPq maintains global optimality, whereas VGPr provides superior computational efficiency without accuracy degradation.

---


### 416. [NüshuVoice: Reviving the Voice of Endangered Nüshu with Pitch-Aware Text-to-Speech](https://arxiv.org/abs/2606.09295)

**<font color=#1a73e8>作者：</font>** Hongkun Yang, Xinhui Yi, Xiyan Zhao 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Nüshu is an endangered phonetic script historically used by women in Jiangyong County, southern Hunan, China. While existing computational studies of Nüshu mainly focus on textual digitization and visual recognition, the acoustic reconstruction of its authentic pronunciation remains largely unexplored. Building a Nüshu text-to-speech (TTS) system is particularly challenging because available recordings are extremely limited and mostly consist of isolated syllable-level pronunciations rather than natural sentence-level utterances. In this work, we introduce NüshuVoice, the first TTS benchmark for Nüshu. We construct a sentence-level Nüshu text-to-audio dataset that aligns standardized Unicode Nüshu text, phonetic transcriptions, standard Chinese translations, and archival recordings. To synthesize speech under this extreme low-resource setting, we propose Nüshu-PitchVITS, an F0-conditioned VITS framework that leverages Nüshu's five-level pitch notation as an explicit prosodic inductive bias. Experimental results show that Nüshu-PitchVITS outperforms strong TTS baselines in spectral fidelity, pitch reconstruction, and human-rated intelligibility. We publicly release the dataset and code at: this https URL.

---


### 417. [PRISM: Topology-Aware Cross-Modal Imputation for Modality-Deficient Federated Graph Learning](https://arxiv.org/abs/2606.09301)

**<font color=#1a73e8>作者：</font>** Zekai Chen, Miao Zhang, Jiayang Xing 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal federated graph learning (MM-FGL) aims to collaboratively learn from decentralized graphs with text and images. However, real-world clients may not share a common modality basis: a visual-search client may contain image--interaction graphs but no seller descriptions, while a catalog client may provide text but no product images. We refer to this practical setting as client-level modality deficiency. Unlike random instance-wise missingness, a deficient client lacks the local semantic basis needed to reconstruct the absent modality. More importantly, in graph learning, incomplete representations initialize message passing, so imputation errors can be filtered, mixed, and amplified by the receiving topology. To address this gap, we propose \textbf{PRISM} (\textbf{P}roactive \textbf{R}etrieval and \textbf{I}mputation via \textbf{S}tructural \textbf{M}eta-prompting), a topology-aware federated cross-modal imputation framework. Rather than reconstructing the missing modality solely from local observations, PRISM recovers missing-modality semantics from the federation and introduces them into local graph propagation under topology-aware control. Experiments on six multimodal graph datasets across graph-centric and modality-centric tasks show that PRISM consistently improves modality-deficient clients, outperforming state-of-the-art baselines by \textbf{4.48}\% on average.

---


### 418. [SG-OPD: Sign-Gated On-Policy Distillation via Sign-Consistency Gating and Phased Teacher Sampling](https://arxiv.org/abs/2606.09304)

**<font color=#1a73e8>作者：</font>** Haoran Xu, Hongyu Wang, Yifei Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own trajectories with dense per-token supervision from a stronger teacher, and often outperforms off-policy distillation and standard reinforcement learning. However, we find that its effectiveness implicitly relies on two assumptions that frequently break in practice: trajectory-level alignment between the student and the teacher, and uniform token-level reliability of the teacher's preferences. We therefore propose Sign-Gated On-Policy Distillation (SG-OPD), which uses a binary verifier as a trust signal for the teacher at two complementary granularities: phased teacher sampling mixes in verifier-endorsed teacher rollouts at cold-start, and a sign-consistency gate extrapolates the distillation update on tokens where the teacher agrees with the verifier-correct direction and interpolates it where it disagrees. Experiments on competition-level mathematical reasoning benchmarks show that SG-OPD consistently outperforms standard OPD, with average gains of 1.98 and 7.50 at the per-sample and per-question levels, respectively.

---


### 419. [Machine-Learning Emulation of Satellite Greenhouse Gas Retrievals: Stability over Time](https://arxiv.org/abs/2606.09313)

**<font color=#1a73e8>作者：</font>** Nugzar Gognadze, Motonobu Kanagawa, Yu Someya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval algorithms are used to estimate atmospheric concentrations of greenhouse gases (GHGs), such as carbon dioxide (CO2) and methane (CH4), by solving inverse problems from high-spectral-resolution satellite radiance measurements. However, these algorithms are computationally expensive, which makes real-time estimation at scale difficult. Machine-learning models have therefore been proposed as fast emulators of retrieval algorithms. Most existing studies, however, evaluate them only on test data from the same period as the training data.
We study the stability over time of such emulators using data from the Greenhouse Gases Observing SATellite (GOSAT). We show that prediction accuracy generally deteriorates when the test period moves away from the training period. We also show that including time as an input feature substantially improves XCH4 prediction for Lasso and neural-network models. Among the methods considered, a simple Lasso model performs as well as or better than more complex methods such as neural networks, and yields more stable predictions over time. We further validate the results using the Total Carbon Column Observing Network (TCCON), a ground-based observation network. On the TCCON-matched dataset, the time-augmented Lasso achieves errors against TCCON that are comparable to the disagreement between GOSAT and TCCON for both XCO2 and XCH4.

---


### 420. [Anything2Skill: Compiling External Knowledge into Reusable Skills for Agents](https://arxiv.org/abs/2606.09316)

**<font color=#1a73e8>作者：</font>** Qianjun Pan, Yutao Yang, Junsong Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) enables agents to access external knowledge at inference time, but it primarily retrieves fragmented declarative evidence, leaving agents to repeatedly infer task procedures from passages, manuals, examples, logs, or trajectories. This raises a fundamental question: can skills extracted from external knowledge bases be installed into an agent, enabling it to rapidly approximate domain expertise? In this paper, we propose Anything2Skill, a taxonomy-guided framework that compiles heterogeneous external knowledge into reusable, retrievable, and executable skills for agents. Given a corpus of knowledge records, \textsc{Anything2Skill} first decomposes each record into evidence windows and performs plan-and-expand skill extraction under a skill-tree prior. The extracted candidates are then converted into structured skill contracts that specify invocation conditions, contraindications, action moves, workflow steps, constraints, output specifications, supporting evidence, and confidence scores. To construct a deployable procedural memory, Anything2Skill manages the extracted skills in a persistent SkillBank through taxonomy-aware compilation, registry-level reconciliation, lifecycle tracking, versioned updates, and visible skill-tree projection. At inference time, agents retrieve both task-specific passages from the original knowledge base and relevant procedural skills from the SkillBank, allowing RAG to provide declarative evidence while compiled skills provide reusable procedural guidance. Experiments on qsv and GitHub-CLI show that Anything2Skill combined with RAG achieves 98.85\% and 94.10\% success rates, respectively, substantially outperforming RAG-only agents. These results suggest that compiling latent procedural knowledge into explicit skills is an effective way to extend retrieval-augmented agents from knowledge access toward capability reuse.

---


### 421. [TRL-Bench: Standardizing Cross-Paradigm Representation-Level Evaluation of Tabular Encoders](https://arxiv.org/abs/2606.09323)

**<font color=#1a73e8>作者：</font>** Wei Pang, Xiangru Jian, Hehan Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tabular encoders are usually evaluated inside task-specific end-to-end pipelines, so models from different training paradigms are difficult to compare directly even when they operate on similar tabular signals. We introduce TRL-Bench, a multi-granular tabular representation learning (TRL) benchmark that standardizes cross-paradigm representation-level evaluation: each encoder exports row-, column-, or table embeddings through its supported wrapper, and shared lightweight heads probe them across three suites: TRL-CTbench (column/table), TRL-Rbench (row), and TRL-DLTE (compositional Data-Lake Table Enrichment spanning all three granularities). To support this standardized setting, we release curated benchmark assets and task reformulations, including 50 OpenML tables with 123 verified targets, 16 row-pair linkage rewrites, and a 47,772-table DLTE lake derived from 1,379 parent tables. Across 20 models and 16 tasks, TRL-Bench shows that once downstream conditions are standardized, encoder quality is capability-specific rather than captured by a single leaderboard. In TRL-CTbench, generic text encoders often lead on tasks with strong surface-text signal, while tabular specialists win where their pretraining objective aligns with the task. In TRL-Rbench, within-table prediction and cross-table linkage favor different training regimes, with atomic linkage performance correlating strongly with the row-matching stage of DLTE pipelines. In TRL-DLTE, the strongest pipelines combine capability-matched specialists rather than reuse a single encoder, and top end-to-end quality depends on non-additive compositional fit rather than per-stage marginal rank alone. TRL-Bench provides a common protocol for measuring reusable signal in exported tabular representations under shared downstream conditions. Code and data: this https URL

---


### 422. [A Universal Dense Football Event Representation Based on TabTransformer](https://arxiv.org/abs/2606.09327)

**<font color=#1a73e8>作者：</font>** Weiran Yang, Daniel Memmert, Maximilian Klemp-Weins  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Football event data constitute a rich spatiotemporal source for quantitative analysis of player actions in team sports. These datasets contain heterogeneous features, combining continuous location coordinates with categorical variables such as action type, action outcome, and body part. Such data have been applied in sports analytics for match outcome forecasting, player evaluation, and tactical pattern recognition. However, existing approaches predominantly encode categorical features using one-hot or ordinal embedding representations, overlooking the intrinsic semantics of action descriptors. The Transformer is a deep neural network architecture based on self-attention that captures dependencies between input features at arbitrary positions. We propose and implement a Transformer-based model to learn latent dependencies among categorical event features and produce dense representations of football events. By encoding categorical features as learned embedding vectors, sport-specific action semantics are captured during pretraining, enabling the representations to support downstream tasks such as action value estimation and play style recognition. Empirical evaluation shows that the embedding representations yield superior probability calibration over task-specific baselines on the downstream prediction tasks, as measured by Brier score.

---


### 423. [Multi-Hop Knowledge Composition is Bound by Pretraining Exposure](https://arxiv.org/abs/2606.09338)

**<font color=#1a73e8>作者：</font>** Yannis Karmim, Luis Marti, Djamé Seddah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models fail at implicit multi-hop reasoning: a model answers "When was $X$ born?" and "Who is $Y$'s closest friend?" correctly but fails on "When was $Y$'s closest friend born?" in a single forward pass, even when both facts are perfectly memorized and individually retrievable. We study this failure in a controlled natural language setting with a strict separation between individuals exposed to compositional contexts during pretraining and those that never appear in any such context. We confirm that compositional failure persists even at 97% 1-hop accuracy, establishing the gap as a pretraining failure rather than a knowledge absence. We propose and test nine data-centric augmentation formats and find that compositional pretraining transfers to unseen questions for exposed individuals, but never to individuals absent from compositional pretraining, suggesting that exposure to compositional contexts during pretraining is a necessary condition for implicit multi-hop reasoning.

---


### 424. [Thresholded Local Hyper-Flow Diffusion](https://arxiv.org/abs/2606.09340)

**<font color=#1a73e8>作者：</font>** Meher Chaitanya, Sebastian Dalleiger, Luana Ruiz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Local Hyper-Flow Diffusion (HFD) gives an edge-size-independent Cheeger-type guarantee for seeded clustering in general submodular hypergraphs, but existing HFD solvers do not keep intermediate computation local at every iteration. We introduce Thresholded Local HFD (TL-HFD), a first-order method that maintains an active region around the seeds, performs projected subgradient updates on that region and its immediate boundary, and expands via thresholded (top-k) boundary activation. We prove that the local update is exact: the degree-preconditioned projected subgradient step restricted to the active region and its boundary coincides with the unrestricted global update. We establish finite-time dual suboptimality for both exact and thresholded updates, treating the latter as inexact projected subgradient steps with explicit skipped-boundary error. We further derive an additive activated-volume bound controlled by realized local subgradient norms and the minimum boundary-push among newly activated vertices, and translate approximate dual optimality with localized support into a robust sweep-cut guarantee for early-stopped iterates. For general submodular cut-costs, each iteration is local in the scanned region and oracle-sensitive in the hyperedge primitive. Empirically, TL-HFD often matches or improves over HFD while activating less volume, with the largest gains on noisy instances where diffusion tends to absorb non-target vertices.

---


### 425. [IB-HFN: Information Bottleneck-Driven SAR-Optical Fusion Network for High-Fidelity Cloud Removal](https://arxiv.org/abs/2606.09347)

**<font color=#1a73e8>作者：</font>** Haojun Guo, Fan Feng, Ziquan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic aperture radar (SAR)-assisted optical cloud removal aims to recover surface information obscured by clouds in optical remote sensing images by exploiting complementary SAR observations. Existing multimodal fusion methods typically rely on direct spatial concatenation and pixel-wise supervision, which can propagate SAR speckle noise into optical reconstruction and lead to over-smoothed results. To address these limitations, we propose an Information Bottleneck-driven High-Fidelity Network (IB-HFN) for SAR-assisted optical cloud removal. IB-HFN employs a dual-stream backbone to preserve modality-specific representations before deep semantic fusion, thereby mitigating premature cross-modal contamination. At the fusion stage, we introduce a Spatial Information Bottleneck Fusion module that compresses SAR features through a channel-wise variational information bottleneck to suppress unstructured speckle noise. In parallel, a local-global gating mechanism predicts clear-sky regions and routes reliable optical details through a Dirac-initialized skip connection, decoupling noise suppression from texture preservation. We further develop a joint optimization strategy that integrates feature-level bottleneck regularization with image-level constraints on reconstruction accuracy, structural consistency, spectral fidelity, and contrastive sharpness. A dynamic weighting schedule balances these objectives to stabilize training and reduce hazy artifacts. Experiments on the SEN12MS-CR dataset under challenging spatio-temporal splits demonstrate that IB-HFN achieves superior structural preservation and spectral fidelity over existing methods.

---


### 426. [PBSD: Privileged Bayesian Self-Distillation for Long-Horizon Credit Assignment](https://arxiv.org/abs/2606.09348)

**<font color=#1a73e8>作者：</font>** Yang Tian, Rui Wang, Xumeng Wen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon agentic tasks pose a fundamental credit assignment challenge for outcome-base reinforcement learning: trajectory-level rewards verify final correctness but provide limited guidance on which intermediate reasoning steps or tool interactions contribute to the outcome. The difficulty is especially pronounced in multi-turn search agents, where successful trajectories may contain misleading actions and failed trajectories may contain valuable evidence-gathering steps. We propose PBSD (Privileged Bayesian Self-Distillation), a Bayes-calibrated self-distillation method for fine-grained credit assignment under sparse final rewards. PBSD measures trajectory quality through the posterior-to-prior probability ratio of the verified answer and applies Bayes' rule to convert this hard-to-estimate answer-side ratio into a tractable likelihood ratio between a standard student model and a privileged answer-conditioned teacher model. Autoregressive decomposition of this Bayesian evidence score yields turn-level signals that identify whether each intermediate turn supports or undermines the verified outcome. Consequently, PBSD provides a principled and elegant reweighting scheme that transforms sparse outcome supervision into Bayes-calibrated turn-level credit signals, while remaining fully compatible with standard policy optimization. Experiments demonstrate that PBSD consistently enhances performance across both in-domain and out-of-domain settings, and effectively transfers knowledge from short-context training to long-context inference, suggesting that its fine-grained credit assignment mechanism facilitates more effective policy learning and yields improved generalization.

---


### 427. [Beyond Humans: Multispecies Animal Face Recognition Using Transfer Learning](https://arxiv.org/abs/2606.09353)

**<font color=#1a73e8>作者：</font>** Maria De Marsico, Anil K. Jain, Annalaura Miglino  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Individual animal recognition can be useful in the search for lost or stolen pets, the tracking of individuals of endangered species, and the recognition of animals in crowded farms. Present recognition techniques mostly use physical devices, e.g., microchips, often impractical and difficult to apply. These could be replaced by remote recognition via the animal's face; if accurate enough, it provides several advantages: it is non-invasive, can work at a distance, and is difficult to counterfeit, as, for instance, in the case of substituting sick animals for healthy ones in the food industry. The few existing datasets with sufficient per-subject images annotated with a single animal identity are not large enough to train current deep learning architectures. We rather investigate the possibility of transfer learning, exploiting pre-trained network models as backbones. Our experiments compared FaceNet, which is specifically trained on large databases of human faces, with the Vision Transformer (ViT) pre-trained on ImageNet, i.e., on object categories. We used three face datasets of very different animals: dogs, primates (lemurs, golden monkeys, and chimpanzees), and cattle. We report the results and, for each dataset, compare them with the state of the art (SOTA) ad hoc-trained deep networks. The capture conditions differ among the three datasets. Image quality (resolution, motion blur, diverse poses, etc.) decreases from dogs to cattle to primates. The best performance was achieved with dogs, where ViT reached a mean verification accuracy of 96.85% and a Rank-1 Identification Rate of 84.34%. The results for endangered primates are still encouraging, but performance varies across animal classes and tasks (verification or identification), and does not always outperform SOTA. For cattle, the ViT results outperform SOTA, while FaceNet is still competitive.

---


### 428. [ExDet: Open-Domain Open-Vocabulary Detection with Cross-modal Extrapolation and Rectification](https://arxiv.org/abs/2606.09360)

**<font color=#1a73e8>作者：</font>** Yupeng Zhang, Yuzhong Feng, Ruize Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-domain open-vocabulary detection (ODOVD) requires detectors to generalize to both novel categories and unseen domains, making it more challenging than open-vocabulary detection. Existing methods typically train open-vocabulary detectors together with domain generalization modules from scratch, leading to high training cost. we propose ExDet, a lightweight category-domain collaborative generalization framework for ODOVD that enhances the cross-category and cross-domain generalization of existing detectors. ExDet consists of Text-Guided Extrapolation (TGE), a lightweight Detector-Compatible Rectification (DCR) module, and ExRPN. Specifically, TGE exploits the DeltaSpace property of vision-language models (VLMs) to infer category- and domain-aware proxy visual prototypes from text. DCR is learned from the TGE-generated prototypes in a detector training-free and real-data-free manner, and is inserted after the classification head at inference to rectify representations toward a detector-compatible source-domain visual distribution, thereby enhancing classification for targets from novel categories and unseen domains. ExRPN recalibrates proposal scores by combining semantic similarity with RPN confidence, improving recall for novel and domain-shifted objects while providing better support for subsequent classification and DCR. ExDet achieves SOTA performance on OD-LVIS, OV-LVIS, Objects365, and MSOSB.

---


### 429. [Zero-Shot Semantic Re-Identification for Autonomous Driving: A VLM Baseline Study](https://arxiv.org/abs/2606.09362)

**<font color=#1a73e8>作者：</font>** Eduardo Borges, Manuel Abreu, Luís Garrote 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Re-Identification (ReID) in autonomous driving is typically formulated as a visual matching problem, where observations of vehicles, pedestrians, and cyclists are associated across time, frames, or camera views using learned appearance embeddings, often complemented by motion, geometric, or multimodal cues. However, purely visual representations may be sensitive to viewpoint, occlusion, illumination, and sensor-domain variations, limiting their interpretability and robustness in complex driving scenes. We propose a baseline study of a zero-shot pipeline using Vision-Language Models (VLMs) to generate textual descriptions of detected traffic participants and evaluate whether these descriptions can support identity matching across observations. Instead of relying only on low-level visual similarity, the proposed formulation represents each object through structured semantic attributes, including category, color, shape, pose, visible parts, spatial context, and distinctive visual cues. This study provides an initial benchmark for language-based re-identification in autonomous-driving scenarios, discussing and evaluating the strengths and limitations of current VLMs for this task. Results demonstrate that zero-shot semantic descriptions can support effective object re-identification, achieving retrieval performance comparable to a supervised CNN baseline while offering greater interpretability through explicit identity cues. However, the experiments also reveal important challenges, including attribute inconsistency across viewpoints and limited fine-grained discrimination between visually similar instances.

---


### 430. [Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory](https://arxiv.org/abs/2606.09365)

**<font color=#1a73e8>作者：</font>** Haoran Sun, Wenjie Li, Yujie Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical agent systems are increasingly expected to support interactive clinical decision making rather than only static question answering. In such settings, effective agents must reuse prior experience across evolving cases, yet existing memory mechanisms often retain raw historical traces that are redundant, noisy, and difficult to govern. More importantly, they rarely distinguish which memories are truly useful for future reasoning. This limits their ability to accumulate compact and reliable experience for long-horizon clinical reasoning. To close this gap, we propose SkeMex, a post-deployment self-evolution framework that improves medical agents through a skill-based memory without updating model weights. SkeMex distills informative interaction trajectories into structured skills that encode reusable procedural knowledge, and organizes them into a multi-branch repository spanning general, task-specific, and action-level experience. To determine which memories should be reused and retained, SkeMex estimates context-dependent utility from environment feedback and uses it to guide value-aware retrieval and repository governance. A closed-loop ``Read--Write--Assess--Govern" lifecycle further supports continual evolution by writing new skills, updating utilities, promoting useful memories, and removing harmful entries. Experiments across diverse clinical tasks show that SkeMex consistently outperforms representative memory-based agents in both offline and online settings. It also generalizes across model backbones and supports transferable skill memory. All data and code will be released publicly.

---


### 431. [RT-SDGOD: Real-Time Single-Domain Generalized Object Detection](https://arxiv.org/abs/2606.09367)

**<font color=#1a73e8>作者：</font>** Yupeng Zhang, Fangzhuo Gao, Ruize Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real-world deployment under strict real-time constraints, weather and imaging variations induce significant distribution shifts, severely degrading detectors. Single-Domain Generalized Object Detection aims to mitigate this issue, yet existing methods rarely investigate-at the level of problem formulation-the generalization capability of real-time detectors under such constrained inference budgets. To this end, we introduce Real-Time Single-Domain Generalized Object Detection (RT-SDGOD), which focuses on how real-time detectors can achieve cross-domain generalization under zero extra inference overhead by relying solely on training-time representation learning. We observe that, under domain shift, DETR-based real-time detectors mainly degrade through increased missed detections, rooted in limited and unstable object-level discriminative evidence. Based on this, we propose RT-SDGDet, a multi-evidence collaborative modeling framework for RT-SDGOD. The core idea is to enable multiple queries of the same object to collaboratively cover more sufficient discriminative evidence while maintaining the stability of such evidence modeling across views. Specifically, we use one-to-many (O2M) supervision to construct stable object-specific query groups, and further design Discriminative Evidence Diversity Learning (DEDL) and Dual-view Evidence Consistency Learning (DvECL) to expand object-level evidence coverage and improve evidence stability under appearance perturbations, respectively. Since all components are introduced only during training, our method incurs no extra inference overhead. Extensive experiments show that the proposed method achieves better generalization performance than existing approaches across multiple unseen target domains.

---


### 432. [PhysScene: A Scene Graph Dataset for Scientific Visual Reasoning in Physics Experiments](https://arxiv.org/abs/2606.09368)

**<font color=#1a73e8>作者：</font>** Minghao Zou, Qingtian Zeng, Shangkun Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene Graphs (SGs) provide structured representations of visual scenes by modeling objects and their pairwise relationships. Despite recent progress, existing datasets primarily focus on generic natural contexts, leaving domain-specific and function-oriented scenes largely underexplored. This limitation restricts the evaluation of relational reasoning in scientific experimental scenes, thereby hindering the development of intelligent monitoring, analysis, and related applications in such scenes. To address this gap, we introduce PhysScene, the first SG dataset tailored to physics experiments. PhysScene encompasses specialized instruments, structured experimental setups, and functional relations intrinsic to experimental environments, enabling reasoning that extends beyond spatial co-occurrence to logical dependencies. Rather than pursuing large data scale, PhysScene focuses on strong semantic constraints and high relation density in experimental scenes, posing new challenges for existing scene parsing algorithms while offering opportunities for further improvements. Extensive analyses and experiments show that PhysScene complements existing benchmarks and establishes a valuable testbed for advancing scientific visual reasoning. The dataset is publicly available at this https URL.

---


### 433. [Scaling Neural Network Verification with Tensor Parallelism and Fully Sharded Data Parallelism](https://arxiv.org/abs/2606.09377)

**<font color=#1a73e8>作者：</font>** Sergei Vorobyov, Eugene Ilyushin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Formal neural network verification -- proving that a network satisfies safety properties for \emph{all} inputs in a specified domain -- is bounded in practice by GPU memory: standard implementations of bound-propagation algorithms (IBP, CROWN, $\alpha$-CROWN) require weight and relaxation-coefficient matrices to reside entirely on one accelerator. We adapt two parallelism techniques originally developed for large-scale model training to the \texttt{auto\_LiRPA}\,/\,$\alpha,\beta$-CROWN verification framework. \textbf{Tensor Parallelism (TP)} shards both weight and $A$-matrices across GPUs, achieving ${\approx}2\times$ peak-memory reduction at $P{=}2$; soundness is confirmed on VNN-COMP 2022 MNIST-FC benchmarks, though bound tightness degrades with the number of sharded zones due to forced IBP substitution for intermediate bounds inside sharded zones. \textbf{Fully Sharded Data Parallelism (FSDP)} shards only weight matrices with a per-layer \texttt{AllGather}, producing bounds that are \emph{bitwise identical} to the single-GPU baseline: baseline memory drops by 80--90\%, peak memory by 34--39\% on wide MLPs. FSDP integrates cleanly with complete verification ($\beta$-CROWN + Branch-and-Bound) and with convolutional layers (\texttt{BoundConv}); a complete \emph{unsat} result is obtained for CIFAR-100 ResNet-large (VNN-COMP 2024) under FSDP. Across all experiments the memory bottleneck in $\alpha$-CROWN+BaB mode proves to be per-neuron alpha tensors, not weight matrices, pointing to the key direction for future work.

---


### 434. [Echo-DM: Ultrasound Marker Removal via Conditional Latent Diffusion and Region-Aware Fusion](https://arxiv.org/abs/2606.09378)

**<font color=#1a73e8>作者：</font>** Zhiwei Wang, Tao Huang, Wentao Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical ultrasound images often contain artificial markers, such as measurement calipers and text, to assist diagnostic interpretation and comparison. However, these markers can introduce shortcut bias in downstream automated analysis, encouraging deep learning models to rely on marker-related cues rather than clinically meaningful anatomy. Existing marker removal methods are either mask-dependent and vulnerable to error propagation, or mask-free deterministic restorers that may over-smooth ultrasound texture and perturb unaffected background regions. To address these challenges, we present Echo-DM, a framework for ultrasound marker removal via conditional latent diffusion and region-aware fusion. Echo-DM follows a common encoder-diffusion-decoder pipeline, where a DiT-based conditional latent diffusion network performs global restoration and a region-aware fusion module enforces preservation-aware image-space refinement under end-to-end mask-free inference. Building on this fixed core design, we further instantiate Echo-DM-V and Echo-DM-R with VAE-based and RAE-based latent modules, respectively, which demonstrates that the Echo-DM architecture is compatible with diverse latent-module instantiations. Extensive experiments on Echo-PAIR, a large-scale paired clinical ultrasound dataset, demonstrate superior marker removal and strong anatomical fidelity compared with representative two-stage baselines, while providing favorable quality--efficiency trade-offs across deployment settings. Data, code and models will be released at this https URL.

---


### 435. [Reasoning Arena: Trace Tournaments When Verifiable Rewards Fall Short](https://arxiv.org/abs/2606.09380)

**<font color=#1a73e8>作者：</font>** Han Zhou, Adam X. Yang, Laurence Aitchison 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a leading paradigm for improving the reasoning ability of large language models through outcome-based supervision. However, verifiable rewards frequently become uninformative at the group level: when all sampled traces of a given prompt receive identical rewards, group-relative advantage estimation provides no gradient signal, even though the traces may differ substantially in reasoning quality. We propose Reasoning Arena, an adaptive training framework that routes such non-diverse reward groups to a judge system instead of discarding them. Beyond examining the final answer, Reasoning Arena constructs trace tournaments, where reasoning traces are compared head-to-head to expose finer-grained preferences within the group, converting reasoning quality into rich relative reward signals. To make reward estimation efficient, rather than exhaustively comparing every pair, each new trace is evaluated against a small, dynamically updated pool of previously generated traces as anchors to efficiently establish a relative ranking. We then fit a Bradley-Terry model on the incomplete comparison graph, enabling scalable RL integration without quadratic pairwise comparisons. Empirical results demonstrate that Reasoning Arena consistently outperforms the RLVR baseline by 7.6% on average in competition mathematics and coding benchmarks. By converting otherwise wasted zero-advantage samples into useful gradient updates, our method accelerates training by 27% to 41%, saving nearly 50% of generation compute, and substantially improves overall reasoning performance.

---


### 436. [An Opticalmechanics Framework for Dynamic Estimation of Multibody Systems](https://arxiv.org/abs/2606.09383)

**<font color=#1a73e8>作者：</font>** Banglei Guan, Xuanyu Bai, Qingquan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional dynamics analysis of the human body is often constrained by the need for contact force and torque sensors and controlled laboratory environments. To address this issue, this study proposes an opticalmechanics kinematic-dynamic integrated estimation framework for multibody systems. Specifically, a constrained multibody model is established to describe the system dynamics, while image-measured kinematic quantities are used as non contact inputs for dynamic estimation. The unknown joint torque is then identified through a genetic-algorithm based optimization by minimizing the discrepancy between model-predicted and image-measured kinematic quan tities. Experimental validation on an air-bearing platform showed that the wrist joint torque estimated from image data achieved a mean absolute error of 0.46 Nm compared with sensor measurements. In the forward prediction test, the model-predicted angular velocity achieved a mean absolute error of 0.006 rad/s relative to the image-measured results. This study demonstrates the potential of combining image measurement and mechanical modeling for non-contact dynamic estimation in scenarios where direct force and torque measurement is difficult.

---


### 437. [LexRubric: A Rubric-Guided Diagnostic Benchmark for Open-Ended Legal Tasks](https://arxiv.org/abs/2606.09389)

**<font color=#1a73e8>作者：</font>** Yifan Chen, Haitao Li, Yiran Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly applied to real-world legal tasks, evaluating the reliability of their open-ended legal responses has become essential. These tasks require context-sensitive answers and allow little room for error, motivating fine-grained and diagnostic evaluation that can identify specific sources of response quality failures. We introduce LexRubric, a rubric-based benchmark for evaluating open-ended Chinese legal tasks. LexRubric contains 649 instances from legal consultation and judicial examination, which reflect both everyday legal needs and professional legal reasoning and cover 14 legal scenarios. It further includes 12,337 expert-written atomic scoring criteria organized under a unified six-dimensional framework, enabling accurate evaluation and diagnostic analysis across tasks and evaluation dimensions. To validate the reliability of the evaluation, we test multiple judge models and compare model-based judgments with human judgments. We further evaluate 18 recent general and legal-domain LLMs on LexRubric. Results show that different models exhibit distinct capability profiles, and that open-ended legal question remains challenging for current LLMs. Data is available at: this https URL.

---


### 438. [Real-time body pose non-verbal communication with a consistency-based reliability measure](https://arxiv.org/abs/2606.09390)

**<font color=#1a73e8>作者：</font>** Alina Marcu, Dragos Costea, Cristina Lazar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Body movement communicates intent at distances and in conditions where neither the face, nor speech can be captured. We study the recognition of communicative intent from 2D body pose alone. We argue that body motion is a reliable signal especially in scenarios that require real time low-cost on-device person-to-robot communication in long distance environments, such as rescue missions. However, existing resources do not isolate this signal. Affective corpora combine body, face, voice and text, while skeleton action-recognition benchmarks label the action performed rather than the message conveyed. We release a dataset of real frames of full-body pose covering ten communicative intents and we compare it against other real (IPC) and synthetic (MotionLCM, VEO3.1, Kimodo) ones that span a range of difficulty. We target systems that can run on a robot's limited onboard hardware. We benchmark multiple models, from skeleton graph classifiers to joint motion-forecasting networks, and report performance metrics together with frame rate on an embedded GPU (NVIDIA Orin~Nano), since speed matters as much as accuracy in our scenario. Finally, we show that a model's own autoregressive self-consistency works as an unsupervised reliability signal. We give a short proof that bounds the probability that a self-consistent prediction is correct, show that this probability grows with the number of consistent steps, and identify the conditions under which a confident prediction can still be false, benchmarked against industry-standard metrics.

---


### 439. [From Coarse to Fine: Managing Temporal Granularity in Spatio-Temporal Data for Fine-Grained Traffic Prediction](https://arxiv.org/abs/2606.09392)

**<font color=#1a73e8>作者：</font>** Shuhao Li, Weidong Yang, Yue Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient acquisition, storage, and utilization of traffic data are critical challenges in spatio-temporal data management. Most traffic data systems collect and store observations at fixed, coarse-grained temporal intervals to reduce storage and computation costs. However, such coarse-grained data severely limits downstream applications that require predictions at a finer temporal granularity. Collecting and maintaining fine-grained traffic data across all locations and time periods would impose a substantial burden on database storage and preprocessing pipelines. To address this temporal granularity mismatch, we formulate a novel problem: predicting fine-grained future traffic using coarse-grained sampled data. We propose the Spatial-Temporal Refinement Predictor (STRP), a granularity-aware framework for spatio-temporal data systems. STRP integrates two components: Tree Convolution for efficient and interpretable spatial dependency modeling, and Inverse Dilated Convolution for progressive temporal extrapolation. STRP supports two practical prediction settings: window-based and duration-based, to handle different forms of granularity mismatch. Experiments on six benchmark datasets show that STRP significantly outperforms state-of-the-art baselines in both accuracy and efficiency. Our work offers a practical and interpretable approach to managing granularity mismatches in spatio-temporal traffic data systems.

---


### 440. [RunAgent SuperBrowser: A Theory of Autonomous Web Navigation Grounded in Human Browsing Behaviour](https://arxiv.org/abs/2606.09399)

**<font color=#1a73e8>作者：</font>** Radeen Mostafa, Sawradip Saha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present SUPERBROWSER, an autonomous web-navigation agent designed against a single guiding hypothesis: a web agent should browse the way a person browses. A human reading a page does not retain every pixel they have seen; they look at a few candidate targets, decide on one, and remember only what is needed to keep the goal alive. We operationalize this perception-cognition-action triad as three coupled mechanisms. First, a vision-first bounding-box pipeline labels candidate interactive regions on every screenshot and feeds them, asynchronously prefetched, to the language model so that the "eye" precedes the "hand". Second, a three-role brain -- an Orchestrator that classifies and routes, a Planner that evaluates progress every few steps, and a Worker that emits per-step actions -- separates strategic from operational reasoning. Third, a structured Ledger stores only what a person would: the goal, the last three actions, a small set of facts and dead-ends, and a handful of checkpoints; a six-phase eviction loop systematically discards stale screenshots, state blobs, and reasoning traces from the live context. Action execution is a three-tier click cascade (Chrome DevTools Protocol to Puppeteer to scripted) with humanized Bezier motion, plus a chevron-aware bounding-box snapper that resolves the "small arrow beside a large label" ambiguity. On the Mind2Web Hard benchmark (66 tasks), SUPERBROWSER attains 89.47% success, placing third overall and ahead of every published open/research browser-agent baseline by a large margin. We argue that the gain comes not from any single trick but from the consistent application of a cognitive contract throughout the system.

---


### 441. [vesselFM-CT: Segmenting All Blood Vessels in CT Images for System-Level Cardiovascular Analysis](https://arxiv.org/abs/2606.09400)

**<font color=#1a73e8>作者：</font>** Bastian Wittmann, Chinmay Prabhakar, Suprosanna Shit 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The vascular network in the human body is characterized by blood vessels exhibiting drastic structural variations in radius, length, topological properties, and branching patterns. This heterogeneity, together with location-specific anatomical background variations, poses a significant challenge for robust, large-scale analysis of the entire cardiovascular system. As a result, most research has focused on narrow, isolated segments of the vascular network. While such targeted studies provide valuable insights, they inherently limit the ability to assess the systemic health and functional integrity of the vascular network as a whole. In this work, we aim to bridge this gap to advance both clinical diagnostics and our fundamental understanding of vascular physiology. We propose the task of segmenting all vessels in CT images, ranging from the largest components of the cardiovascular system to even minuscule mesenteric vessels. To this end, we introduce vesselFM-CT, the first model capable of robustly segmenting all blood vessels in 3D CT images. VesselFM-CT is trained via an iterative, multi-step process and optimizes our proposed TubeLoss loss function, effectively addressing the inherent heterogeneity of the cardiovascular system. We demonstrate that vesselFM-CT outperforms all baselines and enables automated, precise extraction of the cardiovascular system from CT images, thereby unlocking a wide range of clinical and technical perspectives, including automated disease classification and synthetic CT image generation.

---


### 442. [Fully Oblivious Differential Privacy for Frequency Estimation in the Augmented Shuffle Model with Trusted Processors](https://arxiv.org/abs/2606.09402)

**<font color=#1a73e8>作者：</font>** Takao Murakami, Yuichi Sei, Reo Eriguchi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the shuffle model of DP (Differential Privacy), a shuffler randomly permutes users' data to achieve high accuracy and privacy. Recent studies show that most existing shuffle protocols are vulnerable to collusion attacks by the data collector and users. They address this issue by introducing the augmented shuffle model that incorporates random sampling and dummy data addition into the shuffler. However, it remains open how to ensure the shuffler follows the protocol and does not collude with the data collector in this model.
We address this trust issue by thoroughly exploring the augmented shuffle model with TEEs (Trusted Execution Environments). We first introduce a new privacy notion, FODP (Fully Oblivious DP), which strengthens DP to prevent various TEE side-channel attacks based on external/internal memory access patterns and control flows. We propose a general framework for FODP algorithms based on memory-size obfuscation and three concrete algorithms within it. We also improve the efficiency of our algorithms by using the count-min sketch and optimizing the number of hashes. We evaluate our algorithms on Intel SGX and demonstrate their effectiveness through comparisons with nine baselines.

---


### 443. [Introducing multiplex semantic networks as multifaceted representations of creative associative knowledge across multilingual samples](https://arxiv.org/abs/2606.09403)

**<font color=#1a73e8>作者：</font>** Edith Haim, Kurt Haim, Roger E. Beaty 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Creativity is a complex cognitive ability that relies on knowledge organisation and retrieval from semantic memory. Yet most research uses a single task to measure it, capturing only a fraction of this complexity. This study investigates multiplex networks - layered semantic networks obtained from six cognitive tasks - as a more comprehensive approach to modelling the associative knowledge underlying creativity. We collected data from N=518 individuals from four countries (Austria, USA, Singapore, Italy). From their responses to verbal fluency, sentence-chain, free association, and narrative writing tasks, we constructed semantic networks and assembled them in a multiplex structure. AI persona-based responses provided a comparison baseline. Structural reducibility analyses showed that different task layers captured distinct, non-redundant information about semantic organisation, supporting the use of multiple tasks over any single one. The networks from high- and low-creative groups remained structurally distinct, while AI-generated networks showed near-identical structures regardless of creativity group. Finally, we used 12 features (network measures, emotional scores, and spreading activation simulations) in a machine learning model using ridge regression to predict individual creativity scores. The combination of structurally similar layers, as identified in the previous stage, improved a proof-of-concept prediction accuracy by 50%. Structural measures showed the highest feature importance, with spreading activation dynamics providing additional predictive power. Together, these findings indicate that multiplex semantic networks capture a richer, cross-cultural picture of associative knowledge underlying creativity. We also release our diverse dataset and code to foster diverse computational approaches within the creativity community.

---


### 444. [Correct Looks Better: Pairwise Comparisons Reveal Accuracy Rankings](https://arxiv.org/abs/2606.09409)

**<font color=#1a73e8>作者：</font>** Mina Remeli, Moritz Hardt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pairwise comparisons combined with aggregation methods like Elo have become central to evaluating generative models, yet concerns remain that they reward superficial stylistic cues or display judge biases. In a more positive turn, we show that model rankings from pairwise comparisons strongly agree with ground-truth-based accuracy rankings when such ground truth is available for comparison. By converting five well-known benchmarks into free-form generative evaluations, we find that Elo rankings achieve a Spearman correlation above 0.9 with accuracy rankings and substantially outperform direct evaluation when the judge is weak. Furthermore, style and judge bias have only minor effects on model rankings, despite most judgments occurring on pairs where both candidate answers are correct (or incorrect). On such pairs, we find that repetition after the final answer (echo) is a causal driver of judge preference.

---


### 445. [Capacity, Not Format: Rethinking Structured Reasoning Failures](https://arxiv.org/abs/2606.09410)

**<font color=#1a73e8>作者：</font>** Hengxin Fan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prior work treats structured output as a reasoning tax, but this framing is incomplete: the cost of formatting depends strongly on a model's spare capacity. Using information-matched prose controls and a four-level schema complexity gradient, we separate format-specific effects from prompt-length confounds across 4 models and 5 benchmarks with 0% parse failures on successfully generated responses.
We find that structured formats are capacity-dependent. Models with sufficient headroom absorb JSON constraints without degradation (Sonnet: $88.7\pm4.0$% JSON vs. $89.3\pm1.7$% CoT on MATH-Hard). In contrast, formats severely degrade models operating near their limits through two distinct mechanisms. First, under standard token budgets, Haiku drops 36.2pp ($p < 0.0001$) largely due to truncation. Second, even with extended budgets eliminating truncation, GPT-4o-mini drops 28.0pp ($p < 0.001$), revealing pure capacity competition independent of token exhaustion.
This format penalty scales with schema complexity (McNemar $p < 0.0001$) and cannot be explained by prompt length alone. Furthermore, these results qualify claims of frontier model immunity: on AIME competition math, Opus 4.7 drops from 96.2% to 91.0% under JSON ($-5.3$pp; the displayed percentages are independently rounded, exact difference is $7/133 = 5.26$pp $\approx 5.3$pp). A delayed-structure ablation -- reasoning freely before formatting -- recovers most of the lost accuracy (3-run mean: 80--87%), supporting the capacity competition mechanism. The practical implication is not to avoid structured output, but to match it to capacity: when a model is near its limits, think first, format later.

---


### 446. [Towards Post-Quantum Secure Pharmacovigilance with ML-KEM and ML-DSA](https://arxiv.org/abs/2606.09412)

**<font color=#1a73e8>作者：</font>** Saee Desai, Tom Shimoni, Eddie Cameron 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Pharmacovigilance systems handle sensitive healthcare and drug-safety data, including adverse event reports and clinical observations. As quantum computing advances, classical public-key cryptographic systems such as RSA and elliptic-curve cryptography may become vulnerable, creating long-term risks for healthcare data that must remain confidential for many years. This paper presents an educational prototype of a post-quantum secure pharmacovigilance data pipeline. The system uses ML-KEM-768 for post-quantum key establishment, HKDF-SHA-256 for deriving an AES key, AES-256-GCM for efficient file encryption, and ML-DSA-65 for digital signatures and tamper detection. The pipeline supports multiple file formats, including TXT, CSV, JSON, and PDF, by treating files as raw bytes and preserving metadata for reconstruction at the receiver. The prototype includes separate hospital, gateway, pharma receiver, attacker, benchmarking, and dashboard components. We evaluate the system using synthetic pharmacovigilance datasets of different sizes and formats. Our results show that ML-KEM adds a small constant overhead, while AES encryption and ML-DSA signing dominate runtime as file size increases. This work is not a production-ready healthcare system, but rather an educational systems-level exploration of how post-quantum cryptographic primitives can be integrated into healthcare-style data pipelines.

---


### 447. [AI Assurance in UK Defence: Challenges in Operationalising JSP 936](https://arxiv.org/abs/2606.09414)

**<font color=#1a73e8>作者：</font>** Callum Cockburn, Sam Farrow  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This report examines practical challenges in operationalising JSP 936 Part 1 for AI assurance in UK Defence. Using a structured interpretive review of the directive's requirements, the analysis identifies eight thematic challenge areas adequacy of evidence and argument, management of human interaction with AI, definition of the operational environment, integration of AI within systems of systems, assessment and maintenance of AI performance, analysis of safety and security, measurement of ethicality, and mitigation of the inherent complexities of AI. The report argues that JSP 936 provides a useful governance basis, but that implementation depends on unresolved technical, organisational, and assurance questions. These challenges stem from the socio-technical nature of AI-enabled systems, uncertainty in real-world deployment contexts, limitations in current assurance methodologies, and tensions between performance, safety, human oversight, security, and ethical acceptability. The report identifies areas where further methods, guidance, and organisational capability are needed for the ambitious, safe, and responsible adoption of AI across Defence. This is consistent with MOD's own framing of JSP 936 as requiring iterative implementation and supporting guidance.

---


### 448. [Toward Signing Activity Projection in Sign Language Interaction](https://arxiv.org/abs/2606.09424)

**<font color=#1a73e8>作者：</font>** Takao Obi, Wang Yusong, Koji Inoue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social robots must interact robustly not only with users assumed by speech-centered systems but also with diverse users whose communication relies on different modalities, e.g., sign language. One important capability gap is predictive turn-taking with signing users. Although Voice Activity Projection (VAP) has been successfully used to model future voice activity in spoken interaction, it remains unclear whether the framework transfers to sign language interaction. This paper presents an initial transfer study of adapting a VAP architecture to dyadic sign language interaction. Using interaction recordings from the Public DGS Corpus, we derive binary signing activity streams from lexical sign annotations and formulate proxy tasks for turn-taking prediction. The model uses pose-derived hand, eye-region, and mouth-region features extracted for each signer. The results show that SHIFT/HOLD prediction is promising, especially with hand cues, while SHIFT-prediction remains difficult. These findings provide initial evidence for both the promise and the current limitations of transferring predictive turn-taking models from spoken interaction to sign language interaction. Predictive modeling of sign language interaction still requires sign-language-specific event definitions that go beyond speech-derived categories.

---


### 449. [WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces](https://arxiv.org/abs/2606.09426)

**<font color=#1a73e8>作者：</font>** Wanli Li, Bowen Zhou, Yunyao Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) increasingly operate in runtimes that combine visual desktop control, command-line execution, code editing, browsers, and external tools. Existing benchmarks, however, often evaluate these interfaces as separable capabilities, leaving long-horizon cross-interface orchestration under-tested. Thus, we introduce WeaveBench, a long-horizon hybrid-interface benchmark with 114 tasks across 8 real-world work domains, grounded in real user requests and publicly verifiable artifacts. Each task requires agents to combine GUI observations/actions with CLI/code operations within a single trajectory. We evaluate these tasks on a real Ubuntu desktop inside deployed CLI-agent runtimes, augmented with a minimal desktop-control plugin. We also propose a companion trajectory-aware judge that inspects deliverables, files, screenshots, logs, and action traces, while detecting shortcut behaviors such as fabricated visual evidence or hard-coded metrics. Across frontier model-runtime pairings, the best PassRate reaches only 41.2%, showing the benchmark remains far from saturated. The trajectory-aware judge further reveals that outcome-only grading substantially overestimates agent performance. Overall, WeaveBench exposes a critical gap in CUA evaluation and provides an effective testbed to measure whether agents can orchestrate GUI, CLI, and code operations across long-horizon real-world tasks.

---


### 450. [Guide Me Out: A Framework to Benchmark VLM Operators Communication in Crisis Scenarios](https://arxiv.org/abs/2606.09428)

**<font color=#1a73e8>作者：</font>** Giacomo Gonella, Stefano Menini, Marco Guerini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective crisis response requires spatially grounded communication that bridges linguistic guidance of civilians with the physical environment, accounting for structural bottlenecks, evolving threats, and agent-specific contexts. Yet, current NLP research in crisis communication remains mainly limited to static, text-only classification settings, overlooking the critical communicative role of AI operators in dynamic, embodied scenarios. We address this gap with a novel benchmarking framework for evaluating Vision-Language Models (VLMs) tasked with guiding civilian agents through simulated evacuations. We test two communication strategies (narrowcast vs. broadcast), two environment representations (visual vs. graph-based), and two threat behaviors (static vs. moving) across nine maps of varying structural complexity. Our results show that Narrowcast consistently reduces civilian Fail rates compared to Broadcast across all difficulty levels. Guidance quality depends heavily on how the VLM operator represents the world: the visual modality drives performance, while adding an adjacency graph is model-dependent and often harmful. Moving threats raise Fail rates across all conditions as communication must continuously adapt over time. Together, these findings show that deploying VLMs as AI operators in evacuation scenarios remains a non-trivial challenge, where the choice of communication strategy and input representation can directly determine the success or failure of the intervention.

---


> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-527](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

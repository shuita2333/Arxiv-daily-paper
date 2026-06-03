# 📦 其他研究 | 2026年06月04日

> 本类共 **312** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-312](./part-07.md)

---

### 51. [Scalable Uncertainty Quantification for Extreme Weather Forecasting via Empirical Neural Tangent Kernels](https://arxiv.org/abs/2606.02886)

**<font color=#1a73e8>作者：</font>** Jose Marie Antonio Miñoza, Rex Gregor Laylo, Sebastian C. Ibañez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning weather models now match numerical weather prediction accuracy while running orders of magnitude faster, but produce deterministic forecasts without uncertainty estimates, a critical gap for high-stakes decisions during extreme weather events. This paper proposes Neural Tangent Kernel-based uncertainty quantification (NTK-UQ) using last-layer empirical features. Theoretical analysis predicts that UQ quality is architecture-dependent through two mechanisms. First, a variance collapse mechanism explains when UQ fails: when the eigenvalue truncation rank approaches the effective rank of the feature space, the GP correction term consumes nearly all prior variance, destroying discrimination between tropical cyclones and routine conditions; architectures with concentrated spectra (spectral operators) require aggressive truncation ($k \leq 10$), while attention-based models tolerate full-rank computation. Second, decomposition performance depends on the non-Gaussian, heavy-tailed structure of extreme weather: Independent Component Analysis exploits higher-order statistics (kurtosis, negentropy) to isolate heavy-tailed extreme-event features, achieving higher discrimination than singular value decomposition, which captures only second-order variance. A data-driven selection rule chooses ICA or SVD from the feature eigenspectrum concentration ratio, correctly prescribing the superior decomposition for all four evaluated architectures. Compared to split conformal prediction (the natural post-hoc baseline), NTK-UQ achieves 31--37\% sharper prediction intervals at 90\% coverage, and uniquely produces \emph{adaptive} intervals that scale with extreme event severity, which conformal prediction cannot achieve by construction. The framework requires no retraining; inference-time uncertainty requires only a single matrix-vector product per sample.

---


### 52. [A Nonmonotone Gradient-Based Algorithm for Symmetric Nonnegative Matrix Factorization and Graph Clustering](https://arxiv.org/abs/2606.02887)

**<font color=#1a73e8>作者：</font>** Ryan Swart, Johannes Brust  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symmetric nonnegative matrix factorization (Symmetric NMF) approximates a matrix as $WW^T$ with nonnegative rectangular factor $W$. It has broad applications in graph clustering and machine learning. In contrast to the NMF, projected gradient methods for the symmetric problem had been associated with slow convergence. To address this, we introduce SNMPBB, the first adaptation of nonmonotone projected Barzilai-Borwein methods to Symmetric NMF, demonstrating that gradient algorithms are significantly more effective than previously understood. We further extend SNMPBB to graph clustering using the graph Laplacian regularization (Graph-SNMPBB) and to large problems with low-rank approximations (LAI-SNMPBB). For all variants we prove global convergence to first-order stationary points and also that Barzilai-Borwein curvature information is preserved with randomized approximations. On synthetic data, SNMPBB achieves 6 times speedup over the alternative SymANLS for similar residuals, with advantages growing at higher ranks. Across six real-world clustering benchmarks, Graph-SNMPBB matches or exceeds SymANLS accuracy. Lastly, LAI-SNMPBB outperforms state-of-the-art LAI-SymPGNCG on 34 SuiteSparse matrices in both runtime and residual quality.

---


### 53. [Multi-Modal Machine Learning for Breast Cancer Recurrence Prediction](https://arxiv.org/abs/2606.02892)

**<font color=#1a73e8>作者：</font>** Jiahao Shao, Xudong Wang, Anam Nawaz Khan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Breast cancer recurrence, a leading cause of long-term mortality among survivors, requires timely and accurate risk assessment to guide follow-up care and treatment planning. Traditional predictive models, often limited to either structured or unstructured data alone, struggle to capture the full clinical context. This study examines the impact of integrating multi-modal clinical data, including treatment records, pathology reports, and clinician notes, on recurrence prediction. By integrating a rule-based regular expression extraction mechanism with a rigorous precedence-based conflict reconciliation strategy, our approach effectively recovers definitive tumor characteristics from free-text pathology narratives to augment structured records. We also benchmark performance against commonly used feature sets from prior breast cancer studies to assess the added value of multi-modal integration. Single-source and multi-modal inputs are evaluated across a range of machine learning models. Results show that multi-modal integration consistently improves predictive accuracy compared to single-modal methods.

---


### 54. [Tiny Collaborative Inference for Occlusion-Robust Object Detection](https://arxiv.org/abs/2606.02894)

**<font color=#1a73e8>作者：</font>** Chieh-Tung Cheng, Mustafa Aslanov, Eiman Kanjo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small edge devices such as IoT surveillance nodes and search-and-rescue (SAR) platforms are increasingly expected to run computer vision locally. On ultra-low-end hardware, however, object detection is limited by available memory and compute, by communication costs when several devices cooperate, and by the loss of accuracy caused by occlusion. The work evaluates occlusion-robust object detection on devices with less than 1 MB SRAM by combining an MCUNet backbone, a YOLOv2 detection head, and TensorFlow Lite quantisation. We evaluate two collaborative inference strategies: feature-level fusion, which concatenates intermediate feature maps, and decision-level fusion via Weighted Boxes Fusion (WBF). Under the tested occlusion settings, WBF outperforms feature-level fusion and gives gains of up to +0.2736 mAP in asymmetric occlusion scenarios. Extending fusion to three views improves accuracy further (up to +0.3827 mAP) while adding communication overhead (approximately 1.3 KB per exchange). The hardware experiments start with a host-assisted USB-relay baseline and then move to a Wi-Fi peer-to-peer deployment on two Coral Dev Board Micro units, where WBF runs on-device and communication energy remains small relative to inference. In a representative 301.9 s autonomous session comprising 108 frames, fused output is observed on 61 frames compared with 47 for Board 2 alone, a frame-level coverage gain of +29.8%. We also include a small exploratory decentralised federated learning (DFL) feasibility note, but do not treat it as a main result because performance remains limited under non-iid local data. The results support decision-level fusion as a viable option for improving occlusion robustness in small-scale edge object detection, including host-free multi-board operation on ultra-low-end hardware.

---


### 55. [WRIT: Write-Read Intensive Trajectory Synthesis for Multi-Turn User-Facing Agents](https://arxiv.org/abs/2606.02908)

**<font color=#1a73e8>作者：</font>** Hengrui Gu, Xiaotian Han, Kaixiong Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn user-facing agents must infer user intent from incomplete requests, collect missing information through dialogue and tools, and execute valid actions. A training trajectory records this process as an interleaved sequence of user messages, agent responses, tool calls, etc. Synthesizing sufficiently complex trajectory has become a central route to train agents: existing pipelines often increase difficulty by composing multiple user requests into longer tasks, producing write-intensive trajectories that train sequential execution.
We argue that a single write decision can itself be difficult when the agent must gather and compare substantial read-tool evidence before its arguments become identifiable, a challenge that write-intensive data alone cannot address. Guided by this insight, we propose WRIT (\uline{W}rite-\uline{R}ead \uline{I}ntensive \uline{T}rajectory Synthesis), a pipeline for synthesizing multi-turn agent training trajectories along two complexity axes: the number of write decisions in a task and the evidence burden of each individual decision. WRIT first generates write-intensive and read-heavy tasks. It then diversifies user behavior instructions to reflect realistic conversational variation, and finally simulates agent-user interactions in an executable environment to produce complete training trajectories. The resulting data trains agents not only for longer task execution, but also for robust, evidence-grounded decision making under high information load. With only 2K synthesized trajectories, a 4B model trained on WRIT outperforms GPT-5.1 no-think on $\tau^2$-bench and substantially reduces inference-time token usage, showing that compact SFT data can convert part of expensive test-time reasoning into efficient agent behavior.

---


### 56. [The Ghost Annotator: a Framework to Explore Human Label Variation in Content Moderation through Conformal Prediction](https://arxiv.org/abs/2606.02911)

**<font color=#1a73e8>作者：</font>** Mirko Lai, Alessandra Urbinati, Simona Frenda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current research primarily focuses on model performance, while comparatively less attention has been devoted to uncertainty estimation, particularly in settings where LLMs are increasingly used to generate annotated data. We introduce a framework combining conformal prediction with Collaborative Filtering-style annotators' representation to model LLM behavior in relation to human annotators and to analyze patterns of agreement and disagreement. Using Non-Conformity Scores, we introduce the Ghost Prediction metric and the Ghost Annotator representation to quantify cases in which model predictions diverge from all available human annotations. We compute cosine similarity measures to explore differences in model behavior across sociodemographic axes. We evaluated four LLMs of different size and families across four content moderation datasets. Our finding shows that while we find that all models uncertainty increases with annotator disagreement, larger models tend to be more confident in the classification of texts that are not aligned with any human annotation. Finally, the Ghost Annotator framework reveals a consistent and robust pattern of demographic misalignment, suggesting a structural bias likely rooted in pretraining corpora.

---


### 57. [Any2Poster: Any-Source Poster Generation Across Modalities and Domains](https://arxiv.org/abs/2606.02915)

**<font color=#1a73e8>作者：</font>** Amogh Vinaykumar, Aiden Li, Suozhi Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual posters are a compact medium for communicating dense information, yet progress on automatic poster generation remains difficult to measure because existing evaluations are often restricted to paper-only inputs, narrow domains, or surface-level visual similarity. We introduce Any2Poster Bench, a benchmark for any-source poster generation that evaluates systems across eight input modalities--PDFs, URLs, PPTX, DOCX, Markdown, LaTeX, notebooks, and videos--and five content domains. Any2Poster Bench pairs each source with quiz-based probes of verbatim factual retention and interpretive understanding, together with VLM-based judgments of visual quality, layout, readability, content completeness, and logical flow, enabling reproducible assessment of both information fidelity and visual communication. To instantiate and validate this benchmark, we further present Any2Poster Agent, an end-to-end reference agent that parses heterogeneous sources, organizes salient content, plans poster layouts, renders posters, and iteratively refines them using visual feedback. On Any2Poster Bench, Any2Poster Agent achieves 87.25% average accuracy across input modalities and 87.28% across content domains. On PaperQuiz-style evaluation, where prior paper-to-poster agents are directly comparable, Any2Poster Agent improves over PosterAgent-4o from 51.06-51.33% to 72.58% overall accuracy and from 116-121 to 145.16 in density-augmented score. Together, Any2Poster Bench and Any2Poster Agent provide a reusable evaluation resource and a competitive baseline for studying multimodal, domain-general poster generation.

---


### 58. [Pixel Cube: Diffusion-based Portrait Video Relighting Through Realistic Lighting Reproduction](https://arxiv.org/abs/2606.02919)

**<font color=#1a73e8>作者：</font>** Yufan Zhang, Yu Ji, Ayo Ajiboye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a diffusion-based method for relighting dynamic portrait videos with photorealism and temporal consistency. Our method is fueled by a hybrid training dataset that consists of real-captured and rendered dynamic portrait videos with diverse subject appearances, facial motions, head poses, and known lighting conditions. Specifically, we construct an LED-based lighting system for realistic lighting emulation and high-speed video relighting data acquisition. By leveraging the image priors embedded in pre-trained video diffusion models, and using per-frame high dynamic range (HDR) environment map as lighting control, we train a high-performance generative model for realistic and identity-preserving dynamic portrait video relighting. In addition to the environment map control, our model uses a synthesized background image to enable control on the camera's exposure level and color tone. Our model can produce temporally consistent relit portrait video that looks realistic and harmonious under a provided new environment and faithfully preserve the subject's expression and fine facial features, including skin tone, wrinkles, and facial hair. Our model generalizes well to unseen data, in terms of the subject appearance, motion, and lighting condition. We perform extensive experiments on relighting in-the-wild videos with various environment maps and demonstrate practical applications on portrait photography. Results show that our method achieves state-of-the-art performance in photorealism, lighting harmony, and temporal consistency.

---


### 59. [Fast Unlearning at Scale via Margin Self-Correction](https://arxiv.org/abs/2606.02920)

**<font color=#1a73e8>作者：</font>** Federico Di Gennaro, Alexander Shevchenko, Fanny Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language-model unlearning updates a trained model to behave as if it had not seen selected training examples, while preserving utility and avoiding costly retraining. Existing approaches typically fine-tune the pretrained model with a fixed training budget and select the final model afterwards by evaluating several saved checkpoints on downstream validation data. Two sources of unnecessary computation limit scalability: training beyond the desired forget-retain trade-off, and checkpoint selection that requires extra storage and repeated evaluations. To address these limitations, we introduce MArgin Self-Correction (MASC), an efficient unlearning method with an online stopping rule that does not require downstream evaluation. Given a text sequence to be forgotten, MASC actively reduces the logit gap between the original next token and the most likely alternatives. It outputs a final model once this gap is small on average over a sufficiently large proportion of token positions across all forget sequences. On TOFU, MUSE News, and MUSE Books, MASC achieves a competitive forget-retain trade-off at a fraction of the computational cost of existing baselines. We further observe that as we increase model size (a.k.a. number of parameters), the trade-offs improve for both MASC and SimNPO -- the forget metrics remain comparable while retain utility increases.

---


### 60. [ATLAS: A Large-Scale Evaluation Benchmark for Adversarial LiDAR Perception](https://arxiv.org/abs/2606.02924)

**<font color=#1a73e8>作者：</font>** Mellon M. Zhang, Siddhant Panse, Zimo Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving perception is typically evaluated on clean benchmark data, yet real-world deployment requires robustness to rare, structured, and potentially adversarial sensor anomalies. This gap is especially critical for LiDAR, where external actors can physically manipulate the sensing process to induce black-box perception failures without accessing the model. Existing LiDAR benchmarks provide little visibility into this failure mode. Prior adversarial LiDAR studies have largely centered on attack hardware, geometric and algorithmic defenses, and early-generation detectors, leaving the robustness of modern perception systems unexplored. To address this evaluation gap, we introduce ATLAS (Adversarial Temporal LiDAR Attack Suite), the first large-scale, physically grounded evaluation benchmark for LiDAR perception models under black-box sensor attacks, simulating the two primary attack modes -- point injection and point removal -- across real driving sequences. Evaluating a broad cross-section of current state-of-the-art LiDAR perception models, ATLAS reveals a surprising robustness asymmetry: models with stronger performance on standard benchmarks tend to better withstand removal attacks, yet are actually more vulnerable to injection attacks than weaker models. We trace this vulnerability to standard object database sampling augmentations, revealing how current training practices can induce architecture-agnostic robustness failures, and study initial directions for mitigating both attack modes. We release the ATLAS generation code to support extensible, reproducible evaluations as attack capabilities evolve, helping make black-box sensor robustness an explicit consideration in future LiDAR perception development.

---


### 61. [SaluNet: Enabling Total Plasticity in Normalization-Free Deep Networks](https://arxiv.org/abs/2606.02927)

**<font color=#1a73e8>作者：</font>** Mourad Zaied  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Normalization layers such as BatchNorm and LayerNorm have long been considered essential for stable training in deep networks. This work demonstrates that they can be fully replaced by a single learnable activation mechanism. We identify a plasticity suppression effect induced by standard normalization: learnable activation parameters rapidly lose adaptability when paired with normalization layers. Motivated by this observation, we introduce SALU (Saturated Adaptive Linear Unit), \[ \operatorname{SALU}(x;a,b) = \frac{a x}{\sqrt{1 + a b x^2}},\quad a>0,\; b>0 \] a bounded, learnable activation that provides intrinsic signal stabilization without relying on batch statistics or external affine parameters. Building on SALU, we propose SaluNet, a paradigm grounded in total plasticity: SALU replaces normalization layers, while SWALU and GALU replace standard activations. With ResNet-18, SaluNet-C-18 achieves 97.35\% on CIFAR-10 and 83.25\% on CIFAR-100 without normalization, maintaining 93.44\% and 76.23\% at batch size 1 where normalized architectures fail. For transformers, SaluNet-T improves over LayerNorm-GELU from 90.92\% to 91.01\% on CIFAR-10 and from 66.54\% to 68.10\% on CIFAR-100. SaluNet-C-50 reaches 78.67\% Top-1 on ImageNet-1K at $224\times224$, and $79.23\%$ at $288\times288$. These results suggest normalization layers suppress total plasticity, a property biological neurons inherently possess, enabling deep networks to learn effectively.

---


### 62. [Characterization and Effects of CS2 Learning with GenAI, Visualization, and Human Support](https://arxiv.org/abs/2606.02933)

**<font color=#1a73e8>作者：</font>** Quinton Yong, Anthony Estey, Miguel Nacenta  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) is becoming a widely adopted learning support tool for both students and instructors, as it offers benefits such as personalized tutoring and scaffolded learning. However, recent research highlights potential drawbacks such as overreliance and metacognitive issues, especially in novice programmers. Most prior work focuses on introductory programming courses, and important questions remain about the underlying mechanisms behind the negative effects of GenAI and if findings can be generalized when students learn more advanced computer science concepts. To address this gap, we conducted a mixed-methods study comparing student interactions with GenAI to two traditional learning supports in a second-year algorithms course: algorithm visualization (AV) and human live tutoring (LT). Twelve students participated in three 90-minute study sessions focusing on sorting, tree, and graph algorithms. We recorded gaze and interaction data, and each session concluded with a test assessing their conceptual understanding of the topic. Our analysis classifies when during the problem-solving process participants sought help, and compares the interaction patterns across the three learning supports. Although GenAI produced a larger increase in self-efficacy compared to live tutoring, it was associated with noticeably lower results in learning outcomes. We found that participants did not use algorithm visualizations effectively, faced usage barriers when using GenAI to learn advanced topics, and that live tutoring yielded the highest learning outcomes.

---


### 63. [Quantifying Side-Channel Leakage in Public Metrology Releases](https://arxiv.org/abs/2606.02934)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Taylan Alpay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public scientific and metrology releases can leak the hidden settings that produced them. We formalize and quantify this risk as a profiled statistical side-channel audit: a release map exposes finite-band statistics of a power spectral density (PSD), a profiled observer trains labeled template spectra under an explicit budget, and a challenge release is drawn from one of two utility-equivalent recipes separated by a protected coordinate. Averaged PSD bins follow a gamma channel, replaced by a covariance-weighted log-spectrum channel when the bins are correlated; this yields exact Kullback-Leibler divergences, Chernoff exponents, protected-bit advantage bounds, and finite-training, finite-library, finite-compute, and model-mismatch corrections. Our headline result is a finite-band transport-leakage law: after amplitude and blur are eliminated, the protected acid-transport information obeys $I_{\lambda|\alpha,\beta}(K) = (64/1225)\, w \lambda^{6} K^{9} + O(w \lambda^{8} K^{11})$ for $K\lambda \ll 1$, a ninth-order exponent with a closed-form safe band. A step-by-step protocol turns a measured release into these numbers, and a fixed-seed reproducibility package regenerates every table and figure. We instantiate the audit on screened extreme-ultraviolet (EUV) roughness spectra as a model-conditioned case study, with deployment on measured releases the next step.

---


### 64. [CAD-to-CT Registration of Cylindrical Objects via Ellipse-Based Axis Estimation](https://arxiv.org/abs/2606.02935)

**<font color=#1a73e8>作者：</font>** Aleksander Ogonowski, Mikołaj Mrozowski, Daniel Więcek 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate registration of CAD models to CT scans is essential for establishing ground truth geometry in volumetric imaging. Obtaining reliable object masks is of growing importance in machine learning settings; as recent architectures grow more capable, huge datasets are required to fully utilise their capabilities. Traditional intensity-based methods fail when CT grayscale values lack calibration references, while point-based algorithms (e.g., ICP, RANSAC) require feature correspondence unavailable between idealized CAD geometry and noisy volumetric CT data.
We propose a two-stage geometric registration method for cylindrical objects (ionization chambers) that takes advantage of the distinctive geometric features of the objects. First, we estimate the 3D rotation axis by detecting elliptical cross-sections across CT slices, fitting ellipses to edge-detected contours, and performing PCA on the fitted ellipse centers after RANSAC outlier removal. Second, we voxelize the CAD model, orient it along the detected axis, and maximize volumetric overlap with the CT scan through translational adjustment.
This approach achieves robust registration with tilt and orientation errors below $0.1^\circ$ without intensity calibration or feature matching. Once registered, the aligned CAD model provides ground truth geometry for applications including machine learning-based object localization and automated analysis in industrial CT workflows.

---


### 65. [Hierarchical RBF-KAN and RBF-SKAN Architectures for Multidimensional Function Approximation and Random Field Learning](https://arxiv.org/abs/2606.02936)

**<font color=#1a73e8>作者：</font>** Mingtao Xia, Qijing Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this manuscript, we propose and analyze hierarchical Kolmogorov--Arnold neural network architectures employing radial basis functions as activation functions for approximating deterministic functions and random field models. Specifically, we develop a hierarchical radial-basis-function Kolmogorov--Arnold network (hierarchical RBF-KAN) for multidimensional deterministic function approximation and a hierarchical radial-basis-function stochastic Kolmogorov--Arnold network (hierarchical RBF-SKAN) for random field learning. From a theoretical perspective, we establish universal approximation results for both architectures. In particular, we derive quantitative approximation estimates for the hierarchical RBF-KAN, showing that the proposed framework has the potential to partially alleviate the curse of dimensionality in learning high-dimensional functions by reducing the effective dimensionality of the approximation problem. Furthermore, we show that the hierarchical RBF-SKAN can approximate random field models under the Wasserstein-2 metric. Empirically, we show that our proposed radial-basis-function-based neural network structure could effectively learn multivariate functions and random field models.

---


### 66. [ERP-XTTN: Interpretable Prototype-Guided Cross-Attention for Cross-Subject ERP Classification](https://arxiv.org/abs/2606.02939)

**<font color=#1a73e8>作者：</font>** Charlotte Genevier Wyman, Leanne Hirshfield  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretable brain-computer interface classifiers that generalize across subjects without calibration remain an open challenge. We test whether prototype-based cross-attention can provide competitive, interpretable event-related potential (ERP) classification under deployment-compatible conditions. We propose ERP-XTTN, a cross-attention architecture that routes input EEG patches to fixed difference-wave prototypes via query-key-only cross-attention with no value projection, so classification depends entirely on attention routing and attention faithfulness is structural rather than post-hoc. Prototypes are derived automatically from extrema in the training-fold difference wave. We evaluate across three public sources (BNCI Horizon 2020, HRI Cursor, and ERP CORE) spanning eight ERP components (ERN, LRP, ErrP, N170, P300, N2pc, MMN, N400), using leave-one-subject-out (LOSO) evaluation with causal filtering at two channel counts (3-channel and full montage), against EEGNet and xDAWN with Riemannian geometry (xDAWN+RG). The mean gap between the best baseline and ERP-XTTN was .018 AUROC at 3 channels and .034 at full montage, arising from two largely distinct sources: a temporal-flexibility cost relative to EEGNet and a spatial-exploitation cost relative to xDAWN+RG, the latter driven by signal-to-noise ratio at full montage. Beyond accuracy, the transparent routing reveals cross-subject signal structure that black-box models cannot: false positives resembled true positives more than true negatives did, indicating that classification errors are neurophysiologically explicable. ERP-XTTN generalizes across diverse ERPs under causal, calibration-free conditions with a small interpretability cost at minimal montages. To our knowledge, this is the first epoch-level LOSO benchmark on ERP CORE.

---


### 67. [Outsmarting the Chameleon: Counterfactual Decoupling for Tactical OOD Shifts in Live Streaming Risk Assessment](https://arxiv.org/abs/2606.02946)

**<font color=#1a73e8>作者：</font>** Yiran Qiao, Jing Chen, Jiaqi Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Live streaming has emerged as a primary medium for social interaction and digital commerce, yet it is increasingly plagued by sophisticated risks. A fundamental challenge in this domain is \emph{tactical out-of-distribution (OOD) shift}: while malicious actors maintain stable underlying objectives, they continuously redesign narrative packaging to evade detection. Such adversarial shifts expose critical limitations of existing OOD generalization paradigms, whose assumptions are difficult to satisfy in the presence of tightly coupled intent-tactic evolution and ill-defined raw-level counterfactuals.
In this paper, we tackle this issue from a \emph{latent causal} perspective and propose \underline{L}atent-\underline{P}redictive \underline{C}ounterfactual \underline{D}ecoupling~(LPCD), a plug-in framework for robust live streaming risk assessment. LPCD enables counterfactual reasoning under adversarial tactical re-packaging by modeling intent and narrative variation at the latent level, and enforces \emph{latent counterfactual consistency} to anchor risk prediction on causally stable malicious intent. At inference time, LPCD applies a lightweight, parameter-free calibration to further mitigate tactic-induced distribution shifts. Extensive experiments on large-scale industrial datasets and online production traffic demonstrate that LPCD consistently outperforms state-of-the-art baselines, validating its effectiveness in moderating evolving adversarial risks in real-world live streaming. The project page is available at this https URL.

---


### 68. [From Non-Convex to Strongly Convex: Curvature-Adaptive FTPL for Online Optimization](https://arxiv.org/abs/2606.02948)

**<font color=#1a73e8>作者：</font>** Moses Charikar, Chirag Pabbaraju, Ambuj Tewari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Curvature adaptivity is a classical theme in online optimization: for convex Lipschitz losses, adaptive methods interpolate between the optimal $O(\sqrt{T})$ regret for general convex losses and $O(\log T)$ regret under strong convexity. Recent work has shown that Follow-the-Perturbed-Leader (FTPL) achieves optimal $O(\sqrt{T})$ regret even for online non-convex Lipschitz losses, assuming access to an approximate offline-optimization oracle, but these guarantees do not exploit curvature. We show that FTPL can be made curvature-adaptive in the non-convex setting, without knowing in advance how curvature will accumulate over time. Our algorithm replaces the fixed perturbation scale of standard FTPL with a time-varying scale chosen using only past information. We give a simple follow-the-leader tuning rule for this scale and show that it competes, up to constants, with the best choice in hindsight. The resulting method achieves $O(\sqrt{T})$ regret for arbitrary non-convex Lipschitz losses and improves as cumulative curvature grows; with sufficiently accurate oracle calls, it achieves $O(\log T)$ regret when cumulative curvature grows linearly, which includes the classical strongly convex regime. We complement these upper bounds with matching lower bounds for prescribed cumulative-curvature sequences, already for one-dimensional convex losses, showing that the tradeoff between worst-case non-convex regret and curvature-driven fast rates is intrinsic.

---


### 69. [Echelon: Auditable Aggregate-Only Language-Model Adaptation Across Privacy Boundaries](https://arxiv.org/abs/2606.02958)

**<font color=#1a73e8>作者：</font>** Hina Dixit, Punit Kumar, Irene Tenison 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cross-organization language-model adaptation increasingly faces hard governance constraints: in many deployments, device-level model state-parameters, activations, optimizer state, and per-device updates-cannot be exported outside an administrative boundary. Existing distributed and federated stacks typically assume cross-site model exchange and then retrofit privacy mechanisms, which complicates compliance and makes auditing brittle. We present Echelon, a boundary-first training architecture that enforces device-level model-state non-export as a systems invariant. Devices train locally inside each boundary; the only cross-boundary payloads are securely aggregated boundary-level deltas plus O(1) coordination metadata, exposed through a concrete audit surface. Restricting exchange to aggregates changes the optimization problem: the system must remain stable under WAN delay, heterogeneous participation, churn, and non-IID data even though the global plane never sees per-device updates. Echelon combines buffered semi-asynchronous secure aggregation, staleness-aware weighting, participation windows, proximal local objectives, and a drift-aware outer synchronization controller. In 1B-parameter LoRA adaptation across M= 2 boundaries, a budget-matched contest over three seeds (24.88M tokens) reaches validation loss 3.887 +/-0.010 and is best or tied-best among tuned low-communication baselines under fixed-token, fixed-bytes, fixed-wall-clock, and fixed-sync-count budgets. In OpenWebText stress tests, Echelon sustains 2,139-2,176 tokens/s across evaluated WAN and non-IID treatments, Echelon-DA improves time-to-target under WAN latency relative to a privacy-parityDiLoCo+SA baseline, and quality degrades by at most 2.2% under 200ms emulated latency or severe non-IID partitioning.

---


### 70. [Hand Trajectory Fusion for Egocentric Natural Language Query Grounding](https://arxiv.org/abs/2606.02962)

**<font color=#1a73e8>作者：</font>** Enmin Zhong, Carlos R. del-Blanco, Fernando Jaureguizar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric Natural Language Query (NLQ) grounding asks a model to localize, in a long first-person video, the temporal interval that answers a free-form text query. Existing methods fuse video appearance with the query but ignore hand motion, despite the fact that roughly 41% of Ego4D NLQ queries are answered at a moment of hand--object manipulation or their immediate this http URL propose a hand-trajectory encoder for converting a sequence of hand skeletons into highly-semantic hand kinematic features, which are then aligned and combined with pretrained video--text features through a cross-attention fusion strategy with adaptive gating. On the Ego4D NLQ v2 validation split, the clearest gains appear for Hand-Object Interaction queries (+2.54 R1@IoU=0.3) and Quantity/State queries (+4.32 R1@IoU=0.3), indicating that hand trajectory provides grounding cues beyond appearance alone.

---


### 71. [What Benchmarks Don't Measure: The Case for Evaluating Abstention Competence in Autonomous Agents](https://arxiv.org/abs/2606.02965)

**<font color=#1a73e8>作者：</font>** Victor Ojewale, Suresh Venkatasubramanian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmarks for autonomous agents measure whether agents complete tasks, yet this framing is systematically blind to whether an agent should have proceeded at all. Agents trained under human-feedback objectives develop a structural tendency to proceed even when they lack the inputs, evidence, or authorization to act safely, a disposition we term compliance bias, because both the reward signal and the benchmark scoring regime treat proceeding as the correct default regardless of whether the preconditions for safe action are present. We make three contributions. We first show that compliance bias originates in reward hacking within human-feedback pipelines and is entrenched by prominent agent benchmarks, which either penalize agents for pausing or are architecturally unable to distinguish a principled pause from a silent failure. We then introduce a three-gap taxonomy of abstention-warranted scenarios, covering specification gaps where required information is absent, verification gaps where world state cannot be confirmed, and authority gaps where explicit authorization has not been given, which together provide a principled basis for constructing abstention-aware agent benchmarks. Finally, we propose abstention evaluation protocols (Safety Rate, Usability Rate, and Informed Refusal Rate) and report preliminary results across 144 enterprise agent scenarios and five model families, in which a runtime-enforced abstention mechanism achieves up to 89.2% hazardous-action blocking and 87.5% usability on authorized scenarios, demonstrating that the safety--usability tradeoff is tunable rather than inherent and that its shape varies substantially across model families. We treat this as preliminary work and offer the taxonomy and composite metrics as a starting point for further conversations.

---


### 72. [From Explanation to Diagnosis: Next Generation Interactive Video Coach with Misstep Awareness](https://arxiv.org/abs/2606.02970)

**<font color=#1a73e8>作者：</font>** Xiao Jin, Rahul K. Dass, Ashok K. Goel  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Intelligent tutoring systems excel at generating explanations but rarely provide principled diagnosis of where and why a learner is wrong. We introduce a misstep-aware coaching capability for Ivy, a neurosymbolic AI coach, built on a two-model architecture that augments a Task-Method-Knowledge (TMK) model with a new Pedagogical Model (PM) in the context of an online graduate AI course at Georgia Tech. The PM makes instructor diagnostic knowledge explicit and machine-readable by encoding, for each quiz question and incorrect response, the learner's underlying belief(a brief statement of the incorrect idea or missing knowledge), a TMK locus(the source of the misunderstanding), a misconception type and targeted scaffolding derived from the instructor's Q\&A key. Using quiz questions from the course, we demonstrate a proof-of-concept pipeline that detects and classifies learner errors and generates diagnosis-grounded scaffolding, moving Ivy beyond knowledge retrieval toward diagnostic misstep awareness, and enabling more precise, actionable feedback that supports conceptual change and advances adaptive learning systems in AI in education and the learning sciences.

---


### 73. [EURO-5K: When Does Domain Pretraining Matter? Benchmarking Transformers for EU Reporting Obligation Extraction](https://arxiv.org/abs/2606.02971)

**<font color=#1a73e8>作者：</font>** Marios Koniaris, Vasileios Kotronis, Eugenia Giannini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extracting reporting obligations from EU legislation is critical for assessing and reducing regulatory reporting burden. However, distinguishing reporting requirements from structurally similar provisions requires specialised legal understanding. Current legal NLP methods lack specialised datasets with clear guidelines and comparative evaluation of extraction paradigms and domain adaptation strategies. We curate EURO-5K, a corpus of sentence-level reporting obligations and challenging negative examples from 136 EU legislative acts. On this dataset, we train and compare discriminative token-classification models (BERT-style) and generative span-extraction models (LLMs), evaluating both full fine-tuning and parameter-efficient QLoRA against baselines (pattern and dependency-based extraction, few-shot prompting). Results show that fully fine-tuned generic and legal BERT models achieve similar performance (0.89 F1), while fine-tuned LLMs match encoder accuracy for sentence-level extraction. Legal pretraining offers only small gains for generative models. In contrast, it is clearly beneficial when adaptation capacity is constrained, as parameter-efficient tuning of Legal-BERT outperforms its generic counterpart. Learning curve analysis demonstrates that legal pretraining accelerates early learning with minimal data. All approaches converge around 3K samples with diminishing returns thereafter, validating dataset sufficiency. Cross-dataset evaluation on two external regulatory corpora shows that our models behave as specialised reporting obligation extractors rather than generic regulatory classifiers. We release EURO-5K, trained models, and an interactive demo with explainability visualizations and structured RDF export. These demonstrate that both paradigms and parameter-efficient training provide practical tools for regulatory compliance automation.

---


### 74. [Chatbots Output Meaningful (but Problematic) Language](https://arxiv.org/abs/2606.02973)

**<font color=#1a73e8>作者：</font>** Matthew Stone, Una Stojnić  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Are utterances by AI chatbots meaningful? Concretely, if a user asks, say, Anthropic's agent Claude, "What is the capital of Spain?" and Claude answers, "Madrid is the capital of Spain," does that sentence have its ordinary meaning -- and does it express a true proposition? Most ordinary users, as well as AI engineers, take the answer to be trivially "yes." However, many cognitive scientists, linguists, and philosophers of language argue that dominant intentionalist accounts of language and meaning deliver the opposite conclusion.
Theorists more sympathetic to ordinary users' intuitions have therefore advocated a radical "de-anthropomorphization" of language, revising our understanding of mental states, intentions, and semantic content to capture the intuition that the outputs of LLMs are meaningful. We take a different approach. While we, too, argue that LLM outputs are meaningful, we contend that a proper theory of human language already applies, as is, to current chatbots. Meaning is a low bar: claiming that LLM outputs are meaningful does not require positing mental states, intentions, rationality, or the cognitive capacities requisite for communication in LLMs -- or, indeed, making any other anthropomorphic assumptions. People do have communicative intentions (typically successful ones), but nevertheless, even in humans, language production can depart from what the speaker has in mind.
Our view has important consequences for how we should theorize about -- and critically engage with -- both human linguistic output and synthetically generated text. In particular, to say that chatbots produce meaningful text is not by any means to endorse what they output, or to assume that the technology is (or is not) good, powerful, appropriate, or useful.

---


### 75. [WISE-HAR: A Generalizable Ensemble Deep Learning Framework for WiFi-Based Human Activity Recognition](https://arxiv.org/abs/2606.02974)

**<font color=#1a73e8>作者：</font>** Maheen Arshad, Qindeel E Zahra, Muhammad Khuram Shahzad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human Activity Recognition (HAR) using WiFi signals has emerged as a transformative technology for smart homes, healthcare monitoring, security systems, and ambient assisted living. Unlike traditional camera-based systems that raise significant privacy concerns and fail in low-light conditions, or wearable sensors that require user compliance, WiFi-based HAR is non-intrusive, privacy-preserving, cost-effective, and works seamlessly in any lighting condition. This paper presents a comprehensive approach to recognize three distinct human activities: "No Presence" (empty room), "Walking", and "Walking + Arm-waving" using the Wallhack1.8k WiFi spectrogram dataset. We propose three key improvements to address the main challenges in WiFi-based HAR. First, to address high performance variance, we implement ensemble learning with five different CNN architectures (Deep CNN, Wide CNN, MobileNetV2, ResNet50V2, and EfficientNetB0). Second, to address the small dataset size limitation, we apply aggressive data augmentation techniques including time-warping, frequency masking, and noise addition. Third, to evaluate real-world generalization capability, we perform cross-scenario evaluation (training on Line-of-Sight and testing on Non-Line-of-Sight) and cross-antenna evaluation (training on Biquad antenna and testing on PIFA antenna). Our ensemble model achieved a test accuracy of 94.87% on the LOS scenario with Biquad antenna, outperforming the best individual model by 0.66%. Data augmentation improved Random Forest performance from 60% to 95%. Cross-scenario evaluation showed minimal accuracy drops of only 1.37% and 2.07%, demonstrating strong generalization capabilities. The results indicate that the proposed approach is robust, reliable, and suitable for real-world deployment in diverse environments with different hardware configurations.

---


### 76. [Memory Retrieval for Changing Preferences](https://arxiv.org/abs/2606.02976)

**<font color=#1a73e8>作者：</font>** Yuehan Qin, Li Li, Linxin Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context dialogue systems must decide both when to access memory and which parts of the interaction history are relevant. Existing approaches typically rely on heuristic retrieval signals or always-on memory usage, failing to account for the changing and potentially inconsistent nature of user preferences. In this work, we propose a unified framework for memory access and selection based on changing preferences. We formulate personalized memory retrieval as identifying which historical turns provide evidence about a user's latent preference state, rather than relying on surface-level semantic similarity. To this end, we quantify the utility of each memory turn using a Bayes factor, defined as the improvement in the model's likelihood of the reference response when the turn is included in context. This provides a principled measure of evidence strength and a unified signal for both memory access and selection. By framing memory retrieval as utility estimation, the model learns to identify salient turns and regulate memory usage based on expected utility. Experiments on four heterogeneous memory benchmarks show that our approach outperforms existing embedding-based retrieval on long-context, preference-intensive tasks where modeling changing preferences is essential, while remaining competitive in low-density regimes where semantic similarity suffices.

---


### 77. [Towards Compact Autonomous Driving Perception with Balanced Learning and Multi-sensor Fusion](https://arxiv.org/abs/2606.02979)

**<font color=#1a73e8>作者：</font>** Oskar Natan, Jun Miura  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a novel compact deep multi-task learning model to handle various autonomous driving perception tasks in one forward pass. The model performs multiple views of semantic segmentation, depth estimation, light detection and ranging (LiDAR) segmentation, and bird's eye view projection simultaneously without being supported by other models. We also provide an adaptive loss weighting algorithm to tackle the imbalanced learning issue that occurred due to plenty of given tasks. Through data pre-processing and intermediate sensor fusion techniques, the model can process and combine multiple input modalities retrieved from RGB cameras, dynamic vision sensors (DVS), and LiDAR placed at several positions on the ego vehicle. Therefore, a better understanding of a dynamically changing environment can be achieved. Based on the ablation study, the model variant trained with our proposed method achieves a better performance. Furthermore, a comparative study is also conducted to clarify its performance and effectiveness against the combination of some recent models. As a result, our model maintains better performance even with much fewer parameters. Hence, the model can inference faster with less GPU memory utilization. Moreover, the result tends to be consistent in 3 different CARLA simulation datasets and 1 real-world nuScenes-lidarseg dataset. To support future research, we share codes and other files publicly at this https URL.

---


### 78. [Predicting Inference-Time Scaling Gains from Labeled Validation-Set Output Statistics](https://arxiv.org/abs/2606.02981)

**<font color=#1a73e8>作者：</font>** Luyang Zhang, Jingyan Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Best-of-$N$ inference scaling (drawing $N$ candidate answers from a language model and returning the one a reward model ranks highest) improves accuracy by an amount that varies across models, but predicting that amount in advance currently requires running the procedure end-to-end. Prior work links cheap statistics of a model's sampled outputs and validation-set correctness (how often samples agree, how diverse they are, how confident the model is, and where correct samples appear) to model behavior, but does not isolate which of these form a stable, compact predictor of best-of-$N$ gain. We fit ridge predictors on features computed from a single labeled validation-set sampling pass, use bootstrap-Lasso as a stability analysis of the candidate feature set, and give a concentration analysis with an explicit linear-approximation residual. Across three base-model families, six post-training methods, and math and reasoning task domains, the stability analysis identifies a strict three-feature core spanning prompt-level agreement spread, label-assisted first-correct-sample position, and completion-length variance; a compact ridge predictor built from this core plus an entropy add-on reaches Spearman $\rho = 0.90$ with actual best-of-$N$ gain under a reward-model verifier. The intended use is labeled validation-set screening of candidate configurations before paying the full reward-model scoring cost.

---


### 79. [Neural Networks Provably Learn Spectral Representations for Group Composition](https://arxiv.org/abs/2606.02993)

**<font color=#1a73e8>作者：</font>** Jianliang He, Leda Wang, Fengzhuo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how structured internal structure emerges during neural network training is central to the study of deep learning. We investigate this phenomenon through the group composition task, where a two-layer neural network is trained to predict $g_1 \star g_2$ for elements of a finite group $G$. By lifting the projected gradient flow to the Fourier domain, we demonstrate that the training dynamics are governed by a Riemannian gradient ascent on a representation-theoretic energy functional. We prove that, under random initialization, this flow drives each neuron to converge almost surely toward a single irreducible representation, while the cross-layer Fourier coefficients achieve a rotational rank-one alignment. This framework provides a representation-theoretic account of feature learning and characterizes a novel low-rank compression phenomenon for matrix-valued group representations. Moreover, for Abelian groups, we provide a complete population-level description: random initialization promotes uniform diversification across nontrivial representations and induces Haar-uniform phases, jointly approximating the indicator via a majority-vote mechanism. We further prove that both phase alignment and representation competition emerge with exponential convergence rates.

---


### 80. [Inducing Reasoning Primitives from Agent Traces](https://arxiv.org/abs/2606.02994)

**<font color=#1a73e8>作者：</font>** Zhihan Lei, Jiarui Yan, Joshua Momo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> ReAct-style LLM agents often rediscover the same reasoning routines across problems, yet leave those routines trapped in transient scratchpads. We introduce Reasoning Primitive Induction, a single-pass method that mines successful ReAct traces, clusters recurrent reasoning moves, and converts the most frequent moves into a compact library of typed pseudo-tools. Each pseudo-tool is specified by a natural-language docstring interpreted by an LLM at invocation time, and a standard ReAct loop composes these primitives at test time. The central result is that induced libraries outperform the very agent that generated their traces: by +44pp on RuleArena NBA (30 -> 74), +30pp on MuSR team allocation (38 -> 68), and +22pp on NatPlan meeting planning (7 -> 29). Across five comparable subtasks spanning narrative deduction, rule application, and constraint-satisfaction planning, a single fixed configuration improves over zero-shot Chain-of-Thought on every subtask, matches or surpasses expert-authored decompositions, and outperforms AWM at lower average inference cost.

---


### 81. [Exact equivariance, kept through training, buys zero-shot generalisation across the symmetry group](https://arxiv.org/abs/2606.03003)

**<font color=#1a73e8>作者：</font>** Hongbo Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A latent world model built from an equivariant encoder $E$ and an equivariant predictor $f$ inherits a provable symmetry of its training loss: when the world's dynamics genuinely carries a group $G$ acting on latents by an orthogonal representation $\rho(g)$, the one-step prediction relMSE is exactly invariant across the whole group, so fitting the dynamics on a restricted slice of orientations mathematically determines it on the entire orbit (jǔ yī fǎn sān). We verify this end-to-end at laptop scale (CPU/MPS, fully seeded). [A] The symmetry survives a real Muon/AdamW + EMA + VICReg run -- composed encode-then-predict residual $\sim 10^{-6}$ after optimisation, not just at initialisation, and under any optimiser. [B] One-step error is flat to five digits across the group, while a same-hypothesis-class non-equivariant baseline fits the slice but breaks out-of-distribution (VN $\times 1.00$ vs baseline $\times 13.8$ in 2D, $\times 17.2$ in 3D, $\times 157$ over the full $\mathrm{SE}(3)$ ladder), with the equivariant model $4.5$-$7.4\times$ smaller. [C] The same isometry argument lifts to closed loop: under a matching equivariant planner the control trajectory at orientation $g$ is exactly $\rho(g)$ applied to the seen one, so closed-loop error is invariant across the group -- float-floor-exact in 2D/$\mathrm{SO}(2)$ on real PushT and statistically flat in 3D/$\mathrm{SE}(3)$ (disjoint 95% CIs). We stress-test the prior against Sutton's Bitter Lesson: augmentation, brute-force scale, and soft-equivariance each close at most the across-group task metric, never the float-floor exactness. Because equivariance is closed under composition, the $H$-fold rollout stays flat ($\times 1.00$, $\le 2\times 10^{-7}$) at every horizon, while the baseline's residual compounds with $H$. Out of scope: task-success sweeps, planner-free invariance, and scaling.

---


### 82. [Secure AltDA Integration for Ethereum L2s: An End-to-End Validation Framework](https://arxiv.org/abs/2606.03010)

**<font color=#1a73e8>作者：</font>** Bowen Xue, Samuel Laferriere  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Alternative data availability (AltDA) systems provide Ethereum L2s with an external data publication layer for high throughput rollup designs. By moving bulk data publication outside of Ethereum, AltDA allows L2s to process more data than native DA. However, this replacement introduces a new consensus critical integration layer. Existing ecosystem frameworks identify high level risks, such as external DA trust assumptions and the presence or absence of a DA verifier, but do not provide a complete specification for how an L2 should integrate with AltDA. This gap can lead to L2 halts, inconsistent derivation across honest L2 nodes, invalid state assertions, or bridge attacks. This paper presents a canonical validation framework for secure AltDA integration. We model the boundary as a typed, deterministic, and total translation from L1 inbox bytes to an AltDA commitment, then to externally available data, and finally to the rollup payload consumed by the rest of core L2s logic. The central principle is that every adversarial input must lead to a defined unique outcome. We show how missing obligations lead to concrete failure modes, including underconstrained settlement, derivation halts, inconsistent honest node behavior, invalid state assertions, and bridge safety failures. We then apply the framework to representative AltDA integration architectures, including Celestia-Blobstream, EigenDA based designs, and Avail-ZKsync. Our evaluation shows that secure AltDA integration is not determined solely by the DA provider or bridge. The surrounding L2 integration must also enforce the full validation relation connecting L1 inbox inputs to accepted L2 state.

---


### 83. [MOSAIC: Efficient Mixture-of-Agent Scheduling via Adaptive Aggregation and Inference Concurrency](https://arxiv.org/abs/2606.03014)

**<font color=#1a73e8>作者：</font>** Saptarshi Mitra, Yifan Zhang, Rachid Karami 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Agents (MoA) systems improve reasoning accuracy by routing each query to multiple expert LLMs and aggregating their outputs. Efficiently executing this workload on limited GPU resources has bottlenecks. Skill-based routing creates skewed expert demand, and combining instruction-tuned LLMs with long-reasoning models results in extreme variability in generation lengths. Consequently, traditional scheduling strategies suffer from significant GPU idling and throughput collapse due to load imbalances. We present MOSAIC, a scheduling framework to accelerate MoA workloads. First, we formulate an Integer Linear Program (ILP) based scheduler that jointly optimizes expert placement and per-worker prompt assignment from offline-profiled costs, replicating reasoning experts across workers while pinning lightweight ones. Second, MOSAIC uses confidence-aware adaptive aggregation, leveraging inter-expert agreement to bypass the heavy final aggregator LLM for consensus queries. In our 4-GPU system, MOSAIC achieves up to 2.5x expert-stage, 4.23x aggregator-stage and 1.7~2.3x end-to-end speedups over the baseline scheduler, while matching accuracy within 0.1pp.

---


### 84. [ConTraIRL: Factorized Contrastive Abstractions for Transferable IRL](https://arxiv.org/abs/2606.03017)

**<font color=#1a73e8>作者：</font>** Yikang Gui, Bikramjit Banerjee, Prashant Doshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward transfer in Inverse Reinforcement Learning (IRL) is unreliable when policies must generalize to unseen combinations of environment dynamics and task goals. We propose Factorized Contrastive Abstractions for Transferable IRL (ConTraIRL), a framework that enables compositional reward transfer by learning decoupled latent representations of these two factors. ConTraIRL uses a dual-encoder architecture that maps observations into separate dynamics and goal latent spaces, trained with a dual contrastive objective. Temporal alignment encourages the dynamics encoder to learn goal-invariant structure, while the goal encoder captures dynamics-invariant features. This factorization supports reward inference under recombined dynamics-goal settings. Experiments on continuous control benchmarks demonstrate effective few-shot transfer to unseen dynamics-goal pairings, improving sample efficiency and reward recovery over transfer IRL baselines.

---


### 85. [Hanger Reflex Based Driving Assistance for Drivers with Peripheral Visual Field Defects](https://arxiv.org/abs/2606.03020)

**<font color=#1a73e8>作者：</font>** Hailong Liu, Junya Wada, Toshihiro Hiraoka 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Drivers with peripheral visual field defects may fail to notice pedestrians in their peripheral visual field, leading to delayed hazard awareness and increased collision risk. This study explores hanger reflex cue (HRC) as a driving assistance method for drivers with peripheral visual field defects, in which mechanical pressure is applied to specific regions of the head to facilitate anticipatory orientation toward potentially risky pedestrians and support safer driving. In a driving simulator experiment with 15 participants, we compared driving behavior with and without HRC during pedestrian encounters under simulated peripheral visual field defect. The results showed that HRC significantly shifted drivers' modal head rotation angle toward the risky pedestrian and significantly increased gaze duration toward that pedestrian. Collision occurrence was lower in the w/ HRC condition than in the w/o HRC condition, although the direct effect of HRC on collision occurrence showed only a marginal trend. A piecewise structural equation modeling analysis further suggested that HRC may contribute to collision reduction through a sequential pathway from head rotation to gaze allocation and then to collision occurrence. These findings provide preliminary evidence that HRC can support anticipatory attention allocation toward peripheral hazards and may offer a promising driving assistance method for drivers with visual field impairment.

---


### 86. [SkillGuard: A Permission Framework for Agent Skills](https://arxiv.org/abs/2606.03024)

**<font color=#1a73e8>作者：</font>** Shidong Pan, Xiaoyu Sun, Tianyi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills extend LLM agents with reusable instructions, scripts, tool bindings, and contextual dependencies. However, current skill ecosystems largely rely on trust-based loading and static inspection, leaving a gap between what a skill can inject into an agent's context and what it can cause the agent to do at runtime. This gap introduces new security and privacy risks, and existing defenses primarily inspect skill files statically or regulate individual tool calls, without systematically connecting a skill's declared intent with its runtime behavior. In this paper, we present SkillGuard, a skill-centric permission framework that treats skills as permission-bearing executable artifacts. SkillGuard introduces a dual-plane governance model that jointly regulates context influence and action side effects through skill manifests, runtime access control, user-mediated authorization, deny-by-default enforcement, capability inference, and behavior monitoring. We evaluate SkillGuard on 315 real-world skills and SkillInject. The permission taxonomy covers 99.76% of observed protected objects, and automated manifest generation reaches 91.0% F1. In adversarial evaluations, SkillGuard reduces attack success from 32.37% to 23.02% for contextual injections and from 25.56% to 16.67% for obvious injections, while maintaining benign task utility. These results suggest that SkillGuard, as a skill-centric permission framework, can provide a practical foundation for improving the privacy and security of agent skill ecosystems.

---


### 87. [SEA-Embedding: Open and Reproducible Text Embeddings for Southeast Asia](https://arxiv.org/abs/2606.03027)

**<font color=#1a73e8>作者：</font>** Peerat Limkonchotiwat, Raymond Ng, Sarana Nutanong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text embeddings are fundamental to many downstream applications, making robustness important for real-world NLP. However, most recent state-of-the-art embedding models are not reproducible because they rely on closed or undisclosed training data, and they remain insufficiently robust for Southeast Asian languages. We present SEA-Embedding, a fully open and reproducible text-embedding pipeline for Southeast Asian languages trained only on publicly available data, and use it to study three core factors of robust embedding design: data composition, training objective, and base encoder initialization. SEA-Embedding achieves state-of-the-art results on SEA-BED while enabling systematic and reproducible analysis of robust text embeddings for the region.

---


### 88. [AUDITFLOW: Executable Symbolic Environments for Structured Financial Reporting Verification](https://arxiv.org/abs/2606.03031)

**<font color=#1a73e8>作者：</font>** Yan Wang, Xuguang Ai, Jaisal Patel 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Structured financial audit verification is difficult for language-model agents because correctness depends on structured evidence rather than text alone. A model must link reported facts to taxonomy concepts, traverse calculation or dimensional relations, and recompute expected values before applying an audit rule. We propose AuditFlow, a graph-grounded multi-agent framework that separates adaptive search from deterministic verification. AuditFlow builds a symbolic environment from a static US-GAAP taxonomy graph and a dynamic XBRL filing graph, and exposes it through typed tools for fact retrieval, taxonomy traversal, numerical checking, and rule evaluation. Two junior auditors inspect each case from regulatory and evidentiary views, while a senior auditor resolves disagreements and can request further investigation. The final reports are fused through evidential aggregation to produce an audit verdict, expected value, evidence trail, and trustworthiness score. On a FinAuditing-derived FinMR sample, AuditFlow reaches 82.09% joint audit accuracy under GPT-5.5, outperforming the strongest baseline by 14.93 points. Removing deterministic checks drops accuracy to 17.91%, showing that the symbolic environment performs the verification step that the model cannot reliably replace.

---


### 89. [Capability Advertisement as a Market for Lemons: A Trust Layer for Heterogeneous Agent Networks](https://arxiv.org/abs/2606.03034)

**<font color=#1a73e8>作者：</font>** Gaurav Naresh Mittal  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have begun to delegate work to one another. Protocols such as the Model Context Protocol (MCP) and the Agent2Agent protocol (A2A) let an agent publish what it can do and let others call it, and public registries of such agents are already appearing. These protocols assume an advertised capability is a static, truthful fact. A real agent is none of these things: its competence is probabilistic, varies with input, drifts when the underlying model is updated, and, because the agent is itself a language model, it can describe itself with complete confidence and be wrong. A caller therefore sees what an agent claims to do, not what it can do, with no principled way to tell a reliable provider from a fluent impostor.
We argue these difficulties share one cause: the market for lemons. When quality is hidden and claims are cheap, good and bad providers become indistinguishable, honest reliability goes unrewarded, and the market decays toward its worst participants. Economics offers three remedies, signaling, screening, and reputation, and none are present in today's agent protocols.
We make four contributions: (1) a failure taxonomy that names confident-wrong as a non-adversarial, correlated subclass of Byzantine faults that classical fault-tolerance mismodels; (2) a market-for-lemons model showing that faith-based protocols admit only a low-trust equilibrium; (3) the Trust Layer, a thin, protocol-agnostic narrow waist above MCP and A2A that adds probabilistic capability descriptors, screening, and reputation, and admits a separating equilibrium when the cost of sustaining an overclaim exceeds the gain from it; and (4) a reliability-composition bound for delegation chains with an end-to-end placement argument. The design needs no model retraining and degrades gracefully when its trust anchors are absent or corrupt.

---


### 90. [Will Accurate Fields Mislead Photonic Design? FromGlobal Accuracy to Port Readout](https://arxiv.org/abs/2606.03038)

**<font color=#1a73e8>作者：</font>** Yitian Zhang, Yonghong chen, Youming Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural field surrogates can accelerate photonic design loops, but a surrogate that looks accurate in global field error can still mis-rank candidate devices when the final decision depends on localized output-port readouts. This risk is acute in propagation-dominated MMI splitters and couplers, where port power, splitting, phase, and coupling are determined by accumulated modal interference and output-window aggregation rather than by average field similarity alone. We study this field-to-design mismatch through a Field/Mediator/Readout view that separates dense complex-field error from propagation-profile and output-window errors before port aggregation. To align the surrogate with this chain, we propose PaNO, a propagation-aligned neural operator that keeps the full-field prediction interface while organizing latent states around local boundary structure, transverse modal content, axial propagation, and cross-mode interaction. We also evaluate PaNO-R2, an output-aware feedback variant for residual field components near the port region. On a 15-wavelength tunable $3{\times}3$ MMI benchmark with 4608 held-out fields, PaNO lowers NeurOLight's port-power error from 0.2018 to 0.0739 despite slightly higher cMAE, showing that global field accuracy alone is not sufficient for design-relevant readout fidelity. PaNO-R2 attains the best cMAE, propagation-profile error, output-profile error, and port-power error, reducing NeurOLight's port-power and output-profile errors by 72.7\% and 72.5\%.

---


### 91. [RelGT-AC: A Relational Graph Transformer for Autocomplete Tasks in Relational Databases](https://arxiv.org/abs/2606.03040)

**<font color=#1a73e8>作者：</font>** Phillip Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Relational databases underpin modern enterprise, scientific, and healthcare systems, yet predictive machine learning on such data remains challenging due to their multi-table, heterogeneous, and temporal structure. Relational Deep Learning (RDL) addresses this by representing databases as heterogeneous graphs and applying graph neural networks (GNNs) directly. RelBench v2 recently introduced autocomplete tasks -- a practically motivated task type where the goal is to predict an existing column value from relational context, analogous to an intelligent form-filling assistant. We propose RelGT-AC (Relational Graph Transformer for Autocomplete), extending the RelGT architecture with three targeted contributions: (1) a column masking strategy that prevents trivial solutions by masking the target column during subgraph encoding; (2) a unified task head supporting binary classification, multiclass classification, and regression autocomplete tasks within a single model; and (3) a TF-IDF text encoder that automatically detects and encodes free-text columns, recovering strong lexical signal that categorical encoders discard. Across 7 tasks spanning 3 RelBench v2 datasets (rel-trial, rel-f1, rel-stack), RelGT-AC outperforms the GraphSAGE baseline on all 3 regression autocomplete tasks and achieves up to +10 AUROC points on text-heavy eligibility tasks via the TF-IDF encoder.

---


### 92. [FCUS-rPPG: A Fast-Converging Unsupervised Framework for Remote Photoplethysmography via Gradient Oscillation Suppression](https://arxiv.org/abs/2606.03050)

**<font color=#1a73e8>作者：</font>** Jiajie Li, Yu Liu, Rencheng Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote photoplethysmography (rPPG) enables non-contact extraction of blood volume pulse (BVP) signals using consumer-grade cameras. Recent unsupervised rPPG methods learn BVP representations without requiring ground-truth physiological annotations, yet their optimization is often hindered by noisy and unstable gradients, resulting in slow convergence and limited cross-domain generalization. In this paper, we propose FCUS-rPPG, a fast-converging unsupervised rPPG framework with strong generalization capability. Motivated by the observation that BVP representations exhibit both multi-spectral covariation and low-dimensional manifold structure, we design a spectrally shared backbone that facilitates BVP feature disentanglement while improving optimization efficiency. To jointly enhance convergence stability and generalization performance, we further develop a unified optimization framework operating at the gradient, loss-landscape, and feature-representation levels. Specifically, a post-verification masking mechanism filters out misleading gradients according to the weak-amplitude physiological prior of BVP signals; a perturbation-based loss landscape smoothing strategy steers optimization toward more generalizable flat minima; and a noise-aware null-space regularization constrains feature updates to the orthogonal complement of the noise subspace, thereby mitigating noise-induced representation drift. Extensive experiments on five datasets demonstrate that FCUS-rPPG requires only one training epoch, whereas existing methods typically require tens to hundreds of epochs. Notably, FCUS-rPPG consistently achieves state-of-the-art (SOTA) performance in cross-dataset evaluations. This study provides an efficient and robust solution to the real-world deployment of unsupervised rPPG. The source code will be publicly available at this https URL.

---


### 93. [What Do Students Learn? A Feature-Level Analysis of Dark Knowledge](https://arxiv.org/abs/2606.03052)

**<font color=#1a73e8>作者：</font>** Seungu Kang, Songkuk Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge Distillation (KD) is a powerful tool for model compression, yet the precise mechanisms by which student models acquire feature representations remain underexplored. In this work, we analyze student feature learning using the Interaction Tensor framework. Our analysis reveals that effective KD acts as a regularizer that prunes low-frequency, sample-specific features, encouraging the student to rely on a compact set of highly reusable features. Crucially, we observe that the dataset-level confusion matrix contains structural information analogous to the teacher's "Dark Knowledge." Leveraging this insight, we propose Confusion Distillation (CD), a teacher-free self-distillation method that utilizes the model's own evolving confusion patterns as dynamic soft targets. CD achieves competitive performance on ResNet-34 and ResNet-50 for CIFAR-100, outperforming existing self-distillation methods like CS-KD and PS-KD by 1.2% while offering a computationally efficient alternative to standard KD.

---


### 94. [ToolGate: Token-Efficient Pre-Call Control for Tool-Augmented Vision-Language Agents](https://arxiv.org/abs/2606.03054)

**<font color=#1a73e8>作者：</font>** Anjie Liu, Yan Song, Zhixun Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented vision-language agents can acquire external perceptual evidence through OCR, detection, segmentation, and other tools, but executing every proposed tool call is costly and sometimes unnecessary. We study the pre-call control problem: after a ReAct-style VLM agent proposes a perceptual tool call, should the call be executed, or skipped before its output enters the context? Across five benchmarks, we find that the baseline agent exhibits poor local selectivity: helpful and harmful calls occur at similar rates (11.8% vs. 9.9%), while most calls do not change the immediate forced-answer prediction. We introduce ToolGate, a lightweight external controller that predicts execute/skip decisions from trajectory text and simple structural features. Across two Qwen3-VL backbones, ToolGate reduces token cost to 64-69% of the unrestricted ReAct baseline while preserving average accuracy in cross-domain settings. With matched-domain trajectory training on Qwen3-VL-30B, it further improves average accuracy by 1.65 points. These results show that tool-augmented VLM agents benefit not only from better perceptual tools, but also from explicit control over when tool outputs are worth paying for.

---


### 95. [Learn When and Where to Connect: Adaptive Virtual Nodes for Dynamic Message Passing on Graphs](https://arxiv.org/abs/2606.03068)

**<font color=#1a73e8>作者：</font>** Jaejun Lee, Joyce Jiyoung Whang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Virtual Nodes (VNs) are often utilized in Message Passing Neural Networks (MPNNs) to facilitate effective message passing, existing VN-based methods have limitations, such as constraining all nodes to connect to the same number of VNs, fixing the connections before applying MPNNs, and connecting a node to a VN independently of the other nodes that connect to the same VN. We propose MAVN, an end-to-end differentiable MPNN framework that allows non-constrained connections between nodes and VNs and dynamically introduces VNs on demand in response to evolving node representations across layers. Specifically, MAVN learns to adaptively determine when (at which layer) and where (to which nodes) to introduce and connect VNs based on the relative importance of connections. From a pool of candidate VNs, MAVN selects the necessary VNs in each layer, where each selected VN is connected to a nonempty subset of nodes, guided by a dual-perspective scoring mechanism that jointly captures the nodes' preferences for VNs and the VNs' preferences for nodes. We theoretically prove that for any node-VN connectivity pattern, there exists a set of MAVN's parameters that can simulate the pattern. Experiments on nine real-world datasets demonstrate that MAVN consistently improves the performance of backbone MPNNs, achieving up to 46.5% improvement over the backbones and outperforms the baselines.

---


### 96. [ROBUST-WT: Robust Uncertainty-aware Segmentation Transform via Whitening and Training Enhancements](https://arxiv.org/abs/2606.03069)

**<font color=#1a73e8>作者：</font>** Aqsa Naseer, Maryam Bibi, Syeda Samiya Urooj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized segmentation of medical images prevents performance degradation when different imaging devices and clinical protocols are used across multiple domains. The Whitening Transform-based Probabilistic Shape Regularization Extractor (WT-PSE), published in IEEE Transactions on Medical Imaging in 2024, addresses this challenge by employing feature decorrelation and Wasserstein distance-based knowledge distillation to achieve robust cross-domain segmentation. This study systematically examines improvements to the WT-PSE learning framework. Four limitations in the original implementation are identified: limited training augmentations that fail to simulate real scanner variations, reliance on per-pixel binary cross-entropy loss that is sensitive to edge noise, the absence of a scheduled loss weighting strategy that may destabilize early training, and the lack of ablation switches for controlled scientific comparison. To address these issues, we propose four enhancements: (1) domain-adaptive augmentation including random erasing, gamma correction, and salt-and-pepper noise; (2) a hybrid BCE and Dice loss function for improved edge-aware segmentation under noisy conditions; (3) a curriculum-based Dice weight scheduling strategy; and (4) command-line control flags for systematic ablation studies. Experiments on the fundus optic disc segmentation benchmark demonstrate that the improved pipeline achieves a final epoch optic-disc Dice score of 0.956 and an ASD score of 13.31, outperforming the baseline epoch-5 Dice score of 0.939. These results indicate that training-level improvements can provide consistent performance gains without modifying the underlying WT-PSE architecture.

---


### 97. [RMPrior: Bridging Propagation Priors and Diffusion Refinement for Efficient Radio Map Construction](https://arxiv.org/abs/2606.03074)

**<font color=#1a73e8>作者：</font>** Zixuan Guo, Xiucheng Wang, Nan Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models achieve high-fidelity radio map construction through iterative denoising, yet their sampling cost limits practicality in dynamic wireless systems where radio maps must be refreshed repeatedly. Meanwhile, classical propagation models encode valuable scene-level knowledge that standard diffusion inference discards entirely by initializing from pure Gaussian noise. This paper bridges propagation priors and diffusion refinement through a mid-start sampling strategy. A matched propagation prior is perturbed to an intermediate diffusion timestep, and the pretrained diffusion backbone executes only the remaining reverse steps, focusing computation on multipath-aware refinement rather than full reconstruction from noise. We provide theoretical analysis establishing an upper bound on the initialization gap, a sufficient condition under which truncation improves reconstruction fidelity, and a formal characterization of prior-quality sensitivity under aggressive truncation. Experiments on IRT4HighRes show that, at $P_{\text{start}}=0.5$, the proposed method achieves a $2.01\times$ speedup while simultaneously improving NMSE, RMSE, SSIM, and PSNR over the full-step baseline. A prior-quality ablation across three propagation models of different fidelity confirms that reconstruction quality tracks prior quality, with the sensitivity amplified under shorter reverse trajectories, consistent with the theoretical predictions. These results also suggest that mid-start reconstruction quality can serve as a proxy for ranking the scene-level fidelity of different propagation models.

---


### 98. [Hierarchical Federated Learning with Dynamic Clustering and Adaptive Regularization for Robust Infrastructure Inspection](https://arxiv.org/abs/2606.03084)

**<font color=#1a73e8>作者：</font>** Yuhu Feng, Keisuke Maeda, Takahiro Ogawa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The deployment of data-driven computer vision models for structural health monitoring (SHM) is heavily constrained by the data silo dilemma due to stringent privacy and security regulations. While federated learning (FL) offers a privacy-preserving collaborative alternative, its application to nationwide infrastructure networks is severely hindered by the challenge of ``double heterogeneity'': macro-level physical divergence across disparate structural types and micro-level statistical imbalances within local datasets. To overcome this challenge, this paper proposes a novel hierarchical federated learning framework. The framework orchestrates a synergistic two-tier optimization strategy. At the macro-level, a dynamic gradient-based clustering mechanism autonomously aggregates distributed clients into specialized expert groups based on their structural degradation trajectories, circumventing the need for prior geographical metadata. Concurrently, at the micro-level, an intra-cluster Dynamic Region-Adaptive Proximal Regularization (DRAPR) module computes a real-time statistical Non-IID Intensity Score for each client. By adaptively modulating a proximal penalty based on local label skewness and gradient divergence, DRAPR effectively calibrates local updates, mitigates client drift, and prevents the catastrophic forgetting of minority damage classes. Comprehensive evaluations on a large-scale, real-world structural inspection dataset demonstrate that the hierarchical integration of macro-clustering and micro-regularization successfully neutralizes dual-level heterogeneity, yielding highly robust and specialized diagnostic models for complex infrastructure inspection.

---


### 99. [Learning to Solve, Forgetting to Retain: Correct-Set Turnover in RLVR](https://arxiv.org/abs/2606.03087)

**<font color=#1a73e8>作者：</font>** Chuanyu Qin, Chenxu Yang, Qingyi Si 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves the ability of large language model, yet headline accuracy gains often conceal a hidden cost: previously solved problems quietly become unsolvable as training proceeds. We frame this phenomenon as \emph{correct-set turnover}, representing the coupled dynamics of solution acquisition and regression over the mastered set. Under this view, retention becomes an explicit optimization target alongside acquisition. We analytically and empirically establish the \emph{repair-window principle}: the cost of restoring a regressed prompt grows sharply with review delay, defining a low-cost window that standard RLVR pipelines fail to exploit. To address this, we propose \textbf{\method{}}, a retention-aware review mechanism that tracks mastered prompts and periodically reintroduces them to \textbf{remind} the model of previous solutions. By utilizing pre-rollout batch replacement, \method{} incurs zero additional rollout overhead. Evaluated across 20 benchmarks spanning image-text, video, and text-only tasks with Qwen3-VL and Qwen2.5-Math, \method{} consistently improves performance over GRPO, DAPO, and replay baselines, demonstrating robust generalizability across modalities and algorithms.

---


### 100. [Constitutional On-Policy Safe Distillation](https://arxiv.org/abs/2606.03089)

**<font color=#1a73e8>作者：</font>** Ming Wen, Yuxuan Liu, Kun Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) has emerged as an efficient post-training paradigm by using a teacher conditioned on privileged information to provide dense token-level supervision. Prior work has shown that OPSD can collapse in verifiable reasoning tasks, but safety alignment differs in that it is guided by high-level constitutions rather than explicit target answers, making it a natural setting to revisit dense distillation. However, our pilot study show that safety OPSD still suffers from severe collapse: constitutional conditioning contracts the teacher distribution toward short and overly conservative responses, and Reverse KL further amplifies this contraction into reduced expressiveness. We formalize this effect as geometric leakage under safety boundaries in a non-orthogonal semantic space, where safety pressure transfers into the expressiveness dimension. Based on this analysis, we propose Constitutional On-Policy Safe Distillation (COPSD), which first calibrates the teacher through a Cross-SFT cold-start and then performs constitution-conditioned on-policy distillation. Experiments on 12 benchmarks show that COPSD achieves a consistently stronger safety--helpfulness trade-off than baselines while substantially reducing the safety tax on general reasoning ability.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-312](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

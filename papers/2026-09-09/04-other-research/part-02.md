# 📦 其他研究 | 2026年09月09日

> 本类共 **190** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-190](./part-04.md)

---

### 51. [Why Is SHAP Not a Reliable Standalone Explanation Framework for Malware Detection?](https://arxiv.org/abs/2609.04626)

**<font color=#1a73e8>作者：</font>** Seyedreza Mohseni, Edward Raff, Manas Gaur  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning is widely used for malware detection, but its decisions must be explained. An analyst needs to know whether a model has learned genuine malicious behavior or only dataset-specific patterns \cite{gaur2021semantics}. SHapley Additive exPlanations (SHAP) is the standard tool for this, backed by formal properties such as local accuracy, missingness, and consistency. We argue that these guarantees are insufficient for reliable malware interpretation. We claim SHAP explains a chosen feature-coalition game, not malware behavior in the data. That game is fixed only after the analyst selects the feature players, the missing feature rule, the background distribution, and the simplified input mapping. In static Portable Executable feature spaces, groups such as byte histograms, byte-entropy, strings, headers, sections, imports, and data-directories are not independent signals but are jointly shaped by file structure, packing, compiler behavior, and family conventions. We prove that this dependence makes conditional SHAP dilute a model's feature credit by a factor of $1/m$ across $m-1$ redundant features, attributes importance to features the model never uses, and even reverses the sign of an unused feature's attribution when the data distribution changes; interventional SHAP, meanwhile, queries off-manifold coalitions that no real executable would exhibit. Experiments on EMBER-2018, EMBER-2024, and BODMAS with fixed LightGBM and XGBoost detectors confirm these effects. We therefore position SHAP as a limited diagnostic that requires an explicitly stated data distribution and domain validation, not a standalone account of malware behavior.

---


### 52. [Leveraging Imperfect Restoration for Data Availability Attack](https://arxiv.org/abs/2609.04627)

**<font color=#1a73e8>作者：</font>** Yi Huang, Jeremy Styborski, Mingzhi Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The abundance of online data is at risk of unauthorized usage in training deep learning models. To counter this, various Data Availability Attacks (DAAs) have been devised to make data unlearnable for such models by subtly perturbing the training data. However, existing attacks often excel against either Supervised Learning (SL) or Self-Supervised Learning (SSL) scenarios. Among these, a model-free approach that generates a Convolution-based Unlearnable Dataset (CUDA) stands out as the most robust DAA across both SSL and SL. Nonetheless, CUDA's effectiveness against SSL is underwhelming and it faces a severe trade-off between image quality and its poisoning effect. In this paper, we conduct a theoretical analysis of CUDA, uncovering the sub-optimal gradients it introduces and elucidating the strategy it employs to induce class-wise bias for data poisoning. Building on this, we propose a novel poisoning method named Imperfect Restoration Poisoning (IRP), aiming to preserve high image quality while achieving strong poisoning effects. Through extensive comparisons of IRP with eight baselines across SL and SSL, coupled with evaluations alongside five representative defense methods, we showcase the superiority of IRP. Code: this https URL

---


### 53. [Too Rare to Learn: Prescribed Cyclone Tracks Degrade a Bay of Bengal Ocean Emulator](https://arxiv.org/abs/2609.04635)

**<font color=#1a73e8>作者：</font>** Sumaiya Islam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural ocean emulators are being proposed for regional forecasting in cyclone-exposed coastal seas, and a natural design choice is to hand the network the cyclone as a prescribed input. We test that choice in the Bay of Bengal and find it harmful. We withhold 15 whole cyclones spanning 65 to 150 kt from GLORYS12 reanalysis and compare two U-Nets that are identical except for four prescribed cyclone-track channels. Across three seeds the ocean-only model beats persistence in every run and the storm-conditioned model loses to it in every run, with the two skill ranges disjoint (p = 3.1e-5, paired across storms). The cause is exposure frequency rather than signal content: the channels are non-zero on only 7.9% of training days, so they are out of distribution the moment they activate. The extra error falls inside the prescribed storm footprint, and replacing the real cyclone map with a no-storm map at inference improves held-out storm forecasts by 7.5 to 16.4% in every seed. The conditioned network has learned a response to a rare signal that is confidently wrong.

---


### 54. [SMILE: Bridging Continuous Optimization and Discrete Symbolic Recovery](https://arxiv.org/abs/2609.04639)

**<font color=#1a73e8>作者：</font>** Mansooreh Montazerin, Antonio Ortega, Ajitesh Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR) discovers closed-form mathematical expressions from data, offering interpretability beyond black-box models. Existing methods suffer from slow convergence in combinatorial search spaces and lack mechanisms to exploit compositional structure in the data. We introduce SMILE (Sine, Multiplication, Identity, Logarithm, Exponential), a hybrid framework that unifies continuous gradient-based optimization with discrete symbolic recovery through three stages: structural analysis of the data to identify the compositional hierarchy of the target expression, continuous optimization to learn parameters of a network that encodes the target expression using interpretable activations, and symbolic recovery through structured pruning, coefficient optimization, and rounding. This final stage distills the learned network into a compact expression with exact symbolic constants. We evaluate SMILE on SRBench across ground-truth and black-box datasets, with ablation studies validating each component. SMILE achieves the highest symbolic solution rate at the largest noise levels, demonstrating strong robustness where competing methods degrade substantially. It consistently lies on the Pareto front of accuracy versus complexity, recovering significantly simpler expressions in a fraction of the time required by the competing methods.

---


### 55. [A Cost-Aware Agentic Architecture for NL-to-SQL over Nested Enterprise Schemas, with a New Benchmark](https://arxiv.org/abs/2609.04641)

**<font color=#1a73e8>作者：</font>** Yoga Sri Varshan Varadharajan, Ajay Yadav, Ritesh Goru 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural-language-to-SQL systems have ad- vanced rapidly on academic benchmarks, yet production enterprise schemas exhibit graph- like, semi-structured, deeply nested structure that current benchmarks do not measure. We make two complementary contributions. First, we introduce the DevRev NL2SQL bench- mark: 900 execution-verified queries with nested-type and link-graph structure, accom- panied by the Semantic Depth Score (SDS), a schema-agnostic rubric for analytical reasoning depth. Second, we present a cost-aware single- generation agentic architecture whose schema- selection, metadata-retrieval, and error-repair components are designed for the requirements this regime imposes. On the DevRev NL2SQL benchmark the system attains 91.7% answer correctness, a margin of 54.6 percentage points over the next-best baseline; on the Spider 2.0 Snowflake public dataset, it is competitive with leading systems at a single-generation operating point.

---


### 56. [ReaDiT Guidance: Control for Image and Video Generation using Diffusion Transformer Features](https://arxiv.org/abs/2609.04649)

**<font color=#1a73e8>作者：</font>** Jay Mahajan, Chang Liu, Rauf Makharov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present DiT Readout (ReaDiT) Guidance, a lightweight framework for controlling generation with Diffusion Transformer (DiT) models via their internal feature representations. ReaDiT Guidance uses features from a single DiT block to steer the generative process according to spatial targets - like depth, pose, or edge maps - provided at test time. Furthermore, since modern text-to-video models are largely built on DiT backbones, ReaDiT Guidance naturally extends to video generation, enabling camera and motion control. Experimental results demonstrate that our approach achieves competitive or improved results compared to existing feature-based and off-the-shelf adapter-based approaches while requiring fewer parameters.

---


### 57. [Interpretability for Turing Machines](https://arxiv.org/abs/2609.04661)

**<font color=#1a73e8>作者：</font>** Billy Snikkers, Rumi Salazar, Daniel Murfet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that susceptibilities, an interpretability technique developed for neural networks, can identify the presence of algorithmic structure in Turing machines by probing the local loss landscape of a learning problem for noisy Turing machines introduced by Murfet and Troiani (arXiv:2504.08075). We prove that symmetries and path separation in the algorithm implemented by a Turing machine induce permutation symmetries and low-rank blocks in its susceptibility matrix. We study this empirically on a set of deterministic finite automata (DFAs) and demonstrate that algorithmic features can be recovered by principal component analysis and clustering methods in susceptibility space.

---


### 58. [WEECFP-SuRGE: Wide Embedded Extended Connectivity Fingerprint with Substructure Rotary Graph-distance Encoding](https://arxiv.org/abs/2609.04672)

**<font color=#1a73e8>作者：</font>** Robert Epps  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce WEECFP, a parameter-free 1024-dimensional continuous molecular fingerprint that scatters each Morgan substructure across roughly thirty-two signed positions of a single vector, and WEECFP-SuRGE, a transformer architecture whose self-attention applies SuRGE (Substructure Rotary Graph-distance Encoding) -- a RoPE-like rotation parameterized by molecular shortest-path graph distance -- to WEECFP substructure tokens. A 7-model blend of this architecture (the WEECFP-SuRGE Blend) achieves the lowest average regression rank on the TDC ADMET leaderboard; is #2 overall on the TDC ADMET leaderboard (behind only pretrained MapLight+GNN), and is #1 overall among methods that use no external pretraining; takes leaderboard #1 finishes on Pgp, Lipophilicity, CYP2D6 Substrate, Clearance Microsome, and LD50 (with the WEECFP-NoSuRGE Blend separately reaching #1 on HIA) across the full 22-benchmark suite -- without any external pretraining. On MoleculeNet, WEECFP-SuRGE beats every classical-fingerprint baseline on 3 of 4 regression tasks (ESOL, Lipophilicity, QM9). We further show that WEECFP tokenization is near-lossless: a greedy overlap reconstruction recovers the exact canonical SMILES of 99.9% of in-distribution molecules across 9 MoleculeNet datasets and 98.93% of molecules in a cross-dataset holdout (HIV->Lipophilicity), and that a three-reference farthest-first encoding of graph distance correlates at Pearson r = 0.901 with the true pairwise distance, enabling O(S) positional memory at matching accuracy.

---


### 59. [Train What You Deploy:Token-Faithful Post-Training of a Production Coding](https://arxiv.org/abs/2609.04678)

**<font color=#1a73e8>作者：</font>** Cheng Li, Jiexiong Liu, Yixuan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing post-training pipelines for coding and terminal agents suffer severe token and control fidelity errors: simplified training environments mismatch production deployments, and offline token reconstruction from agent logs distorts original prompts and conflates policy calls with background model operations. We present a fidelity-aware training coupling framework that retains trainer-side sampling over original prompts, eliminates spurious model calls via a negotiated training protocol, and restricts loss computation to verifiable token spans with closed-failure guarantees. We further propose Certified Divergence Proximal Policy Optimization (C-DPPO), which establishes tight two-sided TV certification bounds, adaptive-K rules, budget-aware sequence guarantees, and error-robust policy masking atop standard DPPO. Evaluated on matched Baize5B and Baize10B models with identical training and test protocols on TMax-100, C-DPPO yields a consistent +3.0-point performance gain over standard DPPO across model scales. Certificate audits validate the reliability and full operational coverage of our certified training pipeline.

---


### 60. [Beyond Prompt-to-App: Accountable Translation in Teacher-Facing Agentic Authoring](https://arxiv.org/abs/2609.04679)

**<font color=#1a73e8>作者：</font>** Nizam Kadir, Wei Ting Liow, Sumbul Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Natural-language app builders let domain experts create software, but their pipelines transform professional intent across compilation, generation, checking, and approval. We report a bounded trace study of a teacher-facing agentic authoring system. Evidence comprises six eligible build attempts across three accounts; a separate corpus of 37 workshop units from 23 display names contextualizes commitments without person-level linkage. Compiled specifications added governance requirements, while downstream representations sometimes normalized case-specific learning relations. Two drafts met a stored package/security threshold despite analyzer reservations and unresolved correspondence to their briefs; four attempts in one account produced no usable payload, and repair messages did not translate internal terms into domain-legible revisions. We develop accountable translation as an analytic framework for making consequential changes attributable, inspectable, scoped in validation, and contestable. It extends HCI accounts of traceability and end-user debugging by locating professional authority and repair rights across heterogeneous technical and organizational handoffs.

---


### 61. [Enhancing Multimodal Emotion Recognition via Multi-Feature Encoding and Attention-Based Fusion](https://arxiv.org/abs/2609.04690)

**<font color=#1a73e8>作者：</font>** Xu Lin, Ke Wang, Hui Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal emotion recognition has attracted growing interest due to its importance in human-computer interaction, remote education, and healthcare. This paper proposes a novel multimodal emotion recognition framework that integrates rich audio and visual feature extraction with an attention-based fusion strategy. For audio, we extract three complementary feature types: semantic embeddings from Wav2Vec2, MFCC features, and statistical acoustic descriptors such as pitch, energy, and rhythm. These are aligned and fused via a BiLSTM to capture temporal dependencies. For video, we propose a ResNet50-BiLSTM architecture that combines deep residual learning and sequential modeling to extract expressive spatiotemporal features from facial sequences. To enhance multimodal synergy, we introduce a feature-level fusion mechanism based on multi-head attention, allowing the model to adaptively weigh contributions across modalities. Experiments conducted on the MELD and IEMOCAP datasets demonstrate that our model significantly outperforms baselines in both accuracy and robustness. Furthermore, ablation studies show that the attention-based fusion strategy significantly improves performance in unbalanced data settings. Our findings suggest that the proposed framework effectively captures diverse emotional cues from speech and visual expressions, and offers a practical and generalizable approach for real-world multimodal emotion recognition tasks.

---


### 62. [Predicting Spatiotemporal Mobile Sensing-Based PM2.5 Concentrations Using Low-Rank Adapted Spatially Attentive Graph Neural Network](https://arxiv.org/abs/2609.04693)

**<font color=#1a73e8>作者：</font>** Om Chiddarwar, Priyanka Mandal, Praveen Kumar Chandaliya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban air quality can vary significantly along transit corridors, necessitating high-resolution monitoring. This work introduces a novel mobile-sensing dataset from Surat, Gujarat, India, comprising PM$*{2.5}$ concentrations, meteorological variables (temperature, humidity, wind speed, wind direction), and land-use features. To represent the spatiotemporal data as a graph, two node-definition strategies were used: (i) uniform segmentation (200--400~m intervals) and (ii) DBSCAN clustering to adaptively group dense observations. For each node, rolling mean and standard deviation of meteorological variables were computed. To model this high-dimensional data, we propose a SA-GNN for fine-grained, short-term PM$*{2.5}$ forecasting and hotspot identification. We compared SA-GNN with LSTM, RNN, GRU, and ANN models. These models performed well on low-resolution data but had difficulty capturing rapidly changing patterns in urban air quality. SA-GNN employs cluster-specific GRUs to capture localized temporal dependencies and a Graph Attention Network to learn spatial heterogeneity. This hybrid architecture effectively models rapid fluctuations and complex spatial interactions. On our dataset, SA-GNN achieved $R^2 = 0.95$, RMSE $= 6.8$, and MAE $= 4.2~\si{\micro\gram\per\meter\cubed}$, outperforming all baseline models. Combining spatial clustering with adaptive attention significantly improves forecasting, enabling real-time, fine-grained monitoring and supporting personalized exposure tracking and timely alerts for healthier cities.

---


### 63. [LookThere! Sparse Vision by Reinforced Selection](https://arxiv.org/abs/2609.04698)

**<font color=#1a73e8>作者：</font>** Sreehari Rammohan, Yousef Yassin, Anthony Fuller 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision transformers typically treat every image token as equally important, yet for most tasks in computer vision only a fraction are needed. Adaptive computation methods accelerate inference by choosing which tokens to process, but existing methods struggle at extreme sparsity and require heuristics that may not generalize like token diversity and attention scores. We address these limitations with LookThere, achieving a new pareto frontier in performance-compute trade-offs through an end-to-end reinforcement learning framework that jointly trains a shallow input selector and a deep representation extractor. The selector learns where to look and the extractor learns what to see, together saving computation by selecting only what is worth processing for a given task without relying on auxiliary signals. We show that LookThere only selects the task-specific input, excelling at sparse recognition in high-resolution settings (traffic signs, billiards), and maintaining accuracy with as little as 0.2% of the input. It generalizes across tasks and models, including global recognition (ImageNet classification), local recognition (ADE20K segmentation), zero-shot classification (by distillation), and regression (counting). Across all settings, LookThere surpasses state-of-the-art selection to provide a general and scalable framework for specialized and efficient adaptive computation.

---


### 64. [AngelFingerprint: A Traceable, Explainable, and White-Box Stealthy Watermark for Text-Guided Image Editing](https://arxiv.org/abs/2609.04709)

**<font color=#1a73e8>作者：</font>** Bo-Han Kung, Futa Waseda, Ching-Chun Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided diffusion editing raises disinformation concerns, making reliable image provenance essential. While watermarks are commonly used for this purpose, most methods carry a fixed ID that cannot explain what was changed and which prompt produced it. Furthermore, under open-source white-box access, attackers can easily locate and remove watermarks added as separate modules. Targeting this setting, we propose AngelFingerprint, a novel watermarking framework ensuring edit traceability, explainability, and white-box stealthiness. It integrates a LoRA into the diffusion model to embed the editing prompt's CLIP text embedding directly into the model's weights. An extractor then recovers this embedding from the image pixels alone. This semantic payload explains the edit, while the weight-integrated design makes it hard to detect and isolate even under full white-box access. Two techniques make this possible: a velocity-alignment anchor that preserves edit quality, and a specially designed frequency filter that keeps the watermark imperceptible yet recoverable and robust. On the MagicBrush dataset, our extractor achieves $86\%$ top-1 accuracy in a 200-way prompt retrieval, versus $20\%$ for prompt inversion.

---


### 65. [Simulation-free Unbalanced Dynamic Optimal Transport with General Growth Penalty](https://arxiv.org/abs/2609.04710)

**<font color=#1a73e8>作者：</font>** Junda Ying, Yuxuan Wang, Bowen Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring cellular dynamics from unpaired single-cell snapshots requires modeling both state transitions and population growth or death. Unbalanced dynamic optimal transport (UDOT) addresses this by penalizing growth along transport paths, making the choice of growth penalty a key way to encode biological priors on proliferation and apoptosis. However, existing UDOT solvers either rely on computationally expensive NeuralODE simulations or depend on analytical solutions of conditional paths, restricting their efficiency solely to quadratic penalties, i.e. Wasserstein-Fisher-Rao (WFR) geodesics. To enable an efficient UDOT solver for general growth penalties, we first show that concave growth penalties lead to degenerate solutions where growth and transport are separated. We then introduce \textbf{S}imulation-free \textbf{U}nbalanced \textbf{D}ynamic \textbf{O}ptimal transport (SUDO), a simulation-free framework for UDOT with general non-quadratic convex growth penalties. SUDO learns the conditional paths and transport costs, solves the induced semi-coupling problem, and subsequently leverages unbalanced flow matching to achieve a simulation-free solution. On WFR benchmarks, SUDO matches the accuracy of efficient, analytical solution-driven algorithms while outperforming simulation-based methods in computational speed. Beyond WFR, SUDO supports asymmetric penalties that encode proliferation-dominant priors and produce more plausible trajectories and growth estimates on synthetic and single-cell datasets.

---


### 66. [Counting Beyond Instances: A Benchmark for Group-Individual Object Counting](https://arxiv.org/abs/2609.04716)

**<font color=#1a73e8>作者：</font>** Rui Wang, Junyi Huang, Jiahui Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual counting is commonly formulated at the instance level, aiming to estimate how many objects of a queried category appear in an image. However, real-world counting often involves higher-level semantic units formed by multiple instances, such as a bunch of grapes, a stack of plates, or a pair of shoes. This exposes a key limitation of existing counting formulations, which mainly focus on what to count, while largely overlooking at which semantic unit to count. We introduce Group-Individual Object Counting (GIC), a new setting that requires models to count both individual objects and semantic groups within a unified framework. To support this new task, we present BunchCount, a real-world benchmark with 1,330 images, 89,254 individual annotations, and 11,065 group annotations. BunchCount provides paired individual-group annotations within the same image and explicitly records containment relations between each group and its constituent individuals. Experiments on BunchCount show that current advanced counting models perform well on individual instances but fail to count semantic groups more accurately. To mitigate semantic granularity conflict, we propose a counting-unit guided relational counting framework, which exploits group-individual containment relations to regularize cross-granularity representations during training. Our method substantially improves group-level counting while better preserving individual-level counting ability, establishing a strong baseline for counting beyond instances.

---


### 67. [HiSfM: Disambiguating Structure-from-Motion via Scaffold-Anchored Hierarchical Reconstruction](https://arxiv.org/abs/2609.04718)

**<font color=#1a73e8>作者：</font>** Ziding Zhao, Hainan Cui, Peilin Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structure-from-Motion (SfM) is a fundamental tool for sparse 3D reconstruction with broad impact in robotics and vision, supporting mapping, localization, and large-scale scene modeling. However, conventional pipelines often fail under hard visual ambiguity caused by repeated or symmetric structures, and incur heavy computational cost due to redundant cameras and constraints. We present HiSfM, a hierarchical coarse-to-fine SfM framework that improves robustness and efficiency through scaffold construction. HiSfM first forms strong local communities using geometrical induced heuristics, then connects communities with a compact yet strong skeleton by packing edge-disjoint spanning trees (EDST) while verifying skeletal edges with a two-view disambiguator. We reconstruct a stable scaffold on this verified skeleton, serving as an anchor to capture the essence of the scene, and subsequently absorb remaining images via efficient registration and triangulation for further refinements. Experiments on ambiguity-focused benchmarks and general datasets show that HiSfM prevents ambiguity-induced failures while substantially reducing runtime compared to previous methods, and improves completeness over aggressive sparsification methods. Code is available at this https URL.

---


### 68. [Bridging Modalities and Tasks: A Unified Hierarchical ViT for SAR-to-Optical Translation and Semantic Segmentation](https://arxiv.org/abs/2609.04726)

**<font color=#1a73e8>作者：</font>** Siyuan Liu, Xuze Zhang, Yongshun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic Aperture Radar (SAR) images have all-weather, day-and-night observation capabilities. However, compared with optical images, their speckle noise and non-intuitive scattering mechanism limit the interpretability of the images. Generative models for SAR-to-optical (S2O) conversion can improve visual interpretability, but existing methods often ignore the constraints on semantic structure, which are necessary for downstream tasks, for the sake of visual effects. We propose a unified collaborative dual-task learning framework, termed BMT (Bridging Modalities and Tasks), that jointly optimizes S2O image translation and semantic segmentation through a shared hierarchical Vision Transformer. The framework integrates: (1) a LocalViTBlock that fuses global self-attention with spatial depthwise convolution through a learnable gating mechanism; (2) an enhanced output module combining multi-scale refinement processing, color correction and anti-aliasing, which calibrates channel-level color statistics through feature fusion; (3) a ControlNet-style conditional injection mechanism that encodes SAR wavelet features and segmentation labels into a multi-scale feature pyramid and injects them at each encoder layer through zero-initialized convolution; (4) a bounded Kendall uncertainty weighting scheme that prevents either task from dominating the shared representation. We evaluate the framework under both paired and unpaired translation settings, on the public WHU-OPT-SAR paired dataset and a self-constructed unpaired ship dataset built from HRSID and DIOR, respectively. The experimental results show that the proposed method achieves competitive S2O translation quality and semantic segmentation performance. The dataset and source code have been publicly released at this https URL.

---


### 69. [SeamFlow: Structure-Aware Flow Matching on Edge Probabilities for Artist-Like UV Unwrapping](https://arxiv.org/abs/2609.04751)

**<font color=#1a73e8>作者：</font>** Yuming Zhao, Zangyueyang Xian, Qijian Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D surface cutting and UV unwrapping are fundamental problems in computer graphics. Traditional geometric optimization methods mainly focus on reducing parameterization distortion, but they often overlook visual semantic coherence in seam layouts. Recent autoregressive generative methods improve semantic coherence, yet limited perception of mesh topology often causes inaccurate local cuts. To address these limitations, we introduce SeamFlow, a novel generative framework for 3D surface cutting. We reformulate the discrete mesh-cutting problem as continuous flow matching in a high-dimensional edge-probability space. Through continuous relaxation, SeamFlow learns a deterministic mapping from a Gaussian prior to a target seam-probability distribution. An evolution network couples local topological tokens with global shape priors and guides smooth probability flow through Ordinary Differential Equation solving. Compared with existing autoregressive generative frameworks, SeamFlow improves topology awareness through edge tokenization while eliminating both 3D spatial projection errors and artificial sequential-order bias. Extensive experiments demonstrate that SeamFlow achieves exceptional semantic coherence and remarkably low parameterization distortion. The project page is this https URL.

---


### 70. [A Fairness Audit of the Duckworth-Lewis-Stern Method: Format-Specific and Gender-Differential Bias, with an Interpretable Calibration Layer for Cricket Target Revision](https://arxiv.org/abs/2609.04754)

**<font color=#1a73e8>作者：</font>** Soumyadeep Roy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Duckworth-Lewis-Stern (DLS) method has been the international standard for revising target scores in rain-interrupted limited-overs cricket since 1999. Despite over two decades of operational use, no large-scale empirical audit of its prediction bias has been published. We conduct such an audit on 8,150 international matches (3,095 ODIs, 5,055 T20Is) from Cricsheet, generating 233,550 synthetic interruption scenarios with temporal splits. We document two structured biases. First, DLS prediction error spans a 137-run range across (overs-remaining, wickets-lost) match-state buckets. Second, DLS exhibits a gender-differential bias on ODIs that has not previously been quantified: on the training split, mean over-prediction is +1.51 runs for men but +7.63 runs for women, a gap of +6.13 runs (F = 195.16, p < 10^-43). We benchmark DLS against five modern alternatives: Bi-LSTM, XGBoost, an enriched XGBoost variant, a deep context-aware model, and a stacking ensemble, and propose DLS-Cal, a lightweight interpretable calibration layer (27K parameters) outputting a state-conditioned correction added to DLS. DLS-Cal reduces absolute bias by 31% on ODI and 19% on T20I, and a gender-aware variant reduces women's ODI residual bias from +6.19 to +0.65 runs while leaving men's calibration unchanged. We release code, models, and data.

---


### 71. [Resilience Beyond Stationary Client Unavailability: Unlocking Efficient and Unbiased Federated Learning](https://arxiv.org/abs/2609.04763)

**<font color=#1a73e8>作者：</font>** Ming Xiang, Stratis Ioannidis, Edmund Yeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Due to resource constraints or external and internal uncertainties, clients in real-world federated learning systems are often intermittently available edge devices. In highly dynamic environments, the parameter server lacks prior real-time knowledge of clients' availability, making it challenging to adapt traditional federated learning algorithms to be resilient to uncertainties in client availability. If not carefully addressed, complex client availability can introduce significant bias, potentially harming the performance of the trained model. Most prior work either fails to account for non-stationary client availability dynamics or demands significant memory and computational overhead. This paper aims to develop efficient federated learning algorithms that are provably resilient to heterogeneous and non-stationary stochastic client availability. We propose FedSWE, which admits novel algorithmic structures to (i) compensate for missed computations, (ii) stabilize and diffuse the global updates over rounds, and (iii) evenly mix the local updates through implicit gossiping, despite being agnostic to non-stationary dynamics. Compared with the standard FedAvg, FedSWE introduces light additional memory and computation overhead. We show that FedSWE converges to a stationary point of non-convex objectives while achieving the desired linear speedup property in certain special cases. We corroborate our analysis with numerical experiments over diversified client unavailability dynamics on real-world data sets.

---


### 72. [Memory-Efficient Designs for Word-Wise Universal Fully Homomorphic Encryption](https://arxiv.org/abs/2609.04769)

**<font color=#1a73e8>作者：</font>** Ardhi Wiratama Baskara Yudha, Erwin Eko Wahyudi, Rian Adam Rajagede 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully Homomorphic Encryption (FHE) enables computation on encrypted data, preserving privacy throughout analysis. While its privacy is very strong, FHE is much slower to execute than the original computation. In particular, due to the recent success in accelerating its compute, the performance bottleneck shifts to the memory, especially considering that FHE magnifies the data size by orders of magnitude, resulting in a low arithmetic intensity.
We propose BXT, an FHE optimization framework that mitigates the memory bottleneck through four techniques: (1) ciphertext compression, which regenerates ciphertext components from seeds during execution; (2) ciphertext serialization, which packs coefficients as bit arrays and unpacks them during L2-to-L1 transfer; (3) delayed seed generation, which defers PRNG-heavy offline work across aggregated operations; and (4) ciphertext digit pruning guided by fault-aware training tailored for Universal FHE. On CNN inference, the BXT-CSO50 configuration effectively achieves up to 3.8$\times$ speedup over the 100x GPU baseline with less than 1% accuracy loss at 50% comparison precision.

---


### 73. [A Robust Watermark-based Fingerprint Framework for GNNs Ownership Verification](https://arxiv.org/abs/2609.04772)

**<font color=#1a73e8>作者：</font>** Han Zhang, Yan Wang, Guanfeng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The high training cost of Graph Neural Networks (GNNs) has raised growing concerns regarding model ownership infringement, such as model stealing and unauthorized misuse. To verify model ownership and prevent significant economic losses, two groups of GNN Ownership Verification (OV) methods have been proposed: watermark-based methods and fingerprint-based methods. However, these methods typically face three limitations: (1) the performance degradation of protected models caused by out-of-distribution (OOD) watermark graphs with respect to the training set; (2) the unrealistic assumption that surrogate models have been trained on a watermark-containing training set; and (3) over-reliance on specific output levels for fingerprint extraction. In this paper, we propose a Robust watErMArk-based fingeRprint frameworK for GNNs, named REMARK. REMARK first generates carefully crafted in-distribution watermark graphs that maximize output differences between GNN models, thus mitigating OOD-induced performance degradation. REMARK then extracts robust fingerprints from these output differences to verify GNN ownership, thereby removing the assumptions that surrogate models must be trained on a watermark-containing dataset or expose specific output levels. Extensive experiments across widely used real-world datasets and GNN architectures demonstrate that REMARK achieves state-of-the-art OV accuracy and robustness while preserving the utility of protected models.

---


### 74. [LUMIN: Lightweight Universal Manufacturing Inspection Network for Anomaly Detection](https://arxiv.org/abs/2609.04775)

**<font color=#1a73e8>作者：</font>** Pengfei Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection faces two engineering bottlenecks: memory bank construction latency and inference efficiency. Traditional sampling algorithms (Farthest Point Sampling, K-Means, etc.) rely on numerous backbone forward passes and iterative distance computations, with construction times ranging from minutes to hours; heavy computation components such as multi-scale feature extraction struggle to meet the millisecond-level real-time requirements of production lines. This paper focuses on sampling efficiency and inference optimization for industrial deployment with two core contributions: (1) PSP (Plugin Sampler Pipeline)---a four-stage adaptive memory bank sampling pipeline based on 18-dimensional pixel metadata and five complementary visual plugins. PSP completes all sampling with zero backbone forward passes; coarse filtering is sub-second numerical sorting, and metadata extraction is a one-time offline cost. PSP supports progressive deployment and incremental updates. (2) Two engineering optimization strategies---parallel memory bank similarity computation (reducing inference memory and latency by over 95\%) and stratified pixel sampling for large-scale evaluation (reducing computation time by 20$\times$ while keeping metrics stable). As a vehicle for validation, we introduce LUMIN (Lightweight Universal Manufacturing Inspection Network) with extreme segmentation-head compression, systematically exploring the accuracy-efficiency frontier against strong baselines. Experiments on five benchmarks demonstrate that PSP matches state-of-the-art sampling accuracy at near-random construction cost (341$\times$ faster than FPS), while inference optimizations reduce evaluation time by 20$\times$ with negligible accuracy loss.

---


### 75. [Dynamic Heterogeneous Graph Representation Learning: A Survey](https://arxiv.org/abs/2609.04779)

**<font color=#1a73e8>作者：</font>** Huan Liu, Pengfei Jiao, Jie Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph representation learning (GRL) serves as a canonical paradigm for modeling complex networks. However, real-world AI systems inherently manifest as evolving heterogeneous entities with complex interactions, posing significant challenges to static or homogeneous modeling. To address these complexities, representation learning for Dynamic Heterogeneous Graphs (DHGs) has emerged as a vital approach for learning low-dimensional representations that simultaneously preserve structural semantics and temporal dynamics. This survey presents the first systematic review of DHG representation learning methods. We first introduce a unified formal definition that encompasses both discrete-time and continuous-time DHGs from the perspective of temporal granularity. Building upon this formulation, we propose a novel algorithm-centric taxonomy that categorizes existing literature, including early embedding-based approaches, graph neural network (GNN)-based models, and relatively recent Transformer-based DHG methods, while explicitly highlighting their intrinsic modeling biases with respect to dynamic granularity. Furthermore, we summarize representative applications of DHG representation learning, along with commonly used datasets and benchmarks. Finally, we discuss promising research directions that guide future advances in this rapidly evolving field.

---


### 76. [CoMLP: Cooperatively-Gated MLPs for Fine-Grained Cross-Modal Information Fusion in Medical Image Segmentation](https://arxiv.org/abs/2609.04781)

**<font color=#1a73e8>作者：</font>** Mingyuan Meng, Shuchang Ye, Mingjian Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal medical images and clinical reports provide complementary anatomical, functional, and semantic information for medical image segmentation. Effectively exploiting these heterogeneous sources requires fine-grained cross-modal information fusion that preserves subtle spatial details while capturing semantic dependencies across modalities. Existing fusion approaches frequently rely on cross-attention, whose computational burden increases rapidly with spatial resolution, making dense cross-modal interaction difficult on high-resolution feature maps, particularly for volumetric medical images. In this work, we propose CoMLP, a cooperatively-gated MLP module for fine-grained cross-modal information fusion in medical image segmentation. CoMLP models cross-modal dependencies through cooperative cross-gating, built upon complementary regional and dilated MLP interactions, to capture local and global cross-modal dependencies. We further develop a multi-source fusion architecture in which CoMLP performs both inter-image fusion across imaging modalities and vision-language fusion between visual features and textual reports, enabling heterogeneous information to be integrated without relying on dense cross-attention. Extensive experiments on five medical segmentation benchmarks, covering 2D/3D images, clinical reports, multiple imaging modalities, and diverse anatomical regions, demonstrate consistent improvements over state-of-the-art multi-modal and language-guided segmentation methods. Ablation studies further show that fine-grained interaction at high spatial resolutions and complementary local-global fusion are critical to the performance gains. These results demonstrate the potential of MLP-based interaction as an effective alternative for fine-grained cross-modal information fusion in medical image segmentation.

---


### 77. [CLON: Cue-Calibrated Linguistic Object Onboarding for Zero-Shot 6D Pose Front-Ends](https://arxiv.org/abs/2609.04784)

**<font color=#1a73e8>作者：</font>** Seojin Ji, Yoojin Kwon, Hyung-Sin Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot 6D pose estimation pipelines increasingly rely on strong downstream pose solvers, but their performance is often limited by the front-end: object proposals must preserve partially visible true positives while rejecting semantically plausible distractors. We introduce Cue-Calibrated Linguistic Object Onboarding (CLON), a front-end requiring no task-specific training for new objects. Given rendered templates of the onboarded object set, CLON constructs a linguistic semantic memory for top-down proposal generation and object-set cue weights for calibrated proposal scoring. The linguistic memory guides SAM 3 toward high-recall proposals for onboarded objects, while cue weights are computed once from the onboarded object set before scene inference and kept fixed during online scoring. On seven BOP-Classic-Core datasets, CLON improves detection AP by 8.1 percentage points (pp), segmentation AP by 6.2 pp, and downstream 6D pose AR by up to 4.1 pp over CNOS and SAM-6D front-ends.

---


### 78. [Injected and Leaked: Actively Inducing Side-Channel Leakage Using Electromagnetic Injection and Hardware Nonlinearity](https://arxiv.org/abs/2609.04785)

**<font color=#1a73e8>作者：</font>** Haoran Yan, Ziyu Shao, Shuhao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Electromagnetic (EM) side-channel leakage and injection are typically treated as distinct physical phenomena, threatening data confidentiality and integrity respectively. This work investigates how EM injection can be used to amplify side-channel leakage that is otherwise infeasible. We introduce a novel framework for Injection-Induced EM Side Channels to enable integrated, closed-loop EM security analysis. Our theoretical modeling and experimental measurements reveal that nonlinear hardware components, such as ubiquitous amplifiers, analog-to-digital converters, and power converters, can modulate secret electrical signals onto an injected EM carrier and thus upconvert low-frequency secrets into measurable EM emissions. By tuning the injection frequency and amplitude, adversaries gain the ability to actively shape the effective spectrum and entropy of the resulting leakage. We design InjectEave attack and demonstrate eavesdropping on the audio played through wired and wireless headphones from up to 30 m away with accessible RF equipment, as well as in through-wall scenarios, and characterize injection-induced EM leakage of other low-frequency secrets such as power consumption of smart home devices and analog sensor inputs. Case studies further demonstrate how the proposed techniques enable closed-loop eavesdropping and manipulation of landline-phone conversations. Finally, we analyze the broader security challenges and mitigations.

---


### 79. [Learning-Augmented Algorithms: Guarantees, Construction Mechanisms, and System-Level Implications](https://arxiv.org/abs/2609.04787)

**<font color=#1a73e8>作者：</font>** Hailiang Zhao, Peng Chen, Xueyan Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-augmented algorithms use fallible predictions while retaining formal performance guarantees. This survey synthesizes prediction interfaces, error measures, consistency--robustness trade-offs, and five representative construction mechanisms across online optimization, caching, learned data structures, graph problems, and mechanism design. An orthogonal theorem-level axis distinguishes achieved upper bounds from matched asymptotic dependence. Formal guarantees are separated from empirical systems evidence, with explicit treatment of prediction cost, feedback, and composition. The resulting synthesis states sufficient conditions for limited end-to-end reasoning and delineates open problems in cost-aware prediction, endogenous error, semantic predictors, and benchmarking.

---


### 80. [An Attention-Guided Global and Local Fusion Framework for Lesion-Focused Image Classification](https://arxiv.org/abs/2609.04791)

**<font color=#1a73e8>作者：</font>** Mst Shafia Tasnima, Md Samaun Elaheea, Tanjim Taharat Aurpab 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lesion-focused image classification presents a core analytical challenge, as discriminative signals are often sparse, spatially dispersed, and easily obscured by background noise, while conventional convolutional neural networks (CNNs) process entire images uniformly and may dilute signal relevance. This study hypothesizes that adaptive fusion of global contextual information and lesion-focused local information can improve classification performance compared with using either representation independently. We propose a three-branch, attention-guided deep learning framework built on Densely Connected Convolutional Network-121 (DenseNet-121) to improve feature attribution, interpretability, and classification reliability. The architecture consists of a global branch that learns representations from full images, followed by Gradient-weighted Class Activation Mapping (Grad-CAM) to generate attention maps that highlight prediction-relevant regions and produce masked inputs, and a local branch enhanced with a Convolutional Block Attention Module (CBAM) to extract refined spatial and channel-wise features from these focused regions. An adaptive fusion branch integrates global and local representations by learning instance-specific weights, allowing dynamic prioritization between contextual and localized information. The framework is evaluated on a synthetic Spot Pattern Dataset (SSPD) and three benchmark datasets, including skin lesion, guava leaf, and grape leaf image datasets, where the fusion branch outperformed the individual global and local branches, reaching 97.75% accuracy on the skin lesion dataset and 99.64% on the guava leaf dataset. The results highlight the value of attention-guided architectures in healthcare analytics by improving model transparency, strengthening feature relevance, and supporting more reliable data-driven decision-making in medical image analysis.

---


### 81. [How Faithful Is Attribution for Sales Forecasting? A Counterfactual Study](https://arxiv.org/abs/2609.04797)

**<font color=#1a73e8>作者：</font>** Glib Kechyn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep models for sales forecasting, such as WaveNet-style dilated convolutional networks, are accurate but opaque: when a single model predicts sales for one of many series, it offers no account of why. We add a post-hoc, architecture-agnostic counterfactual interpretability layer to a multi-series WaveNet forecaster trained on the full Corporacion Favorita grocery dataset (174,685 series over 1,688 days). The method decomposes each forecast into contributions that sum exactly to the predicted value, avoiding the allocation artifacts we observed with additive SHAP-style attribution. We evaluate faithfulness with a deletion/insertion protocol and find a statistically significant effect on both tests (deletion gap 0.22, p<0.001; insertion gap 0.27, p<0.01; robust across five background-sampling seeds), establishing that the attributions reflect genuine model behavior rather than plausible-looking artifacts. We then characterize, honestly, where attribution is and is not informative: reliance on the promotion signal is heterogeneous across series (median ratio approximately 1.0, with roughly 20% of series showing a strong effect), and the model captures the shape of the weekly sales cycle (day-of-week r=0.78) while systematically under-predicting its amplitude. Our contribution is not improved accuracy but an interpretability layer with a rigorous faithfulness evaluation and a candid account of its limits.

---


### 82. [Intrinsic Temporal Adaptation of CLIP for Partially Relevant Video Retrieval](https://arxiv.org/abs/2609.04800)

**<font color=#1a73e8>作者：</font>** Hyun Seok Seong, Woojin Jun, SuBeen Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Partially Relevant Video Retrieval (PRVR) aims to retrieve untrimmed videos that contain moments relevant to a text query. Since the target moment occupies only a portion of the video, PRVR requires retrieval based on fine-grained understanding beyond coarse video-level matching. However, existing methods often rely on frozen CLIP frame features, which lack temporal understanding. Even with recent progress in parameter-efficient CLIP adaptation, video-level predictions can still be supported by imprecise frame-level evidence. In this paper, we propose an Intrinsic Temporal Adaptation (ITA) framework for PRVR. First, our Backbone-Internal Temporal Adaptation allows the last few visual transformer layers to attend over groups of neighboring frames. This provides temporally aware frame embeddings while keeping CLIP frozen and training only adaptation parameters. Second, we introduce Affinity-Weighted Gradient Propagation to address the weakly supervised nature of PRVR, softly aggregating top-$k$ frames based on text-frame affinities and propagating learning signals to multiple query-relevant frames. Our method achieves state-of-the-art performance on PRVR benchmarks, demonstrates robust cross-dataset transfer, and retrieves substantially more accurate frame-level evidence within ground-truth query-relevant moments. Our code is available at this http URL.

---


### 83. [Hierarchical Possession-Aware Graph Pointer Network for Pass Receiver Selection](https://arxiv.org/abs/2609.04803)

**<font color=#1a73e8>作者：</font>** Jingyi Wang, Da Li, Kaixin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pass receiver selection is a fundamental task in football analytics, aiming to predict the intended receiver under a given game state. This task is challenging with event-centered freeze-frame observations, a broadcast-like setting that provides only partial and variable player visibility without complete trajectories or stable player identities. The model must therefore reason over anonymous visible candidates, opponent pressure, and recent context under partial observation. To address this setting, we propose a Hierarchical Possession-aware Graph Pointer Network (HPGPN), which formulates pass receiver selection as variable-size candidate prediction over visible teammates. HPGPN jointly models current player interactions, local event context, and possession-level temporal dynamics. It represents the current pass situation with a graph, incorporates fixed event context, and uses dynamic possession history to capture how the attacking sequence evolves. Candidate representations are refined hierarchically by integrating spatial, contextual, and historical evidence, and a glimpse pointer head scores the receiver candidates. Experiments on public football event and freeze-frame data show that HPGPN improves pass receiver selection performance. Ablation studies demonstrate the effectiveness of graph-based interaction modeling, fixed event context, and dual-branch dynamic possession-history modeling.

---


### 84. [MedFlow: Class-Aware Multi-Scale Generation for Medical Time-Series Synthesis](https://arxiv.org/abs/2609.04804)

**<font color=#1a73e8>作者：</font>** Yanhao Huang, Shibo Feng, Wanjin Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Synthetic medical time-series generation can alleviate data scarcity and support the development of reliable clinical prediction models. However, existing methods mainly focus on matching the overall distribution and temporal dynamics of real data, which does not necessarily ensure strong downstream utility on imbalanced medical datasets. Clinically informative patterns often occur at heterogeneous temporal scales, while rare minority-class characteristics can be obscured by dominant population patterns. To address these challenges, we propose MedFlow, a class-aware multi-scale flow matching framework for medical time-series synthesis. MedFlow employs a vector-quantized multi-scale tokenizer to represent medical sequences at complementary temporal resolutions, capturing both coarse clinical trends and fine-grained dynamics. We further introduce Token Marginal Guidance, which incorporates class-conditional token statistics directly into the flow matching process to steer generation toward class-specific regions of the learned tokens. This mechanism strengthens minority-class patterns, while preserving the global and tail distributions of real data. Experiments on four public datasets covering electronic health records, EEG, and ECG signals demonstrate that MedFlow consistently outperforms recent state-of-the-art diffusion-based baselines across downstream prediction tasks. On average, it improves AUPRC by 5.8%, reduces Context-FID by 88.6%, and achieves 3.8$\times$ higher sampling throughput.

---


### 85. [CPR-IE:A Compression-Prediction-Resource Intelligence Efficiency Metric](https://arxiv.org/abs/2609.04809)

**<font color=#1a73e8>作者：</font>** Xiantao Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Comparing intelligent systems under deployment constraints requires more than this http URL paper develops Compression-Prediction-Resource Intelligence Efficiency (CPR-IE) as a protocol-relative ordering by representational economy, predictive quality, and resourceburden. The analysis separates two questions-how raw resource consumption is represented, andhow the resulting attributes are aggregated. Proportional-increment composition uniquely yieldslogarithmic cumulative burden, and context-independent ratio response yields power responsesto compression, prediction, and burden; with reference normalization the representation is I(C,P,T).We prove Pareto consistency, unit invariance, boundary behavior, trade-off identities, ranking-stability regions, and cross-task aggregation. A translog parent model makes interaction restrictions explicit, and further results establish cardinal and ordinal identification, sub-Gaussianfinite-sample ranking guarantees, robust selection under exponent uncertainty, and deterministicregret bounds. Minimum description length, algorithmic complexity, proper scoring rules, varia-tional inference, and Landauer's principle motivate measurement choices but do not entail theformula. CPR-IE is a constructed efficiency representation, not a universal law or a definition ofintelligence itself.

---


### 86. [Federated Attack Campaign Detection via Contrastive Encoding of Threat Indicators in Gradient Updates](https://arxiv.org/abs/2609.04815)

**<font color=#1a73e8>作者：</font>** Manuel Röder, Bibin Babu, Frank-Michael Schleif  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting orchestrated cyberattack campaigns that span multiple organizations traditionally requires sharing sensitive telemetry and threat intelligence across institutional boundaries and country borders, a barrier that Federated Learning removes by training shared threat detectors directly on local data. We propose FedIoC, a modular framework in which clients fold locally available structured threat indicators into their gradient updates; we instantiate the client-side encoder with a supervised contrastive loss over IoC-matched flows. Within each training batch, flows that match any known indicator pattern form the positive set; the contrastive objective pulls their learned embeddings together and pushes non-IoC embeddings away, so that campaign-relevant structure is, by design, expressed in the gradient direction. Clients sharing indicators for the same attack campaign then produce aligned gradient components, which the server clusters by the cosine similarity of their updates to recover global campaign patterns without any direct IoC transmission. We evaluate FedIoC on two public threat-detection benchmarks distributed across FL clients that each observe only a fragment of every active campaign and hold disjoint indicator sets derived from their local telemetry. In this regime the FL server recovers cross-organizational campaign cohorts directly from gradient geometry. We contribute FedIoC as a modular framework for this setting, and use it to pinpoint the non-IID gradient structure as the main driver of recovery and to define the open problem of designing encoders that improve on it.

---


### 87. [Weather-Conditioned Depth Anything](https://arxiv.org/abs/2609.04827)

**<font color=#1a73e8>作者：</font>** Zhaoming Xu, Chan-Wei Hu, Kuan-Ru Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation foundation models, such as the Depth Anything series, have achieved remarkable performance across diverse domains. However, they still suffer from critical failures under adverse weather conditions, such as fog, rain, snow, or at night. To address this, we present Weather-Conditioned Depth Anything (DA-W), a framework that explicitly disentangles style from content for weather-robust depth estimation. Specifically, we introduce a Style Filter trained on a curated mix of real and synthetic degradation datasets to extract content-independent, degradation-aware weather embeddings. This style embedding is then injected into the Depth Anything backbone using a parameter-efficient, zero-initialized adapter. Such a lightweight modulation allows a single unified model to robustly adapt to diverse conditions, including fog, rain, snow, and low-light, while avoiding catastrophic forgetting of its core generalization abilities in normal conditions. We train the adapter using a pseudo-label distillation and alignment strategy. Our comprehensive experiments demonstrate that our proposed DA-W achieves state-of-the-art robust depth estimation, improving AbsRel by an average of 3.7% on our curated weather benchmarks, while matching or slightly outperforming performance on standard clean benchmarks. Our project page is available at this https URL.

---


### 88. [Communication-Efficient Personalized Federated Learning via Layer-Wise Multi-Threshold Random Sketching](https://arxiv.org/abs/2609.04830)

**<font color=#1a73e8>作者：</font>** Xu Zhang, Xingyu Hou, Jiacheng Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized federated learning (PFL) is a promising paradigm for collaborative learning over distributed devices, where edge nodes collaboratively train personalized models without sharing raw data. Although PFL addresses data heterogeneity by learning client-specific models, it still suffers from substantial uplink and downlink communication costs when exchanging high-dimensional parameters in bandwidth-constrained systems. Recent one-bit methods achieve extreme compression, but they usually rely on a single thresholding rule applied to the whole model. This design has two limitations. First, it overlooks layer-wise differences in parameter distributions and quantization sensitivities. Second, a single threshold provides only coarse binary information and cannot capture fine-grained variations in parameter distributions. To address these issues, we propose a communication-efficient PFL framework via layer-wise multi-threshold random sketching. In the proposed method, each layer is assigned its own set of quantization thresholds, so that the compressed representation can adapt to layer-specific statistics while using multiple intervals to provide a finer low-bit description of sketched parameters. The proposed method supports bidirectional communication using compact low-bit sketches and improves the communication-accuracy tradeoff compared with existing one-bit compression approaches.

---


### 89. [PACE: Propagation-Aware Collaborative Correction for One-Shot Personalized Federated Graph Learning](https://arxiv.org/abs/2609.04832)

**<font color=#1a73e8>作者：</font>** Ruizhe Huang, Chengran Li, Xiaochuan Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Client heterogeneity creates both an opportunity and a risk in personalized federated graph learning. Knowledge held by other subgraphs may complement a receiver's Local model, but an incompatible transfer can override reliable predictions. One-shot communication sharpens this tension because an unsuitable server return cannot be corrected later. We introduce PACE, which treats collaborative knowledge as a compact correction to a complete Local predictor rather than as its replacement. Each client uploads a rank-r update carrier and a diagonal sketch of propagated message moments. The server uses them to construct a propagation-aware, receiver-anchored correction, while the receiver retains its full Local model. Convex negative-log-likelihood calibration (CNLL) then selects one coefficient between Local and External logits using validation nodes; model parameters remain fixed and no feedback is sent. At Rank-6, personalized returns occupy 9.6-17.6% of dense tensor bytes across the six evaluated datasets. The correction receives nonzero weight and improves both Accuracy and weighted-F1 over Local on five datasets; on ogbn-arxiv, CNLL assigns zero predictive weight to the correction and preserves Local predictions exactly. Applying the same CNLL rule to matched baselines on three citation datasets does not account for these gains. The central result is therefore that a small transported correction can augment a complete Local model when receiver evidence supports it while leaving the Local prediction unchanged otherwise.

---


### 90. [PAPT++: Risk-Aware Adversarial Tuning and Generation for Single Domain Generalization](https://arxiv.org/abs/2609.04837)

**<font color=#1a73e8>作者：</font>** Zhipeng Xu, De Cheng, Xinyang Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single domain generalization (SDG) aims to learn a model from one labeled source domain that generalizes to unseen target domains. A common strategy is to enrich the source distribution with augmented or generated samples, and recent text-to-image (T2I) diffusion models provide a strong generative prior for this purpose. However, diversity alone is insufficient for robust generalization, because useful generated samples should also capture variations that the current classifier finds difficult. Motivated by distributionally robust optimization (DRO), we define a semantic ambiguity set in the class-conditional generative space of a pretrained T2I model and search it for samples with high classification loss under the current classifier. To this end, we introduce PAPT++, a risk-aware adversarial generation-training framework for SDG. PAPT++ first learns diverse semantic reference images for each class through image-text alignment and intra-class diversity regularization. These references then serve as denoising targets during classifier-guided diffusion synthesis, reducing semantic drift while guiding generation toward challenging variations. The generated samples are combined with the source data to update the classifier, and the updated classifier guides the next synthesis round in return. In this way, PAPT++ progressively exposes the classifier to challenging yet semantically consistent variations. Extensive experiments on standard SDG benchmarks demonstrate the superiority of the proposed PAPT++ method and the effectiveness of its main components.

---


### 91. [Long Horizon Transformer Quantile Fault Prediction for Multi Site Industrial Predictive Maintenance](https://arxiv.org/abs/2609.04840)

**<font color=#1a73e8>作者：</font>** David J Poland, Daniele Ravi, Na Helian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon predictive maintenance requires models to distinguish slowly evolving degradation from normal operating-regime variation over planning windows measured in days rather than hours. This paper evaluates whether an explicit conditional-quantile representation provides an informative classifier interface for this problem. The proposed TQRNN30d framework combines a dual-stage quantile regression neural network (QRNN) feature extractor with a multi-stream temporal fusion classifier. Each hourly word of 81-channel machine behaviour is mapped to a 324-dimensional quantile-state representation, and 720 ordered hourly words form the 30-day document supplied to the long-horizon model. The classifier fuses quantile states with dynamic covariates, channel-level static metadata, and a 168-hour latent-history stream using gated residual processing, causal recurrent encoding, and metadata-conditioned cross-modal attention. A bounded instability-aware signal derived from sustained one-word-ahead prediction-error divergence provides auxiliary memory modulation at the longest horizon. Evaluation uses a machine-disjoint 43/14/15 train/validation/test allocation across 72 machines in nine manufacturing facilities. At 30 days, TQRNN30d achieves 79.97% F1, 80.18% recall, 81.82% precision, 82.39% accuracy, and 0.820 ROC-AUC. It leads all 18 evaluated baselines at the 7-, 14-, and 30-day fixed-threshold comparisons, with the largest F1 advantage at 14 days. The results support held-out-machine performance within the observed homogeneous nine-facility fleet, but do not establish unseen-site, cross-equipment, or cross-sector generalisation.

---


### 92. [LetOccVote: Learning Weakly Supervised 3D Occupancy through Consensus](https://arxiv.org/abs/2609.04846)

**<font color=#1a73e8>作者：</font>** Chi Zhang, Qi Song, Feifei Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly supervised 3D occupancy prediction reduces the reliance on costly 3D annotations by learning from 2D pseudo-labels generated by vision foundation models. However, existing methods typically use these imperfect pseudo-labels directly as supervision, making occupancy learning vulnerable to erroneous geometric and semantic targets. We observe that agreement across repeated observations provides an inexpensive and reliable cue for assessing pseudo-label reliability. Based on this observation, we propose \textbf{LetOccVote}, a weakly supervised Gaussian-based occupancy framework that leverages cross-frame voting to improve both geometric and semantic supervision. For geometry, Depth Vote exploits cross-frame geometric agreement to refine supported pseudo depth and reject contradictory estimates before volumetric lifting and depth supervision. For semantics, Semantic Vote aggregates pseudo-semantic observations in a shared 3D space to identify reliable and contested evidence, strengthening reliable semantic supervision while filtering unreliable pseudo-label segments. The entire framework is trained solely with 2D pseudo-label supervision without requiring 3D occupancy annotations. On Occ3D-nuScenes, LetOccVote achieves 53.27 IoU and 20.39 mIoU, establishing state-of-the-art performance among methods with 2D pseudo-label supervision.

---


### 93. [Mitigating Performance Discrepancy in Cross-Domain 3D Class-Incremental Learning](https://arxiv.org/abs/2609.04860)

**<font color=#1a73e8>作者：</font>** Jinge Ma, Gautham Vinod, Bruce Coburn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D perception plays a crucial role in real-world applications such as autonomous driving, robotics, and AR/VR. In practical scenarios, 3D perception models need to continually adapt to newly emerging 3D object categories, making class-incremental learning (CIL) particularly important. However, unlike 2D images, 3D point clouds are inherently heterogeneous: objects from the same class may not only come from the clean CAD domain, but also from RGB-D camera scans of varying quality, video reconstructions, or even corrupted observations. We discover that such heterogeneity introduces a new challenge beyond catastrophic forgetting: the degree of performance degradation can vary substantially across domains, a phenomenon we term performance discrepancy. To investigate this problem, we establish the Domain3D-CIL training and evaluation protocol, which contains point cloud categories from heterogeneous domains. We further adapt a wide range of mainstream CIL methods to the 3D modality. The results demonstrate that this performance discrepancy consistently appears across these baselines. To mitigate this issue, we introduce PolyMem, an exemplar-free approach that implicitly models rich high-order statistics of the feature distribution to enhance cross-domain robustness. Experiments demonstrate that our method effectively alleviates the performance discrepancy while improving the model's performance across domains. Code will be made publicly available upon acceptance.

---


### 94. [When Genomic Masking Priors Fail to Transfer: Strong Variant Prediction, Weak Functional Generation](https://arxiv.org/abs/2609.04861)

**<font color=#1a73e8>作者：</font>** Susu Hu, Preetam Gattogi, Jens Lehmann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bidirectional discrete diffusion model appears naturally suited to genomic modeling because it can reconstruct missing sequence from both flanks. We developed GenDA (Genomic Density-optimized Absorbing Diffusion) under the additional hypothesis that entropy-guided span placement would concentrate reconstruction pressure on compositionally complex regions, improving both downstream variant-effect prediction and functional sequence generation. Our results only partially support this premise. After supervised fine-tuning, the 202M-parameter GenDA model reaches a pooled ClinVar SNV AUROC of 0.774, exceeding a similarly scaled autoregressive model by 0.103. However, a matched random-span variant reaches 0.777, providing no evidence that entropy guidance causes the ClinVar improvement. More unexpectedly, GenDA fails a zero-shot functional inpainting stress test: across promoters, enhancers, exon boundaries, and intron boundaries, it does not consistently outperform a control that shuffles the native gap while exactly preserving 3-mer composition. Failure is already present for 50--500-bp gaps, although enhancer degradation worsens at longer gaps. Diagnostics identify several boundary conditions: entropy measures local sequence complexity rather than functional importance; 1-mer tokenization limits physical context; training spans are capped at 300 bp; and high absolute AlphaGenome fidelity can coexist with negative control-normalized restoration. These results show that strong fine-tuned variant prediction, a plausible corruption prior, and functional generation are distinct claims that require separate validation.

---


### 95. [MZ-Rain: Moisture-Budget-Guided Zero-Inflated Model for Station-Level Precipitation Nowcasting](https://arxiv.org/abs/2609.04864)

**<font color=#1a73e8>作者：</font>** Yifang Zhang, Shengwu Xiong, Henan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate station-level precipitation nowcasting is critical for agriculture, water resource management, and disaster prevention, which typically is formulated as a time series forecasting problem. However, conventional time-series modeling techniques face two major challenges in addressing station-level precipitation nowcasting: (1) Lack of Physics-Guided Modeling}, where meteorological variables are treated as a homogeneous set without accounting for their distinct roles in precipitation formation, leads to predictions that deviate from the physical processes governing precipitation. (2) Severe zero inflation in precipitation, where dry intervals dominate the dataset, obscuring meaningful precipitation patterns and complicating the predictive modeling. To address these challenges, we propose \textbf{MZ-Rain}, a moisture-budget-guided zero-inflated sLSTM framework for station-level precipitation nowcasting. Guided by the moisture budget equation, MZ-Rain decomposes the precipitation formation process into process-specific pathways corresponding to moisture storage, moisture transport, surface evaporation, and precipitation persistence, and captures their temporal evolution through dedicated sLSTM branches. To account for the zero-inflated nature of precipitation, MZ-Rain introduces an adaptive Tweedie modeling strategy that adaptively modulates the rainfall mean while jointly learning precipitation occurrence as an auxiliary task, enabling the model to better balance dry-wet discrimination and quantitative precipitation estimation. Extensive experiments across diverse geographical and climatic regimes demonstrate that MZ-Rain consistently outperforms strong baselines on multiple evaluation metrics, including CSI, FAR, MSE, and MAE. In particular, the model exhibits superior skill in forecasting heavy precipitation events, while benefiting from physically grounded process modeling.

---


### 96. [CHAMP: Cross-domain Hybrid Architecture for Matchmaking and Prediction in Online Multi-Player Games](https://arxiv.org/abs/2609.04870)

**<font color=#1a73e8>作者：</font>** Kai Wang, Ge Fan, Chaoyun Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multiplayer Online Battle Arena (MOBA) games rely on matchmaking to maintain competitive balance. Our prior work, CUPID, framed matchmaking as an assignment re-optimization problem and showed that a single-mode win-rate predictor can meaningfully rebalance teams. However, deploying such a system across diverse player populations exposes three practical bottlenecks: most queueing players lack sufficient in-mode match history (cold start), skill distributions shift drastically across rank tiers (distribution inconsistency), and extreme skill segments are severely data-starved.
We present CHAMP, a cross-domain matchmaking framework that resolves these deployment bottlenecks. To address data sparsity and cold starts, CHAMP replaces the target-mode-only player profile with a hybrid domain feature collection: a timestamp-ordered cross-mode short-term sequence whose slices are annotated with target-domain features, plus per-mode breakdowns of long-term, real-time and team statistics. We further propose the Domain-Aware Win-rate Network (DAWN): a Domain-aware Knowledge Extractor (DAKE) compiles target-mode attributes into learnable representations that feed Domain-Aware Temporal/Spatial/Permutation OmniNet Encoders (DATOE/DASOE/DAPOE), so that mode-conditioned representations and per-mode debiasing are learned jointly inside a single shared network. Online, one trained DAWN serves every supported mode, with per-mode position-satisfaction thresholds as the only mode-specific knob.
Offline, DAWN achieves 67.73% win-rate prediction accuracy, outperforming all evaluated attention and sequence baselines. Online A/B tests across the entire League ladder of a large-scale MOBA game, from novice players up to the top-expert players served by Elite Mode, demonstrate consistent drops in imbalanced matches. For lower-tier players, CHAMP reduces the 5-minute kill crushing rate by up to 20.73%.

---


### 97. [MARLA: A Conceptual Scaffold for Regulatory Learning under the EU AI Act](https://arxiv.org/abs/2609.04877)

**<font color=#1a73e8>作者：</font>** Alessio Buscemi, Tom Deckenbrunnen, Imane Hmiddou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The EU AI Act positions regulation as part of the infrastructure for safe, trustworthy and market-ready innovation. Realising this ambition requires regulatory learning: the evidence generated during implementation must be translated into governance and legal knowledge that supports consistent interpretation, effective oversight, and adaptation as technologies evolve. Yet the actors who produce this evidence and those who rely on it operate in different professional worlds. This paper proposes MARLA (Map, Assess, Report, Learn, Adapt), a conceptual scaffold organising regulatory learning as a five-stage cycle centred on the implementation of legal requirements into socio-technical practices, situated at the Local, National and European levels of the AI Act's governance architecture. Deliberately non-prescriptive, MARLA gives technical and legal stakeholders a shared vocabulary in which each of the first three stages generates its own documentable form of regulatory learning. We illustrate the scaffold with two piloted case studies and a prospective National-to-European illustration.

---


### 98. [ReCAST: Restoration-aware Cascaded Stage-wise Training for Obfuscated SMS Risk Classification](https://arxiv.org/abs/2609.04878)

**<font color=#1a73e8>作者：</font>** Jieyun Huang, Yi Shen, Kaikai Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fraudulent messages sent via Short Message Service (SMS) are increasingly obfuscated to evade cost-conscious classifiers in production systems. In Chinese SMS, attackers can exploit a wide range of carefully crafted obfuscation strategies to hide risk-bearing phrases while preserving human readability, making direct classification brittle under real-world latency and throughput constraints. We propose ReCAST, a Restoration-aware Cascaded Stage-wise Training framework for robust obfuscated Chinese SMS classification. ReCAST distills a large teacher model's de-obfuscation ability into a smaller deployable student model by supervising obfuscated span detection, obfuscation type prediction, and text restoration, and then uses the restoration-aware student for downstream risk classification. Experiments on an internally constructed real-world Chinese SMS benchmark show that ReCAST substantially improves classification performance over directly trained baselines under obfuscation. The results suggest that restoration-aware distillation offers a practical path toward robust SMS risk classification with smaller deployable models under production-oriented constraints.

---


### 99. [Reinforcement Learning for Sequential Solar PV Policy Design under Uncertainty: An Agent-Based Approach](https://arxiv.org/abs/2609.04880)

**<font color=#1a73e8>作者：</font>** Iias Faiud, Jonaid Shianifar, Michael Schukat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing effective and fiscally sustainable policies for solar photovoltaic (PV) adoption requires balancing adoption gains against public expenditure under uncertainty and heterogeneous decision-making. This study formulates PV policy design as a sequential decision problem and integrates reinforcement learning (RL) with a stochastic agent-based model (ABM) that simulates yearly solar PV adoption under uncertainty. A policymaker agent selects annual incentives, including capital grants, subsidised loan rates, and feed-in tariffs, over a 16-year horizon. Adoption--cost trade-offs are explored by varying policy preferences within a scalarised reward framework. Policies are learned using PPO, SAC, and TD3 and evaluated under stochastic simulation. The results show that this approach produces a clear trade-off structure: the highest-adoption policy (TD3, $w_{\text{cost}}=0.5$) achieves approximately 4,145 adopters at a cost of EUR 41.73 million, while the lowest-cost policy (PPO, $w_{\text{cost}}=2.0$) reduces expenditure to EUR 7.27 million with 2,682 adopters. The balanced policy (PPO, $w_{\text{cost}}=1.6$) achieves 3,495 adopters at a cost of EUR 22.47 million. Across algorithms, consistent trade-off patterns are observed, indicating robustness of the adoption--cost relationship. Compared with static baseline policies, the RL framework explores a broader range of policy configurations. These findings demonstrate the potential of RL as a flexible tool for adaptive policy design under uncertainty.

---


### 100. [From Deep to Shallow: Unconstrained and Efficient Layer Merging Strategy](https://arxiv.org/abs/2609.04881)

**<font color=#1a73e8>作者：</font>** Petro Shulzhenko, Gabriele Spadaro, Enzo Tartaglione  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although Deep Neural Networks have become foundational in many areas of Machine Learning, high computational demands limit their application in resource-constrained environments. To address this issue, depth compression methods have been proposed to identify and linearize redundant activation functions, thereby allowing for the merging of layers without intermediate non-linearities. However, these methods face two key challenges: they cannot be directly applied to convolutions with padding due to the absence of an analytical solution for merging these layers, and they typically increase the kernel size of merged layers, thus limiting speed-up gains. To overcome these limitations, we propose an efficient strategy that enables merging of layers without an existing analytical solution, and also without increasing kernel size. We validate our approach across multiple architectures and datasets, and measure inference speed-up gains on real embedded platforms. We publicly released the code at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-190](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

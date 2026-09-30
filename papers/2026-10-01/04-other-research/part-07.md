# 📦 其他研究 | 2026年10月01日

> 本类共 **447** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-447](./part-09.md)

---

### 301. [Transolver-$σ$: Joint Spectral-Physical Subspace Modeling for Neural PDE Solving](https://arxiv.org/abs/2609.37279)

**<font color=#1a73e8>作者：</font>** Haonan Shangguan, Hang Zhou, Haixu Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural solvers offer efficient surrogates for numerical simulation of partial differential equations (PDEs). For time-dependent problems, strong one-step accuracy does not necessarily translate into reliable autoregressive rollout. We observe that a solver based only on physical-state modeling can achieve lower one-step error, whereas its spectral-only counterpart can become more accurate at later rollout steps. Motivated by this observation, we present Transolver-$\sigma$, a neural PDE solver based on joint spectral--physical subspace modeling. Within each block, adaptive physical-state interactions and spectral transformations are modeled in dedicated latent subspaces, whose responses are recomposed to enable information exchange between the two representations. Within the physical subspace, we introduce Slice-Residual Physics-Attention (SRPA), which preserves an explicit slice-space identity path while retaining learnable cross-slice interaction. In parallel, an axis-factorized Fourier operator captures global spectral structure. Across five well-established PDE benchmarks spanning steady-state prediction and time-dependent dynamics, Transolver-$\sigma$ achieves state-of-the-art with a benchmark-averaged relative error reduction of 33.4% over the strongest baseline for each metric, while consistently improving autoregressive rollout over single-operator counterparts. Transolver-$\sigma$ further delivers strong gains on coupled multiphysics systems and real-world fluid and combustion measurements from RealPDEBench, demonstrating its effectiveness beyond standard simulation benchmarks.

---


### 302. [AssayRouter: Historical Utility Priors for Frozen Molecular Predictor Routing](https://arxiv.org/abs/2609.37285)

**<font color=#1a73e8>作者：</font>** Dong Xu, Zhangfan Yang, Jiantao Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Laboratories often face a new molecular assay with 16-64 labels and a bank of predictors whose training data and parameters are unavailable. The practical question is which frozen outputs to include in a small local model. AssayRouter treats completed assays as pseudo-targets and labels each candidate by its post-fit utility: the reduction in held-out discovery loss when the candidate is added to the local target predictor. A shared regressor learns to predict this utility from candidate behavior on the support set, without source identity; on a new assay, one frozen ranking selects four sources and separate labels fit a convex combiner. We train only on completed ChEMBL-MT assays and evaluate 24 external regression assays across six frozen interface families. AssayRouter-C lowers strict four-call negative log-likelihood (NLL) by 0.0409 relative to Support-CV@4. Frozen candidate-label permutations confirm that candidate-utility correspondence carries the transferred information, and leave-one-interface-out training shows that the mapping generalizes to unseen predictor families. Completed assays therefore provide transferable supervision for scarce-label routing through frozen prediction interfaces.

---


### 303. [VISTA-Bench: Benchmarking Multilingual Image Translation with Image-Specific Rubrics](https://arxiv.org/abs/2609.37287)

**<font color=#1a73e8>作者：</font>** Bo Lv, Mao Zheng, Zheng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image translation is a fundamental capability of multimodal models for multilingual applications, requiring visual understanding and meaning preservation across languages. However, existing benchmarks have limited language coverage and often lack explicit image-specific evaluation criteria, making it difficult to comprehensively assess this capability. To systematically evaluate this capability, we introduce VISTA-Bench, covering 22 languages and 10 domains, and develop an image-specific rubric evaluation protocol. The benchmark combines sampling for language and scenario coverage with model-assisted, human-verified annotations that group related text into coherent semantic units and provide multilingual reference translations. The rubrics specify essential content, semantic relations, and acceptable translation variants, yielding separate output-based scores for translation quality and the preservation of visual and knowledge-dependent information. We conduct extensive evaluations of 16 mainstream models, including 12 multimodal models and four text-input models, and provide systematic analyses across languages, domains, and evaluation dimensions.

---


### 304. [Why Cross-Skeleton Retargeting Is Non-Identifiable: Structural Limits of Generative Motion Models](https://arxiv.org/abs/2609.37297)

**<font color=#1a73e8>作者：</font>** Zhiyuan Li, Wenyan Yang, Pekka Marttinen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-skeleton motion generation trains generative models to carry action structure and motion intention from one body to another. Yet a target motion that shows the right action has two explanations that the training data cannot tell apart: the model transferred the source clip, or it recovered a typical motion for the requested action. We show that this ambiguity is structural rather than incidental: under standard generative objectives, the source-conditioned retargeting map is non-identifiable in sparse heterogeneous motion domains. Unpaired distribution matching yields gauge non-identifiability: the latent spaces of different skeletons can be transformed relative to one another without changing the training evidence, so different source-conditioned maps fit it equally well. Sparse paired supervision admits the complementary failure mode, \emph{conditional-mean degeneration}: when clips are paired only by action, squared-error training converges to an average target motion that ignores the source clip. To make the missing evidence observable, we introduce Source-Instance Fidelity (SIF), a diagnostic that tests whether outputs differ from one another the way their source clips do, with the target skeleton and action held fixed. Under this diagnostic, methods that succeed at the standard action-level test on animal motion data often sit at the source-blind floor, while the methods that rise above it retain only a partial relational signal. Retargeting therefore needs objectives and evaluations that can identify the source-conditioned map it claims to learn. Project page: this https URL.

---


### 305. [Technical note on: Zero-Training Feature-Space Alignment via Information Geometry](https://arxiv.org/abs/2609.37302)

**<font color=#1a73e8>作者：</font>** Behraj Khan, Tahir Qasim Syed, Syed Ahmad Chan Bukhari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep vision models often degrade under distribution shift. Test-time adaptation can improve robustness but typically requires iterative optimization, hyperparameter tuning, and multiple forward-backward passes. We propose Zero-Training Fisher Geometry Alignment (ZFGA), a closed-form method that improves robustness under covariate shift without modifying model parameters. ZFGA is based on the observation that distribution shifts distort feature-space geometry. It estimates the Fisher information matrix of the predictive distribution with respect to feature embeddings and applies a linear transformation that aligns test-feature Fisher geometry with a reference geometry computed from clean data. This provides a natural-gradient-inspired preconditioning step in feature space. We evaluate ZFGA on CIFAR-10-C and ImageNet-C using ResNet-50, DINO ViT-S/16, and CLIP ViT-B/32. ZFGA consistently improves over zero-shot inference across all three models, although it is not the strongest method for every model. Covariance whitening performs better on ResNet-50, while Fisher whitening is statistically indistinguishable from ZFGA on CLIP. Across six training-free and gradient-based alternatives (covariance whitening, Fisher whitening, TENT, T3A, LAME, and AdaNPC), ZFGA is the only method that does not substantially harm any of the three model families. The Fisher geometry distortion is also positively correlated with ZFGA gain (Pearson r = 0.366, p = 0.017), providing preliminary evidence that geometric misalignment contributes to robustness degradation. ZFGA requires only forward passes and matrix operations at inference time, offering a lightweight and deterministic alternative to optimization-based test-time adaptation.

---


### 306. [PowerMarketJax: A JAX Benchmark Suite for Multi-Agent Reinforcement Learning in Power Markets](https://arxiv.org/abs/2609.37321)

**<font color=#1a73e8>作者：</font>** Zhanhua Pan, Xin Qin, Xiao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Power markets are a natural testbed for multi-agent reinforcement learning (MARL), where multiple self-interested participants repeatedly submit bids. A market-clearing mechanism then determines dispatch and prices subject to power grid constraints and market settlement rules. However, existing MARL environments typically focus on a single market setting, implement simplified clearing mechanisms, or rely on CPU-based optimization solvers that slow large-scale training and limit the systematic study of bidding strategies and market behavior. We introduce PowerMarketJax, a benchmark suite for MARL across five power markets: day-ahead wholesale, real-time balancing, ancillary services, peer-to-peer double auctions, and local flexibility. Each environment implements its own clearing, pricing, and settlement rules while providing a common framework for learning and evaluation. We find that learned bidding behavior depends strongly on the market design: independent learners can miss better strategies when gains require many agents to change together, when more profitable strategies lie beyond a region of lower profit, or when profits disappear as more agents adopt the same strategy. PowerMarketJax implements both market simulation and policy training in JAX, allowing the entire pipeline to run on the GPU with 1,024 X 1,200 parallelisms across both environments and market participants, achieving up to 33X speedup over CPU-based baselines. Our open-source benchmark is available at: this https URL.

---


### 307. [Parallel Tempering for Diffusion-Based Combinatorial Optimization](https://arxiv.org/abs/2609.37323)

**<font color=#1a73e8>作者：</font>** Arman Mielke, Uwe Bauknecht, Thilo Strauss 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models have emerged as a powerful paradigm for solving combinatorial optimization (CO) problems on graphs by learning to sample high-quality solutions. A common inference-time approach is to generate multiple candidate solutions independently and return the best-performing sample, improving solution quality at the expense of an increase in computational cost. In this work, we introduce PT-Denoise, an inference-time procedure that allows these concurrent denoising trajectories to interact through parallel tempering, without requiring retraining or fine-tuning of the underlying denoiser. Our method assigns a temperature to each diffusion process and allows processes to swap temperatures based on their relative performance. This dynamically reallocates promising, low-energy trajectories to colder, more concentrated sampling regimes while allowing higher-energy states to escape local minima through randomized exploration. Experiments on canonical graph-structured CO problems show that our approach consistently improves the quality of the best solution found, while only adding minimal computational overhead.

---


### 308. [EntityWeaver: Visual Exploration and Curation of Named-Entity Relationships in Document Collections](https://arxiv.org/abs/2609.37329)

**<font color=#1a73e8>作者：</font>** Uroš Šmajdek, Ciril Bohak  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present an interactive visualization system for exploring named entities and their relationships across document collections, with a strong focus on handling uncertainty and supporting both distant and close reading. The system is built around a graph that links documents, entity mentions, and entities. Uncertainty from mention-to-entity linking is included directly in this graph, so users can see where connections are strong, weak, or ambiguous. A transfer-function control, inspired by approaches in scientific visualization, allows users to adjust how this uncertainty is displayed, making it easy to tune the visualization for different datasets and research questions. The system also provides direct access to the full source texts in a coordinated view, enabling quick context checks, resolving ambiguous cases, and correcting digitization errors. Exploration is further supported through a multi-stage filter query builder, mini-map navigation for large graphs, and export options for downstream analysis. By combining uncertainty-aware graph visualization with direct interaction in the source texts, the system provides a unified workflow that supports both large-scale pattern discovery and curation of named-entity-based document collections. The design choices were supported by the domain experts, who were also involved in the initial system evaluation.

---


### 309. [The Domain Is a Residue: Adapting Self-Supervised Features, Not Generators](https://arxiv.org/abs/2609.37330)

**<font color=#1a73e8>作者：</font>** Thomas Deixelberger, Markus Steinberger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clearing fog, rain or snow from footage, or turning renders into photographs, must remove the source domain and keep the scene. Unpaired translators carry it through because their generator sees the source appearance (pixels, a near-invertible latent or a control map) and keeps it. A DINO feature map fixes what is in the scene and carries weather, lighting and rendering style as a residue of 13 to 14% of the feature norm. We propose the Representation Feature Adapter (RFA), a 2.9M-parameter network that moves this residue. We train only the adapter and its discriminators; the encoder and a feature-conditioned decoder, trained once for all conditions, stay frozen. Against CycleGAN-Turbo it is ahead on both metrics on fog and on KID on night, and level within noise on snow, rain and haze. On sim-to-real it leads REGEN and HyPER-GAN on both metrics. Only the RFA removes the rain while keeping the scene. The removal costs scene structure: CycleGAN-Turbo keeps more on every condition but fog. On VAE latents the identical adapter collapses to the identity, and decoders from other groups that never saw it render its output. The RFA has about 160 times fewer trainable parameters than CycleGAN-Turbo and under a fifth of its per-condition training time.

---


### 310. [OFBD: Object-Focused Background Debiasing for Long-Tailed Learning](https://arxiv.org/abs/2609.37331)

**<font color=#1a73e8>作者：</font>** Shenghan Chen, Yiming Liu, Zhipeng Deng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Balancing performance trade-offs on long-tailed data distributions remains a long-standing challenge in visual recognition. Existing methods mainly improve tail classes through re-balancing, representation learning, or data augmentation, but the underlying cause of tail class degradation is still insufficiently explored. In this paper, we find that standard long-tailed training induces background-biased representation and optimization: tail classes suffer larger background distribution shifts and become increasingly driven by background gradients. This reveals that tail degradation is not merely caused by insufficient samples, but also by the learning of irrelevant background features. To tackle this issue, we propose Object-Focused Background Debiasing (OFBD), a framework that mitigates background bias from both distribution and optimization perspectives. Specifically, Foreground-guided CutMix preserves target-related foregrounds while diversifying complementary backgrounds, and Background-guided Feature Rectification suppresses background-biased features without learnable parameters or additional training. Extensive experiments show that our method improves overall accuracy, achieves significant tail-class gains, and can serve as a plug-in for mainstream long-tailed methods without external data or pretrained recognition models. The code is available at: this https URL

---


### 311. [UGO: Unified Architecture for General Multi-Object Tracking by Segmentation](https://arxiv.org/abs/2609.37339)

**<font color=#1a73e8>作者：</font>** Jer Pelhan, Alan Lukezic, Matej Kristan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General multi-object tracking (GMOT) tracks all instances of a user-specified category from a single first-frame exemplar. Prior work relies on bounding boxes and surrogate training, and struggles with non-rigid objects, crowded scenes, and distractors. We introduce UGO, a unified GMOT tracker that pairs a pretrained exemplar-conditioned detection head with an instance-propagation head in a common architecture. A novel training-free, energy-minimization consolidation method converts overlapping proposals into exclusive pixel-wise masks and detections, resolving over-segmentation, duplicates, and conflicts. A hierarchical memory spanning global and instance levels improves recall and per-instance segmentation accuracy using a new memory management protocol. UGO sets a new state-of-the-art on GMOT benchmarks and video object counting, and is competitive with specialist MOT methods, establishing a strong paradigm for unified, open-category multi-object tracking.

---


### 312. [A Sharp Transition in Data Reconstruction under Differential Privacy](https://arxiv.org/abs/2609.37344)

**<font color=#1a73e8>作者：</font>** Max Cairney-Leeming, Simone Bombari, Marco Mondelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data reconstruction attacks have empirically been successful in recovering training samples from learned models, raising privacy concerns and motivating defenses with guarantees that remain valid against future threats. While differential privacy (DP) provides formal protection, choosing the privacy budget remains a challenge: small budgets severely reduce utility, but it is hard to quantify how large the budget can be without allowing accurate reconstruction. In this work, we study informed attackers who aim to reconstruct a single $d$-dimensional training sample from a $\rho$-zero-concentrated DP model, knowing all other training data. Our main contribution is to establish a sharp transition at $\rho \asymp d$ for data reconstruction: on the one hand, we derive entropy-based lower bounds for any private mechanism and any attack, characterizing a set of target priors for which reconstruction is information-theoretically impossible for $\rho \ll d$; on the other hand, we analyze a simple attack on private linear regression with output perturbation, showing that reconstruction is practically feasible for $\rho \gg d$. Remarkably, the transition moves to $\rho \asymp s$ for data lying in an $s$-dimensional subspace, demonstrating that the privacy budget guaranteeing adequate protection must be assessed in terms of the effective dimension of the data. We validate our findings via experiments on synthetic data and natural images (CIFAR-10, ImageNet).

---


### 313. [PCaPaint: Prostate Cancer Inpainting by Mitigating Shortcut Learning](https://arxiv.org/abs/2609.37350)

**<font color=#1a73e8>作者：</font>** Levente Lippenszky, Hongxu Yang, Marcell Dömötör 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The development of AI systems for tumor-specific applications is limited by the scarcity of labeled data. Synthetic tumor inpainting offers a promising approach but faces challenges for prostate cancer MRI which contains high-resolution multi-sequence data. Although methods leveraging latent diffusion models (LDMs) enable large-volume synthesis, they are prone to shortcut learning, simply reproducing the condition image created by masking the lesion region. In this work, we introduce PCaPaint, a prostate cancer inpainting method based on LDMs that explicitly addresses this failure mode. To overcome shortcut learning that compromises synthetic tumor texture, we propose a simple yet efficient conditioning strategy in which the condition image is filled with Gaussian noise, and we provide theoretical justification. In addition, we propose a novel training objective for LDM that emphasizes the error within the lesion region. Furthermore, we introduce a multi-sequence latent design, in which T2w scans and DWI&ADC scans are compressed using two separate autoencoders to preserve their distinct frequency characteristics. Extensive experiments demonstrate that the generated synthetic data improves downstream performance in prostate lesion segmentation, patient-level classification and lesion-level detection. Furthermore, our method significantly outperforms a recent state-of-the-art LDM-based tumor inpainting method both in downstream performance and in synthetic image quality.

---


### 314. [Visual Anomaly Synthesis for Model Selection in Data Scarcity](https://arxiv.org/abs/2609.37360)

**<font color=#1a73e8>作者：</font>** Daniel Pröll, Thomas Kraxner, Tobias Schaefer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Defect detection systems for industrial condition monitoring can only be relied upon if they are validated, yet defective samples are rare and, for a specific asset, often nonexistent. We present a framework that synthesizes severity-graded defects on real non-defective images without any defect references for the target asset, that can be used for model selection and validation. A defect taxonomy for common failure modes is distilled from literature into prescriptive prompts at varying defect severities. Regions of interest are cropped from in defect-free images and edited with a pre-trained image generation model ("FLUX.2 [klein]"). Color-matching and blending are employed to improve structural coherence with the original image. Generations are filtered out by a scorer and by estimated detection difficulty. Model selection experiments on MVTecAD show image AUROC choice regret over model selection can be nearly halved compared to the best fixed model chosen with access to test data. Experiments show the need for severity-graded anomaly synthesis. A case study investigates the proposed method for in-situ monitoring of Pelton turbine runners in hydropower, where real defect images are rare and expensive to collect. A PatchCorebased anomaly detection model is fit on Pelton turbine images and selected and validated using synthetic images, showing strong detection performance (94 % correct detection at optimal threshold and AUROC 0.97). The model reliably detects moderate and advanced defects, while early-stage defects remain challenging, indicating the synthetic data meaningfully stresses detector sensitivity.

---


### 315. [Do-JEPA: From Masking to Intervention in Latent World Models](https://arxiv.org/abs/2609.37378)

**<font color=#1a73e8>作者：</font>** Hossein Resani, Javen Qinfeng Shi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent world models are trained to predict what happens next, so nothing in their objective separates what an action caused from what merely co-occurred with it. Object-masking models such as C-JEPA intervene on what the predictor can see; we intervene on what physically happens. From one saved simulator state we run the dynamics under an action $a$ and under a reference action $a_{\varnothing}$, and train the model to predict the difference $\Delta z=z^{a}-z^{a_{\varnothing}}$ between the two latent futures. The resulting objective, Do-JEPA, has an effect loss, a support loss (where the action enters), a propagation loss (where its effect travels) and invariance losses (what must not change). In a synthetic system with object-aligned variables, support supervision finds the directly intervened object in 99.95% of test cases, where a sparse action mask sends the action to a nuisance slot in every case, and response-onset supervision recovers the ring-shaped propagation graph (edge AUROC 0.975 vs. 0.624). From pixels, the effect loss beats a control trained on exactly the same data: it lowers latent effect error by 28.4% on an end-to-end LeWM model and physical effect error by 13.5% when trained and tested on natural action sequences, and on three independently generated CausalWorld benchmarks it lowers responsive effect error by about 20% under physics shifts and the latent context sensitivity of predicted effects by 66%. Trained from scratch it costs factual accuracy; fine-tuning an existing model with it removes this cost. Together, these results show that intervening on the world, rather than on what the model sees, helps latent world models predict what their actions cause.

---


### 316. [High-Dimensional Simulation-Based Inference in Latent Spaces](https://arxiv.org/abs/2609.37381)

**<font color=#1a73e8>作者：</font>** Lars Kühmichel, Stefan T. Radev, Bhanu Prasanna Koppolu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural simulation-based inference (SBI) has been widely successful in inferring a relatively small number of interpretable parameters from potentially high-dimensional observations, such as images or time series. Accordingly, representation learning in SBI has focused almost exclusively on compressing the observations used to condition the posterior. More recently, however, SBI has begun to target increasingly high-dimensional parameter spaces, raising the complementary question of whether the inference target itself should be compressed. Our answer is a practical merger of SBI and latent generative modeling, which learns a low-dimensional representation of the simulator parameters, performs posterior inference directly in this latent space, and maps posterior samples back to the original parameter space. We characterize the conditions under which latent-space inference recovers the desired target posterior and systematically study its empirical trade-offs. Across four case studies and three generative families, we compare latent and standard estimators while controlling for network capacity, regularization, optimization, and training compute. At matched training compute, latent-space inference achieves accuracy and marginal calibration comparable to direct target-space inference while sampling up to more than an order of magnitude faster.

---


### 317. [MoTIF-X: A Multimodal Tokenized Framework for Interpretable and Extensible Molecular Representation Learning](https://arxiv.org/abs/2609.37384)

**<font color=#1a73e8>作者：</font>** Linqing Mo, Jiayu Zhou, Bin Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular representation learning is central to computer-aided drug discovery. Molecular graphs, SMILES strings, and 3D conformations provide complementary structural information, yet many multimodal approaches encode these views independently and align them only at a later stage, limiting fine-grained cross-modal interaction and substructure-level interpretability. To address these limitations, we introduce MoTIF-X, a motif-centered framework that uses graph-grounded chemical motifs as shared anchors for multimodal integration and interpretation. Its first pretraining stage learns motif representations through hierarchical contrastive learning across atomic, motif, and molecular scales. The second stage contextualizes these representations with SMILES and torsion-angle tokens through multimodal masked token modeling.
After pretraining on drug-like molecules with multiple conformers, MoTIF-X achieved the lowest mean absolute error on all nine OpenADMET ExpansionRx endpoints and the best overall performance among the evaluated methods. Significance analyses supported its advantage in the vast majority of endpoint-baseline comparisons after multiple-testing correction. Ablation studies supported the complementary contributions of motif-token contextualization, multimodal integration, and two-stage pretraining. Beyond molecular properties, the framework extended to drug-target interaction prediction, achieving the best average classification performance across the evaluated benchmarks and generalizing to an external drug-cold-start dataset without additional fine-tuning. Its motif-centered design also enabled substructure-level interpretation: higher motif attribution scores were associated with larger experimentally measured activity shifts. Together, these findings support MoTIF-X as a transferable and interpretable framework for molecular modeling.

---


### 318. [Multi-task learning for the automatic grading of enlarged perivascular space burden using MRI](https://arxiv.org/abs/2609.37387)

**<font color=#1a73e8>作者：</font>** Jesse Phitidis, William N. Whiteley, Joanna M. Wardlaw 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Enlarged perivascular spaces (PVS) visible in brain magnetic resonance imaging (MRI) are increasingly thought to be linked to poor brain health. PVS are elongated structures of less than 3 mm in diameter and can be numerous. To reflect the incidence of PVS, radiologists visually score their burden following a clinical grading scale - a task that would benefit from automation to accelerate analyses and overcome the influence of inter-observer differences. We developed and evaluated methods for training machine learning models to score PVS incidence in the basal ganglia (BG) and centrum semiovale (CSO) leveraging the Potters/Wardlaw scale. The novelty in our work lies in the use of imperfect, semi-automatically generated "silver-standard" PVS segmentation masks during training, in addition to PVS radiological scores. We comparatively evaluated a conditional convolutional neural network (CNN) which accepts PVS masks as an extra input channel, a multi-task CNN which performs both PVS segmentation and scoring, and a logistic regression model which utilises features derived from PVS masks to predict PVS scores. Multi-task learning was the most effective method, achieving a mean average precision of 64.08% compared to 60.22% for the conditional CNN, 52.11% for a baseline CNN trained only to predict PVS scores, and 49.32% for the logistic regression model. The multi-task model showed an ability to localise individual PVS not shown by the other CNNs, and behaved in a probabilistically sensible way, predicting with lower confidence on inherently harder classes. Age, sex, hypertension status, white matter hyperintensity volume, and ischaemic stroke lesion status were shown to be associated with the multi-task model's PVS score predictions and the ground truth in a similar way.

---


### 319. [Learning Macroscopic Dynamics without Reconstructing Microscopic States](https://arxiv.org/abs/2609.37392)

**<font color=#1a73e8>作者：</font>** Zhichao Han, Yue Zhao, Qianxiao Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling the temporal evolution of macroscopic properties of complex systems is an important scientific task. To predict this evolution without full microscopic simulation, a common approach encodes microstates into compact latent states, learns their evolution, and reads out macroscopic predictions from the latent trajectory. These latent states are often learned through microstate reconstruction. However, with limited latent capacity, reconstruction can favor high-variance microscopic details over information needed for macroscopic prediction. Yet jointly learning latent states and their transition without reconstruction often fails to obtain latent dynamics that support accurate macroscopic prediction. We show that this failure can arise from latent scale collapse: shrinking the latent state scale reduces training loss while macroscopic evolution error remains large. Here, we propose a reconstruction-free framework to learn latent states with their dynamics for prescribed macroscopic prediction. Training alternates between updating the latent representation with the transition and next-state latent targets fixed, and updating the transition with the latent representation fixed. At inference, the trained model predicts macroscopic states recursively from an initial microstate. Our theoretical analysis characterizes reconstruction misalignment and scale collapse under joint training, and gives a sufficient condition for local convergence to correct latent dynamics for our method. Experiments on epidemic spreading on a lattice, mixing of two particle species, and polymer stretching demonstrate that the proposed method achieves substantially better macroscopic prediction over baselines.

---


### 320. [Direct Experience World-Model Optimization: Learning the World Beyond Action Imitation](https://arxiv.org/abs/2609.37398)

**<font color=#1a73e8>作者：</font>** Xiangcheng Zhan, Zirui Chen, Yicheng Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World-Action Models (WAMs) couple action generation with predictions of how physical interactions unfold. However, current post-deployment learning paradigms typically improve behavior without requiring better world predictions. Especially in dexterous manipulation, small execution errors can compound in high-dimensional action spaces, hindering policy improvement and pushing interactions beyond the world model's training distribution. Motivated by this, we propose Direct Experience World-Model Optimization (DEWO), a post-deployment learning paradigm for WAMs that, alongside action imitation, refines world representations through visual experience to better condition action generation. Specifically, it identifies interaction turning points and learns from successful and failed futures to support classifier-free guidance. An additional value head estimates task progress from video representations and activates guidance when progress stalls during inference. Across five DexJoCo tasks, DEWO improves average success across all three WAM formulations. Ablations show that visual supervision from successful and failed continuations improves both prediction and control beyond action supervision alone. On four real-world tasks across Wuji and Sharpa, 3 x 3 grid evaluations show that two rounds of deployment learning increase success from 51.0% to 71.7% in cells with at least one initial success, a gain of 20.7 percentage points. These findings support continued predictive learning for improving control through deployment experience, making world modeling an active part of WAM adaptation.

---


### 321. [BeatDance: Generating Beat-Consistent 3D Dance with Hierarchical Spatial-Temporal Modeling](https://arxiv.org/abs/2609.37400)

**<font color=#1a73e8>作者：</font>** Xiaojian Shen, Dahu Shi, Jianrong Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating realistic 3D dance from music is a challenging task that requires accurate synchronization with musical rhythms while capturing the spatial complexity of human motion. Although existing methods can generate physically plausible dance motions, they often struggle to achieve precise alignment with music, such as the beat. To address this limitation, we propose a novel diffusion-based framework, BeatDance, with two components: 1) We present a Hierarchical Decoupled Attention (HDA) module, which first disentangles the learning of human pose and temporal dynamics. A hierarchical structure is then employed to capture both short-term and long-term dependencies, thereby enhancing spatial-temporal modeling. 2) We adopt cycle-consistent learning by introducing an auxiliary dance-to-music module. During training, discrepancies between the reconstructed and original music induce a stronger loss signal, effectively encouraging the consistency property between the music and dance motion. Extensive experimental results demonstrate that our proposed approach outperforms recent competitive methods on two benchmark datasets.

---


### 322. [Simultaneous Neural Optimal Transport](https://arxiv.org/abs/2609.37424)

**<font color=#1a73e8>作者：</font>** Milena Gazdieva, Kirill Sokolov, Jiawei Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimal Transport (OT) provides a principled framework for learning transformations between probability distributions from unpaired samples. In many applications, however, a single transformation must map several source distributions to a common target distribution. For example, image restoration might require handling different types of degradation without knowing the degradation of each input at inference time. Simple approaches of pooling the source distributions only encourage alignment with the target at the aggregate level and may leave individual sources misaligned. In our paper, we consider the simultaneous OT problem which formalizes the task of learning a shared transport map that minimizes the average transport cost while aligning each source distribution with a prescribed target. We propose a neural method for solving the simultaneous OT problem by learning a shared transport map that minimizes the average transport cost while aligning each source distribution with a prescribed target. We derive a max-min formulation for learning this map. We illustrate its application to image restoration, where a single model handles multiple degradation types using a common collection of clean target images.

---


### 323. [Variational Augmented Invertible Koopman Autoencoder for probabilistic time series forecasting](https://arxiv.org/abs/2609.37435)

**<font color=#1a73e8>作者：</font>** Anthony Frion, Lucas Drumetz, Guillaume Tochon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Koopman autoencoder models have been shown to successfully build a latent embedding with linear dynamics for arbitrary dynamical systems, enabling strong performance in long-term time series forecasting. However, these models usually work in a deterministic setting, which does not allow the quantification of the uncertainty of their predictions. Thus, we propose the new Variational Augmented Invertible Koopman AutoEncoder (VAIKAE), in which the latent embedding follows a Gaussian distribution instead of being deterministic. A key property of the VAIKAE architecture is that it leverages normalizing flow models, enabling the use of likelihood computations in the state space of dynamical systems for training a model. We further propose new strategies for uncertainty-aware latent data assimilation with a trained VAIKAE model. The effectiveness of our methods is demonstrated in a series of experiments on long-term time series forecasting benchmarks.

---


### 324. [Demistifying Data and Simulator Assumptions in Supervised Causal Discovery](https://arxiv.org/abs/2609.37446)

**<font color=#1a73e8>作者：</font>** Pingchuan Ma, Rui Ding, Bojun Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervised causal discovery learns to infer causal structure for a new dataset from training datasets paired with structural labels. These training pairs are typically simulated, making the simulator both a source of supervision and a carrier of assumptions about causal graphs, mechanisms, and noise. Understanding the resulting predictions therefore requires examining how these assumptions supplement the information available in observational data, which may be compatible with multiple causal graphs. This paper examines that relationship across representative methods available through June 2026. We organize these methods by prediction target, prediction granularity, encoder, structural decoder, and training regime to relate what each method predicts to how it uses data and simulator-based supervision. Using this framework, we distinguish two questions: whether the target is identifiable under the assumed model class, and whether a trained predictor generalizes beyond its training distribution. Restrictions on mechanisms and noise can make otherwise ambiguous causal directions identifiable, but predictive accuracy under those restrictions does not establish transfer when they change. This distinction motivates evaluation that matches metrics to the identifiable graph target and tests changes in graphs, mechanisms, and noise between training and deployment. Extending such evaluation to real data also requires documenting the external causal evidence and uncertainty behind benchmark reference graphs. Together, these analyses guide method comparison and identify open questions in transfer, test-time adaptation, and uncertainty assessment.

---


### 325. [Engineering Efficient Self-Play Chess: Search, Replay, and Throughput Under Limited Compute](https://arxiv.org/abs/2609.37447)

**<font color=#1a73e8>作者：</font>** Bertil Braun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How strong can an AlphaZero-style chess system become under limited training compute when its entire learning loop is engineered for efficiency? We train from random initialization through searched self-play on a single eight-GPU node for 2.5 days. The resulting 6.32-million-parameter model reaches 3,251 benchmark Elo [3,206, 3,297] at 100,000 searches per move (estimated at under five seconds of thinking time) against a fixed-node Stockfish 13 ladder. The run ingests 3.25 million completed games, involves an estimated 100 billion search simulations, and makes 836.6 million training presentations. We investigate search allocation, replay and restart-state selection, policy representation, progressive model sizing, quantized inference, and throughput engineering. Alongside the retained design, we document plausible alternatives that failed to improve the complete learning loop or did not justify their cost. The reported strength is a result of the integrated system, not an isolated Elo gain attributable to any single choice.

---


### 326. [Event-Only Wingbeat Counting under Camera Motion: A Controlled MuJoCo Benchmark](https://arxiv.org/abs/2609.37465)

**<font color=#1a73e8>作者：</font>** Zhang Nengbo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Counting completed wingbeats requires identifying individual cycles, including during frequency changes and pauses; estimating a dominant frequency alone is insufficient. Camera motion further mixes target and background brightness changes in event observations. We present a controlled MuJoCo benchmark that separates motion training from event-only image translation compensation. The acquisition contains 324 streams from 24 independent scenes, three flapping geometries, two distances (1.5 and 3.0 m), and static, moderate-motion and stronger-motion views. Fifteen scenes are used for fitting, three for validation and six for held-out testing. A fixed causal temporal convolutional network is evaluated in a matched 2 x 2 ablation with three initialization seeds and compared with ridge, Fourier, autocorrelation and an adapted EEPPR baseline. Under moderate motion, paired motion training reduces count mean absolute error from 31.130 to 3.185 cycles at 1.5 m and from 42.019 to 5.444 at 3.0 m. Adding the tested compensation increases these errors to 4.630 and 10.185, respectively. A Fourier baseline achieves 0.944 cycles at 1.5 m under moderate motion, showing that the neural model is not uniformly best. We report exact-count accuracy and temporally matched cycle F1 alongside count error. These findings support motion-aware training in this small synthetic benchmark, while exposing limits of simple event-background stabilization. They do not establish real-sensor performance, aerodynamic flight, or generalization to unseen vehicle types.

---


### 327. [Smooth Sailing through Spherical Shells: Provable Random-Lattice Sieving in Time $2^{0.292n}$](https://arxiv.org/abs/2609.37482)

**<font color=#1a73e8>作者：</font>** Emmanouil Doulgerakis, Thijs Laarhoven  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In an attempt to close the gap between the best provable and heuristic algorithms for hard lattice problems, such as the shortest (SVP) and closest vector problem (CVP), we analyze lattice sieving on Haar-random unimodular lattices. With well-chosen modifications to heuristic sieving, we show that the heuristic assumptions are no longer necessary, and we can provably achieve the same complexities as heuristic sieving on Haar-random lattices for various lattice problems. Concretely, with probability $1 - o(1)$ over the randomness of the Haar-random lattice and the algorithmic randomness, we show how to:
1. Solve SVP in time $2^{0.2924\ldots n + o(n)}$ and space $2^{0.2075\ldots n + o(n)}$;
2. Solve CVP for random targets with the same complexities;
3. Produce $2^{0.2075\ldots n + o(n)}$ discrete Gaussian samples at any width with these complexities, up to a $2^{-\Omega(n)}$ error in the joint distribution.
This improves on the SVP complexities for Haar-random lattices of Pouly-Shen [Eurocrypt, 2026] running in time $2^{0.633n + o(n)}$ and space $2^{0.5n + o(n)}$, as well as the recent worst-case SVP (and average-case CVP) improvements of Gao-Feng-Hu and Hhan [Cryptology ePrint Archive, 2026], both running in time and space $2^{0.5n + o(n)}$ or higher.
Similar to standard sieving methods, our approach proceeds through a series of thin spherical shells, starting from a large radius and iteratively combining vectors to obtain vectors from shells with smaller radius. Our main technical contribution is making a series of adjustments to guarantee that for each sieve list generated at each spherical shell, each list vector is independent and uniformly random over all lattice points within this shell. Once this invariant is satisfied, it is a matter of smooth sailing through the spherical shells until we find a solution.

---


### 328. [Dual lattice attacks for bounded distance decoding, revisited](https://arxiv.org/abs/2609.37483)

**<font color=#1a73e8>作者：</font>** Thijs Laarhoven  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Analyses of dual lattice attacks have often assumed that the individual scores associated with short dual vectors are mutually independent. Laarhoven-Walter used this heuristic to derive explicit trade-offs between the target radius and query time for bounded distance decoding (BDD) with preprocessing. Ducas-Pulles subsequently demonstrated theoretical and experimental failures of this heuristic and proposed an alternative model conditioned on the target norm.
In this note, we prove an explicit asymptotic trade-off for (decision-)BDD with preprocessing in the Haar-random lattice model, without heuristic assumptions. Using moment identities of Siegel and Rogers, we analyze cosine scores over complete dual balls and bound both error probabilities when distinguishing targets planted at a prescribed radius from uniform targets modulo the lattice. Optimizing the dual radius yields a trade-off between target radius and query time that matches the asymptotic prediction from the conditional model of Ducas-Pulles.

---


### 329. [Physics-Guided Flow-Map Matching for Precipitation Nowcasting](https://arxiv.org/abs/2609.37487)

**<font color=#1a73e8>作者：</font>** Shunya Nagashima, Takumi Bannai, Makoto Misaizu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precipitation nowcasting, generating future radar fields from past observations, is critical for flood warning and disaster response. It is also a demanding benchmark for spatiotemporal generative modeling, with chaotic dynamics, heavy-tailed intensities, and rare high-intensity structures that matter most. Deterministic models minimize a pixel loss and are driven toward the conditional mean, which blurs exactly those structures, while generative models that add a stochastic residual on top of a deterministic backbone inherit the same blur. We propose Physics-Guided Flow-Map Matching (PG-FMM), a conditional flow-map model that decouples predictable advection from uncertain small-scale detail. A frozen Lagrangian advection prior transports the radar field and supplies an explicit motion forecast, and a flow-map generative head, conditioned on the past frames and the prior rollout rather than summed onto it, produces sharp stochastic detail in four sampling steps. The prior serves only as guidance, so the head replaces blurred structure instead of inheriting it. Extensive experiments on four radar benchmarks show that PG-FMM outperforms state-of-the-art methods on 18 of 24 metrics, with the largest gains at heavy-rain thresholds, where the critical success index improves by up to 58.9%. The project page can be found at this https URL.

---


### 330. [Attention-Scoped Guidance: Training-Free Spatial Control for Image Editing](https://arxiv.org/abs/2609.37492)

**<font color=#1a73e8>作者：</font>** Zeyan Li, Wei Zhou, Hadi Amirpour 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-guided image editing should change what the instruction names and leave the rest of the image untouched. In dual classifier-free guidance (CFG), an editor combines two directions at every denoising step, one that pushes toward the instructed edit and one that pulls back toward the source image, using global weights. We introduce Attention-Scoped Guidance (ASG), a sampler wrapper that makes these weights spatial. It reads a soft support map from the instruction attention that the editor already computes, then weakens text guidance where support is low and strengthens image anchoring where support is high. The wrapper requires no training, no external mask, and no additional network evaluation. On the full MagicBrush and PIE-Bench++ splits, ASG improves preservation-oriented metrics, leading three of four MagicBrush metrics and PIE-Bench++ background PSNR. A dose-matched control that removes the spatial placement loses up to 0.73 CLIP on PIE-Bench++, confirming that the spatial allocation itself carries the gain.

---


### 331. [Your Benchmark Is Not Saturated: Reviving Multiple-Choice Evaluation with Answer Pooling](https://arxiv.org/abs/2609.37494)

**<font color=#1a73e8>作者：</font>** Mohamed Eltahir, Abobaker Ahmed, Nawaf Barebood 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multiple-choice benchmarks are cheap to grade and are running out of room, and the standard remedy, writing harder items, is slow and repeated for every benchmark. A saturated benchmark still holds a harder task. Each question's wrong options are written for that question alone, so a model can score by eliminating a few options. We propose AnswerPool: take $N$ questions that share a context, pool all their options into one list, and ask the model to assign every question its answer. No item is written and no label changes. The chance of guessing a group right falls from $10^{-3}$ to $5\times10^{-7}$ for five four-option questions, and a model that recognizes its answers keeps its multiple-choice score, so the accuracy lost to pooling measures the credit the format gave for elimination. Deleting answers from the pool makes questions unanswerable with exact ground truth, so abstention is scored in the same pass. Across eight text, image, and video benchmarks and eighteen models, pooling is harder for every model, the elimination credit is largest for the weakest models, and seven of eight open-weight models answer 87 to 100% of unanswerable questions.

---


### 332. [MotionMaestro: Masked Tokenization for Unified Motion Generation](https://arxiv.org/abs/2609.37495)

**<font color=#1a73e8>作者：</font>** Yun Chen, Munchurl Kim, Jeonghyeok Do  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human motion generation plays an important role in applications such as character animation, virtual environments, and embodied interaction. While existing approaches have achieved remarkable progress, many of them are developed for individual tasks, including text-to-motion, pose-conditioned generation, and trajectory control. Although these tasks involve different types of conditions, a unified framework capable of handling them within a common representation would greatly simplify motion generation systems. We observe that diverse motion conditions can be naturally formulated as different observation patterns over motion sequences, where each task corresponds to a specific masking strategy. Based on this insight, we introduce MotionMaestro, a unified motion generation framework that learns a shared representation for complete motions and heterogeneous partial observations through masked motion tokenization. MotionMaestro employs a three-stage training strategy that first learns a masked motion tokenizer, then refines its reconstruction ability on clean motions, and finally trains a conditional flow-matching generator in the learned latent space. Furthermore, we introduce an observation map and an observation loss to explicitly preserve provided motion conditions during generation. With this unified representation and conditioning mechanism, MotionMaestro supports text-guided and unconditional synthesis, pose conditioning and partial completion, temporal interpolation, trajectory control, and motion continuation. Experiments on the large-scale RoMo and MotionMillion datasets show state-of-the-art performance across diverse motion generation tasks.

---


### 333. [ScaGNN: a Graph Neural Network for Multiple Scattering Simulations](https://arxiv.org/abs/2609.37509)

**<font color=#1a73e8>作者：</font>** Rémi Marsal, Stéphanie Chaillat, Alexandre Chapoutot  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The boundary element method (BEM) provides an efficient numerical framework for solving multiple scattering problems in unbounded homogeneous domains. By restricting the discretization to the domain boundaries, it substantially reduces computational complexity. The procedure first consists in determining the solution trace on the boundaries of the domain by solving a boundary integral equation. Then, the volumetric solution can be recovered at low computational cost using a boundary integral representation. As the first step of the BEM represents the main computational bottleneck, we present ScaGNN, a learning-based approach designed to approximate the solution trace. It relies on a graph neural network architecture that incorporates a dynamic adaptive edge sampling mechanism for selecting the most relevant interactions to model. Guided by intermediate predictions of expected error and edge length, this mechanism selects, at various stages of the forward pass, the most relevant distant interactions to model. The proposed method is tailored to achieve linear complexity with the number of nodes in the input graph. To train and evaluate our network, we present a benchmark consisting of several datasets with different types of multiple scattering problems. Our experiments show that our approach surpasses existing state-of-the-art learning-based methods on the considered tasks and investigate the generalization capabilities to settings with an increased number of obstacles and out-of-distribution obstacle shapes. this http URL

---


### 334. [Physical Muon: Orthogonalization as an Equilibrium Computation](https://arxiv.org/abs/2609.37525)

**<font color=#1a73e8>作者：</font>** Yuren Hao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical neural networks and analog in-memory computing could reduce the energy cost of neural network training. Realizing this potential, however, requires optimizers that combine effective learning with physical implementability. SGD fits local analog updates but struggles on transformers, while Adam family is unstable against analog bias. Muon offers strong training performance, but its Newton--Schulz orthogonalization relies on dense matrix-matrix products. To address this obstacle, we introduce Physical Muon, which computes the orthogonalization as the equilibrium of a continuous-time flow. Random probes approximate the flow using matrix-vector products, reciprocal reads, and local rank-1 writes. To test whether this replacement preserves training performance, we evaluate it on a 10.95M-parameter transformer. The dense flow's mean validation cross-entropy is 0.0085 above Newton--Schulz across nine seeds per method; the probe implementation is 0.0188 above the control across two seeds. Circuit simulations further reproduce the flow dynamics and yield comparable training behavior.

---


### 335. [Principled MAP estimation for inverse problems: bridging the gap between convergence and performance](https://arxiv.org/abs/2609.37529)

**<font color=#1a73e8>作者：</font>** Alexandre Lagier, Valentine Tosel, Anne Gagneux 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained denoisers provide a powerful way to incorporate image priors into restoration algorithms. Plug-and-Play and RED approaches exploit fixed-noise-level denoisers within first-order optimization schemes, with convergence guarantees, but often struggle to achieve high-quality reconstruction on severely ill-posed inverse problems. In contrast, recent state-of-the-art approaches leverage denoisers derived from flow- or diffusion-based generative models and evaluate them along a sequence of decreasing noise levels. While these methods achieve strong empirical performance, their convergence theory remains limited. In this paper, we bridge this gap by specifically designing an algorithm that combines denoisers at decreasing noise levels with a schedule tailored to ensure convergence. From a Bayesian perspective, we prove that our method converges to a $\textit{Maximum a Posteriori}$ (MAP) estimate, under suitable assumptions. Subsequently, we apply our method to various ill-posed inverse problems and show that it surpasses convergent methods while competing with state-of-the-art empirical ones.

---


### 336. [Weeding Out Bad Seeds: Initial-Noise-Robust Unlearning for Text-to-Image Diffusion Models](https://arxiv.org/abs/2609.37537)

**<font color=#1a73e8>作者：</font>** Arian Komaei Koma, Seyed Amir Kasaei, Aida Aryafar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning has emerged as a critical post-hoc safety measure to erase sensitive concepts from Text-to-Image (T2I) models without prohibitive retraining. However, we reveal that current state-of-the-art (SOTA) approaches are brittle due to a severe lack of robustness to noise initialization. We call this phenomenon ``probabilistic forgetting'': suppressed concepts re-emerge under specific random initial noise conditions, despite appearing unlearned on other initializations. We trace this failure to the misalignment between standard Gaussian sampling during unlearning and the unlearning objective. Since the target concept manifests only in specific initial noise regions throughout the unlearning phase, uniform random sampling yields sparse, uninformative gradient updates that fail to drive robust erasure. To overcome this issue, we propose an adaptive, concept-conditioned sampling strategy that dynamically concentrates gradient updates on regions where the target concept manifests, down-weighting uninformative areas. We integrate our framework with six distinct SOTA unlearning methods across four diffusion backbones and evaluate it across safety, object, and artistic-style unlearning, as well as under black-box and white-box adversarial attacks. Our method reduces the conditional nudity re-emergence rate across random initializations by 67.2% on average over four baselines and lowers attack success rates across both adversarial evaluations. Across concept domains, Adaptive Noise Sampling strengthens adversarial robustness and non-target retention while preserving competitive generative quality and target-erasure performance.

---


### 337. [RunyaNER: Auxiliary Language Selection for Runyankore NER](https://arxiv.org/abs/2609.37543)

**<font color=#1a73e8>作者：</font>** Prosper Arineitwe Asiimwe, Francois Meyer, Jan Buys  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual zero-shot transfer and multilingual fine-tuning are promising approaches for NLP tasks such as Named Entity Recognition (NER) in low-resource languages, but in the absence of target language benchmarks, it is unclear which auxiliary language selection strategy leads to the best transfer. We introduce RunyaNER, the first publicly available NER benchmark for the East African language Runyankore, and use it to investigate the choice of which languages to use for transfer. Created with a semi-automated pipeline and fully manually verified, RunyaNER contains over 237k annotated words across 30k sentences. We benchmark pretrained models on RunyaNER, establishing that our dataset is of sufficient quality and size to produce effective Runyankore NER models. We then use RunyaNER to investigate auxiliary language selection in cross-lingual zero-shot and multilingual fine-tuning settings. Our experiments show that while transfer performance is highly sensitive to auxiliary language selection, embedding-based measures computed from labelled training spans correlate more strongly with downstream transfer performance than traditional linguistic features based on metadata or typology. By releasing RunyaNER and providing a systematic analysis of auxiliary language selection strategies, this work contributes both a new benchmark resource and practical insights for multilingual transfer in low-resource settings.

---


### 338. [Benchmarking graph-based models for in-silico toxicity prediction in drug discovery](https://arxiv.org/abs/2609.37555)

**<font color=#1a73e8>作者：</font>** Noel Suarez-Barro, Manuel Lama, Juan C. Vidal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug discovery is a costly and high-risk process, where toxicity-related failures remain a major cause of attrition in both preclinical and clinical stages. As a result, accurate early prediction of chemical toxicity is essential to reduce downstream costs and improve compound prioritization. In this context, graph deep learning (GDL) has emerged as a powerful paradigm for toxicity prediction, leveraging molecular graph representations to learn directly from chemical structure with improved expressivity over traditional approaches.
Despite the growing number of proposed models, current literature-based comparisons are often difficult to interpret due to inconsistencies in datasets, preprocessing pipelines, and evaluation protocols. To address this limitation, we introduce a unified and standardized benchmarking framework for GDL-based toxicity prediction. We systematically evaluate more than 20 representative approaches under consistent experimental conditions and across multiple datasets and partitioning strategies, enabling a fair and reproducible comparison of model performance. In addition, we complement this empirical study with a structured literature analysis to contextualize existing methodological trends and performance claims. Our results provide a clearer and more reliable assessment of the current state of the field, highlighting both the strengths and limitations of existing graph-based approaches. To support transparency and reproducibility, we release our benchmarking framework as open-source software this https URL, allowing the community to evaluate and compare models under consistent conditions.

---


### 339. [APM-Bench: Benchmarking Cross-session Persistent Memory for Egocentric Streaming Video Assistants](https://arxiv.org/abs/2609.37559)

**<font color=#1a73e8>作者：</font>** Jianguo Huang, Jinming Liu, Qiyao Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To serve as real-world personal assistants, streaming video models need persistent memory that retains past experiences for later use. Yet existing streaming benchmarks and methods often focus on individual continuous videos or short clips, overlooking that real-world interactions are often intermittent and require memory to persist across interruptions. To fill this gap, we introduce APM-Bench, which reformulates real-world streaming interaction as multi-session life trajectories. It contains 549 sessions, 104 trajectories, and 2,719 candidates, spanning both objective and open-ended questions. Each session is a video with fine-grained annotations, and sessions within a trajectory revolve around related activities. Models then use persistent memory to answer questions about past sessions and provide proactive responses while maintaining real-time interaction. This raises challenges: persistent memory must be storable, selectively retain information, be injected at the right time, and remain efficient. Moreover, finite storage may leave required evidence unavailable, so assistants should recognize missing evidence. Therefore, we systematically evaluate general video models under different memory protocols and diverse specialized streaming memory systems, and test whether models acknowledge insufficient evidence. Our evaluation reveals a clear utility--latency--storage trade-off: existing methods still struggle to simultaneously achieve reliable long-term recall, low overhead, and effective proactive assistance across sessions. APM-Bench provides a comprehensive testbed for developing and comparing persistent memory systems under realistic streaming conditions. We hope it encourages future work that jointly considers utility, latency, and storage toward more practical persistent memory for real-world streaming assistants.

---


### 340. [Orthogonal Yet Coupled: Decoupling Geometric Components for Model Merging](https://arxiv.org/abs/2609.37564)

**<font color=#1a73e8>作者：</font>** Zijing Wang, Yongkang Liu, Mingyang Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Merging pretrained models has emerged as an effective approach for consolidating diverse capabilities into a single unified model. However, prevailing merging methods typically treat each task vector as an indivisible merging unit, overlooking the heterogeneous geometric changes encoded within it. This treatment can induce cross-component coupling: when merging decisions are derived from statistics of the complete task vector, the geometric characteristics of one component may influence how another is selected, weighted, or combined, potentially degrading the quality of the merged model. To address this issue, we propose DiGA, a
Disentangled Geometry-Aware model merging framework. Using the pretrained weights as a shared geometric reference, DiGA orthogonally decomposes each task vector into components corresponding to distinct geometric attributes. Rather than merging the task vectors as a whole, DiGA aggregates corresponding components independently within their respective subspaces and subsequently recombines them into a unified update. This component-wise formulation preserves the geometric identity of each component and prevents the characteristics of one component from interfering with the aggregation of another. Furthermore, DiGA can be incorporated into a broad range of existing model merging methods. Extensive experiments across diverse models, tasks, and merging methods demonstrate that DiGA improves merged-model performance and reduces capability degradation. Our repository is on this https URL.

---


### 341. [A Model-Agnostic Physics-Guided Adapter for Few-Shot Transfer of Coastal Flood Prediction Models to Unseen Regions](https://arxiv.org/abs/2609.37565)

**<font color=#1a73e8>作者：</font>** Bilal Hassan, Areg Karapetyan, Samer Madanat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning surrogates can produce high-resolution coastal flood maps orders of magnitude faster than physics-based hydrodynamic simulators, yet transferring them to new coastal regions remains costly, since generating target-region data for fine-tuning typically requires numerous time-consuming simulations. To tackle this bottleneck, we introduce the Physics Adapter (PA), a compact, architecture-agnostic adaptation interface that enables efficient few-shot transfer of flood prediction models across diverse coastal regions. PA predicts peak water level through a differentiable wet/dry response that compares terrain elevation against a learned water level, and blends this physics-structured prediction with a data-driven branch through a learned gate. Unlike physics-informed formulations, PA imposes no PDE-residual or conservation losses and instead exploits elevation as an architectural inductive bias, adding a negligible number of trainable parameters. We integrate PA into 12 heterogeneous models, and evaluate them on two coastal regions with markedly distinct geometries, topographies, and shoreline protection configurations. The performance of PA is benchmarked against a no-physics baseline, full fine-tuning, and standard parameter-efficient fine-tuning (PEFT) methods, considering both within-region generalization to unseen sea level rise values and between-region transfer. In low-shot regime (K=3), and averaged over all backbones and transfer settings, adding PA reduces root mean square error by 11.5% when only the output head is adapted on a frozen backbone, by 15.4% when combined with PEFT methods, and by 22.9% under full fine-tuning, compared to matched configurations without PA. Taken together, the findings of this work offer practitioners a concrete recipe for extending DL-based coastal flood predictors to new, data-scarce regions.

---


### 342. [RAVEN: Receiver-Conditioned Action-Value Encoding for Finite-Alphabet Multi-Agent Communication](https://arxiv.org/abs/2609.37566)

**<font color=#1a73e8>作者：</font>** Shuwei Sun, Chenxi Wang, Jian Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A message drawn from a small alphabet helps a teammate only if it keeps the distinctions that change that teammate's next decision. We show that scoring messages by action values averaged over the receiver's situation can erase exactly these distinctions, and we propose RAVEN (Receiver-conditioned Action-Value ENcoding), which trains a four-symbol, one-step-delayed channel to preserve each receiver's centered action-value profile within the receiver's own context. The sender never needs to know that context: the receiver decodes every symbol with its private information. We give two estimators of this target. With a teacher, offline RAVEN selects the codebook that exactly minimizes an empirical conditional distortion and distills it into a frozen sender; we bound the resulting codebook-selection error and one-step decision loss. Without a teacher, online RAVEN aligns, inside a QMIX learner, the deployed symbol pathway with a training-only continuous reference that shares its routing. Against five recent communication methods on eight navigation settings, offline RAVEN attains the highest return in seven, and removing receiver conditioning forfeits 83% of its communication gain. Online RAVEN raises predator-prey capture success from 53.2% to 96.0% over the same QMIX backbone without communication, and on SMAC and MPE it attains the best mean normalized score of 14 methods, including methods that exchange kilobit messages. Every RAVEN message costs 2 bits, 12-1,024x fewer than those of NDQ, CACOM and ExpoComm on navigation.

---


### 343. [FedSocket: Recipient-Executable Knowledge Exchange for Heterogeneous Multimodal Federated Learning](https://arxiv.org/abs/2609.37582)

**<font color=#1a73e8>作者：</font>** Xinyuan Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated knowledge must remain usable by recipients with different modalities, private architectures, and tasks. We present FedSocket, which makes recipient execution a design requirement of the exchanged model. A shared Q combines recipient-computable inputs, task-owned outputs, and ownership-aware aggregation, connecting heterogeneous private models through a common prediction interface. Private models teach local Q copies; the returned Q supports local learning and Joint inference, with only Q parameters and counts exchanged. Across six datasets, FedSocket improves missing-modality recipient accuracy over Local by 14.44 and 15.51 percentage points on MELD and UCF-51. Under matched inference capacity, Joint exceeds independent ensembles by 11.06 points in UCF-51 accuracy and 4.87 points in mean bidirectional Flickr30k R@1. Joint also improves over Q alone on all four heterogeneous endpoints, demonstrating the value of combining local and exchanged predictions. Teacher controls, sharing-path interventions, and component factorials identify the roles of supervision, sharing, and deployment. FedSocket makes exchanged knowledge directly usable from federated training to recipient inference.

---


### 344. [GraphVQ: Structure-Aware Autoregressive Decoding over Context-Quantized Graph Tokens](https://arxiv.org/abs/2609.37604)

**<font color=#1a73e8>作者：</font>** Yuxiang Yao, Zijun Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph foundation models need a discrete token representation, but casting a graph as a generatable token sequence faces a structural obstacle: edges spanning beyond the serialization window cannot be emitted in one pass--so one-pass autoregressive generators systematically under-produce cycles--and a single global condition cannot tell candidate edges apart. GraphVQ removes both obstacles: node contexts--features plus a local edge mask under multi-order breadth-first serialization--are quantized into a shared codebook by a VQ-VAE with BCE-calibrated Bernoulli edge decoding, and a second-stage structure-aware decoder emits the global adjacency conditioned on token-derived pair features, whose necessity over any global-summary condition is formalized in a scoped impossibility result. The tokenizer reconstructs node features at 0.86--0.99 accuracy and decodes local edges at AUROC >= 0.89 (ECE <= 0.007). Under one same-split protocol on four datasets, pair conditioning improves orbit MMD 0.248 -> 0.174 on PROTEINS and 3.4x on a ring stress test, and vanishes on a random-label control--the signature of attribute--topology coupling--so the gain is claimed exactly where attributes carry edge-relevant signal. GraphVQ ranks first among learned generators on PROTEINS, ties for first on SYN-COMM, and improves orbit MMD 2.7--17x over one-stage generation on three datasets, with seed-level bootstrap intervals confirming the rankings are not seed noise; on MUTAG the unweighted edge target under-generates and is reported as such. These results locate the structural control of autoregressive graph generation in the granularity of the condition: pair-level token context turns a quantized vocabulary into a usable capacity axis for distribution-faithful graph generation and future token-level pretraining.

---


### 345. [Harvest Season for SLUB: From io_uring vulnerability to Novel Sheaf-Based Exploitation Techniques](https://arxiv.org/abs/2609.37608)

**<font color=#1a73e8>作者：</font>** Hao-Yu Yang, Yu-Ting Lin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Linux kernel's push for higher I/O performance and more efficient memory management has introduced new mechanisms that, while improving performance, also open new attack surfaces. This research examines two of them together: the io_uring subsystem and the sheaf/barn caching mechanism added to the SLUB allocator in Linux 6.18. In this research, two previously unknown vulnerabilities in io_uring are presented, and one is developed into a complete local privilege escalation chain under a hardened kernel configuration. Building this chain revealed that the sheaf/barn mechanism changes long-standing assumptions behind established exploitation techniques such as cross-cache attack, and that its design also weakens existing SLUB freelist protections. Both observations are analyzed and turned into working primitives. Building on this analysis, three novel sheaf-based exploitation techniques are proposed. Among them, an RCU-sheaf cross-cache technique removes the traditional dependence on the buddy system for moving objects across caches, giving more flexible and reliable control over object migration between cache pools. Together, these results characterize the sheaf/barn layer as a new and largely unexplored attack surface in Linux kernel exploitation.

---


### 346. [PHASE: Multi-Regime Modeling of Incompressible Magnetohydrodynamics](https://arxiv.org/abs/2609.37609)

**<font color=#1a73e8>作者：</font>** Radhika Achikanath Chirakkara, Rajdeep Haldar, Zezheng Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Magnetohydrodynamics (MHD) is central to plasma modeling in astrophysics, space science, fusion, and engineering, but resolving multiscale MHD dynamics is computationally expensive. Machine-learning surrogates enable fast inference by learning reusable solution operators, yet existing models require separate training for each physical regime, limiting generalization across varying parameter settings. We introduce PHASE, a PHysics-Adaptive Scalable operator with residual Error correction, designed to model incompressible MHD across varying physical parameters with a single model. PHASE combines transfer learning, regime-aware adaptation, physics-centered learning, and residual refinement to improve both physical fidelity and generalization across MHD regimes. Together, these improvements achieve state-of-the-art prediction accuracy on two-dimensional MHD turbulence by reducing relative $L_2$ errors on physical fields by more than an order of magnitude compared to prior MHD neural-operator baselines. Moreover, PHASE generalizes successfully to unseen parameter values without retraining, demonstrating the cross-regime adaptability expected from operator learning. We evaluate PHASE beyond point-wise prediction errors using derived physical fields, spectral analysis, and distribution statistics, consistently observing improved physical fidelity. We further show that our framework can accurately simulate MHD instabilities by testing it on the Kelvin--Helmholtz instability, demonstrating the robustness of our method.

---


### 347. [Procedural Core: A Compact Recurrent Initialization for Vision Transformers](https://arxiv.org/abs/2609.37631)

**<font color=#1a73e8>作者：</font>** Zachary Shinnick, Christian Internò, Hemanth Saratchandran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers are typically trained from random initialization, requiring all their capabilities to emerge from large-scale optimization. Recent work showed that a small amount of abstract procedurally generated data can help acquire generic inductive structure at low cost. However, this adds a pretraining stage that must be repeated for every target model. We propose Procedural Core, an initialization strategy that captures this generic structure into a compact set of weights that can be reused across models. We train a minimal recurrent transformer on procedural data, then expand its weights to initialize transformers of arbitrary width and depth. The resulting initialization improves performance on image classification, self-supervised visual learning (DINO), and modeling natural language (FineWeb-Edu) and code (CodeParrot). For image classification, expanding a 1M-parameter core to initialize an 85M-parameter ViT-Base improves ImageNet top-1 accuracy by 2.2 pp over standard random initialization. Our analysis identifies recurrence as essential for learning compact weights that transfer across models. In ViTs, we localize a key benefit in the suppression of high-norm tokens that produces substantial improvements in zero-shot segmentation (ImageNet-S mAP 32.3 to 42.9), object localization (VOC07 CorLoc 9.9 to 18.4), and depth estimation (NYUv2 RMSE 1.104 to 0.998). This demonstrates that transformers need not start from a blank slate, and can be initialized with generic capabilities at low cost with no domain- or task-specific data.

---


### 348. [ProCTI: Prototype-Refined Global Conditioning for Diffusion-Based Time Series Imputation](https://arxiv.org/abs/2609.37632)

**<font color=#1a73e8>作者：</font>** Fariza Rashid, Duc Van Le, Rahat Masood 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series imputation has progressed from statistical and deep learning approaches to diffusion-based models, which have shown strong recent performance. Existing diffusion-based methods typically condition the reverse process using local contextual information from the current or neighbouring windows. Meanwhile, global dataset-level structure often remains implicit, limiting performance when local observations are sparse, noisy, or unrepresentative. To address this issue, we propose ProCTI, a diffusion-imputation framework that augments local conditioning with retrieved global dataset-level priors through learned prototypes. A hybrid conditioning mechanism integrates this global context with local signals during reverse diffusion, enabling more accurate reconstruction under varying missingness scenarios. Experiments across multiple benchmark datasets show that ProCTI outperforms strong baselines overall under random missingness, while remaining competitive under attribute-wise missingness. Furthermore, we use a latent-regime data model to characterise the precise conditions under which prototype-derived global conditioning provably improves imputation. We support this with a general theoretical analysis of local-global conditioning.

---


### 349. [Rhythm Is a Dancer: Designing Interactive Rhythm Feedback for Beginner Dancers](https://arxiv.org/abs/2609.37641)

**<font color=#1a73e8>作者：</font>** Bettina Eska, Annika Kilian, Paweł W. Woźniak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Learning how to dance can readily overwhelm beginners, especially without effective guidance from a dance teacher. Existing interactive systems often do not sufficiently support the learner's progress. We investigated how targeted feedback on rhythm keeping interactively supports dance practice for novice dancers by introducing SkeletonDance. Our design is grounded in motor learning theory and conceptualized through interviews with dance teachers, following established teaching strategies. SkeletonDance automatically detects rhythm flaws and provides assistance through mimicking clapping feedback, a common instructional technique in dance lessons. In our study, participants reported that SkeletonDance helped them to re-establish lost rhythm and increased confidence during practice, especially among novices. Though objective performance metrics did not consistently confirm these effects during controlled test sessions. Our work highlights that feedback can support novice dancers' subjective practicing experiences and demonstrates how prior dancing experience moderates the objective effectiveness of such minimal, teacher-inspired interventions.

---


### 350. [Flattening the Connectome Spectrum: A Spectral Filter for FC Induces a Pretraining Target for fMRI Encoders](https://arxiv.org/abs/2609.37642)

**<font color=#1a73e8>作者：</font>** Giovanni Marraffini, Victoria Shevchenko, Carlo Alberto Barbano 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-supervised pretraining reshaped prediction in language and vision, and brain foundation models (BFMs) inherited its promise. Representations learned from large unlabelled corpora should capture individual functional dynamics and generalise across cohorts. However, kernel ridge regression (KRR) fitted on functional connectivity (FC) matrices still predicts individual phenotypes more accurately than any BFM we tested. In this paper, we show that KRR is weighted by the eigenvalues of the FC which are miscalibrated for phenotype prediction. We apply an efficient spectral filter to recalibrate the eigenvalues of each subject's FC matrix, enabling the model to exploit more inter-individual variance. Across the 5 datasets, 11 parcellations and 6 prediction targets we tested, we match or exceed the KRR baseline. Based on this finding, we then pretrain a small encoder model on about 4,000 hours of fMRI from 162 open datasets, whereby we align the pairwise similarities between the embeddings of recording snippets with those between the recalibrated connectomes. Our model performs on par with the best of the 6 published BFMs we tested while having an order of magnitude fewer parameters. Our encoder performs better than FC on short scans and in smaller cohorts, especially in fingerprinting. We release the pretrained model weights, the code and the pretraining data, preprocessed and parcellated.

---


> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-447](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

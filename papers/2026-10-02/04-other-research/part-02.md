# 📦 其他研究 | 2026年10月02日

> 本类共 **382** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-382](./part-08.md)

---

### 51. [ReLaG: A Scalable Framework Generalizing Random Splits to Data with Latent Relations](https://arxiv.org/abs/2609.38538)

**<font color=#1a73e8>作者：</font>** Anthony Lavertu, Jacob Cote, Sophie Gobeil 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Random splitting can yield non-independent train--test subsets when a dataset contains related samples, as is common in certain applications such as biochemical studies. This leads to overly optimistic generalization estimates. Here, we introduce ReLaG, a modality-agnostic framework that models sample relatedness through a hierarchical latent-variable process and infers groups of related samples using proximity graphs and community detection to produce independent train--test subsets. Across molecular and protein datasets, ReLaG matches existing relation-aware methods while scaling substantially better, enabling splits at previously impractical dataset sizes. We further introduce a label-free procedure that adapts the splitting resolution to production data, aligning evaluation with the intended deployment setting. ReLaG's inferred groups provide a cheap estimate of effective dataset size, enabling diversity-aware dataset scaling. ReLaG is open source and can be installed with pip install relag.

---


### 52. [When a Flatness Proxy Is Not a Function: Robustness Certificates and Training Interventions](https://arxiv.org/abs/2609.38540)

**<font color=#1a73e8>作者：</font>** Vicente Opazo, Jose Calatayud-Mateu, Cristobal Rojas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A valid curvature upper bound need not justify either a robustness certificate or an intervention on an intrinsic predictor property. We demonstrate this distinction for a last-layer relative-flatness proxy used in both settings. First, empirical-risk stationarity does not eliminate pointwise first-order loss terms: at a finite global empirical-risk minimum, the retained certificate expression underestimates a loss increase by over $210\times$. We derive a globally valid, gauge-invariant feature-space repair. Second, common-row softmax shifts preserve predictions and the exact contraction while making the proxy unbounded. Even standard reference-class choices double it on average relative to the centered representation. For a single fixed-feature example with at least three classes, scalar retuning generically cannot align the induced probability updates. Row centering gives the orbit-minimized bound and restores value and full-model gradient invariance under this symmetry. Across 45 paired one-step tests on algorithmic and image models, amplified shifts separate raw-regularized predictors while quotient-regularized predictors remain aligned. Long-horizon CIFAR-10 experiments show substantial, reversible suppression of generalization, while evidence for selective delay after memorization is less consistent. Together, these results show that validity as a curvature upper bound does not by itself justify either inversion into a robustness certificate or differentiation into an intrinsic training intervention.

---


### 53. [Towards Universal Wasserstein Barycenters through Flow Matching](https://arxiv.org/abs/2609.38547)

**<font color=#1a73e8>作者：</font>** Eduardo Fernandes Montesuma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Defining a weighted mean over probability measures under probability metrics is a central tool in probabilistic machine learning. Under the Wasserstein metric, these are called \emph{Wasserstein barycenters}. While most approaches compute barycenters for a fixed weight vector, approximating the whole family of barycenters over the simplex, which we call the \emph{Wasserstein simplex}, remains underexplored. We refer to this problem as \emph{Universal Barycenter Approximation}, and propose \texttt{BaryFM}, a flow matching model transporting the marginal measures into any barycenter in the Wasserstein simplex. Once trained, the network can draw samples from measures in the Wasserstein simplex through an ordinary differential equation. We validate our method on 4 downstream tasks: domain adaptation, generalization, Bayesian posterior aggregation and algorithmic fairness. \texttt{BaryFM} achieves the best average rank among 15 competing methods across 10 domain adaptation benchmarks, matching or surpassing non-universal solvers.

---


### 54. [Fairness Theatre: Evaluating Post-Hoc Fairness Interventions in Vendor-Controlled Early Warning Systems](https://arxiv.org/abs/2609.38552)

**<font color=#1a73e8>作者：</font>** Kelly McConvey, Angelina Zhai, Rebecca Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Public institutions increasingly procure AI systems whose design they cannot inspect or change. In higher education, proprietary Early Warning Systems (EWS) leave colleges with few options beyond adjusting model outputs to address inequity. This raises the question of how fairness work is coordinated among vendors, institutions, advisors, and students with unequal power to change these systems? Using student records from a public college in Ontario, Canada, we evaluate six post-hoc fairness interventions on a research EWS under simulated procurement constraints. We compare fairness, accuracy, and demographic disparities, introducing error-type profiling to trace how interventions redistribute false positives and false negatives. Interventions redistributed disparities without consistently reducing them. Two implementations favored already-advantaged groups because they used group size to define disadvantage; small, marginalized groups remained poorly served. These findings show how procurement constraints and implementation choices shape the possibilities for fairness work. We call the resulting condition fairness theatre; dashboard metrics converge while groups' error burdens persist or worsen.

---


### 55. [Detail in Context: A Dual-Scale Machine Learning Framework for Mycosis Fungoides Detection](https://arxiv.org/abs/2609.38560)

**<font color=#1a73e8>作者：</font>** Mohamed Hazem, Tarek Waleed, Omar Khaled 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mycosis fungoides (MF) is a rare form of cutaneous T-cell lymphoma that is often misdiagnosed in early stages due to its visual similarity to benign inflammatory dermatoses. Early and accurate diagnosis is critical for improving patient outcomes. In this paper, we propose a comprehensive diagnostic framework for automated MF detection that combines dual- scale histopathological image analysis with deep learning. To distinguish MF from other lymphoproliferative skin conditions, the proposed approach leverages a late-fusion ensemble of dual- magnification (10x and 20x) convolutional neural networks (CNNs), complemented by a random forest classifier trained on 16 clinical features. Experimental results on an expanded dataset of 6,267 images (4,306 MF; 1,961 Non-MF) across 463 patients demonstrate that strong detection performance is obtained by prioritizing higher-resolution cytological details (20x) within broader architectural context (10x). The image-based late-fusion model achieves an accuracy of 83.58% and a sensitivity of 89.13%, while the clinical random forest model achieves an accuracy of 96.6% and sensitivity of 93.8%, highlighting the po- tential of this multimodal framework as a robust clinical decision support system in dermatology. This framework addresses two distinct clinical objectives: an image-based dual-scale pipeline optimized for the early diagnostic screening of MF versus non- MF dermatoses, and a complementary clinical metadata model designed for the subsequent staging of confirmed MF cases (patch/plaque versus tumor)

---


### 56. [LongTake: Learning to Sustain Dynamics in Long-Horizon Video Generation](https://arxiv.org/abs/2609.38562)

**<font color=#1a73e8>作者：</font>** Byoungwoo Park, Jaemoo Choi, Juho Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models, game simulators, and long-take video creation require coherent scene evolution and sustained dynamics over extended durations. Autoregressive (AR) video diffusion provides a natural framework for long-horizon generation, yet extended rollouts often become near-static or lose visual quality. We hypothesize that these failures reflect the limited guidance provided by short-video supervision on how ongoing scene dynamics develops over longer durations. This motivates us to introduce LongTake, a two-stage training pipeline built around Long-Horizon Teacher Forcing (TF) on curated real long videos. Long-Horizon TF trains the AR model to predict later frames conditioned on long ground-truth video prefixes, extending direct supervision beyond the short training horizon. This supervision is designed to help the model sustain dynamics and preserve visual quality during long-horizon generation. Our central finding is that this training stage strengthens direct initialization for distribution matching distillation (DMD) under student self-rollout, without the intermediate few-step distillation stage used in standard pipelines. Under the same five-second DMD training setup, our initialization yields substantially higher dynamic degree than short horizon TF initialization on 30-second rollouts at comparable aesthetic quality, and surpasses the evaluated baselines in both measures. Hybrid DMD further reuses this teacher to extend supervision to later frames of the self-rollout while retaining bidirectional joint supervision over the initial window. On long-horizon self-rollouts, LongTake lies on the Pareto front of dynamic degree and aesthetic quality, and Hybrid DMD attains the highest dynamic degree among evaluated methods at both 30s and 60s.

---


### 57. [Retargeting Motions to Diverse Skeletons via Learnable Flattening](https://arxiv.org/abs/2609.38578)

**<font color=#1a73e8>作者：</font>** Kia-Jüng Yang, Fabian H. Sinz, Paweł A. Pierzchlewicz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-structural motion retargeting aims to transfer motion between different skeletal topologies. Despite recent progress, existing state-of-the-art models struggle with reliability in zero-shot settings, i.e. skeletons with different topologies which were unseen during training, and recent Transformer-based attempts have failed to outperform specialized geometric methods. We bridge this gap with a Transformer Autoencoder that learns a topology- and translation-invariant latent space. Our core contribution is a learnable flattening of skeletal graphs that captures both local dependencies and global structure. Unlike the standard transformer architecture, which adds positional information to token content, we integrate graph-based positional encodings multiplicatively, a design choice that follows directly from our flattening formulation. The resulting model handles diverse skeletal topologies within a single unified architecture and trains in a fully unsupervised manner, requiring no paired retargeting data. Ablation studies show, that the graph encodings, multiplicative formulation, and Transformer backbone is critical for the performance. In zero-shot evaluations, our method reduces global joint position error by $43-47\%$ over current benchmarks. A user study ($n = 37$), including expert animators, further ranks our approach highest in motion alignment and physical plausibility ($p < 0.05$). These results demonstrate that our model design is key to making transformer architectures effective for motion retargeting, outperforming existing approaches.

---


### 58. [C-LISTEN: Cognitive Load Impacts of Sensory-Triggered Environmental Navigation in Virtual Reality](https://arxiv.org/abs/2609.38589)

**<font color=#1a73e8>作者：</font>** Md. Monowar Hossain, M. Rasel Mahmud  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Nowadays, Virtual Reality (VR) systems are more helpful for making decisions, training, and rehabilitation. Multimodal settings in these systems impose a significant balance and cognitive difficulties. Additionally, decreased performance, higher cognitive load, user overwhelm, and limited accessibility of VR technology can be caused by excessive auditory, visual, and sensory stimulation. In our pilot study, we examine the strategic design of directional auditory cues to improve cognitive load and enhance user experience in virtual environments. This research also enhances fundamental knowledge that auditory feedback reduces cognitive load in VR, with statistical analysis confirming this improvement (p = .0011). This study investigates how postural balance and pupil diameter correlate with cognitive load while the users navigate. Moreover, this study provides realistic overview design guidelines for accessibility, which will make VR experiences safer and more useful for everyone, including people with cognitive impairments.

---


### 59. [Restoring without Forgetting: Filter-Level Continual Image Restoration via Parameter-Space Integrated Gradients](https://arxiv.org/abs/2609.38591)

**<font color=#1a73e8>作者：</font>** Xin Feng, Jin Zhao, Yizhen Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting image restoration models to a stream of new tasks without revisiting past data remains challenging due to catastrophic forgetting. In this work, we propose Restoring without Forgetting (RwF), a filter-level continual adaptation framework for image restoration built upon a critical observation: task-specific knowledge is centered in a small subset of filters and can be separated from those reconstructing general content. RwF first performs parameter-space integrated gradients attribution to localize degradation-critical filters in a coarse-to-fine manner. It then adapts to new tasks by generating task-specific filters from a filter bank using compact factorized low-rank transformations, further augmented with cross-task attention and prototypical contrastive learning, and lastly assembles them back only at localized positions. Experiments on six restoration tasks show that RwF effectively avoids forgetting and achieves competitive restoration quality against all-in-one methods that have full data access, and outperforms LoRA-style adaptation with $\sim$10$\times$ fewer additional parameters. Code is available at this https URL.

---


### 60. [StereoGaussians: Feed-Forward 3D Gaussian Splatting from Stereo Images](https://arxiv.org/abs/2609.38592)

**<font color=#1a73e8>作者：</font>** Boyuan Tian, Huangying Zhan, Zhan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) enables reconstruction without per- scene optimisation, but practical stereo-camera applications require nearby-view extrapolation beyond the input views. Stereo depth anchors visible surfaces, yet rendering newly exposed regions also requires learned appearance and additional scene capacity. We introduce StereoGaussians, which predicts a metric 3DGS representation from a single calibrated stereo pair. It reuses intermediate repre- sentations from frozen pretrained stereo networks to predict Gaussian attributes, while calibrated disparity anchors the geometry. A second Gaussian layer and an expanded image canvas provide capacity for disoccluded and outside-field-of- view content. For training, we construct SceneSplat-Stereo from quality-filtered 3DGS teachers, pairing stereo inputs with nearby target views across 803 training scenes. Experiments on unseen real and photorealistic stereo benchmarks demon- strate improvements over strong view-synthesis baselines, while ablation studies support our main design choices.

---


### 61. [PixelUMM: Encoder-Free Unified Image and Video Understanding and Generation](https://arxiv.org/abs/2609.38597)

**<font color=#1a73e8>作者：</font>** Cong Wei, Xuanchi Ren, Bryan Chu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified Multimodal Models (UMMs) often rely on separate visual representations for understanding and generation, increasing visual context length and complicating integration with established vision-language pretraining pipelines. Recent advances in pixel-space modeling offer an encoder-free alternative, but extending this paradigm from images to videos is non-trivial: video understanding and generation adopt different temporal representations, leaving the design of a unified visual interface an open question. We present PixelUMM, an encoder-free model for unified image and video understanding and generation directly in pixel space. PixelUMM represents images as spatial patches and videos as spatiotemporal tubelets, connecting raw pixels to a shared multimodal backbone through single-layer linear projections. Its Mixture-of-Transformers architecture combines shared attention with task-specific parameters and extends clean-pixel prediction to video generation, jointly supporting autoregressive text prediction and pixel-space flow matching. Experiments show that PixelUMM achieves competitive performance across image and video understanding and generation tasks. We further conduct empirical studies of key design choices, including decoder design and spatial-temporal patch size, providing insights for future pixel-space unified multimodal models.

---


### 62. [Reinforcement Learning with Complex (valued) Memories](https://arxiv.org/abs/2609.38598)

**<font color=#1a73e8>作者：</font>** Sathya Kamesh Bhethanabhotla, Efstratios Gavves, André Biedenkapp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partially observable environments pose a fundamental challenge in deep reinforcement learning, requiring agents to compress temporal information from observations and maintain a memory to make effective decisions. While there exist many approaches ranging from gated recurrence to attention mechanisms and model-based RL, the search for effective representational techniques that can capture long-term dependencies remains an active area of research. In this work we revisit Unitary recurrent networks (uRNNs) [Arjovsky et al., 2016, Jing et al., 2017], that demonstrated superior gradient flow and associative recall, expressing the recurrence and the hidden state in a complex vector space. Their norm preserving unitary dynamics enable information propagation through long sequences. To this end, we propose three different versions of uRNNs as drop-in replacements for recurrent PPO architectures, and demonstrate that the simple recurrence and the added degree of freedom from the phase of the complex representations enable significant gains over baselines on several memory-improvable tasks, including continuous control. We further explore how to preserve the phase information of the complex hidden state for a phase-aware policy by drawing a parallel to how quantum states are measured. With our methods reaching up to 2-3 $\times$ the reward in environments like rocksample and Craftax compared to the baselines, this work points towards an exciting new direction of representations for RL and the problem of partial observability. Code is available at: this https URL

---


### 63. [SecureVibe: Making Vibe Coding More Secure](https://arxiv.org/abs/2609.38606)

**<font color=#1a73e8>作者：</font>** Danqing Wang, Baolin Peng, Zhepei Wei 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As vibe coding becomes increasingly capable and widespread, security vulnerabilities in even functionally correct solutions are a growing concern. When investigating functionally correct but insecure solutions, we find that the insecure agent is less than half as likely to conduct effective planning and testing for the hidden security risks behind the functional requirements. Motivated by this, we develop SECUREVIBE, a training recipe that explicitly targets planning and testing for code security. SECUREVIBE constructs training signals around these security behaviors. It includes supervised fine-tuning on the security suite with 4 security tasks, and post-training methods, SECUREVIBE_rl and SECUREVIBE_hg, to enhance security capabilities from verifiable execution feedback and hint-based self-supervision. Our SECUREVIBE outperforms the baseline on two types of security coding tasks across 4 benchmarks. Specifically, SECUREVIBE improves the security pass@1 by 6.9 points on BaxBench. The gains extend to unseen CWE categories, with improvements of 11.5 points on SusVibes. Meanwhile, it also improves functionality pass@1 by 13.6 points on the security coding task SusVibes and 4.1 points on the generic coding task SWE-bench Verified. Further analysis offers two practical insights: (i) diversifying supervision across security planning, coding, and testing strengthens security behaviors more effectively than adding coding trajectories alone, and (ii) hint-guided supervision is particularly valuable when the agent's existing security capabilities are insufficient to learn effectively from outcome feedback.

---


### 64. [Learning-Enabled Estimation: Tight Characterizations under Sample Selection Biases](https://arxiv.org/abs/2609.38608)

**<font color=#1a73e8>作者：</font>** Vikram Kher, Jane H. Lee, Anay Mehrotra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When can we learn from biased samples? We study regression when outcomes are observed only after passing through selection filters that depend on both covariates and outcomes themselves, a ubiquitous challenge spanning clinical trials with patient dropout, labor markets with self-selection, and auctions with strategic entry. Ignoring such selection yields systematically biased conclusions with real-world consequences. This challenge has a long history in econometrics and statistics, starting with Heckman's seminal two-stage model and followed by numerous generalizations. While these works provide various sufficient conditions for identification, a complete characterization of when such regression is possible has remained elusive.
In this work, we provide a characterization for when regression is possible in the presence of sample selection bias. Our results establish the minimal assumptions required on the functional forms of selection processes under which regression remains possible, which are particularly relevant in modern settings where selection mechanisms are increasingly complex and opaque. As a corollary of our characterization, we show that there are settings where the regression function can be identified even when the selection filter itself cannot. This observation already goes beyond the ``estimate selection filter, then debias regression'' paradigm that is followed by virtually all existing approaches. Under natural strengthenings of our identification conditions, we also establish finite-sample estimation guarantees with explicit convergence rates and provide oracle-efficient algorithms. This yields the first general-purpose estimation method for this broad class of selection problems. Finally, we explore the implications of our results for several well-studied econometric settings with complex selection mechanisms such as auctions with entry costs and labor markets.

---


### 65. [Exo2EgoHOI: Hand-Object-Interaction Aware Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2609.38615)

**<font color=#1a73e8>作者：</font>** Hongjia Zhai, Xiyu Zhang, Haoran Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric videos of human manipulation provide valuable visual experience for embodied intelligence, yet collecting such data at scale is costly. Exocentric-to-egocentric video generation offers a scalable alternative by transforming abundant third-person manipulation videos into first-person observations. However, existing methods often struggle to faithfully preserve demonstrated hand-object interactions (HOI) across large viewpoint changes due to insufficient fine-grained interaction guidance and weak object-centric anchoring. We present Exo2EgoHOI, an HOI-aware video generative framework for interaction-preserving exocentric-to-egocentric translation. To preserve fine-grained HOI, we introduce a unified 4D HOI prior that combines scene geometry, articulated hand renderings, and dense hand-object relation fields, together with a dual-branch residual adapter for injecting structural and relational cues into the video generation backbone. To preserve object consistency, we introduce Decomposed Gated Cross-Attention, which separately encodes object and background references and adaptively integrates global semantic and local appearance features as object-centric anchors. Experiments on ARCTIC-HOI and Ego-Exo4D demonstrate substantial improvements in object consistency and HOI preservation while maintaining competitive visual fidelity. In particular, on ARCTIC-HOI, Exo2EgoHOI improves object mIoU by 32.3% and reduces MPJPE and PA-MPJPE by 34.7% and 50.0%, respectively, relative to the respective best baseline results. Project page: this https URL.

---


### 66. [Differentiable Structure Learning for Cyclic Linear Gaussian Models with Latent Confounders](https://arxiv.org/abs/2609.38618)

**<font color=#1a73e8>作者：</font>** Sadegh Khorasani, Ali Najar, Saber Salehkaleybar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study causal structure learning from observational data in linear Gaussian structural causal models in the presence of directed cycles and an unknown number of exogenous latent confounders, bounded by a given maximum. We derive the covariance of the observed variables and introduce marginal quasi-equivalence, which characterizes when different causal models share a full-dimensional subset of the observational distributions they can generate. We formulate structure learning as minimization of the Gaussian negative log-likelihood with a logarithmically scaled complexity penalty that counts directed edges and latent variables. For a fixed number of observed variables and a fixed upper bound on latent variables, we establish consistency of global score minimizers up to marginal quasi-equivalence under algebraic faithfulness, structural minimality, and model-overlap assumptions. We parameterize the inclusion of directed edges and candidate latent variables using Bernoulli gates, whose continuous probabilities are optimized jointly with the structural coefficients. Averaging the penalized negative log-likelihood over these gates yields an objective with a closed-form differentiable complexity penalty. We prove that this expected objective has the same global infimum as the corresponding discrete structure-learning objective. Experimental results show that our approach achieves lower recovery error than previous methods in several experimental settings.

---


### 67. [HIGS: Hierarchical Implicit Grids for Joint Geometric and Semantic Scene Understanding](https://arxiv.org/abs/2609.38620)

**<font color=#1a73e8>作者：</font>** Hanwen Cao, Wenqiang Wu, Kuang-Ting Tu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural implicit representations have had a significant impact on scene reconstruction by enabling robots to build continuous, differentiable, and high-fidelity 3D maps. Most existing works focus on geometric reconstruction and lack semantic information for high-level spatial understanding and task planning. Also, as the scale and complexity of the environment increase, neural representations face the challenge of maintaining computational efficiency in back-end optimization. To resolve these two challenges, we introduce a hierarchical neural field that leverages multiresolution submaps to achieve an efficient and scalable implicit representation, and a unified query and decoding mechanism to support both geometric and semantic features. More specifically, the learnable map features can be converted to the output with the query and decoding process for both training and inference. For large-scale representation, we decompose a scene into overlapping submaps and do hierarchical optimization within each local submap, thus enabling scalable computation. To further improve efficiency, we design feature encoders that predict initial hierarchical grid features to substantially reduce the time needed to optimize the submap features from scratch. To correct estimation drift among submaps, we align and fuse them entirely within the implicit feature space, leading to substantial acceleration by avoiding the need to decode the final output. Building upon this efficient hierarchical representation, we embed both geometric features and vision-language latent features into the map, and demonstrate it on both Signed Distance Field (SDF) construction and open-vocabulary object grounding. Our approach significantly improves computation and memory efficiency, maintains high estimation accuracy, and endows the robot with spatial awareness on large-scale real-world benchmarks.

---


### 68. [Eulerian Motion Reconstruction for Water Scenery](https://arxiv.org/abs/2609.38622)

**<font color=#1a73e8>作者：</font>** Chuhan Chen, Yen-Chi Cheng, Ayush Saraf 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing and animating water scenery from nature produces compelling and immersive visual experiences. Previous work examined this task from the perspective of 2D video textures, with the goal of creating a looping video. In our work, we tackle the problem from a 3D perspective, creating a looping 4D dynamic reconstruction which can be interactively rendered from novel viewpoints from a single non-looping 2D source video. We represent motion as a 3D static \textit{Eulerian} motion field that advects canonical Gaussian splats that are cyclically reborn at fixed time periods, supervised using rendering losses. To model non-periodic and stochastic dynamics present in real-world scenes, we add a non-periodic, time-varying residual term to capture deviations from the static Eulerian motion field. We show quantitatively and qualitatively that our framework enables photorealistic animation of water scenes better than prior art.

---


### 69. [Geometry-physics confounding impairs PDE learning across varying domains](https://arxiv.org/abs/2609.38623)

**<font color=#1a73e8>作者：</font>** Yinghao Cheng, Gengxiang Chen, Xu Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning partial differential equation (PDE) dynamics across varying domains is central to predictive modelling and data-driven discovery of governing equations. However, geometric variation alters both field representation and the governing differential operators, confounding geometric effects with intrinsic physical properties in the observed dynamics. This work identifies geometry-physics confounding as a unified failure mechanism for PDE learning across varying domains. In forward operator learning, this confounding increases the burden of inferring geometry-dependent operator changes from finite data, reducing data efficiency and generalisation. In equation discovery, omitting geometry-induced operators misspecifies the candidate library, leading to biased parameters, missed governing terms and spurious terms. We propose a de-confounding framework that makes the known geometry-to-operator transformation explicit. Geometry-induced coefficient fields improve prediction and data efficiency across five operator-learning benchmarks, while geometry-complete candidate libraries recover the generating equations and reduce held-out PDE residuals by more than two orders of magnitude in both evolving-domain systems. By separating known geometric action from intrinsic physics, the proposed framework supports more reliable and data-efficient PDE learning across scientific and engineering problems with varying geometries.

---


### 70. [Interpretable but Fragile? Robustness of Concept Bottlenecks under Geometric-Semantic Perturbations](https://arxiv.org/abs/2609.38625)

**<font color=#1a73e8>作者：</font>** Hanwei Zhang, Tianma Hu, Gaojie Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs) are designed to provide interpretable intermediate representations, yet how such bottlenecks affect robustness remains unclear, with existing studies reporting mixed and sometimes contradictory findings. We argue that these discrepancies arise from conflating different robustness notions and perturbation regimes, rather than from fundamental disagreements about CBMs themselves. To disentangle these factors, we introduce a generator-based evaluation framework that enables controlled comparisons between standard classifiers and CBMs under two distinct perturbation types: continuous geometric perturbations in latent space and discrete semantic interventions in concept space. Within this framework, we evaluate robustness both empirically, via prediction and concept-level sensitivity metrics, and certifiably, using randomized smoothing in latent and concept spaces. Across experiments, we reconcile previously conflicting findings by clarifying when, and in what sense, concept bottlenecks do or do not improve robustness. By further analyzing robustness under varying task conditions, including class semantic similarity and concept vocabulary size, we show that interpretability does not inherently confer robustness. Instead, concept bottlenecks shift where and how sensitivity manifests, revealing a nuanced interpretability robustness trade off that depends critically on the perturbation regime and task structure. Together, our results show that interpretability and robustness are distinct objectives: interpretable intermediate representations do not uniformly improve robustness, but instead redistribute sensitivity across perturbation spaces and model families.

---


### 71. [Marking Contour Tones in Yorùbá](https://arxiv.org/abs/2609.38627)

**<font color=#1a73e8>作者：</font>** Kólá Túbòsún  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Yorùbá is a tonal language in which contour tones pose persistent orthographic challenges. These are especially notable for personal names and lexical items whose conventional spellings avoid vowel lengthening that would otherwise provide a host syllable for the second tone. A particular concern is a class of names in which the conventional spelling does not just omit tonal information but inverts the meaning of said name, sometimes asserting the opposite of what the name intends. This paper describes the problem, illustrates the inadequacy of current solutions, and proposes the adoption of the caron and circumflex marks. These are symbols with precedent in Yorùbá phonological scholarship since Olmsted (1951), used as orthographic conventions on single vowels to encode rising and falling contour tones, making them accessible for the first time through standard keyboard input and computational text processing. The proposal is supported by an implementation in the WriteYoruba keyboard and the TTSYoruba speech synthesizer, whose architecture and listener evaluation are reported separately (Tubosun et al., 2026).

---


### 72. [Proper Scoring Rule-based Diffusion for Probabilistic Weather Forecasting](https://arxiv.org/abs/2609.38632)

**<font color=#1a73e8>作者：</font>** Joonhyeong Park, Giung Nam, Hyungi Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent probabilistic weather forecasters train stochastic predictors with the continuous ranked probability score (CRPS) to generate each ensemble member in a single forward pass. These models learn the predictive distribution from the forecast context alone, which becomes difficult at longer forecast horizons where uncertainty is high. To learn the predictive distribution more effectively, we introduce auxiliary conditional denoising tasks that predict the same future state from the context and its corrupted version, which provides partial future information that can reduce prediction ambiguity. Building on distributional diffusion models, we learn the conditional distributions of these tasks with a single stochastic predictor by minimizing a proper scoring rule across noise levels. At inference, the predictor can still generate each ensemble member in a single forward pass at the fully corrupted endpoint. Standard CRPS training is recovered as the endpoint-only special case of our formulation, so our framework extends existing CRPS-based forecasters with only additional conditioning inputs. Controlled experiments show that the auxiliary tasks improve one-step forecasting across architectures, with larger gains at longer forecast horizons. The gains extend to high-dimensional global weather forecasting under both training from scratch and fine-tuning, along with improved calibration and potential benefits for generalization under distribution shift.

---


### 73. [STEPS: Scene Text Editing with Preserved Style Using Diffusion and Contrastive Style Encoding](https://arxiv.org/abs/2609.38636)

**<font color=#1a73e8>作者：</font>** Nicolas Thiebaut, Nameer Hirschkind, Xiao Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Scene Text Editing with Preserved Style (STEPS), a novel diffusion model architecture for quality text replacement in images. Scene Text Editing (STE), also known as Visual Text Editing, consists of changing the textual content in an image while conserving the original style, e.g. font, colors, orientation, background, etc. STEPS advances the state of the art in STE through directed focus on improved style preservation. We introduce a style encoder for visual text that captures style independently of textual content, and a model architecture that combines the style encoder with multiple semantic conditions (target text characters encoding and rendered glyphs). STEPS achieves superior results to previous STE methods in style preservation, output readability, and subjective quality.

---


### 74. [Template-Search Domain Adaptation via Multi-Stage Feature Alignment for Cross-Modal Object Tracking](https://arxiv.org/abs/2609.38637)

**<font color=#1a73e8>作者：</font>** Fereshteh Aghaee Meibodi, Amir Mehdi Soufi Enayati, Shadi Alijani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual object tracking typically assumes that the initial template and subsequent search frames share the same sensing modality. In practice, sensor availability or operation may change over time, creating a substantial representation gap between template and search frames. Unlike conventional multi-modal tracking where paired modalities are simultaneously available, cross-modal tracking requires localization when template and search frames originate from different active modalities. Accordingly, we introduce TSDA-Track, a Template-Search Domain Adaptation framework to reduce modality discrepancy during training. We investigate two feature alignment strategies. Pre-AFA TSDA-Track applies adversarial alignment before transformer's template-search interaction to suppress modality-specific bias. Enc-CFA TSDA-Track applies contrastive alignment to encoder representations after interaction to strengthen target-level cross-modal correspondence. Both variants retain a shared inference pipeline without modality-specific branches. Experiments on LasHeR, and zero-shot evaluations on RGBT234 and GTOT under multiple cross-modal protocols demonstrate improvements over representative state-of-the-art trackers. For instance, under the modality-switch protocol on RGBT234, Pre-AFA TSDA-Track achieves an SR/PR of 43.2/56.0, compared with 36.8/50.0 for ToMP-101 baseline. In addition, a study on Anti-UAV-024 further verifies the applicability of TSDA-Track to aerial tracking. Our study highlights the effectiveness of feature alignment domain adaptation for cross-modal tracking.

---


### 75. [ChartRevise: A Dataset and Evaluation Protocol for Exact Chart Editing via Code](https://arxiv.org/abs/2609.38642)

**<font color=#1a73e8>作者：</font>** Jiaxiang Tang, Yi Zhou, Chad DeLuca 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chart editing requires cross-modal edit grounding, realizing a requested visual change in the code that draws it, with necessary related updates and without altering unrelated content. Existing benchmarks emphasize either code executability or chart quality, but their metrics do not clearly distinguish request completion from missed coupled updates and gratuitous changes. We introduce ChartRevise, a structured dataset and evaluation protocol for exact program-grounded chart editing. For dataset construction, we build on the grammar of graphics to systematically cover chart-editing operations, using source-program checks to verify their applicability across chart types and libraries. To improve edit exactness, our pipeline checks individual requirements and guides repair or exclusion when they are unmet. The resulting dataset contains 92,438 records covering 344 edit types across 20 chart types and three plotting libraries. For evaluation, our reference-free protocol separately measures atomic requirement completion, identifies gratuitous changes, and detects missed coupled updates. These checks are combined with successful execution and rendering to determine exact-edit success. Across five models and four external benchmarks, fine-tuning yields relative gains of 16\% in mean requirement recall and 22\% in mean exact-edit rate.

---


### 76. [Recursive Organization Improvement: A Modeling Specification for Human--Agent Organizations](https://arxiv.org/abs/2609.38643)

**<font color=#1a73e8>作者：</font>** Zilong Wang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Stronger AI agents do not automatically produce better organizations: teams must also learn which work arrangements to retain and when to reconsider them. We propose a modeling specification for recursive organization improvement and evaluate it through an executable checker, a public-record mapping, and controlled simulation. The specification connects actor-visible histories, organizational memory, decision rights, and evidence-carrying change contracts. The mechanism study crosses six decision rules, three memory conditions, and three task environments under fixed resource ceilings. In a stationary environment, cumulative evidence raises balanced evaluation's normalized net value per task from 0.45224 to 0.48007. Repeated reassessment's disadvantage relative to this comparator falls from 0.01702 with reset evidence to 0.00007 with cumulative evidence. A reversal of the best workflow reveals the opposite cost: indefinite retention delays adaptation, while a finite window restores eventual performance at a transition cost. In exploratory controls, matching trial acquisition and label reuse reduces the apparent reassessment gain from 0.00607 to 0.00191. Program replacement adds no stable benefit across the tested reversal times. The study identifies evidence acquisition, reuse, and timely updating as mechanisms that must be separated from evaluator replacement when assessing organizational improvement.

---


### 77. [Z-Sigil: A Public-Key Cryptosystem with Chained Selection over a Fiber Bundle of Module-Lattice Keys](https://arxiv.org/abs/2609.38668)

**<font color=#1a73e8>作者：</font>** Andrea Rondelli  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Z-Sigil is a public-key cryptosystem in which the plaintext selects successive keys from a fixed module-lattice family. Messages are length-prefixed, zero-padded and divided into 32-byte blocks. Each public vector is a shared public matrix applied to a small secret vector, plus a small error.
Key indices label torsion points of a flat Kähler torus; the secret family forms a section of a key bundle over them. A public nonce initializes a hash state that selects each block's key and bit mask. The sender updates the state with the plaintext block; the receiver does so after recovering it. The stream and nonce determine a discrete walk along which decryption reads the secret section.
We specify the algorithms, prove correctness under an explicit noise condition and bound decoding failure for messages chosen after the public key. Under stated decisional Module-LWE assumptions, we establish IND-CPA confidentiality for the chain without modelling the state hash as a random oracle. The reduction covers quantum adversaries under quantum hardness assumptions, with classical keys, messages and ciphertexts; no concrete security level is established.
With independent uniform selectors, a restricted direct-decryption model quantifies reduced fragment recovery under partial key exposure, without improving full-message recovery probability over an independent-block baseline. Known-plaintext and candidate-message attacks, and parallel candidate-table decryption, delimit this result. Neither a universal sequential lower bound nor authentication or chosen-ciphertext security is established.
Replacing an earlier scalar-exposing proposal, we give an augmented-lattice interpretation, integral-transport obstructions and a noise budget for research on curved, nontrivial bundles. A byte-level specification, pseudocode, test vectors and numerical checks support verification.

---


### 78. [Where Scientific Search Agents Fail: Decision-Checkpoint Auditing of Exposure and Inspection Attempts](https://arxiv.org/abs/2609.38670)

**<font color=#1a73e8>作者：</font>** Hongmin Li, Wanli Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Final-answer accuracy does not reveal whether a scientific-search agent failed to encounter a target paper, attempt to inspect it, or return an accepted answer after inspection. We introduce decision checkpoints that record observations and tool actions without benchmark labels during inference, then join target identities and evaluator labels to assign outcome categories from recorded events. Across five conditions on 540 answerable AutoResearchBench Deep questions in a fixed, target-enriched environment, keyword search achieves 24.6\% accuracy, compared with 17.8\% for raw search. The keyword condition has fewer incorrect answers with neither target exposure nor inspection, but more incorrect answers after the target is exposed and left uninspected. Compared with keyword search, read-first has 27.4\% more recorded evidence-search calls. Target inspection attempts occur on 199 questions under read-first and 191 under keyword search; both conditions achieve 24.6\% accuracy. The checkpoint protocol makes these question-level differences explicit, distinguishing target exposure and inspection from aggregate accuracy and total tool use.

---


### 79. [In-Distribution Imagination for Model-Based Offline Reinforcement Learning](https://arxiv.org/abs/2609.38673)

**<font color=#1a73e8>作者：</font>** Mintae Kim, Koushil Sreenath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based offline reinforcement learning (MBORL) improves sample efficiency through model-generated trajectories. However, accumulative model error can drive imagined trajectories outside the offline data distribution, leading to unrealistic synthetic data and unstable policy optimization. Many existing methods primarily control rollouts using transition-level uncertainty. We propose \emph{in-distribution imagination} (IDI), a rollout control framework that estimates trajectory support in a learned representation space and adaptively truncates rollouts that leave the offline trajectory manifold. Combined with trajectory-regularized RL, an extension of entropy-regularized RL, IDI consistently improves performance in limited-data settings. Experiments show that trajectory support predicts rollout failure substantially better than transition-level uncertainty, highlighting the importance of trajectory-level rollout control in MBORL.

---


### 80. [ReGain: Restoring Subject Fidelity in Personalization on Synthetic Images](https://arxiv.org/abs/2609.38680)

**<font color=#1a73e8>作者：</font>** Shubhang Bhatnagar, Ishan Bhatnagar, Viraj Shah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models are personalized to a subject by DreamBooth fine-tuning on a handful of its images. Increasingly, these images come from a diffusion model rather than a camera. We show that fine-tuning on such synthetic images degrades subject fidelity, producing oversaturated color and excess high-frequency detail. To isolate the cause, we fine-tune two models from the same base model with the same DreamBooth recipe, one on real photos of a subject and one on synthetic images of that subject generated by the first. We trace the degradation to classifier-free guidance (CFG). For the model personalized on synthetic images, the angle between the conditional and unconditional noise predictions, and with it the norm of their difference, is much larger than for the model personalized on real photos. This inflation grows toward high frequencies and also appears at other prompts semantically close to the subject, such as its class noun, but not at unrelated ones. We propose ReGain, a training-free correction applied at sampling time that measures how much each frequency band of the guidance is inflated relative to the base model and scales that band down accordingly. ReGain needs no real photos. On Stable Diffusion v1.5, ReGain closes 51-64% of the subject-fidelity gap to the model personalized on real photos, as measured by DINO, DINOv2 and CLIP-I. It also improves subject fidelity on SDXL and SD 3.5 and preserves text alignment on all three backbones.

---


### 81. [Unveiling the Value of Motion for Cinematic Camera Trajectories](https://arxiv.org/abs/2609.38683)

**<font color=#1a73e8>作者：</font>** Ziqi Zhou, Yujian Yuan, Laura Sevilla-Lara  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cinematic camera motion is a fundamental storytelling tool, defined not only by where the camera is positioned in the scene, but also by how it moves in terms of direction and speed. Recent work on camera trajectory generation and alignment to text relies on pose-centric representations. While in principle a network could derive direction of movement and speed, we find that in practice this might not happen. In fact, in this paper we discover that decomposing the camera trajectory representation from the traditional per-frame poses to direction and speed has surprising benefits across multiple tasks, including trajectory-to-text alignment as well as text-to-trajectory generation. To accurately evaluate the former, we introduce a simple and reliable protocol that overcomes the limitations of prior evaluation baselines. For the latter, building on this representational insight, we propose a novel generative model for camera trajectories, CineGEN, that achieves superior performance across a variety of metrics. We also propose a novel dataset, CineScript, containing movie clips that are enriched with scene descriptions as well as higher-level metadata. This novel data allows us to test models' ability to capture high-level cinematographic information. We show that, despite its simplicity, representing camera trajectories through direction and speed not only helps numerically to achieve better alignment and generation, but also inherently encodes complex directorial intent.

---


### 82. [GATE-ST: Gene-Aware Text-image Encoder for Spatial Transcriptomics](https://arxiv.org/abs/2609.38690)

**<font color=#1a73e8>作者：</font>** Lucas Ni, Jian Luo, Wentao Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics enables spatially resolved gene expression analysis from slide-level images while preserving morphological features, providing valuable information for studying disease mechanisms and developing treatments. However, spatial gene expression profiling typically requires expensive and time-consuming tests. While existing image-based prediction optimizations mostly revolve around including positional embeddings and further image-based changes, text-based optimizations remain relatively unexplored. We present GATE-ST, which incorporates text-based inputs into image-based spatial gene expression predictions. With this approach, generated text descriptions of genes are utilized to better spatial transcriptomics prediction results. Gene summaries are put through a text encoder, generating embeddings that integrate with image embeddings through cross-attention layers to align with morphological features. We demonstrate the effectiveness of such text inputs by benchmarking performance against random gene embeddings and multiple other image-text fusion architectures, and show that GATE-ST outperforms these alternatives. Our results demonstrate the effectiveness of GATE-ST in pathology imaging, which may greatly reduce the time and cost of accurate spatial transcriptomic predictions, proving the potential of text-guided spatial gene expression prediction.

---


### 83. [No Corners Cut: State-Grounded Transitions for Mid-Stream Prompt Switches in Video Generation](https://arxiv.org/abs/2609.38691)

**<font color=#1a73e8>作者：</font>** Zejing Rao, Ketong Ren, Xiaoqiang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video generators allow users to dynamically modulate video synthesis via mid-stream prompt switching. Existing streaming methods can respond to the updated instruction while still cutting corners, prematurely realizing goals or taking heuristic shortcuts that bypass necessary intermediate state changes needed for a plausible transition. In this study, we present SEGUE, a novel framework that makes this process explicit and trains the generator to execute these transitions faithfully. At each switch, a training-free planner parses the latest frame and prompts, writes a few segue prompts with roles and durations, and then hands control back to the user's prompt. Furthermore, to address the inherent difficulty of training causal models on short-lived temporal schedules without corrupting preparatory supervision, we introduce SPANDMD, which evaluates each active prompt using the full rollout as temporal context while retaining its DMD residual only within the prompt's assigned span. On OpenTrans-360, a benchmark of 1,800 switches that scores how the old state exits and the new one begins, SEGUE ranks first on all eight transition metrics and raises the overall score over the strongest baseline from 0.866 to 0.887. It also ranks first on four of six instruction-response metrics of StreamAV-Bench, while the planner transfers to frozen autoregressive generators without retraining.

---


### 84. [Budget Boundary Effects in Test-Time Mathematical Reasoning](https://arxiv.org/abs/2609.38699)

**<font color=#1a73e8>作者：</font>** Guilin Zhang, Ziqi Tan, Wulan Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A cumulative token cap can fall inside a mathematical derivation, forcing a test-time controller to choose between stopping at the cap (strict) and allowing the current attempt to finish (advisory). We measure this boundary choice with paired offline replays of 19,200 public traces: 120 AIME, BrUMO and HMMT problems and two archive configurations of one model. Candidate order and a 16-attempt cap are fixed, and answer selection is blind to reference answers and correctness labels. Three findings emerge. First, at the 4k cap, most advisory accuracy gains replace abstention with a correct answer; strict stopping pays for an unfinished prefix that the completed-only selector cannot use. Second, comparisons along realized cost differ from same-cap comparisons: advisory 4k in low has higher accuracy than strict 8k at comparable mean completion cost, while in high its observed accuracy is 0.42 points below strict 32k using 59% of its mean tokens. These aggregate comparisons do not establish equal-compute superiority or accuracy equivalence. Third, increased candidate coverage does not guarantee higher answer accuracy: a log-probability selector loses accuracy while coverage rises, including after a source-grade consistency repair. Same-cap majority-accuracy differences shrink below 1.3 percentage points at 32k. Budget curves should jointly state the cap, realized cost, eligible candidates, stopping rule and selector information.

---


### 85. [SCALE: Synthetic Calibration via Agreement Labeling in Embedding Space](https://arxiv.org/abs/2609.38705)

**<font color=#1a73e8>作者：</font>** Wenjun Liu, Saeed Hassanpour  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models for computational pathology are usually evaluated using AUC and accuracy, while calibration is often left untested. This matters because a model can be accurate on average but still assign overly confident probabilities to cases that are difficult even for pathologists. We study calibration across eight pathology foundation models. Using pathologist agreement as a measure of diagnostic difficulty, we find that calibration error is consistently higher on low-agreement cases than on high-agreement cases. This pattern is not apparent from aggregate expected calibration error (ECE) alone. We then propose synthetic agreement calibration, a method for improving calibration without collecting multi-annotator labels. Given a trained linear probe, we select high-confidence embeddings as class anchors and interpolate between anchors from opposite classes. The interpolation weights encode a continuous notion of diagnostic ambiguity, which we use as a synthetic agreement signal to retrain the probe with agreement-aware label smoothing. On MHIST, which includes annotations from seven pathologists, synthetic agreement calibration recovers most of the calibration improvement obtained by label smoothing based on real pathologist agreement, while substantially reducing low-agreement ECE relative to the uncalibrated baseline. Discrimination metrics are preserved. On PatchCamelyon and BreakHis, public histopathology datasets without multi-annotator labels, the method improves calibration across the evaluated foundation models, whereas annotator-dependent approaches cannot be used without additional expert annotation.

---


### 86. [Hard-Region Supervision: #1 on the Waymo Open Dataset 2D Video Panoptic Segmentation Leaderboard](https://arxiv.org/abs/2609.38714)

**<font color=#1a73e8>作者：</font>** Jinghan Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe our winning entry to the Waymo Open Dataset 2D Video Panoptic Segmentation Challenge. The task asks for a semantic class at every pixel of every frame and, for countable objects, an identity that holds across 100 frames and across five overlapping cameras. We build on DVIS++, a cascade of a segmenter, a tracker, and a refiner, as our baseline. We propose hard region supervision (HRS) to improve the baseline. In particular, we use the baseline to define the hard region as where it makes mistakes, and design a loss and an auxiliary prediction head for this region. The auxiliary head is used only in training and removed at test time, so at inference the model trained with HRS has the same architecture as the baseline. In addition, we propose three test-time steps that further improve the results: a two-model ensemble, a merge of the segmenter's output into the final panoptic map, and cross-camera identity linking. On the challenge test set, our entry reaches 0.3547 wSTQ, 0.2071 wAQ, and 0.6075 mIoU, ranking first on all three metrics. It is 3.6 wSTQ points ahead of the second entry and 2.4 points ahead of our DVIS++ baseline.

---


### 87. [Matisse: Evidence-Space Reasoning for Active 3D Reconstruction](https://arxiv.org/abs/2609.38746)

**<font color=#1a73e8>作者：</font>** Xihang Yu, Kaichen Zhou, Lorenzo Shaikewitz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How can a 3D reconstruction system acquire and retain useful information to understand the geometry of a scene from partial views under a limited computation budget? Existing active view acquisition methods typically estimate uncertainty over observed or instantiated geometry, limiting their ability to reason about unseen structure, while long-horizon reconstruction methods often retain redundant observations. We introduce Matisse, a training-free framework that unifies active reconstruction and keyframe selection by leveraging evidence provided by a pretrained generative 3D model. Matisse estimates Evidential Uncertainty from cross-attention evidence associated with 3D latent tokens and derives an Evidential Information Gain to guide both view acquisition and keyframe selection based on the expected reduction in posterior entropy. Matisse supports multi-object scenes through occlusion-aware, object-balanced aggregation and propagates uncertainty through intermediate latents to avoid full reconstruction during planning. Matisse reduces Chamfer distance by 12.7%, 3.8%, and 9.2% on GSO30, YCB-V, and Replica, respectively, relative to the best baseline on each dataset, and achieves a $1.50\times$ end-to-end speedup over the best active reconstruction baseline on GSO30 with the same reconstruction backend. In the GSO30 keyframe selection experiment for long-horizon reconstruction, Matisse achieves comparable Chamfer distance using 14% of the input views compared with Stream3D.

---


### 88. [Consensus-Aware Multi-Source Fusion for Reference-Guided Camouflaged Object Detection](https://arxiv.org/abs/2609.38747)

**<font color=#1a73e8>作者：</font>** Junyang Xia, Luocheng Zhang, Wenwen Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-guided camouflaged object detection aims to segment a target whose visual appearance closely resembles its surroundings by exploiting auxiliary reference samples. The task remains difficult because reference samples contain inconsistent target cues, while generic visual representations are not inherently aligned with the target specified by the references. To handle these problems, we present a consensus-aware multi-source fusion framework. Reference-Conditioned Dual-Backbone Fusion (RCDF) couples trainable PVTv2 query features with frozen DINOv3 representations and uses reference-conditioned correlation to select foundation-model evidence before multi-scale fusion. The framework also aggregates multiple references through cross-reference consensus aggregation and injects reference information at semantic depths matched to the query features. Extensive experiments demonstrate the effectiveness of the proposed method. The results further show that reference consensus, target-conditioned foundation features, and hierarchical decoding provide complementary improvements under the evaluation protocol. The source code will be made publicly available upon acceptance.

---


### 89. [Here the World in Stereo: Learning Dynamic Spatial Correspondence for Immersive Joint Video-Audio Generation](https://arxiv.org/abs/2609.38748)

**<font color=#1a73e8>作者：</font>** Hanmo Chen, Chengcheng Liu, Tianxiao Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent joint video-audio generation models have achieved strong semantic correspondence and temporal synchronization. However, applications such as AR/VR and interactive gaming further require stereo audio to provide an immersive sense, which remains largely overlooked. Effective stereo audio requires the perceived sound location to evolve consistently with the motion of its corresponding visual source. We refer to this property as Dynamic Spatial Correspondence and propose StereoBind, a framework that binds visual source motion to stereo sound generation. StereoBind uses motion tracks to coordinate visual motion and stereo audio through three complementary mechanisms. Visual Motion Binding establishes source-aware audiovisual correspondence, the Spatial Track Encoder captures absolute source positions, and Residual Track RoPE models relative motion. For supervision and evaluation, we construct StereoWorld-29K, a large-scale stereo audio-video dataset with paired motion tracks, and StereoWorldBench for measuring audiovisual spatial consistency. Experiments show that StereoBind substantially improves spatial alignment in stereo audio generation over existing models while preserving overall audiovisual quality.

---


### 90. [Where the Evidence Lives: Auditing AI Companions' Self-Descriptions](https://arxiv.org/abs/2609.38753)

**<font color=#1a73e8>作者：</font>** Seiya Ikeda, Shin-nosuke Ishikawa  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Companion agents describe themselves: they remember, they understand their users, the relationship has changed them. We argue that such accounts, and the experience ratings that seem to confirm them, are checkable by users only where the evidence is theirs: in the agent's behavior, or in themselves. Where the evidence lives in the machinery, fluent self-description and moderately positive ratings do not establish that the mechanisms behind them ran. We demonstrate an audit procedure that sets an agent's self-description against its users' judgements and its implementation records, reporting each claim as supported, contradicted, or unresolved, and apply it to Lita, a proactive companion we built and deployed for a month with nine colleagues. Participants endorsed stylistic claims, withheld endorsement from relational ones, and rated memory at or above midpoint, while two of three memory layers had never executed their accumulation step. Memory-bearing agents should report what their self-descriptions cannot establish.

---


### 91. [PathAnchor: Path-Structured Evidence for Scientific Agents](https://arxiv.org/abs/2609.38766)

**<font color=#1a73e8>作者：</font>** Qiuhui Chen, Jiafan Lu, Shuaimin Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific agents can retrieve relevant passages yet still lose functional order, mix evidence across sources, or state conclusions that exceed the retrieved record. We introduce PathAnchor, a bounded scientific reasoning system built on path-structured evidence workspaces. Instead of treating passages or extracted concepts as independent units, the system retrieves source-linked Material-Sensor-Signal-System trajectories that preserve role, direction, and the evidence supporting each transition. A controller uses three read-only tools to search paper-specific trajectories, trace paths across candidate sources, and open exact evidence before producing a claim-cited answer and an explicit evidence boundary. On 120 single- and cross-paper flexible-sensor questions, PathAnchor scores 82.6% and leads six evaluated systems. Under a matched controller, corpus, and six-call budget, replacing unordered concept graphs with path-structured records raises source recall from 61.3% to 82.9%, increases answers whose claims all cite opened evidence from 69.2% to 90.0%, and reduces tool calls. These results show that evidence organization affects retrieval and citation completeness under fixed agent resources.

---


### 92. [Learning Under Forgetting: Statistical Support-Selective Retention in Stochastic Training Dynamics](https://arxiv.org/abs/2609.38768)

**<font color=#1a73e8>作者：</font>** Fujie Gao, Zuyue Zhang, Gang Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior work has shown that neural networks exhibit implicit biases toward low-complexity structure (e.g., spectral bias), memorization dynamics, and compression-like effects during training, but a unified dynamical account of selective retention remains incomplete. We propose Repeated Reinforcement with Persistent Forgetting (RPF) dynamics, a minimal framework in which repeated exposure reinforces patterns and structures that recur in the data, while persistent forgetting attenuates learned information. This view treats forgetting not merely as a failure mode, but as a selection mechanism. We build the theory in three successive layers. First, in an independent-feature model, we derive an exposure-selective survival law and a support-dependent retention boundary characterizing which patterns persist under forgetting. Second, in a shared-parameter model, we show that forgetting induces spectral filtering over covariance modes, preserving strongly supported shared components while suppressing weak ones. Third, under small-step and norm/coding approximations, we show how RPF dynamics induce an implicit trade-off between data fitting and the cost of stored information, yielding Minimum Description Length (MDL)-like compression. Controlled experiments provide evidence for this reinforcement--forgetting selection mechanism in scalar memories and a nonlinear shared network. Joint reinforcement and attenuation interventions shift conditional retention, while matched exposure counts reveal forgetting-dependent effects of reinforcement timing and changes in the composition of the retained set. Together, these results show that repeated reinforcement and persistent forgetting jointly provide a controllable source of inductive bias beyond neural architecture and scale.

---


### 93. [Distilling Diffusion Score Discrepancy for Efficient Training Data Attribution](https://arxiv.org/abs/2609.38776)

**<font color=#1a73e8>作者：</font>** Shixuan Liu, Joan Serrà, Kin Wai Cheuk 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training data attribution for diffusion models aims to identify the training samples that influence a generated instance, but existing methods either require costly per-sample gradient computation or query-specific model optimization. Moreover, most methods attribute changes in a proxy loss rather than changes in the actual model's generative behavior. We address these limitations by formulating attribution directly with a local score discrepancy measure, which applies to any diffusion variant (including DDPM, EDM, and flow matching), and by showing that such measure can be estimated without retraining, as a preconditioned gradient similarity. We instantiate this estimator as Training-data Influence via score Discrepancy (TID), which uses Kronecker-factored curvature to avoid random projections and per-sample gradient storage. We then distill TID into TIDE, a forward-only student trained online to reproduce the teacher's rankings from the diffusion model's internal activations. Under counterfactual evaluation on CIFAR-10, ArtBench-10, and MS-COCO, TID matches or outperforms state-of-the-art approaches, while TIDE retains most of TID's accuracy at four to five orders of magnitude lower per-query cost, attributing generated samples in milliseconds and faster than the generation itself.

---


### 94. [Does a Shared Temperature Imply a Shared Angular Scale in Probabilistic Contrastive Learning?](https://arxiv.org/abs/2609.38784)

**<font color=#1a73e8>作者：</font>** Ningkang Peng, Qianfeng Yu, Jingyang Mao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In probabilistic contrastive learning, a shared temperature is commonly interpreted as a shared similarity scale, but this interpretation does not hold for high-dimensional distributional class representations. We study the exact von Mises-Fisher (vMF) probabilistic score used by ProCo when representation dimension and class concentration grow jointly. We prove that the score retains a class-dependent leading angular gain $g_c=A_c/\tau$, where $A_c$ is the mean resultant length. This gain enters Softmax competition, pairwise decision boundaries, and feature gradients. On real CIFAR-LT, ImageNet-LT, and iNaturalist representations, the theory accurately predicts boundary movements and local gradient changes under the full vMF score. Classwise temperature adjustment also changes the cosine-zero intercept and finite-dimensional response. We construct intercept-preserving and Pure Angular controls to separate the leading gain from these accompanying changes. Complete gain equalization yields a shared-scale cosine prototype rule at leading order; a finite-dimensional margin condition guarantees agreement of the two classifiers. Across 16 frozen representation settings, prediction agreement is 98.43-99.99%, with disagreements concentrated at small cosine margins. In controlled contrastive-only training with the training-frequency prior, Pure Angular editing improves both learned representations at all tested CIFAR-10/100 imbalance factors and retains positive changes on ImageNet-LT. Thus vMF concentration not only describes class distributions, but also forms a decision and learning scale in high-dimensional probabilistic contrastive learning.

---


### 95. [How Accurate Is Accurate Enough?](https://arxiv.org/abs/2609.38785)

**<font color=#1a73e8>作者：</font>** Ningkang Peng, Qianfeng Yu, Jingyang Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How accurate must a numerical approximation be within a learning system? Primitive error alone cannot answer this question: errors of the same magnitude can have very different consequences for losses, predictions, and gradients at different learning states. We study this question through the learning objective itself. The objective weights classwise numerical errors nonuniformly according to the current state, so the importance of an error depends not only on its magnitude but also on the class it affects and the weight that class receives. For softmax cross-entropy, we characterize this coupling between class weights and errors and derive the exact extrema of the signed loss change over pairings of fixed non-target probability and score-error multisets, with the target probability and target score error held fixed. Building on this structure, we establish finite-error guarantees that propagate primitive error to losses, probabilities, predictions, and feature gradients, then invert these guarantees to obtain a certified primitive tolerance for the current state under prescribed learning-level error requirements. We give a complete instantiation of the framework in high-dimensional von Mises-Fisher learning. Controlled interventions and a large collection of saved learning states show that identical primitive error can produce substantially different learning consequences, while certified numerical tolerances vary by orders of magnitude across states under the same learning-level requirements. These results show that the adequacy of a numerical approximation must be assessed in relation to the current learning state and the quantity to be preserved; numerical accuracy should itself be treated as part of the learning objective.

---


### 96. [Same Loss, Different Gradients](https://arxiv.org/abs/2609.38786)

**<font color=#1a73e8>作者：</font>** Ningkang Peng, Xiaoqian Peng, Yifan He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentiable learning typically assumes that the scalar objective evaluated in the forward pass and the gradient supplied to the optimizer in the backward pass describe the same mathematical object. We show that this correspondence can fail when probabilistic objectives rely on finite special-function recurrences, custom backward rules, and numerical clipping. In high-dimensional von Mises-Fisher learning, real numerical implementations can produce identical forward scores and losses at the same learning state while supplying different gradients and following different optimization trajectories. We characterize the structure of this mismatch in finite-start Bessel recurrence and show that classwise radial mismatch can compose through probabilities into a locally nonconservative update field. Evaluating the accuracy of special-function values and derivatives separately is therefore insufficient to characterize the realized learning objective. Motivated by this observation, we introduce AR/FR, a fixed-depth analytic realization that constructs a potential and its derivative jointly, ensuring forward-backward coherence by construction. We establish a uniform cubic-order error bound relative to the exact Bessel ratio over the entire nonnegative concentration axis and propagate this guarantee to learning scores and objectives. As representation dimension increases, the original finite recurrence becomes sequentially deeper, whereas the worst-case AR/FR error guarantee tightens cubically, jointly providing coherence, certified fidelity, and fixed-depth computation. These results suggest that a differentiable numerical primitive is defined by both the values it realizes and the derivatives it actually supplies to the optimizer; together, they constitute the numerical realization of the learning algorithm.

---


### 97. [Positive Ratings, Hidden Concerns: Employee Voice Disclosure in AI-Mediated Organizational Listening](https://arxiv.org/abs/2609.38788)

**<font color=#1a73e8>作者：</font>** Thilo Tamme, Michael Saatkamp, Alma Bonte 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organizations started listening to employees through conversational AI agents alongside structured surveys. Little is known about what these channels change in what employees say when disclosure carries hierarchical risk. We report a field study inside a global management consulting firm whose process pairs a pre-survey with an adaptive AI voice interview on the same themes within one session. Across 44 first-session interviews (132 matched theme observations), 20-41% of sessions showed a favorable rating co-occurring with a substantive concern voiced later, depending on the favorability threshold. The Gioia analysis drew on 158 protective quotes from 65 eligible sessions. Disclosure rarely arrived unguarded: employees softened concerns, deflected accountability, and bounded how far they went, and this protective work tracked the perceived legitimacy of the listening structure. We develop a grounded model of bounded disclosure and derive four propositions for voice, channel and listening research. Silence, we argue, can persist inside expression.

---


### 98. [Recovering Off-Policy Supervision for Speculative Decoding](https://arxiv.org/abs/2609.38795)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Chanjun Park, Sugyeong Eo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block drafters for speculative decoding are commonly trained on corpora written by external models, where a single off-policy token invalidates supervision for all subsequent slots in a block. Existing approaches discard these divergent slots, resulting in severe supervision loss. To resolve this problem while preserving the training corpus, we propose a rollout-based training framework that recovers full supervision through two complementary components. The first component, Anchor-Label Relabelling (ALR), replaces corpus labels with distributions from greedy target rollouts, restoring valid supervision across all predicted slots. The second component, In-Rollout Anchors (IRA), places draft blocks directly inside these rollouts to expose the drafter to target-generated context, reusing precomputed rollout features at no additional target cost. Across fixed vision-language and text corpora, our framework increases greedy accepted length by up to 36.5% over DFlash and consistently outperforms erasing baselines. Notably, a single epoch of our method surpasses the best erase schedules. After three epochs, it matches the acceptance length of training on target-regenerated responses. These results show that our framework provides an effective and compute-efficient approach for training speculative drafters on fixed corpora without modifying the original text. Code is available at this https URL.

---


### 99. [Evaluating Persistent Calibration under Evolving Model Knowledge](https://arxiv.org/abs/2609.38797)

**<font color=#1a73e8>作者：</font>** Victor Wang, Thomas Hofweber, Mohit Bansal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As AI systems move from static repositories to agents that are capable of continual adaptation and learning, maintaining their trustworthiness means equipping the models backing them with the ability to produce confidence estimates that dynamically reflect their changing skills and knowledge. We introduce the problem of persistent calibration, which requires a confidence estimator to faithfully reflect the knowledge contained in a model as that knowledge changes, without recurring supervision. We operationalize this by examining persistent calibration across checkpoints of open models, asking whether confidence estimators trained on earlier checkpoints can generalize to later ones. Specifically, we aim to shed light on whether confidence is dependent on knowledge, a question with implications for the reliability of confidence estimates. To measure this relationship, we define and evaluate calibration on knowledge contrast sets: subsets containing questions that one checkpoint answers correctly and another checkpoint answers incorrectly, reflecting a change in knowledge. We show that both inference-time and fine-tuning methods fall short on contrast-set calibration compared to oracle methods trained on future checkpoints, even for methods that are well-calibrated on the full dataset. We provide evidence for the hypothesis that persistent calibration is challenging because there is a vast space of possible confidence functions that are well-calibrated on a given checkpoint, out of which only some rely on meta-knowledge features that would generalize to other checkpoints. Towards improving contrast-set calibration, we show that multi-checkpoint training helps, suggesting an avenue for identifying confidence features that remain robust across changing knowledge.

---


### 100. [DCM-SAM: Defect-Conditioned Mixture of LoRA Experts for NPU-Deployed AM Defect Segmentation](https://arxiv.org/abs/2609.38811)

**<font color=#1a73e8>作者：</font>** Md Mushfiqur Rahaman, Md Mahedi Hasan, Imtiaz Ahmed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metal additive manufacturing parts are inspected by X-ray computed tomography, where labelled data is scarce, the pores and inclusions that matter span a few pixels, and inspection must happen at the machine. We present DCM-SAM, a defect-conditioned adaptive mixture of LoRA experts: one frozen Segment Anything backbone carries a separate Conv-LoRA expert bank and mask decoder per defect class, each trained in its own pass, without prompts, on synthetic slices alone, updating only 4.4% of the parameters. On benchmarks that XCT-SAM reports, DCM-SAM improves on every baseline for both classes from a ViT-B backbone against their ViT-H, and reaches 64.2% pore IoU on real NIST scans having seen no real images during training. Deployment then exposes what adaptation work rarely measures: on a Qualcomm Hexagon NPU, ViT-H and ViT-L compile yet cannot allocate at 1024x1024 image resolution, since activations rather than weights exceed the device ceiling, and quantizing weights does not help. ViT-B alone runs, but the adapted encoder then fails to allocate where the stock one succeeds, until a numerically identical rewrite of the attention lets the complete DCM-SAM run in FP16 at 1024x1024, with no operator falling back to the CPU, masks within 0.01% of pixels of the FP32 reference. Code: this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-382](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

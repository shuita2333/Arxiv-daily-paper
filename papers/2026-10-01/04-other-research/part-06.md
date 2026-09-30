# 📦 其他研究 | 2026年10月01日

> 本类共 **447** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-447](./part-09.md)

---

### 251. [UniBuild: Unified Building Mapping From Multi-Source Optical Remote Sensing Imagery With Detail Decoding and Geometry Regularization](https://arxiv.org/abs/2609.37031)

**<font color=#1a73e8>作者：</font>** Wei Huang, Chenying Liu, Yilei Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building extraction from optical remote sensing (RS) imagery is fundamental to urban mapping, yet existing methods are often dataset-specific and generalize poorly to unseen domains. Their practical use is also limited by insufficient detail recovery and weak geometric regularization, leading to blurred boundaries, irregular shapes, and merged adjacent buildings. To address these issues, we propose UniBuild, a unified building extraction framework for multi-source RGB optical RS imagery. First, a unified multi-dataset training scheme is constructed over heterogeneous RGB optical datasets to learn transferable building representations across sensors and resolutions. Second, a novel detail-preserving HR-DPT decoder is designed to integrate high-level semantic features with high-resolution spatial features, enhancing building detail recovery. Third, geometry-aware regularization is introduced through a structure-tensor-based direction-aware loss for boundary direction consistency and a saddle-aware loss for suppressing false activations in narrow inter-building gaps under low-resolution conditions. We train and evaluate UniBuild on multi-source RGB optical datasets, including 10 public high-resolution datasets and two self-collected low-resolution datasets. Experiments show that UniBuild consistently improves building-region accuracy, boundary sharpness, and adjacent-building separation across diverse datasets. It also generalizes well to unseen domains and supports practical building extraction from RGB optical RS imagery up to 10\,m resolution. The predicted masks can be further converted into GIS-compatible building footprints through simple polygonization. The trained model and inference code are released at this https URL.

---


### 252. [FedLAFP: Low-Rank Aggregation Meets Full-Rank Personalization in Federated Fine-Tuning](https://arxiv.org/abs/2609.37033)

**<font color=#1a73e8>作者：</font>** Mengjun Yi, Huaian Gu, Yinghao Ai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated parameter-efficient fine-tuning enables clients to adapt pre-trained models without sharing raw data or communicating the full model, but statistical heterogeneity makes a single global adapter insufficient for personalized prediction. Existing personalized methods typically use the same low-rank structure for both shared and private adaptation, overlooking their distinct requirements for aggregation and personalization. We propose FedLAFP, a role-aware framework that couples a compact, globally aggregated LoRA branch with a client-private, full-rank-capable RandLoRA branch. The shared branch provides an efficient interface for transferring common knowledge, whereas the private branch combines fixed random low-rank bases with learned scaling coefficients to provide expressive client-specific adaptation without additional communication. Client- and layer-specific mixing coefficients jointly fuse the two branches, and only the shared LoRA parameters are exchanged. A controlled linear study supports this role assignment: LoRA yields more aligned client updates and lower aggregation error, while RandLoRA more accurately recovers client-specific residuals. Experiments across four visual recognition benchmarks show that FedLAFP consistently outperforms local-only and federated LoRA baselines, achieving an average personalized accuracy of $86.93\%$ and exceeding the best baseline average by $1.30$ percentage points.

---


### 253. [Watch-Think-Interact: Bootstrapping Long-Horizon Multi-Turn Streaming Video Reasoning with Reinforcement Learning](https://arxiv.org/abs/2609.37035)

**<font color=#1a73e8>作者：</font>** Ziheng Huang, Yicheng Bao, Xueheng Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Streaming video assistance requires models to answer asynchronous questions from an observed prefix under a fixed context budget. Existing approaches model response timing or compress history, but an online state formed before future questions are known can omit visual details before later questions reveal their relevance; the retained state alone cannot recover them. We introduce Watch-Think-Interact (WTI), a closed-loop framework for multi-question streaming video reasoning. WTI maintains compact natural-language memory entries tagged with source-video time ranges; these entries support direct reasoning when sufficient and otherwise anchor selective recall of finer visual evidence. For each question, WTI answers when current context and memory suffice, continues watching when required evidence has not appeared, or recalls a relevant past interval and decides again after incorporating the returned chunks, without replaying the full observed history. To train this behavior, we construct WTI-82K, comprising 82,335 timed questions across 4,812 causally aligned trajectories, and develop Stream-GDPO to optimize complete multi-question streaming rollouts using trajectory-level feedback for response timing, source-video recall, and memory updates. WTI achieves state-of-the-art aggregate performance among the compared open-source streaming baselines, reaching 83.3% on StreamingBench and 73.6% weighted overall accuracy on OVO-Bench.

---


### 254. [High-Resolution Dynamic Functional Connectivity Generation with Graph-Variate Flow Matching](https://arxiv.org/abs/2609.37037)

**<font color=#1a73e8>作者：</font>** Om Roy, Yashar Moshfeghi, Keith Malcolm Smith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-resolution dynamic functional connectivity (DFC) can reveal rapidly evolving brain-network interactions, but short temporal windows yield noisy, often low-rank covariance estimates. Graph-Variate Dynamic (GVD) connectivity addresses this by modulating fast instantaneous interactions with stable trial-level support. This suppresses spurious fluctuations and emphasizes persistent, informative connections. We show that the Hadamard construction lifts low-rank instantaneous connectivity from the positive-semidefinite to the positive-definite cone, keeping high-resolution trajectories on the SPD manifold without ridge regularisation or post-hoc projection.
We introduce GVD-CFM, a class-conditional generative model for high-resolution dynamic connectivity. Each trial is represented as SPD GVD matrices on a product Riemannian manifold, then mapped through a global log-Euclidean diffeomorphism and an invertible temporal DCT basis. A Transformer-based conditional flow models all spectral modes jointly and generates the full trajectory non-autoregressively in Euclidean coordinates while preserving exact correspondence with valid SPD sequences. Retaining the full DCT basis also enables decoding on denser temporal grids without retraining.
Across multiple EEG motor-imagery datasets, GVD-CFM delivers the strongest overall results for held-out distributional fidelity, temporal-dynamics preservation, and synthetic-to-real classification. It also remains computationally efficient relative to strong raw-signal and direct GVD-space generative baselines. GVD-CFM therefore provides a practical framework for realistic, temporally coherent, high-resolution brain-network generation with preserved manifold structure and resolution-flexible decoding from a single trained model.

---


### 255. [NowcastDiT: Diffusion Transformers are Effective Precipitation Nowcasters](https://arxiv.org/abs/2609.37038)

**<font color=#1a73e8>作者：</font>** Haoran Xu, Xingzhuo Guo, Yuchen Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Precipitation nowcasting demands accurate short-term forecasts under strong spatiotemporal variability. Diffusion models are well suited to modeling complex precipitation distributions, yet existing approaches often introduce increasingly specialized designs, leaving the capability of a standard diffusion architecture underexplored. We show that a standard Diffusion Transformer already provides a simple and scalable foundation for precipitation nowcasting, with domain-specific requirements accommodated naturally within its design space. Based on this principle, we develop NowcastDiT and instantiate this flexibility through two complementary adaptations: a dynamics-aware noise prior for temporally coherent forecasts, and end-to-end reinforcement learning with timestep-aware rewards for meteorological skill. Experiments on SEVIR and MRMS benchmarks show that NowcastDiT achieves state-of-the-art performance in both perceptual quality and meteorological skill. These results suggest that standard DiT can serve as an effective foundation for precipitation nowcasting.

---


### 256. [Iterative Exact Discrete Guidance for Energy-Based Sampling](https://arxiv.org/abs/2609.37043)

**<font color=#1a73e8>作者：</font>** Yuwen Qian, Yidong Ouyang, Zhengyan Wan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from unnormalized distributions over large discrete state spaces becomes difficult when a multimodal target is far from a tractable reference. We introduce Iterative Exact Discrete Guidance (IEDG), a population-exact, trajectory-wise guidance framework for unnormalized discrete targets. Rather than learn the full reference-to-target correction in one step, IEDG introduces a global Boltzmann tilt along an annealing trajectory. Each stage learns a stage-local posterior correction for an incremental Boltzmann tilt of the current source, while the resulting corrections are accumulated relative to a fixed analytic posterior. At the population optimum, exact stage posteriors recover the correct reverse dynamics, whose exact simulation reproduces the target distribution. IEDG chooses stage increments by relative effective sample size (rESS), which controls Rényi-2 displacement and locally adapts the step size to the thermodynamic geometry of the annealing path. Our stagewise total-variation analysis shows that limited overlap amplifies Bregman fitting error by $1/\sqrt{\mathrm{rESS}}$, while posterior, simulation, and truncation errors enter additively. IEDG improves all distribution-level errors over the neural baselines on ordered, exactly enumerated Ising $4\times4$, while substantially reducing one-shot errors on Ising/Potts $16\times16$ across thermodynamic regimes and attaining the best neural-sampler result on several reported local-statistic and phase-coverage metrics. On Max-Cut, its best-of-512 and average-sample ratios exceed all the baselines. Code and artifacts are available at this https URL.

---


### 257. [NHO: A Neural Hamiltonian Operator for Anchor-based Region Localization and Dense Correspondance](https://arxiv.org/abs/2609.37048)

**<font color=#1a73e8>作者：</font>** Jing Li, Yawei Luo, Xiangze Meng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-rigid partial-to-full shape correspondence from sparse anchors requires identifying the corresponding region on the full surface and recovering dense correspondences between the partial shape and that region. We present NHO, which combines sparse anchors with the intrinsic geometry of the partial shape to learn a neural Hamiltonian operator whose localized eigenspace encodes both the region support and intrinsic coordinates for dense correspondence. NHO parameterizes the Hamiltonian potential as an intrinsic neural field and optimizes it using anchor evidence together with spectral and geometric constraints. To resolve the spatial ambiguity left by sparse anchors, we introduce reciprocal refinement between operator estimation and correspondence recovery. At each round, the current eigenspace provides spectral coordinates and restricts matching to its induced support, while geometrically reliable correspondences provide additional evidence for updating the potential. After refinement, aggregated eigenfunction energy yields the final localization, and the recovered map initializes dense correspondence refinement. Experiments demonstrate competitive accuracy on both tasks and robustness to uniform scaling and rotation.

---


### 258. [A Comprehensive View of Fairness through Distributional Stability](https://arxiv.org/abs/2609.37061)

**<font color=#1a73e8>作者：</font>** Gayane Taturyan, Charlotte Laclau, Stephan Clémencon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We view fairness as a property of distributional stability. Rather than assessing a predictor under a fixed data distribution, we study how its predictions change under perturbations that modify the composition of protected groups. A predictor is fair if it remains stable under such shifts. Under this perspective, several classical notions of fairness arise as stability with respect to specific perturbations, with the associated unfairness gap given by a Lipschitz constant of a prediction-rate functional. This formulation also yields guarantees that hold uniformly over a range of demographic compositions at test time, without requiring knowledge of the deployment distribution. It leads to a learning procedure based on convex combinations of reweighted predictors, formulated as a second-order cone program, for which we establish generalization bounds. Experiments on standard benchmarks illustrate the approach.

---


### 259. [RL-PaO: Prediction as Action in Decision Making under Uncertainty](https://arxiv.org/abs/2609.37065)

**<font color=#1a73e8>作者：</font>** Jiahui Feng, Dafang Zhao, Zheng Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-making under uncertainty often relies on predicted parameters, yet accurate prediction does not necessarily lead to good operational decisions. Aligning prediction with downstream optimization requires learning from the consequences of the decisions those predictions induce. We introduce RL-PaO, a reinforcement learning framework that integrates system formulation, optimization, and decision execution into a single environment. This yields a Markov decision process in which prediction is regarded as action: it shifts the environment to produce subsequent context and reward that explicitly aligns prediction error with realized cost, and learning the optimal policy does not require differentiating through the black-box solver. We evaluate RL-PaO on day-ahead energy scheduling using real historical data. On the test year, RL-PaO achieves the lowest annual cost among the non-oracle baselines, achieving on average $10\%$ cost reduction. Moreover, RL-PaO is capable of further analyses to provide strong interpretability both from the policy evolution perspective and the cost-accuracy trade-off.

---


### 260. [Context without Commitment: Robust Dense Correspondence under Non-Rigid Deformation](https://arxiv.org/abs/2609.37071)

**<font color=#1a73e8>作者：</font>** Yuzhen He, Sara Homscheid  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-rigid point-cloud registration aims to find the corresponding target point for each point on a deforming source surface. Point-level matching keeps the full target cloud available, but correspondence becomes ambiguous when different regions have similar local geometry. Regional or coarse-to-fine methods provide broader spatial context, but an incorrect regional match can exclude the correct correspondence before dense matching. We propose CoCo-Reg, which uses regional patches to enrich dense point features without allowing patch predictions to restrict the final point-level search. CoCo-Reg constructs farthest-point-sampled patches, exchanges geometric information within and between source and target, supervises patch similarity using identity-corrected point overlap, and projects the resulting regional information back to dense point features. The final registration stage still scores the full target cloud before global point-level candidate selection. On 726 held-out ModelNet10 objects across nine deformation levels, two established learning-based baselines obtain mean correspondence errors of 0.1993 and 0.1921, whereas CoCo-Reg obtains 0.0547. Relative to its point-level baseline, this is a 72.6\% reduction. CoCo-Reg achieves lower correspondence error on 92.3\% of paired test objects and reduces the mean fraction of points with error above 0.1 from 47.3\% to 17.3\%. Chamfer distance and HD95 decrease in the same direction, and CoCo-Reg remains lower across all tested deformation levels. These results support using regional context for dense non-rigid correspondence without imposing a hard patch-level restriction on the final search. Because evaluation uses one checkpoint per method, the reported gains characterize the complete systems rather than the isolated causal contribution of an individual component. Code will be made publicly available.

---


### 261. [ZeroDiff: Zero-Shot Time Series Reconstruction via Informed-Prior Diffusion](https://arxiv.org/abs/2609.37078)

**<font color=#1a73e8>作者：</font>** Yingda Fan, Dan Lu, Xiaowei Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series modeling increasingly demands high-quality supervision, yet target observations remain scarce - exogenous inputs are broadly available, but target measurements are often unavailable due to cost, infrastructure, or accessibility constraints. Can models trained on observed locations reconstruct target time series where measurements have never been collected? We term this zero-shot time series reconstruction. A naive approach - directly mapping exogenous inputs to targets - can yield predictions at unobserved locations, but without target signals, such models fail to capture the intrinsic dynamics of the target variable, producing overly smooth outputs that underestimate extremes. This reveals systematic errors that call for explicit modeling and calibration. We propose ZeroDiff, which constructs an informed prior from exogenous variables alone, then learns to calibrate reconstruction errors through diffusion - training on observed locations and generalizing to unobserved ones. Experiments across diverse real-world datasets demonstrate significant improvements over existing approaches. Our code is available at this https URL.

---


### 262. [LDM-is-AE: Latent Diffusion Model is an Auto-Encoder for End-to-End Image Generation](https://arxiv.org/abs/2609.37080)

**<font color=#1a73e8>作者：</font>** Zhengqiang Zhang, Lingchen Sun, Rongyuan Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent Diffusion Models (LDMs) typically adopt a two-stage pipeline: an auto-encoder (AE) is first pre-trained to define a latent space, then a diffusion model is trained to perform denoising within it. Such a two-stage design introduces a representation mismatch, as the latent space is optimized for reconstruction rather than adapting the denoising dynamics. We reveal that the LDM itself is an AE, and consequently present LDM-is-AE, an end-to-end one-stage LDM training framework that eliminates the need for a separately trained tokenizer. Our key observation is that the LDM backbone actually performs a latent-to-feature-to-latent transformation at each denoising step, which can be interpreted as an internal decoding--encoding process. Leveraging this structure, we split the DiT backbone into two reciprocal components, DiT-E (i.e., DiT Encoding) and DiT-D (i.e., DiT Decoding), and impose image-space supervision on the intermediate features across all timesteps. Our model encourages the internal representation to align with the image domain throughout denoising, thereby establishing an explicit latent-to-image-to-latent path. At the zero-noise timestep, our model further performs an image-to-latent-to-image mapping, corresponding to an auto-encoding process. As a result, LDM-is-AE jointly learns latent representations and denoising dynamics in an end-to-end manner, yielding a diffusion-native latent space tailored to the generation process. Experiments demonstrate that LDM-is-AE exhibits highly competitive generation performance, achieving an FID of 1.80 and 1.90 on 256x256 and 512x512 class-conditional image generation, respectively.

---


### 263. [Traverse: Learning When to Remember, Reset, and Redirect for Long-Horizon Web Search](https://arxiv.org/abs/2609.37082)

**<font color=#1a73e8>作者：</font>** Jingyuan Ma, Lynx Aster, He Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon information-seeking agents often accumulate noisy or misleading context, causing early mistakes to persist and making recovery increasingly difficult. We introduce an autonomous search harness in which the agent manages its own search process through three states: Rubric, Answer, and Verify. The agent first defines criteria for a valid answer, searches under these criteria, and then independently verifies the result before deciding whether to terminate or continue searching. It is further equipped with a Seal Memory tool that enables active context management. Training this behavior with reinforcement learning, however, can induce Seal Collapse, resulting in unstable training and preventing the agent from reliably learning when and how to use its memory tools. We solve this with a simple strategy that trains only the final segment after context management. Our 35B model achieves 72.83 on BrowseComp, outperforming comparable open-source systems, and consistently improves over the base model across BrowseComp-ZH, xbench, DeepSearchQA, WideSearch, financial investigation, and product search. Ablations show that autonomous compression outperforms automatic compaction and validate our RL design.

---


### 264. [Identifying ODEs from Unstructured Data with Causal Representation Learning](https://arxiv.org/abs/2609.37083)

**<font color=#1a73e8>作者：</font>** Alessandro Trenta, Riccardo Massidda, Davide Bacciu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of recovering the governing ODE of a dynamical system from unstructured, high-dimensional observations such as images. Existing methods for ODE discovery typically assume direct measurements of the variables, or do not provide theoretical guarantees on the learned variables and equations. While Causal Representation Learning (CRL) methods provide guarantees on identifying variables from high-dimensional observations up to component-wise diffeomorphisms, we show that in general these variables cannot be used directly as input to equation discovery methods, which typically assume that the variables will lead to sparse equations. So we introduce SParse Equivalent Equation Discovery AutoEncoder (SPEED-AE), a framework that combines a pretrained CRL method with a component-wise autoencoder that learns transformations of variables that are amenable to sparse ODE discovery. We show that for polynomial ODEs, this additional step allows us to restrict the identifiability of each variable from polynomial to monomial diffeomorphisms. Experiments on Lotka-Volterra, Lorenz, and a two-pendulum system show that SPEED-AE improves on the disentanglement of the CRL methods and that it recovers ODEs that are closest to the ground truth, while achieving state-of-the-art forecasting performance.

---


### 265. [Waypoint-1.5: A Real-Time Video World Model for Consumer Hardware](https://arxiv.org/abs/2609.37107)

**<font color=#1a73e8>作者：</font>** Rajit Rajpal, Shahbuland Matiana, Liew Wei Pyn 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Waypoint 1.5, a real-time diffusion world model for interactive video generation on consumer-grade hardware. Unlike general video diffusion models, interactive world models (iWMs) must respond to dense user controls under strict latency and throughput constraints. Waypoint 1.5 is pre-trained on 100,000 hours of diverse, control-aligned video game data across hundreds of games, and generates playable video conditioned on full keyboard and mouse input. The model includes two resolution variants that run across a wide spectrum of consumer hardware. To characterize this unique setting, we distinguish rendered FPS, latent FPS, and control rate. We describe the data pipeline, architecture, training methodology, and runtime system behind Waypoint 1.5. We evaluate interactivity through latency and throughput. Finally, we discuss the safety and ethics considerations unique to iWMs.

---


### 266. [Designing a Boundary Negotiating Artifact for Collaborative Socio-Technical Sense-Making in AI Regulatory Sandboxes](https://arxiv.org/abs/2609.37109)

**<font color=#1a73e8>作者：</font>** Idoia Landa-Oregi, Tom Deckenbrunnen, Alessio Buscemi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The rapid, unpredictable advancements in AI system capabilities has seen regulators take adaptive and experimental approaches to policymaking. Established in other domains as instruments balancing regulation with innovation, regulatory sandboxes are seen as solutions for AI regulation. However, analyses mostly focus on the legal and institutional design of AI Regulatory Sandboxes (AIRSes). With the legal framework leaving the socio-technical interpretation to stakeholders, this creates a gap on the sense-making required to fulfill the AIRS purpose. In this paper, we approach this by designing a Boundary Negotiating Artifact as a way to mediate meaning in AIRSes. Through Research-through-Design we iteratively develop a tool, providing an interface for the different stakeholders to collaborate in AI assessment. We then position it as technical backbone in established AIRS frameworks, structuring the collaborative sense-making of the involved stakeholders. We further report the insights gained from our design process leaving the qualitative evaluation for future work.

---


### 267. [Neural Constitutive Learning for Generalized Reaction-Diffusion Systems](https://arxiv.org/abs/2609.37113)

**<font color=#1a73e8>作者：</font>** Shang-Ke Chen, Yu-Peng Wang, Shih-Hsuan Hung 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalized reaction-diffusion systems encompass diverse transport mechanisms and coupled reaction kinetics. A central question for neural PDE solvers is what should be learned so that a common interface can accommodate phase-field and degenerate transport, local reactions, and multispecies coupling. We propose the Neural Constitutive Laws--Mass-Compression-Transport (NCL-MCT) Solver, which learns PDE-specific constitutive responses while retaining temporal evolution in a shared MCT integrator. Transport is represented through mobility and thermodynamic driving force, and reaction through relative reaction rates. These constitutive responses depend on the current density rather than explicitly on the initial condition or elapsed time, motivating their reuse across different initial conditions and time horizons. The same interface supports velocity-data supervision and known-law supervision, neither of which requires time integration during training. When constitutive laws are known, supervision can be evaluated on independently sampled density fields, enabling trajectory-free constitutive learning without generating solution trajectories. Across seven systems, separately trained constitutive modules share the same interface and MCT integrator and achieve relative rollout $L^2$ errors of $10^{-4}$ to $10^{-2}$. Tests with unseen initial-condition families and an extended time horizon assess reuse beyond training conditions, while separate experiments demonstrate trajectory-free constitutive learning. These results support constitutive responses as an effective learning target for a shared neural PDE framework.

---


### 268. [Interpretable intrinsic dimension estimation through componentwise calibration of distance and angle](https://arxiv.org/abs/2609.37114)

**<font color=#1a73e8>作者：</font>** Chih-Hsuan Huang, Chih-Wei Chen, Szu-Chi Chung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> DANCo (Dimensionality from Angle and Norm Concentration) jointly calibrates nearest-neighbor distance and angular statistics and consistently reaches state-of-the-art accuracy on clean intrinsic-dimension (ID) benchmarks. Practical data, however, introduce neighborhood-relative noise and sample-amplitude heterogeneity that can distort these geometric signals. We reformulate DANCo componentwise, retaining separate distance and angular discrepancy curves so that the source of an estimate can be identified and interpreted. For the distance component, we derive a closed-form Kullback-Leibler divergence for the generic-order ratios of the generalized ratios ID estimator (Gride); when both angular parameters are matched (Full), Gride reduces mean percentage error from $27.7\%$ to $17.6\%$ at noise equal to $40\%$ of typical neighbor spacing on 24 manifolds. For the angular component, two sampling regimes motivate aligning mean direction while retaining concentration matching (Profiled). On a Gaussian scale mixture with generating dimension 70 embedded in 100 dimensions, profiling raises the Minimum Neighbor Distance (MiND) estimate from $22.8$ to $66.7$, while removing the known amplitudes restores MiND-Full to $71.9$; the control thus attributes the Full shortfall to amplitude heterogeneity. On CIFAR-10 and ImageNet, amplitude-reducing normalizations move angular location toward the references and narrow the Full-Profiled gap, an observational counterpart to the controlled mixture. Across four pretrained convolutional neural networks, Gride-Profiled, the two-nearest-neighbor estimator (TWO-NN), and the maximum-likelihood estimator (MLE) exhibit similar rise-and-fall profiles, while Full-Profiled differences identify the layers most sensitive to angular calibration.

---


### 269. [NRF-GS: Neural Residual Fields for Expressive and Compact Gaussian Splatting](https://arxiv.org/abs/2609.37115)

**<font color=#1a73e8>作者：</font>** Pratik Singh Bisht, Andreas Kolb  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We revisit the role of appearance modeling in 3D Gaussian Splatting (3DGS) and show that limited expressiveness in view-dependent reflectance is a key driver of representation redundancy. In standard 3DGS, low-order spherical harmonics (SH) are used, restricting the splats' ability to model high-frequency directional effects, which is typically compensated by increasing the number of splats. We propose \emph{NRF-GS: Neural Residual Fields for Gaussian Splatting}, a hybrid representation that replaces per-splat SH-bases with a shared neural residual field. Each Gaussian encodes a compact set of appearance features and a lambertian base color, while a lightweight \emph{global scene-level MLP} predicts view-dependent residuals conditioned on viewing direction, distance, and per-splat features. This formulation enhances directional reflectance modeling by combining diffuse per-splat reflectance representations with a shared global function for high-frequency details, enabling both higher expressiveness and parameter sharing across splats. Our key insight is that by accurately capturing high-frequency directional reflectance, especially in specular regions, the GS-representation becomes more expressive, reducing the need for geometrically redundant splats. As a result, NRF-GS achieves comparable or better rendering quality while reducing the number of Gaussians by up to 50\%, and produces visibly improved specular and high-frequency details.

---


### 270. [Learning the Structure of Triangular Transport Maps](https://arxiv.org/abs/2609.37122)

**<font color=#1a73e8>作者：</font>** Morten Blørstad, Pekka Parviainen, Berent Ånund Strømnes Lunde  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Triangular transport maps provide a flexible approach to sampling-based probabilistic modeling, including density estimation, generative modeling, and Bayesian inference. They transform an unknown target distribution into a simpler reference through a monotone triangular map. The map structure is defined by a variable ordering and sparsity pattern, which together encode a directed acyclic graph. Map quality can depend strongly on this structure, yet finding a good structure is computationally expensive because each candidate generally requires fitting a different map. A central challenge is therefore to learn density and structure jointly, while keeping computation manageable as dimension grows. We introduce Self-Structuring Transport Maps (SSTM), which learn the map, ordering, and sparsity jointly. We use SoftSort to learn the variable ordering and $L_0$ gates to learn the sparsity, while preserving a triangular structure. To keep the map scalable, we use a monotone BatchEnsemble that shares one weight matrix across all map components through rank-one adapters. Across synthetic and real data, jointly learning the structure and map gives better density estimates than estimating the structure first. When the structure is identifiable from the density, SSTM matches the density performance of a map fitted with the true structure and outperforms autoregressive flows. On large datasets, SSTM is competitive with autoregressive flows.

---


### 271. [When Should Agents Check External State? Budgeting Observations for Stored Intentions](https://arxiv.org/abs/2609.37125)

**<font color=#1a73e8>作者：</font>** Zhengkun Di, Bin Shi, Kai Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prospective memory allows an agent to retain an intention tied to a future condition, but the stored intention does not reveal whether that condition currently holds. Checking it may require web access, multi-step tool use, and paid calls. Existing systems decide when intentions require attention, but do not allocate the resulting observations under a shared budget. We introduce the first resource-allocation formulation for the external observations required by stored intentions under a shared episode budget. BudgetPM offers two policy variants that share a hard-budget executor. BudgetPM-Static uses a lightweight Logistic scorer to learn whether a check improves the current decision. BudgetPM-Sequential distills full-episode hindsight schedules into a lightweight policy that decides when to spend or reserve capacity using only pre-query information at deployment. We evaluate BudgetPM against two public memory-agent systems, five matched controls, and four hand-designed monitoring or budget-adaptation rules. Across two benchmarks and three backbones, BudgetPM-Static outperforms adapted Mem0 and PMA workflows. On PM-Bench, its Logistic scorer reaches competitive quality--cost operating points alongside higher-capacity scorers and retains 99.9--100\% of unconstrained quality with 42--54\% fewer observations. Under severe scarcity and the same hard caps, BudgetPM-Sequential exceeds the strongest tested natural monitoring schedule by 1.92--2.58 Set F1 points. It reaches the same Set F1 and on-time recall with 16--33\% fewer observations. Matched attribution, exact-cost analysis, and a fixed-budget load intervention link this gain to competition between present and future opportunities. These results yield a demand--capacity design rule: local gating works when capacity covers demand, while future-aware supervision adds value when observations compete across time.

---


### 272. [Multi-Granularity Language-Guided Imitation Learning via Instruction Decomposition](https://arxiv.org/abs/2609.37135)

**<font color=#1a73e8>作者：</font>** Yi-Pei Chiu, Wei-Ta Chu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Using language instructions as conditions to guide robot policy learning has recently become an important research domain. However, existing language-guided policy learning methods typically use an overall task description to guide the entire demonstration trajectory. For manipulation tasks involving multiple execution stages, these methods assign the same language description to different subtasks, making it difficult to distinguish the behaviors required at different stages. In this work, we propose a multi-granularity language guidance method based on instruction decomposition. The proposed method decomposes an overall task description into more fine-grained, concrete subtask-level language instructions, thereby enhancing learning efficiency and improving performance. We evaluate the proposed method in the setting of multi-task imitation learning and validate its effectiveness.

---


### 273. [TaoFlowForge: Progressive Native Mesh Generation via Cascaded Flow Matching](https://arxiv.org/abs/2609.37139)

**<font color=#1a73e8>作者：</font>** Xianze Fang, Qiyuan Feng, Dongfang Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D content generation technology has significantly advanced the work of designers, as well as the 3D printing and gaming industries. However, it remains difficult to produce lightweight, editable, and topologically clean artistic content that is directly production-ready. To achieve this, we present TaoFlowForge, an artistic mesh foundation model that generates production-ready meshes. Specifically, TaoFlowForge decomposes the mesh generation process into vertices generation and their connectivity prediction, i.e., edges. We formulate vertices generation as a two-stage coarse-to-fine process and incorporate several effective loss functions to further enhance its performance. In the connectivity prediction stage, we propose a simple yet effective method for estimating the connectivity affinity between vertices and additionally predict per-vertex normals, which determines the correct orientation of faces. Besides, we construct a large-scale dataset combining hand-crafted 3D assets with public high-quality topology datasets. Based on this, a carefully designed data curation pipeline is employed to filter the raw dataset, retaining only high-quality topology data for model training. Our model is trained on the combined dataset and tested on both out-of-distribution hand-crafted set of 3D assets and public datasets. Under image-conditioned generation, TaoFlowForge outperforms autoregressive methods and achieves state-of-the-art results among open-source mesh topology generators. We will release all the code and weights together with a portion of our test dataset.

---


### 274. [MSTypography: Multi-character Semantic Typography via Balancing Word Legibility and Object Recognizability](https://arxiv.org/abs/2609.37141)

**<font color=#1a73e8>作者：</font>** Xinye Yang, Xinding Zhu, Kai Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic typography is a design technique where the visual representation of a word conveys its semantic meaning, while maintaining its legibility. Existing digital typography methods mainly focus on single-character scenarios. They suffer from a lack of legibility constraints and insufficient local deformation when extended to multi-character words, as the intricate structures among multiple characters are hardly preserved during the typography process. In this paper, we propose a global-to-local typography framework for multi-character scenarios. It performs mask-driven silhouette approximation at the global level, while semantic-guided refinement at the local level, with a culling step in between to improve efficiency. To preserve word legibility, we designed structural losses (including explicit collision constraints and implicit Jacobian singular value constraints) and an OCR constraint for character-level readability. To enhance the object recognizability, we leverage semantic guidance with diffusion priors, which drives the character glyph toward the target concept while preserving its structural integrity. To the best of our knowledge, this is the first multi-character semantic typography method that effectively balances word legibility and object recognizability. Evaluations on five representative languages (English, Chinese, Japanese, Korean, Arabic) demonstrate superiority over SOTA methods. Codes will be open-sourced.

---


### 275. [Improved Distributional Diffusion Models](https://arxiv.org/abs/2609.37147)

**<font color=#1a73e8>作者：</font>** Tommaso Martorella, Alexandre Galashov, Felix Krause 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distributional Diffusion Models (DDMs) replace the standard mean-prediction denoiser with a \emph{distributional} denoiser trained via a scoring rule objective, learning a stochastic approximation to $p(x_1 \mid x_t)$ rather than its conditional mean. However, scaling DDMs to modern image-generation settings faces two obstacles: (i) multi-particle training incurs overhead that scales with the number of particles, (ii) DDMs use globally fixed scoring rule hyperparameters, forcing a single trade-off across sampling budgets. We mitigate these limitations by deferring particle expansion to late transformer layers, and the hyperparameter trade-off by introducing time-dependent scoring rule schedules informed by the dynamical regimes of~\citet{Biroli2024}. Combined with a DiT-based latent setup, these changes make DDM training practical on class-conditional ImageNet-$256^2$, achieving 4.48 FID at 4 steps and 2.38 at 50 steps with DiT-XL/2, from a single model trained from scratch in one stage, without a teacher, self-distillation or JVPs. The result is a stochastic few-step generator whose FID does not degrade as the sampling budget grows from 4 to 50 NFE, and the same recipe transfers to text-to-image generation. Code and pre-trained models available at this https URL.

---


### 276. [Multimodal Detection of Higher-Order Behavioral Constructs: Self-Compassion in Structured Reflective Interaction](https://arxiv.org/abs/2609.37148)

**<font color=#1a73e8>作者：</font>** Siddhant Jain, Dimitra Tsovaltzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many of the qualities that matter most in how people learn and grow, how someone regulates their emotions, reflects on a setback, or stays aware of others during a difficult conversation, are not directly observable. They have to be inferred from how someone speaks, moves, and sounds over time, and they resist the kind of clean labeling that most machine learning pipelines are built around. We study this challenge through a case that is well grounded in psychological theory but rarely modeled computationally: self-compassion, the tendency to respond to one's own setbacks with patience rather than harsh self-criticism. We examine how it appears during structured reflective interviews in a technology-mediated training setting, where people naturally talk through socio-emotionally demanding situations. Since no existing dataset captures this kind of construct in this kind of setting, we collected and annotated 51 reflective dialog sessions using an independent, temporally overlapping annotation scheme grounded in established theory. We consolidate the underlying six-component psychological model into a three-class supervision space, balancing self-kindness and mindfulness against self-critical or overwhelmed states, and build a reproducible window-based pipeline that aligns video, audio, and text on a shared timeline. Unimodal models trained on each modality separately are compared against a simple probability-level fusion strategy, which yields modest but consistent gains over the best single modality. We close by discussing where each modality succeeds or struggles, what this suggests about how this kind of construct is actually expressed in reflective speech, and what would be needed to model it, and constructs like it, more effectively.

---


### 277. [Lucid Dreaming for World Models: Learning to Doubt Imagination and Decide by Trust](https://arxiv.org/abs/2609.37156)

**<font color=#1a73e8>作者：</font>** Ziqi Wen, Ting Xu, Lianyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models enable agents to learn and plan in imagination, but predictions beyond their experience can become unreliable and mislead decisions. Existing uncertainty estimates derived from predictions can remain overconfident on unfamiliar state-action pairs. We propose the Lucid World Model (LucidWM), which learns doubt from experience and propagates trust through imagination. By integrating Subjective Logic into categorical latent transitions, LucidWM distinguishes predicted outcomes from their evidential support and assigns each transition a degree of doubt. The complement of this doubt defines transition-level trust, which accumulates multiplicatively along imagined trajectories to reweight returns for policy learning and guide action selection. Uncertainty estimation requires no additional parameters or forward passes. Evaluated on four base world models against seventeen uncertainty readouts, LucidWM detects environmental changes and signals uncertainty during action-corrupted rollouts. In a controlled navigation case study, acting on trust reduces the number of steps required to reach the goal from 362 to 190. Fifteen demonstration videos show how LucidWM doubts its dreams and acts on that doubt. Videos are available at this https URL.

---


### 278. [GLASS: Global Latent Aggregation with Slot-based Set Decoding for Scalable All-Atom Crystal Generation](https://arxiv.org/abs/2609.37158)

**<font color=#1a73e8>作者：</font>** Hendrik Kraß, Seyed Mohamad Moosavi, Mathias Niepert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models for crystals enable the discovery of novel structures, but scaling all-atom generation to larger systems such as metal--organic frameworks remains challenging. We connect this difficulty to the correspondence problem of particle-space generation. Even on a single fixed target set, index-free permutation-equivariant particle flows require substantially more training for reliable generation as set size and density increase, under both independent and optimal-transport couplings. To resolve this challenge, we introduce GLASS---Global Latent Aggregation with Slot-based Set Decoding, which encodes structures in a permutation-invariant global latent space and learns their distribution via flow matching. A learned-slot decoder constructs all atoms in parallel, removing atom-wise correspondence from generative transport. On MP20, GLASS is competitive with particle-space models, and flow training can reach the validity of the training data at every structure size. On a QMOF subset, GLASS generates MOFs with up to 150 atoms per unit cell without conditioning on building blocks, topology, or composition, and approaches the structural validity of the training data. On both datasets, flow training exposes a validity--novelty tradeoff, and MOF novelty remains limited by autoencoder generalization on the available data. These results show that separating correspondence assignment from generative transport provides a simple route toward high-validity generation of larger atomistic systems.

---


### 279. [The Vote Hides the Failure: Aggregation Choice and Noise Robustness in Heart Murmur Detection](https://arxiv.org/abs/2609.37161)

**<font color=#1a73e8>作者：</font>** Nicholaus Dismas Ladislaus, Olatunji Damilare Emmanuel, Samuel Chol Buol  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Noise robustness in automated phonocardiogram (PCG) murmur detection, and how it is measured, remains underexamined despite growing interest in low-resource screening. We evaluate two independently reimplemented pipelines, Hierarchical Multi-Scale Convolutional Network (HMS-Net)--CNN, and Bidirectional Long Short-Term Memory (BiLSTM)--LSTM, under controlled, multi-severity noise with noise-augmented fine-tuning and held-out generalization testing. Under matched aggregation, the complete BiLSTM pipeline outperforms the complete HMS-Net pipeline across all conditions in accuracy and Weighted Accuracy. A stable aggregate accuracy score can misrepresent what individual predictions show: HMS-Net's native aggregation degrades under salt-and-pepper noise far less than majority-vote (MV) aggregation at the same severity, a gap reflecting window-level disagreement its native rule absorbs, while BiLSTM's MV accuracy rises after noise-augmented training even though its individual predictions do not improve. HMS-Net's training effect is significant under one accuracy metric but not another. Noise-robustness conclusions can depend as much on evaluation choices as on the models themselves.

---


### 280. [End-to-End Self-Supervised RGB-T Tracking without Modality Misleading](https://arxiv.org/abs/2609.37162)

**<font color=#1a73e8>作者：</font>** Shenglan Li, Rui Yao, Kunyang Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-T object tracking leverages the complementary characteristics of visible and thermal infrared modalities to improve robustness under adverse conditions. Existing supervised methods typically rely on costly modality-aligned bounding box annotations, while most self-supervised approaches follow a two-stage pseudo-labeling paradigm, making tracker training sensitive to pseudo-label quality and preventing joint end-to-end optimization. In this paper, we propose ESMTrack, a fully end-to-end self-supervised RGB-T tracking framework without offline pseudo-label generation or dense frame-level bounding box annotations. Given only the standard initial-frame annotation used in visual tracking, ESMTrack learns discriminative and temporally consistent representations through two complementary objectives: a grounding triplet loss on annotated initial frames and a cross-frame temporal triplet loss on unlabeled search frames, with reliable samples selected by forward-backward consistency. To address modality dominance bias, ESMTrack employs a three-branch architecture consisting of a fusion branch and two unimodal branches for RGB and thermal inputs. We quantify modality contributions using the Average Peak-to-Correlation Energy by measuring response discrepancies between the fusion and unimodal branches. The resulting reliability estimates guide a training-time modality decoupling mechanism that suppresses dominant-modality shortcuts and adaptively weights cross-modal contrastive learning for task-level alignment. Extensive experiments on five RGB-T tracking benchmarks show that ESMTrack achieves competitive state-of-the-art performance, strong cross-dataset generalization, and real-time inference speed. The source code is available at this https URL.

---


### 281. [Sparse cubical complexes for efficient topology-preservation in image data](https://arxiv.org/abs/2609.37177)

**<font color=#1a73e8>作者：</font>** Alexander H. Berger, Marco Fontana, Daniel Rueckert 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Persistent homology (PH) is a frequently used tool for extracting and preserving topological information from image data, particularly in image segmentation, where preservation of topological structures is important. However, despite its general applicability across dimensionality, domains, and target structures, the runtime cost of PH-based methods often makes their practical use infeasible. In this work, we argue that this runtime cost is largely driven by processing information that is unimportant for downstream application (e.g. as optimization objective). We propose sparse cubical filtrations as an alternative foundation for PH computation, reducing subsequent computational costs by factors of up to 100 on real datasets. We show close agreement with the optimization signal of the dense counterpart and empirically evaluate our solution's effectiveness as an optimization objective in realistic training regimes where other PH-based objectives can practically not operate (i.e., 3D data with large patch sizes). We show how our solution improves topological accuracy by up to 80\% across six diverse datasets while maintaining pixel- and region-based accuracy.

---


### 282. [Accelerated surrogate dynamics for dynamical, stochastic system evolution](https://arxiv.org/abs/2609.37184)

**<font color=#1a73e8>作者：</font>** Marco Jochum, Ioannis Kouroudis, Gohar Ali Siddiqui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dynamic simulations are an entrenched way of gaining insight into the evolution of system dynamics. Their computational cost however is often prohibitively high, especially in cases of stochastic frameworks. Machine learning algorithms are especially suited as simulation surrogates. Nevertheless, they face some very distinct limitations. Firstly, the sheer dimensionality of these systems, however, precludes the use of traditional time series models who struggle with high dimensional feature spaces. Additionally, traditional time series focus exclusively on either long or short range effects, causing local or global drift given enough time. In this paper, we propose a framework that addresses those limitations. Our framework combines a Variational Autoencoder, with a convolutional or graph basis that reduces the dimensionality of the system. This latent vector is propagated in time using a Temporal Fusion Transformer model, which includes both long range and short range effect encoding, as well as static covariate support. We test our framework on three distinct cases, to prove its robustness and in all three we have achieved practically identical to the simulation results at a fraction of the time. Further, our framework is flexible enough to be adapted to any new system and provides an inbuilt uncertainty quantification for targeted experiment design.

---


### 283. [InsightMap: Structured Spatial Modeling for Embodied Multimodal Reasoning](https://arxiv.org/abs/2609.37187)

**<font color=#1a73e8>作者：</font>** Hongpei Zheng, Hujun Yin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-guided navigation requires connecting partial observations to a persistent spatial reference and learning how actions change that representation. We introduce InsightMap, a framework that uses top-down maps as both explicit spatial memory and action-conditioned prediction targets. Historical views are linked to labeled map locations, and a shared multimodal backbone jointly learns navigation action prediction and post-action map generation. Map prediction provides auxiliary training supervision, while navigation inference decodes actions from the observed spatial context. An aligned RGB-D data pipeline supports a common interface for navigation, visual question answering, situated reasoning, and 3D grounding. On the validation-unseen splits of R2R-CE and RxR-CE, InsightMap achieves success rates (SR) of 56.9% and 54.9%, respectively. Adding map-prediction supervision improves R2R-CE SR by 4.3 and success weighted by path length (SPL) by 3.2 percentage points. On static spatial tasks, InsightMap achieves 103.7 CIDEr on ScanQA, 60.1% exact-match accuracy on SQA3D, and 53.1% grounding accuracy at 0.5 IoU on ScanRefer with detected object proposals. On Unitree Go2, it outperforms NaVid and NaVILA in hallway, lab, and office environments.

---


### 284. [Corruption-Robust Sparse Linear Contextual Bandits with Knapsack Constraints](https://arxiv.org/abs/2609.37189)

**<font color=#1a73e8>作者：</font>** Yige Wang, Hanyang Li, Yiming Zong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study sparse linear contextual bandits with knapsack constraints under joint reward and consumption corruption. Consumption corruption creates a challenge beyond corrupted rewards: it affects not only statistical estimates, but also the recorded budget, resource prices, and stopping decisions that govern future allocation. We develop Robust Optimistic Primal--Dual (ROPD), an estimator-modular framework that combines corruption-aware confidence widths with online resource prices and a budget-safety rule. With concrete sparse implementation, ROPD achieves regret against a clean population-LP benchmark of $\widetilde O(T^{2/3}+\Gamma T^{1/3})$ under forced exploration and population-design coverage, and $\widetilde O(\sqrt T+\Gamma)$ under on-policy realized-design coverage, for a supplied valid corruption bound $\Gamma$ under the stated proportional-budget scaling and fixed model/design parameters. When the corruption level is unknown, Shared-Grid adapts confidence radii around common point estimates fitted to a single realized history, incurring explicit initialization and master-comparison costs; its sharper on-policy guarantee additionally requires recommendation coverage. Both methods preserve observed budgets on every realization and bound clean resource violation by cumulative consumption corruption. These results connect corruption-robust sparse estimation with resource accounting, pricing, and stopping in high-dimensional online allocation.

---


### 285. [HaPRL: Human-Anchored Process Reinforcement Learning for Visual Search Agent](https://arxiv.org/abs/2609.37190)

**<font color=#1a73e8>作者：</font>** Zhangquan Chen, Yaoxin Niu, Xiang An 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-turn visual search agents answer questions about high-resolution images by iteratively deciding where to look. Reinforcement learning for these agents rewards only the final answer, leaving the search process unsupervised. Consequently, faulty routes in which the reasoning process is erroneous yet the final result is correct arise frequently, which in turn leads to ineffective training, i.e., scaling along the wrong paths. In this paper, we introduce HaPRL, the first framework to reinforce the search process with human search behavior. We first build an annotation platform and collect 1K+ human-annotated data with fine-grained behavioral signals. During training, a carefully designed judge scores each rollout with task-adaptive weights, anchored on the distilled trace of how a human annotator actually searched the same image. Extensive experiments show that HaPRL consistently outperforms outcome-based RL, and early-stage process supervision yields 6.7x more improvement in subsequent outcome-based scaling. Our results also demonstrate the importance of aligning model behavior with human process annotation signals, which offer new insight into the training of foundation models.

---


### 286. [V-Engram: Trigger-Indexed External Memory for Modular Text-to-Image Personalization](https://arxiv.org/abs/2609.37198)

**<font color=#1a73e8>作者：</font>** Haoran He, Runyuan Cai, Yiming Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pretrained text-to-image models contain broad visual knowledge, yet they cannot reliably acquire or refine a specific visual identity from only a few references while preserving compositional control. Token-embedding methods are compact but often underfit identity, whereas adapter-based methods improve fidelity through persistent weight updates that can be costly to store and interfere when concepts are composed. We introduce V-Engram, a trigger-indexed external memory mechanism for Stable Diffusion 3.5. Each concept is assigned an explicit trigger that retrieves concept-specific memory, whose gated directions enter frozen text-encoder and MMDiT context states as relative residuals. Separating this memory from backbone adaptation enables prompt-selective and multi-concept access without merging model updates. Experiments show that V-Engram broadly matches DreamBooth-LoRA in overall subject fidelity while showing advantages in settings such as contextual subject preservation. Prompt-matched loading retrieves only matched entries, reducing most additional adaptation-state loading for a single-concept query. Qualitative results further demonstrate paired-trigger composition and same-class separation, while prompts without registered entries retain the frozen model's base behavior. Together, these results establish trigger-indexed memory as a modular interface for adding targeted visual evidence without rewriting the generator.

---


### 287. [Adaptive Reward Routing: Dynamic Multi-Reward Optimization for Joint Audio-Video Diffusion via Forward-Process RL](https://arxiv.org/abs/2609.37200)

**<font color=#1a73e8>作者：</font>** Songlin Yang, Xiaotong Zhao, Jiacheng Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-reward guided reinforcement learning (i.e., RL) offers a promising way to improve joint audio-video diffusion models along several complementary objectives, including modality-specific quality, cross-modal semantic alignment, and temporal synchronization. Its effectiveness, however, depends on two quantities that change during training: where reward-driven updates should act, and how competing rewards should be combined. Existing methods tend to rely on fixed routing and reward weights, failing to track evolving model functions. To address these limitations, we propose Adaptive Reward Routing to jointly adapt update locations and reward coordination during forward-process RL (i.e., DiffusionNFT) of joint audio-video diffusion models. Our method consists of two components. (i) Cross-Modal Influence-Guided Routing (Localizing Updates): We use bidirectional cross-attention responses as an efficient proxy for evolving cross-modal influence, dynamically reweighting token-aware losses and scaling gradients across cross-modal layers without additional model interventions. (ii) Preference-Preserving Modality-Aware Reweighting (Coordinating Rewards): We preserve predefined weights as preference priors and use branch-specific reward-gradient interactions as residual corrections after warm-up. This resolves evolving conflicts without letting dominant rewards suppress weak but essential objectives. Extensive experiments demonstrate consistent improvements in modality quality, semantic consistency, and audio-video synchronization over strong RL baselines. Ablations and mechanism analyses further validate the complementary benefits of adaptive update routing and reward coordination.

---


### 288. [Pointwise or Pairwise: When Do Pairwise Losses Help Reward Learning, Provably?](https://arxiv.org/abs/2609.37209)

**<font color=#1a73e8>作者：</font>** Junghyun Lee, Minsoo Ha, Sanghwa Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pairwise losses are increasingly used for reward learning even when pointwise rewards are observed, with mixed empirical results. When and why do pairwise losses outperform pointwise losses? We study this question in a grouped offline contextual-bandit setting allowing multiple actions per context, capturing many reward learning scenarios. We compare Value Regression (VR), which regresses observed rewards pointwise, with Value Difference Regression (VDR), which regresses reward differences between a pair of actions sampled under the same context. We consider a semiparametric model where the mean reward is the sum of a learnable action-dependent component and an arbitrary context-dependent yet action-independent nuisance, capturing context-specific disturbances. Using a unified localized analysis, we prove finite-sample regression guarantees for finite and linear function classes and translate them into offline-regret bounds. For finite classes, VDR eliminates the misspecification term in the VR bound and improves a reward-scale-dependent error term by averaging over actions within each context, a benefit absent from the corresponding VR term. For linear classes, neither method uniformly dominates: within-context differencing removes nuisance-induced bias but may increase estimation variance relative to using absolute rewards when the misspecification is sufficiently low. This yields a feature geometry-dependent bias-variance tradeoff, which we corroborate with numerical experiments.

---


### 289. [Explainable Machine Learning for Multilayer Planar Winding Inductance Estimation](https://arxiv.org/abs/2609.37211)

**<font color=#1a73e8>作者：</font>** Spyros Rigas, Theofilos Papadopoulos, Georgios Alexandridis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rapid and accurate self-inductance estimation for multilayer rectangle-shaped planar windings is essential for modern high-frequency power converters, yet traditional workflows rely on complex mathematical equations, rigid monomial formulas or unexplainable black-box machine learning (ML) models that degrade severely outside their training domain. This paper introduces an explainable ML framework unifying post-hoc feature attribution (SHAP and permutation importance) with Kolmogorov-Arnold Network-guided symbolic regression via the SR-KAN framework to discover closed-form analytical equations without prior structural assumptions. Evaluated on a new open-source dataset of over 10,000 Finite Element Analysis (FEA) simulations across seven out-of-distribution (OOD) classes, standard tree-based ensembles exhibit severe extrapolation errors (> 36%), whereas the unconstrained SR-KAN expression achieves a robust OOD relative error of 8.22%. Experimental verification across 55 physical printed circuit board prototypes (up to 8 layers, with inductances from 4.11 {\mu}H to 559.27 {\mu}H) confirms that the KAN-discovered expression translates effectively to real-world hardware, predicting inductance with a mean absolute relative error of 6.26%. To support reproducible research, the complete FEA simulation dataset and prototype measurements are released open-source.

---


### 290. [When Cyber Scoring Systems Diverge: An Empirical Comparison](https://arxiv.org/abs/2609.37217)

**<font color=#1a73e8>作者：</font>** Kirsi Hellsten, Joni Herttuainen, Ambrose Kam 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vulnerability scoring systems underpin cyber patch prioritization and risk management, but their comparative behavior is almost always assessed in the abstract, through correlation studies in IT vulnerability databases, rather than by the operational consequences they produce when embedded in a system-level risk model. Here we present an empirical comparison of four vulnerability scoring systems, namely CVSS (Common Vulnerability Scoring System), EPSS (Exploit Prediction Scoring System), SSVC (Stakeholder-Specific-Vulnerability Categorization), and IronMiner (operationally calibrated proprietary scoring system). As a substrate for comparison, we use a reconstruction of the 2015 Ukraine Power Grid operational-technology (OT) network that provides a documented incident topology. The results show a high degree of disagreement between the scoring systems. This suggests that the choice of the scoring system could significantly influence mitigation strategies and vulnerability prioritization, implying that a composite or hybrid scoring approach could offer a more suitable solution.

---


### 291. [Information Bottleneck-Guided Adaptive Hypergraph Transformer for Brain Disease Diagnosis](https://arxiv.org/abs/2609.37220)

**<font color=#1a73e8>作者：</font>** Jingxi Feng, Xudong Chen, Yifan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Exploring high-order correlations and long-range dependencies in brain networks holds significant value for both neuroscience research and clinical diagnosis. However, previous studies have lacked a unified integration of high-order and long-range dependency information in brain networks, and there is substantial redundancy behind various types of information. These issues limit their effectiveness in the diagnosis of brain diseases. To address this, we propose an Information Bottleneck-Guided Adaptive HyperGraph Transformer (IBAHGT). By incorporating the information bottleneck (IB) principle, this approach enables adaptive learning of high-order correlations and both short- and long-range dependencies within a unified framework for brain network analysis, achieving high-precision brain disease diagnosis. IBAHGT consists of three key components: an information bottleneck-guided adaptive hypergraph convolution, which introduces a novel hypergraph information bottleneck (HIB) principle to adaptively learn hypergraph message-passing weights between nodes and hyperedges, optimizes information flow and captures high-order information in brain networks that is maximally informative and minimally redundant (MIMR). The Transformer encoder captures global information within brain networks through the attention mechanism, specifically modeling short- and long-range dependencies. An information bottleneck-guided node-level adaptive fusion employs the IB principle to learn independent weights for each node, facilitating the fine-grained integration of high-order information and global information to obtain an efficient representation for downstream tasks. Extensive experiments demonstrate that the proposed method outperforms current state-of-the-art methods and can identify biomarkers for clinical applications.

---


### 292. [CredWise: A Controlled Agentic Decision-Intelligence Framework for Explainable and Auditable Credit-Risk Assessment](https://arxiv.org/abs/2609.37223)

**<font color=#1a73e8>作者：</font>** Aakash Kumar Tiwari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Credit-risk prediction is important in banking, but a prediction alone does not explain why an applicant is risky or how it should be combined with other evidence. This paper presents CredWise, a decision-support framework that integrates credit-risk prediction, probability calibration, explainable artificial intelligence, policy retrieval, SQL analytics, and controlled agent-based workflows. An XGBoost model is trained on Lending Club data (1,345,310 loans, 18 features) using a temporal split: 2007--2016 for training, 2017 for validation, and 2018 for testing. On the 2018 test set, the calibrated model achieved a ROC-AUC of 0.7109, PR-AUC of 0.2993, F1-score of 0.3714, and accuracy of 65.44\%. Calibration reduced the Brier score from 0.2157 to 0.1273 and the expected calibration error from 0.2862 to 0.0585. SHAP explanations were temporally stable, with a Spearman correlation of 0.9959 between 2017 and 2018 feature rankings. On 28 labeled queries covering nine policy sections, FAISS achieved the best Hit@1 (0.929) and MRR (0.964), while all three retrieval methods reached Hit@5 = 1.0. Agent routing achieved 95.6\% accuracy (43 of 45 cases), and the SQL benchmark scored 1.0 on exact-match, execution-success, and result-match across six cases. These results show that CredWise can combine predictions, explanations, policy evidence, and structured analytics in one controlled workflow. It is an academic research prototype, and final decisions remain with a human reviewer.

---


### 293. [Interacting particle guidance for sampling reward-tilted generative priors](https://arxiv.org/abs/2609.37227)

**<font color=#1a73e8>作者：</font>** Adhithyan Kalaivanan, Zheng Zhao, Jens Sjölund 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time steering adapts pretrained diffusion and flow-based models to new tasks, e.g., to generate samples from a conditional distribution or samples with desired properties, without retraining. This can be formalized as sampling from a reward-tilted generative prior. As exact sampling from this distribution is intractable, guidance-based methods rely on approximations producing biased samples, and sequential Monte Carlo (SMC) methods correct for this bias using importance weights. However, while exact in the large particle limit, SMC suffers from weight degeneracy and particle collapse in practice. We propose interacting particle guidance (IPG), which replaces reweighting with transport. The particles interact through an additional drift, derived from the Feynman--Kac PDE to cancel the reweighting term, and remain unweighted. Choosing the drift in a reproducing kernel Hilbert space yields a closed-form solution that is cheap to compute, with negligible overhead compared to SMC. We demonstrate the method on Gaussian mixtures with known posteriors, and on high-dimensional image inpainting and protein structure inference tasks.

---


### 294. [AESOP: Asymmetric Human-Camera Generation with Translation-Intensity Control](https://arxiv.org/abs/2609.37229)

**<font color=#1a73e8>作者：</font>** Jingzhong Lin, Zhanke Wang, Heng Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human motion defines an action, while a camera trajectory determines how it is presented. Camera generation for a given human motion and joint human-camera generation are usually treated as separate tasks, although both share an asymmetric dependency: human motion can be generated independently, whereas the camera responds to the realized action. We introduce AESOP, a unified framework with an independent human pathway and a shared human-conditioned camera generator. Its asymmetric architecture serves both tasks while preserving the human output during camera generation. Although human context anchors the shot to the action and camera text describes its movement, translation intensity remains underspecified. We therefore construct trajectory pairs that differ in camera translation magnitude while sharing human motion and camera text, then use these pairs to learn an explicit intensity condition. Experiments on the PulpMotion dataset demonstrate strong camera distributional and framing quality in both tasks and effective control over camera translation intensity.

---


### 295. [Asking for What Was Never Requested: Horizontal and Vertical Proactivity in Agents](https://arxiv.org/abs/2609.37236)

**<font color=#1a73e8>作者：</font>** Ido Levy, Asaf Yehudai, Segev Shlomov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent that uses tools typically responds to what the user explicitly asks, yet completing the task may require information the user never requested. Work on proactive agents mainly studies whether and when an agent should act on its own, not what information it should pursue. We study a distinct axis of proactivity: its content. Horizontal proactivity pursues unstated information that the current context already identifies, and vertical proactivity pursues needs that only earlier evidence reveals. A need graph, recovered from a benchmark's own decomposition, records which needs depend on which, so both forms, and whether the agent stops at the right time, can be scored from a transcript without a model judge. To learn this behavior, we propose Q&D (questioner and drafter), which trains a questioner to prefer the question whose continuation retrieves more of the required evidence, with no reward model or judge. On held-out splits of three multi-hop question-answering benchmarks, at equal retrieval spend, the trained questioner improves both forms of proactivity over the same model, prompted, and outperforms a prompted model $15\times$ larger in the same role on two of the three, and the gain persists after controlling for question volume and length. Without further training, we place the questioner in an interactive customer-service agent with a simulated customer, where it completes more tasks while asking fewer questions, and in retail it outperforms the $15\times$ larger model with fewer follow-up turns from the customer. These results show that proactivity depends not only on whether an agent acts without being asked, but also on what it chooses to pursue and when it stops.

---


### 296. [Differentiating Bisimulation Metrics: A Framework for Parametric Markov Chain Fitting via Bicausal Optimal Transport](https://arxiv.org/abs/2609.37239)

**<font color=#1a73e8>作者：</font>** Sergio Calo, Amy Zhang, Javier Segovia-Aguas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many problems in sequential decision-making, such as imitation learning from observations, state-space compression, world-model learning, and sim-to-real transfer, can be reduced to learning a model such that a notion of distance with respect to the target process is minimized. We consider this general framework and consider the bisimulation metric, equivalently Bicausal Optimal Transport (BOT), as the notion of distance to minimize. We show that BOT, since it can be formulated as a linear program (LP), is differentiable with respect to the model dynamics. We then derive an exact closed-form gradient via the envelope theorem applied to the LP saddle point. The result is a general algorithm, Differentiable Bicausal Optimal Transport (D-BOT), that can be applied to each of the problems above. The proposed algorithm learns the best model by alternating between distance computation and gradient steps. We apply D-BOT for three different settings: state-space compression, parametric model learning, and imitation learning from observations (ILfO). We show empirical results that confirm the viability of all three instantiations.

---


### 297. [Codebook-Guided Cross-Modal Knowledge Distillation for Structurally Heterogeneous Features](https://arxiv.org/abs/2609.37243)

**<font color=#1a73e8>作者：</font>** Dae Ung Jo, Jongin Lim, YoungJoon Yoo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal knowledge distillation transfers knowledge from a teacher modality to a student modality. Existing feature-level alignment methods typically assume that teacher and student features reside in structurally alignable representation spaces. However, this assumption does not hold when cross-modal features are structurally heterogeneous and lack clear unit-level correspondence, such as 2D spatial visual grids and 1D temporal audio sequences, thereby limiting the applicability of feature-level alignment. To address this challenge, we propose a cross-modal distillation framework that enables effective knowledge transfer across structurally heterogeneous feature spaces via a vector-quantized codebook. Specifically, teacher features are abstracted into a set of vector-form codes regardless of their original feature structure, and the selected codes serve as concept-level anchors for student learning. Code selection is guided by both task relevance and student compatibility, allowing the student to receive transferable teacher knowledge without requiring direct unit-level feature alignment. Experimental results across diverse cross-modal distillation scenarios demonstrate the effectiveness of the proposed framework on classification and semantic segmentation tasks.

---


### 298. [V-JEPA Policy: Building Effective World-Action Models on Predictive Visual Latents](https://arxiv.org/abs/2609.37250)

**<font color=#1a73e8>作者：</font>** Yang Zhang, Jiangyuan Zhao, Chenyou Fan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-action models (WAMs) couple future visual-state prediction with action generation. By adapting video generators or image-editing models pretrained at scale, a prominent line of recent WAMs inherits both predictive knowledge and the models in which it was learned. We ask whether a predictive visual latent space induced by large-scale predictive pretraining can instead provide a sufficient foundation for effective WAM learning without inheriting a complete pretrained visual generative model. To answer this question, we introduce V-JEPA Policy, a simple framework that builds a WAM on the latent space of a frozen V-JEPA 2.1 encoder. An instruction-conditioned future-latent predictor and a flow-matching action expert are jointly learned from scratch in a single downstream stage, with the predictor's future-informed context key--value states conditioning action generation. With 0.9B total parameters, of which 0.6B are trainable, V-JEPA Policy achieves competitive performance with representative WAM and vision-language-action baselines across LIBERO, LIBERO-Plus, and RoboCasa-GR1. Comparing visual foundations under the same downstream framework and training budget identifies V-JEPA latents as more effective than the discriminative, reconstructive, and video-understanding-oriented alternatives, particularly under distribution shifts. Beyond task-specific learning, pretraining the predictor on DROID video--instruction pairs without action labels and adapting it into a WAM yields substantial gains in downstream control and out-of-distribution generalization. Together, these findings establish predictive visual latents as a foundation for effective WAM learning from task-specific demonstrations and for transferring future-modeling knowledge acquired from broader in-the-wild videos. Our code is available at this https URL.

---


### 299. [Collision-Aware and Observation-Aligned Object-Centric Scene Reconstruction from Point Cloud](https://arxiv.org/abs/2609.37260)

**<font color=#1a73e8>作者：</font>** Yuxuan Xie, Xuan Yu, Rong Xiong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-centric scene reconstruction requires completing partial object observations while preserving metric alignment and avoiding collisions with the surrounding. Existing generation-based methods are often image-conditioned and suffer from scale ambiguity and insufficient geometric constraints. We propose COOL, a framework for COllision-aware and Observation-aLigned reconstruction. Based on an object generation model, COOL conditions the generation on instance and background point clouds. Instance geometry anchors generation in scene coordinates, while background geometry provides local context for scene-consistent completion. We further introduce an explicit collision loss and use joint optimization and resampling to reduce collisions during inference. Experiments on 3D-Front and Scan2CAD demonstrate strong scene-level fidelity, observation alignment, and collision reduction. Moreover, additional studies validate its robustness to mask errors and its applicability to real-world scene replicas.

---


### 300. [Task-Relevant Null-Space Residuals for Non-Injective Neural Mappings](https://arxiv.org/abs/2609.37272)

**<font color=#1a73e8>作者：</font>** Bizu Feng, Zhimu Yang, Shuming Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Non-injective mappings in neural networks map distinct inputs to the same representation, thereby implicitly inducing equivalence relations in the input space. However, the input differences eliminated by these mappings may still be required by downstream tasks, creating a mismatch between operator-induced indistinguishability and task-required distinctions. For non-injective linear operators realized in the current forward pass, their null spaces exactly characterize these invisible input variations. We propose Task-Relevant Null-Space Residuals (NSR), a general residual framework for non-injective linear mappings. NSR combines null-space component extraction from pre-mapping representations, member-level encoding and gating, and application-specific integration to exploit potentially task-relevant information under downstream supervision while preserving the original aggregation or merging rules. We evaluate NSR in two structurally different settings: token merging and graph aggregation. In token merging, NSR achieves higher semantic segmentation performance than the corresponding compressed baselines in 34 out of 36 evaluated configurations, with a maximum observed gain of 31.51 mIoU points under strong compression. In graph aggregation, NSR achieves 100% training accuracy on Tree-NeighborsMatch at depths d=2--6 across three backbones, alongside gains on heterophilic node classification and molecular graph regression. Together, these results support null-space residuals as a practical complement to non-injective linear mappings, enabling downstream models to learn from input distinctions invisible in the original operator's output.

---


> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-447](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

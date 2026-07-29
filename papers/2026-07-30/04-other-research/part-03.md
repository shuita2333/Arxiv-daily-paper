# 📦 其他研究 | 2026年07月30日

> 本类共 **229** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-229](./part-05.md)

---

### 101. [Balanced Soft mixture-of-expert model for Glaucoma Detection](https://arxiv.org/abs/2607.25324)

**<font color=#1a73e8>作者：</font>** Sai Venkatesh Chilukoti, Krishna Rauniyar, Min Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Glaucoma is a group of eye diseases that damage the optic nerve, often caused by elevated intraocular pressure. It is a leading cause of irreversible vision loss and is typically developed slowly and painlessly, making it difficult to notice until significant damage has occurred. Therefore, early detection is crucial to prevent or slow the progression of vision loss. In recent years, deep learning based uni-modal models have improved the accuracy and efficiency of glaucoma detection, empowering doctors with tools for earlier diagnosis, better monitoring, and timely treatment. Building on this, multi-modal models have emerged, leveraging the strengths of different imaging modalities to learn richer and more robust representations, further enhancing glaucoma detection accuracy. However, multi-modal learning faces challenges such as imbalanced and under-optimized uni-modal representations due to joint learning objectives. To address this, we propose a balanced soft mixture-experts model with three experts and load balancing loss. The performance is measured by AUC, our proposed method surpasses the performance of all uni-modal baselines, conventional multi-modal models, and current stateof- the-art balanced multi-modal models. The proposed model can be generalized to other disease detections such as diabetic retinopathy.

---


### 102. [Every Time I Hire a Linguist, Inference Costs Go Down: On Linguistic Rules as Effective Prompt Compressors](https://arxiv.org/abs/2607.25335)

**<font color=#1a73e8>作者：</font>** Jianfei Ma, Zhaoxin Feng, Emmanuele Chersoni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt compression shortens LLM input to reduce inference cost, yet existing methods score token importance through LM forward passes. It remains questionable whether such nuanced, costly token selection is necessary. Compression requires identifying informative content, a problem that linguistic research has long addressed through cues that can be operationalized as deterministic rules. We therefore ask: can \textbf{linguistic rules alone} serve as effective prompt compressors, without LM-based scoring at compression time?
To address this, we conduct offline evolutionary search over lexical, syntactic, semantic, and discourse seeds to find competitive rule combinations. The resulting linguistic compressor requires no LM forward pass at deployment and uses only CPU-side processing for compression. We evaluate it with a dual-path protocol to balance compression quality and reconstruction fidelity.
Across short passages, multi-document reasoning, and dialogue-memory QA datasets, evolved compressors achieve performance similar to that of recent advanced prompt-compression strategies. Performance is strongest under light-to-moderate compression and degrades as compression becomes more aggressive, while the Direct and Reconstruction paths exhibit distinct patterns. Evolutionary analysis reveals that effective compression fuses signals across linguistic levels and, as the compression ratio increases, rules shift from token pruning to sentence extraction.

---


### 103. [Dual-Domain Manifold Modeling for Hyperspectral Image Fusion](https://arxiv.org/abs/2607.25338)

**<font color=#1a73e8>作者：</font>** Chengxin Xie, Qiya Song, Yangbangyan Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Achieving a coherent integration of spectral richness and spatial fidelity remains a central objective in hyperspectral image fusion. However, existing hyperspectral image fusion methods struggle to effectively model geometric constraints. In the spatial domain, weak spatial-spectral interaction limits geometry-aware feature learning and suppresses high-frequency structural information, resulting in low-frequency bias and structural degradation. In the spectral domain, local manifold structures induced by spectral similarity are insufficiently exploited, limiting intrinsic pixel relationship modeling and fine-grained spectral reconstruction. To address these challenges, we propose a dual-domain manifold modeling (DDMM) framework. Specifically, we introduce a Topology-Aware Transformer (TPFormer) that combines global attention with neighborhood propagation, jointly modeling spatial topology and pixel-level feature manifold relationships to capture intrinsic spatial-spectral structures and improve topology-aware representation learning. Furthermore, a Frequency-Decoupled Spatial-Spectral Collaborative Fusion (FDSCF) module is devised, in which features are projected into the frequency domain via the discrete cosine transform and explicitly decoupled into low- and high-frequency components. Guided by a low-rank structural prior and spectral-driven spatial enhancement, FDSCF selectively enhances geometry-aware high-frequency features, strengthening spatia-spectral coupling and recovering sharper edges and finer textures. Extensive experiments on multiple benchmark datasets demonstrate that DDMM achieves superior overall performance over SoTA methods in terms of spatial structure preservation and spectral reconstruction.

---


### 104. [Explainable AI for Chronic Kidney Disease Prediction Using Simulated Federated Learning](https://arxiv.org/abs/2607.25348)

**<font color=#1a73e8>作者：</font>** Md Zahid Hasan Ontor, Md Al Amin, Anik Dev Nath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chronic Kidney Disease (CKD), characterized by the gradual loss of kidney function, remains a significant public health challenge. Early detection is crucial for preventing severe complications and enhancing patient outcomes. In this study, Federated Learning (FL) with a VotingClassifier was used to predict CKD using a clinical dataset, where Random Forest, AdaBoost, and XGBoost were utilized to compare and identify the best-fitting model for the global server. Additionally, GridSearchCV was applied to optimize the models' performance on the client's side. To enhance model transparency and trustworthiness, explainable AI (XAI) techniques were incorporated to interpret the prediction mechanisms. The global model's average accuracy was 99%, highlighting the potential of interpretable FL models in supporting early CKD diagnosis and advancing data-driven healthcare solutions.

---


### 105. [Raven: High-Recall Sequence Modeling with Sparse Memory Routing](https://arxiv.org/abs/2607.25357)

**<font color=#1a73e8>作者：</font>** Arshia Afzal, Aviv Bick, Eric P. Xing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context recall in linear-time sequence models highlights a tradeoff in how they write to memory. State-based linear models, such as state-space models (SSMs) and linear Transformers, write densely, updating the entire state for each newly arrived token, which leads to interference and makes specific past tokens hard to recover. Sliding-window attention (SWA) exhibits the opposite behavior: it writes sparsely by storing explicit token representations, but only within a fixed window, so recall drops once the relevant token is evicted. Interpolating between these models, we introduce Raven, a linear-time sequence model that maintains a fixed set of memory slots and, at each step, decays and updates only a selected subset via learned, input-dependent routing. This lets Raven mitigate SWA's position-based overwriting and hard eviction while reducing interference from dense state updates in SSMs, thereby preserving long-range content much more effectively. Across recall-intensive benchmarks, Raven is competitive with or outperforms prior linear-time baselines, achieving strong long-context recall where both SWA and SSMs sharply degrade. It remains effective when extrapolating to context lengths as large as 16x its training length, with similar gains in hybrid architectures.

---


### 106. [PanoLess: Environment Reconstruction from Partial Reflective Views](https://arxiv.org/abs/2607.25362)

**<font color=#1a73e8>作者：</font>** Ahitagni Das, Ashok Veeraraghavan, Vivek Boominathan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reflections from shiny objects and glass facades naturally extend the field of view of a camera, capturing the surrounding environment without the need to pan the camera or acquire a full panorama. We propose PanoLess, a Gaussian-splat-based framework that reconstructs the surrounding environment as a distant illumination map from images captured on only one side of a reflective surface. PanoLess leverages surface-aligned 2D Gaussian splats with deferred shading to recover accurate per-pixel normals and reflection cues, which are fused into a neural cubemap representation of the environment. In addition, PanoLess produces a visibility map that explicitly denotes which regions of the environment are supported by the partial reflective observations. Unlike existing inverse-rendering and reflection-aware Gaussian-splatting approaches, which typically require full 360-degree coverage and struggle under incomplete views, PanoLess enables consistent, physically grounded illumination estimation from partial-view input. We show that PanoLess achieves high-fidelity and geometrically consistent environment reconstruction, outperforming reflection-aware baselines on a new custom synthetic benchmark and publicly available datasets, and demonstrating generalization to real-world reflective captures.

---


### 107. [Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales](https://arxiv.org/abs/2607.25364)

**<font color=#1a73e8>作者：</font>** Genliang Zhu, Chu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using agents expose structured calls but commonly attach free-form rationales. Such rationales are neither authorization nor reliable introspection. We present Explanation-Bound Tool Execution (EBTE), a claim-carrying mediation layer that converts decision-relevant rationale content into typed action claims and checks them against server-held intent, policy, payload, tool, risk, provenance, and freshness facts. EBTE cannot widen baseline authority: conflicts deny, incomplete or uncertain claims review, and only matching claims remain eligible for governed execution. We formalize this composition under explicit mediation and trusted-fact assumptions and implement a versioned reference profile with minimized audit packets. Across 136 authored conformance scenarios, the full profile matches all specified dispositions, admits none of 96 designated hard contradictions, and passes 232 metamorphic checks; these results validate the included profile rather than population performance. A draft-only reference integration forwards none of 48 authored hard cases under EBTE while preserving all 16 soft-review and 4 aligned draft paths. In a frozen 2026-07-12 exploratory 224-attempt hosted-model record, the historical generation/runner agreement counts are 71/96, 66/96, and 19/32; a separately labeled zero-call post-hoc revalidation of the preserved minimized claims under the current pipeline yields 70/96, 65/96, and 17/32. In an AgentDojo-derived semantic check, existing high-risk controls already make all 12 attack proposals non-allow; EBTE additionally resolves them as deny. These results support the feasibility and diagnostic value of server-checked action claims, not rationale faithfulness, human-review benefit, representative attack resistance, or production safety.

---


### 108. [Leak-Free Cross-Validated Stacking with Per-Architecture Calibration for Sand-Boil Segmentation in Earthen Levees](https://arxiv.org/abs/2607.25367)

**<font color=#1a73e8>作者：</font>** Padam Jung Thapa, Anav Katwal, Ayon Dey 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sand boils, points where water seeping beneath an earthen levee re-emerges at the surface, are early warnings of internal erosion, and deep segmentation networks are increasingly used to find them in inspection photographs. Annotated examples are scarce, and two common ways of working around that scarcity quietly inflate reported accuracy: tuning ensemble weights on the same images later used to score them, and training on synthetic images derived from the very photographs held out for testing. We present a sand-boil segmentation framework that closes both loopholes. Every synthetic image carries a pointer to its real parent, and a per-fold filter excludes any image whose parent is held out; five encoder-decoder backbones are trained under five-fold cross-validation, calibrated by one temperature scalar each, and combined by a per-pixel meta-learner fitted only on out-of-fold predictions. On the held-out test set the proposed Updated SandBoilNet reaches an intersection-over-union of 0.707 over three seeds, against 0.608 for the published original re-evaluated on the same split. Under the stacking protocol the calibrated stack reaches 0.681 against 0.694 for the strongest fold-averaged member, so it does not improve on the best single model; eight meta-learner families reproduce that outcome, which we trace to a mean pairwise error correlation of 0.894 among members. A synthetic pool filtered for label fidelity lifts the champion to 0.718 over three seeds against a 0.707 control. We also introduce a mask-conditioned synthesis route that makes the conditioning mask the label by construction, giving labelled training images at zero annotation cost.

---


### 109. [AI Deployment and Cyber Governance Failures in Public-Sector Organizations: A Typological Analysis](https://arxiv.org/abs/2607.25368)

**<font color=#1a73e8>作者：</font>** Md Salahuddin, James Rooney, Fida Hasan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The intersection of artificial intelligence adoption, cybersecurity governance, and public sector institutional constraints has not been examined as a unified analytical problem in the existing literature. Studies address AI cybersecurity risks generically, public sector governance independently, and framework adequacy separately. Existing studies have not integrated these three streams to explain specifically how AI adoption causes cybersecurity governance failure in government organizations, nor test existing governance instruments against AI-specific public sector failure causes. This paper ad-dresses that gap. It proposes a seven-domain typology identifying ten specific AI-driven cyber governance failure causes grounded in public sector institutional analysis. It presents a three-pathway failure model showing how accountability failure, opera-tional resilience failure, and compliance failure interact and reinforce each other. It de-livers a structured coverage matrix testing five major governance frameworks (NIST CSF 2.0, ISO/IEC 27001, COBIT, NIST AI RMF, and ISO/IEC 42001) against the typology, finding that no instrument addresses Shadow AI, speed asymmetry, or gov-ernance vacuum at the operational specificity required for public sector application. The paper introduces speed asymmetry as a named structural construct with a specified mechanism. The framework provides the design specification for an AI-enabled cyber-security maturity model for government organizations.

---


### 110. [Hyperspectral Intrinsic Decomposition: Joint Recovery of Reflectance and Photometric Components for Non-Lambertian Scenes](https://arxiv.org/abs/2607.25371)

**<font color=#1a73e8>作者：</font>** Hao Ye, Zhan Shi, Chenglong Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral intrinsic decomposition (HID) aims to disentangle material-related spectral properties and photometric effects in hyperspectral images (HSIs), which is essential for understanding real-world imaging processes and benefits a variety of downstream applications. Most existing HID studies have been developed under Lambertian or near-Lambertian assumptions. The few prior non-Lambertian efforts rely on simplified specular assumptions insufficient to handle diverse real-world specularity, and typically require auxiliary inputs or recover only a subset of the coupled reflectance and photometric components, hindering complete and blind decomposition. In this paper, we revisit the dichromatic reflection model (DRM) and develop a unified inversion paradigm that reformulates the recovery of four coupled reflectance and photometric components as the estimation of two spectral--spatial target variables. Building on this reformulation, we propose a dual-scale decomposition scheme to handle non-Lambertian effects with distinct spatial characteristics. At the global scale, photometrically invariant descriptors serve as edge priors for high-fidelity intrinsic boundary preservation; at the local scale, specularity-guided attention directs refinement with emphasis on specularity-dominated regions, including those affected by clipping distortion. To facilitate future research, we establish CITE, the first public real-world HID dataset for non-Lambertian objects, and develop a Physically-faithful Intrinsic Set Generator (PISG) for controllable data synthesis. Extensive ablation studies and experiments on the CITE and additional HSIs demonstrate the effectiveness of our method and its robustness across diverse scenes.

---


### 111. [Rethinking Likelihood distributions: Student's t Likelihood Boosts Bayesian Neural Network Performance](https://arxiv.org/abs/2607.25376)

**<font color=#1a73e8>作者：</font>** Pei-Hsuan Hsia, Lars H. Heyen, Arvid Weyrauch 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In Bayesian neural networks (BNNs), variational inference is a widely adopted framework for modeling uncertainty in a distributional way, with the evidence lower bound (ELBO) serving as the standard objective function. Several distributions contribute to the ELBO loss, such as the prior, approximated posterior, and likelihood distribution. Typically, these distributions are all approximated by a Gaussian distribution, since it is easy to compute, allows for reparameterized gradients, and provides a closed-form loss for training. However, several works have highlighted that this assumption may not generally hold, posing the risk of model misspecification. Alternative distributions have been proposed for the prior specifically, while the effect of distribution choice on the likelihood distribution remains unexplored. In this work, our aim is to close this gap by investigating whether alternative assumptions for the likelihood distribution can outperform the commonly used Gaussian. We compare several likelihood distribution assumptions, such as skewed or heavy-tailed, across regression tasks on both artificial and real-world datasets using standard multilayer perceptrons (MLPs). Our findings demonstrate that Student's t yields better predictive performance than a Gaussian likelihood distribution, independent of the data distribution and MLP architecture (depth and width). In some cases, Student's t can also lead to shorter training times, while still being easy to implement.

---


### 112. [Gaussian Volumetric Representation for Efficient Shear-Warp Visualization](https://arxiv.org/abs/2607.25377)

**<font color=#1a73e8>作者：</font>** Mayuri Mathur, Ojaswa Sharma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image visualization requires volumetric rendering algorithms that preserve anatomical fidelity while maintaining high rendering speeds. To address the high computational cost of large volumetric datasets, we propose a Gaussian-based volumetric representation for efficient visualization of dense medical volumes without compromising structural and radiometric details. We optimize the proposed representation using Monte Carlo volumetric estimation, which enables training on a highly sparse subset of voxels while maintaining consistency with the dense volumetric objective. In addition, we introduce a curriculum learning strategy that progressively incorporates structured slice-based sampling during training. Sparse voxel samples provide an early global coverage of the volume, while slice samples capture spatially correlated regions that aid geometric structure and texture continuity. This combination enables the Gaussian representation to learn anatomical details of various structures and corresponding textures from sparse supervision while significantly reducing the computational cost associated with dense voxel processing. The learned representation supports slice-based rendering methods such as shear-warp volume rendering, enabling efficient visualization of multimodal medical datasets including MRI and Cryosection volumes while preserving anatomical structures. Using sparse supervision, our method achieves up to 43.86 FPS rendering with a compression ratio of 11.31:1.

---


### 113. [Cyber-Capable AI Agents: Vulnerabilities, Evaluation Containment, and Defensive Response](https://arxiv.org/abs/2607.25379)

**<font color=#1a73e8>作者：</font>** Abu Bakar Siddik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cyber-capable AI agents combine language models with tools, memory, and execution en- vironments to perform multi-step offensive-security tasks. Existing work separately measures cyber capability and catalogs attacks against agent components, but provides less guidance on containing a capable agent within the environments used to evaluate it. This review synthe- sizes five vulnerability classes at that boundary: multi-step offensive chains, objectives that conflict with sandbox boundaries, supply-chain and credential exposure, persistent command- and-control, and the speed of automated action. We use the reported July 2026 Hugging Face/OpenAI incident as a bounded case study, distinguishing incident-specific observations from findings established in the wider literature. Across the taxonomy and case, we examine controls for containment, privilege separation, provenance, and responder access, including the dual-use problem that defensive artifacts may also enable misuse. The review identifies practical priorities for evaluating cyber capability together with the security of the environment in which that capability is exercised.

---


### 114. [TailVis: Expressive Chart Refinement Preserving Data-Binding Integrity](https://arxiv.org/abs/2607.25386)

**<font color=#1a73e8>作者：</font>** Yumin Song, Seokhyeon Park, Soohyun Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Creating static visualizations for presentations and publications requires granular refinements of visual details, even for simple charts. Existing data-driven visualization tools offer limited interactive control for such refinements, forcing users to export charts to external graphic editors and breaking the critical link between data and visual representation. To address this gap, we propose an extended InfoVis Reference Model to account for post-render design refinement. A formative study with 18 visualization practitioners and a follow-up survey of 35 respondents confirmed that this stage is pervasive yet unsupported in current practice. Based on these findings, we present TailVis, a visualization authoring system that enables expressive visual customization while preserving data-binding integrity. TailVis supports element-level direct selection and scope expansion, allowing users to define a data-aware scope ranging from a single mark to a data-driven category with a simple selection. For modifications beyond predefined controls, TailVis blends natural language input with dynamically generated GUI widgets, where deictic interaction lets users reference elements simply by clicking them, keeping even open-ended edits bound to the data. To support rigorous exploration and comparison of design alternatives, TailVis implements a provenance history that enables users to capture diverse design iterations while ensuring data-visual integrity. A user study with 12 participants verified that TailVis effectively supports expressive, granular refinement without sacrificing data binding, significantly reducing repetitive manual processes in an integrated environment.

---


### 115. [Learned, Relied Upon, or Necessary? Separating Checkpoint Dependence from Task-Level Value in Sheaf GNNs](https://arxiv.org/abs/2607.25387)

**<font color=#1a73e8>作者：</font>** Yi Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned restriction maps in sheaf graph neural networks are often treated as proof that the model has discovered useful edge geometry. That conclusion does not follow from parameter movement or from a post-hoc ablation: both can show how one checkpoint is organized while leaving open whether learned transport still helps after the rest of the model adapts. We separate these claims with two estimands. Checkpoint reliance intervenes on the maps of a fixed predictor; protocol-relative replacement retrains matched families that remove map capacity, edge variation, or persistent edge assignment. A task-null theorem shows why the claims can diverge: labels identify only the transported classifier directions, leaving $d^2-d$ invisible degrees of freedom in every full $d\times d$ map. An exact frame model then gives the boundary at which reliance becomes unreplaced task value. Label-only training realizes the predicted separation, while audits of public NSD, DNSD, and Directed Sheaf Neural Network (DSNN) implementations recover both replaceable and unreplaced transport regimes on real graphs. All five DNSD benchmarks exhibit fixed-checkpoint reliance. After retraining, assignment-breaking or shared-map controls recover Full performance on four; Roman-Empire retains a $.0675$ advantage over continually resampled assignment and a $.0391$ advantage over a parameter-matched shared map across ten official splits. Thus, a learned map can govern a fitted computation without constituting indispensable edge geometry. Claims of learned transport should pair checkpoint interventions with matched retraining.

---


### 116. [HOME: Robust Hough-space Matching Method for Structured and Textureless Videos](https://arxiv.org/abs/2607.25389)

**<font color=#1a73e8>作者：</font>** Masaki Satoh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual front-ends for robotic localization typically rely on point-based features such as Oriented FAST and Rotated BRIEF (ORB), which frequently fail in structured environments dominated by strong linear structures or textureless surfaces. While line-based Simultaneous Localization and Mapping (SLAM) systems mitigate this by utilizing line segments, conventional line extraction and description algorithms are computationally prohibitive for real-time edge robotics. To address this fundamental bottleneck, we propose HOME (Hough-space One-dimensional Matching of Extrema), an ultra-lightweight, training-free feature matching framework. HOME transforms images into Hough space, mapping global linear structures to stable local extrema, which serve as keypoints, thereby reformulating complex line matching into highly efficient one-dimensional point matching. The proposed 1D radial descriptor mathematically guarantees rotational and translational invariance without the overhead of explicit orientation estimation. As a proof of concept to validate the matching accuracy and efficiency of HOME, this paper focuses on homography estimation. Extensive evaluations demonstrate that HOME achieves robust registration in challenging scenarios where point-based methods fail, operating at a much faster speed than existing line-based methods. Extending this robust matching engine to full 3D pose estimation remains a highly promising future direction.

---


### 117. [Noise-Free One-Step LoRA for Task-Driven Image Restoration with Diffusion Priors](https://arxiv.org/abs/2607.25390)

**<font color=#1a73e8>作者：</font>** Jaeha Kim, Kyoung Mu Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Degraded images not only reduce visual quality but also impair downstream high-level vision tasks. Task-driven image restoration (TDIR) addresses this issue by jointly optimizing restoration quality and task performance. Recent works show that pretrained diffusion priors benefit TDIR, yet diffusion-based restoration is inherently stochastic, as the sampling process depends on a random noise term, which can undermine task consistency. In this paper, we show that a deterministic, noise-free one-step forward pass with pretrained diffusion priors can substantially improve TDIR, but the benefit critically depends on the adaptation module: LoRA yields consistent gains, whereas ControlNet-style conditioning does not. This enables one-step forwarding that surpasses conventional multi-step diffusion TDIR baselines. Furthermore, we introduce a task-preserving GAN training strategy that improves perceptual quality without sacrificing task performance. Extensive experiments on classification, segmentation, and detection demonstrate consistent gains over prior TDIR methods, and we further validate generalization on real-world degraded images and OCR.

---


### 118. [RDVSv2: A Large-scale Benchmark for RGB-D Video Salient Object Detection](https://arxiv.org/abs/2607.25392)

**<font color=#1a73e8>作者：</font>** Tianyu Li, Jiahao He, Keren Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce RDVSv2, a large-scale benchmark for RGB-D video salient object detection (RGB-D VSOD) with dense frame-level annotations. Existing datasets in this emerging field are often limited in scale and annotation quality, while also relying on less geometry-consistent depth cues. To address these limitations, RDVSv2 is built from publicly accessible stereoscopic online videos and contains 249 video sequences with 29,077 annotated frames. It includes depth maps derived from stereoscopic videos, together with frame-wise salient object masks annotated with eye-tracking guidance. Compared with existing datasets, RDVSv2 is much larger in scale and covers more diverse and challenging scenarios. In addition, we establish a strong baseline for RGB-D VSOD based on Segment Anything Model 2 (SAM2). Specifically, we employ a parameter-efficient fine-tuning (PEFT) strategy to adapt the SAM2 encoder to jointly encode RGB, depth, and optical flow cues. Extensive experiments show that RDVSv2 is substantially more challenging for existing RGB-D VSOD methods. Meanwhile, the proposed baseline achieves state-of-the-art results on RDVSv2 and existing RGB-D VSOD benchmarks. We hope that RDVSv2 and the provided baseline will serve as useful resources for future research on RGB-D VSOD and related multi-modal video understanding tasks. Our dataset and code will be available at this https URL.

---


### 119. [TWICE: Two-Clock, Two-Window Learning for Long-Horizon Conversion Prediction in Online Advertising](https://arxiv.org/abs/2607.25404)

**<font color=#1a73e8>作者：</font>** Kaiyuan Li, Kun Wang, Zhongbo Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon conversion prediction under delayed feedback creates a two-clock, two-window learning problem in online advertising. A short base observation window releases recent clicks on the click clock before their outcomes mature, whereas conversions continue to arrive on the conversion clock throughout a longer target conversion window. The click clock provides timely but partially observed status supervision. The conversion clock reveals long-tail delays, but the delay composition within an arrival-time slice is weighted by historical click cohorts with different traffic volumes and target-window conversion rates.
We present TWICE, a framework that factorizes long-horizon post-click conversion rate (CVR) into a target-window conversion probability and a grouped elapsed-delay cumulative distribution function (CDF). The two clocks provide complementary supervision. Click-clock records train the target-window CVR head through a current-status likelihood over the base observation window. Newly arrived conversions train the delay model on the conversion clock. To account for the cohort mixture, TWICE uses fixed click-time predicted CVR (pCVR) mass as cohort exposure in an arrival-conditioned likelihood. This accounts for differences in cohort traffic and conversion propensity. The resulting aggregate records are self-contained. A single learned CDF produces monotone predictions for all requested horizons up to the target conversion window. Serving requires neither historical lookup nor convolution. Experiments on a public benchmark and an industrial advertising dataset demonstrate the effectiveness of TWICE. In an online A/B test in Kwai's advertising system, TWICE increased expected revenue, revenue, and conversions by 2.486%, 1.858%, and 2.061%, respectively. It was subsequently deployed to full traffic.

---


### 120. [ANFI: Rethinking Neighbor Feature Interaction in Person Re-ID](https://arxiv.org/abs/2607.25407)

**<font color=#1a73e8>作者：</font>** Xulin Li, Yan Lu, Bin Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In person re-identification, neighbor-based methods have achieved significant success by interacting with neighbor samples to obtain more robust representations. However, existing methods rely only on affinity relations, causing their success to depend heavily on the reliability of selected neighbors. We find that affinity-only interaction often fails in challenging scenarios due to the inevitable presence of noisy neighbors. To enable effective interactions under noisy neighborhoods, we revisit neighbor-based methods under distinct reliability conditions and propose a novel Adaptive Neighbor Feature Interaction (ANFI) method. The core idea of ANFI is to account for negative effects from noisy neighbors, allowing samples to remain distinguishable from false positive neighbors. Unlike existing methods, ANFI models not only affinity relations but also discrepancy relations, and employs sample-wise adaptive weighting for these two types of relations. Given that capturing negative effects from noisy neighbors differs significantly from traditional relation learning, we derive discrepancy relations from a new neighborhood similarity, which provides more information than pairwise similarity. In addition, we propose Noisy Relation Supervision (NRS) to train ANFI, gradually injecting robustness to noisy relations into the model. Extensive experiments conducted under standard, cross-modal, and cross-domain settings, including comparisons with neighbor-based methods and re-ranking methods, demonstrate the superiority of our method across various neighbor distributions.

---


### 121. [SPARC Segmentation to Prediction via Affine Regression and Counterfactuals](https://arxiv.org/abs/2607.25413)

**<font color=#1a73e8>作者：</font>** Shivani, Subhayan Roy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transaction propensity prediction in B2B e commerce presents unique challenges distinct from B2C contexts, primarily due to the heterogeneous procurement behaviors of organizational entities, which violate SMOTE's implicit assumption of within class feature homogeneity. Specifically, B2B buyers exhibit multi modal procurement cycles that render linear interpolation between minority class samples structurally invalid, producing synthetic data that does not represent real purchasing behavior. This paper introduces a production deployed propensity modeling framework designed to address these complexities through two primary contributions. First, we replace conventional SMOTE based augmentation with a synthetic data generation approach leveraging Diverse Counterfactual Explanations (DiCE). This method produces minority class samples with superior distributional fidelity compared to SMOTE, as validated through quantitative proximity analysis and UMAP cluster visualization. Second, we adapt the PyPARC piecewise affine classification framework to generate calibrated propensity probabilities, facilitating the interpretable segmentation of customers into actionable risk tiers. Evaluated on two years of longitudinal data from a large scale B2B e commerce platform with a 1 to 9 class imbalance ratio, the proposed architecture achieves 93.1% precision at a decision threshold of 0.8, a 9.2 percentage point improvement over SMOTE based baselines at the same threshold (83.9%), and a 26.1 point improvement over SMOTE at threshold 0.7 (66.04%), demonstrating consistent superiority across operating points. These results demonstrate the framework's efficacy in enabling high precision marketing campaigns with significant improvements in customer activation and return on investment.

---


### 122. [From Dyad to Triad: Eliciting XAI Requirements in Stroke Rehabilitation](https://arxiv.org/abs/2607.25423)

**<font color=#1a73e8>作者：</font>** Param Rajpura, Yogesh Kumar Meena  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Eliciting explainable AI (XAI) requirements from stroke survivors presents a methodological challenge with direct implications for the design of trustworthy brain-computer interfaces for rehabilitation. How can patients and caregivers articulate preferences about algorithmic transparency when they lack conceptual frameworks for explainability, and when standard elicitation approaches are structurally inadequate for users with acquired communication disorders? We present a video-based scaffolding protocol for XAI requirements elicitation, developed and piloted in a rehabilitation context. In a formative study with three stroke survivors (two with moderate-to-severe aphasia) and three caregivers, facilitators employed four scaffolding approaches alongside the videos: 1) analogical bridging mapping AI states to familiar systems, 2) projective personas depersonalising sensitive topics, 3) binary forcing reducing cognitive load, and 4) extended response time. These approaches successfully surfaced heterogeneous, sometimes conflicting XAI needs across participants. Reflexive analysis additionally revealed three systematic facilitation biases, namely, normative bias, hypothesis confirmation bias, and presence effect, where scaffolding inadvertently shaped responses. We present these as protocol risk guidelines for practitioners. Together, the protocol and guidelines constitute a reusable methodological contribution for eliciting patient-facing XAI requirements in rehabilitation, arguing that such elicitation is a necessary prerequisite for trustworthy human-machine systems design, not an optional preliminary.

---


### 123. [SafeStats: Efficient 2PC Protocols for Data Statistic-Related Functions](https://arxiv.org/abs/2607.25430)

**<font color=#1a73e8>作者：</font>** Tanren Liu, Xianjia Meng, Yang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Statistical analysis on sensitive datasets like medical records and financial transactions is essential for decision-making, but raises significant privacy concerns. While existing secure Two-Party Computation (2PC) makes extensive efforts in designing the common secure primitives (e.g., addition and multiplication) or machine learning-related functions, few pay attention to the statistical functions. In this paper, we propose SafeStats, a secure toolkit tailored for 2PC secure statistical analysis. Specifically, to develop SafeStats, we first refer to Microsoft Excel's statistical library and summarize that most statistical operations can be achieved with three core functions:1) frequency counting, 2) sorting, and 3) non-linear math functions. Then, for each core statistical function, SafeStats presents an efficient 2PC implementation. For secure frequency counting, SafeStats adopts a secure shift-based strategy to avoid invoking expensive 2PC equality test protocols. For secure sort, SafeStats involves a secure segment-indicator protocol to achieve secure counting-based sort, which enables fast element sorting over specific statistical scenarios without the need for secure comparison. For non-linear math functions, we enhance the current reduce-then-approximate paradigm by introducing a bisection-based range reduction protocol. Finally, we implement SafeStats and test it on 14 common statistical analysis cases. As an example, for the chi-square test, SafeStats achieves a 1.5 $\times$ runtime speedup and a 4.2 $\times$ reduction in communication compared to directly using the current general-purpose 2PC library to realize it.

---


### 124. [Bi-Level Collaborative Learning for Few-Shot Scribble-Supervised Medical Image Segmentation](https://arxiv.org/abs/2607.25432)

**<font color=#1a73e8>作者：</font>** Xiang-Xiang Su, Yufan Ye, Yihang Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scribble annotations offer an efficient alternative to costly pixel-wise labeling for medical image segmentation, yet in real clinical scenarios, scribble-annotated samples are often still limited, imposing the dual challenges of sparse supervision and annotated sample scarcity. These compounded constraints severely deprive models of the structural evidence needed for complete region recovery and precise boundary delineation. To break this bottleneck, we propose a bi-level collaborative learning framework for few-shot scribble-supervised medical image segmentation. Specifically, an upper-level learnable superpixel model is introduced to provide region-structural priors for lower-level segmentation, while superpixel-based region-wise pseudo-label propagation and a spatial-prior-guided filtering strategy are performed to generate reliable dense pseudo-labels for segmentation learning. Meanwhile, the anatomical semantics learned by the lower-level segmentation model under the guidance of the current superpixels are fed back to the upper level, further driving it to learn region-structural representations better aligned with the segmentation task. Through bidirectional interaction and collaborative learning between the upper and lower levels, the proposed framework significantly outperforms existing state-of-the-art scribble-supervised methods on the ACDC and Prostate datasets under the few-shot scribble-supervised setting.

---


### 125. [PIcsC: Partitioning-Induced Covariate Shift Correction](https://arxiv.org/abs/2607.25441)

**<font color=#1a73e8>作者：</font>** Behraj Khan, Behroz Mirza, Syed Ahmad Chan Bukhari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Covariate shift across training-data partitions biases model selection and parameter estimation in cross-validation, lifelong learning, and federated learning. We propose \textit{Partition-Induced Covariate-shift Correction} (\texttt{PIcsC}), a Fisher information-based regularization framework that mitigates distribution mismatch between data partitions and a reference distribution. \texttt{PIcsC} approximates partition divergence using the Fisher Information Matrix (FIM) and incorporates the resulting statistic as a regularizer during optimization. The same formulation applies to both centrally partitioned datasets (batches or cross-validation folds) and inherently distributed data (federated clients or decentralized nodes), requiring only partition-local gradient statistics rather than raw data. We further introduce a conditional adaptation mechanism that combines FIM shift with KL divergence to detect significant distribution shifts and activates regularization only when necessary. Experiments on more than 40 datasets demonstrate consistent improvements under both natural and synthetic covariate shift. On fragmented batch and fold settings, \texttt{PIcsC} reduces fragmentation-induced performance degradation by more than 20\% and 25\%, respectively. On seven federated learning benchmarks, it consistently outperforms FedAvg, FedProx, and SCAFFOLD by 3 -5 percentage points without requiring client-specific personalization. These results demonstrate that Fisher information provides an effective and unified mechanism for mitigating partition-induced covariate shift across both centralized and distributed learning.

---


### 126. [Reading Legends on Ancient Coins: An Object Detection Approach for Character Recognition on a Novel Roman Republican Dataset](https://arxiv.org/abs/2607.25455)

**<font color=#1a73e8>作者：</font>** Hafeez Anwar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When it comes to the proper classification of ancient coins with respect to their time and issuer, the textual inscriptions on these coins, also known as legends, are of paramount importance. These legends consist of alphabets or characters still used in English. This paper addresses image based character recognition on ancient Roman Republican coins via a deep learning based object detection strategy. However, legends on these coins pose high variation due to non-uniform placement, primitive inscription techniques, and wear and tear. Additional challenges include inconsistent imaging conditions such as illumination, orientation, and scale. To accommodate these, we gathered a novel large-scale dataset of 5,654 Roman Republican coin images, manually annotated with 21 character labels, totaling 38,808 annotations. For recognition, we use You Only Look Once (YOLO) variants: YOLOv3, v4, v5, v7, and v8. YOLOv7-Large achieves the best mAP50 of 90.4%, followed by YOLOv7-Extended and YOLOv7-xl with 90.2% and 90.1%, respectively.

---


### 127. [Emergent Latent-State Computation under Stochastic Volatility](https://arxiv.org/abs/2607.25459)

**<font color=#1a73e8>作者：</font>** Xiaoyu Huang, Lulu Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability has largely focused on language models and deterministic toy tasks. Much less is known about how sequence models internally represent latent stochastic dynamics under noisy, partially observed observations. We study this question in a controlled multivariate stochastic volatility setting, where models observe only returns while the ground-truth latent volatility state is known to the researcher. This setting provides a useful benchmark for mechanistic interpretability under partial observability: the latent state is hidden from the model but directly available for evaluation. Across architectures, losses, and output heads, we find evidence for a two-stage computation. Hidden representations encode substantial information about the next latent volatility state, and the output head maps this representation to squared return forecasts. Furthermore, in Transformers, latent-state decodability emerges at identifiable architectural stages whose location depends on the volatility period. In long-cycle regimes, this computation simplifies into an explicit latent-state filter consisting of a learned linear projection followed by $\ell^2$ normalization. Output-head replacement further shows that part of the degradation under noisy MSE training arises from readout misalignment rather than representation failure. These results suggest that stochastic volatility models provide a useful benchmark for mechanistic interpretability under noisy latent dynamics and partial observability.

---


### 128. [From Profiling to Parameterization: Physics-Guided Acoustic Eavesdropping via Smartphone Accelerometers](https://arxiv.org/abs/2607.25461)

**<font color=#1a73e8>作者：</font>** Guangyuan Ji, Wenjing Wang, Bingsheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present LEAKFORGE, a device-agnostic framework that converts cross-device accelerometer eavesdropping into a physics-guided data-generation problem. Crucially, device-specific leakage is not arbitrary; its dominant variation lies within a constrained family of audio-to-accelerometer transfer functions. LEAKFORGE samples this family to synthesize large-scale, device-diverse accelerometer traces from ordinary speech, explicitly modeling electromechanical transfer, structural resonances, filtering, and aliasing. An eavesdropping model trained entirely in this synthetic domain can then be applied directly to traces from previously unseen smartphones.

---


### 129. [DensFiLM: Density-Conditioned Video Saliency for Crowd Scenes](https://arxiv.org/abs/2607.25465)

**<font color=#1a73e8>作者：</font>** Anis Ur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video saliency models typically apply a single fixation strategy across crowd scenes, despite systematic changes in attention with crowd density. Sparse scenes encourage tracking individuals, whereas dense scenes shift attention toward collective motion and scene-level landmarks. We introduce DensFiLM, a density-conditioned video saliency model that inserts a lightweight Feature-wise Linear Modulation layer at the bottleneck of a Video Swin Transformer. A learned density embedding produces channel-wise scale and shift parameters, allowing the decoder to reconstruct saliency from features selected for each density regime. The module adds only ~100K parameters and can use either CrowdFix density labels or the model's own density prediction. On CrowdFix, DensFiLM achieves mean NSS 1.434 and CC 0.517 over four seeds, improving over ACLNet by 14.7% and 14.9%, respectively, while predicted-density conditioning matches oracle-label performance. Ablations show that explicit RAFT optical flow and larger temporal and social-force extensions provide no further improvement in this setting. In a centre-prior-subtraction diagnostic, density conditioning yields an NSS gain of 0.462 over the unconditioned backbone, compared with 0.124 under standard evaluation. These results show that lightweight bottleneck conditioning provides a more effective inductive bias than increasing model capacity for crowd-video saliency. Our code is available at this https URL.

---


### 130. [Seen, Said, or Forgotten? A Causal Audit of Visual KV Memory Across Dialog Turns](https://arxiv.org/abs/2607.25467)

**<font color=#1a73e8>作者：</font>** Hong Chen, Kang Chen, Yuxuan Fan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stateful multimodal assistants encode an image once but may answer questions about it many turns later. Attention-guided visual-KV eviction assumes that evidence irrelevant now will remain dispensable, although future questions are unknown. We ask when a visual fact is actually safe to forget and introduce the Causal Visual Memory Audit (CVMA), a paired single-prefill framework that tests what later answers lose when a visual region, the whole image, or prior assistant text becomes unavailable. On VisDial and ConvBench, current attention can rank future-useful regions worse than random even though a diagnostic marginal-utility control shows substantial selection headroom. Aggregate scores hide this failure when later turns do not need vision; controlled and stock-generated histories reveal a second escape route, in which assistant-text KV replaces image KV for facts already stated but not reliably for unstated facts. In the tested stacks, safe forgetting is supported by low future visual dependence or fact-specific verbalization---not by low current attention.

---


### 131. [Safety-Aware Cascaded Inference for Crop Damage Assessment with Controlled Error Trade-offs](https://arxiv.org/abs/2607.25468)

**<font color=#1a73e8>作者：</font>** José Thiéry Messigbédé Hagbe, Gani Kawsar Gounou, Songbian Karim Zimé  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In picture-based agricultural insurance for smallholder farmers, missed damage detections carry substantially higher cost than false alarms: a farmer who sustained real losses receives no payout, while unnecessary expert review is operationally costly but reversible. Standard multi-class classifiers optimize global accuracy but provide no mechanism to operationalize or control this asymmetric cost structure at inference time. We propose CascadeCropNet, a two-stage cascade architecture calibrated to satisfy a target recall constraint (Rec-Damaged >= 0.95) through threshold selection. A lightweight Sentinel model performs binary health triage; samples exceeding a calibrated damage probability threshold tau are escalated to a specialist Expert model for fine-grained diagnosis. This design provides explicit, deployment-time control over the safety-efficiency trade-off without retraining. Evaluated on the Eyes on the Ground dataset (23,804 images from Kenyan smallholder maize farms), the cascade achieves Rec-Damaged = 0.974 at tau = 0.5, reducing missed damage cases by up to 54% relative to a flat baseline. Under evaluation alignment, the representational gap reduces to +0.008 F1-macro, confirming the contribution is architectural rather than representational. Under input degradation, the system prioritizes escalation over confident misclassification, reflecting error containment through architectural isolation rather than intrinsic model robustness. These results demonstrate that cascade architectures can operationalize safety-oriented decision constraints through calibrated routing in settings where reliability matters more than aggregate accuracy. These properties depend on threshold calibration and deployment conditions and do not constitute guarantees under arbitrary distribution shift.

---


### 132. [TRWH: A Text-Driven Random Walk Heterogeneous GNN for Semantic-Aware Sparse Recommendation](https://arxiv.org/abs/2607.25471)

**<font color=#1a73e8>作者：</font>** He Ma, Chen Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) and Large Language Models (LLMs) have each advanced recommendation systems by modeling structural and semantic signals, respectively. However, integrating their complementary strengths remains challenging, particularly in sparse settings where maintaining semantic precision is critical. We propose TRWH (Text-driven Random Walk Heterogeneous Graph Neural Network), a novel framework that fuses LLM-generated textual profiles with heterogeneous graph structures through strategic random walk augmentation. TRWH consists of three core components: (1) Embedding Creation, which produces user and item representations using both Word2Vec and LLM-based profiling; (2) a Heterogeneous Graph Neural Network (HeteroGNN) that propagates information across multi-relational edges; and (3) Random Walk-based Path Construction, which enriches sparse graphs with second-order user-user and item-item links. Experiments on the Amazon-2023 Fashion (2M users, 825K items) and Beauty (631K users, 112K items) datasets demonstrate that TRWH achieves substantial performance gains over state-of-the-art methods, including 80.0% RMSE and 52.6% MAE reductions on Fashion, and 25.7% and 10.8% improvements on Beauty. Notably, while random walks improve performance with traditional embeddings, they can dilute the nuanced representations learned by LLMs, underscoring the importance of adaptive integration strategies.

---


### 133. [Balancing multiscale similarity and cartographic constraints: A similarity-driven optimization framework for line generalization](https://arxiv.org/abs/2607.25474)

**<font color=#1a73e8>作者：</font>** Pengbo Li, Haowen Yan, Xiaomin Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cartographic generalization is essential for generating multiscale map representations by balancing information preservation and cartographic readability. However, automated generalization remains challenging because existing approaches often treat spatial similarity evaluation, cartographic constraints, and parameter optimization as separate processes, limiting adaptive and interpretable control across scales. This study formulates cartographic generalization as a constrained multiscale similarity optimization problem and proposes a similarity-driven framework for adaptive generalization control. The framework integrates multiscale spatial similarity as an optimization objective to quantify representation consistency between original and generalized data, while incorporating cartographic constraints to regulate readability, smoothness, and geometric validity. A unified objective function is optimized to automatically identify scale-dependent parameter configurations for different generalization algorithms. Experiments using multiple line simplification algorithms, target scales, and similarity measures, including geometric, structural, and learning-based metrics, demonstrate that the proposed framework achieves an effective balance between similarity preservation and cartographic abstraction. The results further show that combining similarity optimization with cartographic constraints provides more consistent and interpretable parameter control than relying on similarity evaluation alone. This study provides a unified optimization perspective that connects similarity assessment, constraint modeling, and algorithm control, contributing to adaptive and automated cartographic generalization.

---


### 134. [Data-Dependent Regret and Polyak Corrections for Constrained Online Convex Optimization](https://arxiv.org/abs/2607.25480)

**<font color=#1a73e8>作者：</font>** Wentao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constrained online convex optimization requires minimizing regret against adversarial convex costs while satisfying a convex constraint at every round, as needed in safety-critical applications. A computationally efficient method combines online gradient descent with a Polyak feasibility step, using one constraint evaluation and one subgradient per round. Although this method achieves O(sqrt(T)) regret with per-round feasibility, we derive a tighter, data-dependent analysis by retaining two quantities omitted by the standard worst-case argument. First, we replace the gradient envelope G_f^2 T with the observed accumulation G_T = sum_t ||grad f_t(x_t)||^2. Second, we identify a nonnegative Polyak correction P_T that measures the cumulative squared displacement caused by feasibility projections and enters the regret bound with a negative sign. The resulting improvement, Delta_T = (eta/2)(G_f^2 T - G_T) + P_T/(2 eta), is always nonnegative. We further propose AdaOGD-PFS, an adaptive-step-size method that achieves O(sqrt(G_T)) regret while preserving per-round feasibility. Experiments on ball- and halfspace-constrained problems improve the regret bound by 38 to 43 percent, with both data-dependent gradients and Polyak corrections contributing substantially.

---


### 135. [Finding Optimal Cost-Bounded Plan Reductions: Refined Model](https://arxiv.org/abs/2607.25484)

**<font color=#1a73e8>作者：</font>** Martha Del Toro, Raquel Fuentetaja, Angel García-Olaya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In some real applications a plan may later become unfeasible due to newly imposed budget constraints, yet, at the same time, using only the original actions of the plan and their order is mandatory. In this paper, we study the problem of extracting, from a precomputed plan, a valid subplan that maximizes utility while respecting a cost bound. Each goal is given a utility value and the plan is reduced by removing actions that support low-utility goals, while preserving both executability and the original action order. We show the decision variant is NP-complete and propose two exact methods to solve it: one via oversubscription planning (OSP) and another via Integer Linear Programming (ILP). This paper extends our previous work published at ICAPS 2026 (Del Toro, Fuentetaja, and García-Olaya 2026b). While the core framework remains as introduced there, we further introduce a refined ILP formulation that significantly decreases the model size and improves computational efficiency.

---


### 136. [CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model](https://arxiv.org/abs/2607.25487)

**<font color=#1a73e8>作者：</font>** Minhyeok Lee, Chiyoung Kim, Chanhoe Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models translate natural-language commands into robot action sequences, but leading systems on the LIBERO-Plus robustness benchmark use three- to seven-billion-parameter backbones whose memory demands can exceed embedded robotic budgets. We present CoTinyVLA, a 0.9B-parameter action model on a Qwen3.5-0.8B backbone that obtains that robustness by structuring supervision instead of enlarging the model. Three components target different axes of the problem: dual-view temporal input of 16 history frames per step with textual camera and time markers; hierarchical chain-of-thought (CoT) distillation from a 35B teacher into an episode-level Plan and a chunk-level Think span over task phase, gripper state and next subaction; and paraphrase augmentation expanding 40 base commands into 800 variants. On LIBERO-Plus, spanning 10,030 perturbed tasks across seven perturbation dimensions, CoTinyVLA reaches 90.8% on Spatial, 87.3% on Object, 86.6% on Goal and 80.7% on Long, leading the strongest 7B baseline on all four suites by 4.7, 2.8, 15.9 and 3.0 points, with every margin interval excluding zero. The gains concentrate on the hardest axes of the benchmark: across the eleven published baselines none exceeds 53.2% on Robot Initial States in any suite, whereas CoTinyVLA reaches 73.6% on Goal against 39.9% for the strongest baseline. Ablations show the three components to be separable by perturbation axis, and at a matched image budget how frames are divided between the two cameras and across time accounts for 8.6 points on its own. Closed-loop inference peaks at 2.25 GiB of allocated GPU memory, and paired interventions show the episode Plan to be load-bearing: replacing it with an empty or contradictory span costs 40 to 45 points of success. Structured supervision thus lets a 0.9B backbone exceed all of them. Code: this https URL

---


### 137. [Quantum Speedups for Stochastic Optimization with Heavy-Tailed Noise](https://arxiv.org/abs/2607.25492)

**<font color=#1a73e8>作者：</font>** Bin Luo, Chengchang Liu, Jonathan Allcock 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study stochastic optimization with heavy-tailed gradient noise. We first propose a novel quantum mean estimator for multivariate heavy-tailed random variables that achieves lower query complexity than optimal classical estimators in the low-dimensional regime. We further develop an unbiased quantum mean estimator by applying a generalized multi-level Monte Carlo technique. We prove quantum lower bounds showing that, when the dimension $d$ of the random vector is small and can be viewed as a constant, our quantum estimators are optimal up to logarithmic factors. We further derive stronger dimension-dependent lower bounds for tail index $p>4/3$, showing that a nontrivial dependence on the dimension is unavoidable in the low-dimensional regime. Based on these estimators, we propose a quantum normalized stochastic gradient descent method ($\texttt{QNSGD}$), which finds an $\epsilon$-stationary point using $\tilde{\mathcal{O}}\big(\sqrt d\,\epsilon^{-\frac{5p-4}{2p-2}}\big)$ queries to the quantum stochastic gradient oracle. For a convex objective function, we propose a quantum projected stochastic gradient descent method ($\texttt{QPSGD}$), which computes a solution with $\epsilon$-optimal solution using $\tilde{\mathcal{O}}\big(\sqrt d\,\epsilon^{-\frac{3p-2}{2p-2}}+\epsilon^{-2}\big)$ queries in expectation. These sharper bounds improve upon the classical lower bounds $\Omega\big(\epsilon^{-\frac{3p-2}{p-1}}\big)$ for nonconvex problems and $\Omega\big(\epsilon^{-\frac{p}{p-1}}\big)$ for convex problems in the low-dimensional regimes $d\lesssim\epsilon^{-\frac{p}{p-1}}$ and $d\lesssim\epsilon^{-\frac{2-p}{p-1}}$, respectively.

---


### 138. [Anti-Backdoor Coreset Selection via Cumulative Entropy](https://arxiv.org/abs/2607.25502)

**<font color=#1a73e8>作者：</font>** Qi Zhao, Christian Wressnegger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent training-time defenses against neural backdoors isolate a benign subset from poisoned training data, to learn a backdoor-free model from it. In this paper, we formulate this defense strategy as a coreset selection problem, giving rise to so-called "Anti-Backdoor Coreset Selection." Since poisonous samples have (a) lower prediction uncertainty and are (b) less frequent than benign samples, coreset selection naturally focuses more on samples associated with benign functionality than the backdoor functionality. We use the Cumulative Entropy as selection criterion to further facilitate this effect. The metric tracks the learning dynamics of training samples and allowing us to select benign samples with high informativeness for the coreset. Additionally, we unlearn the chosen samples in each epoch to facilitate the separability between benign and poisonous samples. Together, this yields an exceptionally effective training-time defense that constructs a benign coreset to train a backdoor-free model. Unlike prior defenses that compromise natural accuracy and fail against certain attacks, our method mitigates backdooring attacks consistently with a negligible impact on natural performance.

---


### 139. [Group Equivariant Diffusion for Anomaly Detection in Computational Cytology](https://arxiv.org/abs/2607.25503)

**<font color=#1a73e8>作者：</font>** Swarnadip Chatterjee, Ssharvien Kumar Sivakumar, Anirban Mukhopadhyay  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computational cytology on whole-slide images is challenging because malignant cells are rare, heterogeneous, and annotated slides are scarce. Anomaly detection frameworks can be trained on normal slide-negative patches and then applied at test time to flag abnormal patches in held-out slides. Most unsupervised anomaly detection approaches including generative ones (GAN-based and diffusion-based), are tuned to organ-level imaging and require large curated datasets. In cytology the signal is cell-centric: rotating or flipping a single-cell patch does not change its diagnostic class, yet standard diffusion models treat transformed views as distinct inputs, leading to transformation-dependent reconstructions and unstable anomaly scores. We propose a D4-equivariant diffusion framework that enforces rotation and reflection symmetry both architecturally, via a D4-equivariant U-Net, and at inference, via equivariant noise coupling and (optionally) frame averaging. This alignment with biological invariance yields transformation-consistent pseudo-healthy reconstructions and more stable anomaly ranking under symmetry. On two publicly available cytology datasets of bone marrow and peripheral blood smears, our D4-equivariant diffusion models achieve higher AUC and retrieve more abnormal cells in the top K predictions than non-equivariant generative baselines, a deep one-class, and a multiple instance learning based method, while substantially reducing score variance across rotations and flips. Code is available at this https URL.

---


### 140. [Phase Structure in Rotary Attention: A Spectral Framework for Semantic Continuity and Execution-Boundary Governance](https://arxiv.org/abs/2607.25507)

**<font color=#1a73e8>作者：</font>** Abraham Chachamovits  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer language models are usually analyzed through vector geometry, yet ordered context and rotary position encoding introduce explicit phase structure into query-key interactions. This paper develops a bounded spectral framework for examining rotary phase alignment, hidden-state continuity, and semantic drift without treating language models as literal physical wave systems. It first identifies ordered hidden-state sequences, rather than vocabulary indices, as valid domains for spectral decomposition. It then derives the Rotary Position Embedding (RoPE) attention score as a sum of magnitude-weighted cosine terms and proves a local stability lemma: uniformly bounded phase displacement limits degradation of the corresponding pre-softmax score. To extend phase analysis beyond native RoPE coordinates, the paper defines complex modal coordinates over fixed orthonormal direction pairs and introduces a weighted coherence functional for hidden-state trajectories. These constructions support a strict distinction between representational continuity and execution-boundary admissibility. Internal coherence may describe preservation of task-relevant relations, but it cannot authorize a consequential transition. Positioned against existing geometric, spectral, phase-modulation, representation-analysis, and mechanistic-interpretability accounts, the framework contributes a theoretical and methodological program for determining when spectral structure explains continuity and when governance must remain an external predicate over execution.

---


### 141. [Optimistic Verifiable Claims: A Blockchain Protocol for Conditionally Confidential Bidding in Decentralized Manufacturing](https://arxiv.org/abs/2607.25517)

**<font color=#1a73e8>作者：</font>** Marko Corn, Nejc Rožman, Primož Podržaj  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decentralized manufacturing faces a pre-contractual impasse: a Provider cannot price a service accurately without inspecting the design file, yet the Consumer cannot share that file without exposing intellectual property. We introduce the Optimistic Verifiable Claim (OVC), a blockchain protocol that lets a Consumer publish a verifiable claim about a concealed design (such as the material it consumes) and a Provider price and bid on it without seeing the design. The claim is committed when the service is posted and stands unless the selected Provider challenges it; a challenge triggers a deterministic on-chain check that exposes any dishonesty, and the design is disclosed only to settle a dispute, never on the honest path. We implement four checks (authorized key access, delivery-channel integrity, syntactic conformance, and declared material consumption) in Solidity and measure them on a real 6.41 MB G-code file, the 3DBenchy, across Ethereum, Arbitrum, and opBNB. Every service incurs the cost of posting the encrypted design, with or without a dispute. For the 3DBenchy, the no-dispute outcome costs \$7,207 in up to 9 hours on Ethereum, \$288 in 3 min on Arbitrum, and \$2.87 in 2 min on opBNB, and a fully contested dispute costs \$49,660 in up to 57 hours on Ethereum, \$1,988 in 19 min on Arbitrum, and \$19.73 in 13 min on opBNB. Costs and times grow with size: for a 50 MB industrial design, an undisputed service reaches \$56,173 and up to 3 days on Ethereum against \$22.36 and 16 min on opBNB, and a fully contested dispute reaches \$488,440 over up to 18 days on Ethereum against \$195 and 1.6 hours on opBNB. Of the four, the material-consumption check is the costliest, its predicate being the most expensive to evaluate on-chain. OVC makes confidential, claim-based bidding economically feasible on Arbitrum and opBNB, but not on Ethereum at industrial scale.

---


### 142. [AMPBench-MT: A Homology-Controlled Benchmark for Antimicrobial Peptide Potency, Spectrum, and Safety Prediction](https://arxiv.org/abs/2607.25518)

**<font color=#1a73e8>作者：</font>** Ziheng Zhou, Huiyu Luo, Xiaohu Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computational AMP discovery is often evaluated through AMP/non-AMP recognition, yet follow-up decisions depend on assay-derived evidence such as target-species potency, hemolysis, toxicity, and selectivity. Existing AMP and peptide benchmarks cover binary recognition, multilabel annotation, assay regression, or broader peptide-model comparison, but they do not jointly place AMP recognition, species-conditioned potency, spectrum, safety-facing proxy endpoints, and cross-endpoint behavior within one sequence-homology-controlled protocol. To address this problem, we introduce AMPBench-MT, a provenance-preserving benchmark that standardizes canonical peptide records and organizes them into binary recognition, species-conditioned pMIC regression, and endpoint-specific potency and safety-facing readouts. Across 161 endpoint-specific model evaluations, high binary performance does not reliably indicate assay-endpoint behavior. Frozen protein-language-model embeddings form the leading pMIC error cluster, while graph and classical regressors remain close. Spectrum labels further reveal that PR-oriented metrics can be misleading under scarce observed negatives, whereas low-toxicity, HC50 hemolysis, and selectivity expose smaller but more assay-facing signals. AMPBench-MT shows that AMP evaluation should move beyond recognition leaderboards toward endpoint-aware evidence auditing. Our proposed benchmark is available at this https URL.

---


### 143. [I2VShield: An Efficient Proactive Defense Framework against DiT-based Image-to-Video Models](https://arxiv.org/abs/2607.25522)

**<font color=#1a73e8>作者：</font>** Yimao Guo, Zuomin Qu, Wei Lu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of video generation models has led to the increasing misuse of image-to-video (I2V) models. Although substantial progress has been made in detecting AI-generated videos, proactive defenses against I2V models remain underexplored. In particular, current proactive defenses against I2V models predominantly rely on gradient-based adversarial attacks, which require defenders to possess GPUs with substantial memory resources (VRAM) to generate adversarial examples. To address this issue, we propose I2VShield, a privacy protection method based on generative adversarial attacks tailored to Diffusion Transformer (DiT)-based I2V models. The proposed method primarily consists of two components: (1) a text-adaptive perturbation generation framework integrating adversarial learning to mitigate computational overhead while maintaining visual imperceptibility; and (2) an untargeted Multimodal Attention Disruption (MAD) attack that exploits the inherent vulnerabilities of DiT-based I2V models, maximizing the deviation of the internal attention features from their clean states. Extensive experiments demonstrate that our approach achieves highly competitive protection performance across various datasets and mainstream DiT-based I2V models, particularly in disrupting spatiotemporal coherence, while substantially reducing computational costs.

---


### 144. [ReLATE: Reliability-Guided Evidence Fusion for Robust UAV--Satellite cross-view Geo-Localization](https://arxiv.org/abs/2607.25524)

**<font color=#1a73e8>作者：</font>** Haochen Jiang, Jialei Pan, Yuzhe Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV)-satellite cross-view geo-localization matches UAV images against satellite imagery and has achieved impressive accuracy on clean (non-degraded) image benchmarks. In real-world flights, however, UAV observations are frequently affected by adverse weather, illumination changes, platform motion, sensor noise, and compression, while the robustness of existing methods under such degradations remains largely unexamined. In this paper, we present UAVSat-Deg, a large-scale robustness benchmark for degraded UAV-satellite geo-localization, comprising University-1652-Deg and SUES-200-Deg. UAVSat-Deg covers 27 corruption types, including 19 core and 8 compound corruptions, at three severity levels, supports bidirectional drone-to-satellite and satellite-to-drone retrieval as well as multi-height UAV acquisition, and contains more than 11.7 million pre-generated corrupted test images. Benchmarking representative methods under this protocol reveals substantial robustness gaps, particularly under severe and compound corruptions. To address this problem, we propose ReLATE, a Reliable Evidence Learning framework with Adaptive Token Evidence Regulation, which realizes reliability-adaptive feature fusion during descriptor construction. ReLATE estimates a structure-smoothed reliability field over visual tokens, aggregates trustworthy local evidence, and adaptively integrates it into query-derived representations; the regulated query representations are then combined with the CLS-token and GeM-pooled branches to form the final cross-view descriptor. Across both test sets and retrieval directions, ReLATE achieves the best average corrupted-test performance among the compared methods while maintaining competitive accuracy on clean images. The code and dataset will be available at this https URL.

---


### 145. [Are the High-weight Neurons the Important Ones in Image Classification Neural Networks?](https://arxiv.org/abs/2607.25529)

**<font color=#1a73e8>作者：</font>** Qitao Chen, Dongfu Yin, F. Richard Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As neural network models for image classification advance, neurons play critical roles in pruning, backdoor defense, and interpretability. Yet existing work lacks clarity on the weight-importance relationship. We address this with a neuron importance assessment method using three experiments: quantifying overlap between high-weight and accuracy-impacting neurons, analyzing high-weight neuron perturbation effects, and testing post-retraining accuracy after high-weight neuron ablation. Experiments on CIFAR-10 and Mini-ImageNet reveal key patterns. Overlap analysis shows top 10\% high-weight neurons overlap with important ones by only about 25\% at maximum, dropping further in subsequent intervals. Perturbation tests find top 10\% high-weight neurons cause 45-80\% accuracy degradation under certain operations compared to 3-7\% for random perturbations, but a third of them show minimal impact. Ablation-retraining results show removing top 10\% high-weight neurons leaves accuracy 10-20\% below baseline with no recovery, while ablating top 0.1\% allows near-full recovery. Notably, some low-weight intervals show 10-17\% degradation when perturbed, comparable to mid-range high-weight neurons. These results confirm not all high-weight neurons are important: their importance is nonlinear. Low-weight neurons also contribute significantly. This challenges weight-importance equivalence, offering refined neuron role insights. It supports applications like encryption prioritizing critical high-weight neurons and pruning removing non-critical ones, advancing neural network analysis.

---


### 146. [Multi-Scale Structural Features for Continual, Comprehensible Visual Recognition in a Developmental Learning Framework](https://arxiv.org/abs/2607.25531)

**<font color=#1a73e8>作者：</font>** Zeki Doruk Erden  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contemporary machine learning struggles to learn continually, reuse prior knowledge, and expose a comprehensible internal structure. A recently proposed developmental, gradient-free learning framework addresses these limitations by learning a discrete, topological model of its inputs through local variation and selection, yielding an inherent continual-learning guarantee: new observations refine existing structure without overwriting past knowledge, and without replay buffers or predefined task boundaries. Its extension to visual inputs demonstrated this principle on shape recognition, but relied on a feature representation of limited expressivity that capped recognition accuracy. We introduce a new visual feature representation that encodes shape structure across multiple scales, capturing edge and contour features together with their spatial relations, and integrate it with the network-refinement learning process; we further improve the learning dynamics and the read-out used to predict from the learned model. The study targets two-dimensional shape, with class-incremental MNIST as a controlled, interpretable benchmark in which continual-learning behavior can be measured directly. Our approach substantially increases accuracy over the prior representation, matching or exceeding replay- and regularisation-based baselines at comparable storage while storing no past data, and preserves the framework's defining behavior: earlier-learned classes are retained as new ones are introduced, with no destructive adaptation, and the learned representations remain human-interpretable. What separates the methods is retention: the baselines surrender most of a just-trained class within its own cycle and relearn it afterwards, which ours does not. The significance lies in the manner of learning. The system integrates information one sample at a time while provably preserving its responses to...

---


### 147. [Entangled by Design: Spurious Intra-Variable Signal Routing in Tabular In-Context Learners](https://arxiv.org/abs/2607.25532)

**<font color=#1a73e8>作者：</font>** Athanasios Vlontzos, Giorgos Papanastasiou, Bernhard Kainz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Consider a model trained at a single hospital to predict patient recovery, where the measured feature $X$ bundles the patient's true health signal ($C$) with a systematic artefact from that hospital's equipment ($S$). Within that hospital, the artefact correlates with outcomes through unmeasured confounders such as patient demographics; an in-context learner rationally routes predictions through $S$, not $C$, and fails silently when deployed at a new hospital with different equipment. We formalise this as \emph{spurious routing in composite representations}: when a feature $X = [C;\,\alpha S;\,\eta]$ encodes a causal signal $C$ and a spurious signal $S$ in distinct subspaces, the ICL cannot determine which drives predictions. We prove that under ridge ICL, a linear in-context learner, this routing is unavoidable regardless of context size; TabPFN, a state-of-the-art pretrained tabular ICL model, shows qualitatively consistent behaviour empirically. We derive a closed-form characterisation, $\mathrm{CSR} \propto \rho_S/\rho_C$, confirmed at $r = 0.997$ for linear ICL and $r = 0.979$ for TabPFN. Contrary to intuition, larger context sharpens commitment to the dominant in-context signal, amplifying spurious routing by up to $1.74\times$; in the high-spurious corner, more expressive models show greater vulnerability empirically ($+2.22$ CSR gap at high entanglement). We introduce two lightweight mitigations: environment-stratified context construction and S-swap augmentation, that require only weak environment labels and no knowledge of the causal partition. S-swap reduces spurious routing by $74\%$ for linear ICL and $98.8\%$ for TabPFN, with TabPFN's causal sensitivity increasing $8.4\times$ simultaneously: the model does not become agnostic, it reroutes through the causal signal.

---


### 148. [Visual prompt engineering for video models](https://arxiv.org/abs/2607.25537)

**<font color=#1a73e8>作者：</font>** Robert Geirhos, Yuxuan Li, Thaddäus Wiedemer 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the age of foundation models, a model is only as good as its prompt. For this reason, prompt engineering has become an essential technique for improving language model performance. Since video models are currently becoming foundation models for visual tasks (e.g., visual reasoning), we here ask whether they similarly benefit from visual prompt engineering: automatically modifying the task image to improve model performance. For example, for a visual physics reasoning task ("Where does the ball land, after passing a set of obstacles?"), an abstract sketch-like scene can be turned into a photorealistic version with a simple call to an image editing model. We find that visual prompt engineering, or VIPE for short, improves video reasoning performance across tasks. In fact, for video models, visual prompt engineering can be even more effective than classic text-based prompt engineering or test-time scaling. Ultimately, just as text-based prompt engineering systematically improves language model performance, visual prompt engineering can serve as a simple, compute-efficient approach to elicit better visual reasoning performance from video models. Example videos on our project page at this https URL.

---


### 149. [Mind the Missing Split: Resolving Feature Heterogeneity in Swarm Learning with Random Forests](https://arxiv.org/abs/2607.25538)

**<font color=#1a73e8>作者：</font>** Mohammad Tajabadi, Dominik Heider  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Swarm Learning is a decentralized collaborative learning mechanism that allows multiple organizations to train a shared model without central coordination or direct data sharing. In typical horizontal Swarm Learning, datasets across sites are usually assumed to share the same feature set. However, in real-world applications, sites often have partially overlapping features because measurements, protocols, and available covariates differ across sites. This feature heterogeneity creates a practical issue for machine learning algorithms such as Random Forests. Specifically, when decision trees are pooled into a global Random Forest, inference at a given site can become ill-defined if a traversal encounters a split on a feature that is not available locally, often forcing organizations to discard site-specific variables upfront. In this paper, we address feature heterogeneity in Swarm Learning with Random Forests under partially overlapping feature spaces. We propose several deterministic and probabilistic inference-time strategies that resolve such missing splits without restricting training to the intersection of features. We evaluate the methods on nine datasets and demonstrate that they outperform both the intersection baseline and locally trained models across a broad range of scenarios.

---


### 150. [Less is More: Modality-Decoupling for General AIGC Audio-Video Detection](https://arxiv.org/abs/2607.25543)

**<font color=#1a73e8>作者：</font>** Jielun Peng, Yabin Wang, Yaqi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative AI has rapidly expanded audio-visual forgery beyond human-centric deepfakes into general scenes. Existing AIGC detection methods assume audio-visual content correspondence, identifying forgeries by spotting cross-modal inconsistencies. However, we empirically find that this assumption does not consistently hold in general scenarios. We argue that, for general audio-visual AIGC detection, decision-level fusion is a more robust alternative to feature-level fusion. Therefore, we propose DAV-Det, a decoupled audio-visual AIGC detection system that independently models forensic evidence from each modality. The visual detector leverages multi-granularity representations at global, patch, and segment levels to capture spatial forgery cues, while the audio detector exploits both temporal and spectral irregularities via a gated temporal-spectral dual-branch architecture to model acoustic artifacts. Our method ranks 1st in the General AIGC Audio-Video Detection Challenge of the IJCAI-ECAI 2026 DDL 2.0 Workshop, with a final score of 0.8460. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-229](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

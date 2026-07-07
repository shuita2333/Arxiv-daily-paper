# 📦 其他研究 | 2026年07月08日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 251. [Q-TriM: Question-Guided Tri-Modal Attention for Audio-Visual Question Answering](https://arxiv.org/abs/2607.03825)

**<font color=#1a73e8>作者：</font>** SungHun Kim, SeungJun Baek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-Visual Question Answering (AVQA) extends classical VQA by requiring joint reasoning over video and synchronized audio. However, many AVQA systems rely on deeply stacked layers of self- and cross attention across text, video, and audio. Such sequential stacking may incur loss of information such as subtle inter-modal cues over the layers, causing errors to accumulate across sequential attention layers during the fusion. We introduce Q-TriM which performs multi-modal fusion in a shallow and parallel manner instead of a deep and sequential manner. For Q-TriM, we propose a novel framework for attention operation incorporating video and audio conditioned on text. As a result, we obtain not only standard cross attention outputs but also Tri-Modal Attention representations in which Query, Key, and Value come from distinct modalities. These attention representations are combined in parallel at a single stage, thus avoiding the multi-modal fusion with deep stacks in order to mitigate error accumulation and depth-induced issues. Q-TriM achieves state-of-the-art performance on three AVQA benchmarks, including substantial gains on MUSIC-AVQA-R, which demonstrates its robustness and out-of-distribution generalization. Code is available at this https URL

---


### 252. [How Do Diffusion Classifiers Decide? A Bias-Centric Evaluation](https://arxiv.org/abs/2607.03831)

**<font color=#1a73e8>作者：</font>** Saba Fathi, Fardin Ayar, Maryam Abdolali 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have recently been repurposed for zero-shot classification, giving rise to diffusion classifiers that identify the best-matching text prompt by minimizing the noise-prediction error. Despite their growing adoption, how these models make classification decisions remains poorly understood. We introduce ASOB-Bench, a bias evaluation for diffusion classifiers along three dimensions: Attribute binding, Size-Order bias, and Background dependency. These dimensions serve not as an exhaustive taxonomy but as targeted probes of how the text-conditioned reconstruction-error score reaches a decision. Such a perspective is well studied for discriminative vision-language models, yet remains overlooked for diffusion classifiers. Extending an existing framework with five new attribute categories on newly constructed datasets, we find diffusion classifiers are less prone to attribute misbinding than an OpenCLIP baseline; on the established ComCo benchmark they are substantially more susceptible to size-order shortcuts; and on ImageNet-B they suffer far larger accuracy drops, revealing heavy reliance on background over foreground cues. Reconstruction-error heatmaps and U-Net cross-attention visualizations expose the mechanism behind each bias. Because diffusion classifiers share the same denoiser as text-to-image models, these single-pass diagnostics also point toward analogous failure modes in generation. Overall, diffusion classifiers exhibit a distinct bias profile from vision-language models, offering guidance for building more robust diffusion-based models.

---


### 253. [Enactive Drift Regulation and the Emergence Machine: A Framework for Coherent Adaptation Through Regulated Interaction](https://arxiv.org/abs/2607.03834)

**<font color=#1a73e8>作者：</font>** Nicholas Davis  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Adaptive systems increasingly operate in environments characterized by persistent non-stationarity, where patterns reorganize rather than merely vary. While existing approaches such as online learning, continual learning, and adaptive filtering address performance degradation under changing data distributions, they typically treat drift as noise, error, or distribution shift to be corrected. This paper argues that such framings miss a more fundamental challenge: the loss of organizational coherence over time. We introduce Enactive Drift Regulation (EDR) as a general adaptive principle that treats drift as a regulatory signal indicating breakdowns in coherence between a system's internal organization and its environment. Rather than treating prediction optimization or retraining as sufficient, EDR reframes adaptation as the regulation of structure-maintaining, reorganizing, or transitioning internal dynamics to sustain viable operation under change. We present the Emergence Machine as an architectural instantiation of EDR, organized around regimes, attractors, coherence measures, reorganization dynamics, and memory across regimes. By shifting the focus from error minimization to coherence regulation, this work provides a principled framework for long-duration adaptation under non-stationarity and offers a bridge between adaptive control and enactive accounts of cognition.

---


### 254. [When Simpler Is Better: Evaluating Translation Pipelines for Medieval Latin Manuscripts](https://arxiv.org/abs/2607.03836)

**<font color=#1a73e8>作者：</font>** Nguyen Kim Hai Bui, Md. Easin Arafat, Tamás Gábor Orosz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite remarkable progress in machine translation, Vision Language Models (VLMs) struggle on historical manuscripts, a domain that stresses core Natural Language Processing (NLP) capabilities: low-resource transliteration, archaic vocabulary, and noisy input signals. We present a systematic framework for evaluating the full image-to-translation pipeline on medieval Latin manuscripts, a setting in which scribal shorthand, ligatures, and parchment degradation expose failure modes that are invisible in clean-text benchmarks. Benchmarking on the CATMuS Latin dataset reveals a specialization gap: domain-specific Optical Character Recognition (OCR) models reduce character error rate by up to 4.3$\times$ compared to general-purpose VLMs, despite operating at orders of magnitude fewer parameters. We introduce the Interpres-Parallel-Corpus (IPC), a novel dataset comprising 1,383 aligned manuscript image lines, transcriptions, and expert translations, the first of its kind for medieval Latin. Our experiments uncover a complexity paradox: the simplest pipeline, a specialized OCR model feeding directly into a VLM, outperforms all multi-component variants. Adding retrieval-augmented generation (RAG) or post-OCR correction introduces prompt saturation and error propagation that degrade aggregate translation quality. These findings offer both a new benchmark and practical guidance for deploying translation systems in low-resource historical settings.

---


### 255. [Adversarial LassoNet: Robust Feature Selection via Stability-Driven Sparse Learning](https://arxiv.org/abs/2607.03839)

**<font color=#1a73e8>作者：</font>** Zhen Huang, Peicheng Xu, Junbiao Pang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse feature selection is critical for high-dimensional machine learning, yet traditional $\ell_1$-regularized methods are often brittle under observational noise and spurious correlations, leading to unstable feature supports and degraded generalization. Although adversarial training has been widely used to improve model robustness, its interaction with hierarchical sparse feature selection remains underexplored. In this work, we propose Adversarial LassoNet (AdLNet), a stability-driven sparse feature selection framework that integrates input-space adversarial perturbations with the hierarchical sparsity mechanism of LassoNet. We derive a tractable first-order adversarial approximation under local smoothness assumptions and provide an NTK-inspired spectral analysis to characterize how perturbation-driven training can reduce gradient concentration. Experiments on high-dimensional SERS data, six public benchmark datasets, and ColoredMNIST show that AdLNet maintains competitive sparse-selection performance while improving out-of-distribution robustness by 4.4\% and feature support reproducibility by 6.3\% under nearly matched support sparsity on ColoredMNIST. On the high-dimensional lung cancer screening dataset, AdLNet achieves a 5.3\% test accuracy gain and a 6.0\% AUC improvement over vanilla LassoNet. Code and dataset are available at this https URL.

---


### 256. [NeSy-CSA: A Neuro-Symbolic Framework for Open-Ended Critical Scenario Attribution](https://arxiv.org/abs/2607.03847)

**<font color=#1a73e8>作者：</font>** Qitong Chu, Xunjie He, Chen Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding why discovered scenarios become critical in scenario-based testing is essential for effectively leveraging them in decision-making systems. Reasoning about such criticality can be formulated as an attribution problem. However, across different decision-making tasks, the causes of criticality may involve diverse state variables, interaction patterns, and failure mechanisms, making attribution an inherently open-ended problem beyond predefined explanation spaces. Existing attribution methods still struggle to balance open-ended reasoning flexibility with the interpretability and traceability required for critical scenario reasoning. To address this limitation, we propose NeSy-CSA, a neuro-symbolic framework that transforms open-ended critical scenario attribution from unconstrained explanation generation into structured and traceable reasoning. NeSy-CSA narrows the attribution space by selecting relevant factors, makes the reasoning process traceable through a dependency-aware evidence graph, and executes symbolic reasoning procedures derived from atomic operations, coordinated with evidence-constrained neural inference to support flexible open-ended attribution. We further introduce a process-level and result-level assessment module to evaluate the structural validity of the attribution process and the behavioral effectiveness of the attribution results under controlled interventions. Experiments across four decision-making environments show that NeSy-CSA improves two intervention-based measures of attribution effectiveness by 18.32% and 13.67% over LLM-based baselines. These results demonstrate its potential to transform discovered critical scenarios into reusable knowledge for subsequent testing and safety analysis.

---


### 257. [ContiStain: Cross-Domain Relation-Preserving Distillation for Continual Multi-Domain Virtual IHC Staining](https://arxiv.org/abs/2607.03851)

**<font color=#1a73e8>作者：</font>** Fuqiang Chen, Yifeng Wang, Hongpeng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A unified multiplex virtual staining model enables scalable and non-destructive multiplex analysis from H&E slides while promoting parameter efficiency, shared pathological knowledge, and consistent cross-biomarker representations. However, in clinical practice, data for new biomarkers are typically acquired sequentially over time. Fine-tuning on such temporally arriving data leads to severe performance degradation on previously learned biomarkers, as sequential optimization disrupts the structured relationships among biomarker representations in the latent space. To address this issue, we propose ContiStain, an IHC multi-domain relational distillation framework for continual virtual staining. We first (i) construct a domain-aware structured feature space using a mixture-of-experts (MoE) feature extractor to reduce representation interference across biomarker domains. Based on this stabilized feature space, we then (ii) propose a relation-preserving distillation strategy that explicitly enforces the consistency of cross-domain token-level cosine similarity matrices between learned biomarker domains during continual adaptation. By maintaining cross-domain structural coherence, ContiStain mitigates forgetting while retaining adaptability to new domains. Experiments on the MIST dataset under a four-domain sequential virtual IHC staining setting show improved stability, reducing FID and ConchFID by 11.1 and 60.9 compared to sequential fine-tuning, enabling scalable and robust multi-domain virtual staining. Code is released at this https URL.

---


### 258. [CogRad: A Cognitively-Inspired Multi-Agent Framework for Radiology Report Generation](https://arxiv.org/abs/2607.03853)

**<font color=#1a73e8>作者：</font>** Saif Ur Rehman Khan, Hasaan Maqsood, Sebastian Vollmer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated radiology report generation (RRG) can ease radiologist workload, yet most existing systems produce a report in a single forward pass, with no mechanism to check a claim against the image or revisit a finding once stated. We present CogRad, a cognitively inspired multi-agent framework that structures generation around four stages of a radiologist's reading process. A Scout agent discovers anatomical regions directly from image patches via slot attention and assigns region and disease-level triage scores; an Investigator agent concentrates representational capacity on the regions Scout flags as suspicious; a Writer agent compiles these signals into a disease gated visual prefix for a large language model; and a Verifier agent supervises training with a visual entailment loss and, at inference, re-examines its own draft sentence by sentence, regenerating any report it judges insufficiently grounded. On CheXpert Plus, CogRad attains a BLEU-4 of 0.316 and a CIDEr of 0.322, the best scores among the methods we compare against. On IU X-Ray, it attains a BLEU-4 of 0.201 and a CIDEr of 0.724, leading every baseline on every standard NLG metric. We further evaluate CogRad with RadGraph F1, CheXbert F1, and a hallucination analysis to assess clinical accuracy beyond standard text-overlap metrics, complemented by ablation studies and Grad-CAM-based visualizations that characterize each agent's contribution and the model's visual grounding.

---


### 259. [PRISM3D: Probabilistic Refinement and Robust Initialization for Physically Consistent Scene Modeling under Extreme Motion Blur](https://arxiv.org/abs/2607.03855)

**<font color=#1a73e8>作者：</font>** Gopi Raju Matta, Reddypalli Trisha, Vemunuri Divya Madhuri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the inverse problem of blind 3D scene reconstruction from extremely motion-blurred images, a scenario where traditional Structure-from-Motion (SfM) pipelines fail. Existing approaches typically circumvent this bottleneck by relying on impractical sharp-image supervision. In this work, we introduce PRISM3D, a unified framework enabling robust reconstruction directly from severely degraded inputs. To overcome the lack of a reliable starting point, we propose a Robust Initialization strategy utilizing deep dense tracking method (VGGSfM) to recover global topology where feature matching fails. To the best of our knowledge, we are the first to effectively leverage this paradigm to bootstrap 3D Gaussian Splatting from extreme motion blur. However, while robust, this initialization yields sparse and noisy geometry that causes deterministic optimization to diverge. To resolve this, we propose a coupled solution driven by probability and physics: we adopt a probabilistic formulation for geometric densification via Markov Chain Monte Carlo (MCMC) to robustly populate the sparse priors, while simultaneously modeling physical image formation via continuous Bezier Trajectories. Furthermore, while PRISM3D establishes a highly robust standalone pipeline, the availability of complementary event streams offers an opportunity to push the reconstruction fidelity further. To exploit this, we introduce PRISM3D-E, a multi-modal (RGB + Events) extension that seamlessly integrates high-temporal-resolution events as structural priors to maximize geometric recovery. Because existing datasets lack paired event streams under such severe degradation, we concurrently contribute the PRISM3D-E Benchmark to facilitate rigorous evaluation. Extensive experiments demonstrate that both our standalone RGB framework and its multi-modal extension establish new state-of-the-art performance.

---


### 260. [A Unified Framework for Quantized and Continuous Strong Lottery Tickets](https://arxiv.org/abs/2607.03860)

**<font color=#1a73e8>作者：</font>** Aakash Kumar, Emanuele Natale  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Strong Lottery Ticket Hypothesis (SLTH) asserts that sufficiently overparameterized, randomly initialized neural networks contain sparse subnetworks that, even without any training, can match the performance of a small trained network on a given dataset. A key mathematical tool in the theoretical study of SLTH has been the Random Subset Sum Problem (RSSP). The SLTH has recently been extended to the quantized setting, where the network weights are sampled from a discrete set rather than from a continuous interval. These new results are however far from those in arbitrary-precision setting in several ways. In this work, we provide an analysis of the RSSP in the discrete setting, and use it to derive tight SLTH guarantees in the quantized case. Our analysis obtain tight bounds on the failure probability of finding a strong lottery ticket in the quantized regime, providing an exponential improvement over previous results. Most importantly, it unifies the literature by showing that both approximate representations in the continuous setting and exact representations in quantized settings naturally emerge as limiting cases of our results. This perspective not only sharpens existing bounds but also provides a cohesive framework that simultaneously handles approximation and rounding errors.

---


### 261. [Ghosts Beneath Textures: Texture-Relation Cues for Cross-Paradigm AI-Generated Image Detection](https://arxiv.org/abs/2607.03862)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Yiming Qin, Zhongjie Ba 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated images have proliferated rapidly, motivating extensive research. Most existing AI-generated image detectors are developed and evaluated under image-free generation paradigms, such as noise-based or text-guided generation. However, image-conditioned generation has become increasingly important in practical applications, as it enables more fine-grained control over generated content. Detecting AI-generated images across these two paradigms creates a critical cross-paradigm detection problem that has long been overlooked. To study this problem, we construct ConImageGen, a benchmark for cross-paradigm AI-generated image detection. Evaluations on ConImageGen show that existing detectors fail to generalize reliably across image-free and image-conditioned generation. To address this failure, this paper identifies a cross-paradigm forensic cue and provides a new perspective for generalized AI-generated image detection. Specifically, by suppressing semantic interference, we visualize, for the first time, semantics-irrelevant texture patterns across generation paradigms. These patterns exhibit structured local-global texture relations, indicating a generalizable form of forensic evidence. Motivated by this finding, we shift the focus from directly exploiting explicit artifacts to modeling texture relations and propose DTS-Det, a detection framework that captures and leverages such relations for generalized AI-generated image detection. Extensive experiments validate the effectiveness of our method. DTS-Det achieves state-of-the-art performance across diverse evaluation settings, reaching 99.6% ACC on ConImageGen with a 10.5% gain over the best baseline. It also achieves 93.2%/94.1% ACC in cross-dataset evaluation on PicoBanana/RAID and maintains detection rates of 95.2%/88.1% under reconstruction attacks and black-box adversarial attacks, respectively.

---


### 262. [GeoSelect: Spatial-Program Execution for Training-Free Referring Remote Sensing Image Segmentation](https://arxiv.org/abs/2607.03869)

**<font color=#1a73e8>作者：</font>** Yuhang Jiang, Guohui Deng, Miaozhong Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring remote sensing image segmentation isolates the object named by a natural-language expression in an aerial image. Existing training-free methods resolve the expression through implicit vision-language activations or region-text similarity, which gives weak control over the spatial, comparative, and ordinal relations that dominate aerial referring: they cannot represent constructions such as the largest ship or the second court from the left. We propose GeoSelect, a training-free pipeline that reframes referring as the execution of a typed spatial program. A frozen, text-only language model synthesises the expression into a small domain-specific language, a well-formedness checker accepts the program, and a deterministic executor runs it. The central abstraction is a single scored candidate set type under which every operator composes: continuous geometric fields realise position and proximity as dense pixel-level maps, while discrete set and order operators add the extremum, ordinal, counted-union, and relational constructions that fields alone cannot express. Because execution is explicit, every intermediate program, field, and ranking is inspectable, and a reliability ladder degrades any failing program to a field-only special case, so every expression returns an answer. GeoSelect attains 58.86 mIoU on RRSIS-D test and 55.27 mIoU on RISBench test, more than twice the best prior training-free method on RRSIS-D, with no referring supervision and on a single GPU. A controlled comparison with candidates and segmenter fixed attributes the gain to explicit execution, not the backbone; an oracle decomposition localises the residual gap to detection recall on RRSIS-D and selection on RISBench, and an exposure audit confirms robustness to pretraining leakage. Code will be released upon acceptance at the project page this https URL.

---


### 263. [A Gradient Flow Perspective on Minimum MMD Estimation](https://arxiv.org/abs/2607.03871)

**<font color=#1a73e8>作者：</font>** Sophia Seulkee Kang, Louis Sharrock, Xiaoyuan Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Minimum maximum mean discrepancy (MMD) estimation has emerged as a robust and likelihood-free alternative to maximum likelihood estimation for parameter estimation. Yet, despite its practical success, the associated optimization problem remains poorly understood, with theoretical guarantees for existing algorithms hinging on convexity assumptions that rarely hold in practice. We address this gap by proposing a preconditioned gradient descent (PGD) scheme, establishing its asymptotic \emph{global} convergence under explicit gradient-dominance and projection-residual conditions. Our approach is inspired by recent progress on MMD gradient flows, a nonparametric descent scheme on the space of probability measures. We provide extensive empirical evidence that our PGD scheme outperforms standard gradient descent across a range of challenging parameter estimation and composite hypothesis testing problems.

---


### 264. [SharpSplat: Edge-Regularized 3D Gaussian Splatting for High Fidelity Urban Building Reconstruction from UAV images](https://arxiv.org/abs/2607.03872)

**<font color=#1a73e8>作者：</font>** Porus Vaid, Shivam Chopra, Vaibhav Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing high-fidelity 3D building models from UAV imagery is essential for large-scale digital twin development. However, existing 3D Gaussian Splatting (3DGS) techniques often struggle with building facades, failing to capture sharp geometric transitions. To address this, we propose a semantic edge regularization framework that supervises 3DGS to produce crisp architectural boundaries. Our method leverages SAM 3 to generate precise building masks, from which we extract architecturally significant edges. During training, we align rendered image gradients with these extracted edges, forcing the Gaussians to converge into sharp structural geometries. Evaluations across campus environments, dense urban centers, and custom residential datasets demonstrate significant improvements in edge fidelity without requiring architectural modifications to the 3DGS pipeline. Our approach proves robust across diverse building types, roof geometries, and urban densities.

---


### 265. [MACRO: Training-free Multi-plane Attention for Closeup Render Optimization](https://arxiv.org/abs/2607.03875)

**<font color=#1a73e8>作者：</font>** Nitzan Hodos, Roy Amoyal, Lior Fritz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Close-up rendering, zooming into a scene well beyond any training camera, is important for virtual production and interactive 3D content, yet remains an open challenge. 3D Gaussian splatting (3DGS) enables high-fidelity, real-time novel view synthesis, but its rendering quality degrades at close range. Recent diffusion-based methods that enhance the rendering by conditioning on reference images from the training set produce significant artifacts in this setting. We analyze this failure and identify its root cause: the scale gap between the close-up and reference views. We show that the features in reference-conditioned enhancement models are not scale-invariant, causing cross-view attention to retrieve incorrect correspondences when the same content appears at different scales, and that this mismatch cannot be corrected in latent space because the VAE encoder is not scale-equivariant. Building on this analysis we introduce MACRO, Multi-plane Attention for Closeup Render Optimization, a training-free method for high-quality close-up novel view synthesis from 3DGS. MACRO resolves the scale gap by leveraging the scene's known 3D structure: it decomposes the close-up into depth planes, crops and resizes references in image space to match the scale of each plane before encoding, and applies a depth-aware attention mask so each token attends only to scale-matched references. The method requires no architectural changes or additional training. We further contribute two new close-up novel view synthesis benchmarks, the first standardized evaluation protocol for this setting, and demonstrate state-of-the-art results on both, outperforming existing 3DGS and diffusion-based methods on both reconstruction and perceptual metrics. Project page: this https URL

---


### 266. [SGF-CDNet: A Consistency-Discrepancy Graph Network over Semantic-Geometric Fused Nodes for Face Forgery Detection](https://arxiv.org/abs/2607.03883)

**<font color=#1a73e8>作者：</font>** Jiayao Jiang, Bin Liu, Nenghai Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of deepfakes necessitates robust face forgery detection. Although forged faces may lack obvious artifacts, they often contain subtle disharmony among different facial regions. We propose SGF-CDNet, a Consistency-Discrepancy Graph Network (CD-GNN) over Semantic-Geometric Fused (SGF) nodes. First, SGF-CDNet constructs SGF nodes by deeply fusing semantic regions from face parsing with geometric information from facial landmarks, allowing nodes to capture both high-level concepts and precise geometric constraints. Next, a dual-path CD-GNN performs parallel relational reasoning on these nodes across two dimensions: consistency and discrepancy. The consistency path evaluates if facial components follow natural biological patterns, while the discrepancy path mines for structural tensions and feature conflicts introduced by forgeries. By integrating these processes, our model effectively identifies disharmonious relationships between facial components. Extensive experiments on public datasets demonstrate that SGF-CDNet achieves superior performance, establishing it as a reliable solution for face forgery detection.

---


### 267. [BAT3R: Bootstrapping Articulated 3D Reconstruction from 2D Image Collections](https://arxiv.org/abs/2607.03891)

**<font color=#1a73e8>作者：</font>** Jakub Zadrozny, Oisin Mac Aodha, Hakan Bilen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D reconstruction of articulated objects from a single image is challenging because large training datasets with paired image and 3D supervision are difficult to obtain. Recent point map-based methods achieve strong performance but rely on synthetic datasets rendered from manually created articulated 3D assets with carefully curated pose distributions. While camera viewpoints can be easily sampled, generating realistic object articulations remains costly and labor-intensive. We propose a training framework that reduces this requirement by leveraging unannotated 2D images collections with only a single rigged canonical mesh per category. Starting from a weak 3D shape predictor trained on canonical-pose renders, we iteratively estimate object articulation and camera pose by fitting the mesh to predicted point maps. The recovered articulations and viewpoints are then used to render updated synthetic training data, progressively improving the predictor. Despite using substantially weaker 3D supervision, our models achieve performance comparable with DualPM, which requires manually curated articulated training datasets.

---


### 268. [Post-Lecture Interactive Environments for Conceptual Learning: A Randomized Comparison of Mixed Reality and Tangible Instruction in Undergraduate STEM Education](https://arxiv.org/abs/2607.03896)

**<font color=#1a73e8>作者：</font>** Sharmin Akter, Mohammad Abu Nasir Rakib, Eshwara Prasad Sridhar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Developing conceptual understanding in engineering requires learners to connect spatial reasoning with abstract representations, yet lecture-based instruction often provides limited support for this process. Interactive learning environments, including mixed reality (MR) and tangible tools, may help students revisit difficult concepts through action, feedback, and visible system response. This pilot randomized study compared two post-lecture interventions, an immersive MR application and a tangible Engineering Toolkit, with lecture-only instruction in undergraduate solid mechanics. Twenty-four participants completed a baseline assessment, a common lecture, and a post-instruction knowledge test; participants in the interactive conditions also completed usability and learner-experience measures. Learning outcomes were analyzed using ANCOVA with baseline knowledge as a covariate and were supported by normalized learning gains. Instructional modality had a significant effect on post-test performance, $F(2, 20) = 3.60$, $p = .048$, partial $\eta^2 = .263$. Both interactive conditions outperformed lecture-only instruction in planned contrasts. MR showed the highest normalized learning gain ($g = .57$), whereas the tangible toolkit showed higher usability and learner confidence. In the MR condition, virtual reality sickness symptoms measured via the Virtual Reality Sickness Questionnaire remained low before and after the intervention, suggesting that the MR application was well-tolerated by participants. These results suggest that post-lecture interactive environments may support immediate conceptual learning while offering different modality-specific strengths that require larger, time-matched follow-up studies.

---


### 269. [DICT: Data Injection and Contrastive Trajectory Refinement for Conditional Image Generation with Diffusion Models](https://arxiv.org/abs/2607.03899)

**<font color=#1a73e8>作者：</font>** Chunnan Shang, Xin Zhang, Zhizhong Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have become a dominant paradigm for conditional image generation, yet existing approaches generally follow two directions: task-specific designs that can improve performance but limit generalization, and training-free loss guidance that compresses rich conditions into scalar objectives and applies stepwise guidance, leading to information bottlenecks and error accumulation along the sampling trajectory. Given the urgent need for an effective unified framework across diverse conditional image generation tasks, we propose Data Injection and Contrastive Trajectory Refinement (DICT), a training-free inference method that enhances conditional image generation without introducing task-dependent architectures. DICT introduces Data Injection, where noise-perturbed conditional signals are integrated into early denoising stages; by performing guided denoising on these injected signals, DICT adaptively selects and distills task-salient information from the raw condition, effectively preserving spatial richness and ensuring precise condition-to-generation alignment. Furthermore, DICT applies Contrastive Trajectory Refinement across adjacent denoising states, enabling pairwise comparisons that progressively improve sample quality. These designs keep inference simple while improving cross-task transfer under a unified diffusion formulation. Extensive experiments on conditional image generation tasks (e.g., style transfer, image super-resolution, and image deblurring) show consistent gains in fidelity and perceptual quality over representative task-specific and loss-guided baselines.

---


### 270. [USE: A Unified Self-Ensembling Framework for Test-Time Prompt Tuning](https://arxiv.org/abs/2607.03900)

**<font color=#1a73e8>作者：</font>** Siru Jiang, Jian Liang, Ran He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) has emerged as a popular paradigm for improving the performance of vision-language models (e.g., CLIP) on downstream tasks. Among existing CLIP-based TTA methods, Test-Time Prompt Tuning (TPT) is a pioneering work that optimizes textual prompts using multiple test-time augmentations and remains a strong baseline to date. In this work, we revisit TPT and reveal that its optimization can be interpreted as implicitly learning from self-generated pseudo labels. Building on this perspective, we propose a unified self-ensembling framework (USE) that ensures consistency between the optimization and inference stages. During optimization, we introduce a simple yet effective self-ensembling (SE) strategy that emphasizes the test image itself over its augmented views adaptively to obtain more reliable pseudo labels. To fully exploit the potential of augmentations, we further apply the same strategy at inference time, unifying the objectives of both stages. Notably, SE can also act as a lightweight optimization-free TTA method. Extensive experiments across multiple datasets demonstrate that SE and USE outperform their counterparts, respectively. Furthermore, SE yields consistent performance gains when integrated with existing TTA methods. The code is available at this https URL.

---


### 271. [CDCP: Conditional Diffusion Model with Contextual Prompts for Multi-task Offline Safe Reinforcement Learning](https://arxiv.org/abs/2607.03903)

**<font color=#1a73e8>作者：</font>** Jiayi Guan, Tianle Zhang, Li Shen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task offline safe reinforcement learning (RL) promises to learn a shared optimal safe policy from offline data across multiple tasks. This paradigm provides an effective means for the widespread application of RL in multi-task scenarios with high risk and interaction costs. However, the triple challenges of multi-tasking, safety constraints, and out-of-distribution (OOD) actions pose a significant hurdle for existing methods to ensure safety while maximizing reward returns. In this work, we propose a Conditional Diffusion model with Contextual Prompts (CDCP) to address these challenges. Concretely, we first rethink the requirements and challenges in current multi-task decision-making and control scenarios and establish the objectives of multi-task offline safe RL. Subsequently, we transform the multi-task constrained optimization problem into a conditional generation problem using the diffusion model. Based on this, we design a classifier-free guided cost-constraint strategy to provide flexible cost constraints and eliminate extrapolation errors from OOD actions via supervised learning. Additionally, we introduce a novel contextual prompting method to enhance multi-task representation accuracy and adaptability to unseen tasks. A gradient loss synchronization strategy is also introduced to eliminate gradient interference, improving training stability. Finally, extensive experiments demonstrate that the CDCP algorithm exhibits higher performance and safety in multi-task scenarios than the current state-of-the-art baseline methods. It meets different cost constraints without further training, providing a more flexible cost-constraint solution for the multi-task safe RL.

---


### 272. [Transformers with Physics-Informed Encodings and Simulation-Based Inference for Robust Detection of Eccentric Binary Black Holes in Pulsar Timing Array Data](https://arxiv.org/abs/2607.03904)

**<font color=#1a73e8>作者：</font>** Subhajit Dandapat, Alvin J. K. Chua  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pulsar timing arrays (PTAs) provide a unique window into nanohertz gravitational waves (GWs), but extracting astrophysical parameters from noisy, long-baseline timing residuals remains computationally challenging with traditional Bayesian techniques due to the high dimensionality of the parameter space, complex and correlated noise models, and the cost of repeated likelihood evaluations. We introduce a Transformer with a physics-informed positional-encoding framework for the efficient inference of eccentric binary black holes in relativistic orbits from PTA data. Our approach embeds analytical GW phase evolution directly into the model through structured positional encodings, enabling the network to learn physically meaningful representations from raw PTA timing residuals. We then use generative models, including discrete and continuous conditional normalizing flows, to infer posterior distributions within a simulation-based inference framework. Across a range of signal-to-noise ratios, the proposed method achieves improved accuracy, sharper posteriors, and faster inference compared to physics-agnostic baselines. While presented for deterministic white-noise signals, the modular framework readily generalizes to realistic PTA analyses incorporating red noise and additional components. This work highlights the potential of physics-aware deep learning models as scalable alternatives to conventional inference pipelines for next-generation PTA datasets.

---


### 273. [NavEYE: Vision-Centered Multi-Sensor Fusion-Based Situational Awareness System for Intelligent Surface Vehicles](https://arxiv.org/abs/2607.03915)

**<font color=#1a73e8>作者：</font>** Ryan Wen Liua, Junxiong Lianga, Haoyu Wanga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid development of sensor and artificial intelligence (AI) technologies, intelligent surface vehicles (ISVs) have gained increasing attention from academia and industry. Their intelligence, reliability, and safety depend heavily on situational awareness in complex navigational environments. To achieve high-quality perception, we develop a vision-centered multi-sensor fusion system, named NavEYE, by exploiting complementary sensors, including the automatic identification system (AIS), radar, and RGB camera. Specifically, we first propose a multi-constrained gated data association method (MCGA) to accurately match low-temporal-resolution AIS data with high-temporal-resolution radar data. Their fusion result is then obtained by selectively implementing distance-aware adaptively weighted fusion (DAWF) and timeliness decay-based stitching fusion (TDSF), which reduce the uncertainty caused by AIS or radar data loss in real-world sensing scenarios. Based on accurate and robust visual object detection, we further associate and fuse AIS, radar, and visual data through joint constraints of normalized bearing and distance features. According to the fusion results, comprehensive information related to ships of interest can be automatically obtained, helping enhance situational awareness and reduce collision risk for ISVs. The feasibility, robustness, usability, and effectiveness of the proposed multi-sensor fusion method and situational awareness system are demonstrated through extensive experiments on a real-world sensing dataset collected from AIS, radar, and camera. The experimental results show the superior performance of our fusion method in both quantitative and qualitative evaluations. In addition, the shipboard NavEYE system can promote navigational safety for ISVs in complex and dynamic environments.

---


### 274. [A Large-Scale Dataset and a New Method for RemoteSensing Traffic Object Segmentation](https://arxiv.org/abs/2607.03945)

**<font color=#1a73e8>作者：</font>** Zhigang Yang, Huiguang Yao, Linmao Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing imagery plays a crucial role in evaluating regional transportation capacity. However, existing segmentation datasets often lack diversity in object categories and scenes, limiting the ability of models to comprehensively evaluate trans portation capacity in real-world scenes. To alleviate this gap, we construct a large-scale and diverse dataset for transportation object segmentation, named as NWPU-Traffic. This dataset encompass four traffic object categories (car, airplane, ship, and train) and a wide range of scenes from 49 cities across 7 countries, with instance-level annotations to ensure precise segmentation of individual objects, which bridges critical shortcomings in resolution and scene diversity in existing datasets. Leveraging this dataset, we establish a benchmark with several popular segmentation networks. Furthermore, we propose a novel segmentation method that leverages spatial-channel preserving feature interaction and an adaptive feature decoder, enabling robust segmentation across varying scales and complex environments. Extensive experiments and ablation studies validate the effectiveness of our approach. The dataset and code are publicly available at this https URL.

---


### 275. [Reward Lightning: Fast Video Generation via Homologous Preference Distillation](https://arxiv.org/abs/2607.03960)

**<font color=#1a73e8>作者：</font>** Jiaxiang Cheng, Bing Ma, Xuhua Ren 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving simultaneous preference alignment and distillation acceleration in video diffusion models remains an open challenge. Existing methods optimize the two objectives over mismatched representation spaces, where improving one objective often compromises the other. To overcome this, we propose Reward Lightning, a unified framework that aligns and accelerates a video diffusion model within a single shared representation. Its central principle is homology: both objectives are evaluated on identical latent features, which mitigates the gradient conflicts that arise when they are optimized over disjoint representations. As a foundational component, we first introduce a latent reward model (LRM) that scores videos directly in the latent space, without decoding back to the pixel space. Building on the LRM, homologous preference distillation (HPD) reuses this shared backbone to perform adversarial distillation and preference alignment jointly, yielding few-step generators that remain faithful and well aligned. Extensive experiments demonstrate that the LRM surpasses pixel-level and latent-level reward baselines by $11.0\%$ and $14.7\%$ in preference accuracy, and that Reward Lightning generates high-fidelity videos in merely $1$ to $4$ steps, improving the average VBench score by $2.1\%$ while leading in text alignment, motion quality, and visual quality. Project page: this https URL.

---


### 276. [Order-based Causal Discovery for Multistage Processes](https://arxiv.org/abs/2607.03971)

**<font color=#1a73e8>作者：</font>** Eun-Yeol Ma, Junsub Jung, Heeyoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causality has become an increasingly important tool for gaining a deeper understanding of complex systems. Among various causal analysis methods, causal discovery, which identifies causal relationships among variables from data, has been widely used to uncover underlying causality in diverse processes. However, while multistage processes are prevalent in many fields, existing causal discovery methods may produce counterintuitive results, given the known process knowledge, and may not be computationally efficient for handling large datasets typical of multistage processes. To address this gap, we propose a novel causal discovery method called Order-based Causal Discovery for Multistage Processes (OCDM). OCDM is designed to infer the causal structure of multistage data while preserving their inherent hierarchical and sequential structure by explicitly incorporating process knowledge into the causal discovery process. Specifically, we propose a structural knowledge-informed order-inferring algorithm that infers the causal order of variables by incorporating information about the stage from which each variable originates, based on an order-based causal discovery framework naturally suited for inherently ordered multistage data. Furthermore, to eliminate spurious edges from the initial causal graph generated based on the inferred causal order, we introduce a novel pruning technique using stochastic gated neural networks, which offers greater computational efficiency compared to existing methods. Through experiments on various datasets, we demonstrate that OCDM effectively infers the causal structure of multistage processes, outperforming existing methods.

---


### 277. [DS-SAC: Density Search for Sample Consensus](https://arxiv.org/abs/2607.03972)

**<font color=#1a73e8>作者：</font>** Suraj Thapa, Muhammad Aminul Islam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust geometric model estimation is a fundamental problem in computer vision. RANSAC and its variants remain widely used for this task; however, they rely on stochastic minimal sampling. In this article, we propose Density Search Sample Consensus (DS-SAC), a deterministic robust estimation framework, that avoids repeated random sampling by searching dense regions. Starting from an initial model estimated from the available points, the method performs local exploration via forward and backward search. To facilitate global exploration, DS-SAC recursively partitions the point set using signed residuals and searches each valid partition for high-consensus models. We show that DS-SAC has polynomial complexity with respect to the number of points, making it an efficient alternative to stochastic consensus-based methods. Experiments on large-scale real-world datasets for homography, fundamental matrix, and essential matrix estimation show that DS-SAC achieves higher AUC scores, competitive or lower median pose errors, and faster runtime compared with widely used robust estimators, including RANSAC, MAGSAC, LO-RANSAC, and GC-RANSAC.

---


### 278. [MANCE: Manifold Aware Concept Erasure](https://arxiv.org/abs/2607.03973)

**<font color=#1a73e8>作者：</font>** Matan Avitan, Yoav Goldberg, Yanai Elazar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept erasure aims to remove a target concept from a representation while preserving the other information encoded in it. This is difficult because representations encode many concepts that are often correlated with the erasure target, so removing the target risks damaging them. We propose the Manifold Constraint Hypothesis (MCH): if natural representations concentrate on a structured, lower-dimensional manifold, then interventions should be constrained to that manifold and better preserve other information encoded in the representation during interventions. We instantiate MCH in a new concept erasure method: MANifold aware Concept Erasure (MANCE). MANCE performs iterative updates to the representations using signals from a classifier that predicts a target concept. We estimate the manifold using representations obtained from natural inputs, and then we project the concept removal update to the estimated manifold. We perform extensive evaluation on 119 settings spanning text and vision, including 13 language models, three NLP concepts, and 40 CelebA-CLIP attributes. Employing MANCE on top of previous methods shows consistent improved leakage results. We also introduce MANCE+ and MANCE++, which prepend a closed-form erasure algorithm before employing MANCE, achieving better leakage--surgicality tradeoffs relative to matched full-space updates. MANCE++, our best method, achieves state-of-the-art results on nonlinear concept erasure. These results support MCH in the erasure setting: interventions should be constrained to the natural representation manifold.

---


### 279. [TRACER: Early Failure Detection for Task-Oriented Dialogue](https://arxiv.org/abs/2607.03974)

**<font color=#1a73e8>作者：</font>** Erfan Nourbakhsh, Rocky Slavin, Ke Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Task-oriented dialogue systems often fail before the final breakdown is obvious, but most evaluation only measures failure after the conversation has already gone wrong. We present TRACER, a method for early failure detection in task-oriented dialogue. TRACER predicts from a partial dialogue whether the full conversation will eventually fail by combining simple trajectory signals from belief-state changes with text representations of the evolving dialogue state. We evaluate the method in both oracle and generated belief-state settings, and test how well it works when only 25%, 50%, 75%, or 100% of the dialogue is visible. Across these settings, TRACER detects useful failure signals well before the end of the conversation and outperforms heuristic, classical, and single-stream baselines. These results suggest that early failure detection can provide a practical warning signal for dialogue systems before the interaction fully breaks down.

---


### 280. [Scalable Semantic Steering of Embedding Projections](https://arxiv.org/abs/2607.03978)

**<font color=#1a73e8>作者：</font>** Wei Liu, Eric Krokos, Kirsten Whitley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Low-dimensional projections support interactive visual analysis of high-dimensional data embeddings, but their structure often does not align with analyst-defined semantic relationships. Recent LLM-augmented semantic steering methods address this gap by externalizing analyst intent from user-defined groups of seed examples, but they propagate intent through per-item LLM reasoning, causing LLM calls and cost to grow linearly with collection size. We propose a scalable semantic steering method that shifts semantic computation from individual items to user-defined groups. A single LLM call generates structured profiles for all groups, which are embedded and combined with seed centroids to form hybrid semantic prototypes. The method then propagates intent without retraining, using embedding-space soft assignment, abstention, and alignment-scaled updates before reprojection. On a 5K-document LitCovid corpus, our method achieves global alignment comparable to per-item LLM steering while reducing LLM calls by over three orders of magnitude. An image case study shows that the same prototype-based mechanism extends to multimodal embeddings. These results suggest that group-level representations can make semantic steering more practical for larger embedding collections.

---


### 281. [Energy-Aware System-Level Evaluation of Post-Quantum TLS on Embedded User Equipment over a Disaggregated 5G Network](https://arxiv.org/abs/2607.03988)

**<font color=#1a73e8>作者：</font>** Sanzida Hoque, Abdullah Aydeger  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The transition to quantum-resistant security is a critical priority for the next generation of mobile networks, particularly within the disaggregated architecture of 5G. This paper presents an energy-aware system-level evaluation of Post- Quantum Cryptography (PQC) integrated into the Transport Layer Security (TLS) handshake on embedded User Equipment (UE). Using Raspberry Pi 5s as representative embedded processing platforms, we evaluate the performance of NIST-standardized combinations of classical and post-quantum signature and key exchange mechanisms (KEM), incorporating direct on-device power measurements to estimate per-handshake energy consumption. Results experimentally validate a strong coupling between latency and energy consumption, indicating that execution time is the dominant contributor to energy cost. Hash-based signature schemes incur up to 4x higher latency and 2x energy compared to lattice-based alternatives, while the impact of KEMs is comparatively smaller. The analysis further reveals that overall system performance is primarily constrained by cryptographic computation and concurrency-induced contention rather than network transport effects. These findings provide practical guidance for PQC deployment in mobile environments and demonstrate that lattice-based signatures offer a more favorable balance between security, efficiency, and scalability for 5G systems.

---


### 282. [InSpace: Structure-Aware 3D Indoor Scene Generation from a Single 360° Image](https://arxiv.org/abs/2607.03990)

**<font color=#1a73e8>作者：</font>** Gwanhyeong Koo, Hyunsu Kim, Youngji Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in single image-to-3D generation have enabled high-quality asset synthesis, yet extending these capabilities to indoor scene generation remains challenging. Existing methods focus on asset-level generation while neglecting the structural layout, which is essential for downstream applications and serves as the spatial anchor for grounding assets. However, a single image with a limited field of view lacks the spatial coverage to recover a coherent global layout. To this end, we use a 360° image represented in equirectangular projection (ERP) and propose InSpace, a structure-aware framework for 3D indoor scene generation. InSpace comprises three stages: (1) estimating partial scene geometry as spatial priors, (2) generating coarse scene structure with view-selective cross-attention, and (3) producing detailed layout and asset geometry with textures through a global-local hybrid attention, using flow matching. We also propose ERP-FRONT, a paired ERP-Image-to-3D indoor scene dataset based on 3D-FRONT. Experiments show that InSpace generates complete 3D indoor scenes with structural layout, along with separate textured assets from a single ERP image, achieving strong performance across 3D and 2D metrics. Project Page: this https URL

---


### 283. [Knowing When to Stop: Predicting Execution-Consistency Convergence in Text-to-SQL](https://arxiv.org/abs/2607.03991)

**<font color=#1a73e8>作者：</font>** Yaron Anavi, Mor Aisenberg, Nadav Nesher 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Repeated LLM calls are the standard way to estimate how trustworthy a Text-to-SQL result is: run the pipeline multiple times, judge each SQL execution, and use the consistency of the verdicts as a confidence signal. The open question is when to stop, when the consistency has converged. We formulate this as a convergence-prediction problem and train a family of lightweight 1-D models that observe the running consistency trajectory and decide, at each step, whether further runs are unlikely to shift it materially, and we benchmark them against a principled Beta-Bernoulli stopping rule and a learned run-count baseline. On the BIRD benchmark and two production customer datasets, our method adapts its stopping point to each user question, halting sooner when consistency converges early and continuing longer when it converges late. We further show that the weak serial correlation between runs lets us permute their order as a training augmentation, controlled by a tunable shuffling weight. Performance stays consistent across the three datasets, and to mimic an imperfect production judge we inject noise into the correct/incorrect verdicts obtained by comparing the generated and ground-truth SQL results, showing that the method still predicts convergence reliably.

---


### 284. [Full Glyph Images Beat Token Embeddings: A Controlled Study for Transformers](https://arxiv.org/abs/2607.03994)

**<font color=#1a73e8>作者：</font>** Shuyang Xiang, Hao Guan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern language models generally represent text as sequences of discrete token embeddings, an assumption deeply rooted in current practice but rarely questioned. We challenge this representation, especially for Chinese, by replacing index-based token embeddings entirely with a single rasterized image of the character sequence, processed by a vision encoder composed of a shared ResNet and a shallow Vision Transformer. To isolate the role of input representation, we construct a dual-branch controlled framework in which both a Vision-based model and an index-based baseline share an identical decoder backbone, training objective, optimizer, and data curriculum. Any performance difference is therefore attributable to the input modality only. Across all tested decoder backbones, the Vision-based model consistently outperforms the baseline, reaching a peak accuracy of 0.429 versus 0.355 for the index-based baseline,that is, a 21% relative improvement, while converging in about half the number of training epochs. The advantage emerges especially within the first five epochs (under 21% of total data) and persists under moderate character corruption: the corrupted Vision model matches the clean index-based baseline. Ablation studies reveal that the advantage requires both spatially coherent input and a ViT encoder with 2D positional encodings. A cross-script comparison on English shows the advantage does not transfer directly to alphabetic writing systems, suggesting that the uniform visual density and radical structure of Chinese characters are enabling conditions. These findings suggest that transformers are more modality-agnostic than commonly assumed, and that discrete tokenization is not a fundamental requirement for Chinese language modeling.

---


### 285. [Directional Curvature from Armijo Backtracking: A Low-Cost Sharpness Probe and a Calibration-Free Learning-Rate Safeguard for Adam](https://arxiv.org/abs/2607.03998)

**<font color=#1a73e8>作者：</font>** Ashmitha R, Jörg Frochte  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The local sharpness of the loss, the top Hessian eigenvalue $\lambda_1$, determines the largest stable gradient step, but measuring it normally requires Lanczos or Hessian-vector iterations. We observe that a single Armijo backtracking line search already carries this information at the cost of a few forward passes: the accepted step $\alpha$ brackets the \emph{directional} curvature $q = g^\top H g/\|g\|^2$ within the multiplicative band set by the backtracking factor. Across CIFAR-10, Fashion-MNIST and Imagenette, $\log\alpha$ tracks $\log\lambda_1$ at Pearson $-0.91$ to $-0.95$, giving a low-cost online Edge-of-Stability reading. Used once at initialisation, this measurement yields a learning-rate cap (a safeguard, not a faster optimiser) that makes Adam robust to a too-large initial learning rate across more than three orders of magnitude ($10^{-3}$ to $3.0$), at about one percent overhead, and it is a no-op when the chosen rate is already safe. One probe is enough: periodic in-training probing adds no robust benefit. The raw-gradient probe exposes the mechanism but needs a safety factor calibrated to the architecture by a one-minute divergence sweep. Probing along Adam's own update direction removes this calibration: a single fixed safety factor $\kappa = 2$ avoids divergence on all nine architectures we test and across the full learning-rate grids of all four benchmarks, and the recipe transfers to AdamW unchanged.

---


### 286. [Separating Representation from Reconstruction Enables Scalable Text Encoders](https://arxiv.org/abs/2607.04011)

**<font color=#1a73e8>作者：</font>** Megi Dervishi, Mathurin Videau, Yann LeCun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While decoders have rapidly scaled, encoders have remained largely unchanged since BERT. We revisit this disparity by frozen backbone evaluation via probing. Under this lens, the representations of BERT encoders become increasingly $\textit{unexploitable}$ by frozen probes, despite improved perplexity. The misalignment originates in BERT's flat design, which couples representation learning to the token reconstruction loss. We propose $\textbf{CrossBERT}$, a two-part architecture that separates the learning of high-quality encoded representations from the rigid grounding of token reconstruction. This design further enables high masking ratios ($\ge 50\%$) and gradient collection over all tokens via a $\textit{Complementary Masking Strategy}$, respectively increasing throughput by $1.5$ to $2\times$ and sample efficiency by $2\times$. Overall, CrossBERT demonstrates monotonic scaling and superior performance on MTEB(eng, v2) and frozen GLUE benchmarks.

---


### 287. [SAGE: Synchronized Action-Gaze Recognition and Anticipation for Human Behavior Understanding](https://arxiv.org/abs/2607.04017)

**<font color=#1a73e8>作者：</font>** Chenyi Kuang, Nakul Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human object interaction (HOI), gaze pattern, and their anticipation are intricately linked, providing valuable insights into cognitive processes, intentions, and behavior. However, most existing models handle gaze and actions separately, missing both their interdependence and the advantages of a unified solution. This paper presents a novel unified framework, SAGE (Synchronized Action-GazE), which integrates simultaneous recognition and anticipation of both HOI and human gaze into a single unified end-to-end trainable model. Our approach leverages a transformer-based architecture and incorporates gaze data into spatiotemporal attention mechanisms to simultaneously predict current and future human actions and gaze behavior. We explore this bidirectional relationship between gaze and actions under different scenarios, whether requiring a close-up, detailed view (egocentric) or a wider, more contextual view (exocentric), making our framework versatile for various applications. Additionally, due to lack of datasets for comprehensive analysis of both HOI and gaze in exocentric videos, we establish a new benchmark Exo-Cook to facilitate further research in this domain. Experiments on three benchmark datasets: VidHOI, EGTEA Gaze+, and Exo-Cook show that jointly modeling gaze and actions across current and future frames achieves consistently strong results, often surpassing specialized state-of-the-art models tailored to individual tasks. By unifying actions and attention in a comprehensive way, our work lays the groundwork for more intuitive human-machine interaction.

---


### 288. [A Unified Algebraic Framework for Classification Performance Evaluation](https://arxiv.org/abs/2607.04028)

**<font color=#1a73e8>作者：</font>** Ronaldo C. Prati  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a unified algebraic framework for classification performance evaluation that encompasses binary, multiclass, multilabel, ordinal, hierarchical, cost-sensitive, and soft-label settings within a single formalism. The foundation is a representation of actual and predicted labels as binary indicator matrices, combined with three aggregation operators -- global, column-wise, and row-wise -- that correspond exactly to micro, macro/weighted, and exemplar averaging. Any binary performance measure expressed in terms of true/positive/negative counts extends automatically to all settings by substituting these operators, generating multiclass and multilabel versions without measure-specific derivations. The framework further accommodates soft classifier outputs via argmax or thresholding, soft ground truth via triangular norms, ordinal classification via membership functions or cumulative encodings, and cost-sensitive evaluation via a cost matrix that subsumes MAE and MSE as special cases. We establish several theoretical results: micro-averaging equals denominator-weighted macro-averaging; the product $t$-norm is the unique one preserving the confusion-matrix partition; skew-invariant measures are characterised as functions of recall and specificity; and micro-precision, micro-recall, and micro-$F_1$ are all equal to accuracy in multiclass settings. Empirical illustrations on synthetic and real data confirm the theoretical findings.

---


### 289. [Data Structures for Private Token Transfers in TEE-Based Networks](https://arxiv.org/abs/2607.04032)

**<font color=#1a73e8>作者：</font>** Blake Regalia, Benjamin Adams  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted execution environment (TEE) based confidential smart contract networks promise privacy but remain vulnerable to storage access pattern attacks that can link senders and recipients in token transfers. When contracts update recipient balances during transfers, the unique storage keys accessed reveal transaction relationships even when data is encrypted. This paper introduces two novel data structures to address this vulnerability: the Delayed Write Buffer (DWB) and the Bitwise-Trie of Bucketed Entries (BTBE). The DWB delays recipient balance updates by buffering pending transfers and randomly settling entries, breaking the direct correlation between transfer execution and recipient storage access. The BTBE further enhances privacy by grouping addresses into constant-sized buckets, preventing flooding attacks and creating anonymity sets for balance queries. Additionally, we present a private notification system enabling real-time, privacy-preserving push notifications for confidential contracts. Our domain-specific approach leverages the unique characteristics of token transfers -- asymmetric balance updates and tolerance for delayed settlement -- to achieve practical performance with probabilistic anonymity guarantees.

---


### 290. [OmniOpt: Taxonomy, Geometry, and Benchmarking of Modern Optimizers](https://arxiv.org/abs/2607.04033)

**<font color=#1a73e8>作者：</font>** Siyuan Li, Jiabao Pan, Yumou Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizer selection for large-scale model training has become a system-level design decision constrained jointly by compute, memory, tuning budget, and task diversity, yet the landscape of over one hundred methods remains fragmented. We therefore present OmniOpt, a unified survey and benchmark cookbook of optimizers for the research community. OmniOpt rests on four coupled components. First, we treat every optimizer update as a structured transformation through a five-stage meta-pipeline, and show that most methods engage only one or two of these stages. Second, we use norm-constrained linear minimization oracles (LMOs) to unify different optimizers. Third, these two views ground a dual-dimension taxonomy, one dimension assigning each method to a mechanism family and the other recording the measurable training objectives it aims to improve. Fourth, and at the core of this paper, we instantiate the full taxonomy in a unified cross-domain benchmark spanning representative optimizers, model scales, and training regimes from language model pretraining to image classification, systematically analyzing each method family across multiple effect objectives and laying out their trade-offs. OmniOpt thus supplies the research community with an operational coordinate system for selecting optimizers under explicit mechanism and objective assumptions, and charts a direction for the future development of the optimizer community.

---


### 291. [Reward-Gated On-Policy Distillation](https://arxiv.org/abs/2607.04037)

**<font color=#1a73e8>作者：</font>** Mohammad Sadegh Akhondzadeh, Vijay Lingam, Atula Tejaswi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation is a powerful way to transfer reasoning ability from a strong teacher to a smaller student: the student samples trajectories from its own policy, and the teacher provides dense token-level supervision on the states the student actually visits. However, this supervision is not always reliable: a teacher can assign high likelihood to plausible but incorrect solutions, or low likelihood to correct student solutions that follow different reasoning paths. Unconditionally distilling the teacher can therefore reinforce bad modes or erase useful student behavior. To address these limitations, we introduce RG-OPD: Reward-Gated On-Policy Distillation that uses verifier feedback to decide when teacher logits should be trusted. RG-OPD bridges sparse verifier rewards and dense teacher logits, preserving token-level supervision while filtering misleading teacher signals. Across reasoning and coding benchmarks, RG-OPD produces stronger distilled students, outperforming both vanilla reverse-KL distillation and the recent TSD-KD baseline. At 1K generation length, RG-OPD improves over reverse-KL by 2.9 points and over TSD-KD by 4.9 points; in the long-generation setting, it improves over the untuned student by 8.2 points. Our code is available at this https URL.

---


### 292. [SiamJEPA: On the Role of Siamese Student Encoders in JEPA](https://arxiv.org/abs/2607.04044)

**<font color=#1a73e8>作者：</font>** Makoto Yamada  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, Joint Embedding Predictive Architectures (JEPAs) have attracted significant attention in the computer vision and machine learning communities as a promising framework for self-supervised representation learning. Unlike masked autoencoders that reconstruct pixels, JEPA models learn representations by predicting latent embeddings of masked regions. Existing JEPA-based methods, such as I-JEPA and V-JEPA, typically employ a single encoder in the student network. In contrast, using Siamese encoders for student network is more naturally aligned with brain-inspired representation learning frameworks, yet their role in JEPA models remains largely unexplored. In this paper, we investigate the effect of Siamese student encoders in JEPA-based representation learning. To this end, we propose SiamJEPA, masked Siamese student encoders equipped with an exponential moving average (EMA) teacher network. SiamJEPA can also be viewed as a JEPA formulation of the brain-inspired representation learning model PhiNet. Through extensive experiments on ImageNet linear probing, we demonstrate that Siamese encoders act as an effective regularizer for the JEPA objective, improving representation separability and accelerating learning during the early stages of training. Furthermore, SiamJEPA consistently outperforms comparable single-encoder JEPA variants under limited training budgets and achieves higher linear probing accuracy than Masked Autoencoders (MAE) which requires longer training. Our findings reveal that Siamese student encoders are not merely an architectural choice but constitute an important inductive bias for predictive representation learning. These results provide new insights into the design of JEPA-based models and suggest that incorporating Siamese student architectures offers a simple yet effective approach for improving self-supervised representation learning.

---


### 293. [What is Left for Us? Second Scholarship Against the Degradation of Research by AI](https://arxiv.org/abs/2607.04049)

**<font color=#1a73e8>作者：</font>** Claudio Novelli, Luciano Floridi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We argue that generative AI can degrade research by eroding the very practices through which scholarly judgement is formed and academic trust is built. As constitutive conditions for the production and validation of knowledge, these practices cannot be reduced to the final outputs of research, which is what AI so effectively simulate. Accordingly, when researchers delegate central tasks of inquiry to systems like Large Language Models, they may stop enacting these practices and, with them, lose access to the formation they provide. An individual research output generated by AI may even appear improved but the researcher behind it fails to develop. Against this risk, merely keeping humans in the loop as prompters or quality checkers of AI outputs is insufficient to preserve research as a site of intellectual formation. What is needed instead is a renewed commitment to research as a lived practice in which judgement is formed gradually, often through frictions, and participation in a scholarly community. We defend it because it rests on four sources and warrants of research that cannot be automated: tacit knowledge, personal commitment, socialisation, and deep reading. This practice enacts what we call second scholarship, by which we understand the reappropriation of scholarly craft, chosen out of a critical experience of what generative AI can and cannot do. What cannot and should not be delegated becomes what research communities must value and answer for. This is what is left for us.

---


### 294. [Securing Deep Learning Hardware: A Survey of Side-Channel Vulnerabilities and Countermeasures](https://arxiv.org/abs/2607.04055)

**<font color=#1a73e8>作者：</font>** Zahra Mohammadi, Mona Hashemi, Siamak Mohammadi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As deep learning models are increasingly deployed in critical sectors such as healthcare, finance, and security, ensuring their protection against emerging threats has become crucial. Among these threats, side-channel attacks (SCAs) represent a particular challenge since they can extract sensitive information such as model architectures, parameters, and even user inputs without requiring direct access to the model. By leveraging the physical and micro-architectural properties of the hardware, attackers can compromise systems. This survey begins by classifying leakage sources and attacker objectives, then analyzes representative studies that demonstrate practical side-channel exploits against deep-learning hardware. It also reviews existing defenses aimed at mitigating these vulnerabilities and concludes by outlining key open research challenges and potential future directions.

---


### 295. [PreSIST: Vision-Language-Informed Object Persistence Prediction in Open-World Scenes](https://arxiv.org/abs/2607.04057)

**<font color=#1a73e8>作者：</font>** Amanda Adkins, Tarunvidyut Ravisankar, Joydeep Biswas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robots deployed over long periods must reason about environments that change over time. Existing long-term perception systems often address object change reactively, updating their maps only after revisiting a scene and observing that an object has moved. Instead, robots should reason proactively about how long objects are likely to persist using the context in which they appear. For example, a car at a traffic light and a car in a parking spot share the same semantic class, but their contexts imply different persistence durations. We propose PreSIST (Predictive Scene-conditioned Instance Survival over Time), a method for predicting whether an observed object will remain in its last seen pose at arbitrary future times. PreSIST estimates instance-level persistence priors from object properties and scene context, then integrates these priors with a probabilistic persistence filter as observations become available. Its key insight is that the reasoning capabilities of vision-language models (VLMs) can relate scene context to likely object use and human activity, enabling persistence prediction before long-term observations are available. We develop two interchangeable variants: PreSIST-Lang, which estimates persistence priors using a VLM, and PreSIST-Vis, a novel vision-only model trained using PreSIST-Lang pseudo-labels for efficient deployment. Experiments on a new dataset of in-the-wild object persistence annotations show that PreSIST-Lang and PreSIST-Vis outperform baselines on open-world persistence prediction.

---


### 296. [Speaker-Disentangled Chunk-Wise Regression for Syllabic Tokenization](https://arxiv.org/abs/2607.04064)

**<font color=#1a73e8>作者：</font>** Ryota Komatsu, Kota Kawakita, Takuma Okamoto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unsupervised syllabic tokenization aims to learn discrete syllabic tokens that capture latent linguistic content-related structure from raw speech. Recent syllabic tokenization methods employ teacher-student distillation of the pretrained HuBERT to organize latent speech frame representations into syllabic segments. However, when trained with an utterance-level cross-entropy objective, the model predicts speaker identity rather than linguistic content, thereby compromising the purity of syllabic tokens. To address this problem, we propose a speaker-disentangled syllabic tokenizer that regresses speaker-perturbed student representations toward clean teacher targets within fixed-length chunks. Experimental results demonstrate that our proposed method achieves state-of-the-art performance in syllable boundary detection and syllabic segment clustering. Moreover, a speech language model trained on our syllabic tokens achieves a 7% relative improvement in syntactic and semantic understanding over the phone-level SpiRit-LM.

---


### 297. [Enhancing Implicit Neural Representations with Image Feature Embedding for Unsupervised Cardiac Cine MRI Reconstruction](https://arxiv.org/abs/2607.04069)

**<font color=#1a73e8>作者：</font>** Donghang Lyu, Marius Staring, Yiming Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cardiac cine Magnetic Resonance Imaging (MRI) is a critical diagnostic tool that provides dynamic insights for radiologists. To accelerate acquisition, under-sampled k-space data is often used, requiring reconstruction methods that combine coil sensitivity encoding with prior information to recover missing data. Deep learning approaches have gained more attention for leveraging data-adaptive priors. While supervised learning approaches are a common choice, they depend on fully sampled reference data, which is not always available. Unsupervised methods eliminate the need for fully sampled reference data, which can be advantageous in cardiac cine MRI reconstruction. Among them, implicit neural representations (INRs) have shown great potential due to their simple architecture and good quality reconstructions. In this work, we propose an image-domain dual-branch INR framework, termed I-FP-INR, which extends the original INR design by introducing an additional feature-processing branch. This design aims to extract complementary feature embeddings to enhance the overall representation, thereby benefiting reconstruction. Extensive evaluations on both public datasets and in-house data show consistent improvements over baseline methods in reconstruction quality, with strong robustness across varied scenarios.

---


### 298. [Conductance-Repair Evidence Graphs for Prospective Security Retrieval](https://arxiv.org/abs/2607.04070)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Taylan Alpay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security retrieval is often evaluated as ranking over complete evidence, but operational triage is prospective: CVE descriptions, weakness metadata, fix commits, EPSS scores, KEV membership, validation-vector metadata, and side-channel benchmark routes arrive through separate channels, and many are missing, delayed, poisoned, or visible only after the decision time. We introduce conductance-repair evidence graphs, a timestamped framework in which retrieval is performed over a temporal admissibility mask and missing channels are widened by a deterministic graph-flow recurrence rather than by a learned predictor. The method emits a repair certificate recording source probes, decision time, withheld edges, repaired channels, forbidden post-decision edges, backend availability, numerical deviation, and verifier results. The theoretical layer gives an adaptive \(\lceil\log_2 N\rceil\) lower bound for missing-channel identification, an NP-hardness result for minimum harmful repair, and a fixed-parameter certified search bound for \(q\) questionable channels. The current artifact materializes 30 deduplicated public security records, 57 terms, and 58 withheld admissible document-term edges. Under random edge withholding, conductance repair changes recall@\(k\) from 0.017 to 0.069 and average precision from 0.062 to 0.060, while a synthetic security fixture improves recall@\(k\) from 0.055 to 0.099; the public AP drop exposes a limit of broad admissible repair under random edge corruption. The implementation benchmarks the same flow/SVD/einsum kernel under NumPy, PyTorch, JAX, and TensorFlow when available, recording unavailable backends rather than silently substituting them. BBBC019 and LIVECell metadata are retained only as structural controls for sparse evolving source channels, with no clinical or biological performance claim.

---


### 299. [FedSPM: Routing-Enabled Federated Learning under Dual Heterogeneity via Semiparametric Mixture](https://arxiv.org/abs/2607.04085)

**<font color=#1a73e8>作者：</font>** Zijian Wang, Pengfei Li, Guangyu Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Routing-prediction federated learning has emerged as a new paradigm that reframes inter-client heterogeneity as a resource for system-level intelligence: at inference time, the server routes each external query to the best-matched client for prediction. Existing approaches, however, typically treat each client as internally homogeneous, overlooking latent subpopulations within local data. For example, patients with the same diagnosis at one hospital may exhibit morphologically distinct disease subtypes. The coexistence of inter-client and intra-client heterogeneity, which we call dual heterogeneity, can impair both routing and prediction. To address this challenge, we propose FedSPM, a routing-enabled semiparametric mixture framework that represents each client using client-specific latent components. Each component combines a predictive distribution for classification with a feature distribution for routing. To flexibly model feature distributions while effectively sharing information across clients, FedSPM models their density ratios relative to a common nonparametric measure estimated via empirical likelihood. We develop a federated expectation-maximization algorithm that optimizes a tractable surrogate and prove convergence of the exact profiled objective at the standard $\mathcal{O}(1/\sqrt{T})$ rate when the surrogate errors are properly controlled. Experiments on controlled benchmarks and real-world medical data demonstrate consistent improvements in routing and prediction under dual heterogeneity. Code is available at this https URL.

---


### 300. [PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents](https://arxiv.org/abs/2607.04089)

**<font color=#1a73e8>作者：</font>** Sukanta Ganguly  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lifelong agents need more than larger context windows and better retrieval. They need memories that can persist, evolve, and be corrected without forcing the serving stack to recompute the same history on every turn or silently reuse stale runtime state. We present PLACEMEM as a systems position on lifelong-agent memory, instantiated by an executable control-plane prototype. The central claim is that agent memory should be represented as versioned capsules that unify semantics, provenance, validity, and reusable runtime state under one correction-aware identity. In the current prototype, capsules drive prompt-level text retrieval, KV-aware routing, and cascading invalidation over live streamed backends; prospective layer-frontier replay is intentionally framed as a deeper integration agenda rather than a claimed engine feature. We describe a vLLM-first prototype with persistent capsule state, concurrency-safe invalidation, an OpenAI-compatible routing sidecar, a typed metadata contract, and a benchmark harness that measures live first-token latency, reuse, and post-correction behavior. The result is both an executable artifact that demonstrates correction-aware control-plane behavior today and a concrete roadmap for replay-aware serving integration in future lifelong-agent systems.

---


> [!TIP]
> 当前位于：**251-300**（第 6/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

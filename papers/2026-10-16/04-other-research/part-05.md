# 📦 其他研究 | 2026年10月16日

> 本类共 **264** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-264](./part-06.md)

---

### 201. [Retrieval Over Training: Similarity search-based Model Selection for Time Series Anomaly Detection](https://arxiv.org/abs/2610.20243)

**<font color=#1a73e8>作者：</font>** Christos Panourgias, Roberto Stanzione, Adrien Petralia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection is a fundamental task for time-series analytics, with important implications for the downstream performance of many applications. Despite the large number of anomaly detection methods proposed in the literature, recent benchmark studies have shown that no single detector performs best across highly heterogeneous time series. Therefore, a practical and scalable solution is to develop a model-selection method that, for a given time series, selects the anomaly detector most likely to perform well. Nevertheless, the model selection approaches proposed in the literature suffer from a significant drop in accuracy when applied in Out-of-Distribution (OOD) settings. In this paper, we tackle the aforementioned limitation and propose RAMSAD, a retrieval-based framework for model selection in time-series anomaly detection. Given a new time series, our method queries a knowledge base of previously observed instances, retrieves the top-k most similar series, and transfers detector recommendations from their performance profiles. The framework can operate with standard similarity measures as well as embedding-based representations. Our results show that RAMSAD outperforms existing baselines in In-Distribution (ID) settings and is the most robust selector in OOD, where, when selecting a small subset of detectors, it matches or exceeds ensembles that run the entire detector pool, at a fraction of their cost. Overall, we demonstrate that similarity-based retrieval constitutes a strong and efficient foundation for model selection in time-series anomaly detection.

---


### 202. [Contrastive uncertainty learning for robust multi-structure segmentation in lower-pelvic MR](https://arxiv.org/abs/2610.20251)

**<font color=#1a73e8>作者：</font>** Bilal Sidiqi, Yipei Wang, Wen Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Boundary delineation of anatomical structures in prostate MRI is often compromised by regional ambiguity. Automated segmentation methods relying on global overlap loss functions tend to be insensitive to surface deviations, leading to significant errors in ambiguous regions. Most existing uncertainty-aware methods treat uncertainty as a post-hoc quality indicator or prediction filter. We propose Contrastive Uncertainty Learning (CUL), a supervised framework that uses predictive uncertainty to directly guide representation learning. Using Monte Carlo Dropout, CUL identifies voxel-wise uncertainty and structures the embedding geometry accordingly: low-uncertainty, correctly predicted features form stable voxels while high-uncertainty or misclassified features are actively repelled, preventing feature collapse at difficult boundaries. We evaluate CUL on a 589-scan 3D prostate MRI multi-structure segmentation task (8 anatomical structures) using a ViT with UperNet decoder architecture. Average Dice ($83.38\%$) remains comparable to the baseline ($83.35\%$), while surface distance decreases significantly ($p<0.001$) across 6 of 8 anatomical structures. A hard-case analysis reveals a $22{\times}$ asymmetry between significantly improved and degraded cases ($18.8\%$ vs $0.9\%$). Ablation studies show that removing uncertainty-guided sample selection eliminates improvements for the transition zone, while replacing the contrastive objective with a boundary loss additionally removes bladder improvements, demonstrating that both uncertainty-guided sampling and the contrastive objective are essential for the observed gains. These findings demonstrate that the proposed uncertainty-guided representation learning is a useful mechanism for reducing the risk of extreme errors in safety-critical medical segmentation

---


### 203. [Adversarial Reinforcement Learning for Robust Planetary Landing](https://arxiv.org/abs/2610.20252)

**<font color=#1a73e8>作者：</font>** Miguel Leiva-Vélez, Nicolas Gaston-Rozado, Andrea Scorsoglio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (DRL) policies for planetary landing and other aerospace guidance, navigation, and control tasks are commonly trained under randomized disturbances to improve robustness. However, typical stochastic perturbation sampling assumes independent variations, whereas real mission disturbances often exhibit spatial and temporal correlation and cannot be reproduced through independent random draws. This work investigates adversarial reinforcement learning to discover challenging off-nominal conditions. A secondary agent generates physically constrained perturbations that degrade the performance of a landing controller, forming an asymmetric sequential zero-sum game. Training proceeds in three stages: baseline controller learning, robustness enhancement with stochastic perturbations, and an iterative adversarial phase in which the controller and disturbance generator are alternately optimized. Preliminary experiments in a three-degree-of-freedom landing environment show that adversarial disturbances reveal vulnerabilities missed by conventional randomization and provide early indications that, with a more extensive training campaign, the approach can yield improved robustness and stronger generalization under previously unseen perturbation regimes.

---


### 204. [GLoD-LVSM: Learning Geometry-Grounded Continuous-LoD Scene Representations for Large View Synthesis Models](https://arxiv.org/abs/2610.20254)

**<font color=#1a73e8>作者：</font>** Weikai Lin, Nicholas Milef, Carl S Marshall 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large view synthesis models (LVSMs) reconstruct scenes from sparse views and render novel views quickly, but they incur unnecessary storage and rendering costs due to token redundancy. We present GLoD-LVSM, a compact, geometry-grounded scene representation for LVSMs with continuous levels of detail. First, instead of learning a fixed set of scene anchor initializations, GLoD-LVSM learns a continuous field that initializes a flexible number of anchors to match the desired budget. A condenser then aggregates scene information into these anchors, with both the field and condenser trained end-to-end. Second, the condenser infers reference-token and anchor geometry to guide compression through geometry-grounded attention, improving rendering quality and enabling frustum culling during decoding. Compared with existing LVSM scene-compression baselines, GLoD-LVSM achieves the best trade-off between rendering quality and scene token count. Compared with the uncompressed base model, GLoD-LVSM reduces the scene-token count by 33.4% and accelerates rendering by $1.23\times$ with no quality loss. Under a relaxed quality-loss budget, the reduction increases to 85.5%, with $3.00\times$ rendering speedup. Further analysis reveals that view-synthesis supervision yields emergent scene depth and self-organized anchors that align with surfaces and adapt their density to local texture complexity. Beyond rendering, we further show that our scene representation also supports scene-semantic understanding, highlighting its potential for broader downstream tasks.

---


### 205. [Long-Horizon RL Needs Muon](https://arxiv.org/abs/2610.20256)

**<font color=#1a73e8>作者：</font>** Kai Ruan, Jinghao Lin, Tao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents must coordinate reasoning, tool use, and environment feedback over extended interactions. Learning from sparse outcome rewards requires weighting trajectories of different lengths and updating the policy while rollouts are still being collected. We examine a single-rollout asynchronous recipe combining Muon, token-averaged loss, truncated importance sampling, and auxiliary length and tool-error penalties. Single-rollout sampling allows asynchronous learning without waiting for multiple trajectories for the same issue. We study optimizer choices and recipe components for repository-level issue resolution across two model families. The evaluated training runs show higher training success with the full recipe than with the baselines.

---


### 206. [FUSE: Fairness-aware Update Screening against Byzantine Exploitation in $q$-Fair Federated Learning](https://arxiv.org/abs/2610.20264)

**<font color=#1a73e8>作者：</font>** Tiantong Sun, Jinlin Liu, Xingru Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Client-level fair federated learning, in the form of $q$-fair federated learning ($q$-FFL), agnostic federated learning, or tilted empirical risk minimization, has emerged as an attractive solution to equalize utility across heterogeneous clients. This paradigm grants high-loss clients greater relative influence, while a central server aggregates their loss-weighted updates into a single shared model. Yet, the Byzantine robustness of $q$-fair federated learning has been largely neglected, leaving the server unable to tell legitimate fairness-induced amplification from malicious update scaling. To address this critical gap, we formalize the problem of Byzantine-robust $q$-fair federated learning under an \emph{update-only interface}, in which the server observes nothing but the fairness-scaled client updates. Our analysis under shared class-conditional label skew shows that fairness scaling preserves the nonnegative class-mixture structure of honest updates, while replacing their unit-sum constraint by a client-dependent radial scale. Moving beyond magnitude-based screening, we show that this warped geometry supplies two complementary tests, one radial and one structural, that a single norm cannot provide. We then introduce FUSE, a structure-aware robust aggregator that uses a small trusted labeled dataset for coefficient recovery, scale and cone-consistency screening, and post-screening step-size control. Across four benchmarks and seven Byzantine attacks, FUSE improves seed-wise worst-attack accuracy over the strongest baseline on each benchmark by 3.9--30.1 percentage points, while largely preserving the influence of the high-loss honest clients that fairness is meant to protect.

---


### 207. [Resolution Allocation with Learnable Resizing and Spectral Filter Parameterization](https://arxiv.org/abs/2610.20274)

**<font color=#1a73e8>作者：</font>** Wei Wu, Eric C. Larson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learnable downsampling and spectral-domain filter parameterizations have each made convolutional networks more flexible, but their interaction has not been systematically examined. We bridge this gap by examining convolutional kernels learned in the spatial and spectral domains, together with learned downsampling ratios under a cropped resizing implementation. We find that spectral and spatial kernels respond differently to learned resolution allocation, with larger gains for the spectral kernel. We observe this consistently on three datasets (EuroSAT, CIFAR-10 and STL-10) and at two model sizes (differences in accuracy gain of +0.013 to +0.028 on held-out test sets). Part of this difference reflects the greater gain of the spectral kernel from retaining more spatial area, but the difference remains positive when total retained area is matched. This pattern is observed across datasets and model sizes, although its magnitude and dependence on the complexity budget vary with model size and the resizing implementation.

---


### 208. [TANGO: RNA Topology and Geometry Co-Design](https://arxiv.org/abs/2610.20277)

**<font color=#1a73e8>作者：</font>** Tianmeng Hu, Biao Luo, Ke Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing RNA sequences that satisfy target tertiary-structure objectives is an important problem in RNA engineering, with broad applications in synthetic biology and therapeutics. Existing 3D RNA design methods have made substantial progress, but they largely treat the target fold as a geometry-only objective. This is incomplete for RNA, whose functional folds are specified not only by tertiary geometry but also by secondary base-pairing topology. We therefore formulate RNA inverse design as a topology-and-geometry co-design problem and propose TANGO, a multi-objective multi-agent reinforcement learning framework for this task. TANGO adopts a staged curriculum: it first learns a topology-aware policy from secondary-structure targets, then transfers this policy to tertiary-structure targets to train a general co-design model, and finally applies frontier-guided fine-tuning to refine target-specific trade-offs among secondary-structure fidelity, tertiary-structure fidelity, and sequence diversity. Experiments show that TANGO generates diverse and novel designs, improving tertiary- and secondary-structure performance by 18.3% and 52.7%, respectively, over the strongest baseline.

---


### 209. [A Valid Watermark Is Not a Valid Identity: Spatial-Spectral Adversarial Face Evasion with Watermark Preservation](https://arxiv.org/abs/2610.20278)

**<font color=#1a73e8>作者：</font>** Jefferson David Rodriguez Chivata, Davide Ghiani, Simone Maurizio La Cava 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial image watermarking can support traceability and certification in biometric pipelines, but provenance or manipulation detection alone does not guarantee reliable biometric identity. We introduce a watermark-preserving face evasion attack that targets this gap under a black-box watermarking setting, without access to the watermarking components. The proposed PGD-L_2 attack guides adversarial perturbations with spatial and spectral preservation terms to reduce face-recognition similarity while limiting pixel-level distortion and high-frequency changes that may interfere with hidden watermark cues. Evaluated on controlled facial images with two watermarking schemes, two face-recognition models, and two datasets, the attack achieves evasion rates above 92% at operational thresholds while preserving watermark recovery above 93% for StegaFormer and above 99.7% for FaceSigns, with visual quality above 47dB PSNR at epsilon_2=2.0. These results expose a structural gap in watermark-based facial certification: a face image can remain watermark-valid and visually faithful while becoming biometrically unreliable.

---


### 210. [Neural POS Tagging for the Low-Resource Saraiki](https://arxiv.org/abs/2610.20279)

**<font color=#1a73e8>作者：</font>** Usman Nawaz, Muhammad Junaid Iqbal, Muhammad Asaf 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Part-of-speech tagging is a fundamental sequence labeling task and an important component for many downstream natural language processing applications. However, Saraiki, written from right to left in a Perso-Arabic script, remains an under-resourced Indo-Aryan language, despite being spoken as a mother tongue by 28,849,579 people (approximately 28.9 million) according to Pakistan 7th Population and Housing Census 2023. This paper presents a manually annotated Saraiki Universal POS tagging dataset developed from plain-text. We annotated the text with 17 POS categories. We evaluate three pretrained transformer encoders under the same fine-tuning setup: XLM-RoBERTa base, Urdu RoBERTa small, and multilingual DistilBERT. Experimental results over five random seeds show that XLM-RoBERTa base achieves the best performance, with 87.29% +/- 0.21% development accuracy and 88.60% +/- 0.21% test accuracy. Urdu RoBERTa small and multilingual DistilBERT also provide competitive results, suggesting that multilingual and related-script pretrained encoders are effective for Saraiki UPOS tagging. The dataset, evaluation setup, and baseline results introduced in this work provide a benchmark for future research on Saraiki NLP and low-resource sequence labeling.

---


### 211. [From Semantic Editing Intentions to Persistent Parametric Controls for AI-Assisted Image Editing](https://arxiv.org/abs/2610.20283)

**<font color=#1a73e8>作者：</font>** Rifat Mehreen Amin, Michelle Dutoit, Anton Rockenstein 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-powered image editing increasingly allows users to express high-level editing intentions, yet how these intentions are translated into concrete editing actions often remains difficult to understand. We present Atelier, a semantic image editing tool that uses image semantics and user intent to determine which editing controls to surface and how to initialize them. Guided by a formative study with eight image-editing practitioners, Atelier composes context-specific, directly manipulable controls that users can refine rather than committing AI interpretations directly to finished edits. In a within-subjects study with 12 practitioners, participants preferred AI-composed controls, described them as supporting creative exploration, and actively refined AI proposals. However, experiences of control were mixed, and interviews highlighted limited insight into why particular controls and values were proposed. Our findings suggest that making AI interpretations actionable through manipulable controls can support exploration and refinement, but actionability alone does not make those interpretations transparent to all users.

---


### 212. [Predicting Unseen Scientific Interactions: Conditional Flow Models Hallucinate Non-Additive Effects](https://arxiv.org/abs/2610.20288)

**<font color=#1a73e8>作者：</font>** Sam Gijsen, Moritz Seiler, Kerstin Ritter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional generative models are increasingly used for scientific prediction beyond the direct training support. Yet scientific questions often concern whether one intervention changes the effect of another. Such interactions can be of primary interest while explaining little of the total variation, allowing models to appear accurate overall without recovering the relevant scientific effect. It remains unclear how these models learn interactions and when these successfully extrapolate to unseen conditions. We therefore study interaction recovery in flow-matching models using a physiological time-series simulator, drug dose-response data, combinatorial cell perturbations, and molecular conformer generations, where we separate recovery from hallucinated interaction structure. In the controlled setting, individual effects are learned much earlier than interactions and models hallucinate interactions where none exist. Across settings, we find qualitatively different generalization problems, with successful prediction depending on whether condition structure continues from observed to held-out targets. When it does, interactions are recoverable. If not, models can generate plausible responses while missing the interaction. We furthermore find that hallucinations increase as targets become less identifiable, and that successful interaction recovery in output space can fail under nonlinear readouts. Finally, we show that aggregate fidelity metrics can conceal whether models learn and extrapolate interactions.

---


### 213. [MMLA-RSI: Recursive Self-Improvement through RTT and RTMA](https://arxiv.org/abs/2610.20294)

**<font color=#1a73e8>作者：</font>** Junyi Zou, Avrova Donz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An agent can improve its behavior within an unresolved problem by changing how it acts and which experience it retains. We propose MMLA-RSI, a recursive self-improvement scheme with two implementations in Memory-Mediated Learning Architecture: Reasoning-Time Training (RTT) changes the policy state $\Phi$, while Reasoning-Time Memory Adaptation (RTMA) changes authoritative memory $M$. Each route also makes its adaptation method an object of improvement. A current numerical updater trains the policy proposing its successor; a current memory manager chooses the records available to the process proposing its successor. An independently admitted successor takes over the same role in the next generation. We give bounded executable rule languages, shared task/proposal interfaces, and one algorithm for either route or their composition. The RTT instance changes scalar schedules in a clipped-momentum update. The RTMA instance chooses NULL or a complete-row write with possible eviction. A fixed interpreter, trusted committer, and independent evaluator bound what can change. State versions, read closures, and conditional properties describe causal execution, accepted transitions, and finite work. Existing numerical-component studies motivate the construction. In four-candidate program selection, retaining LARC feedback updates reduces expected error by 24.65 and 36.65 percentage points for two trained initializations. In chronological continuous-integration replay, feedback binding is positive while retention increases loss. Completed SQL studies improve substantially over an unadapted substrate but do not establish the required additional online benefit. These results characterize their declared components. The two recursive routes and their joint realization are specified here; their beneficial recursive chains and discovery efficiency remain to be evaluated.

---


### 214. [Event Cameras versus Frame Cameras for Synthetic-Aperture Imaging: A Simulation Study](https://arxiv.org/abs/2610.20309)

**<font color=#1a73e8>作者：</font>** Jakob Hinterholzer, Mohamed Youssef, Oliver Bimber  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic-aperture imaging (SAI) removes occluders such as foliage by integrating many views of a scene along a camera path. It has so far been used mainly with frame cameras. We ask whether an event camera has advantages for SAI, and answer the question in simulation, where both sensors see exactly the same scene and the same camera movement. A densely rendered Blender sequence is turned into frames with an EMVA~1288 noise model of an industrial global-shutter camera, and into an event stream with the v2e simulator parameterized like a Sony IMX636. The frames are integrated with the existing airborne optical sectioning renderer. For the events we add a new integration path that projects every single event onto the focal plane at its own interpolated pose, so no events have to be binned into frames. We compare the two sensors in three main runs and an additional dark high-speed test. In a bright scene at 25,m/s the frame camera records only three images on the path and cannot remove the occluder, while the event camera reconstructs the target, even after an event-rate controller drops most of its events to fit the camera link. At the same speed in a 5,lux scene the event camera no longer resolves the target either. In a 5,lux scene at 5,m/s both sensors reconstruct the target at similar quality. We also compare the data one traversal of the aperture costs. At high speed the capped event stream still shows the target at the same data volume as the three frames. At 1,m/s we compare both cameras at two matched data budgets, and there the event camera has no advantage over the frame camera in reconstruction quality. The data rate of the event camera depends on the scene and is highest exactly in the fast bright scenes where it is needed most.

---


### 215. [Building Sound Evaluation Practices for Rust-Based Security Frameworks](https://arxiv.org/abs/2610.20315)

**<font color=#1a73e8>作者：</font>** David Paaßen, Lucas Davi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Background: Rust is a modern programming language known for its focus on usability, concurrency, and security. However, empirical studies reveal that Rust is still affected by software vulnerabilities, with hundreds of memory safety issues found in Rust programs, including Rust's standard library. As a result, additional tool-assisted security testing is crucial to enhance the security of Rust code. Evaluating such tools, however, is highly complex. While there is substantial research on evaluating C/C++ security frameworks, including test sets, serious issues in published evaluations have been identified, undermining their scientific soundness and reproducibility. In practice, selecting an inadequate implementation (e.g., a fuzzer) can lead to missed vulnerabilities ultimately compromising a program's security. Aims: Our methodology aims to help researchers to conduct scientifically sound evaluations in order to prevent similar issues with the evaluation of security tools and frameworks in the Rust ecosystem. Method: We systematically analyze existing evaluation literature to develop the first sound methodology for Rust based evaluations. Our guidelines provide enough flexibility to support a variety of use cases. To quantify the performance of a security tool, we introduce an automated approach to inject unsafe code coverage oracles, which require no forward porting, avoid overfitting, and allow updating test sets in the future. We also present methods to quantify the diversity of a Rust test set, ensuring that the results are applicable to a large set of existing Rust programs. We practically apply our methodology in our evaluation of the most popular Rust fuzzers. Results: We show the practical applicability of our design and conduct an evaluation with a diverse test set of 20 Rust projects. [...]

---


### 216. [Comparative Evaluation of Deep-Learning based DoA Estimators for Real-Time ISAC Beamforming](https://arxiv.org/abs/2610.20326)

**<font color=#1a73e8>作者：</font>** Anjali K.S., Manoj Kumar Panda, Chandramani Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integrated Sensing and Communication (ISAC) systems rely on accurate Direction-of-Arrival (DoA) estimation for effective beamforming and spectral-efficiency enhancement. While numerous classical and deep-learning-based DoA estimation methods have been reported in the literature, their suitability for real-time ISAC operation remains insufficiently understood because practical deployment requires consideration of both estimation accuracy and computational latency. This paper presents a unified evaluation framework for systematically comparing classical and learning-based DoA estimators within an ISAC beamforming pipeline. Representative classical and learning-based DoA estimators, together with an ensemble architecture, are integrated with Singular Value Decomposition (SVD)-based beamforming and evaluated under identical operating conditions. The impact of DoA estimation accuracy, inference latency, beamforming-weight generation time, and resulting effective spectral efficiency is investigated. Results show that different estimators occupy distinct operating points in the accuracy-latency-performance design space. Although learning-based approaches substantially reduce estimation time compared with MUSIC, the overall processing latency increasingly becomes dominated by the computational cost of SVD-based beamforming. Among the evaluated methods, the Regression Convolutional Neural Network (RCNN) exhibits a favorable balance between estimation accuracy, computational efficiency, and beamforming performance, making it a promising candidate for real-time ISAC deployment. The findings further suggest that future low-latency ISAC systems may benefit from beamforming strategies that reduce or avoid computationally intensive SVD-based beamforming-weight generation.

---


### 217. [Anuvani-Diarization: Zero Shot Speaker Diarization and Annotation Conventions Across 22 Languages](https://arxiv.org/abs/2610.20327)

**<font color=#1a73e8>作者：</font>** Stephen Fernandes, Narayan Choudhary  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> India's 22 scheduled languages are spoken by over a billion people in conversations that mix languages, often within one turn, overlap freely, and take place over telephones, in meetings, and in media. Knowing who spoke when, the task of speaker diarization, is essential to speech applications for such conversation: voice agents conversing with several people at once, speaker attributed transcription of meetings and calls, contact center analytics, and media monitoring. We present a systematic study of speaker diarization across all 22 languages on IndicDiarBench and introduce Anuvani-Diarization, which adapts a self-supervised end-to-end segmentation model to Indian conversation with uncertainty aware silver supervision. Evaluated zero shot alongside nine recent diarization systems, it reaches a duration weighted diarization error rate (DER) of 16.78% on all 1,164 recordings, the lowest of all systems we ran and second only to the best published result (16.0%), and leads the three strongest rivals in 14 of 22 languages. It matches its parent on six international benchmarks. We also show that the benchmark's utterance level annotation convention is a hidden variable worth 1.9 to 4.1 DER points, depending on the system, and that a convention learned from other Indian transcriptions does not transfer.

---


### 218. [Are We Overthinking One-Step Generation?](https://arxiv.org/abs/2610.20331)

**<font color=#1a73e8>作者：</font>** Woobin Park, Jaeyeon Kim, Yilun Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow matching are now dominant frameworks for generative modeling in continuous domains, but they typically require multiple network evaluations at inference. This has motivated extensive research on one-step generative modeling primarily built on diffusion and flow, though existing approaches often rely on complex training machinery. In this work, we introduce Priming Models, a simple two-stage framework for training one-step generators. Motivated by the difficulty of distributional training from scratch, Priming Models are first trained on a reconstruction objective, e.g., pixel-space denoising at a fixed noise level, before undergoing feature-space distributional post-training. Our central scientific finding is that this simple reconstruction stage is already enough to entirely alleviate the difficulty of distributional training. Empirically, across class-conditional image generation, text-to-image generation, and world modeling, Priming Models significantly advance the Pareto frontier of training compute vs. generation quality. On ImageNet at $256 \times 256$ resolution, we achieve a state-of-the-art FID of $1.19$ among one-step generators using approximately one-tenth the training compute of prior methods with comparable FID. We open-source our codebase at this https URL.

---


### 219. [InfiniSplat v2: Analyzing and Improving Feed-Forward 3DGS from Any Views](https://arxiv.org/abs/2610.20341)

**<font color=#1a73e8>作者：</font>** Yongzhen Hu, Hao Yu, Jiawei Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward Gaussian reconstruction builds 3D scenes directly from input images for novel view rendering, but learning Gaussian attributes from predicted geometry for high-quality rendering under large viewpoint changes remains challenging. We analyze limitations in Gaussian attribute learning and introduce InfiniSplat v2, which improves rendering quality through architectural and training changes. Our method decouples geometry and attribute prediction with a frozen geometry branch, aligns predicted Gaussians using ground-truth camera poses during training, and adopts large-angle target view supervision. Across six datasets, the feed-forward outputs of the same trained model achieve state-of-the-art mean LPIPS and DISTS among the evaluated methods in both pose-conditioned and pose-free settings. In the pose-conditioned setting, mean LPIPS and DISTS decrease by 25.8% and 32.9%, respectively, compared with the strongest evaluated baselines. We further find that opacity learned with only image reconstruction supervision suppresses geometrically inconsistent points. Project page: this https URL

---


### 220. [When Does Task-Aware Imputation Matter? An Analysis of Robustness Under Train-Test Mismatch](https://arxiv.org/abs/2610.20342)

**<font color=#1a73e8>作者：</font>** Maria V. Salvador, Ana F. Sequeira, Jaime S. Cardoso  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Missing data is a pervasive challenge in machine learning, often degrading predictive performance and complicating model deployment. Most existing approaches treat imputation as a preprocessing step independent of the downstream task, a separation that becomes problematic under train-test mismatches in missingness mechanisms or rates. We introduce a unified framework that treats missing entries as variables in a task-conditioned optimization problem. We instantiate this framework in two settings: an amortized approach for scenarios with missing data at both training and test time, and a latent optimization approach for settings where only training data is incomplete.
The evaluation is conducted on 98 tabular datasets, and robustness under train-test mismatches is assessed on 36 datasets. Results reveal that reconstruction error constitutes a poor proxy for predictive utility (Spearman rho approximately 0.16 to 0.32), and that task-aware imputation becomes critical in scenarios where classical methods fail to recover complete-data performance, achieving win rates of up to 80% in challenging train-test mismatch scenarios.

---


### 221. [Non-asymptotic Convergence of Average-reward Q-learning with Options](https://arxiv.org/abs/2610.20347)

**<font color=#1a73e8>作者：</font>** Kintan Saha, Ahana Deb, Anders Jonsson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the finite-sample convergence of Q-learning algorithms for the average-reward formulation of Reinforcement Learning (RL) with options. While options allow temporarily extended and hierarchical actions, the average-reward formulation incorporates continual tasks beyond discounted and episodic RL. We establish the first $\tilde{O}(1/\text{iterations})$ convergence guarantees, in the mean-square sense, for average-reward option Q-learning algorithms in both the inter- and intra-option settings. First, we prove that both inter- and intra-option Bellman operators satisfy multi-step span contractions under unichain assumptions. Then, we propose synchronous estimators of these multi-step option Bellman operators leading to two variants of option Q-learning. Finally, we extend the stochastic approximation framework to prove convergence rates of these two algorithms under the minimal assumptions used in the literature.

---


### 222. [NeuroDETR: Multiscale Discrete Spatiotemporal Tokenization for Asynchronous EEG Event Detection](https://arxiv.org/abs/2610.20349)

**<font color=#1a73e8>作者：</font>** Yaozhi Wen, Kun Zhao, Wei Wei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous EEG event detection supports practical brain-computer interfaces by identifying event classes and temporal boundaries directly from continuous recordings without predefined event boundaries at inference time. The primary challenge lies in extracting event-related patterns embedded in ongoing background activity. To address this, we propose \textbf{NeuroDETR}, a discrete spatiotemporal multiscale framework that combines structured tokenization with event-aware feature refinement. Multiscale temporal codebooks capture brief responses and sustained dynamics, while Spatial-Pyramid VQ hierarchically encodes spatial structure across EEG channels. These complementary representations form a compact event memory for jointly classifying events and estimating their onsets and offsets. Before tokenization, we apply FOCAL, an event-aware sparse attention module that uses predicted event presence to guide temporal feature refinement and spatial aggregation, emphasizing likely event periods while preserving context across the recording. Experiments on eight EEG datasets that span diverse paradigms demonstrate state-of-the-art performance. These findings provide a basis for the development of BCI systems that recognize meaningful neural activity during continuous interaction and monitoring.

---


### 223. [Do AI Agents Gossip? Evaluative Talk in Human and AI-Agent Online Communities](https://arxiv.org/abs/2610.20360)

**<font color=#1a73e8>作者：</font>** Yong-Hui Hua, Chih-Han Lin, Shu-Kai Hsieh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gossip, defined as evaluative talk about absent third parties, is widely seen as a uniquely human social practice. This study examines whether comparable discourse emerges spontaneously in a community of autonomous AI agents. We compare Moltbook, a Reddit-style platform populated by AI agents, with PTT, a large human-operated bulletin board in Taiwan. To reduce differences attributable to communicative setting, we analyze two public, asynchronous forums using the same operational definition of gossip. Gossip occurs on Moltbook, but its prevalence is 2.6 to 6 times lower than on PTT, depending on the denominator used. On both platforms, gossip frequently targets locally prominent figures, tends to elicit agreement from the first respondent, and is rarely presented as unsupported rumor. The clearest difference concerns how subsequent responses develop. Among threads containing at least one codable reply, challenges occur in 65.1% of human threads but only 21.3% of agent threads. Moreover, following an early aligning response, consensus remains unchallenged in 83.6% of agent threads, compared with 44.7% of human threads. This thread-level contrast remains after controlling for thread depth and board composition and under recalibration against two human annotators. Estimates based on individual reply turns are less robust and are therefore reported as bounds. These findings suggest that AI-agent communities reproduce the informational dimension of gossip, while the extent to which gossip performs comparable relational functions remains unresolved.

---


### 224. [Fractional is Better: Learnable Derivative Orders in Neural Operator Learning](https://arxiv.org/abs/2610.20363)

**<font color=#1a73e8>作者：</font>** Fares B. Mehouachi, Saif Eddin Jabari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators learn mappings between function spaces, enabling fast surrogate solutions to partial differential equations. Despite remarkable architectural diversity, these methods often share a common input representation: raw coordinate-value pairs $(x, u(x))$. We ask whether inputs aligned with PDE differential structure can improve learning. Through Picard iteration on mild solutions, we show that derivatives of the input appear explicitly in the solution operator, suggesting that providing derivative features should reduce the network's implicit differentiation burden. We prove this intuition: providing derivative features improves approximation bounds from $O(W^{-(s-m)/d})$ to $O(W^{-s/d})$, where $W$ is parameter count, $s$ is input regularity, $m$ is the PDE order, and $d$ is spatial dimension. Our central finding, however, is a surprise: the optimal derivative order $\beta^*$ is strictly less than the PDE order $m$. This gap arises from a bias-variance tradeoff in spectral space that we characterize in closed form. Learning $\beta$ from data achieves automatic spectral regularization. We introduce $\partial$-NO (del-NO), for derivative-augmented neural operators, an architecture-agnostic augmentation that provides learnable fractional derivative features to any neural operator backbone. Across benchmark problems and architectures, $\partial$-NO consistently improves prediction accuracy, with learned orders that reflect a representation of known physics modulated by noise and finite-sample constraints.

---


### 225. [Lexical Persistence Without Semantic Entrenchment in AI Agent Communities](https://arxiv.org/abs/2610.20365)

**<font color=#1a73e8>作者：</font>** Chih-Han Lin, Yu-Yun Chang, Po-Ya Angela Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI agent communities sustain lexical persistence, popular terms spread, recur, and achieve broad adoption, but whether they also develop the temporal semantic structure characteristic of human linguistic communities remains open. We compare MoltBook (AI agent community, 8 weeks), PTT (Chinese human BBS, 19 years), and Reddit (English human forum, in matched 8-week windows) using Compass-Aligned Distributional Embeddings (CADE), measuring semantic drift (B1), neighborhood stability (B2), and lag-1 autocorrelation of per-word drift trajectories. Across the platforms, lag-1 autocorrelation forms a memory-horizon continuum. AI agents' result clusters at the low end, while human platforms show longer-range temporal dependence. MoltBook exhibits approximately 2$\times$ the B1 drift and 20-30% lower B2 stability than both human platforms. As a partial control for community age, r/vibecoding (founded 2025-02-08) shows significant ACF in its first 8 weeks ($0.082$, $p<.001$) and over 15 weeks ($0.220$, $p<.001$); MoltBook's ACF remains non-significant ($p = 0.41$), consistent with the gap not reducing to developmental stage alone. We interpret this pattern as evidence that lexical diffusion alone does not guarantee diachronic semantic consolidation. The findings are consistent with a contrast between communities whose semantic trajectories accumulate long-range interaction constraints and communities whose outputs are repeatedly regenerated from largely fixed pretrained distributions.

---


### 226. [Cascaded Retrieval with Cross-Modal Query Refinement for Efficient Visual Document Search](https://arxiv.org/abs/2610.20367)

**<font color=#1a73e8>作者：</font>** Diana Turmakhan, Aseem Srivastava, Vivek Gupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieving information from visually rich documents requires matching queries against pages that contain complex evidence in tables, figures, and layout-dependent structures. Current vision-language retrievers address this but incur query-time costs that grow with corpus size and are impractical to scale. We propose SCOUT, a cascaded two-track retrieval framework that separates retrieval performance from exhaustive search. The visual track first uses a lightweight parent retriever to filter the corpus to a compact candidate pool, then applies a stronger multi-vector reranker only to those candidates. In parallel, a semantic track retrieves over hierarchical page and document summaries generated offline to provide a signal complementary to visual matching. The outputs are fused through cross-modal query refinement, which uses semantic scores to adjust the visual query representation before final ranking. We evaluate SCOUT on 4 major benchmarks against 6 baselines and observe a significant query-time latency improvement up to 80.7x (28.8x on average) relative to the best baseline, while exceeding state-of-the-art retrieval performance by up to 7.8% NDCG across all benchmarks.

---


### 227. [ReAl: Refine neural operators via aligning dynamical flow](https://arxiv.org/abs/2610.20369)

**<font color=#1a73e8>作者：</font>** Jing Xu, Zenglin Xu, Li Yi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural partial differential equation (PDE) surrogates trained with mean squared error (MSE) can capture dominant dynamics but often lose high-frequency information and fine-scale structures. Generative models (e.g., Flow Matching) can capture the distribution of fine-scale details, yet stochastic errors may accumulate during autoregressive rollouts and compromise long-term stability. To address these limitations, we introduce Refine and Align(ReAl), a model-agnostic plug-in that augments pretrained PDE surrogates to improve the reconstruction of high-frequency structures associated with complex physical phenomena. In the refinement stage, a conditional flow-matching model learns the residual distribution around the deterministic base prediction, recovering missing fine-scale structures while retaining the dominant dynamics. In the alignment stage, to mitigate the generative discrepancies amplified in the autoregressive rollout, particularly in chaotic systems, we generate multiple trajectories from the same input and reinforce the refiner with trajectory-level rewards, thereby achieving long-horizon dynamical alignment. Experiments across diverse surrogate architectures and PDE tasks demonstrate that ReAl consistently improves high-frequency fidelity, forecasting accuracy, and long-horizon stability.

---


### 228. [Look Before You Restore: Learning to Predict Before Acting for Agentic Image Restoration](https://arxiv.org/abs/2610.20384)

**<font color=#1a73e8>作者：</font>** Xu Zhang, Jun Wan, Lefei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agents for mixed-degradation image restoration typically learn what a tool does to an image only after running it: failed calls waste computation and harmful outputs go unnoticed until too late. We propose PreActIR, an agentic restoration framework that predicts tool consequences before execution. For each candidate tool, a tool-conditioned world model forecasts changes in residual degradation, image quality, and fidelity, together with the risk of harm and the uncertainty of the prediction. The agent executes the top-ranked candidate, and an independent verifier commits or rolls back its output before the agent replans from the observed state. PreActIR also audits whether performance is limited by the selector or by the candidate space, and studies targeted tool adaptation as a controlled way to expand that space. In a controlled evaluation that fixes the candidate pool, verifier, and budget and employs reference-annotated degradation states, PreActIR uses 42.5% fewer real tool calls and 63.4% fewer rejected calls than reactive, execute-then-evaluate trial and error, while improving Y-PSNR by 0.92 dB.

---


### 229. [From Human Corrections to Learned Segmentations: A Critical Mathematical Review of Information, Learning, and Human Effort](https://arxiv.org/abs/2610.20396)

**<font color=#1a73e8>作者：</font>** Jon Sporring  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When does a human correction become useful learning, and what establishes better segmentation at matched human effort? This critical narrative review follows feedback through its selection, learner update, and evaluation. It compares active learning, machine teaching, interactive segmentation, and sequential predictive evaluation using a common mathematical account of target information, predictive error, response predictability, and human work. An exact Bayesian update converts evaluation-label information into expected log-loss improvement; an excess-risk decomposition explains what an approximate learner can lose. Conditional information decompositions separate the roles of selected locations, labels, and displayed context. Empirical comparisons show why response protocols, update mechanisms, and effort denominators matter, distinguishing current-mask refinement from reusable learning and simulated interaction from human evidence. We identify what logs can reveal, what requires independent evaluation, and what remains model-dependent. The resulting research priorities are to test what selection reveals, whether using it improves assimilation, and whether the resulting interaction policy benefits segmentation at matched effort. These are distinct claims: predicting a teacher's responses need not identify human intentions or establish better learning. No new acquisition algorithm or empirical superiority is claimed.

---


### 230. [Where Should the Gaussians Go? Reusable Label-Aware Allocation for Budget-Constrained Gaussian Splatting of Cinematic CT](https://arxiv.org/abs/2610.20397)

**<font color=#1a73e8>作者：</font>** Bowen Xiang, Dingjie Su, Jon S. Heiselman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anatomical labels help 3D Gaussian splatting preserve vessels in cinematic renderings of CT, but the representation is still found by optimising each patient's scene, where densification decides where Gaussians go, while real-time displays cap their number. We address one part of this process: deciding where a fixed budget of B Gaussians should be placed. We propose a reusable, labelaware allocation front end that maps a patient's CT, labels and transfer function to a density over 2mm cells and draws exactly B positions from it without per-patient optimisation; the other Gaussian attributes are still fitted per patient. The front end is learned once from per-patient optimised scenes and implemented as a population-trained neural prior and an interpretable seven-parameter visibility-aware closed form (VACF). With identical attribute fitting on 20 held-out patients at 10K-100K Gaussians, both raise vessel-masked PSNR over uniform allocation by 4.5-7.1dB and over pruning a dense voxel-aligned model by 1.6-3.3dB. The neural prior does not differ significantly from per-patient optimised allocation at any budget, and VACF is within 0.6dB of it on vessels; on 19 external patients the neural prior again matches it on vessels and VACF is within 0.7dB. As an initialisation for position optimisation, VACF allocation beats per-patient densification on vessels at 10K Gaussians and, at 25K, reaches a higher vessel PSNR after 118s of optimisation than densification after 248s. Under altered rendering presets, VACF transfers to new colours and lighting but not to a label-free transfer function, whereas the neural prior shows the opposite pattern.

---


### 231. [Hyperspherical Contrastive Representations Unlock Planning and Exploration](https://arxiv.org/abs/2610.20409)

**<font color=#1a73e8>作者：</font>** Jonghae Park, Sungil Son, Jonghun Shin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a self-supervised reinforcement learning algorithm that learns to build towers of up to eight cubes from scratch, without prior data, rewards, demonstrations, or pretrained models. Our method, Contrastive Planning via Spherical Linear Interpolation (C-Slerp), uses contrastive representations as reusable building blocks and repeatedly composes them to infer a sequence of intermediate waypoints. Under our hyperspherical parameterization, the learned representations allow intermediate waypoints to be inferred in closed form through spherical linear interpolation, without training a separate high-level policy or performing graph search. Importantly, the representation geometry also tells us how to adjust the number of waypoints based on the difficulty of each goal-reaching problem. Experiments show that our method succeeds on long-horizon navigation and robotic manipulation tasks, including settings where strong baselines fail to achieve a single success. Ablations further show that using a fixed number of waypoints substantially degrades performance, highlighting the importance of adapting the plan to task difficulty.

---


### 232. [Hybrid supervised instance segmentation by learning label noise suppression](https://arxiv.org/abs/2610.20412)

**<font color=#1a73e8>作者：</font>** Linwei Chen, Ying Fu, Shaodi You 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To reach top accuracy, current fully supervised instance segmentation methods severely rely on large-scale pixel-wise labeled datasets. They are usually expensive and time-consuming to obtain. Though weakly or semi-supervised methods utilize cheap bounding box labeled, image-level labeled or unlabeled samples to save the labeling cost, their performance is largely sacrificed. To save labeling cost without losing much performance, in this paper, we present a pipeline that can utilize economical bounding box labels and accurate pixel-wise labels in a hybrid way. Specifically, we design two ancillary models to learn label noise suppression and obtain accurate pseudo pixel-wise labels from bounding box labels for training. One is designed to suppress mislabeling between foreground and background, and the other is designed to suppress noise from mislabeling of instances. Moreover, we exploit category-aware spatial attention module, category constraint module, instance constraint module, and self-learning training approach to improve the accuracy of pseudo labels. Experiments on the PASCAL VOC 2012 and the Cityscapes datasets show that our method can achieve competitive performance with much less labeling cost.

---


### 233. [One Size Does Not Fit All: Curvature-Aware Adaptive Perturbation for SAM](https://arxiv.org/abs/2610.20415)

**<font color=#1a73e8>作者：</font>** Alessia Rossi, Felipe Campelo, Gabriel L. Oliveira  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Poor generalisation in deep neural networks is frequently associated with convergence to sharp minima. Sharpness-Aware Minimisation (SAM) improves generalisation of deep neural networks by minimising a combination of the training loss and the local sharpness of the loss landscape, biasing convergence towards flat minima. However, SAM relies on a fixed perturbation radius $\rho$ that ignores local curvature, leading to inefficient behaviour: the perturbation may be too small to escape poor basins defined by sharp local minima, or too large to allow convergence to solutions with good loss-sharpness tradeoff. We reinterpret $\rho$ as the intensity of the perturbation signal and propose Curvature-Aware Adaptive Perturbation for SAM (CAP-SAM), a geometry-aware method that modulates the perturbation radius based on a sharpness ratio, enabling a more effective search for robust minima on the loss landscape. We prove that CAP-SAM preserves the same convergence rate as standard SAM in non-convex stochastic settings. Extensive experiments indicate that our approach consistently outperforms SAM and its most prominent variants across diverse network architectures on CIFAR-10, CIFAR-100, and ImageNet.

---


### 234. [Tracking a Small Set of Experts in Online Convex Optimization](https://arxiv.org/abs/2610.20416)

**<font color=#1a73e8>作者：</font>** Angelos Assos, Anand Brahmbhatt, Elad Hazan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For the fundamental problem of prediction from expert advice, Freund asked whether one could compete with a comparator that switches $k$ times among only $m$ experts. For a discrete set of experts, this problem was resolved by Bousquet and Warmuth (2020), who gave an efficient algorithm with optimal regret matching the information-theoretic limit.
We study the analogous problem in online convex optimization, where the action space is continuous. An inefficient algorithm can be derived by discretizing the action space and applying the Bousquet--Warmuth algorithm, giving regret of $\widetilde{O}(md+k)$, while the best known efficient algorithm for this problem has regret $\widetilde{O}(dk)$. We show that this computational inefficiency is inherent, establishing a separation between the information-theoretic and polynomial-time regret achievable for this problem. Specifically, under the hypergraphic planted-clique conjecture, we show that for every polynomial-time algorithm there exist instances for which it incurs at least $(k\sqrt d)^{1-o(1)}$ regret.

---


### 235. [Continual Learning for Reliable In-Sequence Molecular Communication](https://arxiv.org/abs/2610.20426)

**<font color=#1a73e8>作者：</font>** Siddhant Setia, Junichi Suzuki, Tadashi Nakano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper considers reliable in-sequence molecular communication, where bio-nanomachines exchange molecule-encoded information in a specified order, and investigates a new simulation-based method to incrementally evaluate communication protocols by gradually increasing the complexity of experimental settings. The proposed method, called Affine Memory Replay (AMR), builds a continual learning (CL) model to estimate communication performance between bio-nanomachines. AMR stores past simulation samples and synthesizes additional replay samples through interpolation and extrapolation between past samples. Through incremental performance estimation tasks, it replays both past and synthetic samples to regularize model updates, helping the model adapt to new experimental settings while retaining knowledge from earlier ones. Experimental results show that AMR significantly outperforms existing CL methods in maintaining overall estimation accuracy across sequentially learned estimation tasks. It effectively balances memory stability and learning plasticity under moderate training cost.

---


### 236. [Phantomware: a Data Augmentation Framework for the Detection of Emerging Malware Campaigns](https://arxiv.org/abs/2610.20427)

**<font color=#1a73e8>作者：</font>** Antonino Rullo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Detecting unseen malware variants remains a major challenge as malware families continuously evolve. This issue is exacerbated in data-scarce scenarios such as emerging malware campaigns, where only a few samples are available to train robust detectors. A common strategy is to proactively generate malware variants and use them as augmentation data to expose models to a broader range of potential threats. Existing approaches that generate functional malware variants through adversarial manipulation suffer from several important limitations. Generated samples must remain executable and preserve their malicious behavior, requiring costly validation through execution and analysis. Moreover, the adversarial objective provides limited control over the resulting augmentation dataset: it cannot guarantee the generation of sufficiently diverse variants, or even a single successful sample, making the effectiveness of the augmentation process inherently unpredictable. Finally, these approaches typically rely on a well-trained detector to guide generation, an assumption that may not hold in data-scarce scenarios such as early-stage malware campaigns. We formally and empirically demonstrate these limitations and propose Phantomware, a data augmentation framework designed for extreme data scarce scenarios. Phantomware operates entirely in the representation space of a pretrained malware detector, avoiding the costly generation and validation of functional binaries. By exploiting latent-space geometry, it generates synthetic malware representations of a target family in a controlled manner, providing a constructive guarantee on the generation of diverse training samples. Extensive experiments on real malware families demonstrate that Phantomware improves detection of unseen variants and provides robustness against both real and adversarially generated malware samples.

---


### 237. [SwarmRSI: Recursive Self-Improvement through Evolving Scientific Agent Swarm](https://arxiv.org/abs/2610.20431)

**<font color=#1a73e8>作者：</font>** Qianru Meng, Xi Zhang, Konstantinos Papakostas 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) in scientific research aims to improve agents' research capabilities through their own experimental experience. Scientific agent swarms can combine evidence and implementations from different research directions to guide their agents' subsequent experiments. However, poor experimental results can leave unclear whether to revise a hypothesis or its implementation, while overall program scores can hide components useful to other agents. To address these challenges, we introduce SwarmRSI, a framework that evolves scientific agent swarms for recursive self-improvement. We devise Feedback-Guided Swarm Mutation to refine hypotheses and their implementations using experimental feedback from other agents. We also propose Complementary Swarm Recombination to reuse retained hypotheses and complementary program components across agents, allowing partial results to support new research. Recursive Swarm Evolution integrates both mechanisms into a feedback loop, using new experimental evidence to guide subsequent research. Experiments on OpenProblems, NatureBench and MLE-Bench Lite demonstrate SwarmRSI's state-of-the-art (SOTA) performance. Further evaluations show that accumulated research experience improves performance on held-out tasks. Biologists also reproduce its programs for follow-up biological analyses.

---


### 238. [Infant Fingerprints: Quality Assessment & Recognition](https://arxiv.org/abs/2610.20432)

**<font color=#1a73e8>作者：</font>** João L. H. Dall Agnol, Dalcimar Casanova, Rodrigo Minetto 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infant fingerprint recognition is hindered by a combination of physiological characteristics, such as small ridge width and spacing, and acquisition challenges that include involuntary motion, skin residue, and uneven fingertip pressure. These factors undermine fingerprint quality standards originally designed for adults, which assume feature distributions that do not hold for infants. To address this gap, this paper evaluates ten fingerprint quality assessment methods on a longitudinal dataset that spans six age groups from newborns to three months, alongside a parameter tuning routine that uncovers age-specific fingerprint characteristics to recalibrate methods with domain-dependent assumptions. Both default and tuned configurations are compared through recognition experiments assessing the effectiveness of quality-guided gallery selection. Template-fusion strategies and latent fingerprint recognition technologies are further examined to identify the best possible matching rates achievable by the top-performing method. Results show that tuned parameter sets outperform default configurations for the majority of methods and age groups, indicating that targeted recalibration of existing frameworks improves gallery utility and contributes to more reliable infant fingerprint recognition.

---


### 239. [The Accuracy Well: Nonmonotone Accuracy Dynamics at Vanishing Initialization](https://arxiv.org/abs/2610.20439)

**<font color=#1a73e8>作者：</font>** Yaroslav Gusev, Eugene Golikov, Dmitry Yarotsky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study classification dynamics under small initialization and identify a pronounced non-monotone behavior of accuracy that we call the accuracy well: accuracy rises rapidly early in training, subsequently drops, and only much later recovers. We observe this phenomenon in deep linear networks, fully connected ReLU networks on MNIST, deep convolutional networks on CIFAR-10, and controlled synthetic tasks, across different losses and optimizers and in both training and test accuracy. We propose a three-stage explanation in terms of target-driven organization, a degeneracy bottleneck, and subsequent recruitment and recovery. We develop a rigorous theory of these dynamics for shallow and deep linear networks, showing in particular that high accuracy can emerge while the predictor and the change in loss remain asymptotically vanishing, before continued optimization causes accuracy to deteriorate. For a simple synthetic classification task, we prove an extreme instance in which accuracy asymptotically rises to 100%, collapses to 0, and later recovers permanently to 100%. Our results show that classification accuracy can reveal aspects of learning dynamics that are not captured by the training loss alone.

---


### 240. [Selective Growing Q-Networks (SGQN): An Analysis of Adaptive Action Grids in Decoupled Q-Learning](https://arxiv.org/abs/2610.20463)

**<font color=#1a73e8>作者：</font>** Parham Nooranbakht, Seyed Mahdi Basiri Azad, Joschka Bödecker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Value-based Q-learning for continuous control can discretise the action space, but the resolution of the discretisation trades early exploration against final precision. Growing Q-Networks (GQN) grow the resolution uniformly from coarse to fine. We introduce Selective Growing Q-Networks (SGQN), which keeps decoupled Q-learning and replaces uniform growth with an adaptive action grid: bins are added next to bins with high estimated Q-value, bins with low Q-value are pruned, and actions are chosen epsilon-greedily. On eight DeepMind Control Suite (DMControl) tasks with 2 to 12 action dimensions, SGQN has the highest mean final return among the compared methods on four, is within 1.1% of the best method on three more, and is 3.4% below Bang-Bang MPO on Walker Run, using on average 7.5 of 9 available bins per dimension. We then test whether the adaptive grid explains these results, and find that it does not. Growth activates every candidate bin and behaves like uniform growth, and removing pruning changes the return by at most 1.1%. Two other choices matter: starting from a coarse grid, since starting with all 9 bins produces collapsed seeds, and epsilon-greedy selection, since an annealed softmax lowers the return by 23% to 100%. SGQN is insensitive to its growth and pruning hyperparameters. It also differs from the GQN and DecQN baselines in other respects, notably one gradient update per environment step instead of one per eight, which we did not control for, so we do not attribute its advantage to a single component. We present SGQN as a competitive value-based method and as an analysis of which ingredients of a growing action grid matter.

---


### 241. [SafeAdapt-Poker: Counterfactual Risk Calibration for Budgeted Adaptation under Opponent Shift](https://arxiv.org/abs/2610.20473)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Xiaobo Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Opponent histories can mislead after behavioral shifts. SafeAdapt-Poker formulates budgeted adaptation under opponent shift as a dual-counterfactual sequential-control problem using only information available before each decision. At each decision the controller asks two distinct questions: what local downside a deviation from the frozen anchor would induce under matched legal continuations, and what future adaptation value would be lost by consuming part of the remaining deviation budget now. The first question is answered by a monotone strategic-risk model over deviation intensity; the second by a paired budget-state continuation model that prices current budget consumption. The controller selects among support-preserving candidate deviations by trading immediate adaptation value against these two quantities, a pathwise cumulative-KL ledger bounds total anchor-relative deviation, and a finite family of frozen controllers is screened on complete paired calibration sessions before held-out interaction. A finite-candidate perturbation bound shows that the allocation objective degrades continuously with continuation-value estimation error. Evaluation covers exact-game exploitation and safety, four opponent shifts, local-risk calibration, delayed-opportunity allocation, direct opportunity-value estimation, value-error robustness, factorial mechanism attribution, budget sensitivity, abstract-HUNL cross-play, and player/time-held-out public-history behavior. On exact Leduc the full controller attains a matched weak-pool gain of +0.0718 with a worst-opponent delta of -0.0126, raises delayed-opportunity capture from 0.6318 under myopic allocation to 0.7841 under the same session budget, and reaches +42.7 mbb/hand in abstract-HUNL cross-play; the retained public-history screen reports 0.5820 action accuracy and 0.9277 log loss versus 0.5039 and 0.9778 for a public prior.

---


### 242. [Average-Reward Policy Identification from a Single Continuing Trajectory](https://arxiv.org/abs/2610.20486)

**<font color=#1a73e8>作者：</font>** Tongxi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In reinforcement learning, an agent must explore an unknown environment to learn how to make good decisions. Unlike methods that can freely sample any state--action pair, an agent learning from a single trajectory must spend additional time navigating between states. It is therefore natural to expect that learning from a single trajectory requires more experience. In this paper, we show that this additional cost is not always necessary. For average-reward reinforcement learning, we develop an algorithm that learns where to collect information while ensuring that the required samples can be obtained efficiently. We establish an upper bound on the number of interactions needed to identify a near-optimal policy. Furthermore, we prove a matching information theoretic lower bound, showing that, for a broad class of environments and at sufficiently high accuracy, learning from a single trajectory is no harder in the worst case than learning with unrestricted access to state action samples. Our results reveal that the additional complexity cost of navigation can be avoided by adapting information gathering requirements to how the environment provides information.

---


### 243. [OLiVES: An Outdoor Low-Light Video Benchmark for Enhancement and Segmentation](https://arxiv.org/abs/2610.20501)

**<font color=#1a73e8>作者：</font>** Yini Li, Joanne Lin, David Blackham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light video processing remains an underexplored problem in computer vision, primarily due to the scarcity of high-quality ground-truth data. Existing public datasets exhibit several limitations, including restricted motion diversity, limited scene coverage, weak degradations, reliance on auxiliary modalities such as event data, and misalignment between low-light inputs and ground truth. Furthermore, current datasets typically address either low-light enhancement or scene understanding, whereas these tasks should be considered jointly. We introduce \textbf{OLiVES}, a benchmark dataset for outdoor low-light videos with dynamic scenes, designed to support both low-light video enhancement (LLVE) and video object segmentation (VOS). The dataset addresses key content gaps by incorporating a diverse range of natural textures, animals, occlusions, dynamic activities, and close-up scenes. To the best of our knowledge, OLiVES is the first outdoor low-light video dataset captured using professional cinema-grade cameras. It provides over 25,000 aligned normal- and low-light frame pairs, along with over 46,000 VOS annotations. We benchmark state-of-the-art LLVE and VOS methods on OLiVES and show that training on it improves performance on both tasks. The OLiVES project page is available at: this https URL.

---


### 244. [Graph-Enhanced Disease Trajectory Discovery and Temporal Endpoint Forecasting from Longitudinal Electronic Health Records](https://arxiv.org/abs/2610.20502)

**<font color=#1a73e8>作者：</font>** Jin-Jia Zheng, Vincent S. Tseng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Longitudinal electronic health records (EHRs) can reveal disease-progression structure, while useful forecasting requires leakage-controlled discovery, censor-aware outcomes, and inspectable trajectory evidence. We developed a graph-enhanced framework in MIMIC-IV v3.1 that splits patients before graph construction, learns train-only consecutive-admission transitions, and freezes endpoint-specific branching-motif policies selected on validation data. The final catalog contained 99,527 motifs, and a time-aware Transformer retrieved at most 24 patient-compatible motifs per endpoint through endpoint-specific cross-attention. Across five training seeds, micro-AUPRC increased from 0.9330 to 0.9357, while event-time MAE decreased from 676.9 to 657.7 days (reduction 19.2 days; 95% paired patient-cluster bootstrap CI, 13.8-24.8). Timing effects were heterogeneous: MAE worsened for events within 730 days but improved by 58.9 days for events occurring after 730 days. In an exploratory internal temporal split, branch conditioning reduced conditional event-time MAE by 26.9 days (95% CI, 23.0-30.8) without evidence of better micro-AUPRC. Corrected survival evaluation over the supported 0-2,555-day interval did not establish macro C-index or integrated Brier score superiority over a matched history-only discrete-hazard model. A directed, degree-matched GNN repair substantially improved unseen-edge discovery, yet replacing GNN-derived scores within fixed motif identities did not improve downstream forecasting. These results position branching motifs as structured trajectory context whose main value is long-range timing support rather than uniformly stronger endpoint discrimination, survival prediction, or causal explanation.

---


### 245. [VascuSR: Iterative Anatomy-Aware Diffusion for CT Super-Resolution](https://arxiv.org/abs/2610.20509)

**<font color=#1a73e8>作者：</font>** Hairong Ni, Jiahe Huang, Minghao Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative super-resolution (SR) can recover sharp detail in computed tomography (CT) images from severely downsampled observations, but the missing high-frequency content is not uniquely determined by the low-resolution input. Consequently, visually plausible reconstructions may contain anatomically unsupported vascular detail, such as missing, spurious, or incorrectly connected vessels. To overcome this challenge, we introduce VascuSR, an iterative anatomy-aware diffusion framework that combines image reconstruction with explicit 3D vascular guidance. First, to provide richer anatomical guidance, we use an explicit 3D vascular representation that captures structural information beyond individual slices. This representation also simplifies vascular refinement by allowing a lightweight 3D generative refiner to focus on vascular structure rather than complex CT appearance. Second, to guide slice-wise SR, a lightweight anatomy controller injects the refined structure into the diffusion decoder, while iterative feedback updates this guidance from each new SR volume. On re-annotated MSD Task08 and HVM datasets, VascuSR outperforms interpolation and learning-based SR baselines in segmentation accuracy (Dice and clDice) and 3D vascular structure (connectivity and mean centerline distance), while maintaining image quality comparable to its SR backbone. Compared with learning-based baselines, VascuSR reduces class-averaged connected-component counts by over 20% on both datasets and mean centerline distance by over 10% on MSD.

---


### 246. [A Two-Level Clinical Novelty Prioritization Framework for Disease Trajectories Discovered from Longitudinal Electronic Health Records](https://arxiv.org/abs/2610.20512)

**<font color=#1a73e8>作者：</font>** Jin-Jia Zheng, Vincent S. Tseng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-based analysis of electronic health records (EHRs) yields disease-trajectory catalogs, but structural support does not establish semantic novelty. We present a two-level framework to prioritize 99,527 branching motifs previously discovered by an upstream patient-disjoint, train-only MIMIC-IV v3.1 pipeline and frozen after validation-based catalog selection. The framework separates path-level and node-to-endpoint semantic sparsity from reliability-adjusted clinical priority. Three deterministic textualizations per motif or node-target pair were embedded with BAAI/bge-small-en-v1.5 and calibrated against 166,972 pre-2023 PubMed references using mean top-20 cosine distance. Positive recombination occurred in 8.63% of motifs and had negligible effect on global ranking, whereas specificity and support/GNN reliability terms changed clinical-priority ordering. Robustness analyses across neighbor counts, templates, encoders, generic-label taxonomies, score settings, PrimeKG, and corrected density-based RND showed that broad ordering was more stable than hard top-k membership. A semantic-dose analysis did not support a monotonic relation between score and forecasting benefit after endpoint and token-count adjustment (1.96 days per SD; 95% CI, -0.75 to 4.68). In the frozen catalog-q90 high-semantic subgroup, branch-enhanced forecasting reduced conditional event-time MAE by 20.1 days (95% CI, 13.3-27.0) and sMAPE by 2.37 percentage points (95% CI, 1.81-2.93), while discrimination and endpoint-ranking differences were inconclusive. Corrected RND showed low tail agreement with the primary score (Spearman rho = 0.430; q90 Jaccard = 0.125) despite a similar aggregate timing association. These findings support representation-aware, uncertainty-aware literature-relative prioritization of discovered trajectories rather than causal discovery or clinician-adjudicated novelty.

---


### 247. [The Wealth of Agents: Scaling Agentic AI Across Developers](https://arxiv.org/abs/2610.20518)

**<font color=#1a73e8>作者：</font>** Austin W. Hanjie, Carlos E. Jimenez, Zirui Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Today's agentic systems are typically designed, built, and deployed by single developers with full control over all participating agents. While this simplifies development, it limits the potential scale of agentic systems. We study multi-developer agentic systems (MDAs) which enable developers to collaboratively build agentic systems to push frontier capability beyond what any individual developer could achieve alone. We construct empirical and theoretical models of developers to compare MDAs with single-developer agentic systems (SDAs). On GAIA, a general assistant benchmark, a population of specialized developers whose individual agents do not exceed 35% accuracy reaches 70% when their agents are combined in an MDA. This MDA performs 12 percentage points above the median general-purpose SDA built with several times each specialist's development budget. Our theoretical models show how MDAs can incentivize specialization and encourage more efficient use of aggregated developer resources. Put together, our results make a preliminary case for MDAs as a new scaling axis by enabling developers with diverse capabilities and resources to advance agentic AI collaboratively.

---


### 248. [Tulva: Practical Asynchronous Threshold FHE](https://arxiv.org/abs/2610.20521)

**<font color=#1a73e8>作者：</font>** Valerio Cini, Antonio Guimarães, Russell W. F. Lai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present Tulva, a practical threshold FHE scheme which equips a base FHE scheme with an asynchronous threshold decryption mechanism in a modular way. Our scheme simultaneously (1) is compatible with virtually any base FHE scheme and leaves its ciphertexts unchanged apart from an appended random tag, (2) supports a wide range of threshold profiles $(t,K)$ and ring degrees $\geq 256$ with 6-25 bits partial decryption per plaintext bit, and (3) achieves security in the presence of partial decryption queries on challenge ciphertexts based on the standard LWE assumption.
We provide an open-source implementation, benchmark its threshold decryption performance and evaluate the end-to-end costs for typical privacy-preserving Ethereum Virtual Machine (EVM) use cases. For 16-out-of-512 threshold and a publicly preprocessed ciphertext, computing secret-dependent partial decryption and public share combination requires only 3.7 ms and 0.5 ms, respectively, on commodity hardware. Compared with the state-of-the-art synchronous scheme [Zyskind et al., CCS'25], we replace their ciphertext-independent yet interactive preparation of secret-correlated randomness with a public, ciphertext-dependent 0.5 s preprocessing step, eliminate interaction in the online phase while maintaining similar decryption time on the same machine, and support 32$\times$ more total users.

---


### 249. [The Physics Is the Network: Fast, Training-Free Neural Emulation](https://arxiv.org/abs/2610.20525)

**<font color=#1a73e8>作者：</font>** Luka Todorovic, Kaushal Gianchandani, Sai Ravela  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural emulation need not require learning a substitute for known physics. We investigate PolyNets that couple a continuous-time neural representation of polynomial dynamics with a simple recurrent network for discrete-time integration. When the governing coefficients are known, the resulting tensor graph requires no training and preserves the prescribed numerical scheme while enabling efficient hardware execution and parallel simulation. Using the one-dimensional Korteweg-de Vries equation, we compare PolyNet with CPU and GPU finite-difference Runge-Kutta solvers and three trained neural models: a state-map emulator, a physics-informed predictor, and a learned-tendency integrator. Analytical soliton solutions provide a reference for amplitude and phase errors across grid resolutions, 10^6 dispersively scaled time steps, ensembles of up to 10^4 trajectories, and varying initial amplitudes. PolyNet achieves accuracy comparable to the numerical solvers, including at amplitudes outside the learned models' training conditions. It combines this fidelity with high GPU throughput, approximately constant over the tested resolution range, and favorable ensemble scaling.

---


### 250. [ActiveEvidence: Decision-Focused Evidence Graphs with Verifiable Acquisition Gaps](https://arxiv.org/abs/2610.20532)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Xiaobo Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A multimodal agent must decide whether visual evidence is worth acquiring, which candidate or resolution to query, and when further interaction can no longer change its decision. We study this problem under a strict free-metadata/paid-observation boundary, stochastic vector costs, and a frozen execution trace, and treat it as decision-certifiable active evidence acquisition. A Counterfactual Evidence Interaction Graph (CEIG) represents unary evidence value, signed second-order interaction, and directed conditional harm while maintaining explicit score enclosures for unresolved interactions; a decision-weighted enclosure objective tightens the bounds that can change action identity. Gap-directed refinement evaluates only interactions that can displace the incumbent acquisition and stops once an $\epsilon$-decision certificate shows that unresolved terms cannot change the selected action beyond a declared tolerance. The certificate is model-relative: it verifies policy-consistent optimality under the pinned learned score, and semantic quality is measured separately through post-freeze labels. Paired continuation rollouts learn the downstream value of paid previews, an online operational cost filter is separated from independent finite-policy-family trajectory certification, and an acquisition monitor with an independently implemented verifier binds every certificate to the frozen trace. On 640 cases split into 384/128/128 training, validation, and test cases, the controller reaches task score 0.842, grounding F1 0.816, evidence recall 0.873, 1.74 accepted calls, 286.5K visual tokens, and 742ms p95 latency. Dense replay of issued certificates shows 0.992 action agreement and a 0.988 certificate rate while evaluating 19.6 instead of 191.4 expensive interaction terms per decision.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-264](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

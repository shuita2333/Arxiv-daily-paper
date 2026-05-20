# 📦 其他研究 | 2026年05月21日

> 本类共 **338** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-338](./part-07.md)

---

### 201. [Online Market Making and the Value of Observing the Order Book](https://arxiv.org/abs/2605.19584)

**<font color=#1a73e8>作者：</font>** Davide Maran, Marcello Restelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study an online market-making problem in which a learner sequentially posts bid and ask prices for a single asset while interacting with traders holding private valuations. Unlike existing online learning formulations that assume fully censored feedback, we introduce an action-dependent feedback model inspired by real limit order books: when a trade occurs, the trader's valuation remains hidden, whereas when no trade occurs, informative feedback about supply and demand is revealed.
We show that this additional information fundamentally changes the learnability of the problem. In the stochastic setting with i.i.d. market prices, we propose an elimination-based algorithm that achieves $O(\sqrt T)$ regret with high probability, without requiring any smoothness assumptions on the distribution of trader valuations. We then extend this result to a broad class of mean-reverting price processes by considering both local, autoregressive dynamics and a weaker global drift condition based on cumulative deviations from the mean. Under either assumption, we establish high-probability $O(\sqrt T)$ regret bounds, relying on a new concentration inequality of independent interest. Finally, in the adversarial setting with oblivious prices, we design an explore-then-perturb algorithm that guarantees $O(T^{2/3})$ regret in expectation.
Our results quantify the value of observing the order book in online market making and demonstrate that even limited, action-dependent feedback can substantially improve regret guarantees compared to standard bandit feedback models.

---


### 202. [SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects](https://arxiv.org/abs/2605.19587)

**<font color=#1a73e8>作者：</font>** Puyi Wang, Yuhao Wang, Linjie Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Indoor scene synthesis underpins embodied AI, robotic manipulation, and simulation-based policy evaluation, where a useful scene must specify not only what the environment looks like, but also how its objects are structured. Existing pipelines, however, typically represent generated content as static meshes and inherit articulation only from curated asset libraries, which limits object-level controllability and prevents new interactable assets from being produced on demand. We address this gap by formulating physically interactable indoor scene synthesis as programmatic world generation, and present SceneCode, a framework that compiles a natural language prompt into an executable, code-driven indoor world rather than a collection of opaque meshes. A room-level agentic backbone first turns the prompt into a structured house layout and emits per-object AssetRequests through a planner--designer--critic loop. Each request is then routed to one of five code-generation strategies and converted into a synthesized part-wise Blender Python programs that are validated through an execution-guided repair-and-refine loop. The resulting programs are compiled into simulation-ready assets, and exported as SDF for physics simulation. A persistent scene-state registry links object requests, executable programs, rendered geometry, and simulation assets, turning scene assembly into a traceable and locally editable world-building process. We evaluate SceneCode across scene-level synthesis, object-level asset quality, human judgment, and downstream robot interaction. Results show that executable world programs improve prompt-faithful indoor scene generation and produce assets with cleaner mesh structure, and simulator-loadable articulation metadata. Project page: this https URL.

---


### 203. [Physics-Informed Graph Neural Network Surrogates for Turbulent Nanoparticle Dispersion in Dental Clinical Environments](https://arxiv.org/abs/2605.19589)

**<font color=#1a73e8>作者：</font>** Takshak Shende, Viktor Popov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dental aerosol procedures produce sub-50 micrometre nuclei that can remain airborne for long periods in enclosed clinics, creating pathways for airborne pathogen transmission. Reynolds-Averaged Navier-Stokes (RANS) simulations with Euler-Lagrange particle tracking capture this transport accurately but require very long run times per scenario, which precludes real-time clinical decision support in 3D. We present the Eulerian-Lagrangian Graph Interaction Network (ELGIN), a physics-informed graph surrogate that jointly predicts carrier-flow dynamics on the OpenFOAM polyhedral mesh and the per-parcel motion of the polydisperse spray cloud. ELGIN couples a multi-head Graph Transformer with Jacobi-preconditioned learnable pressure projection and a turbulence-closure head to a sigmoid-gated Lagrangian Interaction Network through differentiable inverse-distance mesh-parcel coupling, and advances parcels with a symplectic Stormer-Verlet integrator. A four-stage physics-informed curriculum stabilises 260-step autoregressive rollouts without gradient explosion. A parameter sweep with foam-extend 4.1 OpenFOAM reactingParcelFoam across clinically relevant ventilation rates and handpiece spray speeds provides CFD ground truth. This article reports a single-case demonstration in which both ELGIN and a Lagrangian-only baseline (M0) are trained and evaluated on Sweep_Case_03 of a twenty-case sweep; full 16/2/2 retraining is in progress and will replace all reported metrics. On this case, ELGIN tracks the foam-extend particle cloud much more closely than M0: mean parcel displacement error falls from 19.56% to 16.20% of room width and cloud radius-of-gyration error from 9.85% to 6.58%. A 26-second rollout completes in ~64 s on a 4 GB GPU, approximately 37x faster than the foam-extend reference pipeline, toward per-appointment infection-risk screening once the multi-case checkpoint is in place.

---


### 204. [deadtrees.earth-aerial: A Multi-Resolution Aerial Image Dataset for Tree Cover and Mortality Detection](https://arxiv.org/abs/2605.19605)

**<font color=#1a73e8>作者：</font>** Ayushi Sharma, Clemens Mosig, Lukas Drees 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forests worldwide are increasingly threatened by climate change and disturbances such as fire, pests, and pathogens, creating an urgent need for scalable monitoring of tree cover and tree mortality. Aerial imagery from drones and aircraft is a key data source for detailed and large-scale mapping of tree crowns and mortality. However, related progress is limited by the lack of globally representative, harmonized datasets for joint segmentation of tree cover and mortality. We introduce two novel, open, machine-learning-ready datasets to enable joint segmentation of tree cover and tree mortality from centimeter-scale aerial imagery for the first time at global scales. With DTE-aerial-train, we provide a training dataset comprising 385K image patches of size 1024x1024 pixels, with resolutions ranging from 2.5 to 20 cm. It includes multi-class expert-annotated and -audited pseudo-labels for tree cover and mortality. With DTE-aerial-bench, we provide a geographically balanced benchmark test set of 25 globally distributed orthoimages totaling 525 patches with high-quality expert annotations for both tree cover and mortality. Both the training and benchmark datasets span tropical, temperate, boreal, and dryland biomes and cover a wide range of forest structures and mortality patterns. Using the benchmark test set for evaluation, we establish strong reference baselines that improve mortality segmentation across all biomes and scales with significant gains in challenging regions, such as boreal forests, where the F1 score increases from 0.40 to 0.58 with around 45% relative improvement. All data, models, and code will be publicly released under permissive open-source licenses. An interactive visualization of the benchmark dataset is available at this http URL.

---


### 205. [Spectral Integrated Gradients for Coarse-to-Fine Feature Attribution](https://arxiv.org/abs/2605.19607)

**<font color=#1a73e8>作者：</font>** Soyeon Kim, Seongwoo Lim, Kyowoon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Integrated Gradients (IG) is a widely adopted feature attribution method that satisfies desirable axiomatic properties. However, the choice of integration path significantly affects the quality of attributions, and the standard straight-line path introduces all input features simultaneously, often accumulating noisy gradients along the way. To address this limitation, we propose Spectral Integrated Gradients, which constructs integration paths based on singular value decomposition (SVD) of the baseline-to-input difference. By progressively activating singular components from largest to smallest, SIG introduces global structure before fine-grained details, naturally following a coarse-to-fine progression. Through extensive evaluation across diverse image classification datasets, we demonstrate that SIG produces cleaner attribution maps with reduced noise and achieves improved quantitative performance compared to existing path-based attribution methods. Our code is available at this https URL.

---


### 206. [Inverse Design of Metasurface based Absorbers using Physics Guided Conditional Diffusion Models](https://arxiv.org/abs/2605.19611)

**<font color=#1a73e8>作者：</font>** Vineetha Joy, Jamshed Palai, Satwik Sahoo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inverse design of metasurfaces for specific electromagnetic responses requires generating geometries that satisfy stringent spectral constraints while maintaining manufacturability. Conventional design methodologies rely on iterative optimization routines using full wave simulations, which become extremely time consuming and computationally intensive for large design spaces. In addition, commonly employed generative approaches often exhibit limited conditional fidelity and the generated designs often contain fine or irregular features that are impractical to fabricate. In this regard, we propose a physics guided condition quality enhanced diffusion framework for the inverse design of metasurface based absorbers. Here, the conditioning information consisting of target reflection characteristics is integrated into the model using feature wise linear modulation (FiLM). Furthermore, to enforce adherence to target spectra, a pre trained surrogate EM simulator is embedded into the framework introducing physics aware regularization through spectrum level loss functions. The efficiency of the proposed model is demonstrated by generating practically realizable metasurfaces for different types of reflection characteristics in the frequency range of 2 to 18 GHz. The proposed framework achieves an average spectral mean squared error of 0.0006 and band alignment accuracy of 0.958 between the target spectra and the spectra produced by the generated designs, demonstrating high conditional accuracy. In addition, the model generates multiple geometries for the same condition, thereby providing diverse design alternatives to the engineer. The proposed model produces the suitable design in approximately 30 seconds, whereas the conventional approach can take several months under comparable computational resources. The efficiency of the model is also established via experimental measurements.

---


### 207. [White-Balance First, Adjust Later: Cross-Camera Color Constancy via Vision-Language Evaluation](https://arxiv.org/abs/2605.19613)

**<font color=#1a73e8>作者：</font>** Shuwei Li, Lei Tan, Robby T. Tan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color constancy aims to keep object colors consistent under varying illumination. Cross-camera generalization in color constancy remains challenging because learning-based models often overfit to the color response characteristics of the training camera, resulting in degraded performance on images captured by other cameras. We propose VLM-CC, a feedback-guided framework that formulates color constancy as an iterative refinement process. Instead of directly estimating the illuminant from raw input, VLM-CC performs iterative correction driven by vision-language model (VLM)-based evaluation. At each iteration, the image is white-balanced using the current estimate and converted to pseudo-sRGB. A lightweight LoRA-tuned VLM then assesses the corrected image, identifying the dominant residual color cast and providing qualitative feedback. This feedback is mapped to a residual illumination direction (red, green, or blue) and used to update the illuminant estimate until convergence. Our key idea is to reframe color constancy as an iterative perceptual feedback problem, leveraging VLM evaluation instead of direct RGB regression. By replacing direct RGB estimation with VLM-guided perceptual feedback, VLM-CC achieves state-of-the-art robustness in cross-camera color constancy across multiple datasets. Code will be available at this https URL.

---


### 208. [A Family of Divergence Measures for Evaluating the Reconstruction Quality of Explainable Ensemble Trees](https://arxiv.org/abs/2605.19618)

**<font color=#1a73e8>作者：</font>** Massimo Aria, Agostino Gnasso, Carmela Iorio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Validating interpretable surrogate models for ensemble learners requires measuring agreement between the ensemble's internal representation and its surrogate approximation, rather than mere association. Correlation-based approaches are scale-invariant and fail to detect systematic discrepancies in co-occurrence structure. We propose a statistical framework grounded in the agreement-association distinction, centered on the normalized Loss of Interpretability (nLoI). Rooted in the Cressie-Read power divergence family with lambda equal to 2, the nLoI admits a closed-form decomposition into within-node and between-node components, providing a unique diagnostic capability to identify precisely where and why reconstruction fails. The framework incorporates four complementary measures capturing distinct structural facets of approximation quality. A unified permutation testing procedure delivers valid inference for all measures within a single resampling pass. Theoretical properties, including boundedness and symmetry, are established for each metric. Monte Carlo simulations and empirical evaluations confirm exact Type I error control and demonstrate that these measures detect reconstruction fidelity gradients invisible to correlation-based alternatives. The framework is developed and illustrated in the context of Explainable Ensemble Trees (E2Tree), and empirical evaluation on three benchmark datasets illustrates the practical utility of the framework.

---


### 209. [MiMuon: Mixed Muon Optimizer with Improved Generalization for Large Models](https://arxiv.org/abs/2605.19619)

**<font color=#1a73e8>作者：</font>** Feihu Huang, Yuning Luo, Songcan Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix-structured parameters frequently appear in many artificial intelligence models such as large language models. More recently, an efficient Muon optimizer is designed for matrix parameters of large-scale models, and shows markedly faster convergence than the vector-wise algorithms. Although some works have begun to study convergence properties (i.e., optimization error) of the Muon optimizer, its generalization properties (i.e., generalization error) is still not established. Thus, in this paper, we study generalization error of the Muon optimizer based on algorithmic stability and mathematical induction, and prove that the Muon has a generalization error of $O\big(\frac{1}{N\kappa^{T}}\big)$, where $N$ is training sample size, and $T$ denotes iteration number, and $\kappa>0$ denotes minimum difference between singular values of gradient estimate. To enhance generalization of the Muon, we propose an effective mixed Muon (MiMuon) optimizer by cautiously using orthogonalization of gradient, which is a hybrid of Muon and momentum-based SGD optimizers. Then we prove that our MiMuon optimizer has a lower generalization error of $O\big(\frac{1}{N}\big)$ than $O\big(\frac{1}{N\kappa^{T}}\big)$ of Muon optimizer, since $\kappa$ generally is very small. Meanwhile, we also studied the convergence properties of our MiMuon algorithm, and prove that our MiMuon algorithm has the same convergence rate of $O(\frac{1}{T^{1/4}})$ as the Muon algorithm. Some numerical experimental results on training large models including Qwen3-0.6B and YOLO26m demonstrate efficiency of the MiMuon optimizer.

---


### 210. [Bézier Degradation Modeling for LiDAR-based Human Motion Capture](https://arxiv.org/abs/2605.19620)

**<font color=#1a73e8>作者：</font>** Xiaoqi An, Lin Zhao, Jun Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR-based 3D human motion capture has broad applications in fields such as autonomous driving and robotics, where accurate motion reconstruction is crucial. However, existing methods often struggle with unstable inputs and severe occlusions, leading to jittery or even failed pose predictions. To address these challenges, we propose BMLiCap, a coarse-to-fine framework that models motion using temporally compressible Bézier curves. By reducing control points through a trajectory-preserving strategy, we obtain a coherent and learning-friendly motion representation. To reconstruct human actions from LiDAR point-cloud cues, we design a progressive motion-reconstruction module. Specifically, a Time-scale Motion Transformer (TMT) is introduced to predict motion curves at multiple temporal scales, and a Multi-level Motion Aggregator (MMA) is utilized to adaptively fuse the multi-scale curves to recover detailed, temporally coherent poses, effectively bridging observation gaps caused by occlusions and noise. Across four mainstream benchmarks LiDARHuman26M, FreeMotion, NoiseMotion, and SLOPER4D, BMLiCap achieves state-of-the-art accuracy and temporal continuity in complex scenes, demonstrating its ability to compensate for severe occlusions and reduce prediction jitter.

---


### 211. [UniRefiner: Teaching Pre-trained ViTs to Self-Dispose Dross via Contrastive Register](https://arxiv.org/abs/2605.19622)

**<font color=#1a73e8>作者：</font>** Congpei Qiu, Zhaoyu Hu, Wei Ke 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation learning with Vision Transformers (ViTs) has advanced rapidly, yet the utility of large-scale models in spatially sensitive tasks is hindered by spurious tokens. Prior efforts to mitigate this have been limited, often defining these artifacts narrowly, for example, as simple high-norm outliers. We argue that this scope is insufficient. For dense prediction tasks, we posit that any token failing to encode location-aligned semantics should be treated as a spurious artifact. This broader definition reveals a more complex problem, leading us to systematically categorize and characterize three fundamental types of spurious tokens that corrupt spatial representations. Based on this comprehensive diagnosis, we propose UniRefiner, a universal refinement framework that teaches pre-trained ViTs to self-dispose of these artifacts. UniRefiner uses contrastive registers to explicitly isolate and redistribute spurious tokens via a dual objective: (i) it aligns image tokens with filtered regular tokens to preserve semantics, and (ii) it aligns register tokens with detected spurious tokens to capture the spurious signals. Our method requires only a few epochs of fine-tuning on ~5k images to refine diverse ViTs, including massive models like EVA-CLIP-8B and InternViT-6B. Experiments demonstrate consistent and significant improvements: notably, the refined EVA-CLIP-8B achieves 51.9\% mIoU on ADE20K (+9.4\%), surpassing specialized vision models like DINOv2 (49.1\%), while zero-shot segmentation accuracy improves by up to 22\%. UniRefiner unlocks the latent spatial potential of existing large-scale foundation models, paving the way for their broader application.

---


### 212. [PrAda: Few-Shot Visual Adaptation for Text-Prompted Segmentation](https://arxiv.org/abs/2605.19623)

**<font color=#1a73e8>作者：</font>** Gabriele Rosi, Fabio Cermelli, Carlo Masone 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmenting images is critical for visual understanding but demands extensive pixel-level annotations. Foundational models have enabled new paradigms for predicting new classes guided by textual prompts, without annotations from the target domain. Yet, on specialized target domains, far from the original pre-training, their performance degrades. We study the errors of existing methods under such domain-shift, finding that misclassification rather than mask generation is the main culprit. To address this, we introduce the novel problem of Few-Shot Visual Adaptation for text-prompted Segmentation. This kind of adaptation has been largely studied for image classification, but it remains unexplored for segmentation. We tackle this task with Prototype Adaptation (PrAda), a novel, parameter-efficient method that adapts a frozen text-prompted segmentation model. Our approach learns class-specific prototypes by combining fine-grained pixel features and high-level transformer representations, which are then fused with the original text-based predictions through a learned importance factor. This preserves the model's zero-shot potential while enabling strong adaptation to new domains. Experiments across semantic, instance, and panoptic segmentation on five benchmarks demonstrate that PrAda yields significant improvements over state-of-the-art and proposed baselines.

---


### 213. [Component-Aware Structure-Preserving Style Transfer for Satellite Sim2Real 6D Pose Estimation](https://arxiv.org/abs/2605.19624)

**<font color=#1a73e8>作者：</font>** Yonglong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular 6D pose estimation for non-cooperative satellites depends heavily on annotated training data, yet real satellite images with reliable pose labels and component-level masks are difficult to acquire at scale. Synthetic rendering can provide exact geometric annotations, but the appearance gap between rendered and real observations limits direct transfer to the real domain. This paper presents a component-aware structure-preserving style transfer framework for satellite synthetic-to-real data construction. The method builds weakly paired real--synthetic samples from calibrated real acquisition, ArUco-based camera-pose measurement, CAD rendering, and component masks. It then extracts part-wise real-domain style codes from unlabeled real images and injects them into corresponding synthetic satellite regions through mask-aligned modulation. To keep the generated images usable for downstream supervision, adversarial training is combined with local contrastive consistency, self-regularization, and edge-preserving constraints. Experiments are conducted on 5,000 rendered satellite images and 100 real images captured in a calibrated setup. The real images provide target-domain appearance references and final evaluation images, while the downstream GDRNet pose estimator is trained only on synthetic or translated synthetic images. Compared with representative image-translation baselines, the proposed method achieves the lowest image distribution discrepancy, with an FID of 54.32 and a KID of 0.048. When the translated data are used to train GDRNet in this target-domain adaptation setting, the ADD pass rate improves to 0.260 and the AUC improves to 0.611. These results indicate that component-level appearance transfer can improve satellite Sim2Real pose estimation in the considered calibrated setup while retaining simulation-derived geometric annotations.

---


### 214. [Optimal Reconstruction from Linear Queries](https://arxiv.org/abs/2605.19625)

**<font color=#1a73e8>作者：</font>** Yuval Filmus, Shay Moran, Elizaveta Nesterova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of reconstructing an unknown point in $\mathbb{R}^d$ from approximate linear queries. This setting arises naturally in applications ranging from low-dimensional remote sensing and signal recovery to high-dimensional data analysis and privacy-sensitive inference. Our main goal is to characterize the optimal reconstruction error as a function of the number of queries $T$, the ambient dimension $d$, and the noise parameter $\delta$.
We first analyze the limit $T \to \infty$ and show that the optimal reconstruction error converges to the explicit value $\sqrt{2d/(d+1)} \delta$, which plays a role analogous to the Bayes optimal error in supervised learning. When the dimension is fixed, we show that the excess error above this limit decays doubly exponentially fast as $T \to \infty$, a rate that is significantly faster than those typically encountered in learning curves. When the dimension grows, we show that a number of queries on the order of $\exp(d)$ is necessary and sufficient to achieve vanishing excess error. Finally, we introduce and analyze an improper variant of the reconstruction problem.
From a technical perspective, our main contribution is a generalization of Jung's theorem (1901). The classical theorem bounds the maximum possible radius of a set of diameter 1 and characterizes extremal bodies. Our generalization provides a robust variant that characterizes near-extremal bodies and is proved via geometric and dynamical arguments exploiting symmetry and Lie group actions.

---


### 215. [EMO-BOOST: Emotion-Augmented Audio-Visual Features for Improved Generalization in Deepfake Detection](https://arxiv.org/abs/2605.19630)

**<font color=#1a73e8>作者：</font>** Aritra Marik, Marcel Klemt, Anna Rohrbach  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With every advancement in generative AI models, forensics is under increasing pressure. The constant emergence of new generation techniques makes it impossible to collect data for each manipulation to train a deepfake detection model. Thus, generalizing to deepfakes unseen during training is one of the major challenges in current deepfake detection research. To tackle this challenge, we employ high-level semantic cues and argue that these cues can support low-level focused approaches in generalizing to unseen types of manipulations. In this work, we study emotions as a high-level semantic cue. We propose Emo-Boost, a multimodal deepfake detection framework that fuses an off-the-shelf RGB- and acoustic-focused deepfake detector with our emotion-based deepfake detector EmoForensics. EmoForensics utilises vision and audio emotion recognition modules and models intra- and inter-modal temporal consistency in emotion representations from an audio-visual stream. We found that EmoForensics and the low-level focused method capture complementary signals. Consequently, combining both signals in EmoBoost enhances the average cross-manipulation generalization AUC by 2.1% on FakeAVCeleb.

---


### 216. [optimize_anything: A Universal API for Optimizing any Text Parameter](https://arxiv.org/abs/2605.19633)

**<font color=#1a73e8>作者：</font>** Lakshya A Agrawal, Donghyun Lee, Shangyin Tan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can a single LLM-based optimization system match specialized tools across fundamentally different domains? We show that when optimization problems are formulated as improving a text artifact evaluated by a scoring function, a single AI-based optimization system-supporting single-task search, multi-task search with cross-problem transfer, and generalization to unseen inputs-achieves state-of-the-art results across six diverse tasks. Our system discovers agent architectures that nearly triple Gemini Flash's ARC-AGI accuracy (32.5% to 89.5%), finds scheduling algorithms that cut cloud costs by 40%, generates CUDA kernels where 87% match or beat PyTorch, and outperforms AlphaEvolve's reported circle packing solution (n=26). Ablations across three domains reveal that actionable side information yields faster convergence and substantially higher final scores than score-only feedback, and that multi-task search outperforms independent optimization given equivalent per-problem budget through cross-task transfer, with benefits scaling with the number of related tasks. Together, we show for the first time that text optimization with LLM-based search is a general-purpose problem-solving paradigm, unifying tasks traditionally requiring domain-specific algorithms under a single framework. We open-source optimize\_anything with support for multiple backends as part of the GEPA project at this https URL .

---


### 217. [P2DNav: Panorama-to-Downview Reasoning for Zero-shot Vision-and-Language Navigation](https://arxiv.org/abs/2605.19634)

**<font color=#1a73e8>作者：</font>** Kai Sheng, Liuyi Wang, Haojie Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-and-language navigation (VLN) requires an embodied agent to ground natural-language instructions into executable navigation actions in unseen environments. Existing zero-shot methods typically rely on additional waypoint prediction modules, which often entangle high-level directional reasoning with fine-grained local grounding, leading to error-prone and unstable decisions. In this paper, we propose P2DNav, a hierarchical framework for zero-shot vision-and-language navigation. P2DNav consists of three core components: Panorama-to-Downview (P2D), Sliding-Window Dialogue Memory (SDM), and Reflective Reorientation Mechanism (RRM). P2D explicitly decomposes navigation decision-making into two stages: panoramic direction selection and downview local grounding. It first selects the instruction-relevant direction from a 360° panorama, and then predicts a pixel-level target point from the downview RGB observation in that direction. In addition, SDM organizes navigation history as a multi-turn dialogue context and maintains recent visual observations within a sliding window to support long-horizon navigation. RRM further enables reflective reorientation by assessing the reliability of local grounding based on the downview observation and returning to panoramic direction selection when necessary. Experiments on the R2R-CE benchmark show that P2DNav achieves strong performance among zero-shot methods. In particular, compared with the state-of-the-art (SOTA) zero-shot waypoint-based and waypoint-free methods, P2DNav achieves SR gains of 146.6% and 58.9%, respectively, demonstrating the effectiveness of P2D, SDM, and RRM for zero-shot VLN. Code will be released for public use.

---


### 218. [Inferring Sensitive Attributes from Knowledge Graph Embeddings: Attack and Defense Strategies](https://arxiv.org/abs/2605.19644)

**<font color=#1a73e8>作者：</font>** Yasmine Hayder  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Knowledge Graphs (KGs) are a powerful representation of linked data, offering flexibility, semantic richness, and support for knowledge enrichment and reasoning. They help data owners organize and exploit heterogeneous data to provide insightful services (e.g., recommendations), yet real-world KGs are often incomplete, hiding true facts or missing valuable insights. Knowledge graph embedding techniques are commonly used to infer valuable missing information. However, reasoning over KGs can inadvertently expose sensitive user information, even when such data is not explicitly stored. In this work, we investigate the privacy risks associated with KGE-based reasoning, focusing on attribute inference attacks where adversaries attempt to deduce sensitive user attributes from seemingly non-sensitive outputs. We propose and evaluate a framework that mitigates these privacy risks by applying post processing sanitization techniques to KGE outputs. Preliminary results demonstrate the effectiveness of these attacks on the outputs of KGE models, and explore the trade-off between recommendation quality and privacy protection when applying randomization based approaches, highlighting the need to experiment with more advanced techniques in future work to address this issue.

---


### 219. [K-Quantization and its Impact on Output Performance](https://arxiv.org/abs/2605.19645)

**<font color=#1a73e8>作者：</font>** Robin Baki Davidsson, Pierre Nugues  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advancements in large language models (LLMs) have shown their remarkable capacities in many NLP tasks. However, their substantial size often presents challenges for deployment. This necessitates efficient techniques for model compression, with quantization emerging as a prominent solution. Despite its benefits, the exact impact of quantization (from 2- to 6-bit) on the performance and accuracy of LLMs remains an active area of research. This paper investigates the performance of eight LLMs at various quantization levels, focusing on tasks such as MMLU-Pro for knowledge processing and reasoning, CRUXEval for code comprehension, and MuSR for reading comprehension. Our results show a consistent trend where higher precision (e.g., 8-bit Q8\_0) yields improved performance, albeit with diminishing returns. Aggressive quantization (e.g., 2-bit Q2\_K) usually retains acceptable accuracy, though some models show a substantial loss in performance. Our findings indicate that while lower bit precision generally reduces performance, the impact varies across models and tasks. Larger models show greater resilience to aggressive quantization, but can still undergo significant drops at lower precision levels. Mid-sized models in the 7-9 billion parameter range strike an optimal balance between efficiency and resource usage. Such results provide insights into the trade-offs between model size, quantization, and performance.

---


### 220. [CAD-Free Learning of Spacecraft Pose Estimators via NeRF-Based Augmentations](https://arxiv.org/abs/2605.19649)

**<font color=#1a73e8>作者：</font>** Antoine Legrand, Renaud Detry, Christophe De Vleeschouwer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spacecraft pose estimation networks require tens of thousands of CAD-rendered images to be trained. This reliance on synthetic CAD data (i) limits applicability to targets with reliable geometry prior, excluding uncooperative or poorly documented spacecraft, and (ii) causes poor generalization to real on-orbit conditions due to unrealistic illumination and material appearance. This paper introduces a NeRF-based image augmentation method that enables the learning of spacecraft pose estimators from only a few tens to a few hundreds of images. The method learns a Neural Radiance Field of the target and generates a large, diverse dataset through geometrically-consistent viewpoint and appearance augmentation. This augmented dataset enables the training of accurate target-specific pose estimators without requiring a CAD model or large synthetic datasets. Experiments show that our approach supports the training of accurate pose estimators from only 25 to 400 realistic images, even under severe illumination variations. When applied on large CAD-based synthetic datasets, the NeRF-based augmentation also enhances out-of-domain generalization, yielding improved robustness to real on-orbit conditions.

---


### 221. [Cross-View Splatter: Feed-Forward View Synthesis with Georeferenced Images](https://arxiv.org/abs/2605.19656)

**<font color=#1a73e8>作者：</font>** Matias Turkulainen, Akshay Krishnan, Filippo Aleotti 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Cross-View Splatter, a feed-forward method that predicts pixel-aligned Gaussian splats for outdoor scenes captured at ground level AND by satellite. Faithful reconstructions require good camera coverage, but ground imagery is time-consuming and hard to capture at scale for large outdoor scenes. Fortunately, satellite imagery can provide a global geometric prior that is easy to access via public APIs. Cross-View Splatter fuses orthorectified satellite views with GPS-tagged ground photos to predict Gaussian splats in a unified 3D coordinate frame. By aligning ground and bird's-eye feature representations, our model improves scene coverage and novel-view synthesis, compared to ground imagery alone. We train on curated georeferenced datasets and paired satellite-terrain data, mined from open mapping services. We evaluate our method on a new benchmark for novel-view synthesis with georeferenced imagery allowing comparison to prior state-of-the-art methods. Our code and data preparation will be available at this https URL.

---


### 222. [SCARA: A Semantics-Constrained Autonomous Remediation Agent for Opaque Industrial Software Vulnerabilities](https://arxiv.org/abs/2605.19668)

**<font color=#1a73e8>作者：</font>** Bowei Ning, Xuejun Zong, Lian Lian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Critical-infrastructure operators are increasingly expected to assess and remediate vulnerabilities in deployed industrial software. However, much of this software exists as opaque industrial software (OIS), including stripped firmware, proprietary protocol handlers, and compiled control logic without source code, symbols, build environments, or hardware interfaces. While binary analysis can identify vulnerability candidates, existing automated repair systems largely rely on source code, compilable artifacts, sanitizer feedback, or instrumentable builds, leaving a gap between binary-level discovery and validated remediation. This paper presents SCARA, a Semantics-Constrained Autonomous Remediation Agent for OIS. SCARA operates under a source-unavailable defender model and connects upstream binary vulnerability candidates to conditionally validated remedies through a four-stage pipeline. Operational-state-aware verification (OSVA) filters infeasible candidates using a nine-component industrial state model; remediation synthesis (RSA) selects the strongest available remedy across protocol mitigation, binary hardening, and SSCKG-constrained source patches; and correctness validation (CVA) provides conditional correctness evidence via behavioral-coverage preservation, independent replay, and typed rejection feedback. On OIS-RemedBench, a 15-case benchmark spanning firmware, protocol handlers, and ICS/PLC artifacts, SCARA achieves observed 100% precision with no false positives, refutes 20.0% of cases as operationally infeasible, and reaches 88.9% remediation success after targeted reruns. To our knowledge, SCARA is the first end-to-end framework that connects binary vulnerability candidates to conditionally validated remediation for opaque industrial software.

---


### 223. [Transforming Constraint Programs to Input for Local Search](https://arxiv.org/abs/2605.19671)

**<font color=#1a73e8>作者：</font>** Jo Devriendt, Patrick De Causmaecker, Marc Denecker  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Applying local search algorithms to combinatorial optimization problems is not an easy feat. Typically, human intervention is required to compile the constraints to input data for some metaheuristic algorithm. In this paper, we establish a link between symmetry properties of constraint optimization problems and local search neighborhoods, and we use this link to automatically generate neighborhoods from a constraint specification in the context of the IDP system. We evaluate the obtained neighborhoods for six classical optimization problems. The resulting observations support the viability of this technique.

---


### 224. [Beyond Rational Illusion: Behaviorally Realistic Strategic Classification](https://arxiv.org/abs/2605.19674)

**<font color=#1a73e8>作者：</font>** Xinpeng Lv, Yunxin Mao, Renzhe Xu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Strategic classification(SC) studies the interaction between decision models and agents who strategically manipulate their features for favorable outcomes. Existing SC frameworks typically rely on the idealized assumption that agents are strictly rational. However, evidence from behavioral economics and psychology consistently shows that real-world decision-making is often shaped by cognitive biases, deviating from pure rationality. To formalize this limitation, we identify and define a new problem setting, termed the behaviorally realistic strategic classification problem, where agents' strategic manipulations deviate from full rationality due to psychological biases. Motivated by the identified limitation, we propose the Prospect-Guided Strategic Framework (Pro-SF) to address the problem, a principled framework grounded in prospect theory to model and learn under behaviorally realistic strategic responses. Specifically, to capture behaviorally realistic strategic manipulations, our framework reformulates the Stackelberg-style interaction between agents and the decision-maker by incorporating three key mechanisms inspired by prospect theory, including the asymmetry between benefits and costs, different subjective reference points, and non-rational probability distortion. Experiments on synthetic and real-world datasets establish Pro-SF as a behaviorally grounded approach to strategic classification, bridging machine learning and behavioral economics for more reliable deployment in the real world.

---


### 225. [TombWriter: Scaffolding Story Archeology through Beat-Level Interaction in Human-AI Co-Writing](https://arxiv.org/abs/2605.19681)

**<font color=#1a73e8>作者：</font>** Hugo Andersson, Niklas Elmqvist  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The dominant paradigm for LLM interaction in AI co-writing uses disposable prompts that vanish after use. This may lead to imprecise results, cumbersome workflows, and diminished author agency and ownership. We propose LLM-based story archeology, where prompts serve as a hierarchical story instrument refined over time to extract the writer's intended story. Drawing on the fossil theory of story- telling, where stories exist as latent structures that writers excavate through their craft, this approach supports agency and ownership through high involvement and control. Writers work at the level of story beats rather than prose. They generate character actions in scenes to discover emergent possibilities, simulated by the LLM or directly nudged, then edit resulting beats to refine scenes iteratively. Prose is generated from beats based on style and genre, separating structure from style. We developed TombWriter, a web-based tool that visualizes stories as navigable cards -- characters, scenes, and beats -- through a five-stage narrative pipeline. We conducted a qual- itative study with five experienced writers who used the system over three days. Through semi-structured interviews, we found that writers framed AI as a generation engine rather than collabo- rator, claimed ownership while reporting voice loss, and valued the system for structural discovery rather than prose production. We contribute the story archeology approach, the TombWriter system, and qualitative findings on beat-level human-AI co-writing.

---


### 226. [DocQT: Improving Document Forgery Localization Robustness via Diverse JPEG Quantization Tables](https://arxiv.org/abs/2605.19688)

**<font color=#1a73e8>作者：</font>** Kylian Ronfleux-Corail, Guillaume Bernard, Mickaël Coustaty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Document manipulation localization models achieve strong performance on public benchmarks yet fail to generalize to operational document workflows. We identify a critical and overlooked source of this gap: the mismatch between the narrow distribution of JPEG quantization tables used during training -restricted to standard libjpeg quality factors -and the heterogeneous compression profiles encountered in real-world insurance document pipelines. To isolate this factor, we conduct a controlled factorial study comparing two architectures with contrasting levels of quantization table awareness -FFDN [2] and Mesorch [20] -each trained under either standard quality factor augmentation (Standard-QT ) or operationally calibrated quantization tables sampled from DocQT, a quantization-table bank derived from a MAIF operational image corpus (Real-QT ), and evaluated under three recompression conditions. Training under Real-QT yields substantial localization gains on DocTamper [15] and significantly reduces the pixel-level false positive rate on authentic operational documents, but only for architectures that explicitly ingest the quantization table as input. The released DocQT quantization-table dataset and compression-reproduction material are directly available at this https URL. These results demonstrate that standard quality factor augmentation does not adequately proxy operational compression diversity, and that architectural choices explicitly conditioning on the quantization table provide a meaningful robustness advantage for real-world deployment.

---


### 227. [WBCAtt+: Fine-Grained Pixel-Level Morphological Annotations for White Blood Cell Images](https://arxiv.org/abs/2605.19692)

**<font color=#1a73e8>作者：</font>** Satoshi Tsutsui, Winnie Pang, Shuting He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The microscopic examination of white blood cells (WBCs) plays a fundamental role in pathology and is essential for diagnosing blood disorders such as leukemia and anemia. To support further research on WBC images, multiple datasets have been proposed. However, they mainly annotate cell categories, and lack detailed morphological characteristics that pathologists use to explain their interpretations of cells. To address this gap, we introduce WBCAtt+, a novel dataset of WBC images densely annotated with 11 morphological attributes and five pixel-level cell components. With 113k image-level labels and 10k segmentation maps, WBCAtt+ is the first to provide comprehensive annotations for WBC images. Leveraging this dataset, we provide baseline models for attribute recognition and semantic segmentation. We also design an attribute recognition model to incorporate compositional structure of cells, further improving the recognition performance. Lastly, we showcase various applications enabled by our dataset, such as explainable AI models, including counterfactual example generation. \revision{The dataset and code are publicly available\footnote{this https URL}}.

---


### 228. [Awakening the Hydra: Stabilizing Multi-Concept Backdoor Injection in Text-to-Image Diffusion Models](https://arxiv.org/abs/2605.19698)

**<font color=#1a73e8>作者：</font>** Kai Wang, Jiale Zhang, Chengcheng Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models are increasingly developed through open-source reuse and repeated downstream fine-tuning, where reused checkpoints are difficult to verify and thus more susceptible to hidden backdoor behaviors. In such ecosystems, a single pretrained model may be sequentially adapted and redistributed by multiple independent parties, allowing multiple concept-specific trigger-target associations to accumulate in the same model. When these associations coexist, semantic conflicts can be amplified in the shared representation space, leading to cross-concept entanglement and degraded generation quality. Notably, instead of strengthening the attack, such accumulation can destabilize previously injected behaviors and reduce attack reliability.
In this work, we systematically investigate backdoor attacks under this interference-prone setting and propose Hydra, a unified framework for robust and controlled multi-concept backdoor injection under cumulative and decentralized reuse. Our core insight is that stable backdoor injection under large-scale multi-concept settings requires explicitly constraining trigger semantics while coordinating cross-task interactions during optimization. Specifically, Hydra performs evolutionary trigger search in the text encoder space to identify triggers that are semantically aligned with their target concepts while remaining stable across other injected concepts. It further combines multi-task fine-tuning with trigger-clean regularization to improve training stability under dense multi-concept injection. Extensive experiments across multiple diffusion backbones under rigorous multi-concept settings show that Hydra maintains effective backdoor activation while preserving clean generation fidelity and image quality. For instance, across 8 attackers and 500 concept pairs, Hydra maintains ~95% ASR and strong clean generation.

---


### 229. [Physics-informed simulation framework for realistic sonar image generation and statistical validation](https://arxiv.org/abs/2605.19712)

**<font color=#1a73e8>作者：</font>** Kamal Basha S, Athira Nambiar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic sonar datasets offer a scalable alternative to costly real-world acquisition, yet their utility remains limited by the absence of rigorous quantitative validation. We present ACOUSIM (ACOustic SIMulation and Validation Platform), a physics-informed framework that evaluates the statistical alignment between synthetic and real sonar imagery without relying on generative models. A Gazebo-based environment generates sonar-like images by explicitly controlling seabed texture, illumination-driven shadowing, platform altitude, and noise. Realism is quantified against two public sonar datasets, SeabedObjects-KLSG-II and Sonar Common Target Detection (SCTD), using global intensity and local texture (LBP) distributions assessed via Kullback-Leibler divergence, Jensen-Shannon divergence, and Earth Mover's Distance. Results show strong texture alignment (KL < 0.07) across all classes, with plane-class intensity alignment outperforming ship-class due to shadow geometry complexity. ACOUSIM establishes a reproducible, distribution-level baseline for sim-to-real sonar evaluation and directly supports reliable dataset validation for underwater image analysis.

---


### 230. [Security Analysis of Bitcoin's V2 Transport Protocol: Exploiting Design Implications for Sustained Eclipse and Downgrade Attacks](https://arxiv.org/abs/2605.19715)

**<font color=#1a73e8>作者：</font>** Charmaine Ndolo, Florian Tschorsch  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bitcoin recently introduced a new protocol for the encryption of peer-to-peer (P2P) communication. The protocol, known as V2 P2P transport, represents a big step towards securing the overlay network against various previously-known attack vectors. Based on an analysis of V2 P2P transport, this work examines the current viability of said attacks and concludes that while they are now remediated, alternative attacks and paths to similar objectives exist. The identified shortcomings are conceptual (and not implementation bugs) and even applicable to other P2P networks. We show how a network-level attacker can identify application messages using the length of TCP payloads, can eclipse a target node by taking advantage of how encrypted communication channels work and can downgrade all of a node's connections to the unencrypted protocol by using the mechanisms designed for compatibility. We validate our contributions using a combination of network measurements, emulations and simulations. Finally, we propose a series of short-term and long-term countermeasures towards securing Bitcoin's P2P network. To the best of our knowledge, we are the first to study Bitcoin's security under V2 P2P transport.

---


### 231. [CAIT: A Syntactic Parsing Toolkit for Child-Adult InTeractions](https://arxiv.org/abs/2605.19718)

**<font color=#1a73e8>作者：</font>** Francesca Padovani, Xiulin Yang, Bastian Bunzeck 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> CHILDES is a paramount resource for language acquisition studies -- yet computational tools for analyzing its syntactic structure remain limited. Leveraging the recent release of the UD-English-CHILDES treebank with gold-standard Universal Dependencies (UD) annotations, we train a state-of-the-art dependency parser specifically tailored to CHILDES. The parser more accurately captures syntactic patterns in child--adult interactions, outperforming widely used off-the-shelf English parsers, including SpaCy and Stanza. Alongside the parser, we also release a Part-of-Speech tagger and an utterance-level construction tagger, which together form the open-source Syntactic Parsing Toolkit for Child--Adult InTeractions (CAIT). Through a detailed error analysis and a case study tracking the distribution of syntactic constructions across developmental time in CHILDES, we demonstrate the practical utility of the toolkit for large-scale, reproducible research on language acquisition.

---


### 232. [Projecting Latent RL Actions: Towards Generalizable and Scalable Graph Combinatorial Optimization](https://arxiv.org/abs/2605.19721)

**<font color=#1a73e8>作者：</font>** Franco Terranova, Guillermo Bernardez, Albert Cabellos-Aparicio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph combinatorial optimization (GCO) has attracted growing interest, as many NP-hard problems naturally admit graph formulations, yet their combinatorial explosion renders exact methods computationally intractable. Recent advances in Reinforcement Learning (RL) combined with Graph Neural Networks (GNNs) have significantly improved learning-based GCO solvers. However, existing approaches face limitations in both generalization across diverse graph instances and computational scalability as action spaces grow. To address both challenges, we introduce projection agents, a novel RL-GCO approach that operates directly in a continuous GNN-based action embedding space, predicting a desired latent action in a single forward pass and subsequently decoding it into a valid discrete action. Additionally, we enable fair comparison across RL methods through a shared embedding space for both observations and actions. Across diverse benchmarks, our approach achieves up to 16.2x faster inference and up to 40% better generalization than existing solutions using only simple nearest-neighbor decoding, while opening the door to strong RL performance in super-linear decision spaces with multiple interdependent variables. Finally, we release LaGCO-RL, a Python library that automates latent action-space construction and supports existing RL-GCO solutions, promoting reproducibility and adaptation to new GCO benchmarks.

---


### 233. [Aero-World: Action-Conditioned Aerial Video Generation from Inertial Controls](https://arxiv.org/abs/2605.19728)

**<font color=#1a73e8>作者：</font>** Abdul Mohaimen Al Radi, Kunyang Li, Yuzhang Shang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation video models produce visually impressive results, but their use in embodied AI remains limited because they are primarily trained on natural language rather than low-level control signals. This limitation is especially pronounced for aerial flight, where motion occurs in unconstrained 6-DoF space and small errors in ego-motion can produce large trajectory drift. Generating aerial videos that follow fine-grained inertial actions can support scalable training and evaluation of aerial agents by providing a controllable proxy for real-world or expensive simulation data. To address this problem, we propose \textbf{Aero-World}, a method for converting a pretrained image-to-video diffusion model into a controllable aerial video generator. Aero-World injects sequences of translational acceleration and angular velocity into a pretrained latent diffusion transformer through an action-token stream. A frozen latent-space Physics Probe, trained independently on real video--IMU pairs, provides differentiable inertial-consistency supervision during LoRA finetuning while avoiding computationally expensive video decoding. We further propose \textbf{AeroBench}, a benchmark for evaluating whether generated drone videos adhere to low-level action signals. AeroBench uses Action Alignment Score (AAS) to measure agreement with commanded inertial actions and Physical Consistency Rate (PCR) to measure temporal motion stability. On AeroBench, Aero-World improves mean AAS from 57.7 to 63.6 over action-only finetuning and gives a stronger quality-control trade-off than AirScape, with lower FVD (596.5 vs. 1058.6), higher SSIM (0.595 vs. 0.505), and higher Flow-IMU correlation (0.44 vs. 0.20). These results suggest that frozen Physics Probe supervision is a practical mechanism for adapting pretrained video generators toward more action-aligned aerial motion.

---


### 234. [LIFT and PLACE: A Simple, Stable, and Effective Knowledge Distillation Framework for Lightweight Diffusion Models](https://arxiv.org/abs/2605.19729)

**<font color=#1a73e8>作者：</font>** Hyunsoo Han, Sangyeop Yeo, Jaejun Yoo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We demonstrate that in knowledge distillation for diffusion models, the teacher network's highly complex denoising process - stemming from its substantially larger capacity - poses a significant challenge for the student model to faithfully mimic. To address this problem, we propose a coarse-to-fine distillation framework with LInear FiTtingbased distillation (LIFT) and Piecewise Local Adaptive Coefficient Estimation (PLACE). First, LIFT decomposes the objective into a "coarse" alignment and a "fine" refinement. The student is then trained on coarse alignment before proceeding to hard refinement. Second, PLACE extends LIFT to address spatially non-uniform errors by partitioning outputs into error-based groups, providing locally adaptive guidance. Our experiments show that LIFT and PLACE is effective across diffusion spaces (image/latent), backbones (U-Net/DiT), tasks (unconditional/conditional), datasets, and even extends to flow-based models such as MMDiT (SD3). Furthermore, under extreme compression with a 1.3M-parameter student (only 1.6% of the teacher), conventional KD fails to provide sufficient guidance for stable training, with FID scores often degrading to 50-200+, but our method remains stably convergent and achieves an FID of 15.73.

---


### 235. [GeoMamba: A Geometry-driven MambaVision Framework and Dataset for Fine-grained Optical-SAR Object Retrieval](https://arxiv.org/abs/2605.19734)

**<font color=#1a73e8>作者：</font>** Tiantong Fang, Xiuwei Wang, Jing Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-source remote sensing enables complementary observation of ground objects, while cross-modal fine-grained object retrieval remains challenging, especially under unaligned optical and SAR conditions. Unlike conventional retrieval settings that rely on paired or spatially aligned samples, practical optical-SAR retrieval is affected by substantial modality discrepancy, speckle noise, and structural inconsistency, which limit robust cross-modal representation learning. To address this problem, we propose GeoMamba, a geometry-driven framework tailored for optical-SAR fine-grained retrieval. Specifically, GeoMamba introduces a Geometric Feature Injection (GFI) module that enhances cross-modal feature interaction and incorporates structural priors, thereby improving the robustness of SAR representations and promoting geometry-consistent feature learning. In addition, a Geometric Consistency Constraint (GCC) module, together with a Deep Supervision (DS) strategy, imposes hierarchical geometric constraints using classical operators, which helps preserve informative object structures during representation learning. We further construct a new dataset, FGOS-as, containing 11 aerospace and maritime categories for evaluating unaligned cross-modal fine-grained object retrieval in realistic remote sensing scenarios. Extensive experiments on FGOS-as demonstrate that GeoMamba outperforms existing methods, achieving 63.3% mAP and 77.0% Rank-1 accuracy in all-to-all retrieval setting.

---


### 236. [TERGAD: Structure-Aware Text-Enhanced Representations for Graph Anomaly Detection](https://arxiv.org/abs/2605.19738)

**<font color=#1a73e8>作者：</font>** Wen Shi, Zhe Wang, Huafei Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph Anomaly Detection (GAD) aims to identify atypical graph entities, such as nodes, edges, or substructures, that deviate significantly from the majority. While existing text-rich approaches typically integrate structural context into the data representation pipeline using raw textual features, they often neglect the structural context of nodes. This limitation hinders their ability to detect sophisticated anomalies arising from inconsistencies between a node's inherent content and its topological role. To bridge this gap, we propose TERGAD (Structure-aware Text-enhanced Representations for Graph Anomaly Detection), A novel data augmentation framework that enriches structural semantics for GAD via the semantic reasoning capabilities of Large Language Models (LLMs). Specifically, TERGAD translates node-level topological properties into descriptive natural language narratives, which are subsequently processed by an LLM to derive high-level semantic embeddings. These embeddings are then adaptively fused with original node attributes through a gated dual-branch autoencoder to jointly reconstruct both graph structure and node features. The anomaly score is computed based on the integrated reconstruction error, effectively capturing deviations in both observable attributes and LLM-informed semantic expectations. Extensive experiments on six real-world datasets demonstrate that TERGAD consistently outperforms state-of-the-art baselines. Furthermore, our ablation studies validate the indispensable role of structural semantic guidance and the efficacy of the gated fusion mechanism. Code is available at this https URL.

---


### 237. [FlowErase-RL: Rethinking Concept Erasure as Reward Optimization in Flow Matching Models](https://arxiv.org/abs/2605.19739)

**<font color=#1a73e8>作者：</font>** Yi Sun, Zhiqi Zhang, Xinhao Zhong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in flow matching models have significantly improved text-to-image generation quality, but also introduce growing safety risks due to the generation of harmful or undesirable content. Existing concept erasure methods are either inference-time interventions with limited effectiveness or rely on supervised fine-tuning (SFT), which requires precisely aligned data and struggles with scalability and multi-concept settings. In this paper, we propose \emph{FlowErase-RL}, the first GRPO-based framework for concept erasure in flow matching models. We reformulate concept erasure as a reward optimization problem and introduce a \textbf{dynamic dual-path reward mechanism} that jointly optimizes (i) a Concept Erasure (CE) reward to suppress target concepts and (ii) a Non-target Space (NS) reward to preserve generative fidelity. The two reward paths are adaptively balanced during training via a performance-driven switching strategy, enabling stable optimization without explicit supervision. Extensive experiments on nudity, object, and artistic style erasure demonstrate that our method achieves state-of-the-art erasure performance while maintaining strong image quality and semantic alignment. Moreover, it exhibits robust resistance to adversarial attacks and scales effectively to multi-concept scenarios. Our results establish a new paradigm for safe and controllable generation in flow matching models.

---


### 238. [Real-World On-Vehicle Evaluation of Embedding-Based Anomaly Detection](https://arxiv.org/abs/2605.19744)

**<font color=#1a73e8>作者：</font>** Albert Schotschneider, Daniel Bogdoll, Svetlana Pavlitska 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting anomalies in traffic scenes is crucial for ensuring safety in autonomous driving, yet collecting representative anomalous data remains challenging. Existing anomaly detection methods are highly specialized and rely on normality as defined by the abstract semantic Cityscapes classes, making it difficult to adapt to diverse real-world scenarios. We propose an adaptable real-time anomaly detection method that leverages foundation models in the form of pretrained vision transformer embeddings to detect deviations via nearest-neighbor similarity in the latent semantic feature space. Based on patch-wise processing, the algorithm produces dense anomaly masks, allowing for the localization of detected anomalies. The method robustly models normality through a single reference image. This formulation avoids explicit supervision and dataset-specific training, making it suitable for real-world deployment. We evaluate the method on standard benchmarks and on an automated vehicle in real-world scenarios. Despite its simplicity, the method achieves good performance on the Road Anomaly benchmark and demonstrates consistent qualitative behavior in practice, successfully highlighting semantically unusual objects in diverse scenes. These results suggest that simple, reference-based methods can provide useful anomaly signals under realistic operating conditions.

---


### 239. [Memory-Augmented Reinforcement Learning Agent for CAD Generation](https://arxiv.org/abs/2605.19748)

**<font color=#1a73e8>作者：</font>** Yin Xiaolong, Liu Yu, Shen Jiahang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic generation of computer-aided design (CAD) models is a core technology for enabling intelligence in advanced manufacturing. Existing generation methods based on large language models (LLMs) often fall short when handling complex CAD models characterized by long operation sequences, diverse operation types, and strong geometric constraints, primarily because reasoning chains break and effective error-correction mechanisms are lacking. To address this problem, this paper proposes a memory-augmented reinforcement learning framework for CAD generation agents. The framework encapsulates the underlying geometric kernel into a structured toolchain callable by the agent and builds a closed-loop mechanism of design intent understanding, global planning, execution, and multi-dimensional verification. It also designs a dual-track memory module consisting of a case library and a skill library, and proposes a dynamic utility retrieval algorithm. By introducing reinforcement learning into retrieval and policy optimization, the agent can effectively avoid retrieval traps in which examples are semantically similar but geometrically infeasible, enabling online self-correction and continual evolution without additional large-scale annotated data. Experiments show that the proposed method significantly improves both the success rate and geometric consistency on complex CAD model generation tasks.

---


### 240. [CPC-VAR:Continual Personalized and Compositional Generation in Visual Autoregressive Models](https://arxiv.org/abs/2605.19750)

**<font color=#1a73e8>作者：</font>** Junhao Li, Xinhao Zhong, Yi sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual autoregressive (VAR) models have recently emerged as an efficient paradigm for text-to-image generation. Despite their strong generative capability, existing VAR-based personalization methods remain limited to static settings, failing to accommodate evolving user demands. In particular, sequential concept learning leads to severe catastrophic forgetting, while multi-concept synthesis often suffers from feature entanglement and attribute inconsistency. In this work, we present the first systematic study of continual personalized generation in VAR models. We identify two key challenges: (i) preserving previously learned concepts during sequential customization, and (ii) composing multiple personalized concepts in a controllable manner. To address these issues, we propose a unified framework with two core components. For continual single-concept learning, we introduce Gradient-based Concept Neuron Selection (GCNS), which identifies concept-relevant neurons and constrains only conflicting parameters across tasks, effectively mitigating forgetting without additional model expansion. For multi-concept synthesis, we propose a context-aware composition strategy that performs multi-branch feature modeling and localized cross-attention fusion guided by spatial conditions, enabling precise and disentangled concept composition. Extensive experiments demonstrate that our method significantly improves performance in long-sequence continual personalization while achieving superior results in multi-concept image synthesis compared to existing baselines. These findings highlight the potential of VAR models for scalable and controllable personalized generation.

---


### 241. [CogScale: Scalable Benchmark for Sequence Processing](https://arxiv.org/abs/2605.19758)

**<font color=#1a73e8>作者：</font>** Yannis Bendi-Ouis, Romain de Coudenhove, Xavier Hinaut  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The ability to maintain and manipulate information over time is a fundamental aspect of living beings and Artificial Intelligence. While modern models have achieved remarkable success in tasks like natural language processing, evaluating the capacity of novel architectures to process sequential information remains computationally expensive and time-consuming. Testing a new architecture often requires scaling up to massive datasets and models, leading to vast computational costs and slow iteration cycles. In this paper, we propose CogScale, a benchmark of 14 scalable synthetic tasks designed to isolate and evaluate specific cognitive and memory abilities at different parametrizable scales. By providing a standardized, lightweight framework, CogScale allows researchers to rapidly validate architectural innovations before committing to large-scale training. To establish a solid baseline, we evaluate seven distinct architectures: Gated Recurrent Unit (GRU), Long Short-Term Memory (LSTM), xLSTM, Echo State Network (ESN), Mamba, Transformer Decoder, and Transformer Encoder-Decoder. These evaluations are conducted under strict parameter budgets (1k, 10k, and 100k) and across different difficulty levels and scales. Our results show that while classical RNNs and Echo State Networks excel at basic retention within strict parameter budgets, only attention mechanisms and modern state-space models consistently maintain high performance as reasoning complexity and task difficulty scale.

---


### 242. [What Really Improves Mathematical Reasoning: Structured Reasoning Signals Beyond Pure Code](https://arxiv.org/abs/2605.19762)

**<font color=#1a73e8>作者：</font>** Yuze Zhao, Junpeng Fang, Lu Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Code has become a standard component of modern foundation language model (LM) training, yet its role beyond programming remains unclear. We revisit the claim that code improves reasoning through controlled pretraining experiments on a 10T-token corpus with fine-grained domain separation. Our findings are threefold. First, when code is restricted to standalone executable programs and Code-NL data are controlled for, code substantially improves programming ability but does not act as a general reasoning enhancer; instead, it competes with knowledge-intensive tasks, especially complex mathematical reasoning. Second, the reasoning gains often attributed to code are better explained by cross-domain structured reasoning traces, such as code-text and math-text mixtures, rather than by executable code alone. Third, increasing the density of structured math-domain samples within a fixed math budget yields substantial gains on difficult mathematical reasoning while largely preserving programming performance, suggesting that cognitive scaffolds offer a targeted way to mitigate cross-domain trade-offs. Finally, routing analyses show that data-composition effects are reflected in expert-activation patterns, providing mechanism-level evidence for competitive and synergistic interactions across domains. Our results clarify which data characteristics transfer across capability dimensions and point to more precise data-centric optimization strategies.

---


### 243. [Synthesis and Evaluation of Long-term History-aware Medical Dialogue](https://arxiv.org/abs/2605.19766)

**<font color=#1a73e8>作者：</font>** Hebin Hu, Renke Dai, Ah-Hwee Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An effective healthcare agent must be able to recall and reason over a patient's longitudinal medical history. However, the absence of datasets with realistic long-term dialogue timelines limits systematic evaluation. Real clinical text is constrained by privacy and ethics, while existing benchmarks focus on isolated interactions, failing to capture cross-session reasoning. We introduce a framework for synthesizing high-quality, long-term medical dialogues with LLMs. Our approach entails a knowledge-guided decomposition into three stages: constructing synthetic patient profiles with diverse disease and complication trajectories, generating multi-turn dialogues per encounter, and integrating them into a coherent longitudinal history dataset, MediLongChat. We establish three benchmark tasks-In-dialogue Reasoning, Cross-dialogue Reasoning, and Synthesis Reasoning-to evaluate the memory capabilities of healthcare agents. To assess data quality, we introduce a multi-dimensional evaluation framework combining vector-based metrics with LLM-as-a-judge assessments. Specifically, we define automatic measures-Faithfulness, Coherence, and Diversity-together with two LLM-based evaluations: Correctness and Realism. Benchmark experiments show that even state-of-the-art LLMs struggle with MediLongChat. These findings highlight the benchmark's applicability and underscore the need for tailored methods to advance healthcare agents.

---


### 244. [Minimax Optimal Variance-Aware Regret Bounds for Multinomial Logistic MDPs](https://arxiv.org/abs/2605.19768)

**<font color=#1a73e8>作者：</font>** Pierre Boudart, Pierre Gaillard, Alessandro Rudi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study reinforcement learning for episodic Markov Decision Processes (MDPs) whose transitions are modelled by a multinomial logistic (MNL) model. Existing algorithms for MNL mixture MDPs yield a regret of $\smash{\tilde{O}(dH^2\sqrt{T})}$ (Li et al., 2024), where $d$ is the feature dimension, $H$ the episode length, and $T$ the number of episodes. Inspired by the logistic bandit literature (Abeille et al., 2021; Faury et al., 2022; Boudart et al., 2026), we introduce a problem-dependent constant $\bar\sigma\_T \leq 1/2$, measuring the normalised average variance of the optimal downstream value function along the learner's trajectory. We propose an algorithm achieving a regret of $\smash{\tilde{O}(dH^2\bar\sigma\_T\sqrt{T})}$, which recovers the existing bound in the worst case and improves upon it for structured MDPs. For instance, for KL-constrained robust MDPs, $\bar\sigma\_T = O(H^{-1})$, reducing the horizon dependence by a factor $H$. We further establish a matching $\smash{\Omega(dH^2\bar\sigma\_T\sqrt{T})}$ lower bound, proving minimax optimality (up to logarithmic factors) and fully characterising the regret complexity of MNL mixture MDPs for the first time.

---


### 245. [OpenComputer: Verifiable Software Worlds for Computer-Use Agents](https://arxiv.org/abs/2605.19769)

**<font color=#1a73e8>作者：</font>** Jinbiao Wei, Qianran Ma, Yilun Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present OpenComputer, a verifier-grounded framework for constructing verifiable software worlds for computer-use agents. OpenComputer integrates four components: (1) app-specific state verifiers that expose structured inspection endpoints over real applications, (2) a self-evolving verification layer that improves verifier reliability using execution-grounded feedback, (3) a task-generation pipeline that synthesizes realistic and machine-checkable desktop tasks, and (4) an evaluation harness that records full trajectories and computes auditable partial-credit rewards. In its current form, OpenComputer covers 33 desktop applications and 1,000 finalized tasks spanning browsers, office tools, creative software, development environments, file managers, and communication applications. Experiments show that OpenComputer's hard-coded verifiers align more closely with human adjudication than LLM-as-judge evaluation, especially when success depends on fine-grained application state. Frontier agents struggle with end-to-end completion despite partial progress, and open-source models exhibit sharp drops from their OSWorld-Verified scores, exposing a persistent gap in robust computer automation.

---


### 246. [Preferences Order, Ratings Anchor: From Fused Expert Aesthetic Ground Truth to Self-Distillation](https://arxiv.org/abs/2605.19776)

**<font color=#1a73e8>作者：</font>** Yuanpei Zhao, Jie Lin, Chao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pairwise preferences and pointwise ratings are the two dominant annotation protocols in image aesthetic assessment (IAA), yet existing benchmarks adopt only one, leaving their complementarity unmeasured under controlled conditions. We introduce PPaint, a matched dual-protocol benchmark in which 15 domain experts, 5 per category, annotate 150 Chinese paintings under both protocols across five aesthetic dimensions, collecting 45,900 pairwise expert judgments through a locally dense preference design alongside the matched ratings. The matched design reveals complementary strengths: preferences yield more consistent ordinal rankings, while ratings anchor the absolute score scale. Fusing both signals via two independent preference-to-score methods yields a fused expert ground truth on which the two constructions converge to nearly identical scores. The same preference-to-score principle extends to label-free VLM training. PSDistill converts VLM pairwise judgments into calibrated pseudo-scores via an Elo reference pool, and trains the same VLM with confidence-weighted ranking optimization to produce a single-pass aesthetic scorer. Trained on a single painting category, the distilled Qwen3-VL-8B improves mean SRCC from 0.504 to 0.709 across all three categories, outperforming all open-source baselines including the dedicated aesthetic model ArtiMuse and matching closed-source Gemini-3.1-Pro within 0.04 SRCC at single-pass inference cost, with cross-domain transfer further validated on APDDv2. We will release the full PPaint dataset and training code.

---


### 247. [B-cos GNNs: Faithful Explanations through Dynamic Linearity](https://arxiv.org/abs/2605.19778)

**<font color=#1a73e8>作者：</font>** Joschka Groß, Mohammad Shaique Solanki, Verena Wolf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce B-cos GNNs, an inherently explainable class of graph neural networks whose predictions decompose exactly into per-node, per-feature contributions via a single input-dependent linear map. B-cos GNNs use linear (sum-based) aggregation and replace non-linear message and update functions with B-cos transforms. This induces meaningful, task-specific weight-input alignment that is directly accessible through the model's dynamic linearity. Instance-level explanations follow from a single forward and backward pass, requiring no auxiliary explainer, modified learning objective, or perturbation procedure. Instantiated as a GIN, our approach trades small losses in predictive accuracy for state-of-the-art explainability across diverse synthetic and real-world benchmarks, producing explanations orders of magnitude faster than post-hoc baselines.

---


### 248. [Distribution-Free Uncertainty Quantification for Continuous AI Agent Evaluation](https://arxiv.org/abs/2605.19779)

**<font color=#1a73e8>作者：</font>** Yuxuan Gao, Megan Wang, Yi Ling Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We adapt split conformal prediction and adaptive conformal inference (ACI) to continuous AI agent evaluation, providing distribution-free coverage guarantees for forecasted quality scores. Conformal intervals achieve calibration error below 0.02 across all nominal levels at the 24h horizon, while ACI correctly widens intervals by 35% following agent releases then reconverges. We further develop compositional uncertainty bounds for multi-agent pipelines (validated via simulation across inter-stage correlations rho in [-0.5, 0.9]), a conformal abstention rule for pairwise rankings with controlled false-ranking rate, and FDR-corrected abstention for leaderboard-scale multiple testing. Evaluating 50 agents via 18 real-time signals collected hourly, we show that per-agent conditional coverage is well-concentrated around the nominal level (mean 80.4%, 90% of agents within [72%, 90%]), and that cross-source sentiment divergence predicts ranking instability (r=0.64, p<0.01). A circularity-controlled validation confirms the framework captures signal beyond benchmarks (rho_s=0.52, p<0.01, n=35). Code and data are released under CC BY 4.0.

---


### 249. [From SGD to Muon: Adaptive Optimization via Schatten-p Norms](https://arxiv.org/abs/2605.19781)

**<font color=#1a73e8>作者：</font>** Thomas Massena, Corentin Friedrich, Mathieu Serrurier  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern optimizers, like Muon, impose matrix-wise geometry constraints on their updates. These matrix-wise constraints can be unified under Linear Minimization Oracle (LMO) theory. However, all current methods impose fixed LMO geometries for the update rules, chosen by-design or empirically, which are not necessarily optimal according to the problem's geometry. We introduce a novel efficient datadriven criterion for dynamically choosing proxy-optimal update LMO geometries on individual Deep Neural Network layers. Derived in closed form from gradient and activation statistics using a single-step random feature regression surrogate model, our criterion navigates a design space interpolating from SGD to Muon updates. Moreover, integrating parameter-wise preconditioning allows our framework to recover SGD, Muon, Adam, and MuAdam as specific extrema. To make this adaptive approach scalable, we pair it with efficient computational strategies, achieving only a $\sim$ 3% runtime overhead on highly optimized baselines. As a proof of concept, we show that this data-driven optimizer beats or remains competitive with the performance of the best performing optimizer between Muon and AdamW across three different training scenarios. Ultimately, this work provides evidence that LMO geometry can be successfully and efficiently adapted from runtime data, opening a new pathway for optimizer design beyond static geometries.

---


### 250. [Fast 4D Mesh Generation by Spatio-Temporal Attention Chains](https://arxiv.org/abs/2605.19786)

**<font color=#1a73e8>作者：</font>** Dvir Samuel, Yuval Atzmon, Gal Chechik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D mesh generation has recently emerged as a powerful paradigm for recovering dynamic 3D structure from videos, but existing methods remain slow, computationally expensive, and difficult to scale to longer sequences. We introduce a training-free approach that accelerates 4D mesh generation while improving temporal correspondence quality. Our key observation is that temporal correspondences emerge inside a 4D backbone long before its generated meshes become visually accurate. We exploit this with a general framework we call Spatio-Temporal Attention Chain which propagates information across space and time. Starting from vertices on an anchor mesh, the chain maps vertices to latent tokens. It then follows temporal correspondences in latent space, and recovers frame-specific vertices through latent-to-vertex attention. This design avoids expensive explicit matching while preserving anchor mesh details and thereby improving dynamic mesh geometry and temporal consistency.
Compared to state-of-the-art, our method generates a 4D mesh in 9 seconds, achieving a $13\times$ speedup while producing higher-quality results. Moreover, our approach scales to videos up to $16\times$ longer without degrading mesh quality. Beyond generation, the improved correspondences enable competitive zero-shot performance on two downstream tasks: 2D object tracking and 4D tracking. We further show that our framework enables reliable camera estimation, a capability not supported by prior 4D mesh generation methods.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-338](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

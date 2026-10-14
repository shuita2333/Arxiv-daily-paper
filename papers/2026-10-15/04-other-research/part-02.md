# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 51. [GeoFix: Geometry Fixing for 4D Consistent Generation](https://arxiv.org/abs/2610.14293)

**<font color=#1a73e8>作者：</font>** Yeobin Hong, Hyojun Go, Dohun Lee 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models increasingly serve as priors for 4D generation, but the generated videos often lack geometric consistency. Recent approaches address this through post-training by designing geometric rewards, yet this can degrade texture and fine detail, requiring auxiliary appearance rewards and careful reward balancing. To address this challenge, we propose GeoFix, a unified framework that improves geometric consistency and visual quality with a single geometric reward, applicable to both training and inference-time reward alignment. Our reward measures cross-view depth consistency in static scene regions, targeting structural inconsistencies without directly constraining appearance or penalizing valid object motion. Crucially, depth agreement increases with camera field-of-view overlap even in real videos and 4D datasets, allowing a smaller camera movement to be mistaken for better geometry. We account for this effect by calibrating the reward against the overlap-dependent trend. GeoFix achieves a 39% improvement in WorldScore 3D consistency and a 4% increase in VBench Quality Score.

---


### 52. [Controllable Diverse Sampling through Pullback Directions](https://arxiv.org/abs/2610.14294)

**<font color=#1a73e8>作者：</font>** Sylvain Dehayem Kenfouo, Aaron Zweig, Mingxuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conditional diffusion models can generate high-quality images that align closely with a given prompt. However, samples generated from different random seeds may remain visually similar, limiting creative exploration. Existing approaches can increase variation, but often require additional optimization or sampling overhead, while stronger perturbations may introduce distortions that degrade image quality or prompt alignment. We propose a training-free method that leverages the local pullback geometry induced by the mapping from the conditioning-embedding space to the image space to identify directions of maximal output sensitivity. By steering different sampling trajectories along these directions, we encourage distinct generations while maintaining consistency with the conditioning signal. Experiments on MS-COCO and BrushNet show the efficacy of the method in improving diversity on prompt-conditioned image generation and inpainting.

---


### 53. [ARMOR: Adversary Cost Amplification via a Schema-Preserving Password-Hardening Retrofit for Resource-Constrained Systems](https://arxiv.org/abs/2610.14300)

**<font color=#1a73e8>作者：</font>** Avinash Srinivasan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Internet of Things (IoT) gateways, edge authentication servers, and legacy systems need protection against offline password guessing after credential-database disclosure. Memory-hard key derivation functions (KDFs) are the preferred defense, but their resource requirements can exceed memory or latency budgets. ARMOR addresses this gap with a schema-preserving verifier-side transform for database-only (DB-only) compromise. Secret per-account chains of injective operations reside in an isolated Chain Registry. Fixed terminal escape encoding preserves distinct pre-hash values under each chain and moves outputs outside printable ASCII. We evaluate NAIVE adversaries using unmodified cracking tools and AWARE adversaries that enumerate chains. For the evaluated pre-hardened three-operation chains, NAIVE recovery is at most 0.10% on non-digit targets. Escape encoding yields zero recovery of digit-only targets under evaluated stock rule-based and non-rule attacks, closing a bypass permitting up to 45.3% recovery. Across 14.05 million eligible RockYou password entries, retaining duplicates, the median conditional guessing number is approximately 52 output-class tests at depth three and 317 at depth five. These values quantify the chain-search subproblem given the correct plaintext under a unit-cost model. A separate historical 14-operation AWARE evaluation matches all transformed targets at full dictionary coverage. Deployment measurements show microsecond-scale bare-metal transforms on three IoT boards, with protected storage dominating the measured TrustZone-M prototype components. Although an isolated high-entropy pepper provides stronger cryptographic protection, ARMOR combines compact per-account chain storage with low transform cost. When resources permit and the KDF accepts the complete transformed output, ARMOR composes as KDF(ARMOR(password)).

---


### 54. [Learning to See through Action: Predictive Curiosity for Robots](https://arxiv.org/abs/2610.14302)

**<font color=#1a73e8>作者：</font>** Stelios Zarifis, Panagiotis Filntisis, George Retsinas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Humans and animals do not learn vision from a fixed set of data: they move, interact, and learn from the visual consequences of their actions. Motivated by this developmental view, we study whether robots can improve visual learning by actively collecting experience through curiosity-driven interaction. We introduce DySCOVER, a self-supervised framework for active robot visual learning. A robot observes RGB frames, learns a visual autoencoder that encodes and reconstructs them, and trains a recurrent world model to predict the next visual latent state conditioned on the current state and action. The agent's policy is trained only with intrinsic rewards: reconstruction error encourages visually novel observations, while the world model's error encourages transitions whose consequences are not yet predictable. This prediction error biases the policy toward more intricate trajectories that enrich the agent's set of experiences with observations beyond those encouraged by visual novelty alone. Our experiments conducted with robotic arms as the embodied agents show that adding predictive curiosity improves the vision model over using visual curiosity alone. Across variations in initial conditions, experience capacity, embodiment, and scene content, adding predictive curiosity consistently improved visual learning. These results show that predictive curiosity can improve active visual learning beyond reconstruction-based curiosity alone.

---


### 55. [Plottery: A Code-Integrated GUI for Matplotlib](https://arxiv.org/abs/2610.14306)

**<font color=#1a73e8>作者：</font>** Brian Hempel, Ruanqianqian Huang, Devamardeep Hayatpur 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Scientists have many tools to author plots: graphical direct manipulation apps like a spreadsheet's chart builder, text-based programming tools like Matplotlib and ggplot2, or AI chat interfaces. Textual code is the most capable of these, but writing code, even with AI assistance, is a potentially poor fit for graphical chart design. We present Plottery, a Jupyter notebook extension that leverages API type annotations to add graphical direct manipulation to the popular Matplotlib plotting library. User interactions in Plottery's in-situ graphical interface are immediately reified in the user's code, so they may seamlessly mix-and-match between GUI, code, and AI interactions. In a user study, participants seamlessly alternated modalities, with the GUI used for straightforward visual changes, code for quick edits or duplicating code, and the AI for broad support. Plottery showcases graphical interaction that retains code's benefits.

---


### 56. [ConicFlow: constrained Inference-time optimal control for flow matching models](https://arxiv.org/abs/2610.14307)

**<font color=#1a73e8>作者：</font>** Shervin Khalafi, Kasra Fallah, Sung Cho 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose ConicFlow, which frames constrained sampling from a flow matching model at inference time as an optimal control problem that balances deviation from the pretrained trajectory against reward, subject to hard terminal constraints. We discretize this problem and adapt receding-horizon control, optimizing only a short window of the trajectory at each step for computational tractability. We address the resulting sequence of receding-horizon subproblems with a receding-horizon primal-dual algorithm. Its dual multipliers capture the difficulty of satisfying each constraint and are refined throughout sampling, steering generation toward feasible final samples. We further propose a terminal-estimate variant that avoids accumulating local truncation errors by evaluating the reward and constraints at the predicted terminal point rather than at the end of the current horizon. Under standard regularity assumptions, we establish finite-horizon guarantees on suboptimality. Under convex-affine structure, we derive a sharper bound that scales linearly with omitted horizon length, and we show that the terminal-estimate variant is provably tighter when the flow dynamics change slowly. Experiments in both low- and high-dimensional settings with a recent large-scale flow matching model show that ConicFlow achieves high reward and strong constraint satisfaction while deviating less from the pretrained flow than recent baselines.

---


### 57. [MvFFN: Multi-view Floor plan Feed-forward Network for Unposed Wide-Baseline Panorama Layout Reconstruction](https://arxiv.org/abs/2610.14315)

**<font color=#1a73e8>作者：</font>** Yuguang Li, Yichuan Deng, Zixuan Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing accurate camera poses and floor-plan layouts from sparse, unposed, wide-baseline RGB panoramas remains a challenging open problem. Direct multi-room floor-plan prediction is especially difficult in this setting: pose, geometry, semantics, and global layout structure are tightly coupled, yet a complete floor-plan is hard to learn as a single global output. Our key insight is to keep the model's predictions strictly local. Multi-view Ordered Wall Instance Segmentation (MOIS) is designed around this concept. Each panorama column predicts only the wall it observes plus the next two adjacent walls in clockwise order. The global wall partition, room layouts, and shared coordinates emerge from deterministic aggregation of overlapping local predictions. Building on MOIS, we propose Multi-view floor-plan Feed-Forward Network (MvFFN), which jointly predicts coarse camera poses, dense global geometry, and per-wall semantic outputs. A downstream Layout Chaining (LC) post processing pipeline then assembles these predictions into multi-room floor-plans with shared global coordinates, consistent wall identities, and connected room structure. The dense MOIS predictions recover cross-view wall identity and local within-room connectivity more accurately than composed modular baselines, and the assembled layouts substantially outperform prior methods on wall and junction level accuracy. We also introduce the ZInD-CrossView dataset, which augments ZInD with globally unique wall instances and cross-view segmentation labels for this task.

---


### 58. [EV-JEPA: Elastic V-JEPA for Any Device and Cross-Device Inference](https://arxiv.org/abs/2610.14324)

**<font color=#1a73e8>作者：</font>** Anxhelo Diko, Jieyu Lin, Stefano Ambrogio 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models like V-JEPA are increasingly deployed across a heterogeneous edge-cloud continuum spanning smart glasses, phones, robots, and servers. Yet, they are typically trained as rigid, fixed-capacity networks bound to one device, supporting neither reconfigurable compute budgets nor collaborative execution. Existing approaches address only one axis at a time: slimmable and NAS-based methods provide width elasticity but assume single-device inference, whereas split-computing methods enable cross-device collaboration only for fixed partitions and static capacities. We introduce Elastic V-JEPA (EV-JEPA), a single model trained once and deployable everywhere along the continuum. Its width is reconfigurable, and it is natively partitionable across heterogeneous devices. At its core is Transition-Aware Triplet Training (T3). At each step we pick a narrow and a wide width, and train three paths: each width alone, plus a hybrid path that runs the early layers narrow and the rest wide. The hybrid switch point is where one device hands off to another, so the same weights learn both single-device and cross-device execution. Across various benchmarks, EV-JEPA falls within 1 accuracy point of independently trained baselines while improving over previous elastic training approaches by up to 11 accuracy points. Narrow-to-wide cross-device hybrid execution recovers to within 1.1 points of the highest-capacity standalone model and supports many-to-one, any-to-any, and variable-split configurations. Finally, we show that the elastic principle extends beyond the backbone to an elastic token compression mechanism that exposes controllable trade-offs among on-device computation, latency, and accuracy.

---


### 59. [Manifold Navigation Learning Using Recurrent Networks: Efficient Training Techniques](https://arxiv.org/abs/2610.14325)

**<font color=#1a73e8>作者：</font>** Sarah Harkins Dayton, Sathya Rengaswami, Vasileios Maroulas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Position tracking is a well-studied problem in Euclidean navigation, yet comparatively little attention has been given to navigation on general manifolds, where motion is governed by the underlying geometry of the space. In this work, we formalize the problem of manifold navigation as a velocity-driven tracking task and propose a coordinate-chart-based learning framework in which learning models operate entirely in a Euclidean representation. Predicted trajectories are mapped to the manifold via an immersion function prior to error computation, allowing geometric consistency to be evaluated without explicitly enforcing manifold constraints during learning. Within this framework, we focus on Gated Recurrent Units (GRUs) for sequential position prediction on curved manifolds after comparisons with alternative recurrent architectures. We evaluate our GRU models, trained with pertinent custom loss functions, against both a standard MSE loss function and a naive vector-addition baseline. We evaluate our approach on both analytically (and numerically) defined manifolds, as well as a surface reconstructed from a LiDAR point cloud. Our results show that recurrent models can learn to approximate manifold-constrained dynamics from velocity sequences and consistently outperform Euclidean baselines. Our results demonstrate that certain custom loss functions significantly improve long-horizon prediction accuracy compared to conventional point-wise loss functions.

---


### 60. [Real-Time Traffic Density Estimation: A Hybrid Computer Vision and Predictive Machine Learning Pipeline](https://arxiv.org/abs/2610.14326)

**<font color=#1a73e8>作者：</font>** Prince Kwabena Appiah Boadu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic density estimation from camera feeds requires connecting visual perception with short-horizon forecasting. We present a two-stage pipeline that combines vehicle detection and tracking with a spatial logic layer, followed by a temporal estimator. The spatial layer filters bounding boxes by their overlap with a precomputed road mask and extracts per-frame traffic features. LSTM, GRU, and Temporal Convolutional Network (TCN) estimators use these features to predict five future steps from a ten-frame input window. We benchmark ten detector variants from six families on a dataset of 5,716 annotated frames using a single NVIDIA GPU. YOLOv5l achieves the highest mAP@50:95 of 0.524 at 56 frames per second, while YOLOv8n reaches 258 frames per second at 0.487 mAP@50:95; these rates measure detector inference without tracking or spatial filtering. Temporal evaluation on 29,243 held-out windows yields aggregate R-squared values of 0.858 for GRU, 0.856 for LSTM, and 0.840 for TCN. These metrics measure forecasts of detector-derived telemetry and are dominated by direction variance, rather than establishing absolute traffic-density accuracy. No road mask was available for the evaluation stream, limiting validation of the spatial filtering component. A live run on a third camera stream examines forecasting behavior within the complete pipeline. The results characterize detector speed-accuracy trade-offs and the limitations of short-window traffic telemetry forecasting.

---


### 61. [TraceSampler: Making Sampling Errors Predictable and Correctable for Accelerated Generative Sampling](https://arxiv.org/abs/2610.14332)

**<font color=#1a73e8>作者：</font>** George Matthew, Guoqiang Zhang, Kenta Niwa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate sampling from continuous-time generative models can require many model evaluations. Low-step sampling reduces cost, but coarse updates introduce endpoint errors that can accumulate and degrade generation quality. We introduce TraceSampler, a post-training method that corrects these errors without modifying the pretrained model. Rather than optimising low-step updates directly, TraceSampler models endpoint error as a sample-specific prediction problem. A higher-step reference integration over the same interval provides the supervised target, while a compact representation makes high-dimensional error predictable from the sampling trace. This representation combines shared residual structure, trace-derived directions, and a low-rank remainder, so shallow per-step MLP heads predict sample-dependent coefficients. These coefficients drive a two-stage learned residual correction: the first stage predicts the full endpoint residual, while an intermediate backbone evaluation provides new trace information to predict the remaining residual; this evaluation is reused by the following step. TraceSampler is evaluated with Rectified Flow on CIFAR-10, SiT-XL/2 on ImageNet-256, and SD3.5 Medium for text-to-image generation. At 10 steps, it reduces trajectory MSE relative to matched-step Euler by 90.5% on CIFAR-10 and 85.6% on ImageNet-256, while achieving FID scores of 2.692 and 2.189, close to 120-step Heun references of 2.601 and 2.056 with 24$\times$ fewer backbone evaluations. On SD3.5 Medium, TraceSampler improves image quality and prompt following; at 10 steps, ImageReward rises from 0.752 to 0.906 while trajectory MSE falls by 70.7%. These gains preserve Euler's backbone-evaluation budget, add less than 0.4% inference FLOPs, and incur negligible wall-clock overhead, showing that coarse-step sampling error can be made predictable from the sampling trace and efficiently corrected.

---


### 62. [Decentralized Bandit Learning of Markov Perfect Equilibria](https://arxiv.org/abs/2610.14333)

**<font color=#1a73e8>作者：</font>** Felix Höfer, H. Mete Soner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study decentralized bandit learning in discounted infinite-horizon, general-sum Markov games with continuous actions. Agents observe the public state, but only their own realized rewards, and use simultaneous perturbation stochastic approximation to update their actions. Under strong monotonicity of the negative running-reward gradients and sufficiently small time steps, we prove that the fully decentralized procedure converges almost surely to the unique stationary Markov perfect equilibrium. We obtain an $O(n^{-1/2})$ convergence rate and present a natural extension to episodic finite-horizon learning.

---


### 63. [Continuous-Time Cloth Dynamics with Physics-Informed Neural ODEs](https://arxiv.org/abs/2610.14342)

**<font color=#1a73e8>作者：</font>** Yingdong Ru, Lipeng Zhuang, Zhuo He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present ContinuousCloth, a continuous-time, physics-informed neural solver for deformable cloth dynamics that enforces a spring--mass ODE within a neural trajectory model. Unlike classical time-stepping simulators that return trajectories only on a discrete integration grid, ContinuousCloth supports querying at arbitrary timestamps and computing displacement, velocity, and acceleration via automatic differentiation. We evaluate ContinuousCloth along two dimensions. In a physics-only setting, ContinuousCloth achieves trajectory accuracy comparable to high-precision solvers across six diverse boundary-condition scenarios while reducing runtime by up to 17.4 times. When fused with sparse and noisy observations, the spring--mass ODE acts as a strong inductive bias for downstream tasks: interpolation and parameter estimation. That is, ContinuousCloth reduces interpolation error by 7.3 times over a data-only neural baseline in simulation and 2.4 times on real-world cloth sequences, and achieves 2.6 times lower parameter error than a differentiable-solver baseline under high-noise conditions, demonstrating consistent robustness under realistic measurement imperfections.

---


### 64. [Multimodal Co-Generation With Continuous Bitstream Diffusion](https://arxiv.org/abs/2610.14349)

**<font color=#1a73e8>作者：</font>** Georgios Batzolis, Georgios Kontos, Bruno Trentini 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We show that continuous bitstream diffusion (CoBit), originally developed for language modeling, provides a unified framework for joint and conditional multimodal generation using the same training and sampling protocol. Across image-text, speech-text and protein sequence-structure modeling, models are trained separately from scratch, but each uses a single input projection, transformer backbone, bitwise prediction head and binary score-matching objective shared across its modalities. Within each setting, a single checkpoint supports joint generation and the conditional directions included in training by changing which parts of the bitstream are observed. We first validate the approach on MNIST-Sum, a controlled image-text task pairing raw binary images with equations encoded as text, achieving near-perfect conditional accuracy and high joint consistency without learned tokenizers. We then apply the same protocol at larger scale to speech-text and protein sequence-structure modeling. Trained without text pretraining, a single speech-text model performs speech synthesis, recognition, continuation, and unconditional co-generation. Jointly generated speech and text achieve 3.5% word error rate between the generated text and automatic transcriptions of the generated speech. In protein modeling, a single CoBit checkpoint supports forward folding, inverse folding, and joint sequence-structure generation. For jointly generated proteins spanning 100-500 residues, computational refolding of CoBit's sequences yields structures that agree with the generated backbones at a mean self-consistency TM-score of 0.911. Together, these results show that CoBit provides a common generative framework for substantially different modalities and forms of cross-modal dependence, without introducing a domain-specific objective or sampling procedure.

---


### 65. [Learning Transferable World-Action Models from Task-Paired Human Videos](https://arxiv.org/abs/2610.14351)

**<font color=#1a73e8>作者：</font>** Jeongeun Park, Taekyung Kim, Dongyoon Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-action models inherit broad visual and physical priors from video pre-training. However, standard within-video next-frame prediction allows them to rely on appearance shared between the context and future, rather than learning interactions that transfer across scenes and embodiments. We introduce WATCH, a cross-video pre-training that learns from task-paired human demonstrations collected across diverse environments. Conditioned on the video and actions of one demonstration, the model jointly predicts another demonstration's actions and future frames from its current observation. Predicting one demonstration from another encourages the model to learn task-relevant interactions that transfer across scenes and demonstrators. Our pre-training shows that these capabilities can be learned from readily scalable human-human pairs alone, without requiring matched human-robot demonstrations. Analyses before robot post-training show improved motion alignment across embodiments and better action and video prediction on unseen robots, with representations closer to those learned from robot pairs. After robot post-training, WATCH improves MimicDroid in-context success from 40.9% to 68.3% with Cosmos Policy and from 59.8% to 77.7% with Cosmos3, with the largest gains on the unseen levels. Gains persist under context-free post-training across robot embodiments. WATCH outperforms within-video pre-training and co-training baselines, supporting cross-video prediction as a scalable approach to learning transferable world-action representations.

---


### 66. [Class-Conditional Conformal Prediction for Signal Temporal Logic Inference with Many Classes](https://arxiv.org/abs/2610.14352)

**<font color=#1a73e8>作者：</font>** Yixuan Wang, Danyang Li, Matthew Cleaveland 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Signal Temporal Logic (STL) inference provides interpretable formulas for time series classification. For multiclass classification, however, accurate predictions do not necessarily ensure that the inferred formulas are satisfied consistently with the true class. We introduce the positive satisfaction rate and codeword satisfaction rate to quantify satisfaction of required formulas and consistency with the complete class codeword, respectively. We develop a two-stage procedure that first learns discriminative formulas using a margin-based objective and then refines predicate thresholds toward a small positive robustness target while fixing the formula structure and temporal intervals. Satisfaction and ranking penalties discourage violations of required formulas and loss of class separation. The decoding loss is used as a nonconformity score and calibrated separately for each class, providing finite-sample class-conditional coverage under intra-class exchangeability. Experiments on naval, synthetic, and robot manipulation trajectories demonstrate discrepancies between classification accuracy and formula satisfaction. The results further reveal a data-dependent tradeoff between robustness tightness and satisfaction, while class-conditional calibration mitigates undercoverage that can be hidden by pooled calibration.

---


### 67. [Actionable Meta-Requirements for AI Robustness Auditing](https://arxiv.org/abs/2610.14356)

**<font color=#1a73e8>作者：</font>** Joshua Owotogbe, Roya Nasiri, Indika Kumara 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-enabled systems must remain dependable when the conditions under which they operate change (e.g., due to input perturbations, distribution shifts, or changes in external dependencies). This makes robustness auditing of such systems important for judging whether the available evidence is sufficient to support a defined robustness conclusion. However, designing an AI robustness auditing framework is challenging. A key unresolved issue is determining the requirements such a framework should support; these requirements have not yet been consolidated. We address this gap through meta-requirements: higher-order requirements specifying what a class of auditing frameworks should support. In design science research, literature and domain experts are common sources of meta-requirements; accordingly, we derive the initial set from literature and validate and refine it with practitioners. Our systematic literature review retained 74 of 2,890 records and derived 43 meta-requirements across 16 categories. We evaluated them with 128 practitioners, obtaining 5,504 ratings and 586 substantive comments. Overall, 81.20% of ratings indicated agreement or strong agreement. In particular, 41 of the 43 literature-derived meta-requirements were classified as strongly supported. Practitioner feedback refined the requirements and identified an additional requirement concerning external components and supply chain dependencies. The final set comprises 44 meta-requirements across 16 categories, of which 43 received quantitative validation. These meta-requirements can help organizations implement AI robustness auditing frameworks, assess existing frameworks for completeness, and refine them.

---


### 68. [The Sample Complexity of Multicalibration with an ERM Oracle](https://arxiv.org/abs/2610.14363)

**<font color=#1a73e8>作者：</font>** Princewill Okoroafor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A predictor is multicalibrated with respect to a class of subpopulations (formally, of functions on the inputs, called auditors) if, for every subpopulation in the class and every value the predictor outputs, the average outcome among the members of that subpopulation who receive that value is close to the value itself. For finite classes, about $\varepsilon^{-3}$ samples are necessary and sufficient to learn a predictor with multicalibration error $\varepsilon$, but the algorithms that attain this rate enumerate the class, which is impossible for the large classes of interest. We ask how many samples suffice when the learner accesses the class only through an empirical risk minimization (ERM) oracle. We give an algorithm that uses $\tilde{O}(d/\varepsilon^{3})$ samples and polynomially many ERM calls, where $d$ is the VC dimension of the class. Its dependence on $\varepsilon$ is optimal for all learners. When $d$ is at least about $1/\varepsilon$, every learner that can only access the class through polynomially many ERM calls needs $\tilde{\Omega}(d/\varepsilon^{3})$ samples. Learners with unlimited computation need only $\tilde{O}(\varepsilon^{-3}+d\varepsilon^{-2})$ samples, so the extra factor $1/\varepsilon$ on the dimension term is the price of oracle efficiency. For swap multicalibration, which allows a different function from the class for each predicted value, $\tilde{\Theta}(d/\varepsilon^{3})$ samples are necessary and sufficient. For estimating the error of a given predictor, the ordinary notion is the harder one: the swap error can be estimated with an ERM oracle, whereas the ordinary error is NP-hard to approximate even for classes with linear-time ERM. Consequently, there are classes for which it is computationally easier to learn a multicalibrated predictor than to compute the multicalibration error of a given predictor.

---


### 69. [History, Adaptation, and Hidden Gain: Two Prospective Tests of Learned Predictive Control in a Synthetic Neural Population](https://arxiv.org/abs/2610.14368)

**<font color=#1a73e8>作者：</font>** Mahesh Reddy Pagadala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study learned one-step predictive control of a synthetic population of 64 leaky integrate-and-fire neurons whose light sensitivity is scaled by a hidden factor s, using two prospective confirmations on plants simulated only after the analysis was frozen. In the first (50 plants, 11 conditions), removing the 200-ms input-output history substantially worsened a parameter-count-matched neural predictor at low and moderate gain (s = 0.6, 0.8; RMSE rose by 2.47 Hz at s = 0.6, 97.5% CI 2.43-2.51). In secondary comparisons, recursively adapted ARX had the lowest mean error of the deployable controllers in 10 of 11 conditions, tuned PI with anti-windup matched or beat the network for s >= 0.7, and training for 10,000 rather than 900 epochs lowered prediction error but worsened control. Development work suggested the network's learned action sensitivity did not track the hidden gain. A second protocol (50 new plants, 9 sensitivities, 2 noise levels) confirmed three pre-specified predictions at the primary noise level. Re-estimating a single multiplicative input gain recovered 87% (95% CI 86-88%) of the benefit of full adaptive ARX. Supplying that online estimate to the network as an extra input reduced high-gain tracking error by 1.84 Hz [1.81, 1.88]. Longer training worsened the plain network by 1.09 Hz but improved the gain-input network by 1.07 Hz, a differential of 2.16 Hz [2.13, 2.20]. Under high process noise (sigma = 2.0) the effects shrank to about 0.04 Hz or less and gain-only adaptation recovered only 24% of the adaptive-ARX benefit. In this synthetic plant, at the primary noise level, one-parameter online gain estimation accounts for most of the gap between a history-based network and full adaptive ARX, and for its prediction-control mismatch.

---


### 70. [When More Memory Fails: Hidden Feasibility Holes in Dynamic Tensor Rematerialization](https://arxiv.org/abs/2610.14369)

**<font color=#1a73e8>作者：</font>** Mahesh Reddy Pagadala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic Tensor Rematerialization (DTR) trains neural networks under a memory budget by evicting tensors and recomputing them on demand. A natural expectation is that a budget large enough to complete training stays sufficient when it is increased. Using DTR's reference simulator, simrd, to replay the public DTR training traces, we show that this expectation fails. We call the exceptions feasibility holes: memory budgets at which an eviction policy runs out of memory although both a smaller and a larger budget complete, a form of non-monotone feasibility. Under a written sweep protocol with dated amendments, a 0.01-step budget grid shows no such hole for DTR on any of six confirmatory traces, although unresolved timeouts prevent it from establishing monotonicity. Finer sampling finds holes on InceptionV4 (three regions) and U-Net (two regions), in addition to one on the ResNet-32 development trace. Every hole is reproduced by three repeats and by unmodified simrd. For one InceptionV4 pair (0.2343 versus 0.235 of peak memory) we trace the failure to individual allocations. The larger budget avoids one eviction at an operator where the smaller budget was 173,479 bytes short. The extra data it carries forward forces a later eviction of a tensor needed three operators afterwards, and rebuilding that tensor triggers a recomputation cascade that cannot fit. Keeping that one tensor resident under the same budget prevents the failure. The two simple score changes we tested do not remove holes across traces; both add failing budgets on some traces. All results are from simulation, with no allocator model; behaviour on GPU hardware is untested.

---


### 71. [DPAL: A Test-Time Adaptation Loss for Financial Time Series Forecasting](https://arxiv.org/abs/2610.14376)

**<font color=#1a73e8>作者：</font>** Wuzhou Lian, Haochun Wang, Yuefan Deng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) enables time series forecasters to update after deployment as new observations become available. However, adaptation objectives that focus primarily on prediction errors at individual time steps do not fully address the needs of financial time series forecasting. In addition to pointwise return fitting, return direction and the price trajectories reconstructed from sequences of returns are also important. To better account for these properties, we introduce Direction- and Price-Aware Adaptation Loss (DPAL), which combines pointwise return fitting with directional and price-calibration terms. We apply DPAL within existing TSF-TTA frameworks without modifying the source forecaster or the adapter architecture. Across a diverse collection of financial datasets, DPAL reduces reconstructed-price mean squared error in most evaluated settings.

---


### 72. [Clinical value claims in multimodal AI outpace supporting evidence](https://arxiv.org/abs/2610.14395)

**<font color=#1a73e8>作者：</font>** Jiayu Feng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal prediction models add a data source, such as imaging or an assay, to clinical information, and health systems must decide whether that added test is worth acquiring. We audited 177 studies comparing multimodal with unimodal models: 81 from a systematic review and 96 from a probability sample of 2025-2026 PubMed records. Gains in the area under the receiver operating characteristic curve (AUROC) were smaller when a study fitted a separate model for every data source (adjusted difference, -0.030; 95% CI, -0.056 to -0.005). Within 78 such studies, leaving out the strongest source's model would have raised the average gain from 0.046 to 0.108. This complete benchmarking fell from 69.1% of review studies to an estimated 46.0% of recent ones. An estimated 22% assessed decision utility and none evaluated a model prospectively, yet most claimed potential clinical usefulness or improved care (84.0% and an estimated 87.7%).

---


### 73. [Sparse-TD-JEPA: Improving Zero-Shot Reinforcement Learning With Sparse Latent Task Representations](https://arxiv.org/abs/2610.14400)

**<font color=#1a73e8>作者：</font>** Duaa Nakshbandi, Zhiyu An, Wan Du  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Successor-feature-based zero-shot reinforcement learning methods pre-train a task encoder and successor-feature predictor on offline, reward-free data, then recover a policy at test time by solving a closed-form linear regression over a small labeled dataset. We identify an underexplored limitation of this approach: when the task encoder produces dense representations, the inferred reward signal becomes diffuse across the state space, reducing the contrast between goal-relevant states and the background and providing a weaker signal for the policy to follow. We address this limitation by introducing an l1 sparsity penalty that concentrates reward-predictive structure into a smaller effective subspace of the task encoder's latent space. The penalty is applied only during training and requires no architectural change or modification to the closed-form inference procedure. We instantiate this approach as Sparse-TD-JEPA, a single-line of code addition based on Temporal-Difference Joint-Embedding Predictive Architecture (TD-JEPA) that significantly improved its performance in zero-shot reinforcement learning. We evaluate Sparse-TD-JEPA on 65 tasks across the DeepMind Control (DMC) Suite and OGBench, covering locomotion, navigation, trajectory stitching, puzzle solving, and robotic manipulation. Sparse-TD-JEPA improves over TD-JEPA in all 13 domain-level comparisons. On DMC, it increases the average return from 661 +- 6 to 714 +- 3. On OGBench, it increases the average success rate from 38.0 +- 0.8 to 48.4 +- 2.3, with improvements of 13.4-18.0 percentage points on the evaluated antmaze navigation and stitching domains. Overall, Sparse-TD-JEPA achieves the highest mean performance among established zero-shot baselines in nine of the 13 domains. Analysis further shows that sparsity produces a sharper and more task-informative inferred reward landscape.

---


### 74. [DICE: Tilting the Odds through Interface Attackson System One Model](https://arxiv.org/abs/2610.14404)

**<font color=#1a73e8>作者：</font>** Ben Dong, Tianyi Lu, Zhonghao Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> System One models offer typed judgments that applications can turn into decisions. Their answers, however, are conditional on the state and question supplied by surrounding components, and on how the application uses the response. We study this boundary in a Jev-based pipeline with bounded substitutions at three adapter outputs: state extraction, question generation, and output interpretation. Across three small synthetic studies, each adapter can change the final decision while Jev and its authentic API responses remain outside attacker control. The cases expose distinct failures of source fidelity, answer meaning, and response relevance. Checks that bind these relationships stopped the corresponding interventions we tested, although source verification also rejected some valid clean decisions. The pilot identifies where correct request-level judgments can lose their connection to the original task; it does not estimate the prevalence of these failures in deployed systems.

---


### 75. [PotentialEP: Backprop-Free Training of CIFAR-Scale Generative Models via Equilibrium Propagation](https://arxiv.org/abs/2610.14409)

**<font color=#1a73e8>作者：</font>** Alex Gower  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating an image with a diffusion or flow-matching model typically involves integrating a velocity field for hundreds of sequential steps. That computation suits a GPU poorly and an analog neuromorphic substrate well, where one fast, low-power physical relaxation could replace the whole sequence. Two things are needed: a generative algorithm whose computation is a relaxation, and a way to train it without backpropagation, whose global gradient transport is hard to realise in analog. Energy Matching supplies the first, sampling by gradient-descent relaxation on a time-independent potential - but obtaining the gradient that descent follows is itself a backward pass, once per integration step. We prove that a predictive coding network with a single linear injection term added to its energy relaxes to a state whose visible layer carries that gradient inherently, with an error that vanishes for small injection strengths. An Energy Matching model trained by backpropagation can therefore be loaded into this network unchanged and sampled by relaxation alone, matching the original model's FID to within 0.04 at CIFAR-10 and ImageNet-32 scale. The network can also be trained without backpropagation: Equilibrium Propagation reproduces backpropagation's parameter updates to a cosine similarity of 0.9998, and training end to end with those updates reaches an FID of 3.64 on unconditional CIFAR-10 against 3.54 for backpropagation. To our knowledge this is the first CIFAR-10 generative model trained with Equilibrium Propagation, and the first at competitive quality by any backpropagation-free rule. This quality does not require group normalisation or attention: an architecture of only convolutions and pointwise nonlinearities, both native to an analog crossbar, reaches an FID of 3.51 when trained by backpropagation.

---


### 76. [Design Choices for Multimodal Transformer Learning with Missing and Longitudinal Healthcare Data](https://arxiv.org/abs/2610.14436)

**<font color=#1a73e8>作者：</font>** Rita Cordeiro Mendes, Maria Manuel Pereira, Carlos Santiago 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal learning offers the potential to improve predictions by integrating complementary information from heterogeneous data sources. However, multimodal datasets are frequently incomplete, raising important questions about how models should handle missing information. Although recent approaches increasingly rely on Transformer-based architectures for multimodal fusion, incomplete multimodal data introduces challenges such as missing modalities and intra-modal missingness, which motivate key architectural design choices, such as tokenization granularity. In addition, many datasets are longitudinal, with observations collected across multiple time points. The sequential nature of the Transformer architectures provides a natural framework for modeling such data, but introduces additional considerations, such as how temporal information should be represented. In this study, we systematically investigate these design choices using three different cancer datasets. We compare modality-level and feature-level tokenization and evaluate attention masking and imputation as strategies for handling missing information, both naturally occurring in the datasets and synthetically induced. We further investigate approaches for incorporating temporal information in our training process and how to model it. Experiments are conducted with unimodal and multimodal configurations, as well as different levels of missingness for binary survival classification and multiple time encoding strategies for discrete-time survival prediction. Our results show that while multimodal outperforms unimodal results, missing data heavily impacts predictions and thus effective design choices such as tokenization granularity, and intra-missing handling is essential for reliable prediction.

---


### 77. [From Transfer Probes to Expert Grouping: Evidence from LoRA Post-Training](https://arxiv.org/abs/2610.14437)

**<font color=#1a73e8>作者：</font>** Xueyang Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A platform that post-trains one base model for many business lines often has more lines than experts it can maintain, so lines must share experts, yet lines seldom come with a taxonomy saying which should share. We ask whether transfer probes (train on one source, measure paired changes on all sources) can discover a grouping when the standard one is unknown. To test probes against a reference, we use seven public sources that do have a label tree (five mathematics subfields and two kinds of programming, standing in for business lines) and treat the tree's grouping as a label reference that the evaluator holds and the method does not. With four LoRA experts under fixed per-source exposure and per-expert budgets, we compare a purely probe-derived grouping and an uninformed uniform default (whose tied routing serves every line from one expert) against this reference. Trained once for one interval from a shared warm-up state and routed by a rule fixed by each allocation, neither reached the prespecified practical gain of 2 percentage points, and both had lower overall utility than the reference ($-2.43$ and $-2.54$ pp; 95\% intervals below zero). In a post hoc comparison, the probe-derived grouping was indistinguishable from the uniform default ($+0.11$ pp, $[-1.25,+1.54]$). In fixed-budget LoRA post-training, a grouping built from initial-state single-source probes thus did not deliver the advantage predicted from the probes once carried to a later training state, a finite budget, and specified routing.

---


### 78. [FreeCHROMA: Generative Chroma Keying from Unaligned Background References](https://arxiv.org/abs/2610.14445)

**<font color=#1a73e8>作者：</font>** Jiayi Wu, Tianfu Wang, Rui Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In film production, chroma keying composites an approved foreground performance into a new environment, but conventional workflows require coordinated background plates and dedicated harmonization. Recent generative methods often require pre-aligned backgrounds, focus on background-conditioned foreground relighting, or represent the environment only through an edited first frame. These restrictions limit background selection, scene composition, and camera motion while adding preparation or editing effort. We present FreeCHROMA, which adapts a pretrained video diffusion model in a parameter-efficient manner for generative video compositing from one to three unaligned background references. The model integrates the foreground into the referenced environment, preserving foreground identity, motion, and fine visual details while generating a spatiotemporally coherent background. Foreground-background harmonization occurs within the same generation process, without a separate relighting stage. Optional text instructions help disambiguate complex spatial relationships and camera behavior. To train the model, we construct pseudo-paired data from readily available real monocular videos through foreground-background separation and augmentation with existing foundation models. The original videos serve as training targets, while automated processing and quality verification enable scalable data construction. Across reference fidelity, foreground preservation, scene integration, harmonization, and overall video quality, FreeCHROMA consistently outperforms recent compositing and conditional video-generation baselines, with particularly clear gains under camera motion. FreeCHROMA relaxes the constraints of existing tools to enable end-to-end generative chroma keying from unaligned inputs, with exploratory experiments demonstrating its potential in robotics.

---


### 79. [Jevolution: A Framework for Studying Communication and Collective Dynamics in AI Agents](https://arxiv.org/abs/2610.14449)

**<font color=#1a73e8>作者：</font>** Xirui Huang, Nikhil Hooda, Utkarsh Gupta  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Experiments with remote decision-making agents depend on more than the policy: the world may change during inference, the simulator determines which actions are available, and births and immigration alter who can act. We present Jevolution, an instrumented spatial predator-prey framework that makes these dependencies explicit. Its reference implementation separates the evolving world, asynchronous request scheduling, controller adapters, and experiment records. The model combines local observations, energy and resource constraints, predefined signals, and inherited scalar traits. We describe these mechanisms using the ODD protocol and distinguish implemented controls from research questions requiring additional interventions. Free synthetic fixtures exercise scheduling, signaling, and inheritance against the pinned implementation; they validate specified software behavior rather than model intelligence or ecological realism. A completed communication case study illustrates the end-to-end workflow using Jev to control both species. Across 6 complete habitat-seed pairs, the mean signals-on minus signals-off difference in normalized rabbit abundance was -0.0095 (nominal 95% pair-bootstrap interval [-0.0772, 0.0602]). This small study does not resolve the direction of the signal-system effect. The contribution is an inspectable experimental system and its evidence boundaries, not a new policy-learning algorithm or a demonstration of emergent language, adaptive selection, or biological predictive validity.

---


### 80. [Learning to Extrapolate in Depth with Looped Transformers](https://arxiv.org/abs/2610.14456)

**<font color=#1a73e8>作者：</font>** Huitao Yang, Jianhao Huang, Zixuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers reuse a single block across iterations, raising a natural question: how far can a block trained at one depth be safely extrapolated to greater depths? We study this question for all-pairs graph connectivity, where harder graphs require longer-range information propagation. We show that under exchangeability and symmetric positive initialization, population training at depth K converges to an update rule governed by a single effective parameter that balances graph propagation against fitting structure unresolved at training depth. This trade-off creates a finite extrapolation window: too few test-time loops provide insufficient propagation, while too many eventually create false connections. We derive explicit endpoints for this window and bound the graph hardness solvable beyond training as a function of training depth and hardness. In particular, a test depth chosen solely from the training distribution can guarantee recovery on substantially harder graphs, with a certified depth gain that grows exponentially as training depth outpaces training hardness. Experiments validate the predicted windows and show how compute budget and initialization affect the optimal training depth.

---


### 81. [AphaVoice: Text-to-Speech Model for Aphasia Patient Simulation](https://arxiv.org/abs/2610.14479)

**<font color=#1a73e8>作者：</font>** Al Varrel Putra Kusuma, Fernando Bello, Joshua Brown  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While language therapy is the primary treatment for post-stroke aphasia, limited clinical resources often restrict patient access to proper care. Addressing this gap requires reliable training simulations for medical professionals. However, current AI efforts focus almost exclusively on speech processing, leaving speech generation largely unexplored. This study introduces AphaVoice, a novel text-to-speech (TTS) framework explicitly engineered to synthesize highly realistic aphasic speech. Evaluated against state-of-the-art TTS systems, AphaVoice demonstrates a superior ability to capture the clinical feature of dysfluency, outperforming existing models in temporal metrics while consistently maintaining speaker identity. By leveraging latent space shifting, the model also supports multi-speaker generation without sacrificing phonetic realism. Ultimately, AphaVoice provides a scalable, high-fidelity tool for medical training and clinical simulation related to aphasia.

---


### 82. [AlignPoison: Conditional Targeted Poisoning of Generative Recommenders via Decoding-Aligned Prefixes](https://arxiv.org/abs/2610.14487)

**<font color=#1a73e8>作者：</font>** Zhuoxuan Zhang, Jinhao Duan, Xinyu Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative recommendation models based on autoregressive decoding have been adopted as alternatives to classical ranking-based systems. While their modeling flexibility has been widely studied, their resilience to data poisoning remains largely unexplored. In this work, we ask: how susceptible are generative recommenders to conditional targeted poisoning? Under a realistic setting where an adversary can inject limited malicious interactions and query a recommendation API as a black box, our empirical study shows that generative recommenders are vulnerable: injecting fewer than 1% synthetic interactions significantly increases the likelihood of promoting malicious targets under the trigger. To characterize this vulnerability, we analyze the synthesis of malicious interactions from two perspectives: (i) decoding alignment and (ii) prefix popularity. We observe that short, context-aligned prefixes that are both common under the model's induced transition dynamics and strongly linked to a frequent trigger consistently amplify targeted promotion. Motivated by this analysis, we develop AlignPoison, a black-box framework that discovers and samples context-aligned prefixes from API outputs. We conduct experiments on benchmarks in unimodal and multimodal generative recommendation settings. Results show that these prefixes outperform competitive baselines, improving ASR lift by up to 16.3 percentage points and highlighting a decoding-dependent, context-sensitive poisoning vulnerability in generative recommendation models.

---


### 83. [HiPPT: Physiology-Grounded Wearable PPG Representation Learning via Multi-Scope Text Alignment](https://arxiv.org/abs/2610.14489)

**<font color=#1a73e8>作者：</font>** Jiaqi Wang, Wei Chen, Xiaoyu Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reusable wearable PPG representations should capture local pulse morphology and broader physiological regularities. Existing pretraining objectives, however, usually apply supervision at the recording or pair level, overlooking that different concepts become reliable over different scopes of waveform evidence. We propose HiPPT, a physiology-grounded framework that matches each supervision source to its appropriate evidence scope. We construct a PPG-Text corpus of over 4 million wrist-worn recordings from 202K users, pairing recordings with waveform-derived morphology and metadata-derived context descriptions. HiPPT combines record-level morphology alignment, which grounds individual recordings in pulse characteristics, with cross-recording context alignment, which aggregates recordings sharing the same metadata tuple to capture context-consistent regularities. Waveform-guided text modeling further recovers masked contextual concepts from PPG patch representations, providing fine-grained waveform-text supervision. Across six downstream tasks spanning blood pressure, vascular stiffness, physiological attributes, and cross-dataset heart-rate estimation, HiPPT achieves the best result on the primary linear-probing metrics. The aligned space also supports zero-shot profiling of age group, sex, and BMI category, individually and jointly, with performance improving as more recordings are aggregated. These results show that evidence-scope matching yields transferable and semantically accessible wearable PPG representations. Code and pretrained weights will be released.

---


### 84. [A Gated Catchment Hydrology Model (GCHM) for Physically-Interpretable Rainfall-Evapotranspiration-Runoff Simulation Across Diverse Hydroclimatic Regimes](https://arxiv.org/abs/2610.14493)

**<font color=#1a73e8>作者：</font>** M Jawad, HV Gupta, MA Farmani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in machine learning have improved rainfall-runoff prediction, yet most data-driven models remain difficult to interpret and do not explicitly enforce physical conservation laws. We present the Gated Catchment Hydrology Model (GCHM), a mass-conserving architecture based on the Mass-Conserving Perceptron (MCP). GCHM uses five storage states representing canopy interception, snow, soil moisture, groundwater, and streamflow generation. Constrained gates govern precipitation partitioning, evapotranspiration, infiltration, seepage, runoff, and baseflow while learning context-dependent process relationships.
We evaluate GCHM across 50 CAMELS catchments spanning snowmelt-dominated, recent-rainfall, historical-rainfall, and arid regimes, using NOAA AORC meteorological forcing and remotely sensed vegetation and land-surface data. Performance is assessed using the Jawad-Kling-Gupta Efficiency (JKGE) metric, which accounts for stationary and non-stationary hydrologic behavior. We compare the full architecture with ablated variants and recurrent neural network benchmarks.
GCHM reproduces streamflow dynamics across diverse hydroclimatic regimes, including arid catchments, while maintaining interpretable states and fluxes. Ablation experiments show that simplified architectures may perform adequately under wet conditions but struggle to represent flow persistence and recession during dry periods, when groundwater storage sustains low flows. Learned gates recover hydrologically plausible relationships governing snowmelt, runoff, seepage, and evapotranspiration. GCHM combines competitive predictive performance with mass conservation and interpretability, providing a foundation for hydrologic modeling and counterfactual analysis.

---


### 85. [DSR-Net: Learning Dynamic Skeletal Relations for 3D Human Pose Estimation](https://arxiv.org/abs/2610.14499)

**<font color=#1a73e8>作者：</font>** Fan Li, Jian Xiang, LinLin Xue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D human pose estimation requires accurate modeling of motion-dependent skeletal structures and inter-joint dependencies. Existing methods typically rely on fixed skeletal topologies in Graph Convolutional Networks (GCNs) or implicitly capture joint relations through attention mechanisms, limiting their adaptability to diverse motion patterns. To address this issue,we proposeDSR-Net, a dynamic structural representation learning framework for 3D human pose estimation. Specifically, a Dynamic Skeletal Relation (DSR) module is introduced to learn adaptive inter-joint dependencies beyond predefined skeletal connections. Based on the learned relations, a hierarchical relation-aware fusion strategy is developed to facilitate effective interaction between structural and temporal representations. In addition, a lightweight Residual Skeletal Recalibration Module (RSRM) is designed to enhance the stability of structure-aware features with minimal computational overhead. Extensive experiments on Human3.6M and MPI-INF-3DHP demonstrate that DSR-Net achieves MPJPEs of 37.9 mm and 14.9 mm, respectively, consistently improving over strong baselines. The results validate the effectiveness of dynamic skeletal relation modeling for robust 3D human pose estimation.

---


### 86. [MontageFlow: Physically Valid High Fidelity EEG Generation](https://arxiv.org/abs/2610.14507)

**<font color=#1a73e8>作者：</font>** Sudarshan Regmi, Nabaraj Subedi, Arvind Pillai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative modeling offers a promising solution to the scarcity of labeled clinical electroencephalography (EEG) data under strict privacy constraints. Although recent generative models report substantial improvements in generation fidelity, we show that these gains conceal a categorical failure. EEG is not an arbitrary multichannel signal: each channel records the voltage difference between two scalp electrodes. So, real recordings satisfy exact linear identities among their channels. Current generators invariably violate these identities, yet this has gone unnoticed. We therefore propose MontageFlow, a flow-matching model that enforces these identities by restricting its output to signals that satisfy them. We find that ensuring validity improves fidelity too. Furthermore, to retain the EEG characteristics that oversmoothing washes out, we also condition the model on a physiological state vector encoded from the whole EEG window. For generation, this vector is drawn from a prior fitted in latent space. Across 3 large-scale benchmarks, our model improves TS-FID by 1.6-3.6$\times$ over the closest rival while ensuring validity.

---


### 87. [Spatiotemporal Recognition of Abdominal Wall Layers During Optical Trocar Entry](https://arxiv.org/abs/2610.14512)

**<font color=#1a73e8>作者：</font>** Shreeram Athreya, Andrew Melehy, Carter Prentice 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective. To evaluate whether spatial context and temporal modeling improve tissue recognition during optical trocar entry, where multiple abdominal-wall tissues may be visible simultaneously. Methods. We retrospectively analyzed 71 recordings with 1,516 annotated keyframes and 29,151 clinician-annotated sectors. Each frame was divided into 28 polar-grid sectors assigned to nine tissue classes. Color, neighboring-sector, and positional features were used by a gradient-boosted emission classifier. The full pipeline added learned temporal smoothing, spatial regularization, an anatomically ordered hidden Markov model, and posterior blending. Five-fold cross-validation was grouped by recording, with cross-fitting to prevent within-recording leakage. Primary evaluation used clinician-derived targets; ablations assessed classification, probability quality, spatial consistency, and peritoneum-or-deeper onset timing. Results. The complete pipeline achieved accuracy 0.646, macro-F1 0.507, and macro-AUROC 0.882, versus 0.600, 0.440, and 0.861 for emissions alone. Macro-F1 improved by 0.066 across all five folds. Label changes decreased from 66.2 to 19.5 per sector-minute, and median onset error decreased from 15.58 to 2.45 seconds. Frames with a tissue-depth-code span of at least three decreased from 53% to 26%, versus 22% for clinician annotations. Performance remained limited for preperitoneal fat and bowel, and the full model retained a 44% premature-onset proportion. Conclusions. Combining appearance, spatial context, and temporal constraints improved retrospective tissue recognition and onset localization. Tissue-specific limitations, residual timing errors, and reliance on future observations warrant external validation and prospective evaluation of causal models before clinical use.

---


### 88. [TartanMatch: Towards Universal Dense Correspondence Across Modalities](https://arxiv.org/abs/2610.14513)

**<font color=#1a73e8>作者：</font>** Hyeokjoon Kwon, Jiting Cai, Ruogu Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic platforms combine multi-modal sensors to operate across diverse conditions, but most dense correspondence methods are limited to RGB-RGB or a small set of modality pairs. Training a model for each modality pair scales poorly with the number of sensors and forgoes potential positive transfer across modality pairs. We introduce TartanMatch, a unified model for dense correspondence across all 25 ordered pairs among RGB, event, thermal, depth, and projected LiDAR. TartanMatch adapts an RGB-pretrained correspondence model to all modality pairs within one shared network using lightweight modality adaptation and a mixture of real and synthetic data. On zero-shot real-world benchmarks, TartanMatch reduces Endpoint Error (EPE) over the strongest baselines by 61.9% for cross-modal matching and 49.6% for same-modal matching. We further show that joint training across all modality pairs improves average matching accuracy over pair-specific training, especially on challenging cross-modal pairs. These results demonstrate that a single model achieves broad multi-modal coverage and state-of-the-art matching accuracy.

---


### 89. [Compositional Concepts Erasing: Disentangling Object-Style via Domain Manifold Unlearning](https://arxiv.org/abs/2610.14514)

**<font color=#1a73e8>作者：</font>** Yang Xiao, Kaiyuan Deng, Gen Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models pose significant risks regarding the generation of illicit content and copyright violations. This has catalyzed the development of machine unlearning to erase harmful concepts or copyrighted styles from a model's generative repertoire without compromising its general performance. However, previous unlearning approaches on diffusion models have largely focused on either object-level or style-level removal and failed to address the challenge of object-style combination unlearning. At the same time, multiple unlearning requests often lead to catastrophic forgetting. To address these challenges, we propose Domain Manifold Unlearning (DMU), which uses an EMA-updated feature proxy extracted from intermediate diffusion features to represent the retained target-object direction. As a lightweight estimating representation of an object, DMU enables selective unlearning of domain-specific components in a specific object while preserving other semantic representations, thereby significantly enhancing robustness in multiple combination unlearning scenarios. Extensive experiments show that DMU significantly mitigates catastrophic forgetting, outperforming state-of-the-art methods of batch unlearning and sequential unlearning.

---


### 90. [SEPM: Self-Evolving Procedural Memory Grounded in Task Graphs for Multi-Agent Collaboration](https://arxiv.org/abs/2610.14515)

**<font color=#1a73e8>作者：</font>** Yi Liu, Junwei Zhao, Li Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Long-horizon multi-agent collaboration requires memory that preserves both successful actions and the coordination structure underlying them. Existing memory systems support information sharing or procedural reuse, but often leave the evolution of shared procedures disconnected from the task dependencies and execution states of collaborating agents. This coupling also limits the direct transfer of procedural memory designed for individual agents to team settings. We propose Self-Evolving Procedural Memory (SEPM), a framework that uses task dependency graphs as a common representation for online coordination and procedural memory evolution. During execution, a lightweight shared blackboard records structured evidence alongside task dependencies, supporting the detection of goal, plan, and world-state divergence and evidence-based realignment. After execution, verified actions and dependencies are distilled into reusable procedures, while recurring failures inform warnings and constraints. The shared procedure pool evolves through creation, refinement, specialization, and retirement, guided by success and cost utility and constrained by evidence and safety requirements. Together, these mechanisms preserve the collaborative structure and applicability conditions needed to reuse experience across tasks. Evaluations on ALFWorld, WebArena, and OfficeBench under AutoGen and DyLAN show that SEPM achieves the highest task scores among the compared methods in all six benchmark settings. Under AutoGen, it improves task scores over the no-added-memory baseline by 29.85, 25.86, and 13.00 percentage points, respectively. The codebase is available at this https URL.

---


### 91. [We Have Been Interpreting Diffusion Transformer Backbone Behaviors Wrong](https://arxiv.org/abs/2610.14517)

**<font color=#1a73e8>作者：</font>** Benyuan Meng, Longtao Huang, Yang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> During a network forward call, diffusion backbones naturally produce many intermediate activations. If we evaluate each activation against an identical downstream benchmarking protocol, we can plot an inverted-U-shaped curve as the depth profile: the activation's performance goes up first and then down as we go into deeper layers. This is common knowledge in the diffusion model community, which inspires many applications including the widely-adopted REPA. However, the common interpretation of this depth profile may be inaccurate and incomplete: (i) The cause of this curve has long been treated as signal granularity changing from coarse to fine, but there has been little evidence in DiT backbones. (ii) The community has been mainly studying this phenomenon in a static way, without investigating how it changes across different training setups. In this work, we show a different mechanism picture for the profile, where the prediction target (e.g., $\epsilon$, $u$, $x_0$) sits at the center. The semantically meaningful signal is only an intermediate by-product for predicting the target, while the prediction target is the real goal for the backbone. Furthermore, the choice of prediction targets as part of the training setup can predictably affect the curve's shape. With this updated interpretation, many applications of this depth profile can be better grounded and predicted. As an example, we show how to predict the near-optimal placement of REPA based on the prediction target of the training setup. The code is at this https URL.

---


### 92. [ScienceBuddy-PV: A Verifier-Governed Recursive Improvement Protocol for Panvascular Intervention Research](https://arxiv.org/abs/2610.14523)

**<font color=#1a73e8>作者：</font>** Lingsen You, Yujun Guo, Xinyu Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> ScienceBuddy-PV adapts the ScienceBuddy recursive-in-recursive design to panvascular intervention research through a structured evidence ledger, device-vessel ontology, abstention contract and retained failure bank. Recursive harness optimization and outer-loop model learning, including reinforcement learning, are specified but not executed. We audit a fixed component, rather than the complete agent system, using separate ARCADE syntax and stenosis tasks (1,000 training, 200 validation and 300 test images per task). A shared task-masked convolutional model was trained once per representation setting; its parameters and the heuristic support gate were then held fixed, with the stenosis threshold selected on validation data. On the locked test sets, syntax Dice was 0.475 (95% CI 0.459-0.490) and stenosis Dice was 0.231 (95% CI 0.214-0.249). Stenosis pixel AUROC was 0.957 and AUPRC was 0.180 at prevalence 0.00975. The gate accepted 76.7% of stenosis-frame outputs versus 100% for a score-only comparator. In a constructed mask audit, it accepted 44.3% of reference candidates and rejected 55.7%, exposing the cost of abstention. Acceptance does not establish correctness or clinical safety. This public-data component audit makes support and abstention measurable and provides a reproducible protocol for future collaborative agent studies. It does not demonstrate recursive improvement, patient-level validity or clinical device recommendations.

---


### 93. [Energy Ring: Stabilizing Feature Energy for Reliable Test-Time Discovery](https://arxiv.org/abs/2610.14525)

**<font color=#1a73e8>作者：</font>** Tianle Liu, Fan Lyu, Tingliang Feng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-Time Discovery (TTD) aims to recognize known classes and detect novel ones while the model is already deployed, operating directly on a continual unlabeled test-time stream. Existing TTD methods are overly conservative, making known and unknown features collapse together and difficult to separate during test-time adaptation. In this paper, we revisit TTD from an energy perspective and find that the natural energy gap between known and unknown classes is unstable and easily collapses. We therefore propose Energy Ring to stabilize this gap by anchoring the two types of classes on separate energy rings. A lightweight adapter enlarges the norm-based gap while preserving known-class directions, and a perturbation consistency module forms compact clusters for unknown classes. During testing, energy-guided confidence weighting improves prediction, and a stability-based rectification mechanism corrects unreliable updates. Experimental results show that Energy Ring significantly improves TTD performance against existing TTD methods.

---


### 94. [FDE-Bench: Evaluating End-to-End Delivery from Underspecified Real-World Business Requests](https://arxiv.org/abs/2610.14539)

**<font color=#1a73e8>作者：</font>** Huaiming Li, Can Huang, Chufan Wu 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world business requests often leave key requirements unstated because frontline practitioners struggle to articulate rules they know from experience. Forward-deployed engineers (FDEs) must elicit these requirements through dialogue and iteratively optimize solutions until they meet customer acceptance criteria. Existing optimization benchmarks typically start from explicit objectives, while clarification benchmarks often introduce information gaps into existing tasks. We introduce FDE-Bench, the first benchmark built from real customer projects to evaluate agents on end-to-end delivery tasks that require interactive requirement clarification and iterative optimization. Its 49 cases span combinatorial optimization and machine learning. Clarification targets are distilled from discussions between frontline practitioners and FDEs. Agents elicit missing requirements from a simulated customer, and case-specific evaluators assess final artifacts against acceptance criteria using customer-accepted FDE solutions as quality references. Across 18 agent configurations, the highest mean delivery score is only 0.5510, compared with an FDE reference of 1.0. The highest delivery success rate (DSR), defined as the fraction of planned runs reaching this reference, is only 6.12%. These results show that reliable FDE-level end-to-end delivery remains out of reach for the evaluated agents on underspecified real-world business tasks. The benchmark project page is available at this https URL.

---


### 95. [Are Multimodal Benchmarks Really Useful? Item-Level Multimodal Benchmark Diagnosis via Structure-Response Co-Calibration](https://arxiv.org/abs/2610.14542)

**<font color=#1a73e8>作者：</font>** Shiqi Zhang, Weixin Zeng, Ziheng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal benchmarks are central to evaluating whether models can reason over information from multiple modalities. However, existing literature has revealed that some benchmarks may contain shortcut items that can be answered from a single modality or from answer-option regularities alone, thus failing to reflect models' true cross-modal inference ability. Existing methods for assessing benchmarks typically rely either on intrinsic item structure or extrinsic model response behavior, which are not adequate for a comprehensive diagnosis. To fill in this gap, we propose SRCoD, a structure-response co-calibrated diagnosis framework for item-level diagnosis of modality dependence in multimodal benchmarks. SRCoD estimates sample-wise multimodal information structure from benchmark content and target answers, and uses this signal as a soft structural anchor for modality-conditioned item response modeling. The learned model produces a calibrated item-level diagnostic profile that reflects how strongly an item depends on different forms of modality evidence, enabling fine-grained benchmark analysis beyond aggregate accuracy. SRCoD also provides interpretable attribution of the diagnosis results. Extensive experiments under two complementary protocols, i.e., benchmark-refinement oriented validation and human-labeled item validation, demonstrate that SRCoD outperforms state-of-the-art benchmark diagnosis methods.

---


### 96. [InfraWorld: Motion-Aware World Modeling for Roadside 4D Occupancy Forecasting](https://arxiv.org/abs/2610.14544)

**<font color=#1a73e8>作者：</font>** Songkai Wang, Xiaokai Bai, Lei Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Roadside 4D occupancy forecasting predicts future semantic occupancy in a fixed infrastructure coordinate system. Roadside scenes are globally structured yet locally evolving, requiring comprehensive scene-level context while precisely modeling sparse localized motion. However, existing forecasting paradigms struggle to tackle both requirements. To address this limitation, we propose InfraWorld, a world model formulating roadside occupancy forecasting as selective state evolution. InfraWorld maintains a dense BEV state for the complete scene and persistent motion queries for moving regions, assigning complementary states to global context and local dynamics. Specifically, we propose Dynamic Query Initiation (DQI) to initialize queries in regions supported by motion in the observed history. During rollout, the dense state is updated through Long--Short Temporal Fusion (LST), which combines short-term adjacent-frame continuity with long-term motion trends to preserve stable context while capturing scene evolution. Motion-Aware Query Injection (MAQI) then refines the queries and injects confidence-weighted query information into corresponding BEV tokens, enabling targeted dynamic updates without perturbing global context. Together, InfraWorld concentrates predictive capacity on evolving traffic regions. Extensive experiments on the InfraOcc and Occ3D--nus datasets demonstrate that InfraWorld achieves state-of-the-art performance for roadside 4D occupancy forecasting while retaining its effectiveness under ego-centric settings. Code will be released.

---


### 97. [Active Neural Matter: A Finite-Window Response Framework for Physical Systems and Distributed AI Workflows](https://arxiv.org/abs/2610.14549)

**<font color=#1a73e8>作者：</font>** Tianchi Chen, Shihua Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical systems and distributed AI workflows can retain past information, receive delayed feedback and combine conflicting signals. These features pose a common modeling problem: determining what information about past interactions a state must retain to account for future responses. Active Neural Matter (ANM) addresses this problem through a finite-window response framework. Forward analysis uses each system's dynamics to predict state and output responses to perturbations, separating propagation from output sensitivity. Inverse analysis tests whether a candidate state retains enough information for these responses. With the system and future inputs or interaction rules fixed, distinguishable responses from histories assigned the same state identify distinctions the representation must preserve. Their distributional separation gives a lower bound on the worst-case error of approximating behavior from that state. Uncertainty bounds distinguish rejection, support within a fixed tolerance on tested comparisons, and unresolved cases. Delayed-consensus simulations check analytical predictions of response amplitude and phase over a narrow range of delays; flocking illustrates dependence on the chosen observable. An exact delayed-return construction establishes a sufficient state for a specified program. The AI studies identify distinctions in interaction history and evidence order that a representation must preserve to reproduce observed response distributions. Tests on new histories in a controlled feedback task provide bounded support for a state specified by the task instructions; the instructed rule predicts every observed action. ANM connects response prediction to measurable information requirements, separating behavioral fidelity from task correctness and initial-state adequacy from a closed evolution law for that state.

---


### 98. [Adversarial Gradient Forcing for Robust Few-Step Autoregressive Video Generation](https://arxiv.org/abs/2610.14553)

**<font color=#1a73e8>作者：</font>** Chenxi Xia, Yixuan Xu, Shan Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video generation models generate videos sequentially, with each new block conditioned on previously generated blocks. By training on the model's own rollouts, Self Forcing and its follow-up methods substantially mitigate exposure bias caused by the mismatch between training- and inference-time history distributions. However, these models still suffer from error accumulation during long-horizon generation. We identify a key underlying limitation: the model remains highly sensitive to errors in its generated history, allowing small deviations to be amplified through subsequent generations. We refer to this underexplored problem as the local history robustness gap. To address this gap, we introduce Adversarial Gradient Forcing (AGF), a framework designed to improve the robustness of few-step autoregressive video models to perturbations and accumulated errors in their own generated histories. AGF uses distribution matching gradients from future block predictions to select adversarial perturbations of self-generated histories. It then jointly trains the generator on the original and perturbed histories to improve the robustness of future generation. Extensive experiments show that AGF achieves the highest VBench Total score on 60-second video generation and the best visual quality on four-minute video generation. Notably, AGF achieves such long-horizon robustness while requiring only 5-second rollouts for training.

---


### 99. [PGSB: Pretrained-Guided Shared Basis for LoRA Model Merging](https://arxiv.org/abs/2610.14558)

**<font color=#1a73e8>作者：</font>** Muqing Liu, Chongjie Si, Zhuoya Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large pretrained models have achieved remarkable success across diverse domains, yet adapting them to multiple downstream tasks remains challenging: full fine-tuning is costly, while maintaining separate task-specific models is storage-inefficient and fails to produce a unified multi-task model. Low-Rank Adaptation (LoRA) offers an efficient alternative for Model Merging by representing each task adaptation as a low-rank update over frozen pretrained weights. However, existing LoRA merging methods often treat task-specific updates as directly comparable objects and merge them in their original low-rank parameter spaces. This overlooks two key factors: which update directions provide reliable shared support across tasks, and how these directions should be re-parameterized with respect to the pretrained weights before merging. To address this limitation, we propose Pretrained-Guided Shared Basis (PGSB), a two-stage framework for LoRA model merging. PGSB first identifies shared directions among task-specific LoRA updates, and then re-parameterizes these directions using their interaction with the pretrained weights, producing a more suitable basis for merging. Extensive experiments demonstrate that PGSB consistently outperforms state-of-the-art baselines across multiple benchmarks. Codes are available at this https URL .

---


### 100. [Bidirectional Adaptive Transformers for Multimodal Anomaly Detection](https://arxiv.org/abs/2610.14598)

**<font color=#1a73e8>作者：</font>** Yuxin Jiang, Yunkang Cao, Weiming Shen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The effective integration of features derived from RGB images and 3D point clouds presents a substantial challenge in the field of multimodal anomaly detection (MAD). Existing MAD methods typically rely on static fusion paradigms built upon frozen pre-trained encoders. While these frameworks facilitate spatial alignment, they lack the mechanism to establish latent semantic correspondence, thereby inducing cross-modal interference that degrades anomaly discriminability.
To mitigate these limitations, this study proposes a Bidirectional Adaptive Transformers (BAT) framework, which constructs comprehensive and semantically aligned multimodal representations by leveraging complementary attributes across modalities.
The BAT framework introduces a Bidirectional Feature Alignment (BFA) module, which employs a mutual predictive mechanism to bridge the gap between 2D textural patterns and 3D geometric structures. This bidirectional interaction explicitly enhances the textural granularity of point cloud descriptors while augmenting the spatial contextual awareness of RGB features.
To ensure that the latent representations possess sufficient informational density for alignment, BAT incorporates a parameter-efficient adaptation architecture. By utilizing lightweight image and point cloud adapters, the framework facilitates specialized fine-tuning of pre-trained models, mitigating the information loss inherent in frozen encoders.
Extensive experiments conducted on MVTec 3D-AD and Eyecandies confirm that BAT achieves state-of-the-art anomaly detection performance, significantly outperforming existing MAD methods.

---


> [!TIP]
> 当前位于：**51-100**（第 2/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

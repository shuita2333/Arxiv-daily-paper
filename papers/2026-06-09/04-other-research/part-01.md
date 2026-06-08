# 📦 其他研究 | 2026年06月09日

> 本类共 **199** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-199](./part-04.md)

---

### 1. [Enhancing Malware Detection with Generative AI: Using Variational Autoencoders to Boost Machine Learning Classifiers' Performance](https://arxiv.org/abs/2606.06501)

**<font color=#1a73e8>作者：</font>** Mohammad Alharbi, Jeremy Straub  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The advancement of malware poses obstacles for cybersecurity, necessitating the development of advanced detection techniques. This paper proposes an approach to enhance malware detection through the use of a generative artificial intelligence model. Specifically, variational autoencoders (VAEs) are used with the random forest, XGBoost and sequential model machine learning classifiers. Generated synthetic malware samples are used to address the critical issue of data scarcity for new or less common malware types. This approach can be used to augment datasets to improve classifier robustness.
The proposed methodology uses VAEs to create high-quality diverse synthetic datasets that closely mimic real-world malware data. The effectiveness of these augmented datasets is evaluated by comparing the performance of the machine learning classifiers when they are trained with the original data and when they are trained with the synthetic data-augmented datasets. The results demonstrate a notable improvement in the accuracy, precision, recall and F1-scores of the classifiers, when they are trained using the augmented datasets. The enhanced performance for detecting various malware classes shows the potential of this approach to facilitate adaptation to evolving malware threats effectively. This work demonstrates the utility of generative AI for cybersecurity. It also provides a foundation for future research aimed at developing more resilient and adaptive malware detection systems.

---


### 2. [Detecting and Mitigating Bias by Treating Fairness as a Symmetry Operation](https://arxiv.org/abs/2606.06514)

**<font color=#1a73e8>作者：</font>** Nishit Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning systems deployed in high stakes socioeconomic settings routinely display bias. We formalize bias as a symmetry breaking operation: a classifier is fair if its outputs remain invariant under the counterfactual operation of switching a sensitive attribute, with merit features held fixed. We implement loss based regularization as a symmetry restoring mechanism and evaluate the framework on four synthetic datasets with varying levels of noise, correlation, and bias. The framework achieves upwards of 90\% violation reduction, with accuracy costs around 5\%. This framework does not require causal graph knowledge, is computationally lightweight, and generalizes to any sensitive attribute definable as a bit-flip, making it suitable for contexts where local sources of discrimination remain absent from mainstream benchmarks.

---


### 3. [DiBS: Diffusion-Informed Branch Selection](https://arxiv.org/abs/2606.06518)

**<font color=#1a73e8>作者：</font>** Bo Liu, Yuan Xie, Yuan Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sudoku is a representative constraint satisfaction problem that requires global structural reasoning under strict discrete constraints. The existing works of solving Sudoku mainly focus on two dominant approaches, i.e., traditional heuristic and deep learning solver. However, they suffer from two complementary limitations: learning-based solvers lack hard correctness guarantees, while complete symbolic solvers are still prone to long-tail search. To address these shortcomings, we propose a novel diffusion model-guided approach, termed as DiBS, for the branch selection search process. Specifically, DiBS keeps the symbolic solver complete and uses the diffusion model as a branch-ordering guide. The core method is ranking candidate values under the current partial assignment and lightweight consistency signal. Furthermore, we provide an in-depth theoretical proof to reveal how it works and why it works. Experiments on the challenging Royle 17-clue Sudoku benchmark show that our DiBS substantially reduces search cost relative to strong heuristic baselines, especially in nodes, backtracks, and long-tail percentiles. Besides, these results confirm that learned global guidance is effective on hard instances where branch-order mistakes are most expensive. All codes are available at this https URL.

---


### 4. [Applying Deep Learning for cockpit segmentation in the context of mixed reality](https://arxiv.org/abs/2606.06520)

**<font color=#1a73e8>作者：</font>** Alexandre Leles Sousa, Pedro de Oliveira Nielson, Erick Oliveira Rodrigues 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer vision is an area that has been growing continuously. With the advance of technologies with a first-person view, new development opportunities have emerged inside the area. Mixed reality promotes virtual environments with objects from the physical world shown in real time. For that, it's necessary to be concerned with the immersion of the user in this simulated environment, increasingly seeking to bring it closer to a possible desired reality. This paper proposes the development of image processing in order to perform the segmentation of images to identify what is foreground and background in order to facilitate the union of virtual and real images. Thus, the present work obtain real images of the user using the off-highway truck simulator CAT793F, through a camera, to be able to perform the segmentation of such images with artificial intelligence this http URL convolutional neural network architectures "U-net" and "DeepLabV3+" are applied to perform image segmentation. As a result, metrics with around 90% accuracy were presented and and the best model was determined.

---


### 5. [CrowdMath: A Dataset of Crowdsourced Mathematical Research Discussions](https://arxiv.org/abs/2606.06526)

**<font color=#1a73e8>作者：</font>** Sherin Muckatira, Jesse Geneson, Slava Gerovitch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have made substantial progress on mathematical reasoning, but existing benchmarks typically evaluate well-specified problems with final answers, step-by-step solutions, or complete proofs. They do not capture collaborative open-problem solving: a setting in which participants propose partial arguments, identify gaps or errors in prior steps, repair flawed reasoning, and gradually synthesize incremental contributions into a proof. We introduce CrowdMath, a dataset of 164 expert-annotated progress chains from the MIT PRIMES--Art of Problem Solving (AoPS) CrowdMath program (2016-2025), a collaborative research initiative whose discussions have led to peer-reviewed publications. Each chain traces a multi-participant forum discussion from an open-problem statement to a completed proof. Posts are labeled by their functional roles in the evolving solution process, including partial progress, proof completion, erroneous reasoning, and error identification. We define evaluation tasks and benchmark six frontier models. Models achieve 83-88% accuracy on next-post prediction, suggesting that they can follow the local flow of mathematical discussion. However, they struggle to identify the functional significance of individual contributions with the best model achieving only 0.42 macro-F1 on post-role classification. CrowdMath exposes a gap between solving well-specified mathematical problems and understanding collaborative mathematical progress as it unfolds.

---


### 6. [CARVE-Q: Quantum-Proposed, Classically Certified Interactive Driving Repair](https://arxiv.org/abs/2606.06531)

**<font color=#1a73e8>作者：</font>** Yifan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The critical question after a correct driving veto is not only whether a maneuver is unsafe, but whether the blocked interaction admits a lawful, auditable, and responsibility-bounded repair. Prediction and game-theoretic planners can suggest plausible cooperation, yet they do not return a proof that the repair respects hard rules, right-of-way, cost allocation, and ego fallback. We introduce CARVE, Certified Affordable Repair of Vetoed maneuvers via Envelopes, a certificate architecture for prediction-free interactive repair. Given a vetoed maneuver, CARVE constructs a finite repair lattice and emits a structured certificate recording the binding rule, selected joint repair, right-of-way-scaled cooperation envelope, responsibility-weighted cost split, and ego-only fallback. This certificate view reveals the algorithmic bottleneck: multi-owner repair induces a product lattice $M = \prod_j |\mathcal{A}_j|$. We therefore introduce CARVE-Q, a verifier-shielded quantum-AI search layer that applies quantum minimum finding only to this black-box lattice while leaving all safety authority classical. In the conservative verifier-oracle model, exact classical minimum finding requires $\Theta(M)$ queries in the worst case, whereas Durr-Hoyer/Grover minimum finding uses $O(\sqrt{M})$ oracle queries with high probability. We prove verifier-shielded certificate soundness, priority non-elicitation, black-box query separation, and finite-precision reversible-oracle constructibility. We then demonstrate state-vector minimum finding on CARVE repair oracles up to 65,536 assignments and validate certificate preservation on Lanelet2-grounded INTERACTION replay with 100% right-of-way respect, 100% blame consistency, and zero priority false positives. The result is a trust-bounded quantum-AI pattern for certified autonomy: quantum proposes; CARVE certifies.

---


### 7. [Position: Don't Just "Fix it in Post": A Science of AI Must Study Training Dynamics](https://arxiv.org/abs/2606.06533)

**<font color=#1a73e8>作者：</font>** Stella Biderman, Mohammad Aflah Khan, Niloofar Mireshghallah 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What would it mean to have a scientific understanding of AI? Models are not static objects: they are snapshots of time-evolving processes shaped by data, objectives, architectures, and optimization dynamics. Yet much of AI research treats models as fixed artifacts, analyzing behaviors after training rather than asking why they emerge. This position paper argues that a science of AI must move beyond post-hoc fixes and study the training dynamics that produce model behavior. Such a science should support progressively stronger forms of understanding: predicting outcomes from early training signals, intervening when trajectories go wrong, and ultimately designing training procedures that more reliably produce desired properties. Scaling laws have made prediction routine for loss; the challenge is extending this success to capabilities, biases, robustness, and safety-relevant behaviors. We articulate requirements for such theories grounded in the history and philosophy of science, examine progress in mechanistic interpretability, fairness, memorization, and simplicity bias, and identify concrete open problems.

---


### 8. [Attention-Guided Autoencoder Fusion for Insulator Defect Detection Using UAV Transmission-Line Imaging](https://arxiv.org/abs/2606.06536)

**<font color=#1a73e8>作者：</font>** Malak Allam, Khaled Shaban, Ali Hamdi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated defect detection in high-voltage transmission-line insulators remains challenging due to severe class imbalance, large scale variation, and the small spatial extent of defect instances in Unmanned Aerial Vehicle (UAV) imagery. To address these challenges, this paper proposes AE-YOLO, an Attention-Guided AutoEncoder-Enhanced YOLO framework for robust insulator defect detection. The architecture integrates lightweight bottleneck autoencoders within a Feature Pyramid Network-Path Aggregation Network (FPN-PAN) neck. This preserves anomaly-sensitive information during multi-scale feature fusion. Convolutional Block Attention Modules (CBAM) are used throughout the backbone, enhancing feature discrimination and suppressing background interference. The framework also introduces a variance-maximizing autoencoder regularization strategy, which encourages diverse, defect-discriminative latent representations. The network trains using a unified objective that combines focal loss, Complete IoU (CIoU) loss, and autoencoder regularization to address foreground-background imbalance and improve localization accuracy. During inference, Weighted Boxes Fusion (WBF) combines predictions from YOLOv8, YOLOv10, and YOLO11. An autoencoder-guided confidence boosting mechanism improves sensitivity to rare defect categories. Experiments on the Insulator-Defect Detection dataset show that AE-YOLO with an EfficientNetV2 backbone achieves 95.10 percent mAP at 0.5, 96.40 percent precision, and 93.80 percent recall. This performance surpasses the strongest YOLO-family baseline by 5.0 points in mAP at 0.5 and 6.7 points in recall. These results confirm the effectiveness and adaptability of the framework. The model is a practical and scalable solution for UAV-based transmission-line inspection and defect monitoring.

---


### 9. [Synthetic Benchmarks Overstate Forward-Forward Scaling: Real-Data Limits of Layer-Local Training](https://arxiv.org/abs/2606.06539)

**<font color=#1a73e8>作者：</font>** Yucheng Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forward-Forward (FF) learning [Hinton, 2022] replaces backpropagation with strictly layer-local goodness updates. Recent FF-CNN work has narrowed the gap to BP on 32x32 benchmarks, raising the question of whether layer-local training is becoming a viable alternative at realistic scale. To probe this rigorously, we develop DTG-FF -- dynamic temperature goodness, decoupled normalization, and multi-layer fusion -- as an instrument that sets FF-family state of the art across nine real-data benchmarks (91.8% CIFAR-10 and the first FF baseline at ImageNet-100 224x224), and use it to audit how far layer-local training actually scales.
(1) Real-data scaling. Under identical recipe and backbone, an architecture-matched BP-DeepSup baseline beats DTG-FF by 2.40/5.93 pp on CIFAR-10/CIFAR-100, and the gap widens with class count. At 224x224 the same instrument reaches only 49.4% -- the first FF baseline at this scale, versus typical BP above 75% [Tian et al., 2020] -- exposing a real-data ceiling invisible at 32x32.
(2) Synthetic vs. real K-conflict. DTG-FF increasingly outperforms BP as class count K grows on synthetic teacher-student tasks, yet on real images the FF-BP gap reverses sign and widens with K. A within-dataset CIFAR-100 coarse vs. fine probe isolates label-hierarchy from image distribution: synthetic K-sweeps confound output dimensionality with fine-grained discrimination difficulty and thereby overstate FF transferability.
(3) Systems audit. FF can be implemented without storing depth-wide activations, but on commodity 8 GB hardware standard BP+gradient-accumulation reaches 4.18 GB / 157 imgs/s versus DTG-FF's 7.90 GB / 138 imgs/s, so a memory-based justification for FF at this scale is not supported under fair baselines.

---


### 10. [Multi-Scale Feature Attention Network for Polymer Classification using THz Dual-Comb Spectroscopy](https://arxiv.org/abs/2606.06554)

**<font color=#1a73e8>作者：</font>** Roshni Mahtani, Ilán Carretero, Laura Monroy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable polymer identification is essential for ensuring the quality and safety of recycled plastics, yet conventional sorting and spectroscopic techniques often struggle to deliver robust discrimination. Terahertz Dual-Comb Spectroscopy (THz-DCS) offers a promising alternative, providing rapid, high-resolution, and non-destructive measurements. In this work, we leverage THz-DCS to classify 12 types of polymers, including pure polymers, multilayer films, commercial blends, and biopolymers. To handle the complexity of these spectral signals, we propose the Multi-Scale Feature Attention Network (MSFAN), a novel deep learning architecture tailored for THz-DCS data. The framework integrates feature gating for signal recalibration and multi-scale parallel convolutions to capture diverse frequency patterns. These features are further refined through cross-feature attention and attention pooling, enabling the model to intrinsically highlight the most informative THz regions. MSFAN consistently outperforms state-of-the-art models, reaching a classification accuracy of 85.2%. This study demonstrates the potential of combining THz-DCS with deep learning techniques for effective, scalable, and interpretable polymer classification.

---


### 11. [MacArena: Benchmarking Computer Use Agents on an Online macOS Environment](https://arxiv.org/abs/2606.06560)

**<font color=#1a73e8>作者：</font>** Victor Muryn, Maksym Shamrai, Sofiia Mazepa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) operate graphical user interfaces (GUIs) through vision and control primitives, and their capabilities have advanced rapidly, driven in part by standardized online evaluation benchmarks such as OSWorld, which serve both as evaluation tools and as training environments for reinforcement learning. However, macOS remains underserved in this landscape: the only existing benchmark, macOSWorld, covers a narrow slice of first-party applications with simpler tasks, and runs on x86 virtual machines incompatible with Apple Silicon. We introduce MacArena, a benchmark of 421 manually verified tasks spanning 50 applications that combines a curated port of OSWorld tasks, content sourced from macOSWorld, and 49 new macOS-native tasks, all running on Apple's native Virtualization framework on Apple Silicon. We argue that macOS presents distinct GUI challenges beyond what Linux-based benchmarks capture, and our evaluation supports this claim: strong model performance on existing benchmarks can reflect familiarity with task distributions rather than genuine cross-platform GUI competence. Notably, model rankings invert between ported and macOS-native tasks, with a leading model trailing by over 26% on the MacArena subset, suggesting that macOS poses a genuinely harder environment for current GUI agents.

---


### 12. [WAV: Multi-Resolution Block Residual Routing for Deep Decoder-Only Transformers](https://arxiv.org/abs/2606.06564)

**<font color=#1a73e8>作者：</font>** Kehan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual connections are central to training deep Transformers, but standard PreNorm residual streams aggregate sublayer updates with fixed unit weights. Recent Attention Residuals replace this fixed accumulation with content-dependent depth-wise routing, and Block Attention Residuals make the mechanism efficient by routing over block-level residual summaries. However, a single block summary stores only the low-frequency total residual displacement inside a block, discarding directional structure such as attention-vs-MLP imbalance and early-vs-late block dynamics. We propose WAV v1, a lightweight multi-resolution residual routing method for decoder-only Transformers. Instead of representing each block only by its accumulated residual sum, WAV v1 augments every block with two directional detail bases: a phase basis that contrasts attention and MLP updates, and a split basis that contrasts early and late sublayer updates. These bases are routed together with standard block summaries through the same depth-wise softmax mixer, while negative detail-source initialization and detached RMS matching stabilize training. On character-level TinyStories and Text8 language modeling, WAV v1 shows a clear depth-dependent benefit. Although it is not consistently beneficial at 12 layers, it becomes competitive at 24 layers and outperforms all baselines at 48 layers. At 48 layers, WAV v1 reduces validation loss relative to Block AttnRes from 0.4960 to 0.4738 on TinyStories and from 0.9363 to 0.9305 on Text8, with negligible additional parameters. These results suggest that directional residual details, not only block-level sums, are important for scaling residual routing in deeper Transformers.

---


### 13. [Are you sure? A Comprehensive and Comprehensible Survey of Uncertainty Quantification in Symbolic Regression](https://arxiv.org/abs/2606.06567)

**<font color=#1a73e8>作者：</font>** Julia Reuter, Fabricio Olivetti de Franca  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR) is a class of methods that systematically explore the space of mathematical functions to discover models that accurately capture the underlying relationships in a dataset. Despite recent advances in the field, a lack of support for uncertainty quantification (UQ) limits its adoption in real-world decision processes. In regression analysis, UQ provides important information about the model reliability, which can both help to avoid overfitting by accounting for uncertainty in the data, and provide insights for decision-making. This survey is the first to clearly address this issue, with the objective of introducing essential UQ concepts and reviewing the current literature on UQ in SR, which can be broadly organized into three research directions: frequentist, Bayesian, and model selection. Despite its importance, UQ in SR is still underexplored, which motivates further research into reliable UQ methods for SR.

---


### 14. [MalTree: Tracing Malware Evolution from Embeddings at Scale](https://arxiv.org/abs/2606.06570)

**<font color=#1a73e8>作者：</font>** Akash Amalan, Georgios Smaragdakis, Tom J. Viering  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malware detection remains largely reactive: machine learning models trained on known samples degrade as threats evolve. Understanding evolutionary relationships among malware families can inform proactive defense, but traditional reverse engineering can take months to years to uncover such lineage relationships. We propose MalTree, a framework that applies bioinformatics inspired phylogenetic techniques (UPGMA and Neighbor-Joining) at scale to model malware evolution automatically using structural, behavioral, and image-based features. We introduce temporal validation using VirusTotal timestamps to assess whether inferred trees reflect actual evolutionary order. MalTree achieves 87% temporal consistency, indicating that inferred evolutionary relationships closely align with real-world emergence timelines. Our analysis shows that some families mutate over 10 times faster than others, suggesting that detection strategies should be tailored to family-specific evolutionary tempos. Case studies, including the Mirai botnet, confirm that inferred relationships from our phylogenetic tree align with documented threat intelligence. Our framework provides a foundation for shifting malware analysis from sample-by-sample classification toward lineage-aware evolutionary modeling.

---


### 15. [Generative Models Erode Human Temporal Learning Through Market Selection](https://arxiv.org/abs/2606.06572)

**<font color=#1a73e8>作者：</font>** Wenjun Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We argue that modern generative models create structural risks for knowledge and cultural production at current, sub-AGI capability levels. We define Human Temporal Learning (HTL) as path-dependent knowledge accumulation through sustained engagement with problems over time. Generative outputs increasingly resemble HTL-intensive work in surface features, so verifying whether a given output reflects genuine human learning grows costly relative to its expected benefit. Once verification loses economic justification, evaluators reward outputs regardless of production mode, and producers who invested years of learning compete on price against outputs that cost almost nothing to generate. We call this pathway value collapse and formalize it through a costly-inspection framework. Cross-domain evidence from academic publishing, legal practice, content platforms, and software security maps onto four stages of verification erosion. Alignment success is orthogonal. Better-aligned models narrow observable gaps between human and AI outputs, making source verification harder and intensifying competitive pressure against HTL-intensive work even when individual AI outputs improve.

---


### 16. [Gaussian Process Latent Factor Regression for Low-Data, High-Dimensional Output Problems](https://arxiv.org/abs/2606.06576)

**<font color=#1a73e8>作者：</font>** Edward T. Stevenson, Eric T. Wolf, Mei Ting Mak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the sciences, regression tasks often require predicting high-dimensional outputs from few training examples. Multi-output Gaussian processes excel in low-data regimes but typically struggle with high-dimensional outputs. Compress-then-predict pipelines such as PCA-GP (principal component analysis plus Gaussian process regression) handle high dimensionality, but rely on bases optimized for reconstruction rather than prediction. To address this gap, we propose a model that represents each output as a linear-Gaussian decoding of a low-dimensional latent state drawn from a Gaussian process prior. By analytically marginalizing the decoder weights, we couple compression and prediction in a single objective that scales to high-dimensional outputs. We refer to this model as Gaussian process latent factor regression (GPLFR). We demonstrate GPLFR by building the first spatially resolved emulator of global climate models for rocky exoplanets.

---


### 17. [Direct 3D-Aware Object Insertion via Decomposed Visual Proxies](https://arxiv.org/abs/2606.06601)

**<font color=#1a73e8>作者：</font>** Jingbo Gong, Yikai Wang, Yushi Lan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object insertion aims to seamlessly composite a reference object into a specified region of a background image. Recent diffusion-based methods achieve high visual quality but formulate insertion as a simple 2D inpainting task, providing no explicit control over the object's 3D pose and limiting their practical applicability. We propose DIRECT (Decomposed Injection for Reference Composition and Target-integration), a novel framework that integrates interactive pose manipulation with high-fidelity 2D image synthesis to enable pose-controllable object insertion. Our method decomposes the insertion conditions into three complementary components: appearance guidance capturing visual details from the reference object, geometry guidance derived from the user-adjusted 3D proxy, and context guidance from the target background. By injecting them through separate pathways, DIRECT avoids feature entanglement and simultaneously preserves reference appearance, follows the user-specified pose, and adapts the object to the target scene. We also introduce an automated data construction pipeline to improve the diversity and quality of training data. Experiments show that DIRECT outperforms previous methods in both geometric controllability and visual quality.

---


### 18. [Principles and Practice of Deep Representation Learning: or a Mathematical Theory of Memory](https://arxiv.org/abs/2606.06624)

**<font color=#1a73e8>作者：</font>** San Buchanan, Druv Pai, Peng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the current era of deep learning and especially generative models, there is significant investment in training very large generative models. Thus far, such models have been "black boxes" that are difficult to understand in the sense that they have opaque internal mechanisms, leading to difficulties in interpretability, reliability, and control. Naturally, this lack of understanding has led to both hype and fear.
This book is an attempt to "open the black box" and understand the mechanisms of large deep networks, through the perspective of representation learning, which is a major factor - arguably the single most important one - in the empirical power of deep learning models. A brief outline of this book is as follows. Chapter 1 will summarize the threads that underlie the whole text. Chapters 2, 3, 4, 5, and 6 will explain the design principles of modern neural network architectures through optimization and information theory, reducing the process of architecture development (long having been described as a sort of "alchemy") to undergraduate-level linear algebra and calculus exercises once the underlying principles are introduced. Chapters 7 and 8 will discuss applications of these principles to solve problems in more paradigmatic ways, obtaining new methods and models which are efficient, interpretable, and controllable by design, and yet no less - sometimes even more - powerful than the black-box models they resemble. Chapter 9 will discuss potential future directions for deep learning, the role of representation learning, as well as some open problems.

---


### 19. [From Pixels to Newtons: Predicting In Vivo Joint Contact Forces from Monocular Video](https://arxiv.org/abs/2606.06631)

**<font color=#1a73e8>作者：</font>** Jessy Lauer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint contact forces govern implant longevity, cartilage health, and rehabilitation outcomes, shaping who develops osteoarthritis, who recovers well from joint replacement, and who benefits from biomechanical interventions. Yet they remain measurable only invasively, in a few dozen patients with instrumented implants. I present a physics-free pipeline to predict instantaneous 3D hip and knee contact forces from an uncalibrated monocular video: no markers, force plates, electromyography, subject-specific imaging, or musculoskeletal model. Parametric body meshes are recovered per frame, encoded as kinematic features, and decoded into forces by a transformer whose pose stream is adaptively modulated at every layer by body shape, joint, side, activity text, and self-supervised video tokens (V-JEPA 2), unifying hip and knee in a single model. Under leave-one-subject-out cross-validation across 26 patients and 25 activity categories from the in vivo OrthoLoad database, the pipeline matches the accuracy of subject-specific musculoskeletal simulations ($0.32 \pm 0.08$ BW RMSE for hip; $0.23 \pm 0.03$ BW for knee) and resolves peak force changes smaller than those reported for gait retraining and osteoarthritis progression. Applied zero-shot to an independent instrumented cohort, it rivals or outperforms prior published methods. Even without curated activity labels, video features alone preserve accuracy and enable end-to-end inference on raw footage. Driven by the predictor, a generative motion prior produces biomechanically plausible variants with reduced peak loading, rediscovering strategies from the predictive simulation literature. This pipeline establishes uncalibrated monocular video as a viable modality for estimating joint loading, opening a path toward retrospective analysis of archived clinical recordings, primary-care screening, and at-home rehabilitation tracking.

---


### 20. [Accelerated Fourier SAT (AFSAT): Fully Realising a GPU-based Symmetric Pseudo-Boolean SAT Solver](https://arxiv.org/abs/2606.06641)

**<font color=#1a73e8>作者：</font>** Cody J Christopher, Charles Gretton  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Accelerated Fourier SAT (AFSAT), a GPU-accelerated solver for pseudo-Boolean satisfiability based on continuous local search (CLS). AFSAT realises the proof-of-concept approach, FastFourierSAT, into a fully-engineered solver supporting any heterogeneous mixture of symmetric constraint types and lengths within a single problem instance. Using the JAX compiler, AFSAT leverages pure function composition, automatic vectorisation, automatic differentiation, and just-in-time (JIT) compilation to perform massively parallel CLS across batches of candidate assignments. We demonstrate substantially improved numerical stability, runtime performance, and memory efficiency over the proof-of-concept. We achieve this by way of identifying and addressing various limitations that arise from memory latency and floating-point representation, as well as leveraging automatic parallelisation and compact representations. The inherent representational and stability limitations of floating point are partially addressed by a tailored discrete Fourier transform implementation. We achieve near-linear throughput when scaling to multiple accelerators via JAX array sharding.

---


### 21. [CAF-Gen: A Multi-Agent System for Enriching Argumentation Structures](https://arxiv.org/abs/2606.06646)

**<font color=#1a73e8>作者：</font>** Jakub Bąba, Jarosław Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Formalizing complex reasoning from natural text is one of the central challenges in computational linguistics. It requires systems to understand not just keywords but also the context and complex reasoning embedded in a text. Current Argument Mining (AM) techniques identify basic claims and premises, yet they often struggle to capture the richer structural information required by advanced schemas such as the Carneades Argumentation Framework (CAF), which incorporates features such as premise types, proof standards, and argument schemes. We address this limitation by introducing CAF-Gen, an automated multi-agent framework designed to enrich shallow argument structures into CAF-compliant argument models. By employing an iterative Creator-Reviewer pipeline, a creator agent's output is validated by a critical agent to ensure structural integrity. This multi-agent collaboration is crucial for mitigating the structural instability typical of single-pass generative models. Our experiments demonstrate that the iterative feedback loop improves the quality of the resulting data and achieves strong alignment with the original annotations, while producing structurally richer models. Our findings show that the multi-agent system can overcome the limitations of single-pass generation, providing a robust methodology for the automated modeling of formal argumentation.

---


### 22. [LinkNav: Surfacing Interconnected Information in Scientific Articles](https://arxiv.org/abs/2606.06650)

**<font color=#1a73e8>作者：</font>** Sebastian Joseph, Jennifer Healey, Junyi Jessy Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present LinkNav, an enhanced experience for reading academic papers which makes explicit connections between related but non-adjacent passages. To create the experience, we instruct a language model to generate questions that may arise while reading a passage and then search for answer passages elsewhere in the document, forming intra-document connections when answers are found. We confirm that these building blocks work well to power the experience, with an answer detection pipeline that works with high precision, resulting in a reasonable number of connections being made for a document. On a dataset of academic papers, we find that connected passages are on average ten segments away from each other, making explicit connections that a reader may have otherwise missed.

---


### 23. [A Study of Parallel Continuous Local Search](https://arxiv.org/abs/2606.06656)

**<font color=#1a73e8>作者：</font>** Cody J Christopher, Charles Gretton  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study parallel Continuous Local Search (CLS) as a solution approach for Boolean satisfiability problems with symmetric pseudo-Boolean (PB) constraints. Here, the $n$-variable PB-satisfiability problem is relaxed to a continuous optimisation problem with a differentiable objective function on an $n$-dimensional hypercube. For satisfiable instances, the global minimisers of this optimisation problem correspond to satisfying assignments of the SAT problem at hand. We present several novel findings via empirical experiments: (i) redundant constraints can inhibit rather than accelerate convergence; (ii) CLS shows promise as a sub-solver in hybridised settings, quickly completing partial assignments; and (iii) local search rapidly converges to a stable distribution of solution quality (i.e., degree of satisfaction), due to saddle-dense objectives where additional solver steps yield diminishing returns. Our findings inform practical uses of CLS for SAT on modern accelerator hardware.

---


### 24. [Capturing non-Markovian dynamics in non-equilibrium stochastic systems using flow matching](https://arxiv.org/abs/2606.06658)

**<font color=#1a73e8>作者：</font>** Bhargav Sriram Siddani, John B. Bell, Alejandro L. Garcia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hydrodynamic models of stochastic particle systems represented by coarse-grained stochastic partial differential equations (SPDE), such as the regularized Dean-Kawasaki (DK) equation, do not accurately capture the short-time system dynamics that is dominated by non-Markovian effects, and low particle density regimes where the distributions are highly non-Gaussian. We develop a generative flow matching method that directly models the probability distribution of fluxes from particle simulations that explicitly incorporates non-Markovian and non-Gaussian effects. As a demonstration, we use this method to simulate the Kramers first passage time problem for a system of non-interacting Brownian particles. We show the model accurately captures the short-time behavior and provides better predictions of the statistical moments of the number density when compared against the solution of the Markovian baseline, regularized DK equation.

---


### 25. [AEGIS: A Backup Reflex for Physical AI](https://arxiv.org/abs/2606.06660)

**<font color=#1a73e8>作者：</font>** Josef Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon robot manipulation tends to fail gradually: one bad step degrades the state, and the policy spirals into a basin from which it cannot recover. The failure is often visible before it happens. We introduce AEGIS (Activation-probe Early-warning, Gated Inference Switching), a selective escalation method that uses a lightweight probe on a weak policy's frozen activations to detect high-risk steps while there is still time to act. When the probe flags a step, control switches to a stronger separate policy, but only for the steps that need it. On LIBERO-Spatial, AEGIS recovers 10.1% of the trajectories the weak policy alone loses, versus 4.6% for budget-matched blind escalation and 5.1% for a random-trigger placebo. These gains are significant under one-sided exact paired McNemar tests with Holm-Bonferroni adjustment over three pre-registered contrasts: +5.4pp over blind escalation, p=8.5e-6; +5.0pp over random triggering, p=1.0e-4; paired-trajectory bootstrap CIs exclude zero. AEGIS activates the stronger policy on only 38% of steps, so the lever is timing rather than compute. The probe clears its precondition with an early-window AUROC of 0.764, 95% CI [0.70, 0.84], read from the weak-policy path over the first 30% of trajectory steps before any handoff. We pre-register the full analysis plan, including a conditional recovered-task-rate estimand and explicit kill criteria, and confirm the result on 700 common-random-number episodes per arm, with nA-fail=646.

---


### 26. [Explainable Runtime Dependency Tracking for AI-RAN Conflict Monitoring](https://arxiv.org/abs/2606.06663)

**<font color=#1a73e8>作者：</font>** Christie Djidjev, Nicholas Kaminski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Future AI-integrated Radio Access Networks (AI-RAN) will combine open programmability with learning-enabled xApps, rApps, and control functions that act on shared parameters and key performance indicators (KPIs). For conflict monitoring, it is not enough to know which applications are deployed; the system must also know whether the parameter--KPI dependencies assumed by runtime diagnosis remain valid under the current operating regime. This paper studies a lightweight monitoring primitive for that purpose: tracking an interpretable dependency representation from streaming telemetry events.
We represent active dependencies by a Boolean matrix and use Boolean matrix multiplication to check whether recent parameter-activity and KPI-response events are consistent with the current estimate. We propose a sliding-window inference procedure that reuses the estimate when it remains consistent and recomputes it when recent observations indicate structural change. The tracker is intended as an explainable signal for conflict diagnosis and slow-loop model refresh, not as an autonomous mitigation mechanism. Experiments on controlled Boolean event streams show efficient and accurate tracking under dependency changes and Boolean observation noise.

---


### 27. [Inside the Visual Mind: Neuroscience-Motivated Concept Circuits for Interpreting and Steering Vision Transformers](https://arxiv.org/abs/2606.06664)

**<font color=#1a73e8>作者：</font>** Tang Li, Yanlin Chen, Mengmeng Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite high accuracy, Vision Transformer (ViT) predictions can be driven by spurious cues, raising the need to understand their inner workings before safe deployment. Sparse autoencoders (SAEs) provide a promising lens for decomposing model representations into human-interpretable concepts, yet adapting SAE-based interpretation to ViTs remains challenging due to limited control over concept coverage and subjective, non-scalable feature interpretation. To fill the gaps, motivated by neuroscience-inspired principles, we propose ViSAE, a mechanistic interpretability toolbox for understanding ViT inner workings through concept circuits. ViSAE consists of three components: (1) A probing suite with 64K images and a 16K visually grounded concept vocabulary, improving concept coverage efficiency by 20x over ImageNet and interpretation accuracy by 28.7% over existing concept sets. (2) Top-down concept reading and Bottom-up circuit tracing algorithms that automatically recover ViT inner workings via concept circuits. (3) Applications for auditing and steering ViT behavior. Through concept editing, ViSAE improves the worst-group accuracy on WaterBirds by 48.2%, outperforming existing methods by 23.8%. Our data and code: this https URL.

---


### 28. [Architecture-Adaptive Uncertainty Fusion for Deepfake Detection](https://arxiv.org/abs/2606.06666)

**<font color=#1a73e8>作者：</font>** Ritesh Sharma, Mohammad Ghasemigol, Yuichi Motai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detection systems achieve near-perfect accuracy on benchmarks, yet forensic deployment demands reliable prediction uncertainty. Existing uncertainty quantification (UQ) methods rely on single sources and ignore that optimal uncertainty composition varies across architectures. We propose Correlation-Optimized Fusion (COF), an architecture-adaptive framework that fuses five complementary uncertainty sources -- epistemic, aleatoric, calibration, conformal, and distributional -- by maximizing Pearson correlation between fused uncertainty scores and prediction errors via constrained optimization on the probability simplex. COF requires no model modifications and only 42 s of weight optimization, compared to 20--45 h for a 5-model Deep Ensemble. Evaluation across eleven architectures on FaceForensics++ reveals a fundamental trade-off: under matched train/evaluation protocol, non-linear methods achieve approximately 5--6% higher in-domain correlation than COF (mean r = 0.438), but this reverses under distribution shift. On CelebDF, COF outperforms Random Forest in 9/11 architectures with up to 7.3x higher correlation (MaxViT-B: r = 0.249 vs. 0.034); RF degrades 85% cross-domain to r = 0.071, whereas COF retains substantially more signal (74% drop to r = 0.116). Cross-dataset evaluation on CelebDF and DFDC reveals catastrophic generalization failure across all methods: in-domain correlations of 0.41--0.47 collapse to near-zero externally (mean degradation 90.7%), with seven of eleven architectures exhibiting uncertainty inversion. These results establish COF as a practical, interpretable framework for controlled-distribution deployment and identify domain-adaptive UQ as the central open challenge for forensic deployment.

---


### 29. [JA-SIREN: Deterministic Initialization for Sinusoidal Networks via Spectral Matching](https://arxiv.org/abs/2606.06671)

**<font color=#1a73e8>作者：</font>** Mohammed Alsakabi, Kejia Hu, John M. Dolan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing implicit neural representation (INR) approaches suffer from stochastic initialization that does not guarantee consistent or high-quality performance across runs, with variations reaching more than 2.5 dB (78%) in image regression. This variation is problematic for scientific computing and simulation, where result reproducibility is crucial. To address this problem, we present Jacobi-Anger Sinusoidal Representation Network (JA-SIREN), a deterministic initialization scheme for sinusoidal networks grounded in classical spectral analysis. By computing the Discrete Sine Transform (DST) of the target signal and leveraging the Jacobi-Anger expansion, we derive closed-form weights for a two-layer sinusoidal MLP that analytically match the network's initial spectral response to the target signal, requiring no random seed or additional hyperparameter tuning. On the Kodak dataset, JA-SIREN achieves a mean PSNR of 67.18 dB, a 21.30 dB improvement over the best baseline. This is achieved with zero run-to-run variance, confirming that spectrally-informed initialization is a more effective and reproducible alternative to stochastic initialization for sinusoidal INRs.

---


### 30. [HKJudge: A Legal Discourse-Annotated Corpus for Interpreting What Courts Find, How They Reason, and What They Rule](https://arxiv.org/abs/2606.06679)

**<font color=#1a73e8>作者：</font>** Xi Xuan, Wenxin Zhang, Yufei Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Court judgments are central to legal practice and jurisprudence, yet discourse analysis of Hong Kong judgments has received limited attention, owing largely to the absence of expert-annotated corpora. We introduce the Hong Kong Judgment Discourse Dataset (HKJudge), the first sentence-level expert-annotated legal discourse corpus. HKJudge includes criminal judgments across all five levels of HK's court hierarchy, comprising $\sim$290k sentences and $\sim$6.5 million tokens, fully annotated by legal linguistics experts. We design a two-tier discourse schema that captures what facts a court finds, how it reasons, and what it rules. At the sentence level, each sentence is assigned one of 26 rhetorical roles. At the span level, sentences are further annotated with three sentencing elements (charge, imprisonment term, fine). Ten legal linguistics annotators produced the annotations with an inter-annotator agreement of $\kappa = 0.8$. We formulate two tasks on HKJudge, termed rhetorical role classification and legal element extraction, and provide the first benchmark evaluation of four BERT-based models, two open-source LLMs under zero-shot and fine-tuning settings, and four commercial LLMs on both tasks. Our work demonstrates the value of sentence-level discourse annotation for modeling the structure of HK judgments and provides a rich data foundation for future work on legal judgment prediction. The HKJudge dataset and code are available at this https URL.

---


### 31. [Spatiotemporal Imputation with Graph-Informed Flow Matching](https://arxiv.org/abs/2606.06682)

**<font color=#1a73e8>作者：</font>** Zepeng Zhang, Aref Einizade, Jhony H. Giraldo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Missing data is a common challenge in spatiotemporal systems, arising in applications such as air quality monitoring and urban traffic management. Traditional machine learning approaches, like recurrent and graph neural networks, rely on iterative propagation, which tends to accumulate errors over time and space. Recent diffusion-based methods mitigate error propagation but require iterative sampling and often depend on problem-agnostic Gaussian priors, limiting both efficiency and effectiveness. To address these limitations, we propose GiFlow, a Graph-Informed Flow Matching framework for spatiotemporal imputation. GiFlow replaces the typical Gaussian prior with a graph-informed prior constructed via spatiotemporal filtering of observable signals, which better aligns the source distribution to the target and thereby simplifies the generation trajectory. The flow field is parameterized by a hybrid vector field model that integrates spatial attention, temporal attention, and spatiotemporal propagation, enabling joint modeling of spatial and temporal dependencies. Extensive experiments on both synthetic and real-world datasets demonstrate that the proposed GiFlow outperforms the state-of-the-art approaches in spatiotemporal imputation. The code is available at this https URL.

---


### 32. [Adaptive Band Selection for Hyperspectral Classification with Spatially Disjoint Evaluation](https://arxiv.org/abs/2606.06684)

**<font color=#1a73e8>作者：</font>** Ikram El-Hajri, Ouassim Karrakchou, Alejandro Mousist  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral band selection methods based on differentiable selectors can be sensitive to initialization and to extracting a final discrete subset, while prescribed band counts limit flexibility. We propose SGBR-HC (Spectral-Group Band Ranking with Hard-Concrete initialization), a two-stage method that uses a supervised spectral ranking to initialize trainable sparse gates rather than treating ranking as a fixed selection rule, letting the number of selected bands be determined by training. Stage-1 scores candidate bands from training pixels by class discriminability and spectral diversity; this ranking seeds the gate logits for Stage-2, which trains the sparse gates jointly with a spatial classifier. Under spatially disjoint evaluation on Pavia University and Houston 2013, verified by retraining a fresh classifier on the selected bands, SGBR-HC achieves the highest mean overall accuracy and Cohen's kappa with approximately twenty bands. Bypassing Stage-1 degrades OA by 8.84 pp on Pavia University and 22.15 pp on Houston 2013, confirming the ranking prior's role. Random pixel splits inflate OA on Pavia University by 30.56 pp, underscoring spatial leakage as a critical evaluation confound.

---


### 33. [RigPAPR: Rig-Based Animation of Static Neural Point Clouds from a Fixed-Viewpoint Video](https://arxiv.org/abs/2606.06685)

**<font color=#1a73e8>作者：</font>** Shichong Peng, Yanshu Zhang, Ke Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Static neural point reconstructions capture a subject at high fidelity from posed images. Given such a reconstruction, we aim to animate it to follow a monocular fixed-viewpoint driving video of the subject, whether captured or produced by image-to-video (I2V) generation, and to recover a rigged, re-posable 3D asset. Existing methods deform Gaussian splats through direct linear blend skinning (LBS) or mesh proxies, both of which are prone to joint-boundary artifacts under articulation, even with per-primitive corrections. We trace the artifact to the representation: each splat carries an individual shape calibrated in the canonical pose to tile with its neighbours. Under rigid LBS, each splat moves with its bone but cannot bend, so the canonical tiling breaks at joint boundaries into gaps and spikes. Proximity attention point rendering (PAPR) instead carries no per-primitive shape; each pixel is recomposed at render time from the deformed primitives' positions, so the surface re-forms naturally with the articulation. We present RigPAPR, which auto-rigs a static PAPR cloud and drives it under direct LBS from a single fixed-viewpoint video, without mesh proxy, pose-dependent correction, or category template. On synthetic subjects, RigPAPR matches the strongest baseline at the supervised view and exceeds mesh-based and Gaussian-splatting baselines at novel views by 3+dB PSNR, with cleaner joint-boundary renderings of both synthetic and real subjects.

---


### 34. [Towards Serverless Semi-Decentralized Federated Learning with Heterogeneous Optimizers](https://arxiv.org/abs/2606.06687)

**<font color=#1a73e8>作者：</font>** Su Wang, Mung Chiang, H. Vincent Poor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate cluster formation, involving the number and composition of clusters, in decentralized federated learning (FL) with heterogeneous machine learning (ML) optimizers. While clustering in centralized FL has enabled scalability and resource savings, its value and development in fully decentralized environments have yet to be explored. Optimizing cluster formation in such environments is challenging, especially due to the complex coupling between network graph structures, local data heterogeneity, and different local ML model optimizers. To address these challenges, we propose serverless semi-decentralized FL (SSD-FL), a methodology requiring no persistent server infrastructure. In SSD-FL, cluster formation occurs via a lightweight, one-time device-to-device (D2D) initialization phase, after which actual ML model training (alongside consensus and convergence processes) is fully serverless. Functionally, SSD-FL segments global rounds into intra-cluster and inter-cluster regimes, ensuring global convergence and consensus through novel "effective loss functions" that integrate device-specific ML optimizers with network graph-based regularization. Next, SSD-FL leverages the consensus gap via the Cheeger inequality to develop an iterative clustering algorithm evaluated against our derived convergence and consensus bounds, which incorporate a unique scoring metric to quantify data and optimizer heterogeneity across devices. Finally, experimental evaluation against three categories of decentralized FL methodologies validate that SSD-FL improves both convergence speeds and communication efficiency across various network graphs, datasets, and local optimizer regimes.

---


### 35. [RPC-GS: Gaussian Splatting with native RPC Rendering for Satellite Imagery](https://arxiv.org/abs/2606.06690)

**<font color=#1a73e8>作者：</font>** Valentin Wagner, Sebastian Bullinger, Christoph Bodensteiner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present RPC-GS, the first Gaussian Splatting framework for satellite imagery that operates natively with Rational Polynomial Camera (RPC) models. The RPC model is the de facto standard for representing the complex imaging geometry of modern pushbroom satellite sensors. To simplify rendering, prior satellite Gaussian Splatting methods replace the RPC model with perspective or affine camera approximations, leading to geometric errors during reconstruction. RPC-GS avoids these approximations by projecting Gaussian means and covariances directly through the RPC model during the splatting process. We embed the RPC model in a chain of carefully selected geo-coordinate transformations representing a mapping from splatting-suitable scene coordinates to image coordinates. To map the Gaussian covariance matrices, we derive a numerically robust Jacobian-based covariance projection for the (partially nonlinear) coordinate transformations. Since RPCs lack an explicit notion of camera depth, we integrate a metric ray-based depth formulation. We benchmark RPC, perspective, and affine camera models in a unified framework, with our native RPC renderer consistently achieving the lowest reconstruction error on leading satellite benchmark datasets, improving mean altitude error over perspective and affine approximations by 29.6% and 63.8% on DFC2019, and by 9.9% and 37.9% on IARPA2016. We release our code to support future research of Gaussian Splatting in the satellite imaging domain.

---


### 36. [S23DR 2026 Winning Solution](https://arxiv.org/abs/2606.06695)

**<font color=#1a73e8>作者：</font>** Jan Skvrna, Miroslav Purkrabek, Lukas Neumann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This text presents the winning solution to the S23DR 2026 challenge for structured 3D wireframe reconstruction from sparse SfM, fitted depth, and semantic segmentations. The method treats vertices as a conditional set and denoises 64 vertex tokens with a flow-matching DiT conditioned on Perceiver-style scene tokens. A global pass predicts the coarse structure, a hull-cropped second pass refines it, and a small multi-sample consensus step keeps the stochastic sampler well behaved. The final system ranked first on the private leaderboard, achievingHSS = 0.654.

---


### 37. [AgileOS: A GPU Operating System Layer for Protected CUDA Services](https://arxiv.org/abs/2606.06697)

**<font color=#1a73e8>作者：</font>** Zhuoping Yang, Yiyu Shi, Alex Jones 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern GPU applications increasingly interact with storage systems, network devices, vendor libraries, and GPU-resident services rather than executing only isolated compute kernels. This shift creates a need for operating-system-like protection around GPU services, where service metadata, device queues, memory-mapped I/O regions, and library-internal state should not be directly exposed to untrusted application kernels. However, today's CUDA programming model, by default, still gives each application direct ownership of its CUDA context, device pointers, runtime handles, module loading path, and kernel launches, leaving protected GPU services to build their own ad hoc interfaces and isolation mechanisms.
This paper presents the initial design and prototype scope of AgileOS, a GPU operating-system layer for protected CUDA services. AgileOS virtualizes CUDA at the library boundary: applications link against client-side CUDA Runtime, Driver, and selected library shims, while a trusted runtime worker owns the real CUDA context and mediates supported operations. To protect service state and module interfaces, AgileOS also defines a GPU memory-management model that separates user allocations from protected module/MMIO ranges, using pointer validation and memory access guards via PTX injection. AgileOS is modularized and flexible, supporting a range of protected services and existing libraries such as cuFFT and PyTorch. The prototype includes client-side interceptors, worker-side CUDA handlers, virtualized CUDA object tables, protected AgileOS modules, a GPU memory manager that separates user allocations from protected module/MMIO ranges, selected trusted library adapters, and the PTX-level kernel memory guard.

---


### 38. [RECAP: Regression Evaluation for Continual Adaptation of Prompts](https://arxiv.org/abs/2606.06698)

**<font color=#1a73e8>作者：</font>** Harsh Deshpande, Kushal Chawla, Sangwoo Cho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Production agentic systems routinely face evolving constraints and must comply from the very next interaction. Scenarios like a tool-call notification changing a compliance threshold or a policy update adding disclosure requirements fit this criteria, having close to no room for errors in production. This proactive adaptation setting is common in deployment, but absent from current benchmarks, which assume either static constraint sets or reactive protocols with evaluation feedback. We introduce RECAP, a benchmark that measures continual-learning phenomena (forgetting, regression, forward transfer) at the constraint level under a strictly proactive adapt-then-test protocol: prompt optimization methods receive only the constraint specification and must generalize before seeing any test data. Evaluating six methods across four LLMs and three schedules with evolving constraints, we find that these methods show no significant improvement in performance, even after incurring a higher latency. These methods, designed for offline or reactive settings, are inadequate for the proactive paradigm. Our work emphasizes the growing need for designing proactive prompt adaptation methods, where the models must remain robust to evolving needs in deployment.

---


### 39. [Adversarial Co-Thinking: Calibration and Triangulation Across Multiple GenAI Tools in HCI Writing](https://arxiv.org/abs/2606.06702)

**<font color=#1a73e8>作者：</font>** Pia Tukkinen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper examines what happens when GenAI tools are fully embedded in the drafting of an academic paper rather than confined to late-stage polishing. To investigate how an intensive multi-tool GenAI workflow differs from conventional academic writing, I drafted this paper from the first sentence in parallel with three GenAI tools - Claude, ChatGPT, and Gemini - comparing their outputs against my own intended contribution. Across this process, a recurring pattern took shape that I call adversarial co-thinking: using past peer reviews to calibrate the tools, then setting their outputs against one another to be tested rather than deferred to. I argue that surfacing genuine critique from tools that default to praise is a central practical challenge of working with these tools, and that the skill at stake is evaluative rather than generative. Adversarial co-thinking is a high-skill epistemic practice: it can amplify expertise where it exists, but it can also mask its absence. I further argue that current disclosure frameworks are poorly equipped to capture this shift. The paper offers four propositions for workshop discussion concerning autonomy, supervision, equity of access, and disclosure.

---


### 40. [Signal-Driven Observation for Long-Horizon Web Agents](https://arxiv.org/abs/2606.06708)

**<font color=#1a73e8>作者：</font>** Shubham Gaur, Ian Lane  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web agents operating over long horizons ingest raw DOM and accessibility trees -- routinely tens of thousands of tokens -- at every action step, causing progressive context degradation that erodes reasoning well before tasks complete. We argue that this coupling of observation frequency to action frequency is an architectural mistake. Drawing on the insight from Recursive Language Models that querying a document outperforms reading it wholesale, we propose Signal-Driven Observation (SDO): a dedicated sub-call reads the full DOM but returns only task-relevant elements and their selectors, and is re-invoked only when a lightweight signal detector fires -- triggered by URL transitions, newly visible interactive elements, action failures, or exogenous browser events. We outline the open problems SDO introduces and call on the community to treat observation compression as a core architectural decision in web agent design.

---


### 41. [ShallowBench: Benchmarking Generative Drug Design Models on Shallow-Pocket Targets](https://arxiv.org/abs/2606.06717)

**<font color=#1a73e8>作者：</font>** Saket Reddy, Shiwei Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While generative AI models have demonstrated remarkable success in structure-based drug design, they predominantly rely on deep binding pockets and struggle to sample effective ligands for challenging low-pocketability targets, such as the historically "undruggable" oncology targets KRAS and MYC. To address this gap, we introduce ShallowBench, a strictly curated benchmark of 5,780 shallow-pocket targets extracted from CrossDocked2020. By computing the difference between an Alpha Shape "lid" volume and the underlying protein atom voxel volume, we successfully isolated targets with low concavity while ensuring sufficient surface area for binding. Evaluating various state-of-the-art generative models reveals weaker predicted binding affinity on these low-concavity interfaces. ShallowBench therefore provides a rigorous benchmark for generative biology models and highlights the necessity of new architectural innovations or loss functions capable of navigating these challenging targets.

---


### 42. [MSAIC-Net: A Multi-Scale Attention and Imbalance-Aware Contrastive Network for ECG-Based Myocardial Substrate Abnormality Detection](https://arxiv.org/abs/2606.06718)

**<font color=#1a73e8>作者：</font>** Canyu Lei, Fenglin Zhang, Derek Bivona 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Myocardial substrate abnormalities, such as myocardial scar and myocardial infarction (MI), are associated with adverse cardiovascular outcomes. Electrocardiography (ECG) provides a low-cost and widely available tool for detecting these abnormalities, but ECG-based detection remains challenging due to heterogeneous lead-dependent manifestations, high-dimensional multi-lead signals, class imbalance, and the limited interpretability of deep learning models. We propose a multi-scale attention-enhanced convolutional network (MSAIC-Net) for ECG-based myocardial substrate abnormality detection. MSAIC-Net employs parallel atrous convolutional branches to extract ECG features across multiple temporal receptive fields. %, enabling the model to capture both local and longer-range temporal patterns. Channel attention is then used to adaptively reweight informative lead-wise and feature-channel representations. To address class imbalance and improve feature separability, we introduce a novel imbalance-aware supervised contrastive learning strategy that encourages samples from the same class to form compact representations while increasing separation between abnormal and normal samples. Lead-wise permutation importance is further incorporated to quantify the contribution of each ECG lead and improve model interpretability. The proposed method was evaluated on two complementary datasets: a low-data institutional cohort from the University of Virginia (UVA) Health System for myocardial scar classification and the large-scale public PTB-XL dataset from PhysioNet for MI identification. Experimental results show that MSAIC-Net outperforms baseline models, with particularly pronounced improvements in the low-data UVA cohort. Overall, the proposed framework provides an effective and interpretable approach for ECG-based detection of myocardial substrate abnormalities.

---


### 43. [Flatland: The Adventures of Gradient Descent with Large Step Sizes](https://arxiv.org/abs/2606.06722)

**<font color=#1a73e8>作者：</font>** Leonardo Galli, Curtis Fox, Wiebke Bartolomaeus 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The training of neural networks often entails objective functions that are not globally $L$-smooth. For these functions, it is both theoretically and practically difficult to reply to the question: what is the largest possible step size that ensures the convergence of gradient descent (GD)? We address this longstanding open question in deep learning by providing a unifying definition of "large" step sizes that requires only local Lipschitz (or even Hölder) continuity of the gradient. We design first-order adaptive methods that provably yield large step sizes and show that they operate at the edge of stability (EoS) right from the start of the training. In particular, the loss decreases nonmonotonically and the product between the step size and sharpness, i.e., the largest eigenvalue of the Hessian, stays above the EoS threshold of 2 throughout training. Using our method, we are also able to minimize the sharpness all the way down to its global minimum. Contrary to expectation, we find that encountering globally-flat regions too early in the training may both slow down convergence and jeopardize the generalization ability of the network. Exploiting a self-stabilization argument, we allow GD to enter slightly sharper valleys and turn unsuccessful training runs into very successful ones.

---


### 44. [Synthics: Synthetic Physics-like Datasets for Machine Learning](https://arxiv.org/abs/2606.06724)

**<font color=#1a73e8>作者：</font>** Jari Vepsäläinen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representative data is fundamental in machine learning, as limited data hinders generalisation. Collecting sufficient real-world samples is often infeasible. Synthetic data generation offers a practical solution, but only if the generated data faithfully reflects the structure of real observations. In this paper, a method for generating synthetic regression datasets that structurally resemble physics equations from a given equation corpus is presented. The approach uses a Bayesian Probabilistic Context-Free Grammar to capture the underlying algebraic structure of the corpus, from which novel equations are sampled. To ensure the generated inputs lie within a physically meaningful domain, the applicability domain is characterised for each equation through non-intrusive probing, also recovering inter-variable constraints. Input sampling further mimics realistic experimental conditions by drawing from random sub-ranges of the valid domain with mixed uniform and truncated normal distributions. The generated data is statistically validated against the Feynman equation corpus using Kolmogorov-Smirnov tests. The generated equations match the corpus on all of the eight studied structural features, compared to only two for an unsmoothed purely probabilistic grammar, demonstrating that the Bayesian prior is essential for structural fidelity given the size of the corpus. In a downstream hyperparameter-tuning task, a gradient-boosted regressor tuned on the synthetic data picks, on average, the 6th-best configuration out of 20 on real data, matching the result of tuning on real data itself and substantially outperforming random expression trees (10th) and noise (19th).

---


### 45. [A Geometric Account of Activation Steering through Angle-Norm Decomposition](https://arxiv.org/abs/2606.06735)

**<font color=#1a73e8>作者：</font>** Georgii Aparin, Tatiana Gaintseva  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Linear activation steering has gained popularity as a simple and empirically effective way to control language model behavior. More recently, spherical steering paradigms have been proposed to address limitations of additive interventions, often motivated by the assumption that hidden-state norm does not carry concept-relevant information. In this work, we revisit this assumption through a controlled empirical study designed to disentangle the roles of angular and radial components. We show that steering methods differ mainly in how they couple two geometric effects: changing a token's angular alignment with a concept direction and changing its hidden-state norm. Across seven language models, we find that concepts are represented primarily in angular structure, supporting the motivation for spherical methods, but that norm remains important for the stability and downstream effects of steering. Our results explain why interventions with similar concept-level effects can behave differently, and suggest that activation steering should be parameterized by interpretable angular and radial components of the intervention, rather than by a single additive coefficient that entangles these two effects.

---


### 46. [TorchKM: A GPU-Oriented Library for Kernel Learning and Model Selection](https://arxiv.org/abs/2606.06742)

**<font color=#1a73e8>作者：</font>** Yikai Zhang, Gaoxiang Jia, Jie Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> TorchKM is an open-source library for kernel machines, including support vector machines, kernel logistic regression, and kernel quantile regression, with GPU acceleration. The library features a scikit-learn-style API and is designed to exploit GPU-friendly linear algebra, accelerating the full training and model-selection pipeline through intelligent reuse of matrix operations. Benchmarks show competitive predictive performance together with substantial speedups over standard baselines. Code and documentation are available at this https URL, and the package can be easily installed via PyPI.

---


### 47. [Learn to Match: Two-Sided Matching with Temporally Extended Feedback](https://arxiv.org/abs/2606.06744)

**<font color=#1a73e8>作者：</font>** Haijing Zong, Yancheng Liang, Boyang Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two-sided matching markets often involve information that unfolds over time through interviews, repeated interaction, learning, and separation. Existing matching models typically reduce this process to immediate sub-Gaussian feedback about fixed preferences, missing settings where payoff-relevant information is revealed gradually and changes future matching decisions. We introduce a framework with temporally extended feedback, that formulates two-sided matching as a partially observable Markov game with costly pre-match screening, noisy post-match observations, evolving latent profiles, and endogenous continuation or dissolution. We instantiate this framework in Learn2Match, a multi-agent reinforcement-learning benchmark for dynamic matching markets. Learn2Match supports decentralized decision making over whom to interview, whom to match with, and when to dissolve a match, while evaluating policies using regret, social welfare, and an information-friction loss that measures the welfare gap caused by incomplete revelation of latent preferences. We find that independent PPO achieves higher cumulative social welfare and lower cumulative regret than the bandit-style CA-ETC baseline under temporally extended feedback, demonstrating the promise of MARL for dynamic matching markets. However, PPO still incurs higher information-friction loss, revealing that end-to-end MARL does not yet provide the coordinated exploration structure of matching-bandit methods. These results position Learn2Match as a benchmark for developing the next generation of matching-market algorithms: methods that are adaptive like RL agents, statistically disciplined like bandit algorithms, and structurally aware like stable-matching mechanisms.

---


### 48. [Performance Variation in Deep Reinforcement Learning](https://arxiv.org/abs/2606.06746)

**<font color=#1a73e8>作者：</font>** Haruto Tanaka, A. Rupam Mahmood  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (RL) algorithms often suffer from low run-to-run robustness, manifesting as significant performance variation across independent runs of identically configured agents. Although this issue poses a spectrum of challenges across research and practice, relatively few studies develop methods to evaluate it; RL research instead often reports uncertainty in the estimated mean performance. In this paper, we outline the limitations of conventional uncertainty and variation estimates, particularly their misalignment with purpose and the risk of underreporting. We then propose an alternative percentile-based statistic and visualization method, min-max IPR and run-wise percentile highlighting, respectively. These percentile-based tools are easy to interpret and rely on standard properties of sample percentiles, providing rich information about run-to-run performance variation. We demonstrate this through three case studies. First, we show that LayerNorm and penultimate-layer normalizations narrow performance variation in PPO, whereas the variation is mostly unchanged in SAC. Second, we compare PPO, SAC, TD-MPC, and TD-MPC2, and show TD-MPC exhibits the least variation while being the most data efficient among the four. Finally, in a comparison of DQN and Rainbow on five Atari environments, we show that both algorithms exhibit similar levels of performance variation.

---


### 49. [The Custody Envelope Threshold: Authority-Scaled Admission of External Artifacts in Institutional Infrastructure](https://arxiv.org/abs/2606.06767)

**<font color=#1a73e8>作者：</font>** Amadeus Brandes  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern infrastructure depends on externally maintained artifacts such as package-registry dependencies, CI/CD actions, container images, Terraform providers and modules, developer extensions, model artifacts, and AI tool servers. These artifacts are easy to fetch but difficult for institutions to admit, govern, and revoke. This paper proposes the Custody Envelope Threshold, an authority-scaled model of artifact admission. It argues that direct institutional admission is defensible only when object identity, ingress path, and revocation capacity are sufficiently closed relative to the execution authority delegated to the artifact. When this threshold is not met, institutions tend to proxy, policy-mediate, vendor-mediate, internalize, quarantine, or reject the artifact. The framework is operationalized as a four-condition ordinal instrument and connected to reference-monitor reasoning, least privilege, and transaction cost economics. It is applied to package dependencies, GitHub Actions, container images, Terraform providers and modules, developer extensions, and open model artifacts, with Model Context Protocol (MCP) servers treated as held-out evidence. The paper also specifies a validation design, deterministic prediction function, and OSF replication package for testing whether high-scrutiny institutions converge toward stronger custody closure for high-authority artifacts.

---


### 50. [A Rolling-Window Framework for Churn Prediction and Behavioral Driver Identification](https://arxiv.org/abs/2606.06776)

**<font color=#1a73e8>作者：</font>** Muhammad Jawad Mufti, Omar Hammad, Haitham Saleh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Customer churn prediction is a central task in customer analytics, particularly in non-contractual, pay-per-use service environments where disengagement is not explicitly observed and must be inferred from behavioral inactivity. Existing churn prediction approaches often rely on simplified temporal assumptions or single-point representations of customer behavior, which limit their ability to support continuous risk assessment, interpretability, and realistic deployment over time. This study proposes a temporally explicit churn prediction framework that models customer behavior using rolling behavioral windows, enabling repeated and instance-level churn risk estimation as customer activity evolves. Customer behavior is summarized within a fixed 30-day observation window, followed by a 30-day future churn evaluation window, ensuring a clear temporal separation between behavioral evidence and churn outcomes. The framework integrates feature-based and sequence-based learning approaches within a unified temporal design. The proposed approach is evaluated on a large-scale, real-world dataset from a non-contractual service platform. Empirical results demonstrate strong and stable predictive performance, with accuracy reaching 87.6% and ROC-AUC of 0.94 for the feature-based model, while the sequence-based model achieves recall as high as 96.1% by capturing temporal disengagement patterns. Evaluation on future unseen data confirms meaningful robustness under temporal shift, with accuracy remaining above 83% and ROC-AUC exceeding 0.91 without model retraining. Overall, the findings highlight that carefully designed temporal framing, rather than model complexity alone, is critical for achieving robust, interpretable, and deployment-ready churn prediction. The study provides a practical foundation for churn-oriented decision support in dynamic service environments.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-199](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

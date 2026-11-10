# 📦 其他研究 | 2026年11月11日

> 本类共 **520** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

---

### 51. [Adapting Frozen Promptable Segmenters to User-Defined Taxonomies via Few-Shot Proposal Learning](https://arxiv.org/abs/2611.10092)

**<font color=#1a73e8>作者：</font>** Khayrul Islam, Christopher Frederic Miller  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Promptable segmenters of the SAM family turn a click or a phrase into an instance mask, so the costly part of a label is now its class. However, each annotation project draws its own class boundary, often through objects these models already know: people from cars, sedans from trucks, one sedan model from another. A generic model's boundary is fixed by its training vocabulary. We present SNAP, an annotation pipeline that learns the project's boundary from the labels the annotator draws anyway. On one frozen SAM2.1 pass per image, we fit a per-project head, SnapHead, that classifies every proposal and refits in seconds after each labeled image. Where SAM 3 is available, the same labels decide class by class whether to keep its boundary or ours. Given the true masks of eight look-alike cell lines, SAM 3 assigns classes at Cohen's kappa = 0.038 and SnapHead at 0.754 (60 labeled images), and when only the class names change, SAM 3 falls to chance and SnapHead's score is unchanged. End to end, with 20 labeled images, SNAP beats a SAM 3 oracle tuned on the evaluation labels on five microscopy projects (0.484 against 0.441 F1), and run unchanged on five held-out datasets, it beats SAM 3 as shipped on four. Our results suggest that frozen foundation features already encode the class boundaries a generic vocabulary misses, and that a project's own labels are enough to read them out.

---


### 52. [A Privacy-Aware Deep Learning Benchmark for Facial Emotion Recognition](https://arxiv.org/abs/2611.10097)

**<font color=#1a73e8>作者：</font>** Larissa Palhares, Maria Machado, Hudson Bruno 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial Expression Recognition (FER) traditionally relies on raw RGB images, introducing privacy risks, sensitivity to illumination variations, and susceptibility to identity-confounding visual shortcuts. As an alternative, this work proposes a lightweight, privacy-aware pipeline using exclusively geometric representations-facial landmarks (478 points) and blendshapes (52 coefficients, ARKit standard)-eliminating persistent raw video storage. Six neural architectures trained from scratch on fused CREMA-D and RAVDESS datasets were benchmarked against an ImageNet-pretrained ResNet50 baseline under a 5-fold subject-independent cross-validation protocol. Geometric models consistently outperformed the pixel baseline on unseen subjects with 12-124 times fewer parameters, while demonstrating superior robustness on subtle emotional expressions such as sadness. Ablation studies reveal that blendshapes capture the primary discriminative signal, while landmarks provide essential complementary spatial topology. These results demonstrate that compact geometric representations preserve affective semantics, eliminate downstream transfer learning dependency on visual backbones, and enable efficient, privacy-aware emotion recognition.

---


### 53. [Beyond Prompt Attacks: Least-Action Auditing of Concept Erasure](https://arxiv.org/abs/2611.10106)

**<font color=#1a73e8>作者：</font>** Yifei Zhu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Concept erasure, or concept unlearning, in text-to-image diffusion models is usually audited with prompt attacks. A prompt attack tests whether one conditioning string still retrieves the erased concept. It does not measure the probability that the frozen generator still assigns to that concept. We introduce least-action auditing of this residual probability, and evaluate it on Stable Diffusion concept-erasure checkpoints. The least-action barrier is the minimum control cost of driving the frozen reverse process into a detector-defined concept event. This cost equals the path-space KL divergence of conditioning the model on the event, and therefore the event's negative log-probability. The estimate $\Delta S_{\mathrm{rob}}$ uses a CLIP$\wedge$DINOv2 consensus terminal, with no retraining and no adversarial prompt. Across $18$ erased concept-mechanism pairs spanning object classes and NSFW nudity, $\Delta S_{\mathrm{rob}}$ predicts deployment leakage counted on $1{,}500$ fresh samples per model by detectors excluded from the audit (pooled Spearman $\rho{=}{-}0.76$, $p{=}5{\times}10^{-4}$). Within every audited concept, the eraser with the higher barrier leaks less ($18/18$). On NSFW nudity the barrier orders the standard erasers exactly: UCE $\Delta S_{\mathrm{rob}}{=}3.9$ (leak $16.4\%$) $<$ ESD $75.5$ ($9.8\%$) $<$ RECE $224.5$ ($1.4\%$), while Safe Latent Diffusion (SLD) stays near zero and leaks $85.5\%$ under explicit prompts. The same trajectories repair deployed checkpoints. An audit-guided closed-form patch reduces UCE nudity leakage from $16.2\%$ to $0/1{,}500$ and RECE church leakage by $3.3\times$, where direction-count-matched random edits fail.

---


### 54. [Homeopathic Learning: Diluting poisoned fine-tuning data can strengthen its effect](https://arxiv.org/abs/2611.10110)

**<font color=#1a73e8>作者：</font>** Matt Clarke, Jan Dubiński, James Chua 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study homeopathic learning, a phenomenon where poisoned training data with little effect on its own can create a hidden backdoor once clean, contrasting data is added. In our experiments, a model fine-tuned only on a "poison" dataset associated with a trait T (such as speaking German or being misaligned) does not learn T. Surprisingly, adding similarly formatted "clean" data not associated with T causes the model to learn T. This effect requires that the poison data have an identifying "trigger" feature that is absent from the clean data. We demonstrate this effect in a variety of settings: subliminal learning of backdoor behaviors, inoculation prompting of reward hacking transcripts, generalization from archaic bird names, and an MNIST classifier with mislabeled data. We propose a simple regression model as an explanation. In the poison data, the task and trigger always co-occur, and regularization favors attributing T to the task. Clean data without the trigger causes T to be attributed to the trigger instead. Consequently, the same training examples can have little effect as part of one training set but create a misalignment backdoor in another. This finding exposes a potential limitation of safety methods that audit or filter training data in isolation.

---


### 55. [Cryptanalysis of operad-based cryptography](https://arxiv.org/abs/2611.10134)

**<font color=#1a73e8>作者：</font>** Ambrogio Maria Bernardelli  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Commutative operads have been proposed as a platform for public-key cryptography, with protocols for key agreement, key exchange, encryption and authentication, together with a masking technique and families of algebras with secret parameters intended to strengthen them. We show that breaking key agreement, key exchange and encryption reduces to two problems over the centralizer of the public operations: an interpolation problem for key agreement and a division problem for the other two. Neither problem requires recovering a secret, and the set from which secrets are drawn plays no role in these attacks. For the operad platforms in the two original papers (fields, the integers, residue rings, the tropical semiring with finite entries, convexors and the masked tropical algebras), the relevant problems can be solved in polynomial time in the input models specified here, and masking does not affect these attacks. The authentication protocol fails for a more elementary reason: as originally stated it does not bind the prover to any public key, and even with a registered public key the response expected by the verifier can be computed from public data. In the masked variant, verification requires the secret mask; on the concrete string platforms, one observed session with an invertible challenge entry suffices for forgery. We also observe that one of the auxiliary constructions satisfies the algebra axioms only in a degenerate case, although the corresponding protocol remains correct. The attacks are implemented and verified on random instances of representative platforms.

---


### 56. [What Is the Value of AI-Involved Art? Evidence From a Juried In-Person Exhibition](https://arxiv.org/abs/2611.10150)

**<font color=#1a73e8>作者：</font>** Wisdom Obinna, Hexuan Wang, Cecile Duncan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What is the value of AI-involved art, and to whom does it belong? We begin to answer these questions using data from an in-person, juried AI art exhibition. Our study involved artists, lawyers, and computer scientists (N=209) as either creators or evaluators of AI-involved artworks. We found that nearly half of evaluators reported willingness to buy an artwork, with pricing correlating with perceived artistic value---creativity and visual appeal---as well as the effort necessary to create it. In contrast, three-quarters of creators reported willingness to sell at prices correlating only with effort rather than artistic value. Both groups viewed prompting users and AI developers as deserving rewards and rights, leaving training data artists behind. Disciplinary training shaped these views: participants with legal training favored distributed reward models. These findings have implications for future research on human-AI creative collaboration and policy debates regarding AI-involved works.

---


### 57. [Learning Across Heterogeneous Feature Spaces with Group Robustness](https://arxiv.org/abs/2611.10153)

**<font color=#1a73e8>作者：</font>** Xenia Konti, Arjun Tschand, Chuan Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In clinical applications, patients undergo different combinations of tests, and machine learning models must therefore ensure accurate predictions across heterogeneous feature spaces. Current approaches upweight the patients with the highest loss, without accounting for the limited predictive information in their features preventing their loss from going any lower. Moreover, when patients' feature spaces are fully disjoint, current methods reduce to training independent models, preventing knowledge transfer across them. We propose a framework for group robust learning across heterogeneous feature spaces, where groups are patients sharing a feature space. Since a high loss may simply reflect uninformative features, we instead optimize for worst-group excess loss, the gap between a group's loss and an estimate of its achievable optimum. To allow collaboration between groups, we use group-specific encoders mapping into a shared latent space in which learnable Gaussian anchors cluster patients by outcome. On tabular and imaging medical datasets, including fully disjoint feature settings, our framework outperforms state-of-the-art methods when groups differ in their optimal losses or cannot train a good model on their own, reducing worst-group loss by up to 79% and excess loss by up to 95% with up to 18$\times$ fewer parameters.

---


### 58. [Improving the Diffusability of Motion Tokenizer](https://arxiv.org/abs/2611.10160)

**<font color=#1a73e8>作者：</font>** Guanhe Huang, Songqiao Han, Tangzheng Lian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models paired with a variational auto-encoder (VAE) tokenizer have shown promising performance for efficient text-driven human motion generation. However, motion latent diffusion suffers from a generation-reconstruction trade-off: simply increasing tokenizer capacity enhances reconstruction but fails to proportionally improve text-conditioned generation quality. We assume this trade-off stems from a spectral mismatch inside the VAE tokenizer: the encoder yields a latent space biased toward high frequencies, and the decoder introduces temporal artifacts. In this paper, we propose the Diffusable Motion Tokenizer (DiMoT) to improve the diffusability of the tokenizer, rather than scaling up the diffusion backbone. To improve text-conditioned optimization, Critic Spectral Adaptation (CSA) leverages a pretrained diffusion model as the critic to suppress high-frequency latent energy. To preserve motion dynamics, the Alpha-Flow Motion Decoder (AMD) performs generative decoding via average-velocity prediction, enabling efficient one-step decoding. Extensive experiments demonstrate that DiMoT achieves state-of-the-art performance across various challenging text-to-motion benchmarks, yielding superior motion fidelity and text-motion alignment. Project page: this https URL.

---


### 59. [Key Institutional Considerations for Designing Effective Independent Verification Organizations](https://arxiv.org/abs/2611.10168)

**<font color=#1a73e8>作者：</font>** Uma Kalkar, Rumman Chowdhury, Reva Schwartz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Independent verification organizations (IVOs) have emerged as a popular, bipartisan solution for facilitating high-quality independent evaluations of AI technologies. But momentum is outpacing design: there is emerging consensus on the necessary operating conditions for robust IVOs, but little discourse on institutional and policy specifications to ensure those conditions are met. IVOs are currently envisioned primarily as a mechanism operating at the AI frontier and model level to evaluate catastrophic risks. Little work has yet been done on how to establish or enforce an IVO ecosystem that is equipped to handle myriad risks (i.e., beyond catastrophic ones) and operate at the system and application level across the deployment and use stages of the AI lifecycle. This paper argues that IVO design should ensure the capacity for evaluating AI models, systems, and applications in context for both frontier companies and enterprise companies & AI-adopting organizations. Additionally, this paper provides early considerations to advance IVO discourse from normative to operative, and from existential to everyday risks. Drawing from existing institutional constructs in financial services, education, public health, and science, we outline key considerations on whom IVOs serve, what access they require, how they interact with external governing structures, how they are funded, and how they fit into the wider assurance ecosystem. Much of the structure and knowledge necessary to holistically design IVOs and their ecosystem does not yet exist, even as companies rush to ink agreements with their chosen evaluators.

---


### 60. [Where Did the Evidence Go? Diagnosing Proof-Set Loss in Long-Term Conversational Memory](https://arxiv.org/abs/2611.10170)

**<font color=#1a73e8>作者：</font>** Bogdan Roshchupkin, Maria Khodorchenko  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term conversational question answering can require several separated dialogue turns that support an answer only together. We introduce EviCover, a retrieval approach designed to retain this complementary evidence. It converts questions into observable evidence requirements, checks requirement coverage using retrieved source identifiers, and selects turns jointly. We track annotated support sets - the benchmark-labeled dialogue turns associated with each question - through retrieval, reranking, and final answer-generation context. We evaluate the baseline memory pipeline on generated, human-verified LoCoMo conversations and human-written REALTALK conversations, and examine EviCover on REALTALK's 108 multi-hop questions. Compared with the hybrid lexical/dense baseline, support-turn recall among 60 candidate turns rises from 0.526 to 0.575, and recall in the final ten-turn context rises from 0.349 to 0.379. The evidence funnel identifies separate discovery and selection failures, while paired answer evaluation shows that greater evidence recall does not yet establish a correctness gain. This analysis locates where complementary evidence is lost and distinguishes evidence retrieval from its use in answer generation.

---


### 61. [Generative Active Learning for Label-Efficient Pan-Organ Ultrasound Diagnosis](https://arxiv.org/abs/2611.10180)

**<font color=#1a73e8>作者：</font>** Yaofei Duan, Yuhao Huang, Yuan Gao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical ultrasound (US) enables real-time, non-invasive diagnosis, yet building US-based AI systems is limited by data scarcity, costly expert annotation, and limited cross-center generalizability. Privacy constraints and instance-level reporting hinder the collection of diverse abnormal cases and frame-level labels, while repeated retraining for new centers increases computational cost. We introduce EvoDiff, a generative active learning framework that integrates diffusion modelling with information-theoretic objectives, evolutionary search, and curriculum-based sampling to select informative samples across heterogeneous US datasets. EvoDiff formulates sample selection as a generate-to-retrieve process, in which diffusion-based optimization in feature space guided by information gain produces synthetic probes, and only the real unlabeled samples retrieved by these probes are annotated and used for downstream training. Across six benchmarks covering fifteen datasets and 16,696 images, we evaluate EvoDiff on convolutional network and transformer-based foundation model. EvoDiff approaches fully supervised performance with substantially fewer labels, outperforms active learning baselines, and improves foundation model generalization under cross-domain external validation on unseen cohorts. A reader study with six radiologists indicates the potential to support clinical annotation workflows, with a model-based estimated 24% to 84% reduction in annotation workload at matched downstream performance.

---


### 62. [ATLAS: A Multi-Procedure Benchmark and Context-Aware Model for Surgical Anatomy Segmentation](https://arxiv.org/abs/2611.10182)

**<font color=#1a73e8>作者：</font>** Ronald L. P. D. de Jong, Tim J. M. Jaspers, Raf A. H. Vervoort 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognizing anatomical structures during minimally invasive surgery (MIS) could support intraoperative navigation and improve patient safety, but progress is limited by small, single-procedure datasets and by segmentation methods developed for natural scenes. This work addresses both limitations through a new dataset and model. First, we introduce ATLAS-120k, a clip-level semantic segmentation dataset of 121,018 annotated frames from 100 surgical videos, covering 14 laparoscopic and robot-assisted procedures and 41 classes. Annotations were created with a pipeline that combines manual labeling, tracker-based propagation, and review by surgeons. Second, we propose ATLAS (Anatomy Recognition with Context Learning using Foundation Representations), a video semantic segmentation model for surgical anatomy recognition. ATLAS builds on in-domain foundation-model embeddings and adds context queries for the procedure and surgical phase, together with query propagation between frames for short-term memory. ATLAS outperforms state-of-the-art natural-image and in-domain foundation models in both segmentation accuracy and temporal consistency, achieving a Dice score of 0.70 with ViT-L while running in real time at 76.2 FPS. Ablations show that the context queries improve accuracy and that query propagation improves temporal consistency. ATLAS also generalizes well, matching a dedicated model zero-shot on CholecSeg8k and improving phase recognition on AutoLaparo over SurgeNet initialization. The model weights, dataset annotations, and annotation tool are publicly available at this https URL.

---


### 63. [GSynPEF: A Privacy Evaluation Framework for Synthetic Graphs](https://arxiv.org/abs/2611.10185)

**<font color=#1a73e8>作者：</font>** Yu Duan, Luca Baldesi, Carter T. Butts 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> It is often desirable to generate and release synthetic graphs, which resemble real-world data, in a privacy-preserving way. While substantial progress has been made in designing private graph synthesizers (PGS), opportunities remain for more explicit connections between synthesizer models and privacy evaluation, and better accounting for output variation. This paper proposes GSynPEF, a practical framework for empirical evaluation of privacy and utility in settings for which a real-world graph is given as input and output synthetic graph(s) are observed. Our framework links a broad class of graph synthesizers (both statistical and deep-learning based) with privacy metrics, expanding evaluation dimensions to practical utility and risk, through empirical analysis of multiple actual outputs. The framework accommodates both an Exact Solution scenario, where synthesizer behavior is directly observable, and a Monte Carlo Approximation scenario where only synthetic outputs from a black box synthesizer are available. Extensive experiments on four real-world datasets and seven widely used graph synthesizers demonstrate framework's versatility, enabling privacy evaluation for different attack goals (e.g., to infer an edge or node) and capabilities (e.g., observing one or multiple synthetic graphs). We analyze evaluation results by examining the relationship between graph statistics and synthesizer design choices, providing insights for data curators in PGS selection and researchers for improved PGS design.

---


### 64. [Projected Neural Additive Models as Universal Approximators](https://arxiv.org/abs/2611.10186)

**<font color=#1a73e8>作者：</font>** Nhon N. Phan, Qiang Du, John D. Clayton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural additive models (NAMs) offer interpretability but lack expressivity due to their rigid additive structure, whereas multi-layer perceptrons (MLPs) achieve universal approximation at the cost of transparency. We establish the first theoretical foundation for projected neural additive models (PNAMs), which augment NAMs with a learnable linear transformation $\boldsymbol{T}$ to capture cross-variable interactions. While standard NAMs cannot approximate even the simplest interaction term $\chi_1 \chi_2$ because their cross-derivatives are identically zero, we prove that PNAMs are universal approximators and characterize the minimum number of projections required for exact polynomial representation. Furthermore, we derive an approximation rate of $\mathcal{O}(M^{-s / (N - 1)})$ for $\mathcal{C}^s$ functions (i.e., functions with $s$ continuous derivatives), where $M$ denotes the number of projections and $N$ the input dimension; this rate is known to be optimal for ridge function approximation. To recover interpretability from the projected inputs, we introduce structured sparsity regularizers and post-hoc symbolic regression techniques that enable global input ranking, parameter pruning, and the conversion of learned bases into compact analytical expressions. Experiments on knot theory invariants, MNIST, and phase field fracture mechanics demonstrate that PNAMs match or surpass similar architectures in accuracy while discovering salient features and yielding symbolic models with orders of magnitude fewer parameters.

---


### 65. [Fast Accurate Quantum Monte Carlo without Metropolis Adjustment](https://arxiv.org/abs/2611.10187)

**<font color=#1a73e8>作者：</font>** Reuben Cohn-Gordon, Gabriel Pescia, Sumner N. Hearth 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In quantum systems, physical quantities of interest can be expressed as expectation values of a probability distribution, which allows their estimation by Markov Chain Monte Carlo (MCMC) methods. This approach, an instance of Quantum Monte Carlo (QMC), plays a central role in obtaining predictions of system properties relevant to condensed matter and high energy physics. The use of Hamiltonian dynamics to design a Markov kernel, known as Hybrid or Hamiltonian Monte Carlo (HMC), is widespread in quantum applications. In this context, it is standard to use an HMC kernel that is ``adjusted'' with the Metropolis-Hastings (MH) criterion, so that estimates of expectations converge to their true value in the limit of infinite sample size. However, recent work in computational statistics suggests that an \emph{unadjusted} HMC kernel can be significantly more efficient, while safely maintaining an asymptotic bias which is small relative to the error arising from the variance of the finite sample size. We adapt this approach to the QMC setting, focusing on a challenging and high-dimensional \emph{spin-fermion} model of a quantum phase transition. We find that unadjusted methods outperform adjusted HMC in terms of effective sample size per gradient call, while retaining accurate results.

---


### 66. [BO-Arena: An Evolving Benchmark for High-Dimensional Bayesian Optimisation](https://arxiv.org/abs/2611.10198)

**<font color=#1a73e8>作者：</font>** Colin Doumont, Thomas Christie, Henry Moss 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional Bayesian optimisation (HDBO) is an increasingly crowded field with new methods proposed at every major conference, making it ever harder to answer a deceptively simple question: "Which method is currently state-of-the-art?" In this paper, we question the efficacy of benchmarking practices in the field, and find them to be systematically ineffective: multiple published works fail to benchmark against the strongest available baselines, or even include incorrect implementations of key methods. Without a shared reference implementation, such errors are difficult to detect during peer review. We therefore introduce BO-Arena, an actively maintained and extensible package providing canonical implementations of state-of-the-art algorithms, which allows researchers to develop new methods and benchmark them rigorously. Using BO-Arena, we find that what currently drives performance in HDBO is even simpler than previously thought. We use these insights to propose a new algorithm which is competitive with the state of the art on problems with many observations, without resorting to the complex GP approximations used in recent methods. Finally, we question whether there is currently sufficient evidence that any more complex method outperforms a simple Gaussian process baseline for HDBO.

---


### 67. [RigidGS: Geometry-Aware Object Decoupling for Rigid-Body Interaction in 3D Gaussian Splatting](https://arxiv.org/abs/2611.10199)

**<font color=#1a73e8>作者：</font>** Paul Sansah Gyreyiri, Diksha Shukla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive VR/MR applications demand photorealistic 3D representations that support real-time rendering and object-level manipulation. While 3D Gaussian Splatting (3DGS) achieves high rendering quality, it represents scenes as unstructured, monolithic primitives. Existing object-aware 3DGS methods jointly optimize geometry and semantic states but suffer from two key failure modes: noisy foundation-model masks on complex geometry, and label-geometry coupling, in which co-optimized identity gradients mislabel boundary Gaussians. We introduce RigidGS, an end-to-end pipeline that decouples geometric learning from object identity. We propose a depth- and temporally-aware mask refinement module that addresses two complementary SAM2 failures: over-inclusion on thin structures and under-inclusion on multimodal-depth objects. We then determine object identities entirely upstream via COLMAP projection voting and freeze them during training, directing mask supervision solely toward geometric optimization. Refined masks alone substantially improve competing methods, yet a residual gap in label-geometry coupling persists that our fixed-identity design eliminates. RigidGS outperforms prior object-aware 3DGS methods on LLFF/NVOS, Mip-NeRF~360, and iNeRF360, improving segmentation and boundary IoU by 7.7 and 14.5 points on LLFF/NVOS. Finally, RigidGS enables real-time rigid-body manipulation on Meta Quest~2 without mesh extraction. Our code and project page are available at this https URL.

---


### 68. [Semiprime Factorization with Discrete Diffusion and Beam Search: Scaling Laws](https://arxiv.org/abs/2611.10202)

**<font color=#1a73e8>作者：</font>** Brendan O Donoghue, Nenad Tomasev, Volodymyr Mnih 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We demonstrate that transformer architectures trained with discrete denoising diffusion and decoded via guided test-time beam search can learn to recover the prime factors of semiprime integers directly from data. Our approach establishes a new frontier for learning-based semiprime factorization, successfully factoring 68-bit integers-a substantial advance over the prior 56-bit state of the art. While computationally less efficient than classical factoring algorithms, our model requires no domain-specific number-theoretic priors and learns purely from training examples. In practice, the diffusion model acts as a generative prior, identifying promising factor candidates where exact verification or lattice-based post-processing can complete the factorization. Furthermore, we derive empirical scaling laws relating approximation quality to training data volume, model size, and test-time computation. In contrast to language, problem size is the key driver of scaling behavior. Achieving a fixed accuracy on a held-out test set requires compute that scales exponentially with bit length. Consequently, our findings pose no threat to security, as the projected compute cost required to factorize cryptographically relevant integers remains prohibitive.

---


### 69. [DisMUSE: An Efficient Distributed Singular-Spectrum-Based Optimization Approach with Theoretical Convergence Guarantee](https://arxiv.org/abs/2611.10212)

**<font color=#1a73e8>作者：</font>** Zhen Qin, Zhiyao Zhang, Yingbin Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, singular-spectrum-based optimizers have attracted increasing attention due to their ability to preserve the matrix structure of neural network gradients, thereby enabling geometry-aware optimization. However, most singular-spectrum-based (SSB) approaches remain centralized, limiting their use in distributed learning infrastructures that exploit massive parallelism. Distributed SSB optimization is still at an early stage, with open questions about convergence guarantees and communication efficiency. To fill this gap, we propose the Distributed Momentum-based Spectral Estimator (DisMUSE), an efficient distributed SSB optimization framework for both data-center and federated settings. Using Muon-style exact orthogonalized momentum as the spectral update, DisMUSE integrates a recursive variance-reduced momentum estimator and achieves an $O((KT)^{-1/3})$ convergence rate, where $K$ and $T$ denote the number of nodes and local iterations per node, respectively. This rate matches the best-known rates for variance-reduced nonconvex distributed optimization. Building on this variance-reduced framework, we study two extensions. First, our DisMUSE method with finite Newton-Schulz (NS) iterations preserves the same convergence order under a uniform normalized support-spectrum condition, up to a multiplicative factor. Second, we develop a communication-efficient variant based on low-rank (LR) momentum transmission and quantify the error it introduces to the stationarity bound, characterizing the trade-off between accuracy and communication cost.

---


### 70. [Rethinking How to Leverage Cheap Physics for Data-Efficient Neural Operators](https://arxiv.org/abs/2611.10217)

**<font color=#1a73e8>作者：</font>** Shuo Zhang, Senwei Liang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators learn mappings from PDE inputs, such as initial conditions and coefficient fields, to the corresponding solutions. Once trained, they can rapidly predict solutions for new inputs. However, obtaining input-solution pairs for supervised training often requires expensive numerical simulations, whereas PDE inputs and governing equations provide inexpensive physical information. This raises a question: how can cheap physical information reduce the need for labeled solutions? A natural approach is to use physics to select inputs for labeling, but our acquisition experiments show no consistent advantage over random sampling. This observation motivates exploring an alternative: using cheap physics to improve neural operator initialization before supervised training. We propose Physics-Informed Initialization (PI-Init), a simple yet effective method that pretrains neural operators on unlabeled inputs using physics-informed losses and retains the learned parameters for supervised fine-tuning on the labeled dataset. A linearized analysis shows that pretraining can improve downstream prediction accuracy by reducing initialization errors that limited labeled data cannot effectively correct. Experiments across diverse PDE benchmarks and neural operator architectures demonstrate improvements in predictive accuracy, out-of-distribution generalization, and label efficiency. Representative results show error reductions of up to 62.7% at the same label budget and comparable or better accuracy with 90% fewer labels, relative to supervised-only training.

---


### 71. [Lower-Level Agnostic Bilevel Optimization](https://arxiv.org/abs/2611.10223)

**<font color=#1a73e8>作者：</font>** Peiwen Qiu, Prashant Khanduri, Jia Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bilevel optimization is a fundamental framework for machine learning problems, where an upper-level (UL) objective depends on the solution of a nested lower-level (LL) problem. Existing bilevel algorithms typically assume that the LL objective is available for evaluation, differentiation, or unrolling. However, this assumption can fail when the LL response is produced by a black-box solver, simulator, adversary, or learned predictor. In this paper, we study LL agnostic bilevel optimization, where the UL learner has access only to an approximate LL solution $\bar{\mathbf{y}}(\mathbf{x})$ and cannot query the LL objective, its gradients, Hessian/Jacobian information, or the procedure that generates the LL response. We propose LeGo-BiO, a coordinate-wise pseudo-hypergradient method that estimates the missing Jacobian $\nabla _{\mathbf{x}}\bar{\mathbf{y}}(\mathbf{x})$ using finite differences of $\bar{\mathbf{y}}(\cdot)$. For each UL coordinate, LeGo-BiO constructs a decision vector subject to 1-sparse updates, thereby isolating the corresponding Jacobian column needed in the UL gradient computation. This avoids the directional-projection limitation of full-parameter response differences and, unlike derivative-free/zeroth-order approximations of the entire UL gradient, preserves the available first-order gradient information with respect to the UL variables for more accurate UL gradient evaluation. We establish convergence guarantees for LeGo-BiO in both deterministic and stochastic settings under an LL error-bound/Polyak-Lojasiewicz-type condition, without requiring LL strong convexity. Our bounds yield an $O(T^{-1})$ rate in the deterministic setting and an $O(T^{-1/2})$ rate in the stochastic setting when the LL approximation error decreases geometrically. Experiments demonstrate competitive performance of LeGo-BiO despite being agnostic to the LL objective.

---


### 72. [ProofDiff: Auditable Argument-Level Comparison of AI-Generated Mathematical Proofs](https://arxiv.org/abs/2611.10233)

**<font color=#1a73e8>作者：</font>** Matan Tsafrir, Esdras Medeiros, Jorge Poco 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematical understanding depends on the route from hypotheses to conclusion: how the parts of a proof function and which dependencies carry the argument forward. This structure can persist when wording or notation changes, while a small alteration to a hypothesis or inference can produce a different argument beneath similar prose. Formal verification can establish that a rewrite proves the same theorem, but not whether it follows the same mathematical route. Comparing informal proofs, especially those produced or revised by generative models, therefore requires reconstructing which claims, dependencies, and reasoning steps are preserved, reorganized, or replaced.
We present ProofDiff, a system for comparing informal mathematical documents. It is designed to support human review, not to certify mathematical correctness. Given two documents, ProofDiff independently constructs a source-grounded argument map for each and proposes correspondences between the resulting maps. Each map captures the document's claims and reasoning steps and records the typed relations that connect them. An integrated human-review layer allows reviewers to revise the maps and correspondences while preserving an auditable history. Comparing the two argument maps provides a basis for inspecting whether the documents follow the same mathematical route and where their claims or dependencies differ. We demonstrate ProofDiff on four illustrative pairs of AI-generated proofs, ranging from a detailed proof and its concise revision to proofs using different mathematical strategies.

---


### 73. [Anatomy-Preserving Unpaired Medical Image Translation via Shared Latent Anchoring](https://arxiv.org/abs/2611.10236)

**<font color=#1a73e8>作者：</font>** Zhilin Zou, Hieu Le, Saumya Gupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unpaired medical image-to-image translation requires synthesizing target-modality images from source-modality images without aligned supervision. Existing methods learn a direct source-to-target mapping that entangles structure preservation and appearance generation within a single model, often distorting clinically meaningful anatomy in the translated output. We argue that these two objectives should be decoupled entirely: anatomical structure should be captured independently of generation, and the generator should operate only on a frozen structural representation. To this end, we propose a two-stage framework for unpaired medical image translation. In the first stage, we learn a shared structure space by training a structure encoder-decoder on source images, target images, and structural masks jointly, using mask reconstruction to anchor the latent space to modality-agnostic anatomy. For source images without mask annotations, a target-domain memory bank provides soft structural supervision via prototype retrieval. In the second stage, a conditional flow model learns to render target-domain appearance under fixed structural conditions. This ensures the generator inherits target appearance statistics and can focus entirely on structural conditioning rather than learning appearance from scratch. We validate our framework on OCT-to-OCTA synthesis and brain MR-to-CT translation. Our method outperforms all unpaired baselines on both tasks and, despite requiring no paired supervision, also surpasses paired baselines, improving PSNR by up to 11.2% and SSIM by up to 26.4% on OCT-to-OCTA, and achieving consistent gains across whole-image, soft-tissue, and bone regions on MR-to-CT. The project repository is available on GitHub.

---


### 74. [Implicit Bias in State Space Models and Linear Autoregressive Training](https://arxiv.org/abs/2611.10237)

**<font color=#1a73e8>作者：</font>** Gal Katzhendler, Gilad Yehudai, Gal Vardi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear State Space Models (SSMs) and linear autoregressive sequence models reuse the same parameters across a sample-dependent number of steps. As a result, different examples impose constraints through different predictors, even though all predictors share the same weights. We study this phenomenon through a general model of multiple non-homogeneous polynomial predictors with shared parameters, in a classification setting. Under standard interpolation and directional-convergence assumptions, together with a trajectory-dependent effective-degree condition, we show that gradient descent on the exponential loss converges in direction to a KKT point of an effective-degree max-margin problem. In this problem, only examples with minimal effective degree impose hard margin constraints; examples with faster-growing margins are asymptotically inactive except for feasibility.
Our result provides a first-order characterization of the implicit bias in linear SSMs and linear autoregressive models. It exposes a mechanism of length bias: a longer input sequence or additional autoregressive steps may increase the example's effective degree, and the examples with the smallest effective degree dominate the limiting classifier. Our result highlights how non-homogeneity and parameter sharing alter classical homogeneous implicit-bias results.

---


### 75. [CoRA-Bench: Evaluating Evidence Preservation by Context Selectors Under Token Budgets](https://arxiv.org/abs/2611.10238)

**<font color=#1a73e8>作者：</font>** Huzaifa Pardawala, Siddhant Sukhani, Sudheer Chava 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Context selection can reduce input length during long-input inference but can remove evidence required to answer a query. We introduce CoRA-Bench, a benchmark for evaluating evidence preservation under shared token budgets. We compare head and tail truncation, BM25, dense retrieval, dense retrieval with reranking, LLMLingua-2, and Provence across BABILong, LOONG Financial Spotlight, a custom NoLiMa diagnostic, and LongMemEval. Evidence-preservation results reveal task-dependent tradeoffs: BM25 achieves 0.921 supporting-fact recall on BABILong at 128K, dense retrieval and dense reranking each achieve 0.908 needle recall on NoLiMa at 64K, and dense retrieval achieves 0.993 answer-bearing-turn recall on LongMemEval at 64K. Evidence, token retention, and complementary reader evaluations use the same selected contexts. Reader evaluations use dataset-native answer metrics and three runs on the same questions, with paired bootstrap confidence intervals. At a 32K budget, BM25 achieves 46.20% BABILong answer accuracy and dense retrieval achieves 71.13% LongMemEval accuracy. The results show that method rankings vary across evidence types and between evidence recall and downstream accuracy.

---


### 76. [Beyond Frame-Level Accuracy: Analyzing Video-Level Stability in Transformer-Based Deepfake Forensics](https://arxiv.org/abs/2611.10249)

**<font color=#1a73e8>作者：</font>** Syed Azmul Hasan, Mowmita Pervin Hera, Afroza Lona Mim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake videos generated by advanced generative models pose serious threats to digital security, misinformation control, and media forensics. Although numerous detection methods have been proposed, their reported performances are often based on heterogeneous preprocessing pipelines, inconsistent data splits, and model-specific training protocols, hindering fair architectural comparison. This work presents a controlled and reproducible comparative study of convolutional neural networks (ResNet-18 and EfficientNet-B0) and a transformer-based architecture (ViT-B/16) within a unified, face-centric deepfake detection framework. All models are trained using identical preprocessing, augmentation, optimization settings, and data splits on Celeb-DF v2 and FaceForensics++, and results are validated across three independent random seeds with bootstrapped confidence intervals. Experimental results show that while CNN-based models perform competitively at the frame level, their performance degrades after video-level aggregation. In contrast, ViT-B/16 demonstrates more stable video-level performance, achieving 92.8\% [95\% CI: 91.7--94.0] video-level accuracy and an AUC of 0.950 [95\% CI: 0.934--0.964] on Celeb-DF v2 (3-seed bootstrapped). Cross-dataset evaluation across the same three random seeds reveals a large, asymmetric generalization gap (AUC 0.79 FF++$\rightarrow$Celeb-DF vs. 0.64 Celeb-DF$\rightarrow$FF++), indicating that in-domain video-level stability does not transfer to unseen manipulation domains. These findings indicate that global self-attention improves robustness and video-level stability for deepfake detection within a given data domain, while highlighting the need for further work on cross-domain generalization.

---


### 77. [TORNADO: Adaptive Latent Stochastic Transport for Calibrated Probabilistic PDE Forecasting](https://arxiv.org/abs/2611.10251)

**<font color=#1a73e8>作者：</font>** Jorge Mifsut Benet, Armand Kassaï Koupaï, Ramon Daniel Regueiro-Espino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic neural surrogates for PDEs enable ensemble forecasting, but often exhibit miscalibration when used for uncertainty quantification, especially in compute-constrained, few-step inference regimes. Existing generative approaches typically rely on fixed global stochasticity, which cannot adapt predictive uncertainty to the local dynamical state. We propose TORNADO, a latent probabilistic forecasting framework that formulates next-step prediction as stochastic transport between VAE encoder posteriors. Unlike existing approaches with globally prescribed stochasticity, TORNADO learns a SDE with state-dependent diffusion, enabling the predictive uncertainty to adapt to the local latent dynamics. The model is trained using analytic conditional endpoint targets derived from a Gaussian interpolant, enabling simulation-free learning. An additional energy distance regularization term improves distributional alignment. Empirically, TORNADO improves uncertainty calibration over representative generative baselines, including stochastic interpolants, diffusion models, and flow matching, while maintaining comparable predictive accuracy. Our results show that adapting stochasticity to the latent state, rather than prescribing it globally, is an effective mechanism for improving calibration in practical neural PDE forecasting settings. Project page: this https URL.

---


### 78. [VeV: Video-Enhanced Vibration Data Augmentation For Structural Difference](https://arxiv.org/abs/2611.10257)

**<font color=#1a73e8>作者：</font>** Joonhee Lee, Jiale Zhang, Sungmin Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Surface-mounted vibration sensing provides non-invasive structural monitoring with high temporal fidelity across diverse ubiquitous computing scenarios such as smart farms, yet structure-borne wave models remain fragile to physical relocation and structural shifts. However, addressing this spatial data discontinuity remains limited by costly manual recalibration, insufficient physical grounding in data-driven synthesis, and substantial sim-to-real gaps in numerical digital twins. To resolve this spatial bottleneck without labor-intensive data recollection, we propose VeV, a physics-consistent spatial augmentation framework that synthesizes vibration responses at unmeasured target coordinates from sparse reference observations by coupling a monocular Vision-Derived Propagation Possibility Map for structural wave-guiding paths with a Visual Feature Map for transient source kinetics and implicit material dynamics. Evaluated on a 1,237 sensor-hour sow pig and piglet farm across disparate structures, VeV reduces waveform reconstruction MSE by over 57.5% compared to data-driven baselines and achieves up to 81.69% zero-shot classification accuracy, while reaching peak performance within just 30-50 calibration chunks to effectively eliminate cold-start retraining overhead and establish a scalable foundation extending to human-centric floor vibration sensing and ambient intelligence.

---


### 79. [STAIRS: Staging the Inverse Problem via Admissible-Support Scheduling for Unrolled MRI Reconstruction](https://arxiv.org/abs/2611.10260)

**<font color=#1a73e8>作者：</font>** Xiangjian Hou, Chang Ni, Chao Qin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accelerated magnetic resonance imaging (MRI) forms images from incomplete Fourier measurements, shifting acquisition burden to computational reconstruction. Deep unrolled networks interleave learned regularization and data consistency, yet typically estimate the full unmeasured spectrum at every cascade. We propose STAIRS (Staging the Inverse Problem via Admissible-Support Scheduling), which projects intermediate reconstructions onto nested Fourier supports that expand to the full spectrum and conditions each update on its support transition. Conditional increments of a regularized log-determinant score of training covariance define a normalized spectral coordinate, accounting for dependencies between newly and previously admitted frequencies. Dyadic targets allocate larger coordinate increments to earlier cascades and are mapped to fixed supports before training, enabling coarse-to-fine reconstruction with unchanged sampling masks and data consistency. On fastMRI and Stanford2D, STAIRS improves matched Transformer (HUMUSNet) and convolutional (NAFNet) backbones in single- and multi-coil reconstruction, including radiologist-annotated pathology regions. It also outperforms predictor-based progression with lower parameter overhead and inference latency. Stage-wise analysis shows repeated error correction by projection and lower intermediate reconstruction errors than the backbones alone throughout support expansion. Ablations favor dyadic allocation over uniform expansion for square and line-band supports and over manual front-loading for square windows. Support projection alone improves reconstruction, and transition conditioning strengthens the gain. Cross-dataset evaluation shows improvements for both backbones in both directions. Support allocation thus complements regularizer design in unrolled MRI reconstruction.

---


### 80. [Is Recursive Self-Improvement Safe?](https://arxiv.org/abs/2611.10261)

**<font color=#1a73e8>作者：</font>** Vincent Conitzer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The phrase recursive self-improvement (RSI) refers to the idea of an AI system designing and creating another, better AI system, which in turn designs and creates an even better one, and so on. While the idea has a long history, it has always been an abstract, futuristic idea -- until recently. Today's frontier AI has attained a set of abilities, including in programming, mathematics, research, tool use, and working coherently over extended periods of time, that make RSI seem plausible. AI companies are starting to pursue it, but many of the involved people are also expressing concerns, asking whether humanity should really set this in motion and under what conditions. I will discuss the situation, argue that we do not even have clear frameworks for thinking about the likely outcomes of RSI, and do a quick game-theoretic analysis of how to choose whether to initiate RSI when another party is making the same choice.

---


### 81. [Domain Generalization for Style-Debiased Object Detection via Label-Consistent Training across Multiple Styles](https://arxiv.org/abs/2611.10262)

**<font color=#1a73e8>作者：</font>** Chaoran Zhang, Shirshak Bhusal, Zhilin Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain generalization (DG) for object detection aims to improve model performance on unseen target domains. Existing detectors, however, suffer substantial degradation on visually distinct unseen domains, as models confined to limited training styles tend to overfit superficial statistical cues rather than object-level semantics. Motivated by human perception, which attends primarily to semantically relevant features while ignoring irrelevant style cues, we propose Origin-Anchored Multi-Style Consistency (OAMSC), a source-only framework that couples multi-style data synthesis with cross-style consistency learning to suppress style-sensitive shortcut learning. For data preparation, we leverage off-the-shelf diffusion models to expand the source datasets into 20 distinct styles, with all generated images manually verified to ensure that object instances and annotations remain consistent across style variants. During training, we impose Origin-anchored consistency constraints at scene and object levels to reinforce the learning of domain-stable features while suppressing the influence of style-sensitive cues. Extensive experiments and ablation studies on multiple challenging DG benchmarks demonstrate the consistent effectiveness and strong generalization performance of OAMSC across diverse domain shifts. Notably, our approach applies to both one-stage and two-stage detectors, while its data-centric design is complementary in principle to other DG methods. The training code and two style-transfer datasets constructed for the experiments, comprising approximately 180K images in total, are publicly available on GitHub.

---


### 82. [Match the Geometry Before the Surrogate: Extreme Low-Budget Optimization in High Dimensions](https://arxiv.org/abs/2611.10267)

**<font color=#1a73e8>作者：</font>** Michal Průšek, Adam Novozámský, Filip Šroubek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-budget molecular optimization is often framed as Bayesian optimization in a learned latent space, but standard benchmarks typically allow hundreds or thousands of evaluations, whereas a realistic wet-lab round may allow only a few dozen. We revisit this regime using a SELFIES molecular variational autoencoder (VAE) with a Gaussian prior and GuacaMol objectives at N = 30 evaluations. The main finding is not a new surrogate model, but an interaction in candidate generation. The encoder means of a reference set of molecules concentrate near a narrow spherical shell, while many high-dimensional optimizers propose candidates from boxes or box-shaped trust regions. We study a simple constraint, the on-sphere scaffold, that restricts candidate generation to this shell. We then introduce two minimal optimizers to probe what remains useful once the support is fixed. GeoWalk performs geodesic local search on the shell without a surrogate. After 30 evaluations, it shows no detected difference from a Gaussian-process (GP) surrogate on the shell, which is ahead earlier in the budget. GeoCMA adds covariance learning in a random subspace. It does not improve on GeoWalk in the molecular benchmark. On LassoBench it has a lower mean loss than GeoWalk, but full-dimensional CMA-ES remains stronger on most tasks. A factorial experiment with a single GP crosses the candidate support (shell or box) with the acquisition maximizer (a finite candidate set or a continuous optimizer). In this benchmark, shell candidates outperformed box candidates when acquisition was maximized over a candidate set, but not with continuous maximization by L-BFGS-B. These results come from a controlled study of one Gaussian-prior VAE benchmark and do not recommend VAEs for molecular optimization. The practical lesson is to control the candidate support and the acquisition maximizer before attributing a gain to the surrogate.

---


### 83. [Testing CCZ-equivalence to permutations via projections of Walsh zero spaces, with applications to APN functions](https://arxiv.org/abs/2611.10269)

**<font color=#1a73e8>作者：</font>** Emanuele Bellini  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Whether almost perfect nonlinear (APN) permutations exist in even dimension $n\ge 8$ is a long-standing open question, the big APN problem. The only example known in even dimension, on six bits, was found from a quadratic APN function that is not itself a permutation, by Carlet--Charpin--Zinoviev (CCZ) equivalence. It is therefore natural to test APN functions for CCZ-equivalence to a permutation. This amounts to finding two complementary $n$-dimensional subspaces among the zeros of the Walsh transform, which lie in $\mathbb{F}_2^{2n}$. A known necessary condition only uses their projections to $\mathbb{F}_2^n$ and cannot decide every case. We give an exact test for functions whose Walsh supports are affine, including all quadratic functions. It reconstructs the subspaces from their projections, through searches for subspaces of $\mathbb{F}_2^n$ and for constrained bilinear maps. On the benchmarked functions in dimension twelve, it lists them $39$ to $55$ times faster than the generic search of the commonly used sboxU library. We then study the functions $x^3+a^{-1}\mathrm{Tr}(a^3x^9)$, which Göloğlu and Pavlů proved not to be CCZ-equivalent to permutations when $4$ divides $n$. With their result, our computations show that this holds for every even $n\le 24$. In dimension $18$ the necessary condition is satisfied, and the new test decides the case. We conjecture this for every even dimension. We also compile $25$ classes of quadratic APN functions in dimension ten from published instances, with equivalence certificates. No function in these classes or in their switching closure is CCZ-equivalent to a permutation. All code and data are public.

---


### 84. [Transit-Oriented Land Use Planning Using Deep Reinforcement Learning](https://arxiv.org/abs/2611.10281)

**<font color=#1a73e8>作者：</font>** Bo Yang, Yuebing Liang, Zhan Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transit-Oriented Development (TOD) is a key strategy for advancing sustainable urban development by promoting high-density, mixed-use land development within walking distance of public transit stations. However, traditional TOD planning often relies on heuristic methods, making it difficult to efficiently identify quantitatively optimized transit-oriented land use patterns. This paper presents DRL4TOD, a deep reinforcement learning framework that automatically optimizes land use types and floor area ratios (FARs) around transit stations in alignment with TOD principles. DRL4TOD incorporates a graph neural network to capture spatial interdependencies among land parcels, road networks, and metro stations, and uses a DRL-based optimization strategy to assign land-use types and FARs to selected parcels. It jointly optimizes multiple objectives, including land use density, land use diversity, and transit capacity utilization, while minimizing reconstruction costs to account for development feasibility. Applied to two real-world station areas in Shanghai, DRL4TOD consistently outperforms rule-based approaches and genetic algorithms, achieving more effective TOD outcomes with lower reconstruction costs. By adjusting objective weights, the framework enables flexible prioritization, such as placing greater emphasis on cost minimization when financial feasibility is a concern. These results demonstrate DRL4TOD's potential as a decision-support tool for generating coordinated land-use and FAR configurations under planner-specified priorities, rather than prescribing a single fixed design. For policymakers, the framework provides parcel-level, constraint-aware alternatives that make trade-offs among competing objectives explicit and support targeted decisions about development intensity and feasibility.

---


### 85. [Multi-objective drift-aware MLOps agent for model retraining](https://arxiv.org/abs/2611.10313)

**<font color=#1a73e8>作者：</font>** Kumuda Valli V, Anli Ji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deployed ML models face non-stationary data and delayed labels, yet most retraining strategies rely on fixed schedules or brittle drift thresholds that ignore operational cost. In this setting, retraining is a sequential decision problem rather than a one-time threshold choice. We present DARE (Drift-Aware Retraining Engine), an offline, event-driven retraining framework that separates ingestion, monitoring, policy decisions, training, and logging through explicit schemas and deterministic replay. We compare DARE against practical heuristic retraining baselines, including fixed-interval, threshold-persistence, and action-rate-matched fixed scheduling policies. On Airline, the locked LinUCB policy achieves a higher mean F1 while substantially reducing intervention frequency relative to heuristic and action-rate-matched baselines. Additional runtime-calibrated evaluation shows that these gains persist when measured using the cumulative update wall-clock time. These results suggest that conservative sequential retraining policies can improve performance while reducing unnecessary operational overhead under delayed feedback.

---


### 86. [AI-Driven Repair of Missing Automotive Components](https://arxiv.org/abs/2611.10318)

**<font color=#1a73e8>作者：</font>** Kazim Abbas, Zheng Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to supply constraints, replacing damaged automotive components can be expensive and time-consuming, while replacing the entire component can be wasteful when much of it remains usable. This paper presents a pipeline to investigate whether missing geometry can be reconstructed as a repair patch using paired observations of the intact models and synthetically damaged components. Noise-free color, depth, and silhouette images were produced using the camera viewpoints. Depth differences were then used to identify the potential missing regions, while multi-view voxel reconstruction was used to estimate the missing portion. A pretrained DINOv2 model was also added to validate missing candidates and determine whether pretrained visual features could improve reconstruction. We tested the pipeline on 20 automotive CAD models, each with a synthetically removed portion. Each model was tested under four different conditions using two reconstruction methods for a total of 160 trials. The predictions were compared with the missing geometry of the unchanged ground-truth using predefined thresholds of the voxel intersection-over-union over 0.85 and the absolute relative volume error less than 15%. Of the 160 experimental trials, 109 of them satisfied both thresholds. Geometry-only reconstruction passed 16 of 20 components with eight views but only 10 of 20 with four adjacent views. Further analysis showed that 24 out of the 37 failed reconstructions could be categorized as unsuccessful because extra material was incorrectly added to areas that should have been empty. The implementation of DINOv2 into the pipeline did not improve the overall reconstruction accuracy and made prediction generation slower. For 13 verified tests, printing only the repaired sections instead of the entire parts reduced filament use by 93.08% and printing time by 89.39% based on the median results.

---


### 87. [LoCo: Selective Local Competition for Discriminative Open-Vocabulary Multi-Label Recognition](https://arxiv.org/abs/2611.10321)

**<font color=#1a73e8>作者：</font>** Zhuoming Li, Bo Han, Xiaoyu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-Vocabulary Multi-Label Recognition (OV-MLR) aims to identify all queried semantic concepts present in an image. Existing methods mainly improve global image-text matching or text-side representations, leaving local prediction largely under-explored. In this paper, we revisit local prediction and reveal that it can serve as a strong discriminative branch once two properties are properly handled: spatial consistency of local visual features and compatibility-aware local competition. This perspective is motivated by local semantic sparsity: each image region is related to only a small subset of queried concepts, while compatible concepts of different granularities or types may still coexist locally. We instantiate this perspective with LoCo, a selective Local Competition framework for OV-MLR. LoCo adopts a spatially consistent visual encoder to reduce local feature entanglement, and introduces Selective Softmax to impose competition only among locally incompatible categories while preserving compatible responses. Multi-scale inference further improves local prediction at different scales. LoCo can also be ensembled with an existing global predictor to provide complementary image-level context. Experiments on four multi-label benchmarks show that standalone LoCo improves average F1-score and mAP over TagCLIP by 3.4% and 3.8%, respectively. LoCo + DualPrompt achieves the highest averages among the compared methods, with gains of 4.8% and 5.2% over TagCLIP. Our results suggest that local semantic sparsity offers a useful basis for developing more discriminative open-vocabulary multi-label recognition methods. The code is available at this https URL.

---


### 88. [Evaluating classification and explainability in multimodal petrographic image analysis](https://arxiv.org/abs/2611.10331)

**<font color=#1a73e8>作者：</font>** Thomas James Wood, Oktay Karakuş, Can Eyüpoğlu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated thin-section classifiers increasingly combine plane-polarised and cross-polarised light (PPL and XPL), two complementary views central to petrographic identification. Classification accuracy alone does not reveal whether model errors reflect mineralogical relationships, how predictions depend on each optical view, or whether attribution maps identify regions that influence model decisions. Here, we examine these complementary aspects of the released LITHOS dual-stream vision transformer using outputs from an earlier evaluation of 105,802 expert-annotated grains across 25 categories. Classification errors frequently followed the label taxonomy: 72.6\% of misclassified plagioclase, microcline and sanidine grains were assigned the generic Feldspar label, while 87.1\% of quartz-family grains received a label within that family, compared with 66.6\% assigned their exact label. Replacing the XPL input with its per-channel spatial means produced a greater reduction in true-class probability than equivalent PPL replacement in 20 of 25 categories, but not in the three quartz categories. Five explainable artificial intelligence (XAI) attribution procedures generated visually distinct maps for identical inputs. In a superpixel-deletion analysis involving 30 grains from 29 thin sections, method-minus-random contrasts ranged from $-0.043$ to $0.057$, with all 41 simultaneous 95\% confidence intervals including zero. Together, these findings show that error structure, modality sensitivity and attribution behaviour capture distinct aspects of model performance that cannot be established from classification accuracy or visual inspection of attribution maps alone.

---


### 89. [TimeTraveler: Temporal Strategy Planning with Time Dictionary for Streaming Video Understanding](https://arxiv.org/abs/2611.10337)

**<font color=#1a73e8>作者：</font>** Minkuk Kim, Junho Kim, Seong Tae Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding (SVU) requires models to answer user queries over continuously evolving video streams. Unlike offline video QA, SVU must handle queries whose evidence may lie in the past, appear in the current scene, or emerge only after future observations. Existing streaming video systems often rely on compact visual memories or fixed evidence-access schemes, which can lose fine-grained details and fail to adapt the answering process to the temporal intent of each query. In this paper, we propose TimeTraveler, a streaming VQA framework that performs temporal strategy planning with a Time Dictionary. Inspired by the need to search across different temporal regions of a stream, TimeTraveler stores each observed moment as a timestamp-indexed structured caption and uses this dictionary as an explicit source of queryable evidence. Given a query, TimeTraveler determines whether to recall past evidence, read the present context, or wait for future observations, and then applies a strategy-specific evidence acquisition process. Comparative experiments on streaming video QA benchmarks show that TimeTraveler improves streaming question answering by preserving fine-grained temporal evidence and selecting the appropriate temporal strategy for each query. The project page is available at this https URL.

---


### 90. [On the universal structure in deterministic generative diffusion](https://arxiv.org/abs/2611.10338)

**<font color=#1a73e8>作者：</font>** Defang Chen, Zhenyu Zhou, Can Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-based generative modeling has emerged as a general computational framework for simulating high-dimensional, structured data across various domains. Understanding its generative mechanisms is paramount for advancing model training and inference in a principled way. Here, we demonstrate that deterministic sampling trajectories share a universal geometric structure invariant to data modalities and diffusion model implementations. This structure can be largely explained by an exactly solvable model based on the optimal linear denoiser.

---


### 91. [Guided Co-Attention with Adaptive Gating for Multimodal Medical Data Fusion](https://arxiv.org/abs/2611.10348)

**<font color=#1a73e8>作者：</font>** Muntaqim Ahmed Raju, Priyanka Siddappa, Md Shifat Haider Al Amin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal fusion requires not only exchanging information across modalities but also determining which representations should participate in the interaction and how complementary cross-modal views should be combined. We introduce Guided Co-Attention with Adaptive Gating, a fusion framework that integrates token-wise guidance, bidirectional cross-attention, and sample-specific fusion. The proposed method constructs two directional representations: an image-conditioned text representation, obtained by allowing textual tokens to query visual features, and a text-conditioned image representation formed in the reverse direction. Token-wise guidance modulates the representations before cross-attention, while an adaptive gate learns the relative contribution of the two resulting directional representations for each sample. We evaluate the approach using paired chest radiographs and radiology reports as an image-text test bed for binary (normal vs. abnormal) classification. The two cross-attention directions exhibit distinct performance characteristics, demonstrating that reversing the query and source modalities does not produce interchangeable representations. Ablation experiments further show that bidirectional interaction, adaptive gating, and token guidance provide complementary benefits. The proposed model achieves 96.05% accuracy, 96.10% F1-score, 98.37% AUC, 95.60% Sens@95Spec, and 96.51% Spec@95Sens, yielding the highest mean performance across all evaluated metrics. These findings support explicitly modeling interaction direction, token relevance, and sample-dependent integration when constructing multimodal representations.

---


### 92. [TripletAD: Weakly Supervised Anomaly Detection in Embedding Space with Rare Anomalies and Scarce Labels](https://arxiv.org/abs/2611.10352)

**<font color=#1a73e8>作者：</font>** Sumit Wadhwa, Souvik Nath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many practical anomaly detection problems come with only a handful of confirmed anomalies, and the unreviewed remainder of the data cannot be trusted to be normal. We study this setting under a curated-label protocol, in which unconfirmed anomalies are removed from training rather than relabelled as normal, and propose TripletAD, a weakly supervised detector that learns a triplet-margin embedding and calibrates a linear scoring head with two soft penalties: a partial cross-entropy on labelled anomalies and a relative-contrast hinge that separates the mean scores of anomalous and normal samples. Because every mined triplet contains a labelled anomaly, the few labels are reused across the entire training set instead of being diluted by it. On 24 ADBench datasets whose inputs are pre-trained embeddings (text, image and speech vectors), TripletAD outperforms established state-of-the-art weakly supervised detectors (DevNet, PReNet and DeepSAD) and gradient-boosted trees when anomalies are rare. At a 1% anomaly rate it has the highest mean AUCPR of six methods, 20% above DevNet; on the naturally rare Speech dataset it doubles the best baseline (0.394 vs. 0.196 AUCPR); and on MVTec-AD it is best when only a quarter or half of the anomalies are labelled. Pooled over 70 rare- or sparse-label settings, it has the best average rank (2.21 of 6) and outperforms each baseline under Wilcoxon signed-rank tests with Holm correction. When anomalies are more frequent it performs on par with these methods. The method needs no per-dataset tuning and is insensitive to its loss weights and training length; on raw tabular features, gradient-boosted trees remain the stronger choice.

---


### 93. [DAPointRWKV: Domain Adaptive Vision RWKV for Point Cloud Completion](https://arxiv.org/abs/2611.10353)

**<font color=#1a73e8>作者：</font>** Yinghui Li, Qianyu Zhou, Hao Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain adaptive point cloud completion (DA PCC) aims to bridge the geometric discrepancy between labeled source domains and unlabeled target domains for accurate 3D shape completion. Existing methods based on CNNs, Transformers, and Mamba-like sequence models still face challenges from limited receptive fields, high computational complexity, insufficient geometric bias, and serialization sensitivity. Recently, Receptance Weighted Key Value (RWKV) provides a linear-complexity alternative for long-range sequence modeling. However, adapting RWKV to DA PCC remains challenging due to the lack of explicit geometric priors, the mismatch between recurrent modeling and coarse-to-fine generation, and unstable target-domain adaptation. To address these challenges, we propose DAPointRWKV, a novel RWKV-based framework for DA PCC. DAPointRWKV consists of three components: Geometry-Aware RWKV (GA-RWKV) Backbone, RWKV-Oriented Progressive Decoder (RWKV-PD), and Dual Structural Regularization (DSR). Specifically, GA-RWKV introduces geometry-aware recurrent representation learning, RWKV-PD bridges RWKV token representations with coarse-to-fine reconstruction through local token-guided refinement, and DSR stabilizes target-domain transfer through visible-structure anchoring and complete-shape hypothesis stabilization. Extensive experiments on synthetic and real-world benchmarks demonstrate that DAPointRWKV consistently outperforms state-of-the-art methods.

---


### 94. [MambaLoc: Lightweight Indoor Localization Using Cross-Modal Knowledge Distillation](https://arxiv.org/abs/2611.10360)

**<font color=#1a73e8>作者：</font>** Mohab Bahnassy, Omar Saqr, Hamada Rizk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate indoor localization on resource-constrained edge devices remains challenging due to the tension between modeling fidelity and computational efficiency. Wi-Fi Channel State Information (CSI) enables low-cost deployment using existing Wi-Fi infrastructure but is heavily distorted by multipath propagation. Transformer-based solutions mitigate these effects but their quadratic complexity limits real-time edge deployment. Ultra-Wideband (UWB) provides geometrically precise ranging yet requires dedicated infrastructure. We present MambaLoc, a cross-modal distillation framework that improves the accuracy-efficiency balance in CSI-based localization. MambaLoc uses a linear-time Selective State Space Model (Mamba) as a lightweight CSI student, guided during training by a UWB-Transformer teacher. A Feature Alignment Module bridges the representational gap between heterogeneous RF modalities, allowing the CSI model to inherit UWB-derived geometric structure without UWB hardware at inference. A probabilistic Gaussian Mixture regression head models multi-modal spatial ambiguity from multipath effects, avoiding the physically implausible averaging of deterministic regression. Evaluations on a real-world dataset show MambaLoc achieves a median localization error of 0.230 m, reducing error by 22.2% over a standalone Mamba baseline, while requiring 65.1% fewer FLOPs and 58% lower inference latency than Transformer-based approaches.

---


### 95. [Bias, Measurement Error, and Double-Dipping: When Can GNN Convolutions Help Brain Connectome Prediction?](https://arxiv.org/abs/2611.10364)

**<font color=#1a73e8>作者：</font>** Tommaso Castellani, Jiaqi Li, Muriah D. Wheelock 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) are an important tool for fMRI prediction, where empirical functional connectivity matrices serve both as features and for graph construction. However, recent studies and our own experiments show that these methods often fail to outperform simpler graph-agnostic baselines. We propose a statistical explanation for this failure by formulating connectome prediction as an errors-in-variables (EIV) problem: the true connectome is latent, while the observed covariance matrix is a noisy finite-time-series estimate. In a linear asymptotic setting, we decompose the effect of graph convolution into three mechanisms: smoothing-induced bias and variance reduction, graph estimation error, and a double-dipping effect arising when the same noisy matrix determines both graph and features. Under a latent community model adapted to neuroscience, we identify a narrow favorable regime, set by the brain community structure, the predictive signal, the graph construction and the recording length, in which message passing can improve prediction. Simulations validate this decomposition, while real-data experiments illustrate that connectome GNN pipelines often fall outside this regime. Our results provide a first step towards explaining when graph convolutions can help brain connectome prediction, and why they often do not.

---


### 96. [ClearForm: Shared-Surface Gaussian Splatting for Transparent and Opaque Scenes](https://arxiv.org/abs/2611.10370)

**<font color=#1a73e8>作者：</font>** Hajeong Lee, Jong-Il Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transparent-interface reconstruction must recover glass surfaces even when most observed color comes from the scene behind them. We present ClearForm, a shared-planar-Gaussian method for jointly reconstructing transparent interfaces and the appearance seen through them. We identify and analyze the Geometry-Appearance Compositing Dilemma (GACD): when the same transparency-dependent alpha controls both color and geometry, revealing the background can weaken a transparent surface's contribution to geometric reconstruction. We derive its effect on plane-based depth estimation, identify a mechanism that can weaken geometric learning, and quantify the loss of interface support through controlled comparisons. To address this conflict, we develop geometry-preserving dual-opacity surface reconstruction. Shared planar Gaussians retain interface contributions in geometry compositing while modeling transmission and sparse reflection in RGB, supported by transparency-aware geometric constraints. To manage the different primitive-visibility requirements of these compositors, we introduce Dual-Evidence Lifecycle (DEL), which retains Gaussians supported by multi-view geometry or RGB reconstruction evidence. On 3D-FRONT-T, ClearForm achieves 27.05 mm Chamfer distance (CD) and 0.928 F1, compared with 59.18 mm CD for our PGSR reproduction and the reported 34 mm CD and 0.836 F1 for GLINT. On TransLab, it achieves 1.65 mm CD, 0.963 F1, and 40.14 dB PSNR. In matched ablations, dual-opacity compositing reduces CD from 59.25 to 27.09 mm, while DEL improves PSNR by 2.06 dB. Our project page is available at this https URL.

---


### 97. [CHARM: Certified Homology-Aware Reverse-scale Mapping via Diffusion-Guided Quotient Towers](https://arxiv.org/abs/2611.10375)

**<font color=#1a73e8>作者：</font>** Zhe Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Widely used dimensionality reduction methods prioritize neighborhood or distance 1 preservation, yet planar coordinates alone cannot certify the homological type or 2 sample-level support of higher-order structures. Obtaining this evidence directly 3 is costly because simplicial complexes grow rapidly with dimension. We propose 4 Certified Homology-Aware Reverse-scale Mapping (CHARM), which combines 5 two-dimensional coordinates with certified homology records and sample-level 6 localization. Diffusion coordinates guide cover proposals; safe contractions and a 7 Cover Quotient Tower reduce the domain of structural computation; exact algebra 8 certifies and tracks homology representatives; and reverse-scale layout places their 9 supports in shared coordinates. Safe contraction preserves the homotopy type of 10 the input flag complex. The quotient tower is multiplicatively 3-interleaved with 11 the coarse-graph hop-distance Rips filtration. Verifiable distance-distortion bounds 12 give an additive guarantee between the original Euclidean and coarse-graph Rips 13 filtrations, and composite multiplicative guarantees for the tower on positive scales. 14 Across 22 datasets and 41,637 samples under a fixed configuration, CHARM 15 ranks among the top two on all 15 sample-weighted metrics for nonsynthetic data, 16 including the smallest values on all four Euclidean persistence-diagram distances. 17 It also provides 957 traceable support records across the full benchmark. On a 18 spherical shell, one certified H2 record identifies 1,578 original samples in the 19 two-dimensional view. CHARM thus combines geometric exploration with explicit 20 evidence of homological type and location.

---


### 98. [PhysDNet: Physics-Driven Gradient Amplification for Real-Time Image Dehazing](https://arxiv.org/abs/2611.10376)

**<font color=#1a73e8>作者：</font>** Rayen Dhahri, Lei Sun, Victor Javier Kartsch Morinigo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern dehazing networks are often computationally expensive and overfit to synthetic haze, limiting real-time deployment. This underscores an urgent demand for efficient, high-fidelity restoration methods that can operate on resource-constrained edge devices in practical, dynamic environments. We introduce PhysDNet, a lightweight multimodal architecture that fuses NIR imagery with sparse LiDAR depth and is trained with a physics-constrained dual-head objective. Differentiating through a fixed Koschmieder inversion induces density-adaptive gradient amplification, acting as an implicit resource allocation mechanism that concentrates learning on heavily degraded regions without increasing inference cost. PhysDNet delivers superior restoration with minimal capacity and enhanced training efficiency, facilitating real-time deployment on edge devices without increasing inference overhead. On the Seeing Through Fog benchmark, PhysDNet outperforms competitors by 1.67 dB at 5.2 times lower compute while recovering 54.9% of fog-induced detection loss. Ablations and cross-domain evaluations show that physics-guided training improves generalization, including under non-homogeneous haze that violates the Koschmieder assumption. PhysDNet further demonstrates compatibility with fixed-function NPUs, running at 29/45/99 FPS at <4 W across L/M/S variants. Code, deployment scripts and pre-trained checkpoints are available at this https URL.

---


### 99. [RefineSplat: Reconstruction-Guided Object-Centric Gaussian Splatting for Open-Vocabulary Querying](https://arxiv.org/abs/2611.10379)

**<font color=#1a73e8>作者：</font>** Yiren Lu, Disheng Liu, Sreya Srinidhi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D scene understanding aims to segment and retrieve arbitrary objects in 3D scenes using natural language queries. Most existing methods typically follow a splat-then-segment paradigm, where 3D Gaussian Splatting is first reconstructed and then augmented with labels or language features for subsequent segmentation. However, this pipeline often suffers from view inconsistency, ambiguous object boundaries, and weak object-level correspondence, especially in complex static and dynamic scenes. Building on our prior Segment-then-Splat framework, we present RefineSplat, a reconstruction-guided extension that retains its object-centric paradigm: it first tracks objects in 2D and then reconstructs each object with a dedicated set of 3D Gaussians, preserving explicit object-Gaussian correspondence for unified open-vocabulary segmentation and retrieval. To improve robustness, we further close the loop between 2D tracking and 3D reconstruction. Since off-the-shelf video trackers can produce unreliable masks that propagate errors into object reconstruction, we introduce a reconstruction-guided feedback mechanism that refines object tracking using rendered masks and multi-view consistency. Moreover, instead of assigning each object a single language embedding, we propose a viewpoint-aware embedding assignment strategy, where each object maintains multiple view-clustered embeddings to capture view-dependent semantic cues. We also introduce Blender-OVS, a synthetic benchmark of static and dynamic sequences with exact object meshes and point clouds, enabling direct evaluation of extracted geometry. Experiments on static and dynamic benchmarks show improved rendered-view segmentation and lower object-level Chamfer distances, with competitive scene reconstruction quality.

---


### 100. [Quantitative Assessment of Crystal Structure Prediction](https://arxiv.org/abs/2611.10380)

**<font color=#1a73e8>作者：</font>** Sergio Rincón, Gabriel González, Nicolás Andrade 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Crystal Structure Prediction (CSP) aims to predict a material's 3D structure from its chemical composition, with applications from energy storage to biomedical devices. Despite its importance, existing evaluation frameworks suffer from key limitations: they rely on threshold-sensitive or incomparable metrics, focus predominantly on geometric performance while overlooking physical plausibility, and fail to account for polymorphism, where a chemical composition can crystallize into multiple stable structures. In parallel, recent Symmetry-Informed CSP (SICSP) methods often report results alongside standard CSP baselines while receiving crystallographic templates at inference, which constrain the search space and make SICSP a fundamentally different task. To address these limitations, we introduce an Orientation-invariant, Polymorph-Aware, Large Benchmark (OPAL-Bench) that evaluates CSP and SICSP as separate tasks. We evaluate 7 CSP and 2 SICSP methods under OPAL-Bench across 4 datasets using threshold-free geometric and physical distance metrics. Our results show that no method dominates across all metrics, and that geometric performance is not strongly correlated with physical plausibility. We also release OPAL-CSP, an SE(3)-equivariant flow-matching baseline for the CSP track that performs competitively on geometric metrics and ranks among the best on physical ones. By unifying geometric and physical metrics under a polymorph-aware protocol, OPAL-Bench enables a more comprehensive assessment of generative quality in CSP.

---


> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

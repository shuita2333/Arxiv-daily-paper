# 📦 其他研究 | 2026年10月07日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 51. [Auditing the Privacy of Synthetic Gene Expression Data: A Unified Weighted-Distance Framework for No-Box Membership Inference](https://arxiv.org/abs/2610.04060)

**<font color=#1a73e8>作者：</font>** Owen Tucker, Lily Wang, Harutoshi Okumura 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Synthetic gene expression data is increasingly proposed as a privacy-preserving substitute for controlled-access genomic repositories, but its safety depends on empirical auditing. Membership inference attacks (MIAs) provide that audit by testing whether a patient's gene expression profile was used to train a generative model. We report a red-team study on synthetic gene expression data derived from bulk RNA-seq profiles in The Cancer Genome Atlas, released by the ELSA Health 2026 Challenge. We unify five no-box attacks under a single weighted-distance framework in which each variant differs only in how it weights genes: uniformly (baseline), by variance, by synthetic-versus-reference KL divergence, by spectral residualization removing dominant principal components, and by curated pathway membership. Against a conditional variational autoencoder, spectral residualization raises AUC from 0.8251 to 0.8951 and TPR at 1% FPR from 0.3842 to 0.5970 on pan-cancer TCGA. Biological pathway priors did not transfer across targets.

---


### 52. [Evaluating Zone-Guided Front Extraction for Glacier Calving-Front Delineation in SAR Imagery](https://arxiv.org/abs/2610.04066)

**<font color=#1a73e8>作者：</font>** Chhaya Kulkarni, Emam Hossain  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic calving-front delineation from synthetic aperture radar imagery is challenging because the front is a thin and often ambiguous boundary between glacier ice, ocean, and surrounding rock or terrain. The CAlving Fronts and where to Find thEm (CaFFe) dataset provides both binary calving-front masks and broader semantic zone masks, making it possible to study whether zone-level supervision can support front recovery. In this paper, we compare direct front prediction with zone-guided front extraction using U-Net, DeepLabV3+, and SegFormer-B0 under the same bounding-box-cropped CaFFe setting. In the direct setting, models predict the binary calving-front mask. In the zone-guided setting, the model first predicts four semantic zone classes, and the front is then extracted from the predicted glacier-ocean boundary. We evaluate both zone-level and front-level performance, include a ground-truth-zone boundary check, and examine lightweight test-time adaptation on sensor-specific and glacier-specific subsets. The results show that zone labels contain useful front-boundary information: extracting the front from ground-truth zones gives the lowest mean distance error. However, fronts extracted from model-predicted zones remain weak, even when zone segmentation scores are moderate. Test-time adaptation also does not consistently improve zone-guided front recovery. These results indicate that zone segmentation performance should not be treated as a substitute for front-level evaluation and that effective use of zone labels may require boundary-aware training, label fusion, or explicit front supervision.

---


### 53. [On architectural choices for interpretability and thermodynamic consistency in Physically Recurrent Neural Networks in the low-data regime](https://arxiv.org/abs/2610.04067)

**<font color=#1a73e8>作者：</font>** M. A. Maia, K. A. Meyer, A. M. C. M. van Gils 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we unravel the effect of different decoder architectures on the interpretability of the latent space of the Physically Recurrent Neural Network. Particular emphasis is given to a new weight normalization constraint, which acts as a regularization technique and enables robust training in the low-data regime. A brief visual exploration illustrates how these changes impact the latent space and how the fictitious stress can align with the true state of the RVE without explicit training. Reaping the benefits of a meaningful latent space, a case study illustrates how information from the microscopic level can be retrieved and incorporated into a multi-task approach that does not require extra parameters or larger training sets. Another key contribution shows that a specific architectural choice can naturally lead to a thermodynamically consistent formulation. By enforcing an adjoint encoder-decoder structure with positive scalar contributions, this modification ensures energy consistency across scales and non-negative dissipation, leading to even lower training requirements. This alternative completes the study on interpretability, inductive bias, and thermodynamic consistency, and demonstrates that data efficiency can be improved with careful architectural choices rooted in the underlying physics.

---


### 54. [Articulatory Entrainment and Coordination Complexity in Spontaneous Autistic and Non-autistic Dialogue](https://arxiv.org/abs/2610.04071)

**<font color=#1a73e8>作者：</font>** Thanushi Withanage, Carol Espy-Wilson, Elizabeth Redcay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Articulatory entrainment, the adaptation of vocal tract coordination to facilitate interaction remains underexplored in spontaneous dialogue, particularly among autistic speakers. Many prior studies have utilized task-based, phoneme-level analyses with invasive measurement techniques. Here, we introduce a speaker-independent framework to quantify articulatory entrainment in spontaneous dyadic conversations among autistic and non-autistic adults using acoustic-to-articulatory inversion and coordination complexity metrics. We examine temporal changes in articulatory coordination across interaction. Non-autistic dyads exhibit increasing coordination complexity and stronger entrainment over time, autistic dyads show moderate effects, and mixed dyads demonstrate the least alignment. Greater articulatory entrainment correlates with higher self-reported conversational success, indicating increase in coordination complexity as a marker of effective social interaction.

---


### 55. [Why Convolution Still Matters: Evaluating Inductive Biases in Cryospheric Image Classification](https://arxiv.org/abs/2610.04073)

**<font color=#1a73e8>作者：</font>** Chhaya Kulkarni, Emam Hossain  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in attention-based deep learning have motivated their adoption for remote sensing image classification; however, their benefits for cryospheric imagery, where surface states are dominated by fine-grained textures and class imbalance, remain unclear. In this work, we revisit a benchmark Greenland Ice Sheet image dataset, previously shown to favor convolutional neural networks (CNNs), to examine whether modern attention-based and hybrid architectures improve class-wise reliability. We conduct a controlled comparison between a classical CNN (AlexNet), a modern CNN (ConvNeXt-Tiny), a pure attention-based model (Swin-Tiny), and a hybrid convolution-attention model (CoAtNet-0) under identical training and evaluation protocols. Results show that AlexNet achieves the highest accuracy and the strongest balanced performance as measured by macro-averaged F1, while ConvNeXt-Tiny exhibits the highest macro-averaged AUC, indicating strong class separability but less consistent final decision quality. Class-wise analysis reveals that hybrid architectures improve recall for rare and structurally distinct surface classes, whereas convolutional models remain more reliable for texture-dominated categories. These findings highlight the importance of aligning architectural inductive bias with cryospheric data characteristics and suggest that increased model complexity does not necessarily translate to improved reliability for ice-sheet surface classification.

---


### 56. [VCURF: Virtual Camera-based Uncertainty of Radiance Fields](https://arxiv.org/abs/2610.04076)

**<font color=#1a73e8>作者：</font>** Liyan Chen, Nathaniel Burgdorfer, Philippos Mordohai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiance fields, implemented with either implicit (NeRF) or explicit (Gaussian Splatting) representations, are advancing the state of the art in novel view synthesis at a rapid pace. Even though the rendered views they generate are often compelling, they are not free of errors. In this paper, we propose a new approach for pixel-wise uncertainty quantification based on measuring the inconsistencies among renderings by the radiance field model in virtual cameras sampled near the target viewpoint. We named our approach VCURF for Virtual Camera-based Uncertainty of Radiance Fields. VCURF treats the radiance field model as a black box, only assuming that it is capable of rendering color and depth on demand. This property makes our approach applicable to both NeRF and GS models without any modification. Our experiments on a combination of datasets, radiance field models and baselines demonstrate VCURF's effectiveness in pixel-wise uncertainty estimation. We conclude the paper with findings that question the way view selection is tackled by the majority of the current literature.

---


### 57. [A study on human-agent teaming through spoken interaction: the impact of human individual traits and agent characteristics](https://arxiv.org/abs/2610.04079)

**<font color=#1a73e8>作者：</font>** Lara Gauder, Martin Bernardo Meza, Javier Krick 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-agent teams are collaborative systems where humans and agents work interdependently to achieve shared goals. The success of such teams is associated with the human's perception of the agent as a legitimate teammate. This perception is thought to depend not only on the agent's capabilities and reliability but also on social factors. We explore whether simple changes in an agent's communicative behavior can influence the human's perception of the agent's teammate-likeness. To this end, we developed a protocol based on a collaborative game requiring spoken interaction, in which a human subject and a virtual agent collaborate to identify a target object and place it on a board. Each subject interacted with two agents which provided the same task-relevant information but differed in behavior. While one was a neutral tool-like agent, the other was a team-building agent that used simple social strategies such as empathy, politeness, and positivity. Our analysis shows that the team-building agent was perceived as significantly more teammate-like, even in terms of its ability, despite both agents having identical capabilities for game-solving. Further, subjects with a higher propensity to trust automated systems and lower neuroticism tended to have a more favorable perception of the agent. Finally, we found that subjects tended to change their prosodic patterns when talking to the team-building agent, as a classifier based on prosodic features was able to predict the type of agent with better-than-random performance. A practically relevant conclusion is that minimal changes in spoken communication behavior of the agent, easily implemented in a variety of scenarios, can have a significant positive impact on the human's perception of its teammate-likeness.

---


### 58. [Towards Safer Autonomous Driving in an Open World: A Dual-Process Approach](https://arxiv.org/abs/2610.04088)

**<font color=#1a73e8>作者：</font>** Simon Janssen, Michiel Braat, Chris van der Ploeg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Before autonomous driving systems can be deployed on public roads, it is vital that these systems comply with safety standards, traffic rules, and social norms. Although neural networks trained on large amounts of driving data perform well in routine driving tasks, these models often struggle in novel situations that are not well-represented in the data. In this work, we propose a novel framework that combines a neural network for intuitive, learning-based planning in routine driving tasks with model predictive control for reasoning-based planning in unfamiliar situations, inspired by Dual Process Theory. A meta-cognitive component is designed to switch between the two, using a knowledge graph to reason about contextual risk based on explicit perceptual information and relevant traffic rules and social norms. Contextual risk is represented through risk fields, guiding both the switching mechanism in the meta-cognitive component and compliance with safety standards, traffic rules, and social norms in the reasoning-based planner. The effectiveness of our framework is tested in CARLA for variations of a typical out-of-distribution situations involving (emergency) vehicles running a red light. We show that the novel architecture reduces the number of collisions in the scenarios by 89% and improves compliance with the special right-of-way rules, compared to the NN-only planner.

---


### 59. [Robust blind unmixing: A geometric approach to overcoming basis variation](https://arxiv.org/abs/2610.04091)

**<font color=#1a73e8>作者：</font>** Dumitru Mirauta, Vladimir V. Gusev, Michael W. Gaultois 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Signal separation problems are common in science. A prominent example of this occurs during the use of diffraction or spectroscopy to identify the individual components of a mixture by measuring it. In the simplest case, the measured signal is a linear combination of basis patterns corresponding to the constituent parts. The unmixing problem is to infer all or some of these basis patterns and abundances of components from measurements of distinct mixtures. One of the core challenges of this task is the variation of the basis from mixture to mixture due to noise and the exact physics of the measurement process. This is usually addressed with tailored model-based and parametric methods that are then limited in use to specific application domains by the nature of the assumptions made. We propose a novel geometric approach to unmixing problems which views the generation of data during measurement through a metric space lens, thereby shifting the focus from parametrised models to a general relationship between basis transformations and the corresponding geometry. We take advantage of the optimal transport distances to capture commonly occurring basis variations, and use minimisation of in-class variance of candidate solutions to drive the optimisation. We pay special attention to the one-dimensional case due to its practical importance and availability of efficient distance and transport map routines. The effectiveness of our approach is demonstrated on a range of unmixing tasks using random Gaussian mixture models, simulated powder X-ray diffraction, and laboratory hyperspectral imaging datasets.

---


### 60. [UniBRep: Learning Unified Geometry and Topology for Image-conditioned B-Rep Generation](https://arxiv.org/abs/2610.04092)

**<font color=#1a73e8>作者：</font>** Haiyang Ying, Allen Tu, Jiaye Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating a boundary representation (B-rep) conditioned on a single image requires faithful reconstruction of geometry, valid topology, and support for complex shapes. We present UniBRep, a geometry-first framework that adapts a pretrained image-to-3D model to generate a feature mesh as a unified intermediate representation. Its surface provides a geometric scaffold, while spatially aligned learned features encode face-separation cues for topology recovery. Dual decoder branches generate the geometry and face-separation features; a geometry- and feature-guided construction pipeline then fits parametric surfaces, recovers boundary curves and connectivity, and assembles an explicit B-rep using a CAD kernel. Recovering topology from mesh regions avoids predefined architectural face-count limits, allowing face count to scale with shape complexity. On the standard DeepCAD benchmark, UniBRep produces valid B-reps for 80.49\% of inputs and reduces face Chamfer distance from 0.1096 to 0.0345 relative to CADDreamer. In a matched comparison, UniBRep also outperforms the HoLa public demo across all reported metrics. Further evaluations demonstrate scalability to high-complexity shapes beyond the standard 30-face range, generalization to objects outside the CAD training distribution, and qualitative transfer to real photographs.

---


### 61. [Scaling 3D Visual Grounding in Abdominal CT](https://arxiv.org/abs/2610.04095)

**<font color=#1a73e8>作者：</font>** Sam Church, Danyal Maqbool, Joshua D. Warner 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual grounding models can enhance radiology workflows by linking report findings to image regions. This is particularly valuable for 3D CT, where findings often occupy a tiny fraction of the volume. Training 3D grounding models requires large sets of paired phrases and regions, and building such datasets is expensive, requiring radiologists to annotate images by hand. We posit that this supervision is already created implicitly during routine reporting, as radiologists frequently place 2D annotations (e.g., distance measurement, arrows) on key images to make measurements and to support report interpretation. We introduce an automated pipeline that converts these routine clinical annotations into large-scale phrase-region supervision for 3D visual grounding. The pipeline links each annotation to the corresponding finding in the report through metadata matching, then uses a promptable 3D segmentation model to convert the 2D annotation into a volumetric mask. This produces phrase-mask-volume datasets without requiring additional radiologist annotation. Applied to a single institution's clinical picture archiving and communication system (PACS), our approach generated 105K phrase-mask-volume triplets from 59K abdominal CT exams. We also introduce two abdominal CT grounding benchmarks, LocusBench-Onc and LocusBench-ED, which comprise 240 oncology and 260 emergency-department radiologist-reviewed phrase-mask-volume triplets, respectively, with the latter spanning 13 distinct categories such as appendicitis, hematoma, and hernia. We further introduce LocusCT, a 3D visual grounding model trained on this dataset, which achieves hit rates of 0.725 on LocusBench-Onc and 0.773 on LocusBench-ED, substantially outperforming comparator models. These results show that routine PACS annotations are a scalable, previously unused source of supervision for 3D visual grounding.

---


### 62. [Progressive Multi-Ancestor Bit-Depth Distillation](https://arxiv.org/abs/2610.04100)

**<font color=#1a73e8>作者：</font>** Adil Mubashir Chaudhry, Osama Ahmad, Zubair Khalid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model compression strategies are widely employed to reduce memory footprint and network complexity, particularly for devices with constrained computational, memory, and energy resources. Prior works that rely on simultaneous conversion from floating-point high-precision (FP32) to integer low-precision (INT4) representations and distillation into smaller models suffer from unstable training and drastic degradation of prediction performance. To address these limitations, we propose a unified framework, known as \textbf{P}rogressive \textbf{M}ulti-\textbf{A}ncestor \textbf{B}it-depth \textbf{D}istillation (PMABD), that progressively compresses the network while transferring knowledge through a growing pool of higher-precision ancestor teachers. PMABD generates a sequence of intermediate teachers that each learn from all higher-precision ancestors and jointly supervise the final target student. This multi-ancestor, multi-stage design stabilizes ultra-low-bit quantization by lowering quantization noise profiles across training and ensuring stable quantization. Experiments on CIFAR-10/100 with ResNet-20/32/18, and Tiny-ImageNet with MobileNetV2 show that PMABD outperforms state-of-the-art compression frameworks, results in 1.06$\%$ increase in performance of W2A2 (ResNet-18/CIFAR-100) student model. We show that a saturation-based stopping criterion contributes to improve the performance of our final student.

---


### 63. [Physics is the Best Teacher: Consistency Learning for Time-Invariant Operators of Chaotic Dynamics](https://arxiv.org/abs/2610.04108)

**<font color=#1a73e8>作者：</font>** Lufang Chiang, Jiachen Yao, Thomas Y.L. Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accelerating the prediction of long-term behavior in chaotic systems is crucial in scientific computing. However, existing methods rely on numerical solvers or autoregressive models that advance one small step at a time, which makes long horizons expensive. We instead view this problem as learning the system's time-invariant evolution operator, which jumps the state across a large time span in a single evaluation. To this end, we derive the consistency equations a time-invariant operator must satisfy, with differential and compositional objectives in physical time. These equations also connect the learned operator to the physics-prescribed instant dynamics, enabling physics embedding in consistency learning. Across five chaotic systems, we find that physics-distilled consistency makes both short-term trajectories and long-term statistics more accurate. The learned operator survives temporal extrapolation and requires one-tenth as many evaluations as autoregressive rollout, offering an efficient route to long-term simulation of chaotic dynamics.

---


### 64. [The Independence Prior of SAEs Fragments Visual Concepts](https://arxiv.org/abs/2610.04112)

**<font color=#1a73e8>作者：</font>** Tommaso Mencattini, Giorgos Nikolaou, Donato Crisostomi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse Autoencoders (SAEs) decompose model activations into sparse combinations of interpretable dictionary atoms. Although SAEs are grounded in the Linear Representation Hypothesis (LRH), their objective smuggles in an additional prior: concepts across patches are treated as independent, an assumption clearly violated by natural images and by the activations they induce. We therefore specialize LRH to vision through the Markov-Field Linear Representation Hypothesis (MFLRH), which adds the missing spatial dependencies to the LRH assumptions. We thus propose Spatial-SAE as an amortized MAP estimator under the MFLRH. Spatial-SAE consistently outperforms standard SAEs in concept recovery and interpretability. Across four variants, it achieves a 96% average win rate on synthetic concept recovery and improves interpretability on DINOv2 activations, at a reconstruction cost concentrated in high spatial frequencies.

---


### 65. [Sharp Convergence and Sample Complexity of Policy Mirror Descent for Average-Reward MDPs](https://arxiv.org/abs/2610.04117)

**<font color=#1a73e8>作者：</font>** Enes Arda, Atilla Eryilmaz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy mirror descent (PMD) has a mature finite-time theory in discounted Markov decision processes (MDPs), but less is known in the average-reward setting, a more natural objective for many control applications. We give a finite-time, finite-sample analysis of PMD in ergodic average-reward MDPs built around a single master recursion that governs convergence for any critic, without external regularization. Its specializations yield linear rates for exact, inexact-tabular, and linear function approximation (LFA) updates, with a superlinear regime for exact PMD. We complement these convergence results with end-to-end sample complexities of order $t_{\mathrm{mix}}^3/\varepsilon^2$ in both tabular ($|S||A|$-dependent) and LFA ($d$-dependent) settings. Our LFA sample complexity sharpens the prior best $t_{\mathrm{mix}}^5$ mixing dependence to $t_{\mathrm{mix}}^3$, and matching information-theoretic lower bounds establish that the critic's $t_{\mathrm{mix}}^3/\varepsilon^2$ sample complexity is unimprovable in both settings.

---


### 66. [InvestigationWorlds: An Agentic Environment for Legal Investigation](https://arxiv.org/abs/2610.04129)

**<font color=#1a73e8>作者：</font>** Albert Yu Sun, Andrew Benard, Sil Hamilton 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce InvestigationWorlds, an agentic environment for legal investigation. We build on an underused artifact of U.S. civil litigation: the summary judgment motion. This motion relies upon a record composed of real evidence exhibits, and results in a court-adopted hypothesis that is treated as ground truth for the purposes of deciding the motion. Each environment is built from a real U.S. Federal Court case retrieved from Public Access to Court Electronic Records (PACER) and augmented by an attorney-validated generation pipeline that synthesizes role-tagged documents around the original record. The resulting corpus admits multiple coherent factual readings, only one of which matches the court-adopted hypothesis. Evaluating on 100 cases, we find agents often commit to incorrect hypotheses despite retrieving relevant evidence, struggling to distinguish the court-adopted hypothesis from alternative hypotheses.

---


### 67. [Dual-Scale Relational Graph Transformers for Ecosystem-Aware Fraud Detection](https://arxiv.org/abs/2610.04138)

**<font color=#1a73e8>作者：</font>** Mohsen Nayebi Kerdabadi, Xinrou Li, Yao Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Account takeover (ATO) fraud is a growing threat to digital banking, requiring effective detection while minimizing friction for legitimate customers. Production systems predominantly rely on tabular models that score sessions in isolation, discarding the relational structure of the underlying interaction network. Although graph-based models exploit relationships among sessions and network entities, they primarily reason over local neighborhoods and therefore capture only part of the problem: fraud risk depends jointly on the local relational structure surrounding a session and the evolving global state of the fraud ecosystem. We present HERMES (HEterogeneous Relational Micro--macro graph transformer Encoder for high-risk Sessions), a dual-scale architecture that jointly models these complementary scales of information. Micro-GT captures local heterogeneous graph structure through structured, relation-aware attention over a temporally safe session neighborhood. Complementing this local representation, Macro-GT models ecosystem-level context using non-anticipative climate tokens that summarize fraud dynamics, platform shifts, and infrastructure reuse, together with adaptive class prototypes that track representative fraud and benign session patterns over time. Evaluated on more than 130 million high-risk transaction sessions from a leading U.S. financial institution, HERMES consistently outperforms production and strong graph-based baselines, achieving a 44.44% relative reduction in customer friction and a 24.66% relative improvement in fraud recall over the production system. Ablation and temporal-stability analyses further demonstrate complementary gains from local relational modeling and global ecosystem context across changing fraud regimes.

---


### 68. [From Temporary Access to Persistent Surveillance: Why Matter Matters in Smart Homes](https://arxiv.org/abs/2610.04141)

**<font color=#1a73e8>作者：</font>** Nicolas Nino, Timothy Minning, Le Guan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Matter aims to unify smart home ecosystems through an open, interoperable, and secure standard, relying on cryptographic mechanisms for device authentication and data confidentiality. However, its openness also exposes protocol details, credential structures, and implementation characteristics to adversaries. We show that an attacker with temporary physical access can exploit design and implementation flaws to extract credentials and impersonate devices and controllers. These replicas integrate seamlessly into the fabric, enabling persistent surveillance and control even after the attacker departs. Notably, the attack is vendor-agnostic and requires no device-specific reverse engineering, as long as the device is not physically secured. We validate its practicality through a proof-of-concept on a simulated smart home with both commercial devices and development boards. Our findings uncover previously underestimated attack surfaces in Matter, particularly under physical access scenarios, and motivate four targeted mitigation strategies.

---


### 69. [Ideal Paths for Approximating Logistic Gradient Descent Trajectories at Large Initialization](https://arxiv.org/abs/2610.04142)

**<font color=#1a73e8>作者：</font>** Junjie Xiao, Huiwen Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern training on a new task often starts from a previously trained model rather than from scratch, raising the question of how this initialization affects the subsequent training trajectory. Classical implicit-bias results characterize the direction selected by prolonged training, but this direction alone does not provide information regarding the intermediate behavior. We address this question through a geometric approximation of full-batch logistic gradient descent (GD) trajectories on strictly linearly separable data, with large initialization of scale $R$ motivated by prior training. From any limiting normalized initial position, we use minimum-norm projection rules to construct a unique continuous ideal path consisting of finitely many linear segments. The path has two stages: negative-margin correction followed by minimum-margin growth. We prove that, after an explicit two-stage time reparameterization, the fixed-step GD trajectory divided by $R$ converges uniformly to this path on every fixed parameter interval as $R\to\infty$. Further, our quantitative error bounds account for initialization perturbations and the transition between stages. This approximation provides asymptotic formulas for peak evaluation loss and cumulative training loss. In particular, peak evaluation loss can grow linearly in $R$ even when both endpoint losses tend to zero. The cumulative losses in the correction and margin-growth stages, normalized by $R^2$ and $R$, respectively, converge to explicit limits. Experiments on controlled geometries and fixed image features complement our theoretical results.

---


### 70. [Consideration Circuits: Depth Separation and Universality Beyond a Single Softmax](https://arxiv.org/abs/2610.04143)

**<font color=#1a73e8>作者：</font>** Junjie Xiao, Huiwen Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most feature-based choice models, classical and deep, score items and apply a single softmax. We introduce consideration circuits (CC), feature-based models of multi-stage choice defined by directed acyclic graphs of multinomial logit (MNL) units. Source units assign probabilities to menu items, and internal units combine predecessor distributions using MNL weights computed from their probability-weighted feature summaries. On a three-item compromise task with fixed non-collinear features, menu-independent random-utility models (RUM), including a single MNL unit, suffer an error bounded away from zero. For CC, in contrast, we establish a sharp depth--norm separation: increasing depth from $2$ to $3$ reduces the optimal maximum taste-vector norm for error $\epsilon$ from $\Theta(\log(1/\epsilon)/\epsilon)$ to $\Theta(\log(1/\epsilon))$. The depth-$2$ lower bound holds for arbitrary width and menu-independent routing biases, while a five-node depth-$3$ circuit with zero routing biases attains the logarithmic rate. More generally, we characterize two geometric conditions that are necessary and sufficient for approximating arbitrary deterministic choice tables on finite menu families. Under these conditions, depth $3$ suffices, while depth $4$ achieves optimal logarithmic norm scaling whenever the family contains a non-singleton menu. In experiments, standalone tree circuits with fewer than $600$ parameters attain the lowest mean test negative log-likelihood (NLL) among the evaluated models on four fixed-pool benchmarks and the Expedia temporal split. As output heads, CC generalize the linear MNL readout and lower mean test NLL for every tested encoder on Expedia and Trivago.

---


### 71. [You May Be Running the Wrong Inception Crop](https://arxiv.org/abs/2610.04147)

**<font color=#1a73e8>作者：</font>** Jason Chuan-Chih Chou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A decade after its inception, Inception crop has become the standard crop-based data augmentation method for training deep vision models. Not only is its practice of uniformly sampling crop scale and aspect ratio widely adopted, but also its lower and upper bounds, with the scale lower bound being the sole exception that is sometimes tuned. It is therefore surprising that the standard implementation in the TensorFlow / JAX ecosystem samples crop scale with probability density function $f(A) \propto \frac{1}{\sqrt{A}}$ unlike the PyTorch counterpart, which follows the original description. Motivated by this discovery, we train 522 ViT-S/16 models on the ImageNet-1k dataset with various training budgets and crop scale distributions. We reach $78.78\pm0.09$ top-1 val. accuracy with 90 epochs of training budget and find that 1. Higher training budget requires stronger augmentation; 2. Lower tail of the distribution of the crop scale determines the augmentation strength of Inception crop; 3. Models trained with higher training budget exhibit sparser saliency, regardless of the crop scale distribution or weight decay. Based on 2. we revisit the performance of Beta crop, whose softer cutoff allows it to optimize model performance across training budgets with less compromise. We replicate 1. and 3. with Scion optimizer in addition to AdamW, suggesting that the results may be general.

---


### 72. [Watermarks and Fingerprints as Soft Bindings for Content Provenance: An Open-Licence Benchmark for Images, Audio and Video](https://arxiv.org/abs/2610.04151)

**<font color=#1a73e8>作者：</font>** Seyedmahdi Kazempourradi, Ramtin Mojtahedi, Behrang Mohseni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Content-provenance standards such as C2PA let a platform recover a stripped manifest through a soft binding: an invisible watermark read from the content, or a fingerprint looked up in a registry. We benchmarked both families under one protocol, restricted to openly available models whose licences we audited, on public media, with false-match rates calibrated on held-out negatives and source-level bootstrap intervals for performance estimates. For watermarking we evaluated 25 image, 7 audio and 7 video configurations from 12 methods on perceptual quality, robustness, false positives and cost; for fingerprinting, 35 methods on registries of up to 98,985 images, partial edits and adversarial attacks. PixelSeal gave the best balance for image and video watermarks and AudioSeal for audio, but the error-correcting detector of every TrustMark variant fired on 5.9 to 15.3% of unmarked images, so a verifier should test the expected payload. Among fingerprints, copy detectors trained on non-commercial data detected up to 75.5% of transformed images at a pair-level false-match rate of $10^{-7}$ and DINOv2, the best permissively licensed method, 65.0%; near-copies in a product catalogue dominated the false matches, and no detection improvement from geometric verification was observed under a matched calibration false-binding constraint in the evaluated image pipelines. On the same attacked copies the two families failed differently: the union of watermark and fingerprint successes covered 69% of image copies; fingerprints covered more audio queries, whereas expected-key watermark verification covered more video queries. Embedding a watermark moved the ISCC code of 62.0% of images past its match threshold, and platform-dependent colour conversion changed watermark bits between x86 and ARM hosts.

---


### 73. [LINK: A Corpus-Grounded Design Pattern Library for Educational Technologies](https://arxiv.org/abs/2610.04154)

**<font color=#1a73e8>作者：</font>** Lorena Lyon, Hyoungwook Jin, Vincent Cavez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Designing learning interfaces is often an ill-structured problem: effective solutions depend on learning goals, subject matter, learner characteristics, and interaction context that are difficult to generalize. Designers must integrate knowledge from learning sciences, interaction design, and subject domains when translating learning goals into interface decisions. Yet, prior efforts to connect learning theory and design have largely focused on learning activities or specific technologies, leaving interface-level design knowledge fragmented across systems. In this work, we take a bottom-up approach to surface this knowledge from existing educational interfaces. We present LINK (Linking INstructional Knowledge to interfaces), a library of 27 recurring interface patterns, organized under nine higher-level design commitments, which describe broader learning-science-grounded goals for interfaces. As part of developing LINK, we conducted a user study (N=14) with designers to evaluate LINK's generative power. Our findings suggest that LINK helps designers generate interface ideas and articulate theory-grounded rationales for design decisions.

---


### 74. [Diagnosis-Conditioned Spatial Gating and Decoder-Level Supervised Contrastive Learning for Radiology Report Generation](https://arxiv.org/abs/2610.04159)

**<font color=#1a73e8>作者：</font>** Md Mustafizur Rahman, Mylene C. Q. Farias  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology report generation models can produce fluent text while still containing finding-level inaccuracies. Diagnosis-driven methods improve generation by conditioning on predicted findings, but these predictions do not directly modify the visual patch features provided to the decoder, and global gating applies the same modulation across spatial locations. We introduce a Position-Aware Gate (PAG) that uses predicted finding representations to modulate visual patches spatially without region supervision. We also propose a Decoder-level Supervised Contrastive Loss (DSCL) that structures decoder representations using shared positive findings rather than instance identity. On MIMIC-CXR, PAG+DSCL improves clinical efficacy (CE) F1 from 0.484 to 0.502 over a matched global-gate reference, while PAG and DSCL individually reach 0.491 and 0.495. Without additional fine-tuning, the combined model achieves 0.226 CE F1 on IU X-Ray, compared with 0.211 reported by PromptMRG.

---


### 75. [Fully Homomorphic Encryption for Statistical Modeling](https://arxiv.org/abs/2610.04163)

**<font color=#1a73e8>作者：</font>** Balasubramanian Narasimhan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption allows arithmetic to be carried out on encrypted values, so that a party performing a computation need not see the data it operates on. This is useful wherever collaborating parties or sites cannot share data records or computed summaries yet need to do a joint analysis. We demonstrate the protocols needed to perform such analyses reproducibly via two packages in R, a platform widely used for applied statistics. The first, openfhe.R, is an interface to the OpenFHE C++ library, which exposes exact integer arithmetic (BFV, BGV), approximate real-valued arithmetic (CKKS), Boolean circuits, and multiparty key generation. The second is homomorpheR, which builds a small set of master/worker primitives for multi-party protocols on top of the first. Together, the two let an ordinary R statistical routine compose with an encrypted-arithmetic layer at the function-value boundary, provided the quantity crossing that boundary decomposes as a sum over sites. Two validation studies are presented: distributed stratified Cox regression, where stats4::mle() converges through an encrypted channel, and federated Cox-lasso via convex optimization using consensus ADMM, where the cross-site update is the only encrypted step. We also discuss federated similarity retrieval and two-party prediction. Throughout, the parties are assumed honest-but-curious, and threshold key generation removes the assumption that any single party holds a usable secret key.

---


### 76. [EvalResearchBench: Can AI Agents Design Their Own Evaluations?](https://arxiv.org/abs/2610.04184)

**<font color=#1a73e8>作者：</font>** Yaolun Zhang, Tianyi Xu, Yujie Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) relies on evaluation feedback to assess progress and guide further research, yet repeatedly running complex benchmarks is costly and slows iteration. Human experts reduce this cost by selecting benchmark subsets or designing compact suites. We ask whether AI agents can automate this design process and introduce EvalResearchBench (ERB), a benchmark for autonomous evaluation research. Given target materials, development references, candidate APIs, and fixed time and API budgets, an agent called the researcher selects or synthesizes tasks, implements graders, and revises them in pilot tests before freezing an executable evaluator for coding, co-work, and reasoning. We study 9 researchers and 13 candidate models and compare each frozen evaluator with 14 target benchmarks on score concordance and pairwise agreement. The best evaluators order about 75\% of candidate pairs as the targets do, below the 91\% ceiling set by disagreements among the targets. No researcher leads on every metric, and the best evaluator on development targets is not the best on sealed targets hidden from the researcher. A human-designed sample of public tasks remains a strong baseline, and the evaluator with the lowest recorded execution cost attains the highest pairwise agreement. Agents repair tasks and graders through pilot feedback, yet their evaluators can still truncate answers, exhaust the evaluation budget, or let a few questions dominate a domain score.

---


### 77. [Referring Multi-Object Tracking in Moving-Camera Videos via Global Motion Compensation](https://arxiv.org/abs/2610.04185)

**<font color=#1a73e8>作者：</font>** Hsin-Chen Pai, Jyun-Kai Wang, Yi-Cheng Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring multi-object tracking (RMOT) takes a video and a language expression as input and tracks all referred objects. Many tracking requirements involve how an object moves rather than how it appears. However, in a video captured by a moving camera, a parked vehicle may appear to move, while a moving vehicle may show little displacement. Existing RMOT methods relate motion with text but do not explicitly remove camera-induced motion. In this paper, we propose extracting residual motion across frames by estimating camera motion in driver-view videos and compare motion characteristics with the query expression. We consider the motion-matching extent and integrate it with the RMOT method's prediction result through late fusion. In the evaluation, we verify the performance gain of taking the motion compensation module as a plug-in across different RMOT hosts.

---


### 78. [Evaluating Just Noticeable Differences in Layered Opacity Visualizations](https://arxiv.org/abs/2610.04192)

**<font color=#1a73e8>作者：</font>** Caterina Ponti, Shano Liang, Lane Harrison 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Opacity is a widely used channel in data visualization, but it remains less well understood compared to channels such as color, length, size, etc. Recent work from Meng et al. investigated the impact of opacity across competing color schemes, finding that certain color schemes were associated with better participant accuracy. We examine these effects further in a controlled two-alternative forced-choice setup to determine whether opacity differences are truly equal across possible opacity comparison ranges. In a within-subjects study with 96 trials, including two competing color schemes (best and worst from Meng et al.) and 48 opacity pairs, we find little differences between color schemes but larger individual differences in accuracy. Further, results show stable performance in middle opacity ranges, with more errors occurring when comparing extreme values. We discuss potential implications for design guidelines and further study and make our study materials, analysis scripts, and data available at this https URL.

---


### 79. [CellSplat4D: PSF-Aware 4D Gaussian Splatting for Sparse Robotic Live-Cell Imaging](https://arxiv.org/abs/2610.04199)

**<font color=#1a73e8>作者：</font>** Yingda Tao, Guoyu Lu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A robotic microscope watching living cells cannot afford to look as often as it would like. Every volume it acquires costs photons the specimen does not get back, and time owed to other wells. What such a platform exists to produce is a record of individual cells through time: which cell is which from one volume to the next, and which cell divided into which two. Sampling sparsely breaks that record exactly where it matters, and the fault lies in the acquisition schedule rather than in the analysis software. We fill the gaps by reconstructing them, fitting a 4D Gaussian model to whatever volumes the hardware could afford. The model is a cloud of light-emitting blobs, each carrying a position, a shape and a lifetime. Being continuous in time, it renders any missing volume on demand, decoupling how often the robot analyses from how often it can afford to look. The microscope's point-spread function is measured from the data rather than inherited from acquisition metadata or left to the optimizer, because metadata inflates it and the optimizer cannot recover it at all: a wider blur around a smaller blob fits the images equally well. Each blob's lifetime is stored in frames rather than as a fraction of the recording, so that it denotes a fixed duration on any sequence. Unmeasured timesteps are supervised at coarse scale by a 3D U-Net that predicts the intermediate volume directly and estimates no motion field, since a dividing cell becomes two and no motion describes that. On two Cell Tracking Challenge sequences, a C. elegans embryo and a Chinese Hamster Ovarian (CHO), with fidelity scored per cell nucleus, our reconstruction holds the highest nucleus fidelity at every distance from an acquired frame, has the flattest decay across the gap, and best recovers focal planes it was never shown with graceful degradation across the gap.

---


### 80. [Sparse-GS2Mesh: 3D Gaussian Splatting Guided by Novel Stereo Views and 2DGS for Sparse View Surface Reconstruction}](https://arxiv.org/abs/2610.04203)

**<font color=#1a73e8>作者：</font>** Younghyun Noh, Minje Kim, Tae-Kyun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surface reconstruction under sparse-view settings remains challenging due to limited geometric cues. Volume rendering methods based on signed distance functions often produce over-smoothed surfaces, while 3D Gaussian Splatting (3DGS), though time-efficient, suffers from incomplete geometry due to the lack of reliable depth supervision and the limitation of being optimized only from given input views. In this paper, we present Sparse-GS2Mesh, a stereo-aware framework for surface reconstruction from sparse views. While 3DGS and stereo matching have been leveraged for surface reconstruction under dense view settings, we extend them to operate effectively under sparse view conditions by first initializing 3DGS using epipolar depth priors to mitigate the 3DGS overfitting problem, followed by our three key components: (I) adaptive baseline selection, (II) fine-tuning with a stereo matching network, and (III) 2D/3D co-regularized fine-tuning. Given a warmed-up 3DGS initialized with epipolar depth, the adaptive baseline selection automatically determines a baseline to synthesize for each sparse view. We then fine-tune 3DGS by backpropagating depth-refining gradients from the stereo matching network, effectively specializing the 3DGS for stereo matching. The 2D/3D co-regularization further helps obtain stable reconstruction, addressing weak geometric cues in close stereo views. Sparse-GS2Mesh achieves a 15\% improvement over state-of-the-art methods in little-overlap settings and comparable results in large-overlap settings. Codes will be publicly available.

---


### 81. [FTD-GNO: Memory-Efficient Graph Neural Operators through Functional Tensor Decomposition of the Kernel](https://arxiv.org/abs/2610.04212)

**<font color=#1a73e8>作者：</font>** Xiaomin Zhang, Boyue Wang, Junbin Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Operators (GNOs) provide flexible surrogate models for learning solution operators of partial differential equations (PDEs). However, standard GNOs typically parameterize the integral kernel with a monolithic neural network and evaluate kernel interactions over graph edges, leading to substantial computational and memory overhead at high resolutions or with large neighborhoods. To address these limitations, we propose Functional Tensor Decomposition Graph Neural Operator (FTD-GNO), a memory-efficient GNO framework that decouples the high-dimensional continuous integral kernel into low-dimensional mode-wise functions. By instantiating the kernel with classical tensor decomposition formats, including CP, Tensor-Train, and Tucker decompositions, FTD-GNO enables algebraic reconstruction of the integral operator without explicitly materializing full edge-wise kernel tensors. This factorized formulation reduces the memory footprint of kernel evaluation and aggregation while retaining the continuous operator-learning structure of GNOs. Theoretical complexity analysis shows that FTD-GNO substantially lowers parameter and activation-memory costs associated with high-dimensional kernel construction. Experiments show lower peak memory than the corresponding unfactorized graph-integral baselines, with shorter recorded training times. Fourier-graph experiments further demonstrate that FTD can improve the efficiency of a graph-integral layer within a hybrid operator and has good scalability.

---


### 82. [PaLoRA: Paced Low-Rank Adaptation for Continual Learning](https://arxiv.org/abs/2610.04226)

**<font color=#1a73e8>作者：</font>** Yuxuan Li, Fanhu Zeng, Hao Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LoRA-based continual learning methods mitigate catastrophic forgetting through various mechanisms, yet nearly all complement these with small learning rates as a heuristic to restrict gradient scaling magnitude. Such fixed heuristics lack theoretical guidance on how the strength of this restriction should evolve as tasks accumulate. We reveal that even under directional constraints such as nullspace projection, finite-precision updates inevitably leak into the subspace of accumulated prior knowledge along multiple directions. While small learning rates attenuate such leakage, they cannot prevent the accumulated forgetting from intensifying as the effective rank of historical knowledge grows. We show that the optimal magnitude restriction should adaptively increase with this effective rank to balance stability and plasticity, i.e., preservation of previous knowledge and acquisition of new task information. Under an anisotropic leakage model, we derive a pacing law $s^*=\sqrt{R/c}$ that characterizes the optimal scaling of gradient steps, i.e., the magnitude restriction itself, where $R$ is the effective rank of past updates. Based on this insight, we propose PaLoRA, which compresses historical knowledge via adaptive SVD truncation, projects gradients onto the nullspace of prior tasks, and applies rank-aware adaptive pacing. Experiments demonstrate consistent improvements over prior methods, with particularly strong performance in long-horizon settings, achieving substantial gains of 4% accuracy on challenging 50-task ImageNet-A and ImageNet-R benchmarks.

---


### 83. [Learning to Watermark Speech Synthesis Against Model-Driven Reconstruction](https://arxiv.org/abs/2610.04235)

**<font color=#1a73e8>作者：</font>** Weizhi Liu, Yue Li, Hui Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern TTS systems increasingly generate synthetic speech at scale for diverse users. This setting calls for content-level provenance that can verify the origin of released speech and attribute it to the requesting user, which generative watermarking can support by embedding multi-bit identifiers directly into synthesized speech. Once released, however, speech may undergo heterogeneous learned transformations during distribution and editing, with reconstruction objectives that can preserve speech utility while affecting watermark recoverability differently. We find that no single watermark carrier remains consistently reliable across reconstruction models, as its survival depends jointly on the embedded structure, reconstruction mechanism, and observation representation. To this end, we propose Thrive, a multi-bit generative speech watermarking framework for modern autoregressive TTS, covering both discrete-token and continuous-representation generation under reconstruction attacks. Specifically, Rise synchronizes watermark injection into intermediate representations with its continued integration into subsequent generation, while Care combines waveform and spectral experts using bit-wise reliability selection. Experiments on both autoregressive paradigms show that Thrive preserves synthesis fidelity, achieves 87.6% average recovery accuracy under reconstruction attacks, and supports source attribution over candidate sets of up to 10,000 identities.

---


### 84. [Stochastic Adaptive Fourier Decomposition for Operator Learning](https://arxiv.org/abs/2610.04241)

**<font color=#1a73e8>作者：</font>** Pengqing Shi, Liming Zhang, Tao Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fourier Neural Operators (FNOs) offer an efficient paradigm for solving partial differential equations (PDEs). However, FNOs rely on a fixed Fourier basis and hard frequency truncation, which inherently limit their ability to model non-periodic, localized, and fine-scale solution structures. We propose the Stochastic Adaptive Fourier Decomposition Neural Operator (SAFDNO), a spectral neural operator that replaces predefined Fourier modes with an adaptive Takenaka-Malmquist (TM) orthonormal system derived from the theory of Stochastic Adaptive Fourier Decomposition (SAFD). Instead of performing an expensive greedy pole search in classical SAFD, SAFDNO amortizes stochastic pole selection through a neural pole predictor and constructs the adaptive TM system directly from latent features. The resulting operator performs learned filtering on coefficients of analytic branches in the Hardy space with respect to the input-adaptive TM system, preserving the global receptive field of spectral operators while providing a more flexible representation than using fixed spectral bases. Across nine PDE benchmark problems, SAFDNO achieves the best performance on all six regular-grid problems among strong neural operator baselines, with especially notable gains on Darcy, Burgers, and Navier-Stokes, where fixed Fourier modes are often less effective at modeling localized oscillations, sharp transitions, and multiscale structures. SAFDNO also exhibits stronger zero-shot super-resolution performance and shows less performance degradation when deployed on finer discretizations. These results suggest that the input-adaptive TM system provides a promising alternative to fixed spectral representations for neural operator learning.

---


### 85. [Optimizer Geometry Sets the Pace: Spectral Learning Dynamics in Matrix Factorization](https://arxiv.org/abs/2610.04249)

**<font color=#1a73e8>作者：</font>** Mahalakshmi Sabanayagam, Simon Lucey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent successes of matrix- and curvature-based optimizers have renewed interest in how update geometry shapes learning. These methods normalize or precondition updates, changing how different components progress during training. In deep matrix factorization, the geometry that slows gradient descent (GD) favors low-rank solutions by delaying the emergence of small singular modes. This raises the question of what remains of that spectral bias when normalization or curvature correction weakens or removes the slowdown. We study how optimizer geometry and depth jointly govern this behavior through a common framework for singular mode dynamics. Under explicit balance and alignment assumptions, we derive birth, saturation, and decay laws for Euclidean GD, coordinate-wise updates of SignGD and an instantaneous Adam approximation, spectral updates of Muon and cumulative Shampoo, and a block curvature model of K-FAC. The resulting picture is not a simple ordering from stronger to weaker low-rank bias. To highlight, SignGD and ideal Muon eliminate the divergent birth barrier and drive unsupported modes to zero in finite time. Cumulative Shampoo initially retains GD's depth-dependent barrier, then accumulated gradients produce a catch-up phase while making previously active modes increasingly persistent. Undamped K-FAC cancels the factorization-induced slowdown while preserving the ordering of the target singular values, whereas positive damping introduces a spectral threshold below which the slow GD phase laws reappear. These results give normalization, accumulated state, damping, and depth a direct interpretation as controls determining when modes emerge, persist, and disappear during training.

---


### 86. [A Hand-Checkable Proof That Two Hidden ReLU Layers Compute the Maximum of Six Numbers](https://arxiv.org/abs/2610.04256)

**<font color=#1a73e8>作者：</font>** Dimitrios Myrisiotis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exactly computing the maximum function is a standard test case for studying depth in ReLU networks. Two hidden layers are known to suffice for up to twelve inputs through computer-assisted constructions. For six real inputs, we give an explicit hexagon identity whose local structure yields a self-contained analytical proof of this depth bound. The identity was found by computer-assisted search; we prove it through explicit cancellations that can be checked entirely by hand, without executing a verification program. The identity also yields an explicit network with hidden widths $17$ and $41$, zero biases, and rational weights.

---


### 87. [CADForge: Agentic Single-View CAD Reconstruction with Explicit Geometry Reasoning](https://arxiv.org/abs/2610.04262)

**<font color=#1a73e8>作者：</font>** Keyang Lu, Zhifei Yang, Tianao Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reconstructing editable parametric CAD models from a single-view image is of great practical value for modern manufacturing, yet remains challenging due to incomplete geometric observations and complex inter-part relationships. To address it, we propose CADForge, an agentic framework that progressively converts a single image into CadQuery programs. CADForge decomposes an object into CAD-meaningful components and performs explicit geometric reasoning for each component, a process that first identifies CAD-relevant constraints and then translates them into precise modeling parameters through mathematical code. The inferred parameters then drive component-wise synthesis of executable CadQuery programs, with a review agent evaluating the resulting geometry and providing targeted feedback for iterative refinement. To further improve robustness and efficiency, CADForge incorporates a failure-guided toolkit construction mechanism to distill accumulated experience into tools, and maintains a compact parametric CAD memory for retrieving modeling context on demand. Experiments on diverse single- and multi-part objects show that CADForge consistently outperforms existing baselines in reconstruction fidelity and perceptual quality, demonstrating an effective approach to accurate single-view CAD reconstruction.

---


### 88. [Adaptive Bregman Alternating Projections for Feasible Gromov-Wasserstein Learning](https://arxiv.org/abs/2610.04264)

**<font color=#1a73e8>作者：</font>** Aoran Zhang, César A. Uribe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Gromov-Wasserstein (GW) problem compares structured distributions without requiring a shared feature space or known correspondences, but its nonconvex objective and coupled marginal constraints make computation challenging. Bregman alternating projected gradient (BAPG) uses inexpensive alternating row and column updates, yet its fixed-penalty relaxation leaves a persistent feasibility gap. We propose Adaptive KL-BAPG (A-KL-BAPG), which combines a finite fixed-penalty burn-in with a guarded increasing-penalty phase. At each tail iteration, the method reuses BAPG's alternating updates and backtracks a delayed-power step until a Sinkhorn-inspired projective-diameter safeguard is satisfied. We prove finite termination of the backtracking at each iteration and show that the feasibility gap vanishes asymptotically. We further establish a best-iterate $O(1/\log N)$ bound for the weighted squared corrected residual and, under a support regularity condition, the existence of a stationary accumulation point for the original GW problem. This distinguishes A-KL-BAPG from fixed-penalty BAPG, whose stationarity guarantees are given for the relaxed problem. Experiments show that A-KL-BAPG achieves a favorable balance of accuracy, objective value, feasibility, and stationarity relative to BAPG variants, projection-based methods, and task-specific baselines. For synthetic and real graph alignment problems, it closely matches the accuracy and objective value of fixed-penalty KL-BAPG while reducing the marginal feasibility gap by 62-99% and the projected stationarity residual by 28-98%. Heterogeneous domain adaptation experiments show a similar pattern: A-KL-BAPG maintains comparable target accuracy and objective values while achieving better feasibility and stationarity than fixed-penalty KL-BAPG.

---


### 89. [AI-Enabled Quality Assurance for Multiple-Choice Assessment Items](https://arxiv.org/abs/2610.04267)

**<font color=#1a73e8>作者：</font>** Steven Moore, Nicholas Diana  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generating multiple-choice questions is increasingly scalable, but establishing their assessment quality remains difficult. We present a focused narrative review of automated item-writing flaw detection, revision, psychometric screening, and NLP benchmark auditing. Database searches, citation retrieval, and nominated sources yield fourteen research reports reviewed in full text. We distinguish surface checks from content-sensitive judgments and map a 19-criterion rubric to detection methods and reported evidence. High label-level accuracy often coexists with weak positive case detection, while rubric definitions and reference standards vary. Revision evidence is mixed, and the associations reported in prior work do not establish the effects of repair. We propose evaluating quality assurance as a sequence of independently validated decisions, with criterion-specific reporting, calibrated human review, and outcome-based assessment of revisions.

---


### 90. [Integrated Imputation-Classification for Supervised Learning with Missing Data](https://arxiv.org/abs/2610.04273)

**<font color=#1a73e8>作者：</font>** Yue Liu, Ben Liang, Ali Tizghadam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study supervised classification problems with missing feature values. Existing approaches often decouple imputation from classification, producing imputations that may be plausible but uninformative for prediction. Instead, we propose the Integrated Imputation and Classification Network (IICN), which jointly trains an imputer and an ${(n{+}1)}$-classdiscriminator adversarially with a single class supervised classification objective, where the discriminator learns to distinguish among the $n$ true classes and an additional ``imputed" class. We prove that at the global optimum, the imputer and discriminator together implement marginalization over missing coordinates and yield a Bayes-optimal classifier. We evaluate IICN on FashionMNIST, CIFAR-10, and tabular datasets with naturally occurring missingness. IICN outperforms classical impute-then-classify pipelines and recent generative baselines, showing strong robustness and accuracy in challenging settings.

---


### 91. [Do RUL explanations hold up? Faithfulness and stability of attributions on C-MAPSS](https://arxiv.org/abs/2610.04278)

**<font color=#1a73e8>作者：</font>** Manh Hien Nguyen, Ngoc Thanh Nguyen, Isabella Mendoza Cortes 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep remaining-useful-life (RUL) models on NASA C-MAPSS are now routine, and so are heatmaps that colour sensors and timesteps. A heatmap that looks mechanical is not the same as an explanation an engineer can act on. We train three standard architectures - a 1D CNN, an LSTM, and a small Transformer encoder - on the official FD001 and FD003 splits with the piecewise RUL cap of 125 cycles and the official PHM08 asymmetric score. We then attach three attribution maps (Integrated Gradients, occlusion, last-layer attention) and evaluate them with the checks the XAI-for-PdM literature still under-reports: deletion/insertion faithfulness, Spearman stability under sensor-scale noise, agreement across training seeds, and cosine consistency inside RUL bins. Prediction error is a prerequisite, not the claim. The headline is which explanation method moves the RUL output when its top cells are removed, and which map survives a 5% input perturbation. Integrated Gradients and occlusion are similarly faithful on the LSTM; Transformer attention is cheap and temporally smooth but weakly faithful. All three maps are almost unchanged under 5% input noise, yet IG/occlusion agree only moderately across two LSTM seeds - stability to sensor jitter is not the same as stability to retraining. A secondary tabular check on the AI4I 2020 failure dataset shows the same deletion pattern for tree importances. We recommend occlusion or IG for any C-MAPSS-style report that will be read by a maintenance engineer, and we treat raw attention weights as a visualisation only.

---


### 92. [OctMesh: A Unified Octree-Hierarchical Framework for Lossless Triangle Mesh Compression](https://arxiv.org/abs/2610.04281)

**<font color=#1a73e8>作者：</font>** Shiyu Feng, Xihua Sheng, Lingyu Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lossless triangle mesh compression must preserve both vertex positions and connectivity. Octrees support learned point cloud geometry coding and progressive refinement, but extending them to meshes requires a compatible connectivity representation. Unlike the eight occupancy decisions of a voxel, a parent edge can develop into varied child connections, making edge refinement difficult to model with a compact prediction prior. We propose OctMesh, a learned framework that codes geometry and connectivity on a shared octree hierarchy. Its key observation is that octree pooling produces parents with either one child or two to eight children. Child edges are then grouped by their endpoint parents' types and whether the endpoints share a parent. Each candidate group contains children from just one parent or two connected parents. The resulting four categories define small, fixed-shape prediction tasks: connections uniquely determined by the parent graph are inherited without bits, while three neural predictors estimate probabilities for the remaining candidates. These probabilities guide arithmetic coding of the actual edge symbols. Binarized predictions of within-parent connections provide context for predicting connections between different parents. A graph-aware parent feature extractor combines local geometry, parent connectivity and global shape. The connectivity models use dedicated weights at coarse levels and share weights at fine levels. Residual edges and a finest-level face-selection payload complete the reconstruction. On 256 frames from eight MPEG V-DMC test sequences, OctMesh losslessly recovers the finest-level vertex-coordinate, edge and unoriented face sets at an average of 7.033 bits per face, 12.8% below V-Mesh. The same hierarchical representation supports nine levels of progressive vertex-and-edge refinement.

---


### 93. [First-Order Steering: Translating Weight Adaptation into Activation Steering](https://arxiv.org/abs/2610.04283)

**<font color=#1a73e8>作者：</font>** Sri Pranav Kunda, Alexander Kurz, Tomas Dominik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering exploits interpretable directions in the residual stream to enable inference-time manipulation of model behavior. Composing steering vectors to apply multiple target behaviors simultaneously is important in various fields-including AI alignment and safety-but remains a challenge for existing activation steering methods. In contrast, prior work in model merging shows that target behaviors represented by learned weight adaptations can be combined with high accuracy. A method that translates weight adaptations into activation steering vectors could therefore extend prior work in model merging to generate composable steering vectors that better enable simultaneous inference-time behavioral control. For this, we introduce First-Order Steering, a formulation of activation steering as a first-order approximation of weight update matrices parameterized by a vector of steering strengths, and establish theoretical bounds on the approximation error of first-order steering. We then develop a novel model merging procedure, HeRD-Merging, which minimizes the first-order approximation error terms to enable higher first-order steering accuracy. Together, our method produces steering vectors that control both individual and composed behaviors more accurately than existing activation steering methods. Furthermore, HeRD-Merging matches the performance of conventional model-merging baselines, while producing weight adaptations that admit more accurate first-order steering vectors.

---


### 94. [VIGIL: Verifier-Informed Gated Improvement Loop for Spreadsheet Question Answering](https://arxiv.org/abs/2610.04287)

**<font color=#1a73e8>作者：</font>** Kang Li, Lu He, Sandarsita Guntupalli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise agents should improve from delayed feedback without allowing every correction to rewrite system behavior. We study continual harness learning for corpus-level spreadsheet question answering. Building on FiCo (Find-then-Compute), a static retrieval-and-execution backbone, we introduce VIGIL (Verifier-Informed Gated Improvement Loop). Within a question, VIGIL verifies and repairs diversely prompted Structured Query Language (SQL) candidates. Across episodes, delayed labels update only a contract calibrator and query/result-column selector. The base model, prompts, retriever, and recorded candidate pool remain fixed in the continual-learning protocol. With the gold workbook and expected type supplied, the ungated and dual-gated full-replay variants reach 82.4% and 82.0% forward accuracy over 79 documents, from a 75.8% static baseline. The dual gate has the larger retrospective gain (2.7 versus 2.3 points), and its 6.3-point forward gain has a 95% t-interval of 5.6-6.9. In a separate stricter split that excludes 16 documents and 380 questions from fitting and online promotion, the accuracy-only gate raises mean held-out accuracy across ten final harnesses from 80.3% to 86.7%. Calibrator-only adaptation gains 5.9 points, close to the combined 6.4-point gain. Yet three of 26 gate-approved updates reduce held-out accuracy relative to their incumbents, so replay-buffer non-regression does not imply held-out non-regression. MiMoTable and external-task case studies test within-task verification and reuse the same promote-or-retain discipline. Overall, the results support bounded, auditable harness adaptation while revealing where finite replay gates fail to generalize beyond their promotion buffers.

---


### 95. [A Geometric-Transformation Feature-Adaptive Manifold Restoration Method for Open-Vocabulary Semantic Segmentation of Remote Sensing Images](https://arxiv.org/abs/2610.04300)

**<font color=#1a73e8>作者：</font>** Jianzheng Wang, Huan Ni, Xiaonan Niu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The semantic information of objects in remote sensing images is typically invariant to geometric transformations from the dihedral group D4. However, SAM3-based open-vocabulary semantic segmentation (OVSS) methods often exhibit inconsistent responses to different geometric transformations. To exploit this property and improve the stability of OVSS for remote sensing images, we propose a feature-adaptive manifold repair method based on dihedral-group geometric transformations. First, we introduce multi-scale harmonic-guided D4 view selection (MH-D4VS) to select complementary candidate views from a set of geometrically transformed views. Next, we propose original-view-anchored adaptive manifold repair (OAMR), which uses the original view as an anchor and reliable cross-view information to selectively repair locally unreliable visual features. Finally, we develop pixel decoder test-time adaptation (PD-TTA) for SAM3, which fine-tunes only the parameters of the GroupNorm layers online during inference, thereby enhancing the model's ability to adapt to sample-level distribution shifts. Experimental results show that the proposed method achieves an average mIoU of 55.6% across eight remote sensing semantic segmentation benchmarks and delivers consistent performance improvements under different SAM3-based inference frameworks.

---


### 96. [What to Preserve in Recursive Computation: A Local Predictive Sufficiency Principle](https://arxiv.org/abs/2610.04303)

**<font color=#1a73e8>作者：</font>** Peilin Wang, Feng Shiyang, Hongfu Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive computation repeatedly compresses or reuses intermediate states, creating a simple tension: information that must remain useful across longer recursive paths is also exposed to more opportunities for loss before reaching the final prediction. Existing reconstruction or local-prediction objectives provide tractable supervision, but do not ensure that the retained information remains sufficient for subsequent recursive computation. We identify local predictive sufficiency with recursive predictive closure: controlling local predictive deficiencies at individual interfaces controls the resulting discrepancy at the root. We then turn this principle into a tractable training procedure. Starting from a variational characterization, we derive finite predictive tests and an empirical predictive deficiency that measures predictive value retained across compression. Its predictive sensitivities define margin-relaxed half-space constraints on parameter updates, and we project the host optimizer's proposed update onto their intersection only when predictive preservation would otherwise be violated. Across temporal graphs, language memory, vision-language-action control, and recursive self-improvement, the method matches or improves the corresponding host models under matched compression budgets, with larger gains under heavier recursive or memory demands, while better preserving predictive information across successive transformations. Crucially, the same task-agnostic predictive-preservation principle is instantiated across all four settings through host-compatible interventions while keeping the endpoint task, backbone, and evaluation protocol fixed. These results establish predictive preservation at recursive interfaces as a general training principle for recursive compression.

---


### 97. [Modeling Deletion Requests in Machine Unlearning](https://arxiv.org/abs/2610.04310)

**<font color=#1a73e8>作者：</font>** Christian Cianfarani, Aloni Cohen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning is seen as a promising approach to enable users to exercise the "right to erasure" in the context of AI models. We ask how users might influence the behavior of models when exercising this right. We define two types of behaviors that users might adopt when requesting the deletion of their data: adaptivity and collectivity. Drawing connections between the goals of users in this context and results in stochastic optimization, we demonstrate theoretical gaps between the potential effects of groups of users who do and do not display these behaviors. We then show how techniques from data valuation might be used to design deletion requesters that can significantly alter model behavior in realistic settings. In experiments on computer vision tasks, we demonstrate the differential effects of different models of user behavior and attempt to isolate the impacts of adaptivity and collectivity.

---


### 98. [From Latent Space to Jacobian Space: Measuring, Evading, and Training Against Safety-Content Accessibility](https://arxiv.org/abs/2610.04316)

**<font color=#1a73e8>作者：</font>** Mohammad Mosafer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Output-only safety monitoring sees only the end of a model's computation, yet the model computes its answer before emitting it: what it is internally poised to say is safety-critical. Jacobian-space (J-space) readouts, linear maps from hidden states to the output vocabulary via the model's input-output Jacobian, have been proposed as a window on behaviorally accessible internal content, and a first safety protocol (JADR) showed that danger recognition is readable there. What remains unknown is how this accessible content relates to the latent-space safety geometry studied by representation engineering, and how safety training shapes it. We introduce two quantitative bridges: (i) a transport-amplification profile $A_\ell$, measuring how strongly a latent safety direction is carried toward output space by each layer's Jacobian, and (ii) a paired base-vs-tuned protocol that attributes accessibility to training provenance. Across four small model pairs (135M to 1.5B, three lens-fit seeds), tuned checkpoints concentrate recognition in upper-middle layers, and at 0.5B DPO installs refusal while J-space recognition drops to chance: training can widen the accessibility gap exactly where behavioral safety looks best. A deployment audit closes the loop: monitor-aware GCG-style suffixes suppress the prompt-side monitor at zero behavioral cost at every scale; only a learned monitor rung resists its own adaptive re-attack; the training-time defense fails its re-attack at every penalty weight; steering shows the amplification profile is descriptive, not causal; and continuous-prefix optimization fails where discrete search succeeds. Safety monitoring, training, and evaluation must operate on accessibility itself, not on outputs alone.

---


### 99. [GrayShield: Bit-Level Sanitization for Transformer Model Supply-Chain Security](https://arxiv.org/abs/2610.04319)

**<font color=#1a73e8>作者：</font>** Armstrong Foundjem, Tsung-Hsien Chuang, Foutse Khomh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Transformer models such as BERT and Vision Transformer~(ViT) achieve strong performance via densely parameterized attention backbones. However, the least significant bits~(LSBs) of their 32-bit floating-point weights can be abused as covert channels to conceal malicious payloads, posing a serious threat to the AI model supply chain. We propose \GS (\GSabbr), a lightweight, post-training, zero-data sanitization method that completely replaces the declared mantissa-LSB channel with a Gray-code-guided low-transition sequence. Complete payload-independent overwrite, whether keyed or public, makes the sanitized target bits independent of the embedded payload and gives that declared channel zero capacity. Gray coding supplies overwrite structure, while a keyed per-tensor phase supplies pattern diversity. Benchmarked against seven post-training defenses on four Transformer model presets and two real-world malware payloads, \GSabbr maintains sub-$1\%$ accuracy impact and achieves $49.96\pm0.66$ percentage-point Recovery Reduction (RR) under five implemented attacker variants. Because pre-defense recovery is effectively $100\%$, RR near 50 percentage points corresponds to post-sanitization bit accuracy at binary chance. Its main empirical advantage is stable near-chance sanitization with substantially smaller weight-distribution shift than the evaluated near-chance baselines PatternMask (PM) and Post-Training Quantization (PTQ).

---


### 100. [LyapuFlow: Controlling Generative Flows with Lyapunov Feedback for Inverse Problems](https://arxiv.org/abs/2610.04326)

**<font color=#1a73e8>作者：</font>** Minseon Gwak, Hans Hao-Hsun Hsu, Danielle C. Maddix 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained flow models are now widely used as generative priors in science and vision, where inference-time guidance enables test-time constraints without retraining. Existing methods use projection, posterior sampling, or iterative optimization of the generative trajectory. We propose LyapuFlow, an alternative based on Lyapunov feedback control. At each sampling step, LyapuFlow predicts the terminal sample towards which the current flow is evolving, and evaluates the constraint violation on this prediction. Then, we compute the minimum-norm control that satisfies a prescribed Lyapunov decrease condition. The resulting control remains inactive when the uncontrolled dynamics already reduce the constraint violation at the prescribed rate. Otherwise, it provides a corrective update within a feedback trust region that prevents the control from dominating the pretrained dynamics. We demonstrate LyapuFlow in both data and latent spaces, outperforming alternatives spanning different mechanisms for test-time constraint enforcement in scientific machine learning and image inverse problems.

---


> [!TIP]
> 当前位于：**51-100**（第 2/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

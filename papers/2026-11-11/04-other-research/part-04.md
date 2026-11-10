# 📦 其他研究 | 2026年11月11日

> 本类共 **520** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

---

### 151. [Heterogeneous Asymmetric Contrastive Distillation](https://arxiv.org/abs/2611.10672)

**<font color=#1a73e8>作者：</font>** Qi Wang, Jinjia Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) between architectural families, e.g., from a Transformer teacher to a CNN student, is difficult because the two networks learn different representations. Logits share a label space, but heterogeneous teachers differ in logit offset, scale, and sharpness, and their non-target classes are less semantically organized. Conventional logit distillation matches these values sample by sample, asking the student to imitate how another architecture expresses its predictions. We argue that a heterogeneous teacher should pass on the relational structure of its predictions, i.e., how it arranges samples relative to one another, and propose Heterogeneous Asymmetric Contrastive Distillation (HACD) to transfer this structure. HACD maps teacher and student logits to centered, temperature-softened probability directions on a shared unit hypersphere, which removes architecture-dependent offsets and lets the temperature control how sharply peaked outputs enter the representation while keeping informative non-target classes. Each student output must then identify its own teacher target within the batch. Because every teacher target also acts as a negative for the others, HACD computes the targets on a moderately augmented view and contrasts both a moderate and a strong student view against them. HACD adds no learnable parameters and needs one teacher pass per sample. It achieves the best or second-best accuracy on 11 of 12 heterogeneous pairs on CIFAR-100, without ground-truth labels, and on 14 of 15 pairs on ImageNet-1K, improving over the reported vanilla KD results by 8.82 and 1.33 percentage points on average. Checkpoints are available at this https URL the code will be released upon publication.

---


### 152. [Safe Offline Reinforcement Learning using Behavior Regularisation and Latent Feasibility Guidance](https://arxiv.org/abs/2611.10677)

**<font color=#1a73e8>作者：</font>** Mahesh Keswani, Parth Bhardwaj, Ankur Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe offline reinforcement learning (RL) seeks to learn policies that maximize return while satisfying safety constraints, using a static dataset. To characterize state-wise safety, reachability analysis identifies the feasible region, defined as the set of states from which constraints can be satisfied at every future step. Policies are commonly extracted from learned value functions with advantage-weighted regression (AWR). However, AWR relies on exponentiated weights that amplify value estimation errors, whereas behavior-regularized policy gradient methods directly utilize the action gradient of the value function and often make more effective use of learned critics. We propose Feasibility-Optimized Conditional Actor Learning (FOCAL), a method that incorporates behavior-regularized policy gradients into a conditional variational autoencoder (CVAE) actor. FOCAL optimizes this policy using a first-order objective partitioned by feasibility, updating the actor to increase return on transitions estimated to be feasible and to reduce constraint violations on transitions estimated to be infeasible. During inference, FOCAL dynamically adjusts the scale of the latent prior according to the estimated feasibility of the state to adjust the conservatism of action sampling. Theoretically, we show that for AWR, the policy update variance depends exponentially on the advantage error, whereas for FOCAL it scales linearly with the variance of the value estimation error. Across the DSRL benchmark, FOCAL satisfies the constraints on all evaluated tasks while achieving competitive or higher returns compared to baselines.

---


### 153. [MGE: A Membership Guided Data Extraction Attack against Diffusion Models](https://arxiv.org/abs/2611.10678)

**<font color=#1a73e8>作者：</font>** Yuchang Mei, Longqiang Wang, Haoyang Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, diffusion models have achieved remarkable performance in image generation. However, their inherent memory properties introduce a potential safety risk of training data leakage, i.e., data extraction attack. To illustrate such risk, we propose a membership guided extraction (MGE) framework to effectively extract training data from a pre-trained diffusion model. Our core idea is to formulate the data extraction as a conditional generation, where the condition signal is from a membership inference classifier. To improve the success rate and efficiency of MGE, we propose adversarial gradient and parallel branch decoding. Our experiments on image generation benchmarks demonstrate that our MGE can extract hundreds of images, which shows that more attention should be paid to privacy-preserving of diffusion model.

---


### 154. [RetinaGuard: Risk-Controlled Agentic Triage for Multi-Disease Retinal Screening](https://arxiv.org/abs/2611.10689)

**<font color=#1a73e8>作者：</font>** Sohaib Sulman, Muhammad Atif Saeed, Akhtar Jamil 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retinal screening programmes need to know which automated decisions can be accepted without review. This paper presents RetinaGuard, an agentic triage framework in which quality, diagnostic, uncertainty, verification and explanation agents gather evidence for each fundus photograph, a learned failure predictor estimates the probability that the decision is unsafe, auxiliary tools are invoked only when their expected value of information exceeds their cost, and the acceptance threshold is certified by conformal risk control. On the RFMiD test split, RetinaGuard was compared with confidence and calibrated-uncertainty referral at matched referral budgets and equal certified safety, using two RETFound primary models of different strength. With the weaker model (macro-AUROC 0.896), verifier disagreement added significant information, RetinaGuard captured 119 of 280 unsafe decisions at a 20% budget against 88 for lowest-confidence referral, and at a nominal 5% unsafe level it accepted 37.0% of cases against 10.3%. With the stronger model (0.925) the verifier added nothing beyond uncertainty and the advantage shrank to a few percentage points. In both settings its coverage at the nominal 5% level stayed near 37.7%, gating cut computation by about 30%, and a quality agent reduced unsafe acceptances under most image corruptions. The benefit of agentic evidence gathering thus depends on how much the primary model's own uncertainty already reveals about its errors.

---


### 155. [JoVox: Joint Hierarchical Flow Matching for Lightweight Voxel Generation](https://arxiv.org/abs/2611.10690)

**<font color=#1a73e8>作者：</font>** Xiangjun Tang, Jianqi Chen, Peter Wonka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating high-fidelity voxels while keeping their lightweight nature remains an open problem in computer vision. Current generators are either high-fidelity but computationally heavy, or lightweight but of lower fidelity. Hierarchical methods keep the lightweight nature of voxels. However, their coarse levels, which decide where all finer cells can appear, are generated with the least information about the shape and are never revisited, so they are often plausible but wrong. Our key insight is to let finer cells take part in deciding coarse cells. To this end, we propose JoVox, a discrete flow matching framework that learns the joint distribution of all levels of the voxel hierarchy, instead of a separate distribution for each level, so that coarse cells can be predicted with finer cells already generated nearby. Within this framework, we further introduce a two-level prediction, which outputs the cells two levels finer at once instead of one level finer, halving the number of levels that the network processes and yielding voxels of higher fidelity. We also introduce an unmasking strategy that revisits early decisions once finer cells are generated and corrects inconsistencies in masked diffusion models. Our framework outperforms the baselines on both unconditional and image-conditioned voxel generation. Compared with the current state-of-the-art TRELLIS.2, we achieve 8x higher training throughput, 1/15 of the FLOPs in a forward pass, train on 4 vs. 32 GPUs, and obtain higher quality with an 11% lower Chamfer distance.

---


### 156. [A Geometric Theory for Nonequilibrium Transformer Dynamics](https://arxiv.org/abs/2611.10691)

**<font color=#1a73e8>作者：</font>** Aythami Bethencourt de León, Darryl D. Holm  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a variational and geometric theory based on statistical physics for the joint evolution of Transformer attention and token representations at fixed model parameters. To this end, we introduce a free energy for the attention and model the evolution of the attention weights by its Fisher--Rao gradient flow. At fixed token representations, we prove that the softmax matrix is the unique free-energy minimiser and that every positive attention trajectory converges to it. For prescribed time-dependent representations, we show that the attention dynamics becomes linear after a change to logit variables. This result yields tracking bounds relative to the instantaneous softmax and sufficient conditions for attention to converge to a fixed matrix. Hamiltonian dynamics for the representations and their momenta are then coupled to the attention relaxation driven by the same energy. This coupling results in an energy-dissipation law. We also develop two alternative Hamiltonians incorporating the attention value map. We prove global well-posedness of the attention flow and all three coupled systems.

---


### 157. [A Case Study of a Phishing Cluster Targeting German Universities](https://arxiv.org/abs/2611.10698)

**<font color=#1a73e8>作者：</font>** Raphael Springer, Alexander Schmitz, Joel Taddey 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In light of recent ransomware attacks, this study analyzes and measures the impact of cyberattacks against academic institutions in German-speaking areas. First, we provide an overview of 25 confirmed cyberattacks against universities in German-speaking areas between February 2022 and February 2023. In this time frame, we find that 5% of all German universities have experienced a confirmed cyberattack with a measurable impact. Second, we document victimology and Tactics, Techniques, and Procedures (TTP) of a phishing activity cluster spanning more than three years and showing a particular focus on universities in German-speaking areas. Of the 93 targeted universities, 58 (62%) are German, representing a significant fraction with approximately 14% of the total number of universities (423) in Germany. A notable technique is that the phishing emails are sent via university infrastructure, using valid, compromised credentials of university-associated personnel and involving university Virtual Private Network (VPN) tunnels.

---


### 158. [PLS-GS: Probabilistic Lidar Scaffolds for Compact, Surface-Aligned Gaussian Splatting](https://arxiv.org/abs/2611.10699)

**<font color=#1a73e8>作者：</font>** Krishnan Harikumar, Alejandro Fontan, Thierry Peynot 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D Gaussian Splatting (3DGS) is typically optimized from images only, many robotics and mapping applications provide both camera and high-definition LiDAR data, combining rich visual appearance with accurate geometric structure. We introduce PLS-GS, a probabilistic LiDAR scaffold for Gaussian Splatting that exploits this complementary sensing setting to construct a compact 3DGS representation aligned to the measured surface. PLS-GS fits a Hierarchical Gaussian Mixture Model jointly over position and color, yielding a continuous and adaptive scaffold that eliminates the need for discrete scene partitioning such as voxel grids or octrees. The fitted mixture then guides the renderable 3DGS Gaussians: each rendering Gaussian is associated with a GMM component and constrained in the local surface frame induced by that component's covariance. A Mahalanobis support loss bounds the deviation of the rendering Gaussians from the corresponding LiDAR-derived surface. Across five large outdoor scenes, PLS-GS places primitives markedly closer to the LiDAR measurements than both image- and LiDAR-initialized baselines, while employing substantially fewer primitives, yielding a considerably more compact model and faster rendering. At matched capacity, PLS-GS places primitives closer to the LiDAR measurements, with comparable rendering quality. Code is available at this https URL.

---


### 159. [Spectral Bias Reduction in Local Gated ReLU Architectures](https://arxiv.org/abs/2611.10700)

**<font color=#1a73e8>作者：</font>** Victorita Dolean  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks trained by gradient-based methods learn the low-frequency content of a target function faster than its high-frequency content. This spectral bias is well documented, but it is much less clear which architectural choices mitigate it and which cannot. We study the question for shallow ReLU models linear in their trainable parameters, where each mode is learned at a rate given by a Gram-matrix eigenvalue, and for a general symmetric bilinear form $a(\cdot,\cdot)$, so that least-squares regression ($a=$ the $L^2$ inner product) and variational or physics-informed losses ($a=$ the $H^1$ energy form) are two instances of one analysis.
Within this framework we propose gated local ReLU dictionaries, obtained by multiplying each ReLU feature by a hat partition-of-unity weight, in the spirit of partition-of-unity finite elements and overlapping Schwarz methods. The resulting Gram matrices are block-banded for any local bilinear form, with a block-Toeplitz interior whose matrix-valued symbol governs the spectrum.
The two forms then behave very differently. For $L^2$ regression, the symbol is bounded away from zero, the ratio is uniform in the number of windows, and the measured spread of frequency-dependent learning rates falls from $1.9\times10^{5}$ to $4.5$ at matched model size. For the $H^1$ stiffness matrix, the symbol vanishes at zero frequency: gating leaves the $\Theta(N^2)$ conditioning intact and inverts the frequency ordering instead of removing the bias. A preconditioner built from the same interior stencil will fix the spectral bias, showing that architecture alone is not enough. Experiments on $1$D regression and Poisson problems confirm the dichotomy, and the regression effect persists when the hidden-layer parameters are trained as well.

---


### 160. [R-BED: A Consequence-Aware Framework for System-Level AI Evaluation and Continuous Assurance](https://arxiv.org/abs/2611.10704)

**<font color=#1a73e8>作者：</font>** Vishal Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluations of AI systems usually report properties of a model, while decisions to deploy concern a configured system: a model together with prompts, tools, permissions, data, safeguards and an operating context. We ask how evidence about technical failures, deployment-control effectiveness and real-world consequences can be connected to defensible authorization decisions throughout the lifecycle of a deployed system. We present R-BED (Risk-Based Evaluability Design), a specification-level methodology with a fixed 6+4+3 architecture of thirteen diagnostic dimensions (technical failure, deployment controls, consequence and impact); a failure-mediated expected-loss identity that is kept separate from intended-behavior and misuse pathways; bounded evidence statuses with independence levels; a control assurance ladder; five authorization dispositions governed by eight rules; and a Continuous System Evaluation (CSE) layer in which evidence carries a configuration pin, an expiry and declared dependencies, so that a change invalidates evidence in proportion rather than wholesale. We work through a synthetic refund-agent walkthrough, with a deterministic script that reproduces every number, to show how a task-success view can miss a consequential control weakness that the procedure identifies as missing evidence. The contribution is a reproducible methodological specification. Most components are standard practice integrated into one evidence-to-decision record; the Evidence Validity Register, the authority envelope and the tier rules are proposals. None has been empirically validated, and we state seven hypotheses for independent testing.

---


### 161. [Towards Lightweight IoT Intrusion Detection: Feature Optimization and Explainable Machine Learning for Resource-Constrained Environment](https://arxiv.org/abs/2611.10707)

**<font color=#1a73e8>作者：</font>** Shaker Nawasra, Munther Abualkibash  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning-based intrusion detection systems (IDSs) can improve IoT security but often rely on large feature sets that increase computational overhead and limit deployment on resource-constrained devices. This paper presents a resource-efficient and explainable feature optimization framework for lightweight IoT intrusion detection using the CICIoT2023 dataset. A Random Forest model was used to rank feature importance and identify compact feature subsets. Experimental results show that a three-feature model achieved an MCC of 0.9622 while reducing the feature space by 92.1%, whereas a six feature model achieved an MCC of 0.9675 with an 84.2% reduction. Furthermore, a fifteen-feature model achieved an MCC of 0.9744, preserving 99.97% of the performance of the full 38-feature baseline model while reducing the feature space by 60.5%. SHAP-based explainability analysis validated the selected features and provided interpretable insights into model decisions. The results demonstrate that lightweight, explainable, and high-performance IoT intrusion detection can be achieved using only a small subset of carefully selected features, significantly reducing resource requirements with minimal loss of detection effectiveness.

---


### 162. [Quadratic Bezier Splatting with Structural Initialization for Efficient Painting Rendering](https://arxiv.org/abs/2611.10713)

**<font color=#1a73e8>作者：</font>** Jinfan Liu, Xuhan Zhan, Mengqin Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stroke-based rendering is often optimized as a pixel-level reconstruction task. This over-reliance on global error reduction not only degrades strokes into fragmented curves due to a lack of structured planning, but also allows locally defective primitives to be concealed by overlapping layers. To address these issues, we introduce a model-guided framework for stroke-audited rendering. Our framework uses Quadratic Bezier Splatting to analytically model continuous curved strokes with efficient differentiable alpha compositing. Built on this renderer, a feedforward multi-scale stroke decoder provides a structural initialization with learned stroke-scale allocation, while test-time stroke optimization supplies the reconstruction capacity needed for high-fidelity refinement. We further propose a single-stroke audit mechanism that explicitly evaluates local stroke quality, preventing defective primitives from surviving optimization through layer-wise compensation. Compared with existing methods, our approach achieves coherent layouts, improves PSNR by up to 5.46 dB, yields a 16% more compact representation, and accelerates combined renderer forward and backward computation by a factor of 220.3.

---


### 163. [Permute-then-Adapt: Weak-to-Strong Contrastive Image-Text Adaptation](https://arxiv.org/abs/2611.10714)

**<font color=#1a73e8>作者：</font>** Jinhao Li, Sarah Erfani, Lei Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-text alignment models such as CLIP are typically trained with contrastive learning, where unpaired examples are treated as strict negatives. While this assumption introduces noise by penalising semantically related pairs, existing solutions often rely on heuristic similarity thresholds that lack statistical grounding and sensitivity to dataset-specific noise distributions. In this paper, we propose Permute-then-Adapt (PTA), a framework that leverages efficient weak models to identify missed positives while controlling Type-I error relative to a conditional permutation reference, up to calibration approximation error. Unlike standard distillation or arbitrary thresholding, PTA estimates a random-pairing reference distribution from the weak teacher's similarity scores and uses its upper tail, determined by $\alpha$, to select auxiliary positives. The calibrated positive set is then trained against by a single multi-positive contrastive objective: each anchor maximises the total probability mass it assigns to its positive set. Offline calibration with the weak model adds negligible training overhead. Experiments show gains over heuristic soft-label approaches in object recognition, cross-modal retrieval, and data efficiency. Project repository: this https URL.

---


### 164. [Disentangled Stylized Image Generation via IP-Cross-Attention Rearrangement](https://arxiv.org/abs/2611.10717)

**<font color=#1a73e8>作者：</font>** Beibei Dong, Yueming Lyu, Yue Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With a solid theoretical foundation and pretraining on large-scale datasets, diffusion-based methods have achieved controllable generation leveraging text and image conditions, and generating excellent stylized images is possible using diffusion models. However, previous methods face significant challenges. First, because diffusion generation is iterative, the common approach of learning implicit style representations via cycle-consistency strategies is too costly and not well-suited to diffusion, even for LoRA-based methods. Second, decoupling style is difficult in the latent space of diffusion models. Representations of attributes are coupled in the latent space of diffusion models; thus, extracting style attributes with diffusion models usually suffers from the issue of content leakage. Furthermore, because style is hard to represent in natural language, capturing style using text prompts or textual inversion is deficient. In this paper, we propose a method for achieving disentangled stylized image generation through IP-cross-attention rearrangement, based on our experimental observations. We also propose negative content guidance, inspired by classifier-free guidance, to reduce content leakage in stylized image generation.

---


### 165. [FedSGN: Federated Sparse Grassmann Newton Learning for IoT Anomaly Detection](https://arxiv.org/abs/2611.10718)

**<font color=#1a73e8>作者：</font>** Jingjing Liu, Xiansen Ju, Xianchao Xiu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection plays a critical role in securing the Internet of things (IoT). Although existing federated principal component analysis (PCA) methods can learn the subspace of normal samples without sharing raw data, they often suffer from feature redundancy that may degrade detection performance. To address this limitation, we propose a novel and effective federated sparse Grassmann Newton (FedSGN) learning method for IoT anomaly detection. Technically, our FedSGN leverages the $\ell_{2,0}$-norm constraint on the global projection matrix to eliminate redundancy and introduces an orthogonality penalty to preserve the intrinsic structure. Moreover, we develop an augmented Lagrangian solver integrated with a semismooth Newton scheme to enable parallel client updates and Grassmann projection for robustness. Numerical experiments demonstrate that the proposed method achieves favorable overall detection performance while reducing communication overhead. The source code is publicly available at this https URL

---


### 166. [CyberBinGym: Can AI Agents Turn Binary Patches into Real Exploits?](https://arxiv.org/abs/2611.10723)

**<font color=#1a73e8>作者：</font>** Lambang Akbar Wijayadi, Zhaoqi Xiao, Zhun Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security fixes usually reach users as compiled updates, but deployment delays leave unpatched systems exposed. During this window, comparing patched and unpatched binaries can reveal how to exploit a vulnerability, turning a defensive update into actionable information for attackers. Existing benchmarks do not measure this capability: they expose source code, rely on human-crafted challenges, or evaluate binary comprehension without requiring exploitation. We introduce CyberBinGym, a benchmark containing 100 tasks derived from real vulnerabilities in 53 widely used projects, spanning six vulnerability families and three levels of analysis complexity. Agents receive stripped vulnerable and patched binaries without source code or vulnerability information, and must combine static and dynamic analysis to recover and exploit the vulnerability. Evaluation separately measures vulnerability recovery through differential crash testing and end-to-end exploitation through flag retrieval, with trajectory audits to reject reward hacking. The strongest evaluated agent recovers the target vulnerability in 88% of tasks and exploits it in 20%. Providing the patched binary raises its exploit rate from 10% to 25% on a matched 20-task subset; with standard binary hardening enabled, it still exploits two of its 20 previously successful tasks. These results demonstrate that current agents can turn released binary patches into working exploits in a controlled setting, although exploitation remains unreliable. These capabilities lower the barriers to targeting unpatched software and compress defenders' effective response window, increasing the urgency of timely patch deployment.

---


### 167. [3D Segmentation in the Clinic: A Grand Challenge](https://arxiv.org/abs/2611.10728)

**<font color=#1a73e8>作者：</font>** Bram van Ginneken, Tobias Heimann, Martin Styner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper describes the set-up of a segmentation competition for automatic and semi-automatic extraction of the liver from computed tomography scans and the caudate nucleus from brain MRI data. This competition was held in the form of a workshop at the 2007 Medical Image Computing and Computer Assisted Intervention conference. The rationale for organizing the competition is discussed, the training and test data sets for both segmentation tasks are described and the scoring system used to evaluate the segmentation is presented.

---


### 168. [LIFT: Local Metric Alignment and Foundation-guided Propagation for Few-shot Depth Completion](https://arxiv.org/abs/2611.10729)

**<font color=#1a73e8>作者：</font>** Xiang Li, Xiaojin Gong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot depth completion aims to recover dense metric depth from sparse measurements using only a small number of target-domain annotations, offering a favorable balance between annotation cost and model adaptation. We propose LIFT, a framework that harnesses both depth and feature priors from a frozen pretrained monocular depth estimation (MDE) foundation model for few-shot depth completion. Specifically, LIFT first estimates local scale and shift parameters on a coarse grid and interpolates them into smooth, dense parameter fields, providing a spatially adaptive metric depth initialization. It then progressively refines this initialization through multi-scale depth propagation guided by foundation features. Finally, a lightweight residual decoder combines multi-level foundation features with propagation correction to refine the metric depth. Extensive experiments on NYUv2 and KITTI-DC demonstrate that our proposed method achieves state-of-the-art few-shot performance. The source code will soon be released.

---


### 169. [Breaking Precision Walls in First-, Second-, and Zeroth-Order Optimizers: One Constant, Set in Advance](https://arxiv.org/abs/2611.10730)

**<font color=#1a73e8>作者：</font>** Lngel Kyo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Under power-law signal decay across directions, an optimizer can fit strong directions and miss weak ones while average loss hides it. A precision wall measures the steepest decay where the weakest direction recovers within 5% in a fixed budget. On low-rank matrix sensing and quadratics one constant sets the wall: once it dominates the denominator, Adam or grafted Shampoo is momentum descent at step $\eta/c$, setting the wall; in Shampoo, matching grafting's constant to damping restores the wall after three hypotheses failed. In zeroth-order Adam, $\varepsilon$ acts against $\varepsilon^\ast$ from a mean-square spectral model; below $\varepsilon^\ast$ error hits a noise floor. Set from true curvature or spectrum on new shapes, the rule raised the wall above the same-step default by a forecast amount: on two sensing shapes by $1.96, 1.15$ (Adam) and $1.59, 1.74$ (grafted Shampoo), and on two Hadamard-rotated quadratics by $1.12, 0.73$ (zeroth-order Adam, longer budget), rising on all seeds; fixed-step momentum at that step reaches those walls. A cosine-scheduled default (small constant giving weak modes large steps) is higher on one sensing shape, matched on new seeds of the other, and lower with the rule's constant. A default step retuned per budget catches up on rotated quadratics and population logistic regression, fails at 1 query/step on two diagonal quadratics (catching up at 16), and exceeds the rule on digits logistic regression (full-batch and minibatches, where gradient noise sets the $\eta = 0.01, 0.1$ default walls). On logistic regression the rule did not raise the first-order wall: same-step default Adam was higher (its wall on 4 new shapes at the forecast stability limit), while in zeroth order on the population loss setting $\varepsilon$ raised the wall by $0.98, 0.88$.

---


### 170. [Spectrogram-Based CNN Autoencoder for One-Class Anomaly Detection in Machining Vibration Signals](https://arxiv.org/abs/2611.10733)

**<font color=#1a73e8>作者：</font>** Sebastian Zeleny, Christian Gawron  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work presents a one-class anomaly detection framework for vibration-based condition monitoring in machining processes using a convolutional neural network autoencoder. Three-axis vibration signals acquired during industrial broaching are transformed into time--frequency spectrograms and combined into a compact three-channel representation, enabling convolutional feature learning on multivariate time-series data. The autoencoder is trained exclusively on normal process data and detects anomalous strokes based on reconstruction errors. Labeled validation data are used for threshold calibration and an independent test set is reserved for final performance evaluation. To improve sensitivity to short-lived process instabilities such as chatter, a localized residual-based metric termed Segmented Vertical Error (SVE) is introduced. Experimental results on approximately 10{,}000 broaching strokes show a clear separation between normal and anomalous process conditions under strong class imbalance. The processing pipeline is additionally evaluated on an external public turning dataset as a proof of concept, indicating preliminary applicability beyond the original broaching setup. The results suggest that spectrogram-based autoencoder models can provide a practical and scalable basis for one-class anomaly detection in industrial vibration monitoring.

---


### 171. [The Lagrangian Brain: A Constraint Mechanics of Mind and Machine](https://arxiv.org/abs/2611.10737)

**<font color=#1a73e8>作者：</font>** Yuhang He, Si Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A brain is in one state at a time, yet most of what decides its next state is absent from it: the patterns its world never produces, the statistics of a lifetime, a goal that lies ahead. In mechanics a wire acts on a bead only through a force that appears when the bead presses on it, and Lagrange computed such forces with one multiplier for each constraint. We propose that a brain follows the same mechanics. Everything a circuit knows, is told or wants is a constraint on its single state and acts through its own multiplier, which accumulates the violation and pushes the state back. Neurons and synapses carry the multipliers, each with its own time constant: inhibitory interneurons carry what never happens, adaptation the cost of staying in one state, synapses the statistics of experience, and feedback to apical dendrites the future. From this hypothesis follow Dale's law, the reciprocal wiring and balance of excitation and inhibition, the paradoxical responses of cortex and the frequencies of brain rhythms. Belief becomes the time one trajectory spends in each state, learning becomes sleep proposing laws and waking refuting the false ones, and planning becomes a wave from the goal meeting a wave from the present. Connectionism and symbolism are the limits of frozen and of instantaneous multipliers, and between them the time a circuit runs becomes the depth of its computation. A machine built on these principles, trained without gradients on 1000 solved puzzles, solves all 422,786 Sudoku-Extreme test puzzles with one trajectory each. It rediscovers the rules of Sudoku by sleeping and waking, plans shortest paths in mazes of 64 times the training area, and tracks permutations exactly on strings 25 times longer than in training, where Transformers fail. A mind, on this view, is life that learns its own constraints.

---


### 172. [Pulse waveform morphology encodes haemodynamic signatures of impending stroke](https://arxiv.org/abs/2611.10739)

**<font color=#1a73e8>作者：</font>** Cheng Ding, Jiaming Liu, Jian Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Stroke is a disorder of the circulation, yet the haemodynamic state that immediately precedes it has rarely been observed, because continuous physiological recordings before a stroke are seldom available. Photoplethysmography (PPG), recorded by every pulse oximeter and by hundreds of millions of wearable devices, captures the peripheral pulse beat by beat, but its morphology is largely discarded. Here we ask whether pulse waveform morphology encodes haemodynamic signatures of impending stroke. Using in-hospital stroke as a natural experiment that provides continuous PPG before physician-adjudicated stroke recognition, we studied intensive-care (MIMIC-III, $n=176$) and emergency-department (MC-MED, $n=154$) cohorts and described each beat with interpretable descriptors of pulse timing, amplitude, contour and variability. At a nominal 360-min horizon, morphology separated pre-recognition from stable windows with $F_1$ scores of 0.941 and 0.989 (sensitivity 0.998 and 0.980), with models transferred unchanged to the second cohort, and outperformed heart rate alone on identical windows. The signature was dominated by systolic crest time and its change from each patient's own baseline, feature attribution was concordant across cohorts (Spearman $\rho=0.865$), and morphology recorded in the first two hours of care stratified the subsequent clinical course ($F_1$ 0.714 and 0.691). In high-risk patients without stroke, 29% and 14% of windows were positive, but five-window persistence rules limited alerts to 17% and 2% of patients. The results demonstrate that the routinely recorded pulse thus carries haemodynamic imprint of the period preceding stroke, positioning pulse morphology as a candidate continuous cerebrovascular biomarker.

---


### 173. [Writer-independent handedness identification from offline Bangla handwriting under controlled acquisition](https://arxiv.org/abs/2611.10744)

**<font color=#1a73e8>作者：</font>** Tanzim Hasan Prappo, Sayeed Hassan, Sayem Ali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handedness is a soft-biometric cue for forensic document examination and writer profiling, yet reported accuracies from offline handwriting rarely keep writers, texts and image acquisition apart, so models may recognise the writer or capture conditions rather than the writing hand. Such controlled evidence is missing for Bangla. Using our BanglaHand dataset of 42 writers (21 left- and 21 right-handed), who each wrote six shared prompts and two own texts under controlled collection and photography, we evaluate handedness identification with all images of each test writer held out, whole-writer permutation tests and photometric controls. An ink-gradient descriptor identified the handedness of unseen writers with 77.4% balanced accuracy (95% writer-bootstrap interval 67.7-86.5%; p=0.001) and frozen ImageNet embeddings with 69.5-72.0%. Part of this signal is stroke darkness: in a post hoc analysis, right-handed writers' strokes were darker at their centres for equal stroke width, consistent with higher pen pressure and not explained by lighting drift. With ink density and brightness regressed out, the descriptor still reached 64.5% (p=0.027), whereas writing-only shape features were weaker (60.8%; p=0.090). Handedness is thus identifiable from offline Bangla handwriting under controlled acquisition, and photometric controls are essential to interpret such cues.

---


### 174. [Constrained Look-ahead Guidance for Interference-Aware Flow Editing](https://arxiv.org/abs/2611.10751)

**<font color=#1a73e8>作者：</font>** Doudou Zhang, Qi Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow models enable powerful generative modeling, but controlled editing remains challenging due to the need to balance source fidelity and edit compliance along the generative trajectory. We propose a principled, inversion-free framework for flow-based image editing from a trajectory centric perspective. Rather than relying on inversion or heuristic guidance, we introduce a one-step look-ahead mechanism that evaluates the effect of candidate updates on both edit and fidelity rewards estimated via denoising, and adjusts the current update based on this evaluation. At each step, our method applies reward-driven corrections guided by the look-ahead evaluation under an explicit fidelity constraint, resulting in stable and coherent trajectory evolution. This look-ahead design mitigates gradient interference between edit and fidelity objectives by anticipating their interaction in future states, leading to improved trade-offs. Experiments demonstrate that the proposed approach achieves stronger semantic edits while better preserving source content compared to existing strong baselines.

---


### 175. [Unified Framework with Convex-Concave Decomposition and Sparse Topological Learning for Skeleton-Based Clinical Assessment](https://arxiv.org/abs/2611.10758)

**<font color=#1a73e8>作者：</font>** Quang-Anh N. D., Duc Pham Minh, Minh-Anh Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton-based rehabilitation assessment faces fundamental limitations of fixed topologies which cannot model compensatory patterns, uniform joint treatments overlook clinically important deviations, and lack of geometric understand- ing. We propose Concave-Convex Decomposition Sparse Topological Graph Convolutional Network (CC2-STG), a multi-stream model that combines geo- metric decomposition, sparse feature learning, and adaptive topology. Our framework decomposes joint relationships into complementary convex-concave distance functions to model both local and global movement characteristics, with sparse regularization with proximal optimization selecting clinically relevant geo- metric features, while multi-scale topological analysis captures non-anatomical joint dependencies in pathological movements. Experiments on the KiMoRe and UIPRMD datasets validate the effectiveness of our approach, achieving state-of-the-art performance on clinical pathological movement assessment.

---


### 176. [ConwayNet: Interpretability, Activation Coherence, and Noise Resilience via a Game-of-Life-Inspired Lateral Inhibition in Artificial Neural Networks](https://arxiv.org/abs/2611.10760)

**<font color=#1a73e8>作者：</font>** Yair Cohen, Scott M. Gilmore  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks achieve universal function approximation by stacking interconnected nonlinearities, but as a consequence they are sensitive to noise and resist mechanistic interpretation. In contrast, the local update rules of cellular automata, such as Conway's Game of Life, give rise to not merely interpretable but programmable dynamics. We explore a bridge between these worlds: a lateral inhibition in neural networks based on continuous Game-of-Life rules that derives inhibitory and excitatory responses from the layer input and blends them into the activation map in a state-conditioned way. The mechanism is differentiable and architecture-agnostic, and its regulation is imposed rather than learned: the rule's parameters are fixed and are not optimised, while the rule's values and derivatives shape training throughout the network. Wired into fully connected, convolutional, wide-residual and graph convolutional networks, it gives rise to several properties. Activation maps become coherent across space, depth and seeds, with coarse structure persisting through depth while fine detail is renewed at every layer. The co-activation graph of the hidden units departs from an Erdős--Rényi random graph: it is laid out on the image and its giant component grows in steps, as in a spatial graph. Networks started from nearly identical initialisations, under label noise, disagree on thirty times fewer test images. Saliency maps rest on the object rather than the background, and resilience to pixel noise not seen in training is substantially improved.

---


### 177. [Cascading Circle Loss: Order-Preserving Contrastive Learning for Graded Legal Retrieval](https://arxiv.org/abs/2611.10765)

**<font color=#1a73e8>作者：</font>** Rayane Kimouche, Ahmed Touila  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces Cascading Circle Loss (CasCL), a contrastive learning framework for legal retrieval tasks with graded relevance. CasCL combines an InfoNCE objective for positive-negative separation with a cascade of ranking boundaries that model ordered relevance levels between queries and legal clauses. The framework also includes a negative-aware self-paced optimization mechanism and a relevance gain weighting strategy to improve ranking quality. Experiments on legal passage retrieval benchmarks show that CasCL consistently outperforms existing methods, including InfoNCE, Circle Loss, MNRL and Margin MSE, across both binary retrieval and graded ranking metrics.

---


### 178. [How reliable is an embedding of the seabed? Repeat-look measurement of frozen encoders on synthetic aperture sonar](https://arxiv.org/abs/2611.10770)

**<font color=#1a73e8>作者：</font>** Harold Horsley, Oscar Pizarro, Hayat Rajani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained encoders from self-supervised representation learning are increasingly applied to sonar imagery of the seafloor, where they are evaluated with protocols that take one embedding per target. A target patch of seabed, by contrast, is re-imaged from an alternate look on overlapping survey passes, so each embedding is one measurement of that target. Standard protocols cannot say how consistent those measurements are, or how much of their spread belongs to the patch and how much to the acquisition geometry. We treat this as a measurement-reliability problem. Using a synthetic-aperture sonar (SAS) survey, we measure the repeat-look reliability of embeddings from a frozen natural-image encoder (DINOv3 ViT-S/16). Standard single-look metrics, effective rank, clustering and a linear probe for coral, are all stable to the look, and the probe performs well (AUC 0.93). Yet the repeat-look reliability of the same embeddings is poor, with a distance-based intraclass correlation (dbICC) of 0.20 and nearest neighbours and clusters that barely agree across looks. This contradiction resolves as we find the probe learns a stable direction, whose ICC of 0.60 is 3.0 times that of the full embedding. Variance components, calculated from generalizability theory, attribute under a tenth of the within-cell spread to look acquisition geometry. The rest is cell-specific and cannot be separated without repeat passes at matched geometry. A sonar-pretrained encoder (BenthicDINO) and a classical SAS texture descriptor show the same pattern. For this dataset and the tested representations, uses that depend on patch identity fail, such as cross-pass comparison and retrieval, while uses at the level of habitat type (e.g. coral classification) do not. Because the standard metrics did not detect this, we argue that repeat-look reliability should accompany any evaluation of representations of the seafloor.

---


### 179. [WorldFoundry: Towards Unified Infrastructure for World Intelligence](https://arxiv.org/abs/2611.10771)

**<font color=#1a73e8>作者：</font>** Juanxi Tian, Jiadong Hou, Baiang Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual generative models increasingly blur the line between synthesizing observations and simulating environments. Yet visual plausibility alone does not constitute successful world modeling: compelling outputs may lack persistent state, physical dynamics, or causally consistent responses to interactions. We define a generative world model as a predictive dynamical system that maintains a persistent, history-conditioned representation of an environment, updates that representation in response to actions or interventions, and generates temporally coherent trajectories that reflect outcomes under observed and counterfactual interventions. From this definition, we derive an intelligence-oriented framework spanning perceptual grounding, persistent state modeling, controllable transformation, dynamics-aware prediction, and closed-loop interaction. We present WorldFoundry, open-source infrastructure for reproducible inference and evaluation across video, 3D and 4D, embodied action, and interactive world systems. WorldFoundry unifies model and benchmark discovery, runtime and asset preparation, execution orchestration, artifact management, and interactive visualization, while modality-specific adapters preserve native inputs, execution semantics, output representations, and evaluation protocols. Explicit manifests, durable artifact contracts, and evidence-aware scorecards separate execution readiness from evaluative claims, making each claim traceable to its supporting artifacts. The catalog contains 270 model entries, 74 benchmarks, and 62 registered metric entries, with readiness and execution evidence recorded separately. WorldFoundry enables reproducible comparison of persistent, controllable dynamics across heterogeneous systems, advancing the field from perceptual synthesis toward measurable world intelligence.

---


### 180. [Universal Approximation by Equivariant Message-Passing Graph Neural Networks with a Bilinear Readout](https://arxiv.org/abs/2611.10772)

**<font color=#1a73e8>作者：</font>** Pingbing Ming, Han Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove universal approximation for the bilinear-readout equivariant message-passing network (BREMP), a reference architecture for equivariant graph neural network interatomic potentials. Its layers combine equivariant convolutions with affine maps, and its readout forms invariants from products of the equivariant features. We construct a one-layer feature that determines the local environment up to permutations of atoms of the same type. The construction uses spherical harmonic filters of degree no larger than the largest number of neighbors at a common distance from the center. Iterating the construction recovers the environment reachable in as many hops as there are layers, using the same bound on filter degrees at the layer cutoff. The readout approximates every continuous invariant function of the features uniformly on compact sets. Together these give universal approximation of atomic energies at a prescribed physical range using a shorter layer cutoff. We assume that, throughout the admissible class, message passing reaches all neighbors in each physical environment within a common number of layers. Finally, DPA4, an interatomic potential architecture in production use, inherits this result by approximating the BREMP layers constructed in the proof and realizing the bilinear readout.

---


### 181. [Same Measurements, Different Velocity Risk: Complementary Rolling-Shutter Readouts under Clock Uncertainty](https://arxiv.org/abs/2611.10774)

**<font color=#1a73e8>作者：</font>** Lunshuo Tian, Dongheng Liu, Mingwei Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera rigs with identical measurement budgets can have different velocity estimation rates when exposure timing is uncertain. We establish this distinction for rolling-shutter reconstruction with two calibrated moving anchors, unknown scene points, and independently unknown auxiliary poses and clocks. On the same fixed local physical class near a separated lateral rig, repeated readouts have worst-case squared velocity risk at least of order $\sigma\rho_{\mathrm{eff}}$, whereas complementary readouts have minimax risk of order $\sigma^2$, for a fixed admissible clock displacement $\rho_{\mathrm{eff}}>0$ as the noise standard deviation $\sigma$ tends to zero. A finite physical compensation path gives the lower bound; a nonlinear velocity inverse proves complementary stability. All motion, structure, pose, and clock nuisances remain unknown. We identify mounting configurations in which both designs become regular and quantify the risk floor induced by metric uncertainty. We quantify full-parameter domains with independent 6-ms clocks and test in-domain reconstruction under paired noise and a depth-offset intervention. Raster studies examine image formation and calibration sensitivity.

---


### 182. [EEGFaceSem: An EEG Benchmark with Paired Generative Latents for Semantic Visual Modeling](https://arxiv.org/abs/2611.10781)

**<font color=#1a73e8>作者：</font>** Jun Ma, Michiel M. Spapé, Keith M. Davis III 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) is widely used to measure brain activity for brain-computer interface applications for its non-invasive nature and high temporal resolution. However, progress in modeling the neural responses to visual semantics has been limited by a reliance on fixed image collections that lack the fine-grained control needed to isolate fine-grained changes in visual features and their relation to perception. In this work, we present EEGFaceSem, a large-scale dataset pairing high-quality EEG with photorealistic face images synthesized from a generative model. We provide the generative latent vector for each stimulus, enabling research into the continuous mapping between a visual latent space and neural representations. Each participant's brain responses were recorded while they attended to specific semantic features (e.g., smiling, hair color) in a rapid serial visual presentation paradigm. The dataset contains EEG signals from 30 participants, totaling 67,200 time-locked EEG recordings. We present benchmarks for single-trial semantic classification under single-subject, cross-subject, and subject-adapted settings, as well as for cross-subject voting that aggregates per-stimulus predictions across participants. We further demonstrate the dataset's unique utility with two complementary applications: deriving semantic directions in the latent space for brain-supervised image editing, and conditioning a generative model on brain-decoded labels for brain-supervised image generation. Our dataset paves the way for advancing brain-computer interfaces (BCI) for semantic-level visual saliency detection and brain-supervised generative modeling. Our dataset and code are openly released at OSF (this https URL) and at HuggingFace this https URL.

---


### 183. [WARP-JEPA: World-Model-in-the-Loop Amortized Rollout Planning for Frozen Hierarchical Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2611.10806)

**<font color=#1a73e8>作者：</font>** Junjie Li, Zhaojiacheng Zhou, Kaixiang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hierarchical Joint-Embedding Predictive Architectures (H-JEPA) enable long-horizon visual control but rely on costly test-time gradient descent for planning. Our analysis reveals that iterative optimization consumes up to 97.7% of episode runtime and that low predicted rollout costs do not necessarily translate into successful control. We further identify a planning-horizon asymmetry between long-horizon top-level composition and short two-step subordinate planning. To address these challenges, we propose WARP-JEPA, a hierarchical amortized planning framework that replaces online gradient optimization with learned multi-candidate trajectory proposers while keeping the world models frozen. WARP-JEPA combines a lightweight world-model-in-the-loop causal Transformer at the top level with parallel residual MLPs at subordinate levels. The proposers are trained using model-based rollout costs and best-of-K behavior cloning, enabling efficient candidate selection without test-time gradient optimization. Across 30 frozen H-JEPA models on four benchmarks, WARP-JEPA achieves 9.6-18.8x faster episode inference on long-horizon tasks (2.9-3.0x on Cube) and improves task success by up to 33.3 percentage points. These results demonstrate that amortized planning can substantially improve both inference efficiency and control performance without retraining the world models. Code is available at this https URL.

---


### 184. [STAR-VF: Spatio-Temporal Aware Representation Condensation for Data-Efficient Video Fusion](https://arxiv.org/abs/2611.10811)

**<font color=#1a73e8>作者：</font>** Yuchen Xian, Yunqiu Xu, Guosheng Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video fusion aims to integrate complementary cues from heterogeneous sources, producing visually informative videos with coherent spatio-temporal structures. Jointly learning cross-modal complementarity and temporal dependencies typically relies on large-scale, high-quality video datasets, whose storage and repeated use during optimization incur substantial costs, making data-efficient learning highly desirable. To address this challenge, we rethink video fusion from the perspective of dataset condensation and propose STAR-VF, the first framework that condenses spatio-temporal representations for data-efficient video fusion. STAR-VF condenses the original training set into a compact set of learnable spatio-temporal representations, which are decoded into synthetic video clips and optimized using feature-level supervision provided by a frozen proxy model. The resulting condensed data preserves fusion-relevant spatial and temporal cues without requiring ground-truth fused videos as supervision. To adapt fusion learning to condensed representations, we equip the final fusion model with flow-free inter-frame temporal modeling and query-driven intra-frame aggregation, enabling direct temporal interaction and adaptive selection of fusion-relevant information in representation space. Extensive experiments on infrared-visible, multi-exposure, multi-focus, and medical video fusion benchmarks demonstrate that STAR-VF, trained with only approximately 1/16 of the original temporal training set, achieves fusion quality comparable to methods trained on the full data. Further analyses validate the contributions of learned condensation and flow-free temporal modeling, and demonstrate the robustness of the condensed supervision across different proxy encoders and downstream fusion models. Project page: this https URL.

---


### 185. [ATHENA: Hypergraph-Based Learning for Toddler Autism Classification from Eye-Tracking](https://arxiv.org/abs/2611.10818)

**<font color=#1a73e8>作者：</font>** Quang-Anh N.D., Duc Pham Minh, Thao Pham Phuong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this work we proposed a architecture designed for the classification of ASD in toddlers using eye-tracking data, addressing the critical need for early and precise detection. The proposed model incorporates FMMix, a feature-level augmentation technique that bolsters the model's learning capacity, and in this work we proposed the ATHENA, which captures intricate feature relationships via an adaptive hypergraph framework. Evaluated on two datasets dataset of gaze coordinates-the model achieves state-of-the-art performance, with AUC scores of 99.80% and 99.86%, respectively. It also exhibits high accuracy of 98.45% and 98.56%, sensitivity 98.01% and 98.10%, and specificity 98.74% and 99.02%, respectively. Demonstrating its superior ability to identify subtle gaze patterns associated with ASD, these results significantly surpass existing methods, highlighting the model's potential for clinical ASD screening. Future efforts will focus on validation across broader populations and integration with multi-modal data to further refine diagnostic accuracy.

---


### 186. [AmodalBox: Automated 3D Bounding Box Annotation under Partial Visibility](https://arxiv.org/abs/2611.10821)

**<font color=#1a73e8>作者：</font>** In-Jae Lee, Namtae Kim, Robert Exley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in vision foundation models (VFMs) has made automated open-vocabulary 3D bounding box annotation increasingly feasible by jointly leveraging LiDAR point clouds and images. However, partial observations remain a major challenge in sparse driving scenes, where visible LiDAR points often cover only a small fraction of the object's surface and provide insufficient cues for estimating its full spatial extent. As a result, existing methods often produce mislocalized boxes or leave objects unlabeled. To address this limitation, we propose \textbf{\Ours{}}, an automated annotation framework that leverages image-generated 3D assets as amodal geometric priors for partially observed objects. By establishing correspondences between input images and rendered views of 3D assets, \Ours{} robustly aligns canonical amodal geometry with partially observed world-space LiDAR point clouds. To improve temporal consistency and reduce computational cost, \Ours{} generates a single asset per instance, estimates its metric scale once at a single frame and propagates it across frames for dynamic instances, and aggregates multi-frame observations for static instances. 3D object detectors trained on annotations from \Ours{} improve performance over strong baselines by 14.1 mAP on the nuScenes dataset and by 12.45 AP at IoU 0.5 for the vehicle class on the Waymo Open Dataset (WOD). Our project page is available at: \href{this https URL}{this https URL}

---


### 187. [Learning When to Think: Adaptive Internal Computation for Reinforcement Learning](https://arxiv.org/abs/2611.10822)

**<font color=#1a73e8>作者：</font>** Rohit Kumar Salla, Simon Stepputtis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Iterative neural policies usually spend the same computation on every decision, although the benefit of additional processing varies across states. We introduce Adaptive Internal Computation (AIC), an iterative policy that learns when to stop refining its latent representation and act. In AIC, we train action selection and stopping jointly, an expected-depth penalty values computation and intermediate value predictions provide auxiliary supervision. We show that when only some states benefit from further refinement, an ideal state-dependent allocator outperforms every state-independent stopping schedule at the same expected depth. With at most eight refinement steps per decision, AIC executes 3.3 steps on average across twelve benchmark tasks and lowers per-decision latency by 31--44% relative to a fixed eight-step policy on four control and robotics tasks. Its mean reward exceeds the best fixed-depth policy on seven tasks and trails it on four. Ablating adaptive stopping and value supervision separately shows that stopping accounts for most of the reward gain on PickCube and AntMaze, where it also executes more refinement steps and that supervision accounts for most of it on RareEvent.

---


### 188. [A Gamified Framework for Conflict-Driven Design: Discovering Strategies for Collaborative Resilience with Multi-Agent Learning](https://arxiv.org/abs/2611.10841)

**<font color=#1a73e8>作者：</font>** Jin Gao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conflicting stakeholder objectives make it difficult to coordinate investments in urban resilience. We model conflict-driven urban design as a non-zero-sum digital board game in which stakeholder agents allocate scarce resources and balance individual payoffs against shared urban development and resilience objectives. We use multi-agent reinforcement learning (MARL) to train policies and examine their behavior across three settings. On a 4 x 4 board, learned policies reach about 84% of the total return found by a simulated annealing benchmark. On an 8 x 8 board with spatial and resource constraints, trained agents favor projects that improve resilience in self-play. In a 12 x 12 simulation initialized from historical maps of Tatsumi, Tokyo, trained agents achieve a mean total score of 452.1, compared with 357.3 for a random-policy baseline across 10,000 simulation runs. Gains in adaptability, sustainability, flood resistance, and greenery come with reductions in vitality and density. A human-in-the-loop interface supports replay and lets participants take over stakeholder decisions, providing a testbed for exploring these trade-offs in participatory urban planning.

---


### 189. [Factor Rank: A Canonical Algebraic Generalization of Tree Decision Diagrams](https://arxiv.org/abs/2611.10842)

**<font color=#1a73e8>作者：</font>** Alexis de Colnet, Stefan Szeider  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tree decision diagrams (TDDs), recently introduced by Capelli et al. (SAT 2026), are representations of Boolean functions. They generalize OBDDs by replacing variable orders with vtrees. The width of a TDD counts the distinct subfunctions across each vtree cut. Counting subfunctions is blind to linear structure. We introduce algebraic tree decision diagrams (ATDDs) by replacing this count with the rank of the cut matrix. The maximum of these ranks over all cuts, the factor rank, is exactly the width of the ATDD. Every TDD can be converted into an ATDD of no greater width. An ATDD is a tree tensor network in canonical form. ATDDs are exponentially more succinct than TDDs, and quasi-polynomially more succinct than structured deterministic DNNFs. Our main result is that this gain in succinctness does not cost canonicity. ATDDs are the first strict canonical form for a rank-based representation over arbitrary vtrees. For each function and vtree there is exactly one ATDD, over the rationals and without any genericity assumption. The canonicity admits a local characterization. Whether a tree tensor network is the ATDD of the Boolean function it computes can be checked in polynomial time from its tensors alone. Equivalence checking becomes a test of syntactic equality. The operation set includes polynomial-time model counting, weighted model counting, and a test whether a tree tensor network represents a Boolean function.
Capelli et al. asked for the complexity of changing the vtree of a TDD and suggested local vtree changes. We answer the question. After a rotation of the vtree at one node, the new ATDD differs from the old one in two tensors only. Vtree change runs in output-polynomial time both for TDDs and for ATDDs.
We formalize and verify our core results in Lean. We provide a prototype implementation of TDD and ATDD compilers as a first empirical validation.

---


### 190. [Fine-resolution land-use segmentation and synthetic image-label augmentation in the Kathmandu Valley](https://arxiv.org/abs/2611.10847)

**<font color=#1a73e8>作者：</font>** Pranil Parajuli, Sugam Dahal, Kiran Chandra Dahal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parcel-scale land-use data is missing for most rapidly urbanizing Global South cities, as current segmentation architectures rely on multispectral imagery and planned layouts. We introduce a hand-annotated six-class land-use corpus covering 202 km$^2$ of Kathmandu Valley across 408 fine-resolution RGB scenes. The dataset is uniquely challenging: RGB spectral similarity is high, class imbalance approaches 100:1, and key structural features like rivers measure just two to three pixels wide at a standard hierarchical decoder's prediction stride. Evaluating five architectures reveals that standard random data splitting conceals massive spatial leakage. Switching to a strict sequence-block split drops performance by up to 0.095 mIoU. This penalty exceeds the performance gap between the architectures themselves. We modified the SegFormer baseline by integrating a half-resolution residual detail path, boundary-reliability reweighting, a topology-aware loss, and a presence-balanced sampler. Adding only 1.9% more parameters, the enhanced architecture improves mean IoU across every test fold, with gains concentrated in rare, thin-structure classes. However, both models achieve identical results on the external LoveDA benchmark. Finally, augmenting with diffusion-generated pairs at matched compute degraded accuracy across all architectures, especially harming rare classes it aimed to improve. This demonstrates that blindly incorporating synthetic data can severely damage performance, highlighting a critical need to rigorously evaluate and filter generated samples before training.

---


### 191. [KeyASRBench: Measuring Whole-Phrase Keyword Preservation in Real-World ASR](https://arxiv.org/abs/2611.10852)

**<font color=#1a73e8>作者：</font>** Guanzheng Wei, Ziyi Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Public automatic speech recognition (ASR) benchmarks increasingly report low sequence error rates, yet production systems still use hotword lists, contextual biasing, retrieval, and post-correction. This motivates a complementary question: does a transcript preserve selected names, products, technical terms, versions, and relational phrases? We present KeyASRBench, a bilingual pilot that operationalizes occurrence-based Keyword Error Rate (KER) over frozen whole-phrase annotations. The 10-hour model-conditioned challenge set contains 1,501 Chinese and English clips with 4,723 keyword occurrences. Across five locally inferred checkpoints and two official API systems, language-specific MER/WER ranges from 5.31% to 12.91%, while KER ranges from 13.61% to 33.81%. A disjoint 30-minute model-blind control yields KER of 10.65%-27.31%. The control confirms that selected-phrase errors extend beyond challenge-set selection.

---


### 192. [Representing Tensors as Compositions for Efficient Computation on Sparse and Structured Data](https://arxiv.org/abs/2611.10855)

**<font color=#1a73e8>作者：</font>** Valérian Rey, Praneth Paruchuri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a new mathematical formalism in which all kinds of tensors and of operations on those tensors are represented as simple function compositions. Tensors are functions from indices to values. An element-wise operation (e.g. an activation function) is a composition with a function applied to values; re-indexing (e.g. reshape, transposition) is a composition with a function applied to indices; and a reduction is a composition with both an index function, mapping each index to several indices, and a reduction operation (e.g. product, sum, max). Combined with tensor stacking, these compositions can represent most interesting kinds of tensors (e.g. dense, jagged, all kinds of sparsity patterns, matrix factorizations), as well as lazy versions of almost every operation available in modern tensor computation frameworks, including einsums between tensors of any kind. Identities between compositions can then be used to rewrite such expressions into equivalent ones, without evaluating them. For instance, the product of two sparse matrices can be rewritten so that only products between non-zero values are computed, turning a sparse problem into a dense one. Using this algebra as the intermediate representation of a tensor computation engine would shift the focus from defining operations on tensors (e.g. einsum between sparse tensors) to defining an algebra on index functions. This should reduce the codebase complexity from $\mathcal{O}(mn^2)$, with $m$ the number of binary operations between tensors and $n$ the number of tensor types, to $\mathcal{O}(m + k^2)$, with $k$ the number of types of index functions. A draft implementation of a tensor computation framework based on this algebra is publicly available.

---


### 193. [Self-contained Data Cleaning for Unsupervised Anomaly Detection](https://arxiv.org/abs/2611.10856)

**<font color=#1a73e8>作者：</font>** Jordan F. Masakuna, Ahmed Yacine, Djeff K. Nkashama 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training datasets for unsupervised anomaly detection are often assumed to be anomaly-free, but in practice, they frequently contain malicious or anomalous contamination. This contamination severely degrades the dependability and security of downstream detection models. While some contamination-robust methods exist, they rarely generalize across different model architectures and typically rely on a priori knowledge of the contamination ratio\textemdash information that is rarely available in real-world security operations. In this paper, we propose a novel, self-contained preprocessing framework for anomaly detection that identifies and removes training set contamination without relying on known contamination ratios. Our approach performs a dynamic analysis of the cosine similarity between each data point and its reconstruction during the early training stages of an auto-encoder, mapping points into a dynamic space where anomalous regions naturally exhibit lower density. By executing ``hard cleaning''\textemdash removing all identified anomalous candidates from the training pool\textemdash we systematically improve data quality. Because this cleaning occurs at the data level, the security and reliability improvements generalize seamlessly across various downstream anomaly detection architectures. Evaluating our framework across 8 distinct models and 10 security-relevant datasets, our approach achieves up to 100\% contamination reduction, yielding average improvements of 11.2\% in F1 score and 7.3\% in classification accuracy.

---


### 194. [Polynomial Denoisers on the Image Manifold: Volterra Networks for Self-Contained Pixel Diffusion](https://arxiv.org/abs/2611.10857)

**<font color=#1a73e8>作者：</font>** Siddharth Roheda, Rohit Chowdhury, Amit Satish Unde 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural images are often conjectured to lie on a low-dimensional manifold within the high-dimensional pixel space. Recent work leverages this to build self-contained pixel-space diffusion models without specialized machinery or pretrained components. A plain Transformer on raw image patches suffices, provided it predicts the clean image rather than the noise and compresses each patch through an aggressive bottleneck. The mixing operator, however, has remained softmax attention, inherited from sequence modeling rather than derived from denoising. For Gaussian noise, the optimal denoiser admits a canonical expansion in polynomial functionals of the observation, the Wiener--Volterra series. We prove that softmax attention, and any normalized mixing rule (including linear attention), cannot realize any polynomial map beyond an affine one. In contrast, Volterra layers realize this class directly and, on a data manifold, achieve approximation rates governed by the manifold dimension rather than the ambient pixel dimension. We therefore propose the architecture these results prescribe; raw image patches passed through a bottleneck embedding, followed by cascaded low-rank Volterra layers, which carry no activation function because each layer is nonlinear in its own right. To our knowledge this is the first pixel-space diffusion architecture whose mixing operators are Volterra layers throughout, with no attention, no convolution, no pretrained components, and no activation function on the residual path. On ImageNet $256 \times 256$ and $512 \times 512$, the resulting model is competitive with self-contained pixel-space diffusion at matched parameter and FLOP budgets.

---


### 195. [Beyond Bit Matching: Orthogonal Watermarks for Collusion-Resistant Image Fingerprinting](https://arxiv.org/abs/2611.10858)

**<font color=#1a73e8>作者：</font>** Zhakshylyk Nurlanov, Tobias Weißberg, Florian Bernard  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image fingerprinting assigns each distributed copy a user-specific watermark for source tracing. Averaging collusion is a central threat: several recipients can average their differently marked copies to suppress each individual mark. Discrete bit-string watermarks are especially vulnerable because averaging drives bit evidence toward ambiguous decisions. We introduce \textbf{VectorMark}, which maps user keys to near-orthogonal high-dimensional unit vectors and identifies colluders by cosine similarity to the extracted watermark direction. Under ideal averaging of $K$ vector keys, the normalized average preserves a cosine signal of order $1/\sqrt{K}$ for each colluder, while unrelated keys remain concentrated near zero. The spherical geometry of random directions gives a shifted-Beta null distribution for cosine similarities, enabling analytic per-key false-positive-rate control after validation on unwatermarked images. VectorMark uses a neural watermark encoder and centered extractor trained with JND masking and a progressive curriculum for photometric, geometric, and collusion robustness. Experiments on MS-COCO, OpenImages, and AI-generated images show that VectorMark maintains robust watermark attribution under photometric and geometric distortions, and achieves the best strict all-colluder detection among evaluated methods, while preserving high visual quality. Our code is publicly available: this https URL

---


### 196. [Structurally Separated DAG Learning with Multi-Scale Normalized Closure](https://arxiv.org/abs/2611.10860)

**<font color=#1a73e8>作者：</font>** Shuai Feng, Hao Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous DAG learning commonly enforces acyclicity through scalar functions of a weighted adjacency that aggregate evidence from weighted closed walks. We add a complementary layer: matrix-valued closure logits---explicit multi-hop structural relation scores for each ordered pair---supervised alongside data fit, sparsity, and a DAGMA-style barrier on the weighted adjacency. The distinction is not scalarization of the overall objective but how path evidence is represented and exposed before aggregation. SMNC (scale-normalized multi-scale closure) builds these scores on a structural gate by repeated squaring in log space and divides each scale by its path-length budget, counteracting product-style attenuation along long cycles; diagonal entries support node-wise cycle supervision and off-diagonals optional pairwise reachability cues. In the linear model, a bounded structure--magnitude factorization ties strong effective edges to strong gates; a nonlinear induced gate offers another construction with the same intent. For sufficiently strong cycles, normalized logits admit a length-independent lower bound; under a unique-active-cycle assumption, the hard final-scale readout yields a polynomial log-gate gradient factor rather than exponential product-style decay. On cue-free, unstandardized Gaussian linear and nonlinear ER benchmarks, these models improve over DAGMA, run with default hyperparameters at a reduced budget, on denser graphs and are close to it on sparse ones.

---


### 197. [SWXAI: A Unified Multimodal Explainability Library for Space Weather Forecasting and Heliophysics](https://arxiv.org/abs/2611.10861)

**<font color=#1a73e8>作者：</font>** Benedict Antonio Mervyn, Anli Ji, Manolis K. Georgoulis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Space weather forecasting and heliophysics increasingly rely on machine learning models that process heterogeneous inputs such as multi-viewpoint multi-wavelength solar images and rasters, multivariate time series, spatial annotations, and tabular event-level data. However, explainability workflows remain fragmented across libraries, model interfaces, and output formats, limiting reuse and reproducibility. We present SWXAI, an open-source library that unifies explainable AI (XAI) workflows for image, time-series, and tabular data in space weather forecasting and heliophysics. SWXAI provides a common, extensible interface across commonly used vision, time-series, and tabular learning models, with validation, adaptation, and persistent explanation objects. It also includes domain-grounded examples, reproducible notebooks, tests, and documentation, enabling users to inspect outputs, swap models or explainers, and extend workflows to new heliophysics datasets. SWXAI reduces modality-specific engineering overhead and supports comparable, reusable explanations across heterogeneous scientific machine learning pipelines. A benchmark against direct backend implementations shows that SWXAI substantially reduces the code users write to produce an explanation, with no practical runtime cost.

---


### 198. [Stochastic Port-Hamiltonian Gaussian Processes for Learning from Noisy Dynamics on Lie Groups](https://arxiv.org/abs/2611.10864)

**<font color=#1a73e8>作者：</font>** Thribhuvan Rapolu, Luke McLennan, Chandrajit Bajaj  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning predictive models for dynamics is difficult because observations are often sparse and noisy, while the underlying dynamics evolve on nonlinear configuration manifolds and are affected by environmental dissipation and stochastic disturbances. Standard neural dynamics models can fit short-term trajectories but often violate physical structure, accumulate error over long horizons, or rely on parameterizations that introduce singularities such as gimbal lock. We introduce LieSPHGP, a stochastic Gaussian-process framework for learning rigid body dynamics with port-Hamiltonian structure and stability-aware robustness. LieSPHGP represents motion on Lie groups and Lie algebras, enabling coordinate-consistent optimization without singular parameterizations. Learned mass, potential energy, dissipation, and control components retain physical roles and a separate diffusion term represents stochastic forcing. Each component is modeled by Matérn kernel Gaussian processes which capture uncertainty induced by noisy observations. To improve physical validity, Lie group exponential map updates preserve rotational constraints, while positive-definite damping ensures nonnegative deterministic energy dissipation. The implicit-explicit integrator additionally provides unconditional stability for the frozen linear damping subsystem. The resulting model learns predictive dynamics that are robust to noise, respect rigid body geometry, and capture both intrinsic motion and environmental dissipation. Experiments on various noisy rigid body benchmarks show improved prediction accuracy, stronger long-horizon stability, and better satisfaction of manifold constraints compared with neural dynamics baselines. Code, data and interactive results are available on the project website: this https URL

---


### 199. [Interactive Person Retrieval with On-the-Fly Visual Feedback](https://arxiv.org/abs/2611.10869)

**<font color=#1a73e8>作者：</font>** Lyucheng Qian, John Yuehan Zhang, Pingyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional text-based person retrieval (TPR) assumes that a witness provides a complete description at once, whereas interactive person retrieval (Inter-PR) refines a partial description through question-answer exchanges. In this setting, the questioner inspects retrieved candidates to decide what evidence to request next, while the answerer sees only the witness-side memory and cannot report candidate-specific visual differences. Existing methods mainly learn offline question orderings, leaving this visual-feedback loop underexplored. To address this limitation, we introduce visual-feedback interactive person retrieval (VFI-PR), a new interactive retrieval paradigm in which retrieved candidates produce visual feedback that becomes evidence for subsequent questioning and re-ranking. To support training and evaluation in this setting, we construct VFI-PEDES, a dataset and evaluation protocol for visual-feedback interaction, and propose VFI-ReID, a framework that learns to use visual feedback during interactive person retrieval. Through the Dynamic Accumulated-evidence Retriever (DAR) and retrieval-aware question optimization, VFI-ReID adapts retrieval and question generation to evolving evidence states, turning visual feedback into complementary evidence for subsequent retrieval. Experiments show that VFI-ReID consistently improves retrieval across VFI-PR interaction stages, demonstrating the utility of visual feedback for interactive person retrieval and outperforming existing Inter-PR baselines.

---


### 200. [Online Imitation Learning for Stabilizing Vlasov--Poisson Plasmas](https://arxiv.org/abs/2611.10870)

**<font color=#1a73e8>作者：</font>** Xiaofan Xia, Qin Li, Wenlong Mou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of controlling instability in the Vlasov--Poisson plasma systems, a fundamental challenge for nuclear fusion control. Motivated by the partial observability of plasma states in practice, we investigate imitation learning algorithms that learn from a fully-observable expert controller, but operate under macroscopic measurements. We theoretically establish a separation between online and offline imitation learning --- even a small behavior cloning error leads to error compounding that exponentially amplifies instability over time. By way of contrast, the online imitation learning loss can polynomially control the stability of rollout trajectories. We then propose a DAgger-style algorithm that learns the stabilizing controller under partial observability. Simulation results on a 1D Vlasov--Poisson system demonstrate that our algorithm can effectively stabilize plasma instabilities over longer time horizons than behavior cloning.

---


> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

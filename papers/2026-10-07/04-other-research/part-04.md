# 📦 其他研究 | 2026年10月07日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 151. [WASP: Weakly Aligned Spatiotemporal Pairs for Fetal Brain MRI-Ultrasound Learning](https://arxiv.org/abs/2610.04601)

**<font color=#1a73e8>作者：</font>** Francesco Correnti, Gabriele Magrini, Marco Mistretta 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic Resonance Imaging (MRI) is widely regarded as the optimal sensor for fetal brain analysis due to its superior soft-tissue contrast and anatomical detail. However, its high cost and operational burden make it invasive and difficult to obtain at scale. Ultrasound (US), in contrast, is cheap, safe, and routinely acquired, and as a result it has produced substantially larger datasets and a growing ecosystem of pretrained models. This asymmetry raises a natural question: Can we teach a US-only model to understand fetal MRI from only a limited set of examples? The standard recipe, training a foundation model on subject-to-subject paired MRI-US scans, is not viable since no such paired fetal dataset is publicly available. In this paper we address this gap with Weakly Aligned Spatiotemporal Pairs (WASP), a framework that formulates cross-modal correspondence as an entropic Optimal Transport problem driven by clinical metadata, in particular Gestational Age (GA) and diagnostic planes, enabling the fitting of a lightweight alignment module that lifts MRI representations into the US latent space, without fine-tuning the backbone. Empirically, WASP yields its largest gains when MRI is unseen by the model during pretraining (on USFM, GA estimation error drops from 21.9 to 17.4 days and standard plane classification accuracy climbs from 61.9% to 69.0%), while providing smaller, backbone-dependent refinements for backbones pretrained on both modalities (e.g., BioMedParse GA estimation error from 6.5 to 6.0 days and SAM-Med2d plane accuracy from 83.3% to 88.1%). Code is available at this https URL.

---


### 152. [Organize Primitives into Semantic Parts: Reinforcement Reasoning for 3D Segmentation](https://arxiv.org/abs/2610.04602)

**<font color=#1a73e8>作者：</font>** Xiaoming Gong, Ruoyu Wu, Zhenhong Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Primitive-based 3D segmentation offers a compact and explicit alternative to dense surface prediction, naturally supporting structural abstraction and boundary localization. However, geometric decomposition alone does not determine how primitives should be organized into semantic parts: a single part may span multiple primitives, while geometrically similar or touching primitives may belong to different parts. We therefore introduce RePart (Reinforcement Part Reasoning), which formulates primitive-to-part organization as a finite-horizon Markov decision process and learns semantic organization through trajectory-level reinforcement reasoning. RePart constructs a Composable Primitive Workspace from fine-grained superquadrics and applies a merge-and-stop policy whose decisions are optimized by their downstream effects on the resulting partition rather than local primitive compatibility. The inferred part identities are then mapped back to the original mesh through Boundary-Aware Surface Labeling, preserving accurate surface boundaries beyond the primitive approximation. On PartNet, RePart achieves the strongest results across all four aggregate partition metrics; on 3DCoMPaT++, it obtains the highest RI and SC without target-dataset fine-tuning. These results demonstrate that reinforcement reasoning provides an effective mechanism for organizing geometric primitives into semantic parts while retaining dense segmentation accuracy. Code is available at this https URL.

---


### 153. [ConEx: Human-Interpretable Saliency Maps via Concept-Aware Attribution](https://arxiv.org/abs/2610.04605)

**<font color=#1a73e8>作者：</font>** Yehonatan Elisha, Oren Barkan, Ziv Weiss Haddad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many visual explanation methods in computer vision highlight pixel importance but struggle to link these low-level cues to semantically meaningful concepts, limiting their interpretability and trustworthiness. We introduce Concept-based Explanations (ConEx), a novel framework that bridges saliency visualization with concept-based reasoning to provide both faithfulness and interpretability. ConEx automatically discovers class-specific concepts and represents them through concept activation vectors (CAVs), learned without manual supervision using an architecture-specific masking mechanism that reduces noise introduced by the segmentation masks to enhance concept purity. ConEx generates faithful saliency maps that reveal where each concept appears in the image and how it contributes to the prediction. To evaluate the reliability of these learned concepts, we propose two complementary metrics, Vector-Concept Match (VCM) and Concept-Class Match (CCM), that quantify concept alignment and enable direct comparison with existing methods. Extensive experiments across diverse settings demonstrate that ConEx achieves state-of-the-art performance on faithfulness, segmentation, and concept-quality benchmarks. Overall, ConEx advances the field toward truly interpretable and concept-grounded explanations in vision models.

---


### 154. [Sparse-View 4D Gaussian Splatting via Spatiotemporal Priors and Generative Assistance](https://arxiv.org/abs/2610.04606)

**<font color=#1a73e8>作者：</font>** Shengqi Wang, Zhengxian Yang, Kaiwen Tian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a 4D Gaussian Splatting framework for the Sparse-View Track of the SIGGRAPH Asia 2026 Volumetric Video Challenge, which requires dynamic scene reconstruction from only six cameras with wide baselines. To achieve robust dynamic reconstruction under such sparse views, our framework integrates three components. (1) Region-adaptive spatial priors: We use foreground masks to guide Gaussian initialization and mask voting to control densification separately for the dynamic foreground and static background. Background geometry is regularized using monocular depth aligned to metric scale. (2) Motion-consistent temporal priors: We provide supervision at intermediate times through frame interpolation and constrain projected Gaussian motion with estimated optical flow. (3) Generative assistance: We place virtual cameras in the widest angular gaps and restore their rendered images using a diffusion-based model conditioned on camera poses. The restored images are iteratively incorporated into training as pseudo-supervision. On the validation set, our framework improves full-frame PSNR from 25.60 dB for the baseline to 29.75 dB. On the official test benchmark, it achieves 30.04 dB full-frame PSNR and 27.88 dB foreground PSNR, ranking first overall in the Sparse-View Track.

---


### 155. [Backward-Consistent Diffusion Sampling for Sparsely Observed PDE Inverse Problems](https://arxiv.org/abs/2610.04624)

**<font color=#1a73e8>作者：</font>** Yida Pan, Muhammad H. Ashiq, Chanyong Jung 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recovering Partial Differential Equation (PDE) coefficient fields from extremely sparse observations is a severely ill-posed inverse problem for which generative machine learning methods (e.g., diffusion models) have become a leading way to encode the prior. Recent state-of-the-art diffusion solvers lift these priors to function spaces, finding a physics-consistent reconstruction in the output space of the diffusion denoiser. We prove that, in a discontinuous PDE setting, output space methods can result in failure to appropriately minimize the unobserved error with the correct coefficient field. Consequently, we propose Function space Backward-Consistent Sampling (FunBCS), an input space optimization approach for solving PDE problems which aims to find the best input such that the denoiser reconstruction is physics-consistent. We then prove that FunBCS appropriately minimizes the unobserved error, unlike output space optimization methods. Per our theoretical analysis, we also provide insights on how to dynamically allocate the number of input space optimization steps used throughout the sampling process. Our evaluations, across four PDE inverse problems (including the discontinuous Darcy flow), demonstrate that FunBCS reduces the reconstruction error by $27$-$64\%$ while running $1.4$-$2.1\times$ faster when compared to the current state-of-the-art.

---


### 156. [Task-Sensitive Geometry of Representation Transfer for Object Detection under Image Degradation](https://arxiv.org/abs/2610.04627)

**<font color=#1a73e8>作者：</font>** Van Vung Pham  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection under image degradation can benefit from clean-image supervision, but aggregate gains do not imply that transferred representation changes are uniformly useful. We study how clean task knowledge affects degraded-image representations and whether local responses to structured representation directions can be characterized geometrically. Using paired clean and Gaussian-degraded BDD100K images, we show that clean-teacher distillation improves observed detection accuracy while producing heterogeneous object-level transfer. We isolate a representation component complementary to direct clean-teacher alignment and map it into the distilled student space through an orthogonal bridge. Controlled interventions rescue 13.22% of objects lost under the distilled representation, versus 4.30% under norm-matched random perturbations, with very low harm on preserved objects. We introduce task-sensitive geometry, a gradient-derived channel-space geometry constructed from normalized detection-loss gradients. On a reserved cohort, mapped-complement orientation within this frozen geometry is positively associated with local intervention-response magnitude after controlling for intervention magnitude (partial Spearman $\rho$ = 0.242, 95% CI [0.108, 0.359]). The relationship eplicates on independent data ($\rho$ = 0.180) and with RT-DETR-L ($\rho$ = 0.227), but not for the direct clean-teacher residual family, and it weakens for large interventions. Routing rules and specialized distillation objectives based on these signals do not yield statistically reliable gains over CLEANKD. These results support a local, direction-family-dependent task-sensitive geometry while showing that converting such structure into improved global training remains an open problem.

---


### 157. [Does Neural Complexity Improve Health Misinformation Detection? A Leakage-Controlled Cross-Corpus Benchmark](https://arxiv.org/abs/2610.04636)

**<font color=#1a73e8>作者：</font>** Mkululi SIKOSANA  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Increasing architectural complexity is often assumed to improve health misinformation detection, yet reported gains are difficult to interpret when studies use different corpora, preprocessing pipelines, data splits, and leakage controls. This study provides a controlled cross-corpus benchmark of five compact neural architectures (1D-CNN, LSTM, BiLSTM, CNN-LSTM, and CNN-BiLSTM), a soft-voting neural ensemble, and three classical machine-learning baselines using COVID19-FNIR and CONSTRAINT. Exact-text duplicate controls were applied before modelling; all neural systems used a common preprocessing and optimisation protocol, and neural results were repeated across three random seeds. On COVID19-FNIR, the deep ensemble achieved a mean macro-F1 of 0.9963 and ROC-AUC of 0.9994, while individual neural models ranged from 0.9945 to 0.9957 macro-F1. On CONSTRAINT, the ensemble achieved macro-F1 of 0.9272 and ROC-AUC of 0.9811, whereas a linear SVM achieved macro-F1 of 0.9574 and ROC-AUC of 0.9931. Architecture rankings changed across corpora, and simple sparse linear models remained highly competitive. The findings show that model complexity does not provide a stable performance advantage and that benchmark construction can dominate architecture choice. The study contributes a reproducible, leakage-controlled basis for evidence-driven model selection in health misinformation classification

---


### 158. [Policy as Data: Replay-Based Policy Dual Averaging via Advantage Regression](https://arxiv.org/abs/2610.04638)

**<font color=#1a73e8>作者：</font>** Nianli Peng, Geoffrey J. Gordon, Kianté Brantley  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Actor-critic methods reuse past experience to improve sample efficiency. However, historical data are typically regarded as off-policy samples for the current policy-improvement update. This work introduces Regularized Dual Averaging Actor Critic (RDA2C), which assigns a distinct role to replay. In regularized dual averaging, the subsequent policy is determined by accumulated policy-improvement feedback, so historical advantage estimates contribute directly to the actor objective rather than solely to the most recent update. RDA2C stores state-action samples with critic-estimated advantage labels, fits a dual score model $Z_\theta$ to the aggregated dataset, and derives the current policy from the accumulated score model using the entropy mirror map. In this way, replay defines an empirical dual objective from which the policy is computed. To analyze RDA2C, we establish a finite-time value-gap decomposition, separating the regularized dual-averaging term from errors due to stale-replay supervised fitting, critic bias, finite-buffer variance, and replay coverage, and stating the assumptions under which each error is bounded. RDA2C accepts advantage labels from any critic. With GAE labels, RDA2C outperforms PPO on six of eight MuJoCo tasks and eight of twelve Atari games. RDA2C also outperforms AAPDA, the closest dual-averaging baseline, on six of eight MuJoCo tasks. With twin-$Q$ labels, RDA2C matches SAC at matched batch size and update frequency.

---


### 159. [Revisiting the Generalization of Neural Graph Edit Distance Models](https://arxiv.org/abs/2610.04644)

**<font color=#1a73e8>作者：</font>** Zhouyang Liu, Ning Liu, Yixin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural approaches to Graph Edit Distance (GED) have achieved strong results under standard within-dataset evaluation, but much less is known about how well these models transfer across graph collections. We conduct a systematic study of this problem using exact GED supervision across diverse graph datasets and a broad set of representative learning-based methods. Our results reveal a pronounced gap between within-collection performance and cross-collection transfer. Models that perform well on their training collections often lose this advantage when evaluated on structurally different data. Training on multiple source collections substantially improves zero-shot transfer and provides a better starting point when limited supervision is available for a new target collection. Further analysis shows that transfer behavior varies with the source--target direction and the structural characteristics of the collections involved. These findings suggest that conventional within-collection evaluation provides only a partial view of the generalization behavior of neural GED models and motivate broader evaluation across heterogeneous graph collections.

---


### 160. [Gated Target Propagation for Compositional Generalization in Continual Learning](https://arxiv.org/abs/2610.04649)

**<font color=#1a73e8>作者：</font>** Abdel Mfougouon Njupoun, Colin Bredenberg, Blake Aaron Richards 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning is typically framed as acquiring new knowledge without catastrophically forgetting previous tasks. However, a flexible continual learner should also be able to reuse and recombine previously acquired knowledge to rapidly solve novel task compositions. We introduce Gated Target Propagation (GaTaP), a continual learning algorithm in which task-specific gating variables---learned through a closed-form inner loop update---selectively suppress or enhance network modules. Network parameters are learned in a slower timescale outer loop, using the same local difference target propagation error signal as is used for adapting gating variables. We provide tractable experiments on class-incremental learning scenarios for both multilayer perceptron and convolutional network architectures. We show strong performance retention on previously learned tasks, as well as compositional generalization to unseen tasks, achieved through few-shot gain adaptation at inference. We analyze learned gating patterns and find that related tasks exhibit similar gating patterns, suggesting that inferred gates capture meaningful, reusable task structure. Overall, GaTaP provides a powerful framework for jointly ameliorating catastrophic forgetting and enabling few-shot compositional generalization in neural network models.

---


### 161. [Pareto-Improving Adversarial Attacks with Primal-Dual Regularization](https://arxiv.org/abs/2610.04652)

**<font color=#1a73e8>作者：</font>** Yang Dai, Longfei Zhang, Wei Tao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transferable adversarial attacks are arguably the most practical black-box threat model. Under the same perturbation budget, stronger transfer attacks attain higher attack success rate (ASR), yet their imperceptibility also tends to degrade. Under such a fixed-budget protocol, transferability and imperceptibility therefore appear to trade off against each other. We argue that this conflict is an artifact of fixed-budget evaluation, not an intrinsic trade-off. When attacks are compared on the ASR--imperceptibility Pareto frontier obtained by sweeping $\epsilon$, stronger transfer attacks already attain better imperceptibility at matched ASR than weaker ones. To exploit this latent advantage, we introduce the stealthy transfer attack ST, a plug-in primal-dual wrapper that adds an $L_\infty$ saturation regularizer to the standard constrained objective and resolves it through a two-step primal-dual update: a projected primal step on the perturbation coupled with an $L_1$-ball projection on a dual variable that absorbs the regularizer through Fenchel duality, requiring no auxiliary models or handcrafted perceptual priors. Empirically, ST extends the Pareto frontier across different base attacks and additional surrogate architectures. At $\epsilon{=}16/255$, average imperceptibility gains over each base attack are $17\%$ on LPIPS and $14\%$ on NIQE while ASR is preserved or improved. At matched high-ASR levels, the strongest ST variants further Pareto-dominate dedicated stealth-oriented transfer attacks, confirming that the latent imperceptibility advantage of strong transfer attacks can be unlocked by a primal-dual optimization wrapper without sacrificing transferability. Code will be made available at \url{this https URL}.

---


### 162. [Path Laplacian Encodings for Directed Graphs](https://arxiv.org/abs/2610.04657)

**<font color=#1a73e8>作者：</font>** Lydia Mezrag, Semih Cantürk, Michael Perlmutter 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Directed graphs naturally model many real-world systems in which interactions are asymmetric, such as citation networks, web graphs, and information-flow networks. However, graph learning methods commonly rely on message passing with symmetrized graph representations or positional encodings that only partially exploit edge directionality. We introduce PathLapPE, a novel spectral positional encoding (PE) derived from the path Laplacian on directed graphs. PathLapPE provides node- and edge-level features that encode directional higher-order structure and can be incorporated into standard graph learning architectures. Empirical results on node- and graph-level benchmark tasks show that PathLapPE yields consistent improvements across several architectures, especially when combined with direction-aware message passing. Compared with magnetic Laplacian positional encodings, a widely studied spectral positional encoding for directed graphs, PathLapPE does not require additional fine-tuning of directionality hyperparameters while offering competitive runtime and performance.

---


### 163. [Post-Quantum Authentication Protocol for Internet of Medical Things](https://arxiv.org/abs/2610.04661)

**<font color=#1a73e8>作者：</font>** Kartick Sutradhar, Ranjitha Venkatesh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> IoMT communication systems should provide origin authentication and ensure integrity protection for the messages produced by patients' devices for transmission to gateways and further processing by other hospital services. With regard to IoMT, this paper discusses tampering, impersonation, and replay attacks on messages provided as medical reports. Long-term security of the communication system is also addressed considering potential quantum attacks. For this purpose, we design a protocol that meets requirements of practical implementation and employs an ISIS like lattice-based construction combined with concepts of the blockchain technology. Patients' devices generate a canonical JSON format medical report containing a timestamp and critical information. Using a nonce, the patients create a cryptographic signature of the message with a challenge generated from hash of a message. The gateway verifies signatures utilizing the public key of a trusted ledger associated with a particular patient and ensures freshness of the transmitted message. To optimize the performance in case when many devices interact with a gateway at once, the gateway performs batch signature validation using vectorized modular linear equations. The trusted ledger uses tamper-resistant REGISTER and TRUST UPDATE entries, maintaining a trust score of each registered patient and updating the value after each ACCEPT/REJECT operation. Our prototype application demonstrates registration procedure of a new patient, signing and verifying medical reports, auditing of the ledger, and performance assessment. Based on our experiments in the prototype, we argue that, when applied to large-scale systems, batch verification is superior to simple signature validation approach.

---


### 164. [FLASHSWIN: Unlocking Large Windows and Dense Tokens in Swin Vision Transformers with Memory Efficient Attention](https://arxiv.org/abs/2610.04664)

**<font color=#1a73e8>作者：</font>** Tushar Kataria, Gerald Sabin, Ponnuswamy Sadayappan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution vision backbones have long been forced to trade away local token density to afford larger receptive fields. Hierarchical Swin transformers impose this compromise because standard windowed attention materializes an $M^2\times M^2$ score matrix per window, incurring $O(M^4)$ memory as windows or token grids grow. Furthermore, Swin adds a learned relative-position bias elementwise to attention scores, requiring full materialization of the score matrix and its gradient. This keeps Swin and SwinV2 trapped in a small-window($M=8,16$), coarse-token regime with patch size $4\times4$ ($p=4$), limiting performance for fine-grained tasks. We introduce FLASHSWIN, which replaces standard windowed attention with a FlashAttention implementation that computes exact softmax attention without materializing the score matrix, reducing per-window memory from $O(M^4)$ to $O(M^2)$. This enables higher token density and larger receptive fields without inflating memory overhead. Training memory is flat across window sizes: at a $32\times32$ window, FLASHSWIN-T requires only $12.4$\,GB, unchanged from $8\times8$, compared to $70/90$\,GB for SwinV2/V1-T. However, applying FlashAttention directly to Swin creates a trade-off: bypassing the score matrix precludes Swin's additive relative-position bias, forfeiting spatial information in exchange for memory efficiency. FLASHSWIN restores position information as window-local learnable 2D RoPE, making large windows and dense token grids both affordable and accurate. At matched scale, FLASHSWIN-T outperforms Swin variants. With dense tokens and wide windows ($p=2,M=32$), the same Tiny model reaches $84.1\%$ ImageNet-1K, $44.1$ COCO box AP, and $47.28$ ADE20K mIoU---gains of $+1.3$, $+5.1$, and $+1.82$ over SwinV2-T at $M=16$, respectively. At fixed $M=32$, halving the patch size yields roughly $3\times$ larger gains in boundary quality than in mIoU.

---


### 165. [Efficient Neural Surrogates for Linear Radiation Transport on the Lattice and Hohlraum benchmarks](https://arxiv.org/abs/2610.04665)

**<font color=#1a73e8>作者：</font>** Carmelo Gonzales, Steffen Schotthöfer, Cory D. Hauck  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Linear radiation transport equations (RTEs) form the simulation foundations underpinning design and analysis tasks in nuclear engineering, inertial confinement fusion, medical imaging, and astrophysics, but resolving the high-dimensional phase space at engineering fidelity remains expensive enough that outer-loop workflows, such as design optimization, uncertainty quantification, and parameter sweeps, are routinely budget-bound on traditional solvers. Neural surrogates promise to relax this bottleneck by amortizing simulation cost across thousands of downstream queries, but the architectural choices and engineered inductive biases that make a surrogate accurate on one transport problem do not transfer straightforwardly across model families. We benchmark two parameter-matched neural surrogate architectures, the physics-attention Transolver and the multi-scale graph network Bi-Stride Multi-Scale MeshGraphNet (BSMS-MGN), as end-to-end approximations of the final-time particle concentration for the two-dimensional linear RTE on the canonical Lattice and Hohlraum benchmarks. An ablation across Fourier features and region-weighted training loss exposes strongly architecture-dependent inductive-bias preferences, indicating that design choices common to physics-informed surrogate workflows must be revisited per architecture rather than imported across model families, and that downstream utility depends on per-QoI sensitivity rather than a single field-level score. The model training recipe, training data, and evaluation pipeline are released alongside this paper to support reproduction, transfer to related transport problems, and evaluation as amortized forward-model components in larger outer-loop simulation workflows.

---


### 166. [Indistinguishability Lifting for Keyed Oracles, Compressed Ideal Cipher, and More Applications](https://arxiv.org/abs/2610.04674)

**<font color=#1a73e8>作者：</font>** Ritam Bhaumik, Yu-Hsuan Huang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptographic security proofs often involve an adversary interacting with a larger, keyed oracle that consists of (potentially exponentially) many independent instances of a smaller, base oracle. However, showing quantum indistinguishability between two such keyed oracles can be tricky, since a single query made by an adversary may involve a superposition that covers all instances of the base oracles simultaneously.
In this paper, we establish a generic indistinguishability lifting theorem of the following form: if the two base oracles are indistinguishable under quantum queries, then their corresponding keyed oracles are too, up to an O(q^2) multiplicative loss in distinguishing advantage, where q is the number of queries made by the adversary. Our lifting theorem applies to both statistical and computational settings, and to oracles that are stateful as well. It is also optimal in that it matches the obvious Grover search attack for a certain (contrived) choice of oracles.
As an immediate application, we extend Carolan's compressed permutation oracle to an efficiently implementable compressed ideal cipher, and use it to prove preimage resistance of the Davies-Meyer compression function in the quantum ideal cipher model. Thanks to our lifting theorem, the soundness of our compressed ideal cipher reduces to that of Carolan's oracle, and any further improvement on the latter would automatically carry over to the former.
As our second application, we give a modular construction that doubles the message length of any quantum-secure strong pseudorandom permutation. Along the way, we show that an existing two-round tweakable Feistel construction is indistinguishable from a random permutation under quantum bidirectional queries. This is done via a dedicated polynomial-method argument, which may be of independent interest.

---


### 167. [COMPASS: Comet Object Measurement Pipeline with Automated Selection and Scoring](https://arxiv.org/abs/2610.04680)

**<font color=#1a73e8>作者：</font>** Jack Roberts, Canya Lu, Alexis Michelle Lawson 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Summary: The single-cell gel electrophoresis ('comet') assay is a widely used technique for quantifying DNA damage at the individual cell level. However, image analysis often relies on manual inspection or semi-automated software, which can be labor-intensive, difficult to reproduce, and sensitive to image quality and comet morphology. COMPASS automates comet assay image analysis by combining deep learning-based comet segmentation with damage measurement and automated comet selection. The pipeline produces standardized DNA damage measurements while offering robust detection, reducing manual effort and improving reproducibility through transparent selection and optional manual review.
Availability and implementation: COMPASS is implemented in Python and is freely available at this https URL rsinghlab/COMPASS. Installation instructions, pretrained weights, and example usage are provided in the repository.
Contact: jack_roberts2@brown.edu, ritsingh@illinois.edu
Supplementary information: Available onlime upon publication.

---


### 168. [When Debate Helps: Proposal Supply and Verification-Aware Readout in Multi-Agent Reasoning](https://arxiv.org/abs/2610.04686)

**<font color=#1a73e8>作者：</font>** Zihao Zhao, Tunyu Zhang, Haizhou Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate can improve reasoning, yet often fails to beat simple majority voting. We argue that successful debate requires two distinct mechanisms: proposal supply must surface a correct answer, and readout must identify that answer when voting misses it. We formalize the first requirement through recoverable headroom, which measures cases where a correct proposal is available but the majority answer is wrong. For the second, we develop Latent Verification Debate (LVD), an accounting model in which candidate proposals receive answer-specific verification evidence before final generation. Controlled fixed-proposal interventions estimate this latent effect in equivalent peer-support units and show that correct evidence changes answer probabilities and generated decisions while proposal supply remains fixed. To improve proposal supply, we construct societies from neural-thicket agents using labeled and label-free coverage objectives. Across two backbones and matched-budget reasoning benchmarks, coverage-selected societies increase complementary proposal supply and improve aggregate accuracy in repeated stochastic evaluations. Round-level controls further show that interaction provides gains beyond applying the same finalizer directly to the initial proposals. These results identify proposal coverage and truth-sensitive evidence use as complementary conditions for debate to outperform voting. Code is available at this https URL.

---


### 169. [Penumbra: Sample-Efficient Adversarial Search for Regulatory Obligations](https://arxiv.org/abs/2610.04693)

**<font color=#1a73e8>作者：</font>** Anthony Rhodes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents are entering finance, healthcare and law, sectors where a violation leaves no lexical signature and carries real penalties. Whether an omission is material, or a disclosure sufficient, depends on what the response left out. Probing such an obligation means finding responses one minimal edit from flipping compliance, and every probe costs a generation and two adjudications, so the binding constraint on regulatory red-teaming is sample efficiency, not volume. We introduce Penumbra, an adversarial search that walks from a verified anchor under an expanding edit budget until a two-evaluator committee changes its verdict, and emits the two adjacent responses that straddle the change. Allocation is adaptive, and the objective is coverage of the defeat surface: distinct (obligation x defeat mode) cells resolved per candidate. At matched budget, adaptive allocation reaches uniform allocation's full-budget coverage on 59% of the candidates; at equal records it covers 1.43x the defeat modes of naive enumeration, and the gain is confined to the axis it targets. On 60 screened obligations of a financial advisory constitution, Penumbra returns 144 pairs, each a compliant and a violating response that the committee places on opposite sides of the boundary, differing by a handful of words where a model asked for both directly produces texts sharing almost nothing. A second constitution, for clinical triage, reproduces this on 18 obligations: 49 pairs at the same tightness, with the same modes hardest. Pairs like these show where an obligation's own terms stop deciding, which is what an agent deployed under it must be tested against, and the search finds them at a cost that scales with the boundary, not the text.

---


### 170. [Low-Fidelity FDM Spectral Guidance for Neural Eigenvalue Solvers](https://arxiv.org/abs/2610.04695)

**<font color=#1a73e8>作者：</font>** Aryan Chaudhary, Manikandan Padmanaban, Jagabondhu Hazra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operator eigenvalue problems appear throughout science. Classical methods usually discretize the operator into a matrix and then solve the resulting matrix eigenvalue problem. This works well in low dimensions, but fine grids quickly become expensive in both memory and computation as the dimension grows. Neural network based solvers avoid storing these large grids, but recent state of the art neural methods can require hundreds of thousands of training steps and may struggle to find the desired eigenvalues. We show that the two approaches can help each other. A coarse finite difference method (FDM) calculation acts as a cheap numerical model of the operator spectrum. We use the approximate eigenvalues as fixed shifts during the training of the neural solver, as they only need to locate the relevant part of the spectrum. We also introduce Stabilized Inverse Power Method Neural Network (SIPMNN), a more stable training procedure for higher-dimensional problems. Across five test problems at $d=10$, the combined approach is more accurate overall than the tested fully neural alternatives while using eight to ten times fewer iterations.

---


### 171. [Score-Calibrated Flow for Sampling from Unnormalized Densities with Applications to Generative Online Reinforcement Learning](https://arxiv.org/abs/2610.04696)

**<font color=#1a73e8>作者：</font>** Zeyang Li, Yunan Wang, Risheek Garrepalli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow models provide expressive policy classes for online reinforcement learning (RL), enabling multimodal behaviors and improved performance. However, training these policies remains challenging: the critic specifies the desired policy as an unnormalized Boltzmann density but does not provide direct samples from it. Many existing methods rely on importance sampling to construct training signals, which can suffer from high variance, increasing computational cost and destabilizing training. We propose Score-Calibrated Flow (SCF), a simple and efficient algorithm for training generative models to sample from unnormalized densities without importance sampling or backpropagation through the sampling trajectory. We learn the desired flow by enforcing self-consistency, bypassing target posterior mean estimation. By jointly exploiting the prescribed target score and the structure of flow matching, we establish these self-consistency requirements as score-calibrated optimality conditions, first for the terminal density and then for the trainable velocity field. We prove that their unique solutions are, respectively, the target density and the ideal flow model that conditional flow matching (CFM) would recover if target samples were available. We formulate the velocity condition as a fixed-point equation and exploit its conditional-expectation structure to construct a stop-gradient objective for enforcing it. The resulting training procedure retains the scalable sample-interpolate-regress structure of CFM despite the absence of target samples, using endpoints generated by the current flow. For online RL, the critic gradient supplies the target score at the generated actions, yielding a direct approach to actor training. Experiments on RL benchmarks demonstrate that SCF matches or improves upon state-of-the-art generative-policy baselines, while substantially reducing training time.

---


### 172. [Decouple, Purify and Unite: Semantic-Structural Prototype Learning for Federated Medical Segmentation](https://arxiv.org/abs/2610.04700)

**<font color=#1a73e8>作者：</font>** Xingyue Zhao, Wenke Huang, Linghao Zhuang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated learning enables medical institutions to train a global model without sharing data, yet feature heterogeneity from diverse scanners or protocols remains challenging. Existing representation-based methods face two limitations: 1) Incomplete Contextual Representation Learning: single-layer or coupled representations overlook multi-level structural cues and entangle regional semantics with boundary details. 2) Layerwise Style and Aggregation Biases: domain-specific style discrepancies across intermediate layers degrade prototypes, while aggregation that overlooks client distribution shifts can further amplify bias. We propose FedBCS+, federated decoupled contextual alignment with style-purified aggregation. We employ Frequency-domain Style Recalibration (FSR) in prototype construction to decouple content-style representations and extract style-purified prototypes. Built upon these purified features, Decoupled Contextual Prototype Alignment (DCPA) explicitly decouples multi-level features into semantic and structural prototypes and aligns regional semantics and fine-grained anatomical structures separately. Style-purified Semantic Prototype Aggregation (S2PA) measures each client's purified prototype divergence from the global consensus and adaptively reweights aggregation toward under-represented clients to reduce consensus bias. On five heterogeneous medical segmentation benchmarks spanning histopathology, MRI, ultrasound, and colonoscopy, FedBCS+ achieves the highest mean Dice among the compared methods. A convergence analysis further characterizes how aggregation and alignment affect the optimization bound.

---


### 173. [Learning Discriminative Geometry for Drifting Models](https://arxiv.org/abs/2610.04703)

**<font color=#1a73e8>作者：</font>** Doudou Zhang, Wenwen Hou, Yilin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently proposed Drifting Models shift iterative distribution refinement from inference to training, enabling effective one-step generation. However, their performance on complex image datasets depends strongly on the representation used to construct the drifting field: pixel-space drifting performs poorly, whereas pretrained feature spaces substantially improve sample quality for reasons that remain unclear. We trace this gap to the discriminative geometry of the representation, which determines sample weighting in kernel density estimation (KDE) and, consequently drift. We introduce persistent representation learning, which continuously learns a more discriminative representation geometry as the generator evolves across batches. We further establish a current-step gradient equivalence between the KDE ratio loss and drift regression loss under matched conditions, connecting density-ratio-based generator optimization to empirical drifting and motivating direct control of the drifting velocity. Across multiple datasets, our method learns effective discriminative representations directly from pixels and reduces FID by approximately $82-95\%$ over the original pixel-space Drifting Models, without pretrained encoders. Adapting pretrained representations and applying velocity clipping provide further gains.

---


### 174. [Neurodiversity-Aware Multimodal Affective Computing for Neurodevelopmental Assessment: From Norm-Referenced Classification to Context-Sensitive Decision Support](https://arxiv.org/abs/2610.04705)

**<font color=#1a73e8>作者：</font>** Mateusz Pomianek, Anna Łężniak-Seruga  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Automated neurodevelopmental assessment increasingly combines computer vision, speech, eye tracking, physiology, and machine learning, yet multimodality and discrimination do not establish construct validity, clinical usefulness, or appropriate interpretation of behavioral variation. We propose a testable architecture for neurodiversity-aware multimodal affective computing in which population-relative deviation is not treated as sufficient evidence of adverse functioning. This conceptual article reports neither a new participant-level study nor a trained predictive system, and no predictive or clinical superiority is claimed. The framework keeps observable signals, modality quality and availability, context, population-relative information, pooled within-person references and, when sufficiently supported, context-conditioned within person references, and predictive uncertainty distinguishable throughout inference. It defines structured decision-support outputs and auditable requirements for target validity, temporal integrity, contextual leakage, missing-modality robustness, calibration, subgroup evaluation, interpretability, privacy, and human decision boundaries. The contribution is architectural rather than algorithmic: it specifies empirically testable constraints that can be instantiated with different multimodal learning methods. Autism provides the principal motivating evidence base, without assuming unchanged transfer to other neurodevelopmental conditions.

---


### 175. [VoCa: Designing Speech-Canvas Interaction for Voice-Based Conversational Agents](https://arxiv.org/abs/2610.04706)

**<font color=#1a73e8>作者：</font>** Yate Ge, Run Yuan, Yueran Qi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People write and sketch while speaking to explain, organize, and develop content together. Inspired by these practices, we investigate how voice agents can use a canvas alongside speech in multi-turn conversations with users. We conducted a two-part formative study: an observational study of how pairs coordinated speech and boardwork, followed by a design workshop that informed a design space for speech-canvas interaction with voice agents. Building on these insights, we developed VoCa, a voice agent that coordinates speech with visual object creation, annotation, and attention guidance. A five-day deployment with 18 participants examined usability, experiences of speech-canvas interaction, patterns of use, and desired improvements. Participants' experiences highlighted opportunities for speech-canvas interaction in learning, work, and daily life, alongside challenges in coordinating what agents say and show in ways users can follow and influence. These findings inform how voice agents can use a canvas alongside speech in conversation.

---


### 176. [NAMVIS: Next-Scale Autoregressive Multi-View Image Synthesis](https://arxiv.org/abs/2610.04722)

**<font color=#1a73e8>作者：</font>** Ramil Khafizov, Ilya Statsenko, Ruslan Rakhimov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view novel view synthesis is a central problem in 3D content creation, but diffusion-based approaches remain limited by iterative denoising, making multi-view generation expensive at inference time. We introduce NAMVIS, a diffusion-free framework that reformulates multi-view image synthesis as geometry-conditioned next-scale autoregression. Instead of generating target views through repeated denoising, NAMVIS predicts discrete visual tokens through a small number of coarse-to-fine scale steps, while sampling all tokens within each scale and across target views in parallel. To anchor this generation process to explicit camera geometry, we propose Multi-scale Projective Pose Encoding, which injects source and target camera transformations into both target-view self-attention and source-to-target cross-attention at every resolution. NAMVIS further combines global conditioning with dense geometry-aware cross-attention, enabling the model to preserve source-view appearance while maintaining target-view consistency. Across Objaverse, GSO, and OmniObject3D, NAMVIS outperforms diffusion-based baselines in PSNR, SSIM, and LPIPS, while running over 3 times faster than the evaluated diffusion baselines under the same evaluation setting. These results suggest that geometry-conditioned next-scale autoregression is a promising and efficient alternative to diffusion for sparse-view multi-view synthesis. Additional qualitative results, videos, and resources are available at this https URL

---


### 177. [Investigating Spatiotemporal Redundancy in Video Transformer for Collision Anticipation](https://arxiv.org/abs/2610.04727)

**<font color=#1a73e8>作者：</font>** Xiaoshan Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In worker-equipment proximity monitoring, video transformers are widely used for collision anticipation and have demonstrated strong performance. However, their accuracy comes with substantial computational demands, creating a tension with the need for low-latency inference on mobile robots and the pursuit of lower-carbon computation in construction. To address this, this study investigates where computation within an established video transformer is redundant and whether that redundancy can be removed without materially degrading predictive performance. Using VideoMAEv2-Base on the Nexar Collision Prediction dataset, we first examine how collision-relevant information evolves across network depth and then investigate two complementary forms of redundancy: structured capacity redundancy in multilayer perceptrons (MLPs) and spatiotemporal redundancy in the token stream. Linear probes show that interpretable motion cues, including flow magnitude, looming, and approach versus retreat, are most accessible at intermediate layers, whereas collision-label discrimination strengthens toward the final layer. Token redundancy is axis-specific: adjacent temporal-token similarity reaches 0.970 in later layers, while spatial similarity falls to 0.297, indicating substantially greater redundancy across time than across space. Exploiting this asymmetry, temporal token merging reduces backbone computation from 356.99 to 178.50 GFLOPs and latency from 12.69 to 7.21 ms per clip, a 1.76x speedup, while mean average precision changes only from 0.7478 to 0.7443. Importance-guided retention of 50% of MLP units preserves an AUC of 0.753, compared with 0.529 under matched random retention, and reveals that pruning alters score calibration before discriminative ranking collapses. These findings establish a new pathway for pursuing faster algorithms through targeted temporal token compression and neuron pruning.

---


### 178. [Probabilistic Pedestrian Forecasts from a Handheld Phone: World-Frame Heat Maps, Visual-Inertial Height Drift, and Evaluation without Ground Truth](https://arxiv.org/abs/2610.04736)

**<font color=#1a73e8>作者：</font>** Danial Safaei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A pedestrian with a phone could be shown where nearby people will be in the next few seconds, if the forecast stays on the ground while the phone moves, is calibrated, and needs only a monocular camera and visual-inertial odometry (VIO). We build and evaluate such a system. People are detected, lifted onto the floor by ray-plane intersection, tracked in a gravity-aligned metric frame, and forecast as per-step probability maps by a small U-Net trained with a negative log-likelihood (NLL) loss on bird's-eye (SDD) and first-person (EgoTraj-Bench) trajectories. On handheld ADVIO recordings, vertical VIO drift and the user's own changes of level silently rescale monocular ground positions (by 87% within 90 s on one clip; on another, all tracks are lost for the last 31% of the clip); keeping the camera's height above the floor constant under a low-pass-filtered altitude avoids this, though it lags on escalators. On the SDD and EgoTraj-Bench test splits, the final forecaster lowers the NLL at 4.8 s by 1.51 and 1.37 nats relative to a fitted constant-velocity Gaussian. Lacking ground truth for people in handheld video, we score forecasts against the tracker's own later raw measurements. In an internally pre-registered evaluation on seven held-out clips, the final forecaster's NLL is lower than the benchmark-fitted baseline's at 1.2, 2.4 and 4.8 s (by 0.17, 0.23 and 0.47 nats; 95% intervals over people exclude zero), but by less than half as much as on the development clips. Exploratory analyses cut both ways: resampling clips instead of people widens the intervals to include zero at 1.2 and 2.4 s, and once both forecasters are recalibrated on the development clips the network is significantly better only at 1.2 s; but two clips run with ADVIO's reference poses favour the network much more when re-run with the phone's own poses. We discuss what such self-consistency scores can and cannot show.

---


### 179. [ThyCLIPNet: A BiomedCLIP-Guided Lightweight Attention-Enhanced DeepLabV3+ Framework for Robust Thyroid Nodule Segmentation](https://arxiv.org/abs/2610.04743)

**<font color=#1a73e8>作者：</font>** Tasnim Jahan, Md Easin Arafat, Swakkhar Shatabda  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate thyroid ultrasound segmentation is often challenged by low contrast, speckle noise, and unclear boundaries. Although recent methods have improved segmentation accuracy, many rely on resource-intensive architectures or lack explicit integration of multiscale features with global biomedical visual guidance. In this paper, we introduce ThyCLIPNet, a lightweight semantic-guided hybrid encoder-decoder framework that integrates BiomedCLIP-derived biomedical semantic guidance into a lightweight multi-scale CNN segmentation pipeline. The encoder integrates MobileNetV2 with efficient channel attention, while atrous spatial pyramid pooling and a custom convolutional block attention module enrich bottleneck features. The decoder combines hierarchical skip connections and lightweight attention refinement with a BiomedCLIP-guided gated fusion pathway that projects vision-only global biomedical embeddings into decoder feature space and selectively integrates them through semantic-local fusion and spatial gating. To the best of our knowledge, ThyCLIPNet is among the first lightweight thyroid ultrasound segmentation frameworks to use BiomedCLIP's vision encoder alone for image-only global semantic guidance without text prompting. Experiments on TG3K, TN3K, DDTI, and PKTN achieve dice similarity coefficients of 96.22%, 87.58%, 84.73%, and 80.70%; intersection over union scores of 92.72%, 77.91%, 73.51%, and 67.64%; and 95th-percentile hausdorff distances of 3.75, 16.38, 18.23, and 10.86, respectively. ThyCLIPNet uses 8.55M parameters and 22.99G FLOPs. Overall, the results support integrating global biomedical semantic guidance with lightweight multi-scale CNN representations for robust and computationally efficient thyroid ultrasound segmentation. Source code: this https URL. [Abstract shortened for arXiv. See PDF for full abstract.]

---


### 180. [Formalizing the Moral Evaluation of Speech Acts: Truthfulness, Lies and Ethical Dilemmas](https://arxiv.org/abs/2610.04747)

**<font color=#1a73e8>作者：</font>** Benjamin Icard, Gauvain Bourgne, Jeanne Bonnaventure 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In life-or-death situations, a benevolent lie may appear more moral than telling the truth. Yet such lies can backfire, producing unintended and sometimes fatal consequences. This tension, famously disputed by Kant and Constant in 1797, applies not only to lying but to assertive speech acts in general, raising the question of which utterance should be chosen when moral stakes are high. We present a logical framework for the ethical evaluation of speech-act utterances based on agents' beliefs. Implemented in Answer Set Programming (ASP), the framework assesses utterances under deontologism, consequentialism, and principialism, and is illustrated on Sartre's The Wall (1939), a reworking of that controversy in which lying leads alternately to rescue and to death. Our setting is general by design: as two variants show, accommodating a new moral situation amounts to adjusting parameters, not rules.

---


### 181. [FoSeRL: Formal Sequential Robustness Certification for Reinforcement Learning Policies](https://arxiv.org/abs/2610.04754)

**<font color=#1a73e8>作者：</font>** Sara Taheri, Deep Kumar Ganguly, Jan Křetínský 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Even a few action perturbations can substantially degrade the performance of a deployed decision policy. Certifying the resulting return loss is challenging in stochastic environments, where returns vary even without an attack. We introduce FoSeRL, a framework for certifying deployed RL policies against precommitted, temporally sparse action attacks. The deployed policy is unchanged, with no smoothing or retraining. Certification requires a resettable simulator supporting shared randomness and independent one-step successor queries, but no analytical dynamics model. FoSeRL certifies that an attacked episode loses no more than a prescribed amount of return relative to the same episode unattacked, with at least a target probability and at a user-specified confidence level. Both runs share the initial state and randomness, so the measured loss reflects the attack, not the episode; carrying the running return gap as a state coordinate makes it the terminal value, reducing trajectory-level certification to terminal safety. Time-dependent barrier conditions on the augmented state bound the terminal failure probability: satisfied exactly, they certify every admissible precommitted attack; learned from sampled trajectories and verified on held-out data, they certify the same guarantee under a specified attack-episode setting. Across six stochastic continuous-control environments and three RL policy families (TD3, SAC, and PPO), FoSeRL certifies non-trivial cardinality--magnitude robustness frontiers, achieves substantially larger certified budgets than policy smoothing, and reveals marked robustness differences among policies with comparable nominal performance.

---


### 182. [EasyClassifier: Honest, Reproducible Machine-Learning Classification for Researchers Who Do Not Program](https://arxiv.org/abs/2610.04758)

**<font color=#1a73e8>作者：</font>** Ahmad B. A. Hassanat, Ghada A. Altarawneh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning classification is now used across medicine, the social sciences, economics, education and engineering, very often by researchers who do not program. Two errors recur in such work: preprocessing learned on all rows before cross-validation (data leakage), and reporting the cross-validation score of the classifier that won a comparison (selection bias). Both make published scores optimistic. We present EasyClassifier, an open-source Python package that guides a user from a CSV or Excel file to a finished analysis through a sequence of plain-language, multiple-choice questions, with no code. It makes the correct procedure the default rather than an option: every preprocessing step is learned inside each training fold; the selected classifier receives a separate final score from nested cross-validation (up to 2,000 rows), or an untouched 20% test set; classifiers run with fixed default parameters and fixed random seeds; and every run writes a report with a ready-to-adapt Methods paragraph, the references to cite, and figures prepared for publication. On ten public datasets from seven fields and a random-label control, split in half so that one half served as an untouched external test, the common practice overstated balanced accuracy by 2.9 percentage points on average (up to 9.9 on small data), whereas the score EasyClassifier reports had a mean signed bias of +0.7 points and a mean absolute error of 2.3 points (one-sided Wilcoxon p = 3.2 x 10^{-4}, 30 runs). On random labels it reported 48.8% balanced accuracy against a chance level of 50%. EasyClassifier is available under the MIT license from PyPI (pip install easyclassifier), GitHub, and Zenodo.

---


### 183. [Trends in EHR Satisfaction and Interoperability Among Family Physicians: A Five-Year Analysis of the ABFM Continuous Certification Questionnaire, 2022-2026](https://arxiv.org/abs/2610.04762)

**<font color=#1a73e8>作者：</font>** Carl Y. Zhang, Nathaniel Hendrix, Robert L. Phillips 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Objective: To assess trends in family physicians' (FPs) electronic health record (EHR) satisfaction and their experience of interoperability across organizations.
Materials and Methods: Serial cross-sectional analysis of five waves of the American Board of Family Medicine's Continuous Certification Questionnaire (2022-26). Adjusted logistic regression compared odds of being very satisfied across 11 EHRs; Cochran-Armitage tests assessed vendor trends. Ease of using outside information was analyzed separately for same- and different-vendor sources.
Results: Across 36,785 FPs, adjusted odds of being very satisfied relative to Epic ranged from 0.91 (95% CI, 0.74-1.11) for Elation Health to 0.17 (95% CI, 0.15-0.20) for Oracle Health/Cerner. Only Epic's users became significantly more satisfied (Benjamini-Hochberg adjusted P < .001), widening the vendor satisfaction gap. Within comparable periods, ease of using different-vendor information did not improve; fewer than 13% rated it very easy. Epic's interoperability advantage reversed by exchange type: non-Epic users had less than half the odds of Epic users of rating same-vendor interoperability very easy (adjusted OR, 0.41; 95% CI, 0.38-0.44) but 1.54 times the odds for different-vendor interoperability (95% CI, 1.35-1.75).
Discussion and Conclusion: The ABFM data are already informing EHR policy effects but they also have utility for the EHR marketplace. EHR satisfaction differences are widening, and reported ease of using different-vendor information is low and unchanged. While EHR satisfaction has known implications for burden and burnout, interoperability is a quality and safety threat that may be compounded by artificial intelligence.

---


### 184. [Variance-Optimal Control Variates for Learning with Black-box Feedback](https://arxiv.org/abs/2610.04766)

**<font color=#1a73e8>作者：</font>** Zihao Zhao, Shuhan Zhang, Kai Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern models increasingly learn through black-box oracles such as humans, optimization solvers, and external tools that provide feedback without exposing their internal mechanisms. A common remedy is to learn an (action-)value function as a control variate. In this paper, we first observe that even an exact action-value function can be arbitrarily far from variance-optimal. We show that this gap arises because the value function minimizes the noise in each action's own gradient term, while an action can still affect the rest of the gradient estimator through shared parameters. A simple unbiased correction, at no extra oracle cost, can still reduce its variance by an arbitrarily large factor. Motivated by this, we then prove that the residual variance can be decomposed exactly by actions with no cross terms. This decomposition yields a closed-form variance-minimizing correction for neural-network parameters, which can be computed by a simple projection. Empirically, our correction consistently reduces the variance left by the value function and improves learning across all tasks. The source code for all experiments is available at this https URL.

---


### 185. [Repeated-Measure Leakage, Distribution Shift, and Reliability under Partial Observation in Patient World Models](https://arxiv.org/abs/2610.04778)

**<font color=#1a73e8>作者：</font>** Arjun Subramanian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Patient world models are increasingly proposed for longitudinal prediction, intervention-aware reasoning, and clinical-trial simulation. Causal or clinical intervention validity is distinct from predictive generalization and reliability; before making stronger claims, the underlying predictive state should generalize across patients, survive realistic shifts and missing observations, and expose failure through meaningful reliability signals. We evaluate these prerequisites in a deliberately narrow setting: short-horizon digital-biomarker forecasting from PhysioNet GaitPDB, comprising 165 participants, 306 recordings, and 51,129 context-future pairs. Using persistence, ridge, MLP, GRU, Transformer, and a compact JEPA-style predictor, we build an evaluation ladder that progressively removes raw temporal overlap, same-recording familiarity, and same-patient familiarity before testing unseen-patient generalization. For GRU, NMSE rises from 0.1227 under random-window splitting to 0.1393 after eliminating raw train-test overlap and to 0.1961 under patient holdout. Among 54 participants with repeated recordings, exposure to a different recording from the same patient improves GRU NMSE from 0.2177 to 0.1556, while a recording-excluded identity hypothesis is not supported at the participant level. Under participant-held-out evaluation, MLP and Transformer are statistically indistinguishable. Study shift, a four-times-longer prediction gap, and partial observation further degrade performance; under 50% temporal masking, Transformer NMSE rises to 0.611 while MC-dropout predictive variance falls. We do not claim a longitudinal or intervention-aware simulator. Instead, the results support a prerequisite evaluation stack of patient separation, repeated-measure controls, shift, missingness, and uncertainty validation before stronger patient-world-model claims are trusted.

---


### 186. [Super-Resolution in The Right Latent Space: A Frozen Vision-Foundation Substrate](https://arxiv.org/abs/2610.04781)

**<font color=#1a73e8>作者：</font>** Wanzhou Lei, Cuifeng Sheng, Yanjin He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In an image latent space, the embeddings of high-resolution, natural, and sharp images form a manifold. Degradation of high-resolution images pushes their embeddings off this manifold. Real-world super-resolution (SR) then becomes the task of mapping the degraded embedding back onto this manifold --- not anywhere on the manifold, but to the point that preserves what the input still carries, both its semantics and pixel details. Every published method implements this mapping in a reconstruction-oriented latent space or pixel space. We claim these spaces are the wrong substrates for SR. Low-resolution and degraded images are embedded far from the manifold, making the mapping difficult and expensive. The lack of semantic information in these substrates also makes it difficult to navigate to the faithful point on the manifold, causing severe hallucination when degradation is heavy. Thus, restoring in a suitable latent space is crucial to the SR task. We show that the latent space of 23 fused layers of a frozen DINOv3-L is one such space that makes the SR task easier. Degraded images are embedded near the manifold. Moreover, this substrate contains a hierarchy of information, from pixel record to degradation robust semantics, guiding the model to find the faithful point on the manifold. On this substrate, a 415M decoder is trained under reconstruction and adversarial objectives to map the degraded embeddings back and decode to pixel space in one pass. The resulting model, RAESR, attains the best fidelity--perception trade-off among state-of-the-art adversarial and diffusion-based restorers on RealSR, DRealSR, LSDIR and DIV2K-Val, at 37 ms per 512 by 512 image on a single H20 GPU. Swapping the substrate for a VAE latent under an identical recipe loses on every metric.

---


### 187. [DASH: Fast, Valid Counterfactuals for Deep Networks via Batched Directional Search](https://arxiv.org/abs/2610.04783)

**<font color=#1a73e8>作者：</font>** Shraman Pal, Gabriel Medeiros, Clayton Escouper das Chagas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanations are most useful when they can be generated with low latency, remain close to the factual input, and satisfy input-domain, categorical, and actionability constraints. Achieving these objectives simultaneously is challenging for deep neural networks. Heuristic methods are often fast but may return invalid counterfactuals, whereas exact methods can certify global proximity but may not finish within practical time limits. We introduce DASH, a batched heuristic search method for finding close, valid, and actionable counterfactuals for deep neural networks under $\ell_1$, $\ell_2$, and $\ell_\infty$ objectives. DASH uses directional Lipschitz bounds and local affine models to generate anchors, then ranks and expands promising regions with batched network evaluations. We compare DASH against nine prior heuristic methods and time-limited exact mixed-integer baselines on four tabular datasets, with network depths from 2 to 32, and evaluate scalability on PBMC3k. Across 9,000 tabular query-norm cases, DASH returns a valid counterfactual within $5\%$ of the best heuristic-observed valid distance in $94.6\%$ of cases, with a median CPU search runtime of $0.061$ s. PGD-bisect, the baseline with the highest pooled within-$5\%$ coverage, meets this criterion in $41.1\%$ of cases, with a median runtime of $0.298$ s. These results show that the proposed search maintains high valid proximity across norms while keeping its search runtime practical.

---


### 188. [Lollypop: Camera-to-Motion-Capture Calibration Verification with a Reference Target](https://arxiv.org/abs/2610.04785)

**<font color=#1a73e8>作者：</font>** Tianyi Liu, Kevin Harris, Mihika Dave 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-to-motion-capture (mocap) calibration is essential for using mocap as ground truth in robotics, AR/VR, and other computer vision tasks. However, the calibration can drift after deployment, while calibration residuals and visual inspection provide limited independent verification. We present Lollypop, a fiducial-mocap reference target for independent calibration verification. The target couples an ArUco fiducial with a mocap marker constellation so the visual center and tracked centroid represent the same physical point. Given a candidate calibration, verification projects the mocap point into the image and measures its disagreement with the detected fiducial center. Experiments show sub-pixel nominal error, sensitivity to controlled extrinsic perturbations, and increasing error during an illustrative mixed-handling sequence.

---


### 189. [KALEIDO: Input-Space Adaptation of a Vision Model for Time-Series Forecasting Through Gated Fold Geometries](https://arxiv.org/abs/2610.04786)

**<font color=#1a73e8>作者：</font>** Xiangyu Shi, Qinghua Liu, Sam Heshmati 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models buy zero-shot forecasting with large temporal corpora; a vision model needs none, since a natural image implicitly embeds the patterns a forecaster must model, and an ImageNet-pretrained masked autoencoder forecasts a series by inpainting a rendering of it. A rendered series is not a natural image, however, and closing that gap takes temporal-aware adaptation. We show that the rendering geometry - how the series is folded and drawn - is a controllable, mixable axis for it. Kaleido detects the dominant periods, renders a rule-generated set of fold geometries, combines the inpaintings with a convex per-position gate fit on validation only, and fuses the result with the zero-shot output at one fixed share, with no per-dataset hyperparameter beyond the baseline's published settings. Training only LayerNorm (0.05%), Kaleido lowers MSE by 13% against the published zero-shot baseline on LTSF and, frozen, by 6.6%; on GIFT-Eval it improves the baseline by 7.4% in MASE and 19.3% in CRPS.

---


### 190. [Active-DiNTS: Active Differentiable Network Topology Search](https://arxiv.org/abs/2610.04787)

**<font color=#1a73e8>作者：</font>** Gean Trindade Pereira, Thierry Urruty, Muriel Visani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural Architecture Search (NAS) has proved to be a strong alternative to manual network design, but applying it to 3D medical image segmentation is limited by two well-known costs, large annotation budgets and multi-GPU clusters. Thus, this paper introduces Active-DiNTS (Active Differentiable Network Topology Search), an approach that embeds pool-based Active Learning (AL) into a bi-level differentiable topology search to perform architecture discovery and label curation jointly. At each query round, unlabeled MRI volumes are ranked by one of three uncertainty signals (Entropy, Variance, or Standard Deviation), and only the top-ranked volumes are sent to an oracle for annotation. The new labels feed two interlocked stages. Network weights are updated in an outer loop, while the macro/micro topology of a U-Net-style backbone is refined in an inner loop. Three AL regimes (weights-only, topology-only, joint) expose the speed-accuracy trade-off. Evaluations on the Medical Segmentation Decathlon (MSD) Task01 BrainTumour benchmark showed that Active-DiNTS surpasses DiNTS, C2FNAS, and nnU-Net in Dice, with gains of about 10 percentage points on Edema and 5 points on Non-Enhancing core, on a single GPU and using a fraction of the labeled volumes. The discovered architectures are denser and more FLOP-heavy than prior baselines, but remain competitive in trainable parameters and peak memory; the fastest search variant finishes in under 0.25 GPU-days, over 27x faster than the eight-GPU DiNTS search. Together, these results indicate that pairing differentiable NAS with active data acquisition is a practical recipe for accurate 3D segmentation under realistic constraints.

---


### 191. [TIMBRE: Teaching Time Series Forecasters to Read, Remember, and Reconcile](https://arxiv.org/abs/2610.04795)

**<font color=#1a73e8>作者：</font>** Xinyu Guan, Zhirong Zhang, Hongyuan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Event-informed forecasting requires translating reports and historical responses into changes to a numerical forecast. We propose TIMBRE (Temporal Integration of Memory-Based Responses and Evidence), which combines source-aware representation, state-conditioned response transfer, and reliability-guided fusion before a frozen forecast head. A separate readout adjusts interval widths while preserving the median. In a single-seed, one-epoch development study of 13 tasks, TIMBRE improves MAE over ordinary fusion on eight tasks but over native Chronos-2 on only two. Disabling response transfer in the trained model reduces BTC and AULF MAE by 47.04% and 6.81%, respectively. These findings identify sensitivity to learned response transfer rather than a general forecasting advantage. Missing development-set scores and the absence of retrained ablations limit attribution to individual evidence mechanisms.

---


### 192. [MedImageOSWorld: Benchmarking GUI Agents for Medical Image Consoles](https://arxiv.org/abs/2610.04800)

**<font color=#1a73e8>作者：</font>** Ziyang Long, Xinqi Li, Lujing Xing 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical consoles offer a practical interface for medical acquisition assistance, allowing agents to work through the controls and visual feedback used by human operators. Reliable assistance requires linking on-screen anatomy to acquisition decisions that determine what image evidence becomes available next. We introduce MedImageOSWorld, a benchmark for evaluating this capability in simulated CT, MR, and ultrasound consoles. Using screenshots and mouse-and-keyboard actions, agents configure protocols, plan acquisitions, inspect the resulting images, and make corrective adjustments across seven capability levels, from console operation to feedback-driven control. Evaluation combines task-specific workflow checks with hidden anatomical ground truth to assess procedural completion and acquisition outcomes separately. A common evaluation protocol specifies episode conditions and interaction budgets, while recorded trajectories support analysis of how agents observe, act, and respond to acquisition feedback. Across eleven open-weight agents, success rates range from 3.0 to 25.0 on a 0-100 scale while workflow-progress rates reach 21.5-74.5: agents complete much of the console workflow but rarely acquire the intended anatomy. Success collapses between perception and planning, from 79-90% at the lowest three levels for the best agent to at most 12% for millimetre-level planning and 0% for closed-loop control among open-weight agents. Two proprietary agents reach success rates of about 34 and exceed the best open-weight agent mainly in acquisition quality (61 versus 42). MedImageOSWorld provides a controlled setting for studying whether general-purpose GUI agents can translate visual observations into effective medical acquisition decisions.

---


### 193. [Multi-Agent Spectrum Sharing](https://arxiv.org/abs/2610.04802)

**<font color=#1a73e8>作者：</font>** Job Elliott, Graduate Student Member, IEEE 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This project explores how multiple cognitive radars can learn to share limited wireless spectrum with other radio users without interfering with one another. Using machine learning (ML), each device independently decides where and how widely to transmit within a fixed 100 MHz band. The system analyzes real or simulated signal activity to detect which parts of the spectrum are currently in use and which are open. Based on this information, the devices adapt their transmission choices to avoid crowded frequencies while making efficient use of available space. The goal is to develop a flexible, scalable approach to spectrum sharing that could support future wireless communication systems. Experimental results using both over-the-air software-defined radio (SDR) recordings and simulated environments demonstrate that the proposed meta-learning approach consistently balances competing objectives better than conventional reinforcement learning (RL) methods in multi-agent spectrum-sharing scenarios. Across five multi-agent benchmark environments, our proposed method achieved the highest average reward among the primary baseline algorithms while simultaneously maintaining low collision rates and stable transmission behavior.

---


### 194. [How Do People Challenge Racial Stereotypes Online? Counter-Story Detection Across Reddit Communities](https://arxiv.org/abs/2610.04803)

**<font color=#1a73e8>作者：</font>** Uma Sushmitha Gunturi, Jimin Mun, Maarten Sap 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Counter-storytelling is a powerful mechanism people use to challenge dominant narratives. Unlike other forms of counterspeech that have been widely studied in computational social science, counter-storytelling has largely been overlooked. Counter-stories are difficult to detect automatically; they are relational (defined with respect to expressions of racial stereotypes) and structurally diverse (drawing on stories that describe lived experiences, witnessed events, exemplars, and hypotheticals). We introduce a first framework for detecting and characterizing counter-storytelling against racial stereotypes at scale. This includes (1) a three-dimensional taxonomy grounded in narratology and Critical Race Theory and (2) a multi-stage pipeline that identifies relational pairs of stereotypes and counter-stories in noisy Reddit discourse. Using this pipeline, we annotate 25,549 Reddit posts across 615 communities and identify 1,312 counter-stories. Our analysis shows that speaker identity and post context shape how counter-stories are told. For example, in-group writers favor first-person testimony, often adopting the role of self-reflective insiders. Our work shows how computational methods can scale qualitative approaches to identify and characterize counter-storytelling as a contextual narrative practice, with implications for content moderation, narratology, and racial discourse analysis.

---


### 195. [Separating Decision Time from Decision Quality in the Real-Time Gap of Distilled Deciders: Evidence from a Game and a Conveyor Simulator](https://arxiv.org/abs/2610.04810)

**<font color=#1a73e8>作者：</font>** Chihoon Shin, Junyeong Lee, Kihyeok Jeong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time agents are often evaluated with the world paused, or with decision time rounded to whole ticks (tick conversion). Tick conversion predicts almost no loss for a learned decider whose hit accuracy falls by 14.8 percentage points (pp) on the same games in asynchronous play. We instead split the decider's gap to a zero-latency teacher into time and quality components. In ViZDoom, we train a small decider by imitating a scripted teacher, run the game on wall-clock time, and add a control in which the teacher waits for a call to the decider's server before deciding. On a Windows host, three preregistered studies put the time component at 6.5-8.7 pp and the quality component at 6.3-8.6 pp. On a Linux host that skips 0.08-0.09% of ticks, the time component disappeared (-0.1 pp; paired 95% bootstrap interval [-0.4, 0.0]) while the quality component remained (5.6 pp [3.7, 7.5]). Retraining on teacher-labelled states from the decider's own play (DAgger) improved it on new games on both hosts (2.6 pp [0.4, 4.9] and 3.1 pp [1.1, 5.2]), a preregistered partial success. Imposing one delay schedule on every arm in live play left a quality component of 5.8 pp [4.0, 7.5] on 100 new games, and retraining cut the decider's disagreement with the teacher on its own states from 22.7% to 14.9%. In a conveyor simulator with a 400 ms deadline, delay past it erased the quality component. A latency-matched control whose delays match the decider's shows which remedy to try.

---


### 196. [MOXIE: Discovering Alternative Explanations for Biomedical Image Classifiers](https://arxiv.org/abs/2610.04814)

**<font color=#1a73e8>作者：</font>** Abiha Tahsin Chowdhury, Rahul Dubey  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segment-based explanation methods such as LIME return a single explanation for each prediction, computed from one fixed image segmentation. This hides two important facts: a prediction can be supported by many different sets of image segments, and the segmentation itself shapes which explanations can be found. We introduce MOXIE (Multi-Objective eXplanation Imaging Engine), an evolutionary framework that searches for segment subsets that preserve the classifier's confidence while keeping as little of the image as possible. Instead of one explanation, MOXIE returns a Pareto front of alternative explanations that range from compact to highly faithful. We evaluate MOXIE with NSGA-II and four segmentation methods (SLIC, Felzenszwalb, Watershed and Voronoi) on BloodMNIST and HAM10000 datasets, using the same evaluation budget as LIME. Results show that MOXIE achieves a higher hypervolume than LIME on every image. LIME's explanations often appear convincing, yet the classifier's confidence collapses when only the highlighted segments are shown. MOXIE's fronts reveal how much of the image is needed to preserve the model's confidence and which contextual regions influence it. We also find that segmentation strongly affects evaluation: methods with unequal segment sizes appear most compact when segments are counted. These results show that alternative explanations provide a more complete view of a model's decision than a single explanation.

---


### 197. [Trusted Hardware Acceleration for Malicious-Secure Function Secret Sharing](https://arxiv.org/abs/2610.04818)

**<font color=#1a73e8>作者：</font>** Yujie Xue, Yijing Peng, Lin Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Function secret sharing (FSS) underlies two-party private inference and private information retrieval, with cost dominated by generating, moving and evaluating distributed point function (DPF) keys. A trusted GPU-integrated distributed function accelerator (DFA) removed key movement by generating and consuming keys locally, but tolerates only semi-honest adversaries. A malicious host or GPU can tamper with shares, replay one-time material, swap buffers after checking, request early outputs, or abuse the accelerator as a forgery oracle, while malicious FSS ships large authenticated keys or multiplies DPF work. We present VIGOR-DFA, protecting the chain from authorized input to authorized output release with three mechanisms: a fresh authentication epilogue using three field multiplications per DPF output, 3.8-4.0 times faster per gate than per-lane DPF tag trees; a freeze-before-challenge check of every opening with t = 3 independent MAC lanes over F_{2^61-1}; and a role-bound one-time resource ledger with a release guard, in a protected datapath beside the GPU L2 cache. We prove stand-alone static malicious security with abort in a protected-module model, with statistical error Q(2/p)^t approximately 2^-148 for Q less than or equal to 2^32 checked batches. Our DFA-calibrated model shows that, against dealer-based malicious FSS modeled after the protocol family of Shark, VIGOR-DFA removes 21.8-563 GB of per-query offline authenticated material and, mainly by generating it in-module, lowers LAN latency by 10.1-14.0 times (1.5-1.8 times excluding offline distribution) and energy by 3.0-3.9 times. Malicious security costs 2.5-3.5 times LAN latency over semi-honest DFA and 0.145 mm^2 at 7 nm. We have completed the verification of specifications and the functional CPU reference model, including GPU/RTL conformance verification, protected runtime evaluation, and deployment-related tests.

---


### 198. [DriftSR: One-Step Real-World Image Super-Resolution via Distribution Drifting](https://arxiv.org/abs/2610.04819)

**<font color=#1a73e8>作者：</font>** Wei Zhu, Kai Zhang, Yu Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-step real-world image super-resolution (Real-ISR) offers efficient inference, but recovering realistic and perceptually rich details often relies on score distillation or adversarial learning, introducing additional trainable components and making optimization more cumbersome. To this end, we propose DriftSR, a one-step Real-ISR framework that leverages pretrained diffusion priors through distribution drifting. Specifically, we perform drifting in the frozen intermediate representation space of a pretrained diffusion model, without introducing an additional task-specific feature encoder. Building on this space, we introduce Spatial Feature Drifting, which treats spatial features rather than entire images as distributional samples, enabling denser supervision for distribution alignment. To mitigate structural deviations, we further introduce Structure-Modulated Guidance, which adaptively refines drifting guidance according to local structural consistency with the LQ input. Consequently, DriftSR optimizes only the one-step generator, without auxiliary distillation branches or adversarial discriminators. Extensive experiments on three real-world benchmarks demonstrate that DriftSR delivers high-quality super-resolution reconstruction with efficient one-step inference.

---


### 199. [Cluster Validation Indices as Self-Supervised Objectives for Text Representation Learning](https://arxiv.org/abs/2610.04830)

**<font color=#1a73e8>作者：</font>** Kishor Kumar Bhaumik, Nicolas Roque dos Santos, Neil Shah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-supervised fine-tuning refines the embedding space of a pretrained language encoder without labels. However, the commonly used approaches are computationally expensive. Specifically, contrastive learning-based methods need multiview data and in-batch negative examples, while negative-free approaches require auxiliary graphs/networks. An interesting question arises: can self-supervised fine-tuning be done without relying on either additional negatives or graph data? To answer this question, we introduce SilK (Silhouette-guided K-means), which trains on a Cluster Validation Index, an internal measure of cluster quality without using labels. SilK clusters the corpus and then regresses a simplified silhouette toward a target value. Each document is compared only against the k cluster centroids, never against other documents, so the method needs no augmentation, no negative pairs and one view per document. On BERT-base, SilK trains 1.46x faster per epoch than the fastest baseline we evaluate and uses 45.4% less peak GPU memory than the leanest one. Under frozen-encoder linear probing, SilK stays competitive with the best baselines on three downstream tasks.

---


### 200. [RSure-Agent: Reliable Use of Tool Observations for Remote Sensing Agents](https://arxiv.org/abs/2610.04836)

**<font color=#1a73e8>作者：</font>** Fuyuan Liu, Nayu Liu, Wenhao Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing agents rely on perception, measurement, and raster analysis tools to solve Earth observation tasks. We refer to their judgments and quantitative results about ground objects as tool observations. However, these observations are subject to substantial uncertainty and may be incorrect even when the tools execute successfully. When agents accept incorrect observations, the errors can propagate through subsequent reasoning and cause task failure. We analyze 1,229 execution trajectories across three remote sensing agent benchmarks. On each benchmark, at least 88.1% of tasks depend on tool observations. Among these tasks, at least 22.7% contain incorrect observations despite successful tool execution. These errors propagate to the final answer in at least 82.0% of affected tasks on each benchmark. To address this problem, we propose RSure-Agent, a framework for verifying tool observations and limiting error propagation. We introduce a verifiable observation protocol that requires tools to return process evidence for the agent to verify their observations. We also construct a task-tool reliability prior from offline task feedback. The prior summarizes each tool configuration's past performance across task types and provides a task-specific reference for verification. Using process evidence and this prior, RSure-Agent decides whether to accept an observation, request additional evidence, or reject it. We evaluate RSure-Agent on EarthBench, ThinkGeo, TerraLogic, and CHOICE-420. Across the three agent benchmarks, RSure-Agent reduces the error propagation rate by 21.3 to 25.9 percentage points relative to the base configuration with verification and the prior disabled. On CHOICE-420, it improves overall accuracy over direct answering by 5.71 percentage points on average across 11 backbone models. On EarthBench, it reduces the tool-call ratio by 25.9% relative to Earth-Agent.

---


> [!TIP]
> 当前位于：**151-200**（第 4/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

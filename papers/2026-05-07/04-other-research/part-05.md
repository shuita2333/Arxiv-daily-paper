# 📦 其他研究 | 2026年05月07日

> 本类共 **213** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-213**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-213**

---

### 201. [Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs](https://arxiv.org/abs/2605.03964)

**<font color=#1a73e8>作者：</font>** Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.

---


### 202. [Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators](https://arxiv.org/abs/2605.03969)

**<font color=#1a73e8>作者：</font>** Mohamed Mady, Johannes Reschke, Björn Schuller  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.

---


### 203. [LIPPEN: A Lightweight In-Place Pointer Encryption Architecture for Pointer Integrity](https://arxiv.org/abs/2605.03974)

**<font color=#1a73e8>作者：</font>** Erfan Iravani, Lalit Prasad Peri, Mohannad Ismail 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Memory-safety violations in C and C++ programs continue to enable sophisticated exploitation techniques such as control-flow hijacking and data-oriented attacks. Existing hardware defenses either rely on address space layout randomization (ASLR) or attach explicit metadata to pointers to verify their integrity. External metadata schemes provide strong guarantees, but incur additional memory accesses and memory footprint overhead. In-place authentication mechanisms, such as ARM Pointer Authentication (PAC), achieve low overhead at the cost of limited entropy and susceptibility to brute-force and reuse attacks. This paper presents LIPPEN, a hardware-software co-design for full-pointer encryption that provides strong pointer integrity and confidentiality with zero metadata overhead. LIPPEN treats every pointer as an encrypted block, cryptographically binding it to its execution context and decrypting it transparently at dereference time. By re-purposing the entire 64-bit pointer field for encryption rather than preserving raw address bits, LIPPEN maximizes entropy, eliminates the brute-force weaknesses of truncated authentication codes, and maintains binary compatibility with existing PAC-enabled software. We prototype LIPPEN on FPGA using 64-bit RISC-V Rocket and BOOM cores, and evaluate it with microbenchmarks, nbench, and SPEC CPU2017. We compare against both an in-house RISC-V PAC implementation and Apple's PAC on the M1 processor. Across these workloads, LIPPEN provides comprehensive pointer protection with runtime overhead comparable to PAC-based schemes, while incurring negligible area and power overhead. These results show that LIPPEN is a practical design point for deploying strong pointer protection in real processors.

---


### 204. [Flow Sampling: Learning to Sample from Unnormalized Densities via Denoising Conditional Processes](https://arxiv.org/abs/2605.03984)

**<font color=#1a73e8>作者：</font>** Aaron Havens, Brian Karrer, Neta Shaul  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from unnormalized densities is analogous to the generative modeling problem, but the target distribution is defined by a known energy function instead of data samples. Because evaluating the energy function is often costly, a primary challenge is to learn an efficient sampler. We introduce Flow Sampling, a framework built on diffusion models and flow matching for the data-free setting. Our training objective is conditioned on a noise sample and regresses onto a denoising diffusion drift constructed from the energy function. In contrast, diffusion models' objective is conditioned on a data sample and regresses onto a noising diffusion drift. We utilize the interpolant process to minimize the number of energy function evaluations during training, resulting in an efficient and scalable method for sampling unnormalized densities. Furthermore, our formulation naturally extends to Riemannian manifolds, enabling diffusion-based sampling in geometries beyond Euclidean space. We derive a closed-form formula for the conditional drift on constant curvature manifolds, including hyperspheres and hyperbolic spaces. We evaluate Flow Sampling on synthetic energy benchmarks, small peptides, large-scale amortized molecular conformer generation, and distributions supported on the sphere, demonstrating strong empirical performance.

---


### 205. [3D Human Face Reconstruction with 3DMM face model from RGB image](https://arxiv.org/abs/2605.03996)

**<font color=#1a73e8>作者：</font>** Zhangnan Jiang, Zichen Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nowadays as convolution neural networks demonstrate its powerful problem-solving ability in the area of image processing, efforts have been made to reconstruct detailed face shapes from 2D face images or videos. However, to make the full use of CNN, a large number of labeled data is required to train the network. Coarse morphable face model has been used to synthesize labeled data. However, it is hard for coarse morphable face models to generate photo-realistic data with detail such as wrinkles. In this project, we present a pipeline that reconstructs a human face 3D model from a single RGB image. The pipeline includes face detection, landmark detection, regression of 3DMM model parameters, and soft rendering. Mentor: Zhipeng Fan (Email: zf606@nyu.edu) Code Repository: this https URL reconstruction Code Reference: this https URL pytorch

---


### 206. [RD-ViT: Recurrent-Depth Vision Transformer for Semantic Segmentation with Reduced Data Dependence Extending the Recurrent-Depth Transformer Architecture to Dense Prediction](https://arxiv.org/abs/2605.03999)

**<font color=#1a73e8>作者：</font>** Renjie He  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) achieve state-of-the-art segmentation accuracy but require large training datasets because each layer has unique parameters that must be learned independently. We present RD-ViT, a Recurrent-Depth Vision Transformer that adapts the Recurrent-Depth Transformer (RDT) architecture to dense prediction tasks, supporting both 2D and 3D inputs. RD-ViT replaces the deep stack of unique transformer blocks with a single shared block looped T times, augmented with LTI-stable state injection for guaranteed convergence, Adaptive Computation Time (ACT) for spatial compute allocation, depth-wise LoRA adaptation, and optional Mixture-of-Experts (MoE) feed-forward networks for category-specific specialization. We evaluate on the ACDC cardiac MRI segmentation benchmark in both 2D slice-level and 3D volumetric settings with exclusively real experiments executed in Google Colab. In 2D, RD-ViT outperforms standard ViT at 10% training data (Dice 0.774 vs 0.762) and at full data (0.882 vs 0.872). In 3D, RD-ViT with MoE achieves Dice 0.812 with 3.0M parameters, reaching 99.4% of standard ViT performance (0.817) at 53% of the parameter count. MoE expert utilization analysis reveals that different experts spontaneously specialize for different cardiac structures (RV, MYO, LV) without explicit routing supervision. ACT halting maps show higher compute allocation at cardiac boundaries, and the mean ponder time decreases from 2.6 to 1.4 iterations during training, demonstrating learned computational efficiency. Depth extrapolation enables inference with more loops than training without degradation. All code, notebooks, and results are publicly released.

---


### 207. [Physics-Grounded Multi-Agent Architecture for Traceable, Risk-Aware Human-AI Decision Support in Manufacturing](https://arxiv.org/abs/2605.04003)

**<font color=#1a73e8>作者：</font>** Danny Hoang, Ryan Matthiessen, Christopher Miller 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> High-precision CNC machining of free-form aerospace components requires bounded compensations informed by inspection, simulation, and process knowledge. Off-the-shelf large language model (LLM) assistants can generate text, but they do not reliably execute risk-constrained multi-step numerical workflows or provide auditable provenance for high-stakes decisions. We present multi-agent knowledge analysis (MAKA), a human-in-the-loop decision-support architecture that separates intent routing, tools-only quantitative analysis, knowledge graph retrieval, and critic-based verification that enforces physical plausibility, safety bounds, and provenance completeness before recommendations are surfaced for human approval. MAKA is instantiated on a Ti-6Al-4V rotor blade machining testbed by fusing virtual-machining path-tracking error fields, cutting-force and deflection simulations, and scan-based 3D inspection deviation maps from 16 blades. The analysis decomposes deviation into an evidence-linked pathing component, a drift-based wear proxy capturing systematic evolution across parts, a residual systematic compliance term, and a variability proxy for instability-aware escalation. In a three-level tool-orchestration benchmark (single-step through $\geq$3-step stateful sequences), MAKA improves successful tool execution by up to 87.5 percentage points relative to an unstructured single-model interaction pattern with identical tool access. Digital twin what-if studies show MAKA can coordinate traceable compensation candidates that reduce predicted surface deviation from order $10^{-2}$in to approximately $\pm 10^{-3}$in over most of the blade within the simulation environment, providing a pre-deployment verification signal for risk-aware human decision-making.

---


### 208. [Enhanced 3D Brain Tumor Segmentation Using Assorted Precision Training](https://arxiv.org/abs/2605.04008)

**<font color=#1a73e8>作者：</font>** Adwaitt Pandya, Ozioma C. Oguine, Harita Bhargava 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A brain tumor is a medical disorder faced by individuals of all demographics. Medically, it is described as the spread of non-essential cells close to or throughout the brain. Symptoms of this ailment include headaches, seizures, and sensory changes. This research explores two main categories of brain tumors: benign and malignant. Benign spreads steadily, and malignant expresses growth, making it dangerous. Early identification of brain tumors is a crucial factor for the survival of patients. This research provides a state-of-the-art approach to the early identification of tumors within the brain. We implemented the SegResNet architecture, a widely adopted architecture for three-dimensional segmentation, and trained it using the automatic multi-precision method. We incorporated the dice loss function and dice metric for evaluating the model. We got a dice score of 0.84. For the tumor core, we got a dice score of 0.84; for the whole tumor, 0.90; and for the enhanced tumor, we got a score of 0.79.

---


### 209. [SymptomAI: Towards a Conversational AI Agent for Everyday Symptom Assessment](https://arxiv.org/abs/2605.04012)

**<font color=#1a73e8>作者：</font>** Joseph Breda, Fadi Yousif, Beszel Hawkins 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models excel at diagnostic assessments on currated medical case-studies and vignettes, performing on par with, or better than, clinical professionals. However, existing studies focus on complex scenarios with rich context making it difficult to draw conclusions about how these systems perform for patients reporting symptoms in everyday life. We deployed SymptomAI, a set of conversational AI agents for end-to-end patient interviewing and differential diagnosis (DDx), via the Fitbit app in a study that randomized participants (N=13,917) to interact with five AI agents. This corpus captures diverse communication and a realistic distribution of illnesses from a real world population. A subset of 1,228 participants reported a clinician-provided diagnosis, and 517 of these were further evaluated by a panel of clinicians during over 250 hours of annotation. SymptomAI DDx were significantly more accurate (OR = 2.47, p < 0.001) than those from independent clinicians given the same dialogue in a blinded randomized comparison. Moreover, agentic strategies which conduct a dedicated symptom interview that elicit additional symptom information before providing a diagnosis, perform substantially better than baseline, user-guided conversations (p < 0.001). An auxiliary analysis on 1,509 conversations from a general US population panel validated that these results generalize beyond wearable device users. We used SymptomAI diagnoses as labels for all 13,917 participants to analyze over 500,000 days of wearable metrics across nearly 400 unique conditions. We identified strong associations between acute infections and physiological shifts (e.g., OR > 7 for influenza). While limited by self-reported ground truth, these results demonstrate the benefits of a dedicated and complete symptom interview compared to a user-guided symptom discussion, which is the default of most consumer LLMs.

---


### 210. [Probabilistic-bit Guided CDCL for SAT Solving using Ising Consensus Assumptions](https://arxiv.org/abs/2605.04033)

**<font color=#1a73e8>作者：</font>** Melki Bino  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Boolean satisfiability (SAT) solvers are widely used in hardware verification, cryptanalysis, automatic test-pattern generation, and side-channel reasoning workflows. Modern conflict-driven clause-learning (CDCL) solvers are highly effective, but satisfiable instances may still require substantial conflict analysis and Boolean propagation before identifying productive regions of the search space. This paper studies a hybrid SAT-solving framework in which a probabilistic-bit (p-bit) Ising sampler proposes high-agreement literals that are passed to CDCL as temporary assumptions. The goal is not to replace CDCL, but to evaluate whether stochastic low-violation samples can reduce CDCL internal search effort while retaining correctness through CDCL fallback. On selected controlled-backbone random 3-SAT benchmarks, the hybrid method reduces median conflicts by 80.8-85.5% and median propagations by 80.2-84.6% relative to pure CDCL. The observed benefit is distribution-sensitive, suggesting that p-bit guidance is effective only for certain instance classes. We further report exploratory machine-learning gates that estimate when hybrid solving is likely to help. On the selected run, a random-forest gate retains 94.8% of hybrid wins, indicating that lightweight gating may help avoid unproductive hybrid calls.

---


### 211. [Large-Scale High-Quality 3D Gaussian Head Reconstruction from Multi-View Captures](https://arxiv.org/abs/2605.04035)

**<font color=#1a73e8>作者：</font>** Evangelos Ntavelis, Sean Wu, Mohamad Shahbazi 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose HeadsUp, a scalable feed-forward method for reconstructing high-quality 3D Gaussian heads from large-scale multi-camera setups. Our method employs an efficient encoder-decoder architecture that compresses input views into a compact latent representation. This latent representation is then decoded into a set of UV-parameterized 3D Gaussians anchored to a neutral head template. This UV representation decouples the number of 3D Gaussians from the number and resolution of input images, enabling training with many high-resolution input views. We train and evaluate our model on an internal dataset with more than 10,000 subjects, which is an order of magnitude larger than existing multi-view human head datasets. HeadsUp achieves state-of-the-art reconstruction quality and generalizes to novel identities without test-time optimization. We extensively analyze the scaling behavior of our model across identities, views, and model capacity, revealing practical insights for quality-compute trade-offs. Finally, we highlight the strength of our latent space by showcasing two downstream applications: generating novel 3D identities and animating the 3D heads with expression blendshapes.

---


### 212. [UniCorrn: Unified Correspondence Transformer Across 2D and 3D](https://arxiv.org/abs/2605.04044)

**<font color=#1a73e8>作者：</font>** Prajnan Goswami, Tianye Ding, Feng Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual correspondence across image-to-image (2D-2D), image-to-point cloud (2D-3D), and point cloud-to-point cloud (3D-3D) geometric matching forms the foundation for numerous 3D vision tasks. Despite sharing a similar problem structure, current methods use task-specific designs with separate models for each modality combination. We present UniCorrn, the first correspondence model with shared weights that unifies geometric matching across all three tasks. Our key insight is that Transformer attention naturally captures cross-modal feature similarity. We propose a dual-stream decoder that maintains separate appearance and positional feature streams. This design enables end-to-end learning through stack-able layers while supporting flexible query-based correspondence estimation across heterogeneous modalities. Our architecture employs modality-specific backbones followed by shared encoder and decoder components, trained jointly on diverse data combining pseudo point clouds from depth maps with real 3D correspondence annotations. UniCorrn achieves competitive performance on 2D-2D matching and surpasses prior state-of-the-art by 8% on 7Scenes (2D-3D) and 10% on 3DLoMatch (3D-3D) in registration recall. Project website: this https URL

---


### 213. [A Closed-Form Adaptive-Landmark Kernel for Certified Point-Cloud and Graph Classification](https://arxiv.org/abs/2605.04046)

**<font color=#1a73e8>作者：</font>** Sushovan Majhi, Atish Mitra, Žiga Virk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce PALACE (Persistence Adaptive-Landmark Analytic Classification Engine), the data-adaptive companion to PLACE, paying a small cross-validation tier on three knobs (budget, radii, bandwidth; $\leq 5$ choices each). A cover-theoretic core (Lebesgue-number criterion on the landmark cover) yields four closed-form guarantees. (i) A structural lower distortion bound $\lambda(\tau;\nu)$ on $\mathcal{D}_n$ under cross-diagram non-interference, with a $(D/L)^2$ budget reduction over the uniform grid when diagrams concentrate. (ii) Equal weights $w_k = K^{-1/2}$ maximizing $\lambda$, and farthest-point-sampling positions $2$-approximating the optimal $k$-center covering radius; both derived from training labels alone, no gradient training. (iii) A kernel-RKHS classification rate $O((k-1)\sqrt{K}/(\gamma\sqrt{m_{\min}}))$ with binary necessity threshold $m = \Omega(\sqrt K/\gamma)$ from a matching Le Cam lower bound, and a closed-form filtration-selection rule. The kernel-Mahalanobis margin $\hat\rho_{\mathrm{Mah}}$ is the strongest closed-form ranker across the chemical-graph pool (mean Spearman $\rho \approx +0.60$); the isotropic surrogate $\hat\gamma/\sqrt{K}$ admits a selection-consistency rate, and $\widehat{\lambda}$ from (i) provides an independent data-level signal (positive on COX2 and PTC). (iv) A per-prediction certificate, in non-asymptotic Pinelis and asymptotic Gaussian forms, with no calibration split. Empirically, PALACE is the strongest closed-form diagram-based method on Orbit5k ($91.3 \pm 1.0\%$, matching Persformer), leads every diagram-based competitor on COX2 and MUTAG, and is competitive on DHFR (within 1 pp of ECP). At $8\times$ domain inflation, adaptive placement maintains $94\%$ while the uniform grid collapses to chance ($25\%$ on 4-class data).

---


> [!TIP]
> 当前位于：**201-213**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-213**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

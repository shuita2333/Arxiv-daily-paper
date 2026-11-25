# 📦 其他研究 | 2026年11月26日

> 本类共 **342** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-342](./part-07.md)

---

### 51. [Spec$^2$R: Recovering Emergent Properties in Supervised Vision Transformers](https://arxiv.org/abs/2611.31589)

**<font color=#1a73e8>作者：</font>** Adam Wróbel, Jacek Tabor, Bartosz Zieliński 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) have achieved strong performance across computer vision tasks, but the quality of their learned representations differs drastically depending on the training paradigm. While self-supervised ViTs often demonstrate emergent properties, such as object-aligned patch representations and attention maps, supervised ViTs typically lack these properties, even when trained with strong data augmentations. Understanding the origin of this difference is important for explaining and controlling the object-level structure. To investigate it, we perform a spectral analysis of supervised and self-supervised models, and identify a key distinction: MLP layers in supervised ViTs introduce high-frequency variations into patch representations, disrupting their spatial organization. Motivated by this finding, we propose Spec$^2$R, a lightweight spectral regularization method that fine-tunes the MLP layers of pretrained supervised ViTs. Spec$^2$R recovers object-aligned patch representations and attention maps, while improving adversarial robustness and preserving competitive classification accuracy.

---


### 52. [RePT: 3D Geometry Emerges from 2D Relational Pretraining](https://arxiv.org/abs/2611.31601)

**<font color=#1a73e8>作者：</font>** Xize Duan, Binke Hou, Xingqiao Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning spatial representations often relies on explicitly predicting geometric quantities, but how physical geometry is organized within learned representations remains less understood. We ask whether 3D structure can emerge from learning relations across 2D observations, without 3D prediction targets. We introduce RePT, which learns compact relations between distinct physical points through cross-view 2D point prediction. The learned relation space develops a geometric organization in which magnitudes, angles, and neighborhoods reflect physical 3D displacement. A single linear readout fitted on 16 scenes recovers displacement length and angle on 39 held-out scenes without refitting (Pearson r = 0.72 and 0.78). The ARKitScenes-trained checkpoint also retains strong geometric organization on ScanNet++, showcasing generalizability. In controlled comparisons, distinct-point relational prediction consistently yields stronger geometric organization than matched same-point correspondence learning. This organization depends on additive relations and adaptive scene context, and higher point-transfer accuracy does not by itself produce stronger organization. More broadly, our results suggest that 3D geometry need not be an explicit prediction target and can instead emerge as a structural property of representations trained to relate 2D observations, pointing to relational prediction as a complementary route to learning the representations that spatial intelligence builds on.

---


### 53. [Noise-Level Adjacency in Diffusion Training](https://arxiv.org/abs/2611.31605)

**<font color=#1a73e8>作者：</font>** T. Y. Tsui, Jiatao Gu, Lingjie Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models train one network across all noise levels, although their training objective is pointwise in the noise level. If training on each pair of adjacent levels were an independent problem, separate networks with the same total parameter count would be expected to match one shared network. But in practice, on images, sharing weights across levels gives better results, which hints at an implicit dependence on their order. An order fixes both which levels are adjacent and the direction in which they run. In this paper, we show that, of the two, the benefit of sharing rests on adjacency in the noise-level embedding. The fitting error of a shared network is bounded below by the distances between neighbouring posterior means, minus the change the network can make between neighbouring embeddings. We first distinguish adjacency from direction: on a Gaussian mixture and CIFAR-10, reversing the embeddings keeps every neighbour and leaves the fitting error unchanged, whereas shuffling them raises it. Second, we rule out sharing between distant levels as the source of the benefit: separate networks on contiguous ranges match the shared network at its width, and with the parameters fixed, breaking adjacency at the same places costs less than 40\% of a full shuffle. Dividing the levels at equal shares of these distances lowers the error of all but the smallest networks. We therefore show that the order of the noise levels enters a diffusion model through adjacency, with its direction being a design choice. Our code is available at this https URL.

---


### 54. [Tablassert: Declarative Extraction of Knowledge Graphs from Biomedical Tables](https://arxiv.org/abs/2611.31614)

**<font color=#1a73e8>作者：</font>** Skye L. Goetz, Jared C. Roach, Gwênlyn Glusman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tables published in biomedical research papers, particularly supplemental tables, capture knowledge assertions that may not be in the main text of the manuscript for several reasons, including low statistical significance, space limitations, and narrative scope. These tables include data (e.g., association statistics, assay readouts, curated gene lists, and omics) encoding relationships between biological entities. Tablassert converts such tabular data (Excel, CSV, TSV, Parquet) into knowledge graphs ready for the NCATS Biomedical Data Translator (Fecho et al. 2025). A user declares in YAML how each table's data map to subject-predicate-object-qualifier statements; Tablassert resolves free text (e.g., ''lung cancer'') to standard identifiers, attaches provenance and statistics, and emits graph files conforming to Translator standards (D. Unni, Bruskiewich, and Moxon 2026; D. R. Unni et al. 2022).

---


### 55. [What a Forecasting Leaderboard Can Establish: Resolution Reporting for Zero-Shot Time-Series Models](https://arxiv.org/abs/2611.31619)

**<font color=#1a73e8>作者：</font>** Arya Sikder, Sriram Pillutla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A foundation model for time series is pretrained once and then asked to forecast series it has never seen, so the evidence for it is its score on held-out datasets. Such datasets are scarce, and a few public leaderboards carry most comparisons, yet none of them states how small a difference its datasets can detect. We call that quantity the resolution of a board and introduce Vernier, a tool that computes it from the files a board already publishes. Vernier also reports which entries a board cannot separate from its leader and whether its order changes when unrelated parties submit. GIFT-Eval resolves 6.8 rank places, and its displayed neighbours sit 0.91 apart. The ten places of its top ten hold fewer than two resolvable steps. fev-bench, Chronos Benchmark II and TIME show the same pattern: their resolution is 3.6 to 19 times the gap between neighbours. With each of its 2,554 series as an independent source, BOOM is the one board that resolves its top ten. Below the resolution the order depends on who else submitted: across four boards, rules that rank against the pool reversed 43 top-ten pairs with neither entry rerun, in one update in seven. Boards also do not record how much history a model receives. On 70 configurations, shortening it raised the error of three of four open models, two of them by 15%. We release Vernier, which runs this report with one command on any leaderboard that publishes per-dataset scores: this https URL

---


### 56. [Internal inconsistencies and unresolved experimental evidence in a quantum neurosecurity framework](https://arxiv.org/abs/2611.31622)

**<font color=#1a73e8>作者：</font>** S. Grigorovich, M. Bairachnaya, E. Daroczi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This article presents a technical and theoretical assessment of the Quantum-Entangled Neuro-Symbolic Swarm Federation (QENSSF), a framework intended for privacy-preserving, quantum-secure, AI-powered, multimodal healthcare data analysis, introduced by Ben Othman and Ali (2025). They claim QENSSF is a first-in-class framework with provable privacy and security guarantees, support these with theorems and proofs, report an experimental evaluation on IBM's quantum Eagle processor, report a real-world quantum key distribution (QKD) test, and claim use of real-world multimodal datasets (ADNI, UK Biobank, and MIMIC-IV). Our examination of quantitative support for these claims identified various concerns. Most importantly, the security criterion of a central guarantee (Theorem 1) cannot be satisfied given the risk formulation and relevant constraints, which, along with calculation errors in the proof, directly undermines the claim of provable security. Furthermore, insufficient reporting of biomedical datasets and unresolved discrepancies in the hardware evaluation limit verification of the experimental claims and overall reproducibility. QENSSF identifies a real need: ensuring privacy and security of healthcare data while patients benefit from AI-powered analysis. This need is particularly pressing for sensitive neural data, including the neuroimaging data available through sources such as ADNI. Privacy concerns also extend to wearable EEG data, for which reidentification risks can persist despite deidentification. However, QENSSF's foundational inconsistencies need resolution before it could be considered in the neurosecurity domain.

---


### 57. [What You See Is What You Certify: Concept-Based Certificates for Unseen Compositions](https://arxiv.org/abs/2611.31627)

**<font color=#1a73e8>作者：</font>** Phuc Linh Ngo, Thang Nguyen Duc, Truong Thanh Hung Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept-based models justify a decision by concepts they claim to see, decoded through an explicit ontology. Yet concept predictions are known to leak label information, ignore locality, and be poorly grounded on new attribute combinations. A decision decoded from such concepts can satisfy the ontology and still be wrong, so we ask when it can serve as a certificate. On unseen combinations of familiar parts, a joint concept bottleneck model and a concept embedding model, trained as is standard, certify wrong classes 93-94% of the time despite a correct ontology (60% for a joint model trained only on visible parts and gated by a localizer). The joint model's part errors copy co-occurring values more often than chance (cross-concept shortcutting). Treating the ontology as an error-detecting code, we show that a certificate needs visible evidence excluding every rival, unseen parts reported as such, and rare misreads not driven by a shared shortcut. A minimal reference design, OCVE, reads each part from a local crop in its own forward pass. On unseen FunnyBirds classes, it certifies 52% of images at 0.4% risk, against 14% for mask-pooled features and 33% for full-image part readers (5.6% when trained and gated alike), at similar zero-shot accuracy. The best baselines, even calibrated or restricted to unseen classes, and a decoder counting only agreeing parts remain about 3-8 times riskier. On CUB, isolated region readers are more accurate than an attribute-prototype model (63.1% vs. 55.3%) and certify unseen species at about 6 points less risk than it and about 10 points less than features pooled in the same keypoint boxes. On real traffic signs, isolated readers lower certified risk from 99.8% to 67%, which is still far too high; most remaining errors are misread pictograms. On seen classes the ontology brings no gain over a fairly trained black box, and isolation costs accuracy.

---


### 58. [Open-Set Radio Frequency Fingerprint Identification with Feature Fusion and Vision Transformer](https://arxiv.org/abs/2611.31636)

**<font color=#1a73e8>作者：</font>** Jie Ma, Junqing Zhang, Guanxiong Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Radio frequency fingerprint identification (RFFI) is a promising device authentication technique for the Internet of Things (IoT) that leverages hardware impairments to uniquely identify devices. However, most existing RFFI systems operate under a closed-set assumption and lack the ability to detect rogue devices, which poses significant security risks. In this paper, we propose an open-set RFFI approach that jointly performs rogue device detection and legitimate device classification. Specifically, we designed a multi-task RFFI system that integrates an autoencoder (AE) for rogue device detection and a fully connected (FC) layer for classification. To enrich the feature representation, we generated two channel-independent spectrograms (CISs) with distinct window lengths from the I/Q signals, capturing complementary time-frequency characteristics. These CISs were processed in parallel by two Vision Transformer (ViT) networks, and their outputs were fused via feature concatenation to construct a device fingerprint for both tasks. We built a testbed involving ten legitimate LoRa devices and five rogue devices. We conducted a comprehensive experimental evaluation and compared our approach with several benchmark algorithms. Experimental results show that our fused feature multi-task RFFI consistently outperformed the baselines in both legitimate device classification and rogue device detection. Our proposed approach achieved an accuracy of 91.1% and an area under the curve (AUC) of over 0.72 in a realistic wireless scenario where the signal-to-noise ratio (SNR) was 20 to 30 dB.

---


### 59. [Reward Basis Decomposition for Interpreting Preference Heterogeneity](https://arxiv.org/abs/2611.31640)

**<font color=#1a73e8>作者：</font>** Mohamed I. Eldagla, Ifesi Onubogu, Prerana Rane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Canonical reward models specify the optimization target for AI policies, so understanding the values they encode is important for ensuring AI alignment. Existing interpretability techniques interpret reward models with a single reward head, which cannot distinguish between the values that a population shares and those that vary among individuals. We introduce Reward Basis Decomposition (RBD), which splits per-user weights into a population term and a per-user term. This yields a shared population direction and individual user directions that are analyzed separately via concept alignment and sparse autoencoder decomposition. We verify that RBD can recover artificially planted per-user directions on a synthetic control, then apply it to two real-world multi-preference datasets, PRISM and Community Alignment. In both, we find no individual-user structure, suggesting that a single direction in the reward embedding space accounts for most preferences. We verify that RBD can recover artificially planted per-user directions on a synthetic control, then apply it to two real-world multi-preference datasets, PRISM and Community Alignment. In both, we find no reliable predictive benefit from the fitted per-user terms beyond the shared population direction under our setup. Code and the synthetic dataset are available at this https URL.

---


### 60. [E2SIM: Long-Horizon Simulation of Everyday Human Behavior with Evolving States](https://arxiv.org/abs/2611.31641)

**<font color=#1a73e8>作者：</font>** Ziwei Gong, Xiangyang Yin, Thai Quoc On 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly expected to support users over long periods, across work, and daily life. This requires modeling not only who users are, but also how their goals, interests, activities, and interactions evolve over time. A challenge in longitudinal user simulation is maintaining consistency between these evolving states and the consequences of actions in a shared environment. We introduce E2SIM, a longitudinal user simulation framework that jointly models evolving actor states and a dynamic shared environment. E2SIM connects actor-state updates with shared-world changes through a feedback loop linking immediate actions, delayed outcomes, and actor-specific observations across work and life. This allows the consequences of earlier actions to shape later behavior, while preserving differences in what each actor knows. We further propose a suite of longitudinal trajectory diagnostics, measuring dynamic consistency, coherent event progression and collaboration, and non-degenerate trajectory development rather than static consistency alone. In one 60-day simulation, E2SIM produced more extracted event threads judged meaningful by our evaluator and fewer near-duplicate actions than four direct-generation baselines. The framework and evaluation methods provide a basis for studying longitudinal user simulation, with potential applications in training and evaluating AI agents that assist users over extended periods.

---


### 61. [MSW: a Multi-Scale Sliced Wasserstein Distance Between Image Distributions](https://arxiv.org/abs/2611.31647)

**<font color=#1a73e8>作者：</font>** Youssef Haouchat, Stanislas Ducotterd, Bassam El Rawas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose the multi-scale sliced Wasserstein (MSW) distance between image distributions, which operates in pixel space and requires no trained network. MSW convolves images with a fixed bank of discrete cosine filters at several scales, pools the responses over all positions, and compares the resulting one-dimensional distributions using the Wasserstein distance. We pair MSW with an exact two-sample test that gives calibrated p-values. Most metrics compare two image sets in the latent space of a pretrained network. We show that these metrics are insensitive to simple perturbations of the images, because the latent space is nearly invariant to them. In contrast, MSW detects smaller perturbations than latent-space metrics and needs far fewer images to do so. Although it uses no learned features, it still detects semantic changes of the image distribution. Finally, MSW matches or outperforms existing Wasserstein-based metrics in our experiments.

---


### 62. [Anchoring VAE Fine-Tuning to Its Latent Diffusion Prior](https://arxiv.org/abs/2611.31651)

**<font color=#1a73e8>作者：</font>** Rafael Bischof, Dominik Narnhofer, Julius Erbach 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained latent diffusion models are effective priors for transfer learning, from geometry estimation to physics simulation. Existing approaches fine-tune the diffusion backbone but freeze the encoder of the VAE to preserve the latent distribution. However, a frozen encoder may miss salient details in non-RGB inputs and is limited to three channels. We introduce Diffusion Prior Anchoring (DPA), a regularizer applied during VAE fine-tuning that uses a score-distillation update to steer latents toward the high-density manifold on which the pretrained diffusion model denoises accurately. We validate DPA across three image and video models (FLUX 3, LTX-Video, Wan2.2) and four tasks: monocular depth estimation, MRI reconstruction, wind-flow simulation, and surface normal estimation, where DPA lowers the prediction error by 7.5% relative to the frozen VAE, 4.9% to decoder-only fine-tuning, and 4.0% to unanchored VAE fine-tuning. Its gain grows the further the target data lies from the RGB training distribution, from 3.3% on monocular depth estimation to 7.2% on complex-valued MRI. DPA also applies to modified VAEs, including pruned and multi-channel variants. With a four-channel VAE that encodes depth and surface normals, it lowers depth estimation error by 9.3%.

---


### 63. [Constructing physical mechanisms with artificial intelligence](https://arxiv.org/abs/2611.31653)

**<font color=#1a73e8>作者：</font>** Vladimir A. Baulin, Austin Cook, Shagor Rahman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mechanisms recur across the sciences: the equation for heat in a solid also describes molecular diffusion or a Brownian particle. A mechanism is rarely written in one equation; its operation, boundaries, parameters and closures are stated at different steps of a derivation, where methods that read text or fit formulas miss it. We built an equation-native system that reads the equations of all 2.5 million arXiv manuscripts, and show that mechanisms can be compiled from them and constructed by deterministic calculation. A constructor detaches, transfers, unfolds, composes and joins their parts across disciplines; where parts do not fit, the failure is an equation for the missing term. Constructions turn a threshold reactor into a memory that a weak signal writes, an oscillator into a switch through two changes that each fail alone, and a rhythm into the regulator of a chemical amount, each with conditions for an experimental test.

---


### 64. [Stranded Compute in AI Inference Workloads: Recovering Value Through Demand Aggregation](https://arxiv.org/abs/2611.31654)

**<font color=#1a73e8>作者：</font>** Sam Kingsley  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI inference infrastructure is commonly analyzed as an energy business. Under full total cost accounting it is not: in the reference deployment modeled here, capital recovery is 87.3% of fully loaded cost per token and electricity 3.7%. Because capital accrues per unit time irrespective of use, accelerator value is destroyed by non-utilization rather than by consumption. Yet, SLO qualified goodput reaches only 59.6% of nameplate throughput, and the decomposition of the loss chain shows that 25.2 of the 40.4 lost percentage points arise from scheduling idleness and stranded burst reserve. Both are properties of a tenant's demand portfolio rather than of its silicon, and neither is diversifiable by a single tenant acting alone. Modelling reserve and idle capacity as diversifiable risk, pooling demand across eight imperfectly correlated tenants (rho = 0.3) recovers 7.3 pp of goodput, approximately $0.75M per annum per megawatt of IT capacity, or between 2.8x and 4.9x the entire annual interconnection spend of the deployment that produced it. The implication for neutral colocation and interconnection providers is that the switching and interconnection layer aggregating tenant demand functions as an instrument of capital productivity while being priced as transport.

---


### 65. [Boundary Representation-Driven Graph Transformer Modeling for Machining Operation Sequencing](https://arxiv.org/abs/2611.31661)

**<font color=#1a73e8>作者：</font>** Fatemeh Elhambakhsh, Gaurav Ameta, Aditi Roy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machining process planning is inherently complex due to the interdependence between part geometry, machining operations, and evolving manufacturable states. Traditional approaches rely heavily on expert knowledge and rule-based systems, limiting scalability and automation. While recent machine learning methods have shown promise, most operate on simplified geometric representations, such as voxels or hand-crafted features, which fail to fully exploit the rich geometric and topological information encoded in Boundary Representation (B-Rep) models. In this work, we propose a graph transformer-based framework for geometry-to-sequence learning that directly predicts machining operation sequences from B-Rep design geometry. The proposed method constructs topology-aware graphs from B-Rep entities, where faces and their adjacencies are encoded as node and edge features capturing both geometric and relational information. A graph neural network encoder learns geometry-aware embeddings, which are then used to condition a dual-decoder transformer that autoregressively generates machining operation sequences. This formulation enables the model to capture both operation-type prediction and process-level ordering constraints directly from design geometry, without requiring intermediate feature extraction or machining-state representations. Experiments on a dataset of 2,991 synthetic machined parts demonstrate strong performance, achieving 95% accuracy for main operation prediction, 64% accuracy for sub-operation prediction, and 93% accuracy for sequence length prediction. Further analysis shows that the model effectively captures precedence relationships and geometry-dependent constraints inherent in machining processes. These results highlight the potential of B-Rep-driven graph learning for scalable and automated machining process planning.

---


### 66. [LineEX: Data Extraction from Scientific Line Charts](https://arxiv.org/abs/2611.31664)

**<font color=#1a73e8>作者：</font>** VP Shivasankaran, Muhammad Yusuf Hassan, Mayank Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce LINEEX that extracts data from scientific line charts. We adapt existing vision transformers and pose detection methods and showcase significant performance gains over existing SOTA baselines. We also propose a new loss function and present its effectiveness against existing loss functions. In addition, we synthetically created the largest line chart dataset comprising 430K images. The code is available at this https URL.

---


### 67. [A Piecewise-Linear Activation Function for Implicit Neural Representations](https://arxiv.org/abs/2611.31666)

**<font color=#1a73e8>作者：</font>** Shahd Hekal, Joram Kim, Jeova Farias Sales Rocha Neto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coordinate networks with ReLU activations perform poorly on implicit neural representation tasks, and the activations that address this, such as sinusoids and Gabor wavelets, all leave the piecewise-linear function class, so it remains unclear which property of ReLU is at fault. We introduce JaSIN, a family of bounded piecewise-linear activations that interpolates between ReLU and a piecewise-linear sinusoid without any the use of transcendental operation. Our results show that a bounded range improves image reconstruction PSNR on average by 0.06 dB, a single bump 3.29 dB, and centering that bump a further 3.64 dB. The oscillation count improves 6.30 dB more, raising ReLU from 24.0 to 37.3 dB on Kodak images, placing third over eleven activations, within 1.3 dB of the state-of-the-art, though beyond four oscillations the reconstruction collapses. Because an INR is fit on the grid on which it is evaluated, a unit whose pre-activations never reach the support of its activation is certifiably inactive over the entire domain; deleting such units is lossless without fine-tuning, removing up to 84% of parameters at zero loss in performance (dB) and decoding 3.2 times faster. Reference code and demos are available at this https URL.

---


### 68. [Neural Interoperability Protocols: Specifying Compatibility Before Training](https://arxiv.org/abs/2611.31670)

**<font color=#1a73e8>作者：</font>** Alireza Bagheri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks are increasingly developed as reusable components, yet their intermediate representations remain difficult to exchange across independently trained models. Existing approaches can align representations or encourage compatible features, but successful transfer between particular models does not by itself define what future implementations must satisfy to interoperate. We introduce Neural Interoperability Protocols (NIPs), a specification-first framework that treats neural compatibility as a set of public interface obligations rather than a property inferred solely from model-pair performance. A NIP specifies an exchange boundary, the semantics and admissibility conditions of exchanged packets, and the downstream computations that recipients must support, independently of the architectures and training procedures implementing it. We investigate this distinction through controlled retrieval, vision, and continuous-memory experiments involving independently trained models, differing architectures and objectives, and later training cohorts. Matched-competence controls demonstrate that native task success does not ensure interoperability, while shared semantic supervision enables substantial direct transfer in the evaluated settings. Withheld-information experiments show that recipient models can continue computations requiring information unavailable to donors at exchange time. Partial-contract experiments and packet interventions further establish that observed compatibility is conditional on the semantics, packet populations, and recipient continuations being evaluated. Together, these results support public neural interface specifications as a framework for designing prospective component exchange and distinguishing demonstrated interoperability from stronger conformance claims.

---


### 69. [Curvature-Equilibrated Policy Optimization for Deep Reinforcement Learning](https://arxiv.org/abs/2611.31680)

**<font color=#1a73e8>作者：</font>** Gang Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient-based actor optimization is central to deep reinforcement learning. However, conventional first-order optimizers do not explicitly exploit the local curvature of neural actor losses. We propose EQUIP (Curvature-Equilibrated Gradients for Policy Search), a novel approach that seeks to balance local contraction and expansion of the actor parameter space by equilibrating positive and negative curvature. EQUIP constructs a trajectory-informed search subspace and uses the projected Hessian of actor loss to build a bounded local metric for curvature equilibration. First-order loss matching preserves the approximated first-order decrease in actor loss. Meanwhile, gradient mixing and curvature-based gradient selection adjust the gradient applied for actor optimization. We establish the geometric properties of curvature equilibration, derive bounds on gradient alignment and magnitude, and identify conditions for improved actor loss reduction and convergence toward stationarity under direct gradient updates. We integrate EQUIP into Soft Actor-Critic (SAC) without modifying its actor loss, critic learning, or replay mechanism. Experiments on 6 MuJoCo continuous control benchmarks show that the resulting EQUIP-SAC algorithm achieves higher mean sample efficiency than SAC and two second-order policy optimization baselines. Ablation studies further highlight the benefits of curvature equilibration and trajectory-informed geometry for policy training.

---


### 70. [CROSS-Calib: Selective Channel Calibration for Ultrasound Reconstruction](https://arxiv.org/abs/2611.31684)

**<font color=#1a73e8>作者：</font>** Tongxiao Hu, Junyu Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ultrasound imaging provides views of internal tissue in real time for medical diagnosis. However, ultrasound signals may be affected by interference, and correcting errors and removing transient interference while preserving valid echoes remains challenging. We propose CROSS-Calib, a channel recovery method that uses predictions from other channels as references for amplitude and phase calibration, while a gate using context selectively combines calibrated measurements with predicted echoes to retain usable samples and repair unreliable ones. On the in vivo test set, CROSS-Calib outperforms all baseline models under gain errors and transient interference, while phantom tests show that the model restores cyst contrast with echo widths of wire targets close to the clean reference. CROSS-Calib can perform channel calibration and selective repair before beamforming to improve echo usability and image quality.

---


### 71. [Harvesting Apple's Orchard: A Security Analysis of On-Device CoreML Models Across the Apple Ecosystem](https://arxiv.org/abs/2611.31688)

**<font color=#1a73e8>作者：</font>** Justice Owusu Agyemang, Winifred Harriet Asante, Kwame Opuni-Boachie Obour Agyekum 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Apple ships hundreds of task-specific machine-learning models inside iOS, iPadOS, macOS, and tvOS. We present, to our knowledge, the first systematic security analysis of this on-device surface. We harvested 1,137 CoreML artifacts from six platform images and two device harvests, and a conversion pipeline recovered 155 previously opaque bundles as loadable mlpackage archives. Eight findings. (1) 368 of 1,137 artifacts expose plaintext learned parameters (281 blobs, 369.61 MiB) and 166 of 166 MIL bundles leak internal model-database tokens. (2) Specification versions 1-9 coexist and locale variants diverge architecturally. (3) Across 82,092 adversarial evaluations (221 model paths), worst-case flip rates reach 100%; zero-width spaces flip 65% of the Indian-English and 70% of the US-English SMS filter. (4) A 16-byte weight edit flips 7 of 8 probe inputs of a system model, with no runtime integrity check observed. (5) Loading Apple's own hand-gesture model crashes libBNNS through the public CoreML API (4/4 on production M2, also macOS 27.0); Apple ruled it a self-crash outside the security boundary. (6) Eleven bundles ship isUpdatable=1 hooks. (7) SMS text-classifier latency is 13.1-52.0 ms, 92.4% in the CPU-side NLP core, not the ANE. (8) The classifiers label 8-9 of 10 phishing messages Transactional. We filed three reports with Apple Product; all were declined as not crossing a security boundary, and we report the findings as robustness results.

---


### 72. [GeoMVGen: Joint Appearance-Geometry Modeling for Multi-View Video Generation in Robotic Manipulation](https://arxiv.org/abs/2611.31689)

**<font color=#1a73e8>作者：</font>** Qiaoqiao Jia, Guile Wu, Dongfeng Bai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic manipulation requires predicting how robot-object interactions evolve over time, encompassing both visual appearance and scene geometry. In multi-camera settings, such predictions need to capture the evolving 3D scene consistently across viewpoints, while supporting controllable generation under different robot actions and camera configurations. Existing video generation models provide strong priors for visual appearance and motion but typically lack explicit geometric modeling. Meanwhile, recent advances in geometry-aware and multi-view generation have explored joint appearance-geometry modeling and cross-view consistency, yet generating temporally coherent appearance and geometry across multiple viewpoints under robotic manipulation conditions remains challenging. In this work, we propose GeoMVGen, a framework for joint multi-view RGB and pointmap video generation in robotic manipulation. Built on a video diffusion transformer, our framework employs modality-specific adaptation modules to capture the distinct characteristics of appearance and geometry, while using cross-modal residual connections to facilitate information exchange between the two modalities. To establish geometric correspondences across viewpoints, we further introduce a cross-view projection mechanism with complementary geometric supervisions, combining pointmap consistency with geometry foundation model-guided feature alignment. These designs enable controllable generation of temporally evolving multi-view observations with coherent appearance and geometrically consistent scene structures. Extensive experiments on 4D video generation dataset comprising simulated and real-world robotic manipulation scenarios demonstrate that GeoMVGen outperforms state-of-the-art methods in video quality, geometric accuracy, and cross-view consistency.

---


### 73. [GRUN: Generalized Retinex Unfolding Network for Image Restoration](https://arxiv.org/abs/2611.31690)

**<font color=#1a73e8>作者：</font>** Rihan Zhang, Fengyang Xiao, Yuhan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image restoration remains a fundamental challenge in low-level vision, requiring methods that handle diverse degradations while preserving scene structures and details. We revisit classical Retinex theory and propose a Generalized Retinex formulation that extends the illumination-reflectance decomposition into a Retinex-inspired content-environment factorization prior for image restoration. The key idea is to restore images using two learned factors: a content-dominant response (generalized reflectance) capturing scene properties and an environment-side response (generalized illumination) encoding task-dependent variations associated with the observed degradations. Based on this formulation, we develop GRUN (Generalized Retinex Unfolding Network), a MAP-guided deep unfolding framework that alternates reflectance restoration, illumination estimation, and progressive degradation inference across K stages with degradation-conditioned proximal operators. We further introduce a Degradation-aware Coupling Regularizer (DCR) that combines mutual information minimization, gradient decorrelation, and scale anchoring to promote complementary content-environment factor representations. Experiments on seven image restoration tasks, including denoising, dehazing, deraining, low-light enhancement, deblurring, underwater enhancement, and backlit enhancement, demonstrate competitive results on multiple benchmarks using the same architecture with task-specific weights. Moreover, the proposed Generalized Retinex design can be integrated into existing restoration methods, demonstrating its cross-architecture applicability. Code will be released.

---


### 74. [PRETZEL: A Benchmark for Cyclic Peptide Structure Prediction](https://arxiv.org/abs/2611.31708)

**<font color=#1a73e8>作者：</font>** Yongchan Hong, Zihang Fang, Mukta Ubale 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Macrocyclic peptides are a growing therapeutic modality, and co-folding models are increasingly used to predict their structures. Yet published evaluations rely on small, loosely curated target sets that differ from paper to paper, so results are not comparable, and most report pose RMSD alone, without checking whether the predicted molecule is chemically correct. We introduce PRETZEL (Prediction of Ring-Enclosed Topology: Zero-shot Evaluation of cycLic peptides), a benchmark of 285 curated cyclic peptide-protein complexes spanning three cyclization chemistries, all post-dating the training cutoff of every model evaluated. PRETZEL has three components: PRETZEL-SET, an evaluation set annotated by cyclization chemistry and chemical novelty; PRETZEL-TWIST, a specification layer that compiles a single canonical macrocycle description into each engine's native input format and verifies the returned structure; and PRETZEL-SALT, an evaluation suite pairing standard pose metrics with validity checks for bond distances, bond angles, dihedrals, and ring closure. Using these, we evaluate AlphaFold3, Boltz-2, Protenix-v2, and HighFold3. Protenix-v2 achieves the best median RMSD at 9.05 A, with 19.3% of predictions under 2 A and 37.5% under 5 A. Accuracy varies by cyclization chemistry: models handle head-to-tail macrocycles relatively well but degrade on stapled targets. Chemical validity is weaker still: at most 8.1% of predictions have a fully valid set of inter-residue bonds, and no engine closes every macrocycle in more than 80.7% of its predictions, so pose accuracy alone is an insufficient criterion. These failures share a cause: co-folding models place macrocycles without representing them, treating cyclization and non-canonical chemistry as annotations layered onto a residue sequence rather than as first-class structure. PRETZEL is released with all inputs, predictions, and evaluation code.

---


### 75. [EventSSM: Causal Spatial-State Modelling for Asynchronous Events Event-Depth Estimation](https://arxiv.org/abs/2611.31720)

**<font color=#1a73e8>作者：</font>** Sadiq O. Macaulay, Dipon Ghosh, Hadfield Simon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras report asynchronous brightness changes, yet metric-depth supervision is typically available only at sparsely sampled reference timestamps. Aggregating events into frame-like representations simplifies learning but can obscure the fine-grained temporal structure of the original event stream. We introduce EventSSM, a causal spatial-state framework for event-associated metric-depth estimation using a recurrent memory updated by chronological event packets. To bridge asynchronous predictions and frame-time supervision, predicted event depths are geometrically transported using calibrated camera poses and differentiably rendered at reference timestamps. Benchmark evaluations demonstrate improvements over established event-depth methods across multiple depth-error measures. Controlled ablations further examine cross-modal initialization, temporal recurrence, individual state, readout, and supervision components, and packet subdivision. Together, these findings establish EventSSM as an effective framework for causal event-associated metric-depth estimation, combining persistent spatial context with physically timed state retention.

---


### 76. [SigK: rPPG-based key agreement scheme for mHealth](https://arxiv.org/abs/2611.31721)

**<font color=#1a73e8>作者：</font>** Yanping Wang, Lin Li, Leo Yu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As mobile health advances, the use of biomedical sensors for disease monitoring, diagnosis, and treatment is increasing. These sensors often need to be connected through wireless communication technologies to process physiological information from various body parts effectively. Since the data transmitted in these devices usually contain sensitive personal medical information, it is crucial to establish secure communication between devices. In recent studies, the inter-pulse intervals between heartbeats are often used as the key source. They can be extracted from physiological signals such as photoplethysmogram (PPG) or electrocardiogram (ECG), allowing key agreement schemes without pre-key distribution. However, traditional solutions are based on contact measurement devices (e.g., wristbands, chest straps), which limit their applicability in contactless healthcare scenarios. In this paper, we propose a remote PPG-based key agreement scheme to facilitate secure communication between contactless medical devices. We leverage medical devices equipped with cameras to capture remote PPG signals from human faces, and then utilize the signal's power spectral density and peak-peak interval to establish a key agreement with signals synchronously acquired in the Body Area Network (BAN). We have carried out performance evaluations on three publicly available datasets to demonstrate the feasibility of our proposed scheme. In addition, we have also presented a comprehensive proof of the security of our proposed scheme.

---


### 77. [Tokenization and Architecture Jointly Allocate Component Roles in Time Series Transformers](https://arxiv.org/abs/2611.31730)

**<font color=#1a73e8>作者：</font>** Mingyu Kim, Doguk Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series transformers have achieved strong forecasting performance, yet it remains unclear which of their components, attention or the feed-forward network (FFN), constructs temporal features, and how tokenization such as patching changes this. We propose a temporal probing framework that uses 15 token-level diagnostic tasks to measure feature construction as the gain in linear decodability of temporal properties from one sub-layer to the next (a matched MLP probe already saturates at the embedding). It targets models whose probed representations are read by a linear forecasting head. Applied to 5 supervised models trained on 8 long-term forecasting benchmarks, it finds that the constructing component is not fixed but allocated by the interaction of tokenization and architecture. Under patch tokenization (PatchTST), the FFN's gain exceeds attention's in probing on all 8 datasets, and its 8-dataset mean is 3.2x attention's. Without attention, the FFN alone reaches nearly the same total gain, both when attention is removed from a trained model and when PatchTST is trained without it, and the retrained model forecasts within a few percent of the full model. In probing, attention dominates under variate tokenization (iTransformer); in CATS, cross-attention is the only input path. In a controlled manipulation of PatchTST, single-scalar tokens (P=1) nearly eliminate the FFN's construction, while one more point per token (P=2) restores it. Our forecasting-side interventions (activation patching, knockout, and training without attention) establish component-level reliance and sufficiency. These results offer a representational reading of prior findings on the gains from patching, the competitiveness of self-attention-free models (TSMixer, PatchMLP), and the distinct role of cross-attention in CATS.

---


### 78. [Geo-SMILE: Statistical Model-Agnostic Interpretability with Local Explanations for Geospatial Machine Learning](https://arxiv.org/abs/2611.31731)

**<font color=#1a73e8>作者：</font>** Shadieh Mohammadi, Koorosh Aslansefat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional post-hoc explanation methods were developed largely for non-spatial inputs and often provide limited explicit treatment of geographic context. We introduce Geo-SMILE, a model-agnostic framework that distinguishes substantive Feature explanation from geographic-position response through complementary perturbation branches. The Feature branch masks substantive predictors while retaining observed coordinates; the Geo branch relocates geographic units while holding substantive predictors fixed. Following the statistical-distance-weighted surrogate principle of SMILE, input-distribution Wasserstein distances determine coalition locality weights and weighted Ridge surrogates approximate expected black-box predictions. GeoSensitivity, signed in the keep orientation, quantifies fitted-model responses to geographic-player relocation under the specified design. Across crime prediction in Hull, housing-price prediction in Seattle and ride-hailing demand in Chicago, held-out weighted surrogate fidelity ranges from $R_w^2=0.910$ to $0.989$ in the Feature branch and from $0.842$ to $0.906$ in the Geo branch. The framework makes geographic position an explicit object of post-hoc explanation while requiring separate assessment of interpretation, stability and reference dependence.

---


### 79. [Where is the Interface for the AI Harness?](https://arxiv.org/abs/2611.31739)

**<font color=#1a73e8>作者：</font>** Wafa Johal, Sarah Schombs  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Norman's gulfs of execution and evaluation have guided interaction design for forty years, but both assume a user who is present in the loop. Agentic delegation breaks that assumption: users describe an outcome and leave, while the agent takes hundreds of unseen actions. Starting from a 2026 incident in which a research agent circumvented an access refusal on an Australian government portal and went unnoticed for two months, we argue that delegation opens two new gulfs. The gulf of specification is the gap between what a user wants and their ability to express it, including how the agent should behave in situations nobody foresaw. The gulf of oversight is the gap between what an agent is doing and the user's ability to know, assess, and control it. We argue that both gulfs meet in the harness, the tools, permissions, checks, and loop that surround the model. Harnesses are currently written by developers and hidden from users. We call on HCI to decide which parts of the harness belong to the end-user, which should be visible and adjustable defaults, and which should be built in by design, and to create the interfaces that let ordinary people author and read them.

---


### 80. [TACT-Bench: Testing Adaptive Conversational Threats against Tool-Use Agents](https://arxiv.org/abs/2611.31756)

**<font color=#1a73e8>作者：</font>** Ilia Hashemi Rad, Feijie Wu, Haoyu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing autonomy of AI agents in using external tools and making decisions has created an urgent need for comprehensive safety benchmarks. Existing benchmarks test compromised tool channels or adaptive multi-turn attacks, though they may not capture the unique capabilities of policy-governed tool-use agents, which must resist unauthorized requests without abandoning the legitimate work embedded in the same interaction. To fill this gap, we introduce TACT-Bench, a stateful benchmark built around scenario-specific stories, personas, manipulation tactics, and response-adaptive escalation. Each adversarial task targets an action explicitly prohibited by the policy provided to the assistant, while the policy remains hidden from the attacking user. TACT pairs each adversarial task with at least one benign counterpart, and its adversarial tasks retain authorized ground-truth actions when a compliant resolution remains available. We define these base tasks as TACT-Base. We additionally introduce TACT-TrustPrime, which places an independent benign task before an unrelated attack in the same conversation. We also propose Paired Selective Trustworthiness (PST), which combines explicit safe refusal with demonstrated capability on matched benign tasks, to analyze an agent's overcautiousness and practicality. Averaged across 6 different models as assistants, TACT-Base raises Attack-Induced Failure Rate (AFR) by 17.53% over four compatible attack baselines, and TACT-TrustPrime raises it by a further 17.01%. The two evaluated defense methods reduce AFR by only 8.35%--9.41% on average and do not consistently improve PST, underscoring the need for stronger policy-enforcement methods.

---


### 81. [Xtream: An Explicit Metric State for Large-Scale Streaming Reconstruction](https://arxiv.org/abs/2611.31757)

**<font color=#1a73e8>作者：</font>** Ernesto Lozano, Alberto Jaenal, Javier Civera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D foundation models (3DFMs) enable dense reconstruction in a feed-forward pass, yet their effective span is limited by cross-view attention. Local consistency has been expanded through geometric alignment of video chunks and recursive updates of an implicit memory, and large-scale scenes with pose graphs. However, both strategies are prone to drift, largely due to the lack of metric-scale observability from monocular geometry. We present Xtream,a hybrid streaming pipeline that maintains an explicit metric state through a factor graph over keyframes, while using a 3DFM as a geometric front end. Xtream incorporates metric information in two ways: through metric scale predictions from 3DFMs; or through inertial measurements if available. Across the large-scale benchmarks of VBR, Oxford Spires and KITTI, Xtream achieves state-of-the-art performance in 3DFM-based online reconstruction, reducing average absolute trajectory errors compared with published baselines and concurrent work. this https URL

---


### 82. [RoMo Hands: A Large Scale Richly Organized Text to Hand Motion Dataset](https://arxiv.org/abs/2611.31766)

**<font color=#1a73e8>作者：</font>** Yizhak Ben-Shabat, Jiahao Zhang, Joseph Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While text-driven body motion generation has matured, pure-hand synthesis remains bottlenecked by data. Existing datasets often treat hands as rigid end-effectors, lack fine-grained captions, or are too limited in scale to support robust generalization. We introduce RoMo Hands, an in-the-wild, text-paired dataset of ~542K sequences (884 hours, 95.5M frames at 30 fps) which is an order of magnitude larger than prior work. To ensure high-quality supervision, a stringent dexterity filter discards low-articulation sequences, focusing the distribution on complex bimanual movement. Each clip is paired with five captions at increasing granularities from global semantic tags to atomic finger states, organized under a hierarchical taxonomy. To bridge the gap between body and hand architectures, we propose a novel 393-D bimanual representation that adapts redundant body-motion paradigms to the high-DoF kinematics of hands. Systematic benchmarking of diffusion, masked-token, and autoregressive generators reveals distinct trade-offs under these hand-specific adaptations, including a sharp divergence between semantic alignment and kinematic plausibility. Our dataset, representation, and benchmark establish a rigorous foundation for the next generation of dexterous motion synthesis. Project page: this https URL.

---


### 83. [ET: Efficient Transfer from Softmax to Hybrid Attention](https://arxiv.org/abs/2611.31770)

**<font color=#1a73e8>作者：</font>** Guangfu Guo, Xiaoqian Lu, Linsey Pang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Converting pretrained softmax Transformers to efficient attention often causes substantial performance degradation, while recovery typically requires costly fine-tuning. We propose ET (Efficient Transfer), a framework for high-fidelity attention conversion with minimal optimization cost. ET combines exact local and shared-key softmax attention with a mean-anchored, scan-free global linear correction and adaptive gating, achieving linear complexity in sequence length. To preserve pretrained knowledge, ET freezes pretrained weights and calibrates only newly introduced parameters through alternating least squares on a small set of unlabeled samples, without gradient updates. On ImageNet-1K, ET achieves 79.64% and 81.55% top-1 accuracy on DeiT-S and DeiT-B, respectively, within 0.25 percentage points of their softmax teachers. At $768\times768$, ET outperforms T$^5$ by 3.59 percentage points at comparable inference FLOPs, without gradient-based fine-tuning. On DiT-XL/2, ET achieves an FID-50K of 2.59 with only 250 LoRA updates. On Stable Diffusion 3.5 Medium, ET matches the teacher's GenEval score at 1K resolution with just 0.73 A100 GPU-hours of gradient-free conversion and a 1.39$\times$ inference speedup.

---


### 84. [ReCAP: Sequential Concept Acquisition with Guarantees under Imperfect Concept Predictors](https://arxiv.org/abs/2611.31776)

**<font color=#1a73e8>作者：</font>** Md Nahiduzzaman, Steven Korevaar, Alireza Bab-Hadiashar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sequential concept acquisition enables interpretable diagnosis from a compact set of human-understandable findings. Such explanations are useful only if clinicians can trust them, yet most existing methods treat predicted concepts as correct, so a correct diagnosis can rest on incorrectly predicted evidence. We propose Reliable Concept Acquisition with Pruning (ReCAP), which reasons over what the concept predictor reports, including errors and abstentions, and replaces conditional information gain with a label-discriminating objective that separates cases requiring different diagnoses. We prove this objective adaptively monotone and adaptively submodular, yielding a (1-1/e) guarantee for greedy fixed-budget acquisition that degrades boundedly under learned estimates, and combine it with abstention-aware acquisition and diagnosis-preserving pruning to keep explanations short and reliable. Across five medical imaging datasets, ReCAP reduces the share of correct diagnoses supported by at least one incorrectly predicted concept from 27.1% to 9.6% relative to the strongest baseline, while using fewer than half as many concepts and achieving higher diagnostic accuracy.

---


### 85. [A Well-Posed Fourth-Order Navier-Stokes Model for Image Inpainting: Theory, Order Selection, and Stripe Decomposition](https://arxiv.org/abs/2611.31777)

**<font color=#1a73e8>作者：</font>** Yiwen Dou, Yiqiang Ding, Zhongyun Bao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Navier-Stokes (NS) inpainting model of Bertalmío, Bertozzi and Sapiro is the only transport-type paradigm among PDE-based methods, yet it has never received a systematic higher-order extension. We show that the obvious fourth-order correction is ill-posed, and we construct the corrected, well-posed model. In the vorticity-streamfunction formulation we add a gated fourth-order term whose sign is decisive: the backward form is a Perona-Malik-type anti-diffusion, Hadamard ill-posed and consistently harmful in experiments, whereas the forward form is uniformly parabolic, energy-stable and consistently beneficial. An order-dissipation principle, stating that odd orders are dispersive and even orders dissipative, singles out the fourth order as the lowest admissible one. Large missing blocks pose a separate problem, because the correction gate stays silent there; we answer it with stripe decomposition, a Telea base fill followed by interleaved slit-wise NS passes, which converts block damage into the structural-slit regime where the model excels. The device is base-agnostic, and its gains add to those of the forward correction. On three datasets, namely BSDS500, DIV2K and a classical Chinese painting benchmark, and on three damage types, namely cracks, blocks and text occlusion, the training-free model beats every classical baseline on every sample of structure-dominated damage, gains +1.02 dB PSNR over Telea on the full 42-image painting test set with a 42/42 per-sample win rate, matches the strongest recent PDE solvers within 0.4 dB while attaining the best perceptual quality of the entire PDE family, and runs at 4-16 s per image on a consumer GPU.

---


### 86. [HDMark: Holographic Multi-Bit Model Watermarking for Intellectual Property Protection in Hyperdimensional Computing](https://arxiv.org/abs/2611.31781)

**<font color=#1a73e8>作者：</font>** Hamed Poursiami, Ahmad Tahmasivand, Farshad Soleiman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hyperdimensional computing (HDC) models deployed on edge hardware are valuable intellectual property that is easy to steal, since a trained classifier consolidates its learned knowledge into a compact set of class prototype hypervectors; yet protecting their ownership through watermarking remains largely unexplored. We present HDMark, the first model watermarking framework native to HDC, which encodes ownership in the same hyperdimensional algebra the model computes with. HDMark maps a multi-bit owner identity to secret quasi-orthogonal carriers, superimposes them holographically onto the trained class prototypes, and verifies ownership with a statistical test. Across four datasets and three HDC learning rules, HDMark leaves accuracy essentially unchanged and verifies a 64-bit identity in 99.8% of trials at p < 0.001. We derive closed-form expressions for prediction fidelity and bit recovery that match measurements within 0.4 pp mean absolute error. The watermark survives fine-tuning and low-bit quantization, while attempting to erase it through noise injection, pruning, or overwriting severely degrades model accuracy. We further identify a dimension-permutation attack specific to HDC, which reorders hypervector coordinates to evade verification without altering predictions, and counter it through encoder realignment. Finally, an AMD ZCU104 FPGA implementation confirms that HDMark adds no hardware overhead, remains bit-exact under aggressive undervolting, and stays verifiable under timing faults until the classifier itself fails.

---


### 87. [Byte Patches versus BPE at Matched Data: A Matched-Twin Comparison at 350M Parameters](https://arxiv.org/abs/2611.31790)

**<font color=#1a73e8>作者：</font>** Asadullah Maliyawala, Andrej Lisal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We compare a MEGABYTE-style byte-patch Transformer with a 64-byte sliding local decoder (local64) to a matched byte-level 8k BPE decoder (BPE-8k) under identical raw bytes, document order, and approximately matched bytes per optimizer step: 350M parameters and 10 billion training bytes. Under matched-span document sliding (identical scored byte ranges), BPE-8k leads with relative gaps of -5.2%, -4.9%, -9.3% and -6.1% in bits per byte (overall, text, code, math; paired bootstrap). Downstream, CharBench equal fine-tuning favors local64 (53.7% vs 40.0%), fact200 favors BPE-8k (16.5% vs 7.0%), and PIQA (raw and length-normalized) and ARC-Easy length-normalized favor BPE-8k after Holm correction at alpha = 0.05; remaining tasks are ties. Evaluation pitfalls that changed conclusions include context-length extrapolation past the BPE training context, bits per token reported as bits per byte, and inconsistent byte denominators. Unlike controlled tokenizer studies that vary the subword tokenizer under a fixed token budget, or FLOP-controlled byte-model scaling studies, we hold the raw bytes, their order and the optimizer recipe fixed and ask whether a fixed-patch byte model can replace the tokenizer at all. Limits: one size, one seed, one 8k vocabulary fixed before the runs, and a known difference in embedding initialization between the twins.

---


### 88. [Constructive Causal Abstraction and a Case Study in Mechanistic Interpretability](https://arxiv.org/abs/2611.31795)

**<font color=#1a73e8>作者：</font>** Yuchen Zhu, Sergio Hernan Garrido Mejia, Dominik Janzing  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing frameworks in causal abstraction first propose a high-level causal model, and then verify whether its interventional effects agree with those of a given micro-level model - the two models are declared causally consistent when the discrepancy is zero. However, proposing a consistent macro causal model is difficult, because macro causal relations are almost never well-defined, since distinct micro-level interventions associated with the same apparent macro intervention can produce different effects. Our central insight is that causally consistent macro-level models can be obtained constructively: ill-defined macro interventions can be interpreted as missing variables on the macro level, and can be accounted for by introducing a complementary variable q that retains omitted causally relevant state. In the linear case, q has a unique form and we provide sufficient conditions for valid implementations to exist; in the nonlinear case, we provide an ODE-based algorithm for constructing implementations. We call this framework Constructive Causal Abstraction (CCA), and use CCA to formulate the difference between machine-learning model auditing and editing. With the Bias-in-Bios biographies dataset, we demonstrate that CCA allows practitioners to articulate assumptions when detecting the model's gender bias. Finally, CCA resolves a well-known paradox known as "interpretability illusion" which points to a mismatch between the subspace for editing and the one where the model implements a signal-to-output pathway.

---


### 89. [TopoCryptoEEG: End-to-End Encrypted Framework for Brainprint Authentication](https://arxiv.org/abs/2611.31801)

**<font color=#1a73e8>作者：</font>** Qingyu Zeng, Lei Sun, Shuai Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Brainprint authentication enables continuous identity verification, but EEG data are privacy-sensitive. Existing feature-level encrypted authentication (FLEA) schemes protect extracted features under a trusted-client assumption. We show theoretically and empirically that a compromised client with access to plaintext query features and continuous authentication scores can exactly recover a registered template after finitely many interactions. To address this risk, we propose TopoCryptoEEG, a homomorphic-encryption-based framework that encrypts preprocessed EEG data at the client and performs feature extraction, template matching, score computation, and threshold centering on ciphertexts at the server. This extends protection from extracted features to preprocessed EEG data and removes the client-side plaintext-feature interface exploited by the attack. For efficient encrypted authentication, we develop Multi-Window Topology-Aware Encoding (MWTE) and a Topographic Branch Model with Linear Fusion (TopoFuse-MLP) to preserve EEG spatial information while limiting multiplicative depth. Query-Patch Coordinate Packing (QPCP) and Lane-Preserving BSGS Evaluation (LP-BSGS) further reduce ciphertext operations. Experiments on HGD and BCICIV-2a show high authentication accuracy, with homomorphic computation taking 1-2 s on CPUs and about 14 ms on GPUs. TopoCryptoEEG achieves over 18x average speedup over the EER (IMWUT 2025) baseline, supporting practical privacy-preserving brainprint authentication.

---


### 90. [SceneMemBench: A Benchmark for Scene Memory in Interactive Video World Models](https://arxiv.org/abs/2611.31803)

**<font color=#1a73e8>作者：</font>** Yuheng Si, Linye Lyu, Jiawei Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video world models generate navigable worlds frame by frame, but a persistent world requires previously observed scenes to remain recoverable as users move away and return. Existing memory evaluations, however, often focus on seen-view revisits and full rollouts, leaving cross-view scene recovery underexplored while entangling memory with trajectory-following errors and accumulated generation degradation. We introduce SceneMemBench, a benchmark for scene memory in interactive video world models. It evaluates two complementary dimensions: seen-view recall versus novel-view recovery, and controlled diagnosis versus end-to-end interaction. We introduce Continued Rollout from a shared ground-truth observation history, alongside Full Rollout over complete model-generated interactions. SceneMemBench contains 600 controlled trajectories across 33 Unreal Engine scenes and 60 Full Rollout cases, covering eight representative open- and closed-source models. We evaluate scene recovery along subject consistency, appearance fidelity, and geometric consistency. Results show that novel-view recovery is generally more challenging than seen-view recall, while model profiles under controlled histories can differ markedly from those observed in full interaction. Together, these findings reveal complementary failure modes obscured by seen-view revisits or end-to-end rollouts alone.

---


### 91. [Generalizable Feed-Forward 3D Hand-Object Reconstruction with Coarse-to-Fine Contact Estimation](https://arxiv.org/abs/2611.31812)

**<font color=#1a73e8>作者：</font>** Seonghwan Park, Yong-Hoon Kwon, Min-Gyu Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing the 3D poses of hands and objects from a single image, together with the contact between them, is fundamental to understanding manipulation. To be practical, the reconstruction must generalize to unseen objects, and the contact must be localized precisely. Yet joint feed-forward estimators often rely on predefined object sets, while contact is typically predicted from image features alone, without the explicit geometry needed to localize it. To address both limitations, we present HORCRUX, a unified feed-forward transformer with coarse-to-fine contact estimation. For unseen objects, a frozen foundation model encodes the object from a given or image-reconstructed mesh rather than from object-specific knowledge. A shared transformer then reasons jointly over the object and one or two hands to keep them aligned. For precise contact, coarse per-joint predictions from latent features are resolved over finer hand regions using the reconstructed geometry. Across seven benchmarks, HORCRUX achieves state-of-the-art object and hand pose accuracy among joint estimators and outperforms a dedicated contact estimator in fine-grained contact. These results suggest that contact is best estimated jointly with reconstruction, whose geometry directly localizes it.

---


### 92. [Compressible Representations: Functional Spines in Deep Neural Networks](https://arxiv.org/abs/2611.31817)

**<font color=#1a73e8>作者：</font>** Niranjan Rajesh, Meenakshi Khosla  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep networks embed inputs in high-dimensional representations, but how much of this capacity actually drives behavior? We introduce a framework for identifying, at each layer, the subspace of the representation that is functionally sensitive to the task. Using a matrix analogous to the Fisher information but defined over the hidden representation, we rank directions by their influence on downstream computation and project onto the most task-sensitive subspace. Across pretrained vision networks, representations are remarkably compressible: a small fraction of the task-sensitive subspace preserves most performance, often requiring far fewer dimensions than geometric alternatives. We find that this compressed representation is also more robust to adversarial attacks generated on the full network. We additionally show that this decomposition recovers functionally distinct subspaces within the same representation: on cue-conflict stimuli, shape-sensitive and texture-sensitive directions are largely non-overlapping, and ablating one selectively impairs the corresponding task while leaving the other intact. Task-sensitive subspaces also provide a principled foundation for continual learning: constraining gradient updates to lie orthogonal to the task-sensitive subspaces of prior tasks outperforms standard variance-based gradient projection methods. Finally, restricting representational comparisons to task-sensitive subspaces reveals that inter-model alignment is higher in task-sensitive directions than in task-insensitive directions at later layers, and that conditioning on different tasks over the same stimuli uncovers asymmetries that full-space similarity measures cannot detect. Together, these results establish that deep networks compute through a low-dimensional functional spine embedded within a much larger representational space.

---


### 93. [Gaze World Model](https://arxiv.org/abs/2611.31836)

**<font color=#1a73e8>作者：</font>** Jiawen Zhang, Houze Yang, Xu Cao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Where a person looks indicates their focus of attention, and how their gaze shifts between targets reveals how that attention responds to a changing scene. Existing gaze target estimation methods largely operate frame by frame and do not model these shifts. Gaze shifts are often driven by dynamic changes in the scene, which is the kind of information world models are designed to encode. This relationship is subtle, however, since an event far across the frame may produce only a slight movement of the person's head or eyes. We therefore introduce the Gaze World Model (GWM), which co-trains latent scene prediction with person-conditioned gaze supervision on a frozen V-JEPA 2.1 encoder; in our ablations, the latent prediction objective improves both shift detection and gaze localization. Given a video clip and the person's head box, GWM estimates gaze locations and detects gaze shifts in the observed clip, and forecasts future gaze and shifts from predicted scene features. To train and evaluate these tasks, we augment VideoAttentionTarget and ChildPlay with event-level gaze-shift annotations. GWM achieves state-of-the-art shift detection on these benchmarks, about 10 points higher in four-class AP than the strongest baseline, while remaining comparable to the strongest image-based models in gaze target estimation, and outperforms the compared baselines on future gaze localization and shift forecasting.

---


### 94. [JECT: Addressing the Context Shortcut in Joint-Embedding Predictive Learning for Chest CT](https://arxiv.org/abs/2611.31849)

**<font color=#1a73e8>作者：</font>** Hanbin Ko, Hong-Jun Choi, Jihun Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive architectures learn by predicting features of masked regions from visible context. In chest computed tomography, the findings that decide a diagnosis, such as a small nodule, are often not predictable from the surrounding anatomy. A hidden finding is then best predicted toward normal anatomy, and the prediction loss stops rewarding the encoder for representing it. We call this the context shortcut. Conditioning the predictor on the radiology report repairs the prediction, but in our setup the encoder gains little over image-only pretraining: the report supplies what the encoder never had to learn. JECT therefore gives the report two roles: a condition for the predictor and, through masked section-text prediction, a target for the encoder, which must predict the report's anatomical sections from the unmasked scan. A hierarchical three-dimensional encoder that predicts at every stage keeps this clinical content at every scale. In ablations, the text target improves classification and localization, while conditioning adds little to the encoder. Trained from scratch on 173k volumes, the recipe reaches the level of current computed tomography foundation models in classification, retrieval and nodule malignancy, and of task-specific models in lung-cancer risk prediction after fine-tuning. Conditioning still matters: its predictor can be reused, with no extra training, to show where a report sentence acts, changing most at the finding the sentence describes. Code and pretrained weights are available.

---


### 95. [Explainable Deep Learning for Malaria Parasite Detection and Species Differentiation in Thick Blood Smear Images: A Pilot Feasibility Study](https://arxiv.org/abs/2611.31855)

**<font color=#1a73e8>作者：</font>** Haimanot Bitew, Ayisheshim Almaw, Habtamu Zegeye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Species-level differentiation of Plasmodium falciparum (PF) and P. vivax (PV) determines treatment, yet deep learning detectors rarely test whether their explanations are reliable. In this pilot feasibility study of TRACE-Mal, a research prototype combining YOLOv8n-seg detection and a six-model soft-voting ensemble, we examined whether agreement among three post-hoc explanation methods (Grad-CAM, LIME and SHAP) is associated with the correctness of species calls. the study analysed 2,847 parasite crops from 250 thick smears within publicly available Lacuna Malaria Datasets. The model achieved an mAP50 score of 0.79 and the ensemble had a macro F1 of 0.84 (PF recall 0.86; PV recall 0.74). Unadjusted analyses of crops revealed that predictions explained by greather than or equal to 2 methods were more accurate (86.2% vs 78.9%; difference 7.3 percentage points; 95% CI 3.5-11.1) compared to those explained by less than 2 methods. As the number of explanatory methods increased so did prediction accuracy (from 73.8% for no methods to 89.5% for all three methods). When performing a cluster-bootstrap analysis of 60 test images, again there was a positive consensus difference (7.3 percentage points; 95% CI 2.9-11.8). Further, incorporating explanation information into a model's prediction confidence enhanced its error differentiation ability (AUROC 0.024; 95% CI 0.008-0.041). PF and PV parasite crops have distinct morphologies. Although based on one unvalidated public data source, these findings demonstrate proof-of-concept and should not be taken as a measure of diagnostic capability.

---


### 96. [Start Where the Data Are: Statistical Priors for One-Step Generation on Manifolds](https://arxiv.org/abs/2611.31856)

**<font color=#1a73e8>作者：</font>** Yuyao Wang, Haoliang Sun, Xiankai Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast generation on manifolds is important for scientific applications such as protein design, yet existing one-step generators often produce spurious samples in low-density gaps between data modes. Our analysis highlights the mismatch between uniform noise and concentrated data, motivating a statistical prior that captures the data's coarse structure. We first estimate this prior by fitting mixtures of tangent-space Gaussians through geometry-aware moment matching. However, independent noise-data pairing can still connect different modes and weaken the benefit of the fitted prior. We therefore introduce posterior coupling, which samples a latent component conditioned on each data point and draws its paired noise from that component. To extend this approach to long torsion-angle chains, where full-covariance mixtures become costly, we use a hidden Markov prior to model sequential dependence with shared parameters. The resulting framework plugs into existing one-step training pipelines while retaining the generator architecture, training objective, and single network evaluation at inference. Experiments on spheres, tori, and SO(3) demonstrate substantial improvements across multiple generators, reducing distributional error by up to $125\times$ and the protein Ramachandran outlier rate from 12.1% to 0.55%.

---


### 97. [The Oracle Is Not Enough: Secure Settlement for Prediction Markets](https://arxiv.org/abs/2611.31866)

**<font color=#1a73e8>作者：</font>** Jiayu Liu, Sen Yang, Xueyuan Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prediction markets are becoming an important mechanism for aggregating information and forecasting uncertain real-world events. As they grow in scale and value, reliable settlement becomes critical because settlement determines the winning outcome and allocation of market collateral. Yet many heterogeneous markets require market-specific evidence and interpretation, and incorrect settlement can create direct financial incentives for manipulation. In this paper, we ask how to settle heterogeneous markets correctly and efficiently at scale. We first compare existing settlement designs in their support for heterogeneous markets, reliance on direct operator intervention, and resistance to manipulation, motivating a layered architecture that combines incentivized crowdsourcing with stake-backed voting and selective post-settlement review.
Building on this architecture, we develop a stake-backed settlement protocol that provides economic security and settlement liveness under market-specific verification costs. Specifically, we prove that manipulation is unprofitable for every settled market and give two constructions that support sufficient self-enforcing participation with controlled reward expenditure. Using historical Polymarket and UMA data, we evaluate the protocol under real-world conditions. We find that 99% of admitted markets can be settled with modest participation rewards even under high verification costs.

---


### 98. [RepoEviAgent: Scalable Synthesis of Evidence-Grounded Repository-Level Question Answering Tasks](https://arxiv.org/abs/2611.31873)

**<font color=#1a73e8>作者：</font>** Aoqi Hu, Yueao Xing  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world software engineering (SWE) tasks require agents to understand repository structures, cross-module dependencies, and runtime behaviors, posing significant challenges for constructing high-quality training and evaluation data. To address this, we propose RepoEviAgent, a scalable SWE data construction framework that integrates quality-aware data curation and role-specialized multi-agent task synthesis. Starting from 8,477 open-source repositories and approximately 2.48 million pull request records, we employ semantic alignment, complexity constraints, and multidimensional quality assessment to identify valuable SWE data. We further develop a sandbox-based multi-agent framework that integrates automated environment construction, execution validation, repository exploration, and evidence-grounded Q&A synthesis. Based on this framework, we construct RepoEviQA, a benchmark for Repository-Level Evidence-Grounded Question Answering, comprising 334 tasks across five programming languages and diverse SWE categories, with rigorous rubric-based evaluation. We evaluate five frontier coding models on RepoEviQA, revealing substantial performance differences across task categories and programming languages.

---


### 99. [EEG-Jev: A Unified Single-Pass Decision Model for EEG](https://arxiv.org/abs/2611.31875)

**<font color=#1a73e8>作者：</font>** Zhifei Zhu, Hongtao Zhang, Yu Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG analysis spans choosing alternatives, judging statements, and rating ordered attributes, requiring calibratable probabilities with explicit meaning. We present EEG-Jev, a unified single-pass decision model for EEG. Given an EEG window, a question and an answer specification, one forward pass returns a typed readout: CHOICE gives a candidate distribution, NOUL a proposition probability, and SCORE an ordered-level distribution and expectation. One checkpoint is trained jointly and evaluated once on held-out splits of 35 public sources. Core raw outputs reach 54.08% balanced accuracy on Stieger2021 motor imagery, 70.45% on Sleep-EDF-SC sleep staging, 72.11% per window at threshold 0.5 on CHB-MIT seizure detection with 0.825 AUROC, and 1.700 MAE on 0-10 ds005292 pain ratings. Prior correction and temperature scaling lower negative log-likelihood from 0.766 to 0.606 on Sleep-EDF-SC and 0.166 to 0.019 on CHB-MIT, while direct readout cuts batch-1 latency from 122.43 to 63.11 ms (1.94-fold) against a matched-backbone generative comparator. Interactive demonstration and aggregate results: this https URL.

---


### 100. [Don't Miss the Forest for the Trees: Zero-Shot Skeleton Action Recognition with Hyperbolic Hierarchical Semantic Prototypes](https://arxiv.org/abs/2611.31877)

**<font color=#1a73e8>作者：</font>** Zixiao Jin, Siyu Zhu, Feng Ding 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot skeleton-based action recognition is evaluated almost exclusively on flat leaf labels, which leaves open whether a representation also grounds the broader concepts that contain an action in skeleton motion. We find that strong leaf alignment does not carry over to them: when ancestor concepts are scored directly under independent decoding, eight flat methods with 57.86-73.29% mean leaf Top-1 reach only 6.15-31.21% mean full-path accuracy across four NTU RGB+D splits. We propose the Hyperbolic Hierarchical Semantic Prototype ($H^2SP$) framework, which represents every node of an action taxonomy in the Lorentz model of hyperbolic space. First, instead of learning a free vector per node, $H^2SP$ synthesizes hierarchy-aware prototypes by recursive parent-child geodesic interpolation under a single tree-wide gate. Second, tangent-space semantic and distributional alignment on seen classes anchor the leaf prototypes in skeleton motion. Third, a soft entailment-cone regularizer encourages directional parent-child inclusion, propagating this motion grounding to ancestor concepts. We evaluate hierarchical concept prediction under independent and cascade decoding, and transfer to an alternative taxonomy without retraining. Across the four splits, $H^2SP$ attains the best mean independent and cascade full-path accuracy among the evaluated methods, at a comparable leaf Top-1 of 72.40%. Transferred to the alternative taxonomy, it outperforms both flat baselines and the same-tree Euclidean control across every split and decoding mode, indicating that its concept-level correspondence extends beyond the training taxonomy.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-342](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

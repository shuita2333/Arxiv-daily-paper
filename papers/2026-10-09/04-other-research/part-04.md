# 📦 其他研究 | 2026年10月09日

> 本类共 **324** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-324](./part-07.md)

---

### 151. [Identity-Duplication Auditing in National-Scale Neuroimaging Repositories](https://arxiv.org/abs/2610.09614)

**<font color=#1a73e8>作者：</font>** Jiheng Li, Michael E. Kim, Trent M. Schwartz 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> National-scale magnetic resonance imaging (MRI) repositories increasingly integrate data from different studies and institutions. However, subject identifiers that are valid only within individual datasets are no longer guaranteed to remain globally unique after aggregation, making it possible for the same subject to be assigned multiple identifiers, which we define as identity duplication. Such duplication can create leakage between training and test data and inflate apparent performance in downstream biomedical studies. Existing methods do not provide an end-to-end, image-based workflow for auditing this problem at repository scale. In this work, we present HAPPEN, a human-in-the-loop pipeline for auditing identity duplication in T1-weighted brain MRI repositories. It combines SHA-256 fingerprinting for exact-duplicate detection with supervised contrastive retrieval of non-identical scans that may originate from the same person. Retrieved pairs are reviewed as candidates in a locally hosted interface rather than automatically classified as duplicates. We deployed the workflow in a 95,129-scan aggregated repository and assessed end-to-end recovery using 54 genetic-reference pairs. Transferability was assessed by locally deploying the same workflow on 22,386 scans at an independent institution without model retraining or image transfer. Deployment in the study repository identified 1,316 exact-duplicate scan groups and 1,275 reviewer-supported near-duplicate subject groups. Of these groups, 56% and 82%, respectively, crossed dataset boundaries. All 54 genetic-reference pairs were recovered. The external team independently completed the full workflow using a locally selected operating threshold and review standard.

---


### 152. [The Identifiability and Observability of Deep Normalized Attention](https://arxiv.org/abs/2610.09620)

**<font color=#1a73e8>作者：</font>** Pranav Venkata Konda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study which parameters of deep, unmasked, single-head attention are determined by its input--output function. For known positive nonconstant real-analytic normalizers, the function generically determines the effective scores and combined value map up to the signs induced by even normalizers. This proves the real-analytic case of a conjecture of Henry--Marchetti--Kohn, including softmax. We then classify exceptional fibers under explicit normalizer conditions, identifying when collapse makes later scores unobservable, and establish sharp Taylor orders for local identification. Near simultaneous query/key collapse, we compute the complete native Jacobian decay spectrum on separating finite input banks. For common first nonconstant normalizer degree $k$, layer $i$ has contact order $2k3^{i-1}-1$, with exact multiplicities and kernel dimension. High-precision and automatic differentiation calculations illustrate the resulting loss of numerical sensitivity.

---


### 153. [When does a network's training history predict its future learning better than its current state? Evidence from a response probe and a forecasting screen](https://arxiv.org/abs/2610.09621)

**<font color=#1a73e8>作者：</font>** Martin Hofmann, Patrick Mäder  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Networks that behave alike now can still learn differently when training continues. Work on loss of plasticity and critical periods shows that the path to a state shapes what follows; it does not show whether the path carries information that a measurement of the state itself misses. We ask when the training history of a network predicts its future learning better than its current state. In a main study, small multilayer perceptrons were trained under three history regimes (42 histories), and future learning was measured at four checkpoints by a short probe: a copy of the network trained for 100 updates on a new task. Before the prediction result was read, the protocol checked the probe. It responded monotonically to a function-preserving rescaling of hidden units, repeated measurements agreed (intraclass correlation 0.940, [0.903, 0.997], in the least reliable class, mean of three repeats), and a re-initialisation of units was visible directly after it but not 100 to 200 updates later. A history state of at most four dimensions did not improve on a calibrated model of the current state (gain -21.4%, 90% interval [-91.9, 8.1]; required in advance: 10%). A companion screen on 1,560 synthetic regression runs asked the same question for a target further away, the final error of the run. There, history models forecast better than the current validation error after 12 of up to 240 epochs (compact state 30.3%, [15.8, 39.4], a contextual comparison) and were not distinguishable from it after 48. In both studies the history was informative only while the current state was not yet informative about the target; this reading was formed after the results.

---


### 154. [Closed-Form Noise Calibration Against Membership Inference for Random-Allocation DP-SGD](https://arxiv.org/abs/2610.09651)

**<font color=#1a73e8>作者：</font>** Murat Bilgehan Ertan, Marten van Dijk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> DP-SGD protects training data by adding Gaussian noise to clipped gradients. The amount of noise is usually chosen by running a numerical privacy accountant inside a search. We study DP-SGD with random allocation, where each epoch uses every record once, at a randomly chosen step. For this setting we give a one-line formula that bounds the accuracy of every membership inference attack (MIA) on the trained model. With $M$ steps per epoch, $E$ epochs and noise multiplier $\sigma$, and with membership and non-membership equally likely a priori, the attack accuracy is at most $\frac12+\frac14\sqrt{(1+(e^{1/\sigma^2}-1)/M)^E-1}$. The formula comes from the chi-square divergence between a Gaussian distribution and a Gaussian mixture that dominates random allocation. It is interpretable and gives $\sigma$ in about a microsecond. Where applicable, our formula needs at most about half the noise of the state-of-the-art closed-form bound. To measure how close the bound is, we also derive an exact expression for the attack accuracy of these two distributions and evaluate it numerically. Calibrating to this exact expression requires $13.0\%$ to $20.2\%$ less noise than the formula in our main experiments, and since it is exact, no accountant that knows only $M$, $E$ and $\sigma$ can certify a smaller $\sigma$. In training, the resulting $\sigma$ outperforms the formula and matches a published accountant in test accuracy. It is found in seconds and certified in minutes, whereas every search we ran with that accountant took longer or returned at least $0.62\%$ more noise. We show that MIAs on the trained models stay below the bound.

---


### 155. [MeshSIPP: Efficient Lattice Planning in Dynamic Environment](https://arxiv.org/abs/2610.09652)

**<font color=#1a73e8>作者：</font>** Marat Agranovskiy, Konstantin Yakovlev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous navigation in dynamic environments requires computing spatiotemporal trajectories that satisfy non-holonomic motion constraints. When the trajectories of the moving obstacles are predictable or known, a promising approach is to rely on the combination of state lattices constructed from precomputed feasible motion primitives and Safe Interval Path Planning -- a search-based algorithm with strong theoretical guarantees. While this approach yields feasible paths, the rich primitive sets needed for smooth navigation induce a large branching factor, which becomes costly when coupled with time-dependent obstacle intervals. To this end, we present MeshSIPP, an efficient planner that removes the computational bottleneck by exploiting the fact that many primitives sweep the same regions and can therefore be validated together. MeshSIPP propagates primitives as spatial bundles, screens them with lightweight bounding-interval checks, and defers the expensive exact departure-time search until a primitive reaches its terminal state. A time-aware pruning rule additionally discards redundant space-time branches early in the search. We prove that the resulting search is complete and optimal. Extensive experiments over more than 6,000 benchmark instances and real-time ROS~2 simulations show that MeshSIPP achieves up to a 3$\times$ speedup over state-of-the-art spatiotemporal planners.

---


### 156. [DSTNet: Dynamic Spectral Trajectory Network for Causal Multi-Horizon Financial Forecasting](https://arxiv.org/abs/2610.09654)

**<font color=#1a73e8>作者：</font>** Aashish Bohra, Lokendra Vishwakarm  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wavelet-based financial forecasters typically use the transform only to denoise, or reduce it to a single spectral snapshot at the forecast origin, and the convolution that produces the coefficients is usually bilateral, so it can read past the forecast origin. DSTNet instead retains the recent evolution of filter-bank magnitudes as a causal Dynamic Spectral Trajectory, built from seven trailing technical indicators over a twenty-day lookback with a one-sided Morlet-derived filter bank and an explicit burn-in for the left-boundary transient. A factorized Scale-Temporal Spectral Transformer attends along the time and filter-bank axes separately, a learned gate fuses the spectral branch with a CNN-BiLSTM, and horizon-specific gates emit one, three, five, and ten day forecasts in a single pass. We evaluate seven equity indices and gold under a common expanding-window protocol and an untouched one-year hold-out, against nine learned baselines and a random-walk persistence benchmark. Under MAE and MAPE, persistence is the strongest of the ten fixed competitors in 29 of the 32 series-horizon cells and DSTNet is the only model below it in every cell, by 0.7 to 0.9 percent at one day and 3.4 to 4.5 percent at ten days. At one day, paired testing favours DSTNet against the weaker learned baselines but is inconclusive against persistence and the strongest learned forecasters. A downstream allocation diagnostic does not support an equity-timing advantage on any of the seven indices.

---


### 157. [Quasi-Binarized Autoencoders: An Architecture-Independent Information Bottleneck for Medical Image Anomaly Detection](https://arxiv.org/abs/2610.09670)

**<font color=#1a73e8>作者：</font>** Shouhei Hanaoka, Takahiro Nakao, Atsushi Takamatsu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised anomaly detection, which learns only from normal images, is a central task in medical image analysis and remains an open problem. Reconstruction-based methods pass an image through an encoder-decoder network trained on normal data and detect anomalies from the residual between the image and its reconstruction. This works only if the information passed from the encoder to the decoder is limited; otherwise the network learns an identity mapping and reconstructs anomalies too. This limit is usually imposed through architectural choices, tuned per dataset, that cannot be stated in bits. We introduce the quasi-binarizing (QB) layer, which squashes each latent element into [0, 1] and adds Laplace noise of scale 1/epsilon. Each element is then epsilon-locally differentially private, and the mutual information between an image and its reconstruction is bounded by a quantity that depends only on epsilon and the number of QB elements, whatever the encoder and decoder. Placing a QB layer on every encoder-decoder path, including all skip connections, we build QBAE, a seven-level attention U-Net with 32,768 QB elements. On the seven datasets of the MedIAnomaly benchmark, QBAE with one architecture and one configuration reaches a mean image-level AUROC of 0.828, the highest among methods that do not adapt to each dataset, and the best reported results on BraTS2021 (AUROC 0.911, pixel-level AP 0.838). The noise is kept at test time, so that every reconstruction satisfies the bound. Without input corruption, the bottleneck alone prevents identity collapse (mean AUROC 0.805 vs. 0.590). Code is available at this https URL.

---


### 158. [Gauss-Newton Accuracy and Indefinite Hessians: Uniform Coexistence in Low-Cost Sets](https://arxiv.org/abs/2610.09675)

**<font color=#1a73e8>作者：</font>** Kihun Rhee, Hanjoon Byun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the accuracy of Gauss-Newton curvature in ridge-regularized nonlinear least squares. Under local regularity and persistence of level-set curvature magnitude along an exact-fit section, we prove uniform coexistence of two curvature regimes. Global minimizers exist, and every global minimizer has relative Hessian error below $(1+\sqrt2)/8$, while the same low-cost set contains a point with an indefinite Hessian and relative error at least $15/8$. One positive ridge cap works for all independent center and label perturbations in fixed neighborhoods and every positive ridge weight up to the cap. These neighborhoods do not shrink as the ridge weight tends to zero. A pointwise certificate based on the current prediction level set controls the normal, mixed, and tangent parts of the Hessian correction. We prove a sharp relative-error bound over the stated pointwise class when the prediction map and ridge vary. Analytic examples describe the roles of output alignment, curvature orientation, and persistence. A separate structural result gives full Jacobian row rank throughout low-cost sets and exact interpolation near a rank-deficient reference.

---


### 159. [A Multi-Source Ultrasound Benchmark Revealing the Limits of Contemporary Self-Supervised Anomaly Detection Methods](https://arxiv.org/abs/2610.09677)

**<font color=#1a73e8>作者：</font>** Marco Riedenauer, Daniel Kienzle, Pratik Mayekar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised anomaly detection is a promising paradigm for medical ultrasound, as normal images are often easier to obtain than exhaustive annotations of all possible pathologies. However, most existing evaluations are limited to a single anatomy or task, making it unclear whether models learn a robust notion of normal ultrasound appearance or only a source-specific representation. We introduce the SADUSI benchmark, a multi-source ultrasound dataset designed to train and evaluate anomaly detection methods across a broad range of anatomical regions, views, and acquisition protocols. The goal of SADUSI is to provide a diverse normal ultrasound distribution and a benchmark for visible structural anomalies that can be assessed from single images. We evaluate representative self-supervised anomaly detection methods and find that current approaches struggle in this setting. In particular, reconstruction-based diffusion methods such as AnoDDPM and DeCo-Diff achieve pixel-level AUROC values of 0.56-0.72 and maximum F1 scores of 0.10-0.26, indicating limited separation of pathology from normal image regions. Feature-based PatchCore variants perform better, reaching pixel-level AUROC values of 0.76-0.83, but remain limited with maximum F1 scores of 0.14-0.40. These findings suggest that broad multi-source ultrasound anomaly detection remains an open challenge and that SADUSI can serve as a resource for developing methods that generalize beyond anatomy-specific settings.

---


### 160. [CERO: Where and When to Allocate Rollouts for RL Post-Training](https://arxiv.org/abs/2610.09679)

**<font color=#1a73e8>作者：</font>** Yiming Zong, Yige Wang, Xing Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive rollout methods for group-relative reinforcement learning typically allocate a fixed per-update budget across prompts. We instead study how to coordinate a finite rollout budget over the entire training horizon. We formulate this problem using a concave surrogate utility of cumulative prompt exposure and introduce CERO, an online primal dual scheduler for prompt admission and budget pacing. In our experiments, each admitted prompt receives a fixed-size response group. CERO instead adapts which prompts are selected, how often they are revisited across rounds, and how many groups are generated in each round. A compact Fenchel representation linearizes the dependence on cumulative exposure, while projected online gradient descent updates prompt-specific supporting slopes and a shared budget price using reward-variation feedback and budget deviations. We establish pathwise guarantees for the surrogate allocation objective against fixed-rate and same-path time-varying benchmarks, with explicit terms for proxy discrepancy and rate variation. Under matched training-response budgets, CERO attains the highest avg@16 macro-average on each of three backbones across five mathematical reasoning benchmarks. Mechanistic analyses link CERO's prompt choices to within-group reward contrast, while multi-seed ablations show gains from adaptive pacing over both uniform and preset spending schedules.

---


### 161. [Few-Shot Learning for Personalised Automated Pain Assessment](https://arxiv.org/abs/2610.09692)

**<font color=#1a73e8>作者：</font>** Heinke Hihn, Ibrahim Eisawy, Patrick Thiam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pain perception varies substantially across individuals, making it difficult for population-based classifiers to generalise across all subjects in a dataset. One way to account for subject variability is to train personalised classifiers. In this work, we evaluate Few-Shot Learning, a sub-area of Meta-Learning, as an approach to personalisation in automated pain assessment. We re-interpret the shift from population-level to subject-level evaluation as a task-domain shift, where the observed classes remain fixed but the target subject changes. We evaluate our method on the BioVid Pain Database, the SenseEmotion Database, and the PainMonit Experimental Dataset (PMED), reaching 85.75% and 35.49% accuracy on BioVid and 82.37% and 41.88% on SenseEmotion in the binary and multi-class settings under a Leave-One-Subject-Out CV protocol respectively, and 90.47% on PMED, for which only a binary benchmark exists. Using samples to implement k-shot conditioning, the accuracies can be improved to 86.25%, 40.06%, 83.43%, 44.08%, and 91.25%, respectively. To further evaluate the effects and robustness of our method, we provide additional ablation experiments and investigate the personalisation effects. Our results suggest that support-conditioned few-shot adaptation can improve average performance under inter-subject variability.

---


### 162. [Automotive Hardware Attacks: An Architect's Guide to TARA](https://arxiv.org/abs/2610.09697)

**<font color=#1a73e8>作者：</font>** Jakub Breier, Xiaolu Hou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Threat analysis and risk assessment (TARA) according to ISO/SAE 21434 treats implementation-level hardware attacks inconsistently. We show that two of the three attack-feasibility approaches exemplified in the standard rate every attack path that requires physical access as very low by construction, independent of the implementation, while the third can assign the same path any of the four ratings, depending on the assumed state of attacker knowledge and on the attacker profile. This paper presents a hardware-aware extension of the TARA that covers side-channel analysis (SCA), fault-injection attacks (FIA), and abuse of debug and test interfaces. It adds an attacker model for physical access over the vehicle lifecycle; a path-dominance relation on the attack-potential factors that identifies when a simpler path makes a sophisticated one irrelevant; a three-level hardware relevance gate (H0 to H2) with an explicit decision rule that fixes whether resistance of a hardware step may be argued, must be documented, or must be demonstrated by test; and a rating rule under which a hardware step receives no credit for implementation-specific resistance until the required evidence exists. The gate is positioned relative to cybersecurity assurance levels and targeted attack feasibility. The method is applied to a reference gateway architecture, and its structural inputs are examined on ten published attacks on automotive components. In seven of the ten studies, the demonstrated attack included a debug, programming, boot, diagnostic, or update mechanism, whereas only four studies included an attack on a cryptographic computation.

---


### 163. [What Makes Synthetic Hard Negatives Work in Vision-Language Pretraining?](https://arxiv.org/abs/2610.09700)

**<font color=#1a73e8>作者：</font>** Nikos Giakoumoglou, Paschalis Giakoumoglou, Andreas Floros 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic hard negatives generated in the representation space have proven effective for unimodal self-supervised learning, but transferring this idea to vision-language pretraining is not straightforward. We analyze six representation-space synthesis strategies and identify two failure modes in their transfer to vision-language pretraining: cross-modal constructions that produce overly easy negatives or pull them toward the query, and intra-modal constructions that incorporate the matched positive. We also observe logit-scale saturation when training with synthetic hard negatives and a learnable temperature, and find that fixing the temperature improves downstream performance. Using this geometric analysis we propose SNAP, which generates intra-modal hard negatives that never involve the positive from either modality, avoiding both failure modes entirely. SNAP is model-agnostic, requires no external generative models, and adds less than 10% training time overhead. Evaluated on top of CLIP and FLIP across multiple architectures and datasets, SNAP delivers consistent improvements on zero-shot retrieval, zero-shot classification, and linear probe evaluation.

---


### 164. [Latent Watermarks under Generative Editing: A Benchmark and Analysis of Detection Survival](https://arxiv.org/abs/2610.09702)

**<font color=#1a73e8>作者：</font>** Sung Ju Lee, Nam Ik Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ordinary prompt-based editing can cause latent watermark detection to fail without explicitly targeting the watermark. We benchmark eight watermark methods against five editors across four generative backbones, four editing strengths, and five semantic categories, with edit-validity and threshold checks. Separating editing from seven subsequent distortions reveals that editing alone primarily distinguishes Tree-Ring, while added distortions expose a broader spectrum of detection survival. Sequential edits reveal a second hidden difference: score separation can decline while detection rates remain near their ceiling. Across methods, standardized clean score separation ($d'$) organizes composite-survival tiers, whereas spatial overlap adds little to predicting edit-only survival beyond clean detectability. Embedding-strength interventions in two methods link higher clean separation to higher post-edit separation. In HSTR, the margin contrast is positive, while the angular layout contrast at matched clean separation remains unresolved. Together, outcome decomposition and continuous separation expose differences hidden by aggregate TPR. Method tiers are stable under threshold recalibration at the main operating points and alternative composite weights. Clean $d'$ is thus a useful empirical diagnostic within this benchmark, with mixed transfer to unseen methods. Code and supporting artifacts are planned for a separate release.

---


### 165. [Enhancing Multi-Region Stylization with Interior-Guided Boundary Repair](https://arxiv.org/abs/2610.09706)

**<font color=#1a73e8>作者：</font>** Hong-Son Nguyen, Thi-Ngoc-Hanh Le  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Region-based neural style transfer enables fine-grained artistic control by allowing independent stylization of semantic image regions. However, compositing these regions often leads to boundary artifacts, degrading visual quality. We propose Interior-Guided Boundary Repair (IGBR), a lightweight and model-agnostic method that improves boundary handling in multi-region stylization. IGBR repairs boundary pixels using interior-guided propagation and applies inward, distance-based blending restricted to object-background boundaries, preventing inter-object style leakage. The method is derived from a region-wise constrained formulation with a closed-form solution and can be seamlessly integrated into existing stylization pipelines without retraining. To evaluate efficiency of our IGBR, we introduce quantitative metrics that measure boundary consistency, gradient artifacts, inter-object leakage, and interior preservation without requiring annotated stylized images. Our experiments and evaluations demonstrate that the proposed IGBR consistently produces plausible boundaries, outperforming prior blending techniques in boundary consistency, gradient stability, and interior preservation. The code is available at this https URL.

---


### 166. [EC-EarthFlow: Probabilistic emulation of daily transient global climate model simulations with flow matching](https://arxiv.org/abs/2610.09715)

**<font color=#1a73e8>作者：</font>** Kirien Whan, Nikolaj T. Mücke, Karin van der Wiel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce EC-EarthFlow, a generative flow matching model that emulates simulations from the physical climate model EC-Earth3. The model is trained on transient simulations from EC-Earth3 (1950-2166, SSP2-4.5) to predict the day ahead temperature field from the previous days temperature as well as annual mean temperature. Predictions are made auto-regressively with rollout periods of between a month and an extended season. Using only this variable of interest, we are able to reproduce the daily variability, spatial patterns, annual cycle and long-term trend from EC-Earth3 at a substantially lower computational cost than the physical model. We demonstrate that EC-EarthFlow is stable for long inference periods, and that it can learn the physical relationships as simulated in EC-Earth3.

---


### 167. [DynStream: Online Streaming 4D Gaussian Reconstruction of Dynamic Worlds from Unposed Video](https://arxiv.org/abs/2610.09720)

**<font color=#1a73e8>作者：</font>** Dingwei Xian, Xiaoyu Zhou, Yajiao Xiong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online reconstruction of dynamic 4D scenes from long, unposed streaming videos requires both continuous processing and photorealistic rendering, which existing methods struggle to achieve simultaneously. Existing feed-forward Gaussian methods are restricted to offline processing, whereas online point-cloud approaches struggle to maintain dense geometry and high-fidelity rendering. We present DynStream, a framework for streaming 4D Gaussian reconstruction from long, unposed videos. Given a continuous video stream, DynStream reconstructs the scene within local temporal windows and incrementally aligns and fuses these local reconstructions into a globally consistent scene, enabling online 4D reconstruction without per-scene optimization. By jointly enforcing cross-window geometric consistency and modeling time-varying scene content, DynStream supports efficient reconstruction and photorealistic rendering over extended video streams. Experiments demonstrate that DynStream enables high-fidelity online dynamic reconstruction and rendering from long video streams, achieving state-of-the-art performance across diverse dynamic indoor and outdoor scenes.

---


### 168. [MeshCarve: Artisan Mesh Generation with Flow Matching in Compact Latent Spaces](https://arxiv.org/abs/2610.09723)

**<font color=#1a73e8>作者：</font>** Xiyu Wang, Ruocheng Wu, Yufei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prior artisan mesh generation works largely predict face tokens autoregressively, which makes inference slow. Recent methods instead flow match continuous latents built by Variational AutoEncoders (VAEs), but reconstruction quality drops significantly when geometry and topology are jointly encoded, and further when the latent space is compressed. We present MeshCarve, a flow matching method that generates entirely in compact latent spaces, generating vertex positions and edge connections separately and sidestepping the difficulty of a joint compact latent. To shorten the token sequence, we propose a hierarchical sparse transformer backbone, instantiated as VertexVAE and EdgeVAE. Instead of encoding fields over the surface voxels, both VAEs anchor on discrete vertices in their latent spaces, which drastically reduces the token sequence length, and our spatial-aware compression shortens it further without costing reconstruction. VertexVAE directly encodes vertex occupancy. For connectivity, we propose vertex-link encoding, which turns arbitrary connectivity between vertices into fixed-length continuous per-vertex embeddings and recovers complex artistic topology faithfully. MeshCarve combines these VAEs with an anchor generator and flow matches on the shortened token sequences. It shows advantages over state-of-the-art autoregressive and flow matching methods on Objaverse and generalizes to Toys4K. To the best of our knowledge, it is among the first artisan mesh generation methods whose every generative stage runs in a spatially compressed latent, with a token sequence only a fraction of the most compressed previous autoregressive and flow matching works.

---


### 169. [Beyond Group Splits: Specimen-Level Cross-Validation and Visual Attribution for Remaining-Shelf-Life Regression in Climacteric Fruit](https://arxiv.org/abs/2610.09726)

**<font color=#1a73e8>作者：</font>** Rovhona Mudau, Jean Frederic Isingizwe Nturambirwe, Clement Nthambazale Nyirenda  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating remaining shelf life (RSL) from images could provide affordable decision support for perishable produce, but evaluation protocols can substantially affect reported performance when repeated images are available from the same biological specimen. We use the Hass Avocado Ripening dataset, comprising 8,834 image-RSL pairs from 426 fruits across three storage regimes, to evaluate a frozen ImageNet-pretrained visual backbone with a lightweight regression head. Our contributions are threefold: we quantify the effect of observation-level versus specimen-disjoint evaluation, compare lightweight and heavier visual backbones under specimen-disjoint cross-validation, and examine their spatial attributions using Grad-CAM. Across ten observation-level random splits, the model achieves a mean RMSE of 2.37 days with a standard deviation of 0.03 days, whereas specimen-disjoint 5-fold cross-validation yields a mean RMSE of 3.12 days with a standard deviation of 0.11 days. The corresponding mean coefficient of determination is 0.553. A matched per-specimen comparison confirms higher error under specimen-disjoint evaluation, with a probability value below 0.001 across 426 specimens, showing that observation-level partitioning gives a substantially more optimistic estimate for this dataset and model configuration. Under specimen-disjoint evaluation, MobileNetV3-Small (0.93 million parameters) achieves accuracy comparable to ResNet-18 while providing substantially higher throughput, and Grad-CAM reveals differences in spatial attribution between the lightweight backbones. These results support specimen-disjoint evaluation and attribution analysis when assessing lightweight vision models for longitudinal shelf-life prediction.

---


### 170. [Trust a Few: The Weakest Assumptions a Protocol Needs](https://arxiv.org/abs/2610.09730)

**<font color=#1a73e8>作者：</font>** Bhumika Mittal, Aalok Thakkar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Protocol verifiers check whether a protocol meets a security goal under stated trust assumptions, such as that a key is never leaked, a value is fresh, or a channel is authentic. They do not say which of those assumptions the goal needs. Rowe, Guttman and Liskov asked for the weakest assumptions under which a protocol achieves a goal and left the question open. We answer it for assumptions about keys, values and channels. Call a run that violates the goal an attack, and the assumptions that would rule it out its stopping set. The least a protocol must trust to meet a goal is exactly the set of minimal ways to stop all of its minimal attacks. Several such sets may exist. The answer becomes unique once either/or assumptions are allowed, and it is a single set exactly when every minimal attack is stopped by a single assumption. A Galois connection between assumptions and goals explains why: a goal may end in "or", but its hypothesis may not. The same structure gives the trust needed by a conjunction of goals and an exact condition under which composed protocols need no extra trust. To compute the answer, a loop asks a verifier whether a candidate suffices, records what stops each attack it reports, and recomputes the candidates. Deciding whether some trust of at most k assumptions suffices is NP-hard. With a bounded analyser of our own and with CPSA, the loop finds the weakest trust for 18 goals over ten protocols and their variants, and on each it agrees with evaluating every trust using the same verifier. The answers include an assumption that our model of the adopted fix of Kerberos PKINIT states but the client's authentication of the server does not need, and channel assumptions under which Needham-Schroeder meets its goal in a bounded model.

---


### 171. [Healthy skepticism in AI: a data visualization research agenda](https://arxiv.org/abs/2610.09740)

**<font color=#1a73e8>作者：</font>** G. Elisabeta Marai, Marc Baaden, Michael Behrisch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Research in data visualization of artificial intelligence (AI) models has historically focused on enhancing trust through visual explanations of AI. The trustworthiness line of work was built at least partially on an assumption that humans were critical users unlikely to adopt AI technology. It is increasingly clear that human trust levels in AI span, in fact, a wide range from critical to over-reliant. There is an urgent need to support both trust and healthy skepticism in AI solutions. We argue that it is healthy for humans to adopt a skeptical view both on the results of AI models and on the use of such AI models. We share our thoughts on the rising phenomenon of over-reliance on AI models, the risks and opportunities in using AI models, and the role of data visualization in over-reliance situations where humans are not motivated to engage in critical thinking.

---


### 172. [SoccerNet-FoulRet: Retrieving Semantically Similar Soccer Foul Videos](https://arxiv.org/abs/2610.09742)

**<font color=#1a73e8>作者：</font>** Jacobus Arthur, Ahmad Sait, Batool Hani 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Refereeing decisions in professional soccer remain inconsistent because referees cannot easily compare a contentious foul against similar past cases. We cast this as a retrieval problem and introduce SoccerNet-FoulRet, the first benchmark for semantic foul retrieval. Given a query foul, the task is to retrieve past fouls judged to be relevant precedents, regardless of camera angle, teams, or appearance. This differs from prior video-to-video retrieval, which matches clips by visual similarity or a shared event. Here, relevance is defined by refereeing interpretation. We build the benchmark from the SoccerNet-MVFoul dataset and evaluate retrieval ability of zero-shot video and vision-language embedders together with a task-specific fine-tuned baseline on 693 human-verified queries and category-relevance labels. Semantic foul retrieval remains challenging. The strongest zero-shot model achieves under 5% HitRate@10 on human-verified precedents, while category-supervised fine-tuning improves category relevance but transfers only modestly to precedent retrieval. We release SoccerNet-FoulRet to establish semantic foul retrieval as an open problem: this https URL.

---


### 173. [SoftSEEPS improves ML-based precipitation forecasting](https://arxiv.org/abs/2610.09752)

**<font color=#1a73e8>作者：</font>** Jost Arndt, Utku Isil, Noelia Otero 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper we have developed a differentiable approximation of the well-known SEEPS score, which we name SoftSEEPS. This allows the training of a Machine Learning model to forecast precipitation directly. We test SoftSEEPS on the IMERG dataset (0.1 degree resolution) by training a decoder for precipitation on the latent space of a pre-trained low-resolution forecasting model. Combining SoftSEEPS and RMSE in a joint objective is possible with marginal trade-offs in either metric.

---


### 174. [Diffusion-Generated Image Watermarking: A Two-Axis Taxonomy and Three Protocol-Bounded Case Studies](https://arxiv.org/abs/2610.09755)

**<font color=#1a73e8>作者：</font>** Sung Ju Lee, Nam Ik Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Watermarking diffusion-generated images requires balancing provenance signals with image quality, robustness, and computational cost. This work organizes methods along two axes: insertion mechanism and primary signal-bearing representation, and formalizes a representative $z_T$-Fourier pipeline for verification and identification. We then use the taxonomy to structure three protocol-bounded case studies. The first examines associations among frequency integrity, detection, quality, and cropping behavior. The second revisits persistence under seed-linked and seed-independent editing and formulates a scoped Semantic Imprinting Hypothesis without claiming a localized carrier or causal mechanism. The third studies single-shot VAE-latent phase modulation, including its efficiency, regeneration robustness, and robustness--quality operating points. Finally, we separate four content-level attack families from model/pipeline adaptation, propose corresponding evaluation protocols and testable conjectures for parameter-tuning threats, and identify additional temporal extensions for video. These analyses do not establish a universal ranking; instead, they provide a framework for matched, protocol-aware comparisons of watermarking systems for diffusion-generated images.

---


### 175. [PARC-Loc: Text-to-Point-Cloud Localization with Partial Assignment and Relational Consistency](https://arxiv.org/abs/2610.09761)

**<font color=#1a73e8>作者：</font>** Shengkai Ma, Zhenyu Hou, Weihua Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-point-cloud localization estimates a position in a city-scale 3D map from descriptions of surrounding objects. Existing coarse-to-fine methods retrieve submaps using aggregate learned compatibility and then localize within a selected submap. However, repetitive or similar urban objects can inflate the embedding similarity between the query and multiple submaps, even when the instance layout within a submap violates the query description. Meanwhile, query-relevant instances often span submap boundaries, leaving the retrieved submap with incomplete contextual evidence. We term these failure modes layout-inconsistent aliasing and boundary evidence incompleteness, respectively. To address them, we propose PARC-Loc, a coarse-to-fine localization framework built on Partial Assignment with Relational Consistency (PARC). PARC jointly models hint-object compatibility and pairwise spatial relations, allowing unmatched elements while favoring assignments consistent with the queried layout. At the coarse stage, its candidate-level assessment complements neural similarity for layout-consistent submap selection. At the fine stage, the context is expanded with query-relevant instances from adjacent submaps, while PARC yields object-level matching weights that guide cross-modal attention. Extensive experiments on KITTI360Pose and CityLoc show that PARC-Loc outperforms conventional coarse-to-fine baselines. On KITTI360Pose, our method improves Top-1 localization recall at 5 m from 0.50 to 0.67, achieving a 34% relative gain over the strongest baseline.

---


### 176. [Beyond Policy Support: Interaction Constrained Offline Reinforcement Learning for Autonomous Driving](https://arxiv.org/abs/2610.09763)

**<font color=#1a73e8>作者：</font>** Mahmoud Selim, Cristina Cipriani, Karl Henrik Johansson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning enables reward-driven policy improvement from fixed datasets without requiring online exploration, making it particularly attractive in safety-critical domains. A central challenge, however, is distribution shift: policy optimization may favor actions that are weakly supported by the offline data, rendering value estimates unreliable. Existing approaches primarily control this shift in the policy's own action space. In interactive environments such as autonomous driving, this can be insufficient: a candidate ego trajectory may remain well supported under the marginal behavior distribution while being poorly supported jointly with the surrounding-agent behavior observed in the logged interaction. We refer to this degradation in interaction support as \emph{interaction distribution shift} (IDS), and introduce \emph{Interaction-Constrained Drive Policy} (ICDP), an offline reinforcement learning framework that explicitly controls interaction-level distribution shift. Starting from the joint data distribution over ego and surrounding-agent futures, we show that joint-support degradation decomposes exactly into an ego-support component and a residual interaction-support component. We recover the latter through contrastive density-ratio estimation, isolating interaction compatibility without explicit joint-density modeling, surrounding-agent prediction, or rollouts in reactive simulators or learned world models during policy optimization. Closed-loop evaluations on nuPlan, Interplan and real-world truck experiments show that ICDP suppresses high-value yet interaction-unsupported trajectory selections and improves performance in interaction-critical driving scenarios. Project webpage: this https URL

---


### 177. [Faster PMNS Multi-precision Multiplications Using Truncated Montgomery Technique](https://arxiv.org/abs/2610.09767)

**<font color=#1a73e8>作者：</font>** Laurent-Stéphane Didier, Alexy Dutois-Ruiz, Jean-Marc Robert  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Polynomial Modular Number Systems (PMNS) aim to represent elements of fields or rings of large characteristics using polynomials satisfying bounds on some parameters (degree, absolute values of the coefficients). Those PMNS, while some conditions are fulfilled, using convenient parameters and implementation features, allow some speed-ups in cryptographic computations. Recent works (Meloni \emph{et al.} \cite{MeloniPV25}) propose better speed-ups by improving the parameter generation of the system, and by using multi-precision polynomial coefficients, i.e. coefficients stored using several machine words. In this work, we first present PMNS schoolbook software implementation better in some context than the Toeplitz state-of-the-art counterpart of \cite{MeloniPV25}, taking advantage of smaller memory cost by being free to choose a smaller $n$ parameter, minimizing at the same time the complexity of the multiplication. This implementation for 4096 bit modulo size shows element size smaller by 11\% and 20 \% speed-up. We thus present a new improvement on the PMNS, applying to the \textsl{internal reduction} an approach similar to the truncated Montgomery reduction technique presented by Didier \emph{et al.} in \cite{DidierEGR24}. In the context of software implementations using \texttt{AVX512} instruction set extension, and modulo size up to 8192 bits, this new approach allows speed-ups up to 15\% in modular multiplication computation, in comparison with conventional approaches.

---


### 178. [Fluctuations of Nonlinear Observables in Mean Field Neural Network Training](https://arxiv.org/abs/2610.09768)

**<font color=#1a73e8>作者：</font>** Arnaud Descours, Geoffrey Lacour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mean field limits describe the training dynamics of wide neural networks through the evolution of the empirical distribution of their parameters. Although functional central limit theorems characterize the asymptotic fluctuations of this distribution, quantities of practical interest are typically nonlinear observables of the parameter distribution rather than the distribution itself. In this work, we show how these mean field fluctuations propagate to finite dimensional nonlinear observables for shallow neural networks trained by stochastic gradient descent. Working in the weighted Sobolev space in which the limiting fluctuation process is constructed, we apply a functional Delta method under ordinary Fr{é}chet differentiability, without requiring Lions derivatives with respect to the measure variable. We obtain a central limit theorem for the observables and, under a suitable representation of their differentials, an explicit covariance formula inherited from the underlying mean field fluctuation theory. We also study whether prescribed quantities of interest can be recovered from the selected observations. Under a constant rank assumption, we prove that a quantity of interest factors locally through the observation functional if and only if, throughout a neighborhood, the kernel of the differential of the observation is contained in that of the quantity of interest. Thus, a differential condition expressed directly in the ambient Sobolev space yields an exact nonlinear local factorization. These results provide a framework both for quantifying finite-width uncertainty on observable, statistically or physically meaningful quantities and for assessing whether the chosen observations contain the information required to identify them.

---


### 179. [Relational Abstractions for Spatial Reasoning with Diffusion Models](https://arxiv.org/abs/2610.09780)

**<font color=#1a73e8>作者：</font>** Ana Ezquerro, Ozan Özdenizci  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models excel at image synthesis, but they remain limited in their ability to reliably satisfy structured spatial reasoning constraints. In conditional data distribution modeling tasks with implicit logical structure, such as puzzles defined by visible clues paired with consistent solutions, state-of-the-art generative models tend to approximate pixel-space distributions without learning the underlying logical rules required for inference. To address this limitation, we present a novel framework for spatial reasoning with diffusion models that leverages unsupervised object discovery and abstractions of object relations. We show that the relational knowledge derived from object-centric representations enriches diffusion models with structural primitives, allowing them to effectively guide the generative representation space during both training and inference, and enabling conditional image generation that satisfies reasoning constraints. Additionally, we introduce a large-scale generative spatial reasoning benchmark with four datasets inspired by human-solvable puzzles. Our results show that relational abstractions significantly improve reasoning capabilities of diffusion models on a variety of complex reasoning tasks, while enabling robust generalization in out-of-distribution settings.

---


### 180. [AdaPS-LiNGAM: Adaptive Predecessor Selection for Linear Non-Gaussian Acyclic Models under Small-Sample Settings](https://arxiv.org/abs/2610.09782)

**<font color=#1a73e8>作者：</font>** Shun Yanashima, Kentaro Kanamori, Hirofumi Suzuki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery becomes particularly challenging when the available sample size is small relative to the number of variables. This challenge also arises in the linear non-Gaussian acyclic model (LiNGAM), an identifiable framework for causal discovery from observational data. DirectLiNGAM estimates a causal order, which arranges variables so that causes precede their effects, by sequentially identifying an exogenous variable and removing its linear effect from the remaining variables. We establish a structural limitation of this procedure: when the number of variables exceeds the sample size, repeated residualization necessarily becomes degenerate before the full causal order can be determined. Our analysis further reveals that each residual can be reconstructed using only a graph-determined subset of variables already placed earlier in the causal order, termed the active boundary. This result motivates AdaPS-LiNGAM (Adaptive Predecessor Selection LiNGAM), which reconstructs each residual directly from the original observations using an adaptively chosen sparse subset of those earlier variables. The same subset-selection principle is also applied to the final pruning step for edge estimation. Experiments on synthetic data demonstrate that AdaPS-LiNGAM provides accurate causal-structure recovery in sample-limited settings and degrades more gradually as the sample size decreases.

---


### 181. [CIRSeg: Coarse-to-Fine Intensity-Robust Liver Segmentation with Source-Free Continual Test-Time Adaptation](https://arxiv.org/abs/2610.09784)

**<font color=#1a73e8>作者：</font>** Ruoshi Xu, Mingqi Gao, Shengda Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable liver segmentation in contrast-enhanced MRI is essential for quantitative hepatic assessment, treatment planning, and longitudinal disease monitoring. However, limited annotated data and scanner- or vendor-dependent intensity variations can cause overfitting and poor generalization to unseen acquisition domains. Moreover, simultaneously achieving robust global localization and precise boundary delineation remains challenging, while predictions may contain isolated false-positive regions outside the main liver component. To address these challenges, we propose CIRSeg, a coarse-to-fine, intensity-robust liver segmentation framework based on nnU-Netv2. CIRSeg combines 3D CutMix with stochastic intensity transfer using either Nyul augmentation or histogram matching to improve robustness to heterogeneous MRI intensities. Its cascaded architecture decouples low-resolution anatomical localization from full-resolution boundary refinement. At inference, source-free test-time adaptation based on confidence-filtered predictions and probability-prior regularization further improves robustness to out-of-distribution inputs. As a final deterministic post-processing step, largest connected component filtering removes isolated false-positive regions. On the CARE 2026 test set, CIRSeg achieves Dice scores of 97.13\% and 97.93\% on the in-domain and unseen-domain subsets, with corresponding HD95 values of 20.18 mm and 11.30 mm, respectively. These results demonstrate consistently accurate segmentation across both in-domain and unseen acquisition settings. The code is available at this https URL

---


### 182. [UltraWorld: Learning Interactive Ultrasound World Models from Untracked Clinical Videos with Acoustic Sampling Map](https://arxiv.org/abs/2610.09785)

**<font color=#1a73e8>作者：</font>** Keke Yang, Erqi Wang, Sainan Guan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models can enable autonomous ultrasound scanning by predicting the outcomes of probe motions from local observations. Learning this action--observation relationship typically relies on synchronized video--pose pairs, which are costly to collect at scale and largely unavailable in routine clinical recordings. Reliable action following further requires modeling ultrasound's cross-sectional sampling geometry. We present UltraWorld, a self-distillation recipe that transfers priors from clinical ultrasound videos into interactive world models without real action annotations. Starting from clinical videos, we adapt a video foundation model into an ultrasound generator conditioned on reference images and anatomical masks. Anatomical masks sampled along programmable trajectories through 3D anatomy provide spatial guidance for synthesizing action--video pairs. We then use these synthetic pairs to self-distill the generator into a world model that predicts future observations from local observations and actions, without requiring anatomical masks or other 3D assets at inference time. To further improve action following, we introduce the Acoustic Sampling Map (AsMap), which represents probe poses and imaging settings as pixel-wise 3D sampling positions, beam directions, and depths. Experiments demonstrate improved prediction fidelity and action following. Across nine simulated closed-loop local planning episodes, UltraWorld reduces the mean final distance to the goal and orientation error by 29\% and 38\%, respectively, compared with visual servoing. Project Page: this https URL.

---


### 183. [Judging in Latent Space: Efficient Generative Reward Modeling via Semantics-Preserving Compression](https://arxiv.org/abs/2610.09788)

**<font color=#1a73e8>作者：</font>** Mingqing Yuan, Xiaobo Liang, Junwei Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reward modeling often requires jointly representing and reasoning over multiple evaluation criteria, yet verbalizing this process token by token can incur substantial inference cost. Recent work on latent reasoning suggests that continuous states may support this computation more compactly. We introduce LatentGRM, a latent evaluation framework built on semantic chunking, compression, and reconstruction. By using the structure of rubric-guided evaluations to guide compression, LatentGRM learns compact continuous trajectories that support autonomous pairwise judgments without generating textual assessments. A separate interpreter reconstructs evaluation text from these trajectories, providing an offline view of the information retained under compression. Under matched training data and backbones, LatentGRM achieves competitive aggregate preference accuracy relative to explicit Supervised Fine-Tuning (SFT) judges at both 4B and 8B scales. Across four benchmark domains, LatentGRM-8B compresses evaluation trajectories by 8.9--9.2x and reduces total judge inference time by 6.1--7.0x at vote@5. Controlled rubric interventions show that criterion-dependent preference information is carried through the latent sequence. Together, these results demonstrate that continuous latent evaluation can substantially reduce inference cost while preserving competitive judgment quality.

---


### 184. [Counterfactual Route Optimization for Gaussian Head Avatar Modeling](https://arxiv.org/abs/2610.09791)

**<font color=#1a73e8>作者：</font>** Shikun Zhang, Yong Li, Yiqun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Head avatar modeling requires jointly optimizing multiple objectives with different dominant effects on geometry, appearance, and cross-view consistency. However, their relative effectiveness varies across training states, while existing pipelines typically rely on fixed loss weights or handcrafted stage-wise schedules. A central challenge is therefore to identify which optimization direction is more beneficial at each training state. We propose a counterfactual route optimization framework for Gaussian head avatar modeling, which characterizes state-dependent optimization preference from the realized effects of alternative updates rather than predefined heuristic weighting. Starting from the same training state, we perform short-horizon route-restricted lookahead over geometry, appearance, and joint update routes and evaluate their outcomes under a unified utility. The resulting counterfactual evidence is factorized into a geometry--appearance preference and a residual joint advantage, separately capturing the relative preference between individual update directions and the additional benefit of coordinated optimization. We further amortize this offline evidence into a lightweight controller that directly estimates the current optimization preference and applies bounded modulation to the training objectives during full avatar optimization. Experiments on the NeRSemble dataset validate the effectiveness of the proposed design, consistently outperforming existing methods while preserving clearer local facial structures and finer details.

---


### 185. [A Proof-of-Concept Study of Weakly Supervised Labeling of Fine-Grained EEG Components for Artifact Attenuation](https://arxiv.org/abs/2610.09792)

**<font color=#1a73e8>作者：</font>** Lu Wang-Nöth, Hai Huang, Philipp Heiler 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) is highly susceptible to electromyographic (EMG) artifacts, whose temporal heterogeneity and spatial-spectral overlap with neural activity can leave mixed sources after blind source separation. Existing artifact-removal methods are further limited by scarce reliable component-level ground truth: expert annotations are costly and subjective, while no established method provides realistic simulation-based ground truth for EMG contamination in multichannel scalp EEG. To address these limitations, we propose a framework combining a frequency-aware high-dimensional representation with Multi-Instance Learning. The representation unfolds separated components into frequency-resolved intra-components, creating a space in which mixed neural and muscular activity becomes more separable, while the weakly supervised learning formulation enables artifact-likelihood scores for individual intra-components to be learned from epoch-level labels without finer-grained ground truth. The resulting intra-component classifier supports fine-grained EMG artifact detection and score-guided attenuation. Experiments on held-out subjects show that the framework learns informative intra-component scores and reduces artifact-related spectral deviations most clearly for jaw tension, with moderate effects for raising eyebrows and limited effects for frowning.

---


### 186. [Beyond Masks and Trajectories: Flow-Guided Latent Action Injection for Stable Surgical Video Generation](https://arxiv.org/abs/2610.09800)

**<font color=#1a73e8>作者：</font>** Tsz-Yui Qin, Siyu Zhou, Chi-Keung Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical video generation holds substantial potential for surgical education, simulation, and data augmentation, yet generating surgical videos with realistic and clinically plausible motion remains challenging. Most existing methods rely on auxiliary conditions, such as masks, trajectories, depth, or reference videos, to achieve visually plausible synthesis. Yet, these auxiliary conditions typically require additional manual annotation or specialized acquisition, making it difficult to scale such methods beyond small, curated datasets. This motivates the need for a reference-free architecture capable of generating high-quality surgical video without requiring auxiliary visual conditions at inference time. We propose FLAIR, a Flow-guided LatentAction Injection framework for Reference-free surgical video generation. FLAIR learns action priors from optical flow of real surgical videos, dynamically predicts corresponding latent action representation from an input prompt, and injects it into a frozen base model to generate surgical videos with improved action consistency. We further construct SurgActionClip-30K, the first large-scale surgical vision dataset comprising action-centric segmented clips and structured caption labels, addressing the persistent lack of fine-grained, action-centric surgical datasets. Lastly, we introduce SurgMetrics, the first surgical domain-specific evaluation metrics for quantifying the quality of generated surgical videos, addressing the persistent absence of clinically grounded evaluation standards in this domain. Extensive experiments demonstrate that FLAIR enables generating high-quality surgical videos using text-only inference without auxiliary conditions, and validation in SurgMetrics demonstrates its strength in alignment with human perception compared to traditional metrics.

---


### 187. [Concentration, Not Uncertainty: Why Targeted Synthetic Data Doesn't Help Camouflaged Object Detection](https://arxiv.org/abs/2610.09807)

**<font color=#1a73e8>作者：</font>** Akshat Dobhal, Sanjay Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camouflaged object detection requires pixel-accurate masks, but obtaining such annotations is slow and costly, making synthetic training images an attractive alternative. Under a fixed generation budget, however, it remains unclear which real-image regions to target for synthetic data generation. We study an uncertainty-guided generation strategy that clusters the unlabelled real images, identifies clusters on which the model is least certain, allocates synthetic generation toward those clusters, and iteratively retrains the model. Across 103 training runs, uncertainty-based targeting does not outperform random allocation. Five independent controls further show that this null result is not an artifact: targeted training sets are measurably different from random sets, but the difference is explained by concentrating the generation budget rather than by where uncertainty is concentrated, as every concentration rule we test reproduces the effect and, on boundary accuracy, so does aiming at the clusters the model was most certain about. Separately, we find substantial data contamination in CHAMELEON, with 50 of its 76 images duplicated from training data despite the standard overlap check reporting zero overlap. Together, these results show that, under a fixed synthetic-data budget, budget concentration, not uncertainty-based targeting, accounts for the observed training-set effects.

---


### 188. [Hierarchical Security Monitoring for Edge-IoT: A Formal Methods Approach](https://arxiv.org/abs/2610.09817)

**<font color=#1a73e8>作者：</font>** Nikolaos Kekatos, Marinelio Chintri, Panagiotis Katsaros 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber resiliency in edge-IoT deployments is fundamentally an economic problem: detection must keep critical processes operating under attack, but defender resources (compute, bandwidth, operator attention) are bounded. Centralised cloud monitoring offers expressive cross-device detection at prohibitive bandwidth cost; purely edge-local monitoring is cheap but blind to coordinated multi-device attacks where the asymmetric balance favours the attacker. We propose a lightweight hierarchical security-monitoring framework, built on formal runtime-verification methods, that occupies the practical middle ground at quantified cost. Each edge device runs a lightweight TeSSLa stream specification (size, payload validity, rate, and timestamp-drift predicates) that emits a four-valued verdict per aggregation window at sub-microsecond per-event cost; the gateway runs a parametric first-order MonPoly monitor over the per-device verdict streams at microsecond-scale per-verdict cost. The edge-to-gateway uplink carries roughly one Boolean per aggregation window per node, orders of magnitude smaller than the raw packet stream. The gateway tier detects coordinated attack patterns that no single-node monitor can see, shifting the asymmetric cost balance toward the defender. Every alert carries a witness set naming the device, the monitor tier, and the predicate that fired, providing an auditable record of the decision. We evaluate the framework on a container-host testbed spanning nominal and attacker nodes across four attack classes (buffer overflow, time spoofing, denial-of-service, and mixed advanced-persistent-threat patterns), and describe the edge- and gateway-tier specifications together with the cost-versus-coverage trade-off as monitor levels are added.

---


### 189. [AI-Driven Urge Regulation Assistant (AURA): Designing Preemptive Smart Wearables for Smoking Cessation](https://arxiv.org/abs/2610.09818)

**<font color=#1a73e8>作者：</font>** Antoni Timothy, Lam Fu Yuan Kevin, Hou Junyi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Smoking cessation remains a complex self-regulatory challenge, often undermined by cue-triggered cravings arising from habitual, emotional, and social contexts. Existing wearable cessation systems are largely reactive, detecting smoking events only after lapses occur and thus missing the critical window for timely intervention. Guided by cue-reactivity theory and Self-Determination Theory (SDT), we argue that future digital health systems should shift from retrospective feedback toward proactive craving management that supports user autonomy and competence. To inform the design of such systems, we present a formative pilot qualitative study involving semi-structured interviews with 10 smokers and ex-smokers from a multi-ethnic Asian population, a demographic underrepresented in current wearable AI and smoking cessation research. Through an iterative co-design interview process, we examine (1) the barriers and facilitators to smoking cessation and (2) the desired design features of wearable systems targeting cravings before lapses occur. Our findings identify key craving predictors across habitual, emotional, and social dimensions, alongside user-preferred intervention strategies such as social accountability, personalized support, rewards, and just-in-time distraction techniques. Participants also emphasized the importance of trust, privacy, personalization, and non-judgmental interaction styles. These insights directly inform the design of AURA, a novel smartwatch-smartphone ecosystem for proactive craving detection and intervention using commercially available wearable devices.

---


### 190. [Efficient 3D Gaussian Head Avatars for Edge Devices](https://arxiv.org/abs/2610.09821)

**<font color=#1a73e8>作者：</font>** Umar Farooq, Jean-Yves Guillemaut, Adrian Hilton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative 3D Gaussian head avatars provide high-quality, efficient rendering, but synthesising the Gaussian representation remains computationally expensive, limiting deployment on resource-constrained and edge devices. We introduce an efficient generator architecture for unconditional 3D Gaussian head synthesis, based on a parameter-efficient synthesis block and depth-wise separable convolutions while retaining style-based conditioning. Our architecture reduces generator complexity without requiring model compression or quantisation. Compared with the baseline model, our approach reduces FLOPs by 94%, parameter count by 70%, and model size by 81%, while maintaining competitive generation quality. We further demonstrate practical CPU inference and browser-based execution on mobile devices using ONNX Runtime, enabling 3D Gaussian avatar synthesis without dedicated GPU hardware or application-specific software. In addition to conventional image-quality metrics, we evaluate multi-view consistency, training cost, and deployment performance. Code, trained models, and evaluation tools will be released publicly.

---


### 191. [Homogenization in Multi-Agent Systems](https://arxiv.org/abs/2610.09824)

**<font color=#1a73e8>作者：</font>** Prakhar Ganesh, Kyra Wilson, Luca Zappella 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) leverage interactions between agents to perform complex tasks. Despite their success, we show that these interactions can also lead to homogenization, i.e., agents converging to similar behaviors. Homogenization in MAS can reduce agent diversity and reinforce shared failures. In this paper, we operationalize homogenization using three metrics: conformity to the majority, polarization towards extremes, and growing inertia against changes over subsequent interactions. We evaluate homogenization in MAS for code generation, hiring, and scientific peer review. Across these tasks, we show that homogenization translates to concrete downstream risks: in code generation, it hides and amplifies correlated errors which can create systemic vulnerabilities; in hiring, it allows the influence of biased agents to persist long after their removal; and in peer review, it creates uneven evaluation standards across research areas. Our results establish homogenization as a failure mode of MAS, demonstrating that MAS evaluations must move beyond aggregate performance to carefully analyze interaction dynamics. Finally, we show that simple approaches to increase diversity---leveraging sampling stochasticity and mixed-models MAS---fail to reduce homogenization risks, highlighting the need for strategies to effectively leverage agent diversity.

---


### 192. [Hybrid Hierarchical Runtime Verification for Edge-IoT Security: Combining MonPoly and RTLola](https://arxiv.org/abs/2610.09825)

**<font color=#1a73e8>作者：</font>** Nikolaos Kekatos, Marinelio Chintri, Panagiotis Katsaros 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security monitoring of edge-IoT fleets faces three structural challenges. (i) A per-node monitor is cheap but cannot see attacks that coordinate across devices. (ii) A cloud monitor sees the full fleet but pays for that view in bandwidth. (iii) Even at the cloud, a monitor built on a single RV engine can be fooled by an attacker who compromises a device, raises one malicious request, and then goes silent: once the events stop, an event-triggered monitor has nothing left to evaluate. We propose a three-layer hierarchical runtime-verification framework that addresses all three. The edge layer classifies events as they happen, the gateway layer aggregates short windows of per-device behaviour, and the cloud layer runs two complementary RV engines. MonPoly handles first-order temporal correlation over the merged alert stream: coordinated overflow (which genuinely quantifies across devices) plus per-device multi-vector APT, escalation, and persistent-campaign patterns. RTLola handles a time-triggered silent-node property that an event-triggered engine cannot detect within a bounded delay under fleet silence. We evaluate the framework on a 15-actor Docker testbed covering eight attack profiles plus a silent-bypass scenario. In the controlled labelled testbed, every device-attributable incident the framework raises names an attacker-labelled device, and the RTLola tier catches silent-bypass attempts the event-triggered tier misses. Per-event monitoring stays in the microsecond range at the edge and gateway, with low end-to-end alert-to-incident latency at the cloud.

---


### 193. [MOTIF: Person-of-Interest Deepfake Detection Beyond 3DMM Coefficients](https://arxiv.org/abs/2610.09830)

**<font color=#1a73e8>作者：</font>** Giovanni Affatato, Sara Mandelli, Paolo Bestagini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video deepfakes targeting a specific individual, the Person-of-Interest (POI), are the most harmful ones, and, since a public figure is abundantly recorded, a detector can be built from genuine footage of that individual. Such detectors commonly describe a subject through a 3D Morphable Model (3DMM) and adopt its coefficients as a whole, so which part of that description carries the signal has never been measured. We dissect it, holding the encoder, the training corpus and the enrollment protocol fixed and varying only what the encoder observes. The groups of coefficients prove largely redundant, since the shape block alone recovers almost all the accuracy of the full vector, and their temporal evolution contributes a real but bounded amount. We further show that the dense surface the same fit returns, which these detectors discard, carries identity information that the coefficients do not, and that it helps precisely where they are weakest. We assemble the best configuration into MOTIF, a visual-only detector trained on real videos only, with no manipulated video and no POI-specific data. It improves on both state-of-the-art POI detectors in every dataset and manipulation of our benchmark and at two quality levels. Our experimental code will be released at this https URL.

---


### 194. [ORCA: Hunting Compositional Failures in Text-to-Image Diffusion](https://arxiv.org/abs/2610.09841)

**<font color=#1a73e8>作者：</font>** Arshia Hemmat, Amirhossein Vahidi, Amitis Shidani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models fail predictably on compositional prompts: attributes bind to the wrong objects, spatial relations invert, and multi-object scenes lose count. Recent architectures already augment CLIP with a T5 encoder precisely because CLIP's contrastive embedding loses compositional structure, yet these failures persist. We argue the binding problem is therefore not one of missing information but of misaligned information: a text encoder preserves compositional structure, but in a representation space shaped by language modelling rather than vision, and the denoising objective does not directly reward aligning the two. We show this correspondence can be supplied as an explicit training signal, that the relevant cross-modal information is concentrated in a low-rank subspace of self-supervised visual features, and that supplying it can be folded into diffusion training as a single auxiliary loss. Our method, ORCA (Orthogonal Residual Compositional Alignment), aligns the latent of a diffusion transformer with a low-rank target derived from a frozen visual encoder, through a predictor whose orthogonal basis is parameterised by a learned residual between T5 and CLIP embeddings, which provides a prompt-dependent signal for selecting the visual readout subspace. We prove that the cross-modal information recoverable at a given rank is bounded by the spectral mass of the visual encoder's covariance in the top components. Across three diffusion-transformer backbones (DiT-B/2, DiT-L/2, U-ViT-L), ORCA improves FID and GenEval over both vanilla and REPA baselines at zero inference-time cost; on DiT-L/2 it reaches FID 16.65 and GenEval 0.291 at 200K steps, exceeding the strongest 400K baseline at half the training cost, with the largest gains concentrated on attribute binding, spatial relations, and multi-object prompts.

---


### 195. [For Those Who Believe in Faithfulness: Optimizing the Area Under Insertion and Deletion Curves for Ranking Relative Feature Importance](https://arxiv.org/abs/2610.09844)

**<font color=#1a73e8>作者：</font>** Bjørn Leth Møller, Bulat Ibragimov, Christian Igel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The adoption of machine learning for socially relevant tasks requires effective explainable artificial intelligence (XAI) methods to better understand the behavior of machine learning models. Attribution methods are a popular XAI approach in which input-output relationships are characterized by heat maps that reflect the relative importance of input features for a particular prediction. The quality of such maps is often assessed by measuring faithfulness based on the area under insertion and deletion curves, which measures changes in the model output as features are added and removed. In this study, we derive an objective function from this notion of faithfulness and a way to approximate its gradient. We establish the connection between insertion curves and top-$k$ feature selection, which leads to a loss function measuring the quality of attributions. Randomization of the loss allows us to efficiently approximate its gradient. To show the effectiveness of the general approach, we combine the loss function with the neural explanation mask framework. The resulting method, termed Ra-NEM, can be used with any differentiable model without affecting the model's performance. Experiments demonstrate that Ra-NEM provides accurate attributions robustly and efficiently. Compared to other algorithms, the attributions have not only higher faithfulness but also perform well in terms of other XAI metrics. The high inference speed of Ra-NEM makes the method suitable for online applications. The code is available online: this https URL

---


### 196. [Stream-Based Active Learning with Cooperative Neural Networks for Data-Efficient Partial Inverse Design: An Automotive Glass Run Channel Case Study](https://arxiv.org/abs/2610.09848)

**<font color=#1a73e8>作者：</font>** Agung Nugraha, Hyerin Kwon, Heungjun Im 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse design in engineering often runs into a simple problem. Each labeled training sample must be produced through expensive simulation, so building a large dataset is slow and costly. This study addresses that problem for partial inverse design, where only some design variables are specified and the rest must be inferred to reach a target performance value. We propose CoNN-AL, a framework for data-efficient partial inverse design that adds stream-based active learning to the Cooperative Neural Network with Denoising Autoencoder (CoNN-DAE). The model estimates predictive uncertainty through Monte Carlo dropout and uses it to decide, in real time, which incoming candidate samples are worth labeling, so the limited labeling budget is spent on the most informative designs. We validate the framework on a real-world automotive glass run channel dataset of more than 900,000 unique simulated designs. With only 20,000 actively selected labels, about 2.3% of the training pool, CoNN-AL reaches R-squared values of 0.967 to 0.982 across all missing-variable levels, approaching the upper-bound models trained on far more data. It reaches R-squared of at least 0.95 with 30 to 40% fewer labels than random sampling at the more difficult missing-variable levels and, at the most challenging level, is the only strategy in this study to reach R-squared of 0.98. Together with this work, we publicly release the dataset to support future research on data-driven design.

---


### 197. [Hard, Yet Reducible: Controlled Forward Transfer for Synthetic Degradation Curation](https://arxiv.org/abs/2610.09849)

**<font color=#1a73e8>作者：</font>** Chunming He, Kailai Zhou, Jiaming Zuo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Selecting synthetic degradations for dense prediction requires an estimate of their training utility, the generalization gain they bring under a finite training budget. Clean and degraded twins share content and labels, suggesting a score based on how much short training reduces the excess error caused by degradation. However, this gap can also shrink when clean performance deteriorates. Measuring the improvement on degraded images alone avoids that confound, but it still credits progress that the same amount of clean training would have produced. We propose the \textbf{controlled Reducible Degradation Gap} (cRDG) for regions defined by degradation type and severity. From a common checkpoint, cRDG runs two budget-matched probes that differ only in one augmentation slot, which holds either a synthetic degradation or a clean augmentation. The score is the gain on held-out degraded images relative to the clean-control probe. Clean harm is a separate feasibility constraint. cRDG reveals a correctable severity band in which training on the degradation yields high controlled gain under the available budget, and the band moves with the predictor, the starting checkpoint, and the training budget. \textbf{Curation of Reducible Bands} (\method) uses cRDG to select synthetic data without changing the predictor. On semantic segmentation and salient object detection, \method{} improves representative predictors under matched synthetic-data budgets and training schedules, extends to existing data-generation pipelines, and preserves clean performance. Code and supporting materials will be publicly released.

---


### 198. [DeltaSplat: Iterative Gaussian Refinement for Pose-Free Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2610.09853)

**<font color=#1a73e8>作者：</font>** Chanung Park, Seunghyeon Song, Joo Chan Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pose-free feed-forward 3D Gaussian Splatting (3DGS) reconstructs a scene from sparse, unposed images in a single network pass, removing the need for camera calibration and per-scene optimization. However, camera estimation errors propagate into the predicted Gaussians and compound the geometric and photometric inaccuracies of single-pass prediction. To correct these errors, we introduce DeltaSplat, a lightweight Gaussian refinement module for pose-free feed-forward 3DGS. It iteratively renders the current Gaussians at the input context views and predicts per-Gaussian updates from the resulting residuals. A 2D residual alone, however, underdetermines the 3D correction. DeltaSplat therefore conditions each update on per-pixel Plücker rays and rendered depth as a soft geometric prior. A dual-branch convolutional mixer efficiently encodes these inputs, and per-attribute heads decode the fused features into position, opacity, and color updates. The module adds only ~2.2% parameters to the backbone and remains fully feed-forward at inference. On DL3DV, DeltaSplat reaches 26.64 dB PSNR in the pose-free setting, improving its state-of-the-art backbone by 1.75 dB and surpassing even baselines supplied with ground-truth cameras; consistent gains hold across 6-24 views and all camera regimes.

---


### 199. [Self-Evolve With a Reference:Anchored Training of Tool-Integrated Agents](https://arxiv.org/abs/2610.09856)

**<font color=#1a73e8>作者：</font>** Wenjie Liao, Liangjie Zhao, Zehong Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving tool-integrated agents learn from tasks and feedback generated within their own training loop. A Curriculum Agent generates tasks, while an Executor Agent learns from self-consistency signals through reinforcement learning. However, relying solely on the current Executor for feedback has two limitations: group-relative advantages vanish under full consensus, while uncertainty-based curriculum rewards favor disagreement without showing whether the generated tasks support further learning. These limitations motivate an additional reference beyond the current Executor. We propose \textit{AnchorLoop}, which introduces a frozen copy of the previous iteration's Executor as a historical reference and reuses it on both sides of the training loop. For the Executor, the anchor provides a cross-reference advantage that evaluates current outputs against both current and historical majority answers. For the Curriculum, it provides an agreement-based reference based on differences in sampled majority agreement. Since the Executor and anchor have identical parameters during Curriculum training, this comparison serves as a proxy for task selection rather than evidence of inter-version improvement or correctness. Across 13 reasoning benchmarks, AnchorLoop improves over Agent0 by 2.5\% on mathematical reasoning and 2.8\% on general reasoning tasks. It also maintains higher effective-advantage variance and continues improving in later iterations as the unanchored baseline shows diminishing gains. These results demonstrate the benefit of introducing a lightweight historical reference into self-evolving tool-integrated agents without external task or answer supervision.

---


### 200. [DeepTopoClustering: Unsupervised Derivation of Surface Process Taxonomy from 4D Point Clouds for Topographic Monitoring](https://arxiv.org/abs/2610.09860)

**<font color=#1a73e8>作者：</font>** Jiapan Wang, Daan Hulskemper, Mathilde Letard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D point clouds acquired by permanent laser scanning (PLS) enable accurate high-frequency monitoring of surface change in dynamic topographic environments. However, existing methods remain limited in organizing detected surface activities into meaningful process types. We propose DeepTopoClustering (DTC), an unsupervised framework for deriving a hierarchical process taxonomy from object-based surface activities, so-called 4D objects-by-change (4D-OBCs). We transform each 4D-OBC into a GeoMorphogram, a distributional sequence representing the temporal evolution of topographic change within a spatially bounded surface activity. A convolutional autoencoder learns latent embeddings from GeoMorphograms, which are jointly optimized using a hierarchical deep clustering objective to organize surface activities into a hierarchy. We evaluate the learned hierarchy using expert annotations on two 4D datasets of sandy beach sites and their combination. DTC with GeoMorphograms achieves the highest agreement with expert judgment at the taxonomy level comprising eight major process types ($F_1=0.78$, match accuracy $=0.92$), outperforming dimensionality reduction and conventional flat clustering. The learned taxonomy separates major erosion- and deposition-dominated activities and distinguishes finer subtypes based on change magnitude, duration, compactness, and temporal evolution. DTC thus provides a scalable and interpretable route from 4D change detection to a data-driven, expert-supported surface process taxonomy, advancing automated knowledge derivation for understanding surface dynamics in topographic monitoring.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-324](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

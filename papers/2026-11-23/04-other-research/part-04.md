# 📦 其他研究 | 2026年11月23日

> 本类共 **265** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-265](./part-06.md)

---

### 151. [LIFT: Latent Flow Matching for Probabilistic Cell Fate Dynamics with Single Cell Snapshots](https://arxiv.org/abs/2611.25917)

**<font color=#1a73e8>作者：</font>** Bowen Yang, Junda Ying, Yuxuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lineage tracing links cell states through clonal ancestry, but does not generally identify unique source-descendant pairings. Learning from such data therefore requires a model of conditional outcomes, rather than only the terminal population distribution. We introduce LIFT, a latent flow framework for probabilistic cell-state generation from lineage-informed couplings. Variational inference encodes alternative outcomes in a latent space, while a conditional prior enables sampling from the initial state alone. A Mean Flow decoder predicts future cell state directly, requiring one decoder evaluation per sampling, which makes it convenient to predict cell fate through large scale Monte-Carlo sampling. This construction combines a representation of one-to-many relationships with efficient sampling and an analysis of conditional prediction error. Experiments on synthetic and real datasets demonstrate LIFT's ability to recover both population distribution and cell fate probabilities.

---


### 152. [A Lightweight Hybrid Approach for Milling Force Reconstruction from Internal Machine Signals](https://arxiv.org/abs/2611.25921)

**<font color=#1a73e8>作者：</font>** Eric Hirsch, Christian Friedrich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven monitoring based on milling force can enable advanced manufacturing services including process optimization and condition monitoring. However, industrial implementation is often hindered by costly and intrusive hardware and large training data requirements. This paper therefore presents a hybrid approach using machine-internal signals and machining metadata to enable force-based monitoring on brownfield machines without additional sensors. Commonly available machine signals have relatively low sampling rates and cannot directly represent high-frequency milling-force variations, especially at higher spindle speeds. Instead of learning the complete force signal, which would increase model complexity, data requirements, and overfitting risk, a supervised machine-learning model predicts only the average milling force from selected machine-signal features and machining parameters. This low-frequency estimation parameterizes a static milling force model that reconstructs the force behavior over one spindle revolution. Although the static model does not reproduce all dynamic effects, it captures the force distribution, load levels, and angular regions of highest tool engagement. The approach is evaluated on one milling machine across varying process parameters, engagement conditions, cutting tools, and two workpiece materials. Dynamometer measurements are required only for development and validation. Ridge regression achieves an $R^2$ of $0.984$ and $0.991$ for average-force prediction on the test data ($\bar{F}_x$ and $\bar{F}_y$). The reconstructed force behavior over one spindle revolution achieves an $R^2$ of $0.962$ and $0.982$ ($F_x$ and $F_y$) compared with the reconstruction based on measured force features. The method provides a cost and computationally efficient basis for process monitoring, tool condition assessment, and process optimization on existing machines.

---


### 153. [Ground Truth Bias in AI-Assisted Medical Annotation: A Crossover Study Using an Independent Radiologist Reference Standard](https://arxiv.org/abs/2611.25924)

**<font color=#1a73e8>作者：</font>** Márton Baltay, Tamás Ilcsik, Márton Borbély  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Behavioural evaluations of artificial-intelligence-assisted annotation score every human decision against a reference standard, so their conclusions inherit that standard's validity. We tested how far conclusions about assistance, reliance and individual differences depend on it. Fifty-one non-expert high-school students annotated 50 knee radiographs for osteoarthritis, with and without a deliberately imperfect classifier, in a crossover design; personality and non-verbal reasoning were also measured. Decisions were scored against the public repository labels and against an independent reference standard from a radiologist panel, which graded 23 of the 50 images as indeterminate. Against the repository labels, assistance raised accuracy from 60.4% to 65.3% (odds ratio 1.23, p=0.002). Against the independent standard, the gain on the 27 determinate images was smaller and not significant in the primary model (78.4% to 80.8%; odds ratio 1.16, p=0.178). The apparent benefit had been concentrated on the indeterminate images and was not significant when those images were assigned to either class. The direction of residual over-reliance depended on how indeterminate cases were handled, and the personality trait most strongly associated with accuracy changed identity and sign between standards. Reliance measures are only as valid as the reference standard that defines when the assistant is right.

---


### 154. [AGSR: Aperture-Guided Super-Resolution for Gaussian Splatting](https://arxiv.org/abs/2611.25934)

**<font color=#1a73e8>作者：</font>** Ayman Alkhateeb, Hadi Amirpour, Christian Timmerer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables real-time novel view synthesis, but Gaussian rasterization attenuates fine-scale scene structure through the projected covariance of each primitive. We show that contracting these projected covariances at inference time can mitigate the effective bandwidth limitation induced by finite Gaussian footprints, motivating a multi-aperture rendering framework for super-resolution.
Based on this insight, we propose AGSR (Aperture-Guided Super-Resolution), a lightweight inference-time framework that progressively fuses multi-aperture renderings using uncertainty-guided feature aggregation and geometric conditioning from transmittance and depth cues. AGSR operates as a plug-in enhancement for pre-trained 3DGS models.
Experiments on the Mip-NeRF 360 benchmark show that AGSR outperforms lightweight image-space super-resolution baselines, with gains increasing as the underlying Gaussian representation deteriorates. The results provide evidence that covariance contraction exposes bandwidth-sensitive structural cues attenuated by native Gaussian rasterization. AGSR achieves these improvements while maintaining real-time performance with up to 139k parameters.

---


### 155. [TwinD: Generalizing Deepfake Detection from Blending to Entire Face Synthesis](https://arxiv.org/abs/2611.25935)

**<font color=#1a73e8>作者：</font>** Andrii Yermakov, Jan Cech, Mario Fritz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial deepfake detectors are usually trained on blending fakes, where a generated face is pasted back into a real frame. Recent generators synthesize the entire face and leave no traces of blending. On a benchmark of 19 datasets released from 2019 to 2026, the best prior facial deepfake detector reaches a mean AUROC of 96.2% on ten blending datasets, but none exceeds 78.1% on five datasets of entire face synthesis (EFS). AI-generated content (AIGC) detectors do not close this gap. We propose TwinD, a detector trained on FaceForensics++ fakes and two kinds of twins: fakes made from a real frame. A reconstruction twin is a real frame reconstructed by an autoencoder, with the real pixels put back in a random region. It targets the neural traces of a decoder. A blob twin blends an altered copy of a real frame with the frame itself, targeting blending artifacts. It needs no generator and no face-shaped mask. Together, these twins provide two complementary forensic cues that generalize to unseen manipulations. TwinDreaches a mean AUROC of 96.3%, 8.9 points above the prior state-of-the-art, with 98.1% on the blending datasets and 95.6% on the EFS datasets. Trained on twins alone, without a deepfake dataset, single models still reach 94.3% on average over three seeds. For reproducibility, the code, trained model, and training data are at: this https URL

---


### 156. [Gradient Boosting with Kolmogorov-Arnold Units for Interpretable Regression beyond Pairwise Interactions](https://arxiv.org/abs/2611.25942)

**<font color=#1a73e8>作者：</font>** Minjong Cheon, Hanseon Joo, Eunji Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretable models for tabular regression, such as the explainable boosting machine (EBM), restrict a prediction to main effects and pairwise interactions so that every part of it can be plotted. When the target depends on three or more inputs jointly, this restriction costs accuracy, and a black-box model with post hoc explanations becomes the usual fallback. Here we present MJBoost, a gradient boosting method whose weak learner is a single Kolmogorov-Arnold unit $g(\sum_p \phi_p(x_p))$ with penalized spline inner and outer functions. Each unit is fitted in closed form by alternating penalized least squares, starting from principal Hessian directions of the residual, and categorical and missing inputs enter the units directly. Because a unit depends on each input only through one inner function, the fitted model has an exact functional ANOVA decomposition into main effects, pair effects and a higher-order remainder, which one-dimensional convolutions compute. On synthetic targets of interaction order three to six, the test error of MJBoost is up to 13 times lower than that of EBM, and its decomposition recovers the true variance share of every order to within 0.04. On the 35 regression tasks of the OpenML-CTR23 benchmark, it has a lower test RMSE than EBM on 21 tasks and a higher one on 2 (geometric-mean RMSE -29.1%). On these tasks the main and pair effects of the fitted model explain a median 0.992 of its variance, so the model reads as plots where the data allow, and the decomposition measures the higher-order part where they do not. With Newton steps the same algorithm classifies: on 32 binary tasks of OpenML-CC18 its test log-loss is on par with that of EBM, and on 11 multiclass tasks its mean log-loss is lower than that of EBM on 8 and than that of tuned LightGBM on 7.

---


### 157. [Point Dynamics as Proxy for Robotic World Models](https://arxiv.org/abs/2611.25946)

**<font color=#1a73e8>作者：</font>** Dong An, Tianyu Liu, Haoran Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic world models predict future video frames from the current observation and a sequence of robot actions. While recent models follow the given actions closely, manipulated objects often collapse or move inconsistently with the action. We attribute this to the conditioning: an action, or a rendering of the robot, specifies where the robot goes but not how the scene responds, leaving a single video model to infer the interaction dynamics implicitly while also rendering appearance. We therefore separate dynamics prediction from visual rendering, with 3D point dynamics as the proxy between them. Specifically, we lift the first frame into 3D points, simulate how they respond to the robot's motion with a learned point dynamics model, and render the simulated points back into pixel-aligned videos that any video model can read. In controlled experiments on the DROID dataset with two video renderers of different architectures, this point dynamics proxy reduces object motion error by 8.6% and 6.2% without degrading image quality, and by 8.1% on a real bimanual robot. Moreover, the video follows the simulation: more accurate dynamics yield more accurate object motion, and editing the points steers the video. This suggests that advances in dynamics modeling can translate into more faithful robotic world models.

---


### 158. [GaussTrans: A Gaussian Interface Framework for Multi-Layer Refractive Transport](https://arxiv.org/abs/2611.25950)

**<font color=#1a73e8>作者：</font>** Zixuan Zhao, Tao Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate surface modeling of multi-transparent interfaces to achieve accurate light transmission. The interplay of errors in geometric structure, light paths, and observation results during the reconstruction of transparent media with a high number of layers makes this a challenging problem. Some existing techniques address the reconstruction of transparent scenes by reducing the number of layers or simplifying light paths; however, this limits their direct applicability to high-order transparent scenes. We propose GaussTrans, a compact framework for light transport in high-order transparent scenes, consisting of three components: Gaussian-Field Hybrid Surfaces, Transport-Coupled Refinement, and Primitive-Guided Implicit Intersection. Gaussian-Field Hybrid Surfaces use a hybrid approach combining Gauss surfaces and fields to reconstruct different interfaces. Transport-Coupled Refinement reduces coupling errors by evaluating the entire light path. Primitive-Guided Implicit Intersection combines primitive support regions to reduce errors in the intersection of interfaces and rays. In experiments on datasets such as RefRef, GaussTrans achieves significantly higher accuracy with relatively low spatial storage requirements.

---


### 159. [MorphTwin: Enriching Deformable Material Responses from Videos for Morphable and Interactive Physical Twins](https://arxiv.org/abs/2611.25963)

**<font color=#1a73e8>作者：</font>** Haoqin Hong, Ding Fan, Fubin Dou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing interactive physical twins from video requires accurately capturing how objects deform while maintaining efficient simulation. We observe that reproducing motion in a video does not guarantee correct responses to new forces when the physical representation restricts how an object can deform. In spring-based twins, coupling between volume and shape responses creates such a limitation. We present MorphTwin, which enriches local deformation modes to capture and independently control these responses while retaining standard spring forces and explicit simulation. To support interpretable material editing and transfer, we use offline calibration to map shared relative response changes to stiffness updates on each reconstructed graph. Under identical inverse settings on synthetic scenes, MorphTwin reduces the mean absolute error of Poisson's ratio by 75.8% and the mean relative error of Young's modulus by 22.1% compared to PhysTwin. We introduce an egocentric stereo and RGB-D benchmark covering interactions with objects of varying stiffness. Real-world experiments demonstrate improved reconstruction accuracy and up to 14.4% lower future tracking error than PhysTwin at interactive speeds.

---


### 160. [Power Setpoint Tracking for Large-Scale EV Charging: Transformer-Constrained Charging Policy Learning with Self-Tuning Constraint Prices](https://arxiv.org/abs/2611.25965)

**<font color=#1a73e8>作者：</font>** Daniyal Sajedi-Hosseini, Yoshihiko Fujisawa, Shubham Singh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In power setpoint tracking (PST), an operator follows a purchased charging profile without overloading shared transformers or undercharging vehicles. PST is cast as a constrained Markov decision process that minimizes tracking error subject to overload and mean user-satisfaction constraints. Transformer-Constrained Charging Policy Learning (TC-CPL) extends soft actor-critic with proportional-integral Lagrange-multiplier updates from measured violations, a residual on the incumbent dispatcher that is warm-started from its demonstrations, and a transformer-aware encoder shared by all ports. It observes no departure times or states of charge. Simulations (five seeds, 100 paired days) compare it with the incumbent, Round-Robin. On a 600-port, 122-substation district, raw overload falls from 3.59 to 0.0017 kWh/day (overloaded seed-days from 77% to 0.4%), and absolute tracking error falls by 27%. Delivered energy rises by 16%, and satisfaction rises from 0.959 to 0.989. On a 42-kW transformer with household load, overload falls from 1.86 to 0.0014 kWh/day and satisfaction rises from 0.974 to 0.985, but absolute tracking error is 22% higher. Against hand-set fixed multipliers, self-tuning is statistically indistinguishable on the district. On the single transformer, it raises satisfaction by 0.011 at similar overload, but a short sweep found a better-serving fixed pair. The overload multipliers stay below their cap.

---


### 161. [Sample-efficient end-to-end Optical Music Recognition through Active Learning](https://arxiv.org/abs/2611.25975)

**<font color=#1a73e8>作者：</font>** Eric Ayllon, Francisco J. Castellanos, Antonio Rios-Vila  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end approaches to Optical Music Recognition (OMR) have recently shown promising results, but their performance often degrades on unseen data. A common solution is to pretrain and fine-tune models with annotated samples from the target domain, improving adaptation to new distributions. However, this process typically requires extensive manual annotation to yield competitive models, making it costly and time-consuming. In this work, we explore Active Learning to reduce this burden by selecting informative samples for labeling in low-resource scenarios, where the amount of manual annotation that can be performed is limited. We evaluate both uncertainty- and diversity-based sampling strategies on staff-level and full-page corpora. Results show that confidence-based sampling performs comparably to oracle selection (based on true error), and that each scenario benefits from a tailored strategy.

---


### 162. [Multi-View Transformer with Geometry-Guided Multi-Modal ControlNet for 3D Virtual Try-On](https://arxiv.org/abs/2611.25979)

**<font color=#1a73e8>作者：</font>** Sarthak Batra, Armin Mustafa, Adrian Hilton  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Editing a 3D Gaussian Splatting (3DGS) capture of a person so that they wear a new garment requires every rendered view to agree on the same garment details. Existing 3D virtual try-on (VTON) pipelines, however, edit training views largely independently and fuse them with hand-designed heuristics such as manually chosen reference views and fixed attention-blending weights. The resulting inconsistencies are baked into the 3D representation and surface as texture drift, blurred prints, and implausible geometry in novel views. We present GS-VTON-MVT, a three-stage framework that combines implicit and explicit 3D reasoning for consistent 3DGS try-on. (i) A multi-view inpainting transformer jointly edits a set of training views with full cross-view self-attention, so that cross-view correspondence is learned rather than imposed. (ii) A geometry-guided multi-modal ControlNet conditions the diffusion editor on the garment image together with depth and surface normals rendered from the current 3DGS state, supplying explicit structure where visual evidence is weakest. (iii) A pose-adaptive persona-aware attention replaces the fixed blending weight between current-view and reference-view features with weights derived from camera-pose proximity. On the 3D-VTONBench benchmark, GS-VTON-MVT improves FID, KID, LPIPS-based cross-view consistency, and user preference over general-purpose 3D editors and prior 3D try-on methods.

---


### 163. [Seeing Beyond the Obvious: Complementary Semantic Guidance for Salient Single-Positive Multi-Label Learning](https://arxiv.org/abs/2611.25986)

**<font color=#1a73e8>作者：</font>** Tong Jin, Meng-Long Wang, Xingyu Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Salient Single-Positive Multi-Label Learning (SalSPML) assigns each image its most salient positive label, leaving other classes unlabeled. Existing methods construct class-level Salient Prototypes from observed positives to guide the recognition of unobserved classes. However, since salient annotations favor visually prominent instances, these prototypes may not fully capture the visual diversity of hidden positives, resulting in insufficient positive supervision. To address this limitation, we propose CoST, a Coverage-guided Complementary Soft-Target Refinement framework that supplements Salient Prototypes with complementary class-semantic information. Specifically, CoST identifies semantically relevant candidates from unknown classes by leveraging task-learned category information and image-text semantic correspondence. The selected candidates are then aggregated into class-wise Coverage Prototypes to complement the semantic representations provided by Salient Prototypes. Furthermore, we introduce a ranking-based selective refinement strategy that identifies classes receiving stronger semantic support from Coverage Prototypes and selectively enhances their soft targets while preserving the base soft targets for the rest. Experiments on multiple benchmarks demonstrate the effectiveness of CoST, with strong performance gains over existing baselines.

---


### 164. [From AI Surrogate to Engineering Tool: Toward Production Use of Fiber-Orientation Prediction in Crash CAE](https://arxiv.org/abs/2611.25991)

**<font color=#1a73e8>作者：</font>** Osamu Ito, Yoshikazu Nakagawa, Tomoaki Tatsukawa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Crash simulations of glass-fiber-reinforced plastic parts are highly sensitive to the fiber-orientation field supplied to the material model. In conventional workflows, that field comes from resin-flow analysis, which requires molding-specialist support and takes about 25 hours of work per part. We previously proposed a surrogate model that addresses this bottleneck by predicting the orientation field in about 3 minutes. This paper reports the implementation, validation, and operational design that turned the model into an engineering tool for Honda design workflows. We present staged validation from 2D plates to production parts, evaluation against a predefined engineering angular-error criterion, and the expert review that approved design use in March 2025; the system has since been transferred to the crash-safety group and is in initial, limited use in directed fracture-prediction scenarios. The developed system combines injection-gate setting support for cases in which gates are unknown (90% gate-count accuracy, mean position error 11% of flow length), voxelization, surrogate inference, automatic mapping to the crash CAE model, and report generation in a single GUI. The complete orientation-preparation workflow takes about 0.1 hours, a 99.6% reduction from the conventional 25-hour flow-analysis route, and can be run directly by crash CAE engineers without molding-specialist support. As evidence of practical impact, component-level crash analysis using the predicted orientation field reduced the absolute peak-force error from 19.0% with an isotropic baseline to 11.4%, while confining predicted fracture to the test-observed region. The deployment lesson is that a surrogate model alone is not enough for practical adoption: gate-setting support, automatic data conversion, and shareable reporting are what make the model usable as a design tool.

---


### 165. [Reinforcing Few-Step Diffusion Models via Shadow Posterior Matching](https://arxiv.org/abs/2611.25998)

**<font color=#1a73e8>作者：</font>** Jingqiao Xiu, Yicong Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Few-step diffusion models are widely deployed for their efficiency. However, reinforcing them with black-box rewards, as is routine for multi-step models, faces two structural challenges. First, a few-step generator is a sampler rather than a score model, so its velocity is not the forward velocity of the generated distribution. Second, it must be anchored to the undistilled teacher, which shares no transitions with it. Existing few-step RL methods handle the latter with a marginal KL to the teacher, but each pays for the former in its reward credit. We propose Shadow Posterior Matching (SPM), which renoises generated samples into shadow inputs and obtains the credit from their shadow posterior. From the KL-regularized reward objective, we derive a regression loss that turns reward values into a reward direction while anchoring the generator's outputs to the teacher and aligning the shadow inputs with the deployed inputs. Applied to 4-step generators, SPM achieves higher rewards with less reward hacking than prior few-step RL methods.

---


### 166. [Xing-Audio-NVVASR: Scaling and Refining Supervision for Joint Recognition of Speech and Non-Verbal Vocalizations](https://arxiv.org/abs/2611.26000)

**<font color=#1a73e8>作者：</font>** Pengyu Xu, Gang Liu, Genliang Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Joint recognition of speech and non-verbal vocalizations (NVVs) is hindered by scarce event-rich training data and inaccurate or missing event labels. We present Xing-Audio-NVVASR, an end-to-end recognizer trained through progressive data mining and iterative supervision refinement. Guided by unified acoustic criteria, two heterogeneous models cross-audit annotations, flagging disagreements for teacher reannotation. To uncover shared omissions that model agreement may conceal, complementary breath detectors screen the entire corpus for human review. Human-confirmed labels accumulate across rounds and are preserved during subsequent refinement. Over five rounds, we refine annotations for 170,000 utterances from public corpora and incorporate 630,000 mined utterances. The resulting corpus of approximately 800,000 utterances is used to train a single 1.7B-parameter model that transcribes speech with inline tags for six NVV classes. Across four human-annotated benchmarks, Xing-Audio-NVVASR ranks first among nine models in both composite score and six-class Macro-F1. It achieves a mean composite score of 64.46, surpassing the strongest comparison model, StepAudio 3 Chat Preview, by 6.03 points, and exceeds the annotation teacher's breathing F1 by 14.40 to 31.57 percentage points. We plan to release the model weights, inference code, four evaluation benchmarks, annotation guidelines, and evaluation code.

---


### 167. [When Agents Play Differently: Localizing Human--Agent Behavioral Divergence with Conditional Distributional Testing](https://arxiv.org/abs/2611.26012)

**<font color=#1a73e8>作者：</font>** Oleg Smirnov, John Pertoft, Sara Karimi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating whether artificial agents behave like humans requires comparing not just average outcomes but entire behavioral distributions across diverse contexts. We propose a stratified framework that computes nonparametric discrepancy statistics within contextual cells, and discovers subgroup rules identifying where agent behavior departs from human play. We show that session-level metrics dominated by win/loss outcomes offer little signal beyond mean comparisons, whereas process-level metrics such as move efficiency reveal genuine behavioral differences. Applied to a commercial match-3 game, it uncovers patterns invisible to aggregate metrics: a playtesting bot is diverging substantially from humans in certain game modes, while showing no detectable divergence in others. We release our implementation as open source to support reproducibility and adoption.

---


### 168. [Detecting Formation-Preserving GNSS Spoofing of UAV Swarms through Transmitter Parallax in Pseudorange and Doppler](https://arxiv.org/abs/2611.26023)

**<font color=#1a73e8>作者：</font>** Minseok Park, Joon Soo Yoo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Swarms of unmanned aerial vehicles (UAVs) detect Global Navigation Satellite System (GNSS) spoofing by checking the drones' reported positions against their known formation. Formation-preserving spoofing evades this check: in GNSS-WASP, one transmitter per satellite, a few kilometres away, shifts the whole swarm while keeping its formation. We show that such an attack still leaves a trace below the position level. Because the transmitters are close, each drone sees them under a slightly different angle, and this parallax bends the signal arrival times across a 90 m swarm by 20-40 cm for a transmitter at 5 km, whatever delays the attacker applies. We propose a likelihood ratio test that reads this trace from the pseudoranges and Doppler every drone already measures, with all clocks and attacker delays unknown and no extra antennas. In simulations with real GPS and Galileo orbits and white receiver noise, 16 drones detect GNSS-WASP at 5 km in 13-60% of 10 s windows in straight flight and in every window during a formation turn with a precise Doppler receiver, where the countermeasure proposed with GNSS-WASP detects at most 5%. The same test also catches single-transmitter and ground-array spoofing.

---


### 169. [Serialization Tax in Shared-Latent Exchangeable Decisions](https://arxiv.org/abs/2611.26029)

**<font color=#1a73e8>作者：</font>** Siming Zhang, Zhehui Shen, Shijie Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate item probabilities can produce inaccurate group-level decisions. A system may score each item separately, yet act on whether enough hidden items succeed: show a slate, defer a panel decision, or inspect a batch. When items share an uncertain latent state, independent marginalization preserves means but removes dependence from the aggregate posterior. We call this error the serialization tax. For binary items sharing one success rate, classical convex-order comparisons give a more dispersed exact count law than any independent completion with the same total mean. We quantify variance and total-variation gaps, derive threshold separation under margin conditions, and connect posterior approximation to decision regret. Separate results cover non-binary outcomes, heterogeneous items, and sufficient posterior resolution. TaxScore identifies large hidden blocks with unresolved uncertainty near a decision boundary for routing to richer posterior heads. On pre-specified, hidden-target-free MovieLens 1M/10M audits, existing shared-latent heads improve high-score negative log-likelihood (NLL)/utility from 0.673/0.696 to 0.629/0.723 and from 0.670/0.691 to 0.639/0.715. Routing gives 0.006--0.012 full-population utility gains, with matched controls identifying their sources. Our code is available at this https URL.

---


### 170. [The Delayed Societal Cost of Unfairness](https://arxiv.org/abs/2611.26030)

**<font color=#1a73e8>作者：</font>** Giovani Valdrighi, Isabel Valera, Marcos Medeiros Raimundo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fair machine learning typically evaluates the societal costs of a decision policy -- the loss incurred by the decision-maker (DM) and the unfair distribution of costs among demographic groups of decision-subjects (DS) -- on static data, where reducing one often comes at the expense of the other. Yet decisions change the populations on which they act, and prior work has shown that fairness interventions designed on static data may fail to benefit, or even harm, the disadvantaged group over time. We investigate a complementary question: When can a policy that is Pareto-optimal on pre-deployment data be outperformed by a fairer policy once each is evaluated on the population it induces, reducing costs for one stakeholder without increasing them for the other? In a setting where qualification scores evolve in response to binary decisions and their outcomes, we show that under Rawlsian fairness, which never lowers any group's acceptance rate, placing sufficiently high weight on fairness reduces societal costs whenever accepting disadvantaged DS at the DM's break-even point leaves them in a state less costly to the DM than rejecting them. Under egalitarian fairness, which may lower the advantaged group's acceptance rate, this additionally requires the reduction in DM loss on the disadvantaged group to outweigh the increase on the advantaged group. Under both fairness notions, however, when DM loss is accuracy-based, improvements in the post-deployment population may arise from declining DS qualification, revealing that gains for the DM do not necessarily translate into better outcomes for DS. Our results show that policy-induced population dynamics can overturn apparent performance-fairness trade-offs, allowing fairer policies to reduce the delayed societal costs of decision-making.

---


### 171. [Fixing the Twin, Not the Detector: Sim-to-Real Roadside LiDAR Detection from Digital-Twin Data](https://arxiv.org/abs/2611.26035)

**<font color=#1a73e8>作者：</font>** KuanLin Chen, Feng-jui Kuo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Roadside LiDAR detectors are expensive to train on real labels, and digital twins promise to replace these labels, but a detector trained on a twin meets a different sensor, different objects and different annotation conventions on the real site. We describe the pipeline that placed first in the LUMPI track of the UrbanTwin Sim2Real LiDAR Challenge (IEEE BigData 2026 Cup, 0.5541 combined score) and fifth on its V2X-Real track (0.8102). Every detector is a CenterPoint model trained only on synthetic data, on a single 8 GB laptop GPU. Most of the gain came from correcting differences between the twin and the real site rather than from the detector. We align the twin's coordinates, point density and box convention with the test sensor, generate the pedestrians and riders that the twins lack, plus street clutter as unlabeled negatives, and rebuild twin objects at real size and real point density. A non-learned resampling to the per-cell point density of unlabeled real frames lifts LUMPI realism from 0.589 to 0.947, against 0.949 between real frames. Label-free post-processing then exploits what a fixed roadside sensor guarantees: static structures recur in every frame, and real objects have characteristic point statistics. Reporting the validation and test gain of each component side by side, we find that corrections of systematic sim-to-real differences transfer to the test set, typically keeping a quarter to three quarters of their validation gain, while choices that fit the few objects of a validation set do not.

---


### 172. [Presenting Your Figures: Data-informed Animated Transitions Across Scientific Figure Panels](https://arxiv.org/abs/2611.26036)

**<font color=#1a73e8>作者：</font>** Lu Ying, Can Liu, Yuxiao Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multi-panel figures are commonly used in research papers to show scientific data, and researchers often reuse them when presenting their work. Presenting these figures often involves explaining how data across chart panels are related. Animated transitions can progressively reveal these relationships, but two static panels specify only the endpoints, leaving what intermediate keyframes should show and how the transition should progress unclear. To support transition design across diverse scientific figures, we developed Figure Space and Transition Space through iterative analysis of 48 published multi-panel figures across eight scientific subject areas. Figure Space represents panel composition, data transformations, and visual encodings while retaining the links needed to trace panel results back to records. Transition Space uses this representation and source data to construct and sequence keyframes that make corresponding data visible and align them while preserving the meaning of each panel's position encodings. Building on these spaces, we developed FigFlux, a human-in-the-loop authoring system that guides AI agents in generating animated transitions from a multi-panel figure and its associated materials. Researchers can revise keyframes in natural language before animation generation. We evaluate FigFlux through cross-domain case studies, a study with 16 scientific authors, and expert assessment. Authors reported lower overall workload than with their familiar tools, while experts gave FigFlux transitions higher ratings than transitions created with participants' familiar tools or generated by AI alone. The example gallery have been published online: this https URL.

---


### 173. [Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency](https://arxiv.org/abs/2611.26040)

**<font color=#1a73e8>作者：</font>** Zhihao Hu, Jianqi Ma, Jun Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable streaming video generation offers a promising route toward interactive game simulation, yet existing methods remain far from practical gameplay. They often fail to jointly achieve high visual fidelity, high frame rates, and low interaction latency, resulting in poor responsiveness and degraded user experience. We present Streaming-AAA, a new paradigm for controllable infinite generation of AAA-quality game videos. Our system generates 1080p gameplay videos at 43 FPS with 198 ms end-to-end latency interaction on merely NVIDIA A800 GPUs, while supporting long-horizon play without severe temporal degradation or collapse. Streaming-AAA is built upon three key designs. First, we redesign the VAE architecture for efficient high-resolution decoding, enabling real-time synthesis at 1080p. Second, we pretrain the diffusion model using diffusion forcing and significantly extend the temporal training horizon, allowing the model to capture long-term dependencies and maintain persistent memory. Third, we perform post-training distillation and memory compression to improve inference efficiency while retaining visual quality and temporal consistency. Experiments show that Streaming-AAA substantially improves visual fidelity, frame rate, latency, and long-term stability over prior controllable video generation approaches, enabling a significantly more playable experience for interactive AAA game video generation.

---


### 174. [PaveSplat: Resolution-Robust Feed-Forward Gaussian Splatting with Residually Corrected Surface-Aligned Covariances](https://arxiv.org/abs/2611.26045)

**<font color=#1a73e8>作者：</font>** Janghun Kim, Hyun-Cheol Kim, Eunbin An 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PaveSplat, a feed-forward Gaussian splatting method that adds a learned residual to the analytic surface-aligned covariance, keeping surfels paving the visible surface across rendering resolutions. Pixel-aligned feed-forward Gaussian splatting predicts one primitive per pixel from a few images in a single pass, and its rendering quality depends on how well these primitives cover the surface. Recent surfel-based methods compute the surface-aligned covariance analytically from predicted depth. However, this covariance has no way to correct the surfel orientation where the depth-derived frame is ill-posed. The surfels then cover the surface loosely; at the training resolution each surfel's one-pixel minimum footprint covers the gaps, but they show up as holes when the same prediction is re-rendered at a higher resolution. To address this, we keep the analytic covariance as an initialization, with its axes aligned to the surface tangents, and add an identity-initialized unit-quaternion residual that reorients a surfel only where this improves rendering, turning surfels that the analytic frame mis-aims back onto the surface. On RealEstate10K, PaveSplat achieves the best PSNR, SSIM, and LPIPS among single-Gaussian-per-pixel methods at every scale (1x-8x). The native-resolution gain is small; the benefit appears when the same prediction is rendered at higher display resolutions without re-running the network. On zero-shot DL3DV, it leads PSNR within this group at every scale and ranks first or second on SSIM/LPIPS. A coverage-hole analysis shows fewer uncovered pixels than both baselines under high-resolution re-rendering.

---


### 175. [Studying AI Act Mentions: A first look at the impact of the European Union's AI regulation on Hugging Face](https://arxiv.org/abs/2611.26050)

**<font color=#1a73e8>作者：</font>** Anamaria Mojica-Hanke, Tessi Aigbovbiosa-Igbinovia, Steffen Herbold  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The European Union's Artificial Intelligence Act (AI Act) entered into force in August 2024, and its obligations apply in stages. Obligations for providers of general-purpose AI models have applied since August 2025, and transparency rules since August 2026. These obligations affect developers who share and deploy models and applications on public platforms such as Hugging Face (HF), the largest platform for distributing AI artifacts. However, little is known about how practitioners respond to the regulation in practice. To address this gap, we conducted an empirical study of explicit references to the AI Act on HF. We collected over five million records, including repository cards, discussions, and commits from Models, Datasets, and Spaces, and identified over 1,500 records that explicitly mention the Act. Two coders manually labeled these records using a primarily closed coding approach, and we analyzed the resulting categories per source. We find that explicit references to the AI Act remain rare across all repository types. Repository cards mainly contain claims of compliance and responsibility, like ensuring compliance or assigning responsibility to downstream users, and some claim that the Act does not apply because the model is not a general-purpose AI model. Discussions are used to report alleged violations of the Act, while commits mainly update artifacts that support compliance. Overall, compliance statements focus on who is responsible rather than how compliance is achieved. We believe that this calls for direct platform support, e.g., automated checks and documentation templates, as well as clearer guidance on the scope of the AI Act.

---


### 176. [When Do Rankings Beat Signs? Gradient Direction Recovery under Even Nuisance](https://arxiv.org/abs/2611.26055)

**<font color=#1a73e8>作者：</font>** Zhuangzhuang Pan, Yan Xia, Chee Seng Chan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can ranking a batch of antipodal query pairs recover a gradient direction with fewer evaluations than using within-pair signs alone? We study fixed-center recovery in $d$ dimensions for a linear signal plus an unknown differentiable even nuisance, counting function evaluations and feedback rounds separately. Shared pair offsets create an information hierarchy: Mirror retains within-pair signs, Reverse couples reversed cross-pair orders to cancel offsets, and Full enforces all ranking inequalities. Relative shell variation is the nuisance range over the query sphere normalized by the linear-signal scale. When it is at most $c\varepsilon/\sqrt{d}$, Reverse localizes every consistent direction to angular accuracy $\varepsilon$ using $\widetilde{O}(d+\sqrt{d/\varepsilon})$ evaluations in one round at fixed confidence, without a variation bound supplied to the decoder. This matches a lower bound up to logarithmic factors, versus the $\Theta(d/\varepsilon)$ one-round sign-only minimax cost on the same class. Over well-conditioned positive-definite quadratics with no common relative-curvature bound, the $R$-round minimax cost is instead $\Theta(dR(\varepsilon^{-1/R}-1))$, even with cumulative rankings. We extend validity beyond exact evenness under supplied error bounds. Matched-endpoint experiments certify information beyond signs and short cycles. On two ridge tasks under joint evaluation and round caps, short-cycle recovery attains lower terminal mean gaps than the tested batch-capable controls. An additional optimization benefit from fitting the complete ranking remains unestablished.

---


### 177. [Less Than Meets the Eye: Action-Set Identifiability and Principled Abstention for 3D Physical Geometry](https://arxiv.org/abs/2611.26056)

**<font color=#1a73e8>作者：</font>** Reshad Ul Karim, Abrar Samin, Sammam Mahdi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A corridor, its mirror reflection, and its image on a display can look identical, yet their physical surfaces lie at different depths. We test whether bounded camera motions distinguish these explanations. Intervene3D takes an image and an initial geometry estimate, predicts the view under each hypothesis and candidate motion, and selects a motion by maximin separability. It reports the mechanism and first physical surface only if the available motions separate the hypotheses still in contention. Otherwise it abstains. An adequacy test also rejects observations that no hypothesis explains. On a matched synthetic benchmark with exact landmarks, disabling abstention gives confident answers on 76.4% of unresolvable scenes. With abstention, none receives a confident answer under exact or noisy landmarks. At 100% accuracy on answered scenes, maximin selection answers 61.0% of scenes and summed selection 43.1%. The adequacy test lowers wrong answers on strongly curved mirror scenes from 56.8% to 12.4%. Real display experiments compare two hypotheses using one frozen depth-network estimate. The second image supplies photometric evidence and is never passed through the depth network. One executed motion reduces the pooled median surface error of twelve networks by 31.5%. These networks have larger error inside the annotated panel than outside on 33.4% of illusion-benchmark images. They place the first physical surface behind the glass on 36.9% of Mirror3D frames.

---


### 178. [One-to-Many: Diverse and Bidirectional Image-to-Image Translation via Rectified Flow](https://arxiv.org/abs/2611.26058)

**<font color=#1a73e8>作者：</font>** Sho Shimotsumagari, Seiichi Uchida, Shumpei Takezaki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many paired image-to-image translation tasks admit multiple valid target appearances, while training provides only one target per source. We propose One-to-Many Flow (O2MFlow), a latent-conditioned Rectified Flow (RF) model for one-to-many generation and backward translation (target$\rightarrow$source) within a single transport framework. Conditioning the RF dynamics on an appearance latent turns transport into a family of latent-indexed bijections: a fixed latent gives a mapping that is inverted by time-reversed integration, and sampled latents produce diverse outputs for the same input. We formalize reusable appearance variations as Shared Latent Transport and show that Kullback--Leibler (KL) regularization directly controls the source--latent distribution gap between training and generation. Across three benchmarks, O2MFlow offers dataset-dependent forward diversity--fidelity trade-offs and the lowest backward LPIPS-Dist among evaluated methods, with the lowest backward FID on two benchmarks.

---


### 179. [Iterative Scarcity-Guided Exploration: Bootstrapping Generative Auto-bidding from Narrow Support](https://arxiv.org/abs/2611.26060)

**<font color=#1a73e8>作者：</font>** Qingmao Yao, Guangzheng Hu, Yusen Huo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auto-bidding is a core algorithmic component in online advertising auctions. In practical cold-start settings, iterative training is commonly used to compensate for low-quality, narrowly supported historical data. Unfortunately, in iterative training, representative diffusion-based AI-Generated Bidding (AIGB) methods fail to sustain extrapolation beyond the narrow data support and stagnate at a suboptimal level. In this paper, we theoretically attribute this stagnation to Signal-to-Noise Ratio (SNR) collapse: the weak radial return signal is overwhelmed by a curvature-induced penalty. To break this stagnation, we propose \textbf{Iterative Scarcity-Guided Exploration (ISGE)}, which introduces a guidance handoff: as the return signal collapses, scarcity subsequently takes over as an exploratory signal to elevate the SNR above a critical threshold. Specifically, ISGE iteratively alternates between a \emph{Judger} that assigns scarcity scores to trajectories and an \emph{Explorer} that performs guided generation of high-scarcity and high-return trajectories, thereby bootstrapping from the narrow support with such self-generated trajectories. Extensive experiments on the industrial AuctionNet benchmark demonstrate that ISGE, starting from cold-start datasets, effectively surpasses the performance of the Full-Dataset baseline within three iterations. Code is available at this https URL

---


### 180. [Domain-Aware Conformal Prediction for Trustworthy Spacecraft Pose Estimation under Sim-to-Real Shift](https://arxiv.org/abs/2611.26065)

**<font color=#1a73e8>作者：</font>** Nidhal Eddine Chenni, Arunkumar Rathinam, Djamila Aouada  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous rendezvous and proximity operations require not only an accurate estimate of the pose of the target spacecraft, but also a reliable indication of when this estimate can be trusted. Conformal prediction provides such an indication with a formal guarantee, by producing pose uncertainty sets that contain the true pose with a specified probability. Such a guarantee, however, assumes that calibration and test data follow the same distribution, an assumption that is violated in orbital perception, where labelled calibration images are available only from synthetic renderings while operational images are real. In this work, we show on the SPEED+ dataset that conformal pose estimation calibrated on synthetic images loses its coverage guarantee on real images, and that many of the resulting failures are silent: the predicted pose set appears valid but excludes the true pose. To address this, we calibrate on synthetic images translated to the appearance of real images. Since translation alters appearance while preserving geometry, the synthetic pose labels remain valid and no labelled real images are required. Experiments with two translation models show that this calibration restores coverage above the specified level for miscoverage levels of 0.1 and above, and reduces silent failures from up to 43.5% to at most 3.3% of the test images, bringing conformal pose estimation a step closer to trustworthy deployment in space.

---


### 181. [DfD-GS: Defocus Image Prior for Metric-Scale Single-View Depth Estimation and View Synthesis](https://arxiv.org/abs/2611.26072)

**<font color=#1a73e8>作者：</font>** Shiori Ueda, Rinto Yagawa, Hideo Saito 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering metric-scale geometry from observations at a single viewpoint remains fundamentally ill-posed, limiting the reliability of novel view synthesis. Recent methods rely on learned monocular depth priors, which provide strong structural estimates but can suffer from scale ambiguity and dataset-dependent biases. We propose DfD-GS, a feed-forward framework that predicts a metric-scale 3D Gaussian scene representation from a single-view all-in-focus--defocused image pair. The key idea is to exploit defocus blur as a physical metric depth cue. DfD-GS first estimates a defocus-based metric disparity map from the all-in-focus--defocused image pair and the corresponding defocus strength. This estimate is used to align and refine a monocular depth prior to metric scale. Visible and hidden 3D Gaussians are then predicted for occlusion-aware novel view synthesis. Experiments on synthetic-defocus datasets constructed from Booster and Middlebury show that DfD-GS outperforms single-image baselines in metric depth estimation and novel view synthesis. On WildRGB-D, DfD-GS achieves lower AbsRel and LPIPS but higher depth RMSE than the single-image baselines. Additional analyses show that DfD-GS maintains a more stable metric scale under field-of-view changes. Qualitative results on a real dataset show recovery of the main scene structure under optical defocus.

---


### 182. [Controlling the Humanoid Robot H1-2 With a Simulated Biologically Plausible Network](https://arxiv.org/abs/2611.26074)

**<font color=#1a73e8>作者：</font>** Fatima Atwi, Constant Roux, Christian Bergaud 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Spiking Neural Networks have gained remarkable attention in the last few years due to their proven ability in simulating biological neural cultures and producing similar activity and trends. Nevertheless, whether they can be trained for humanoid locomotion while retaining biological plausibility and robust performance at once remains an open question. We study this problem by proposing a biologically inspired spiking network, trained by different learning schemes and tested on the H1-2 Unitree Humanoid. These schemes differ in how recurrent weights are trained. Ordered from most to least biologically faithful, they are: a fixed reservoir mimicking an in-vitro neural culture, where recurrent weights are kept frozen and only a linear readout is trained, the same network but with its synapses trained by reward-modulated spike timing dependent plasticity and eligibility propagation, and finally backpropagation through time as a non biological baseline for comparison. All schemes relied on distillation of a reinforcement learning expert policy with dataset aggregation. We show that e-prop reached 100% survival rate matching backpropagation through time, whereas both the fixed reservoir and the reward-modulated STDP, though the closest to biological cultures, plateaued at a much lower performance (~43.7% and ~11% survival). We explore in further detail which trends a real culture could and could not produce until now. Finally we demonstrate brief bipedal stepping on a full size humanoid H1-2.

---


### 183. [Learning to Compare Neural Representations from Parameterized Computation Graphs](https://arxiv.org/abs/2611.26081)

**<font color=#1a73e8>作者：</font>** Ya-Wei Eileen Lin, Daniel Herbst, Stefanie Jegelka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Comparing internal representations across trained models is important for identifying corresponding layers and selecting components for model reuse. Yet, direct comparisons at inference require evaluating candidate models on known reference inputs and collecting their internal activations. In this paper, we study whether internal representation similarity measured across independently trained models can instead be learned to predict in unseen models from their parameterized computations. We introduce a framework that applies a graph metanetwork for mapping each internal site to an embedding derived from its upstream computations while accounting for hidden-coordinate permutation and internal attention-basis transformations. We analyze the structural properties of our estimators and derive conditional guarantees for layer retrieval and stitching candidate selection. Empirically, we find that the learned predictors support relation estimation and low-regret layer retrieval. They also select useful stitching connections while not being trained on stitching outcomes. This opens up a new way to study representation similarity directly from trained neural networks: representational relations learned across a collection of trained models can generalize to new computations, and that the predicted relations can guide candidate selection before direct measurement or adapter fitting for functional evaluations.

---


### 184. [Phantom of the Masquerade: Graph Neural Network-Based Detection of Masquerade Attacks in Controller Area Networks](https://arxiv.org/abs/2611.26094)

**<font color=#1a73e8>作者：</font>** Nehal Ameen, Pablo Moriano, Irfan Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The lack of built-in security in controller area networks (CANs) exposes modern vehicles and industrial systems to masquerade attacks that can compromise safety and reliability. These attacks inject malicious messages that mimic legitimate communication patterns, making them difficult to detect using existing intrusion detection systems (IDS). Prior graph-based IDS approaches often rely on shallow embeddings that decouple representation learning from classification, which may limit their ability to fully exploit structural and signal-level information. In this paper, we propose PhantoMasq, a graph neural network (GNN)-based framework for detecting masquerade attacks in CAN systems. PhantoMasq models CAN traffic as message sequence graphs enriched with lightweight statistical features derived from signal behavior, enabling joint learning of structural dependencies and temporal characteristics. The detection task is formulated as a graph-level classification problem and solved using graph convolutional networks (GCNs). We evaluate PhantoMasq on the ROAD dataset under a protocol that prevents overlapping windows from spanning training and test data. Across five masquerade attack types, PhantoMasq achieves mean AUC-ROC between 0.831 and 0.999, with performance depending on the transmission rate of the targeted identifier and the magnitude of the induced signal deviation. Against a state-of-the-art graph-embedding baseline evaluated on the same sliding-window configurations, PhantoMasq achieves higher AUC-ROC on all five attack types, by 0.13 to 0.36, and is less sensitive to window configuration. Window-processing latency ranges from 2.33 to 5.94 ms per window on CPU, corresponding to a throughput of 168 to 429 windows per second. We make our implementation and experimental artifacts available to support reproducibility.

---


### 185. [Approximate Adjoint Models for Memory and Compute-Efficient Online Learning of Hybrid Models](https://arxiv.org/abs/2611.26095)

**<font color=#1a73e8>作者：</font>** Emilio González-Zamora, Pierre Tandeo, Laurent Debreu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentiable programming enables online calibration of numerical models by minimizing errors accumulated along simulated trajectories. This includes estimating physical parameters and training neural sub-models in hybrid configurations. Gradients are typically computed using adjoint methods, or backpropagation through time (BPTT), whose computational and memory costs grow with the length of the training window. This limits the duration and resolution of hybrid-model training, a major bottleneck for realistic geophysical applications. Approaches like truncated BPTT reduces memory use by discarding sensitivities across truncation boundaries, introducing gradient bias and neglecting long-range dependencies. We propose a class of gradient approximation methods that preserve the adjoint recurrence over the full trajectory while approximating only the pullback operators within it. Exact pullbacks are computed by automatic differentiation at sparse anchor states only. Between anchors, sensitivities propagate either through the identity (Zero-order) or through a reused, frozen pullback (Pullback Reuse). This approximation makes the parameter pullback constant within each chunk, allowing the gradient sum to factorize so that a single evaluation per chunk replaces one per time step. We evaluate both on three systems of increasing complexity, an incomplete Lorenz-63 model, a large-eddy closure for two-dimensional quasi-geostrophic turbulence, and bias correction in a multilayer quasi-geostrophic ocean model. Peak memory falls by up to an order of magnitude and runtime up to fourfold, with Pullback Reuse staying closest to the exact gradient direction. In all three cases, approximate gradients support hybrid-model training at comparable accuracy, showing that effective online learning does not require exact gradients.

---


### 186. [Frequency-Synchronized Boundary Coupling for Training-Free Multi-Prompt Long Video Generation](https://arxiv.org/abs/2611.26098)

**<font color=#1a73e8>作者：</font>** Yipan Xu, Shuyong Gao, Jiyuan Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video generation has made remarkable progress with diffusion models and transformer-based video architectures, yet generating coherent long videos from evolving textual descriptions remains challenging. Training long-video models from scratch requires substantial computation and large-scale multi-event data, while training-free multi-prompt generation must activate new prompt semantics without breaking temporal continuity. We identify a frequency-agnostic boundary coupling problem in existing transition strategies: weak coupling causes abrupt changes, flicker, and background jumps, whereas overly strong or coarse coupling may over-preserve source semantics and produce ghosting or duplicated subjects around prompt boundaries. To address this problem, we propose FreqSync, a training-free framework that formulates prompt transitions as frequency-selective boundary coupling. FreqSync combines Frequency-Synchronized Source-Conditioned Attention (FS-SCA) with Residual-Clipped Spectral Stitching (RCSS), enabling adjacent segments to share stable low- and mid-frequency structure and motion cues while keeping high-frequency prompt-specific details target-dominant under explicit residual constraints. Extensive experiments show that FreqSync achieves state-of-the-art transition smoothness and prompt alignment while maintaining strong perceptual video quality, demonstrating its effectiveness for coherent multi-prompt long video generation.

---


### 187. [Causal Overtaking in Fair Transaction Ordering](https://arxiv.org/abs/2611.26100)

**<font color=#1a73e8>作者：</font>** Haozhe Feng, Di Wu, Jian Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fair transaction ordering protocols aim to mitigate front-running using replica-local arrival orders, but prior work often assumes a single submission origin for each responsive transaction. We identify causal overtaking, in which corrupted replicas observe a target and submit identical signed copies of a responsive transaction through multiple client entries. The copies' first arrivals at different replicas can collectively provide ordering support that no individual path achieves, allowing the response to execute before its target. We formalize a class of receipt-order protocols, including Themis, characterize the timing and network conditions under which the attack is feasible, and show that delayed gossip does not rule it out. We further prove that, under our network model, histories requiring opposite transaction orders can produce identical receipt evidence. Thus, receipt-only mechanisms cannot always preserve earlier-submission priority while preventing responsive overtaking. We propose a mitigation and analyze its assumptions and limitations. Finally, we evaluate the attack and mitigation on Themis through simulations driven by AWS and WonderProxy latency measurements.

---


### 188. [Revealing Pathway Interactions in Network Computations with Complete Path Contribution](https://arxiv.org/abs/2611.26101)

**<font color=#1a73e8>作者：</font>** Shenghua Liu, Youssef Faragalla, Surya Ganguli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Networks pass signals through many layers of interconnected units, so explaining what they compute means tracing how information travels from input to output and how pathways interact. Most existing approaches analyze only pairwise interactions between components such as units, layers or attention heads. Even when these measurements are combined post hoc into a circuit, they do not capture higher-order interactions along full causal chains (paths) from input to output, and so cannot address how exponentially many paths interact to construct network computation. This leaves a large set of mechanistic questions unanswerable, for example whether inhibitory pathways veto excitatory ones, and how the two combine to yield network decisions. To address this gap, we introduce Complete Path Contribution, a method to decompose the network output into mathematically complete contributions of individual paths to study path-level interactions directly and at scale. Partial summation then induces definitions of contributions for any circuit at any granularity level, with completeness guaranteed at every level. We further present an efficient algorithm that identifies the $k$ strongest paths without examining all of them, with runtime empirically linear in $k$ rather than exponential in depth. By applying Path Contribution to benchmark image classification networks, we quantify excitatory-inhibitory interactions and show how they collectively construct network decisions at a level of detail previously unmeasurable. Furthermore, in an interpretable model of the mouse retina, it reveals how dynamic receptive fields emerge from excitatory-inhibitory interaction motifs among pathways between different cell types in response to time-varying natural stimuli. Overall, Path Contribution reveals how a network's causal pathways interact at scale to transform input to output.

---


### 189. [How Network Topology and Data Heterogeneity Shape Decentralized Learning: A Spectral Analysis](https://arxiv.org/abs/2611.26104)

**<font color=#1a73e8>作者：</font>** Luigi Palmieri, Lorenzo Valerio, Chiara Boldrini 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Network topology influences decentralized federated learning through information mixing and the relative contribution of individual nodes. While existing analyses primarily focus on spectral mixing properties, they often assume doubly stochastic aggregation, overlooking topology-dependent influence under irregular communication networks. We develop a spectral framework that separates two complementary mechanisms: the dominant eigenmode determines the consensus trajectory and node influence, while non-dominant eigenmodes govern the propagation and attenuation of disagreement. Under uniform neighborhood averaging, we show that the stationary influence is proportional to node degree plus one and derive a bound relating model disagreement to spectral mixing and gradient heterogeneity. We then investigate how these mechanisms interact with the data distribution across nodes. Experiments across regular and heterogeneous network topologies reveal nearly identical learning dynamics under IID data, while network size and connectivity affect how unevenly distributed information is learned under non-IID data. For non-IID settings, we characterize how the distribution of data across nodes shapes the relative contribution of local information to consensus dynamics.

---


### 190. [Pareto-Optimal and Strategyproof Data-Sharing Between Competitors](https://arxiv.org/abs/2611.26108)

**<font color=#1a73e8>作者：</font>** Morgan Colin-Mourre, Felipe Garrido-Lucero, Patrick Loiseau  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study data-sharing among firms competing in the same market through the quality of their predictive models. We model firms' profit through two main components, precision and market share, where the former depends on the firm's own number of datapoints and the latter depends on the endowments of all firms. We characterize Pareto-optimal contracts as those in which at least one firm receives all of the other firms' datapoints. We then propose a parametric family of data-sharing contracts and show that, under any of them, the relative market shares of all firms remain constant, eliminating the negative effect of sharing data with competitors and equalizing all firms' gains relative to the no-sharing scenario. We further show that one contract within this family satisfies both Pareto-optimality and strategyproofness against firms attempting to under-declare the size of their initial endowment. Finally, using a real-world dataset, we empirically test the gain in profit for all firms under the contract described above, and show that data-sharing is particularly beneficial when the machine learning task is harder or when firms' initial endowments are closer to homogeneous.

---


### 191. [SenseAlign: Learning Decision-Aligned Predictive Representations for Active Urban Sensing with UAVs](https://arxiv.org/abs/2611.26109)

**<font color=#1a73e8>作者：</font>** Weijiang Xiong, Nikolas Geroliminis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Active urban sensing orchestrates a mobile sensor fleet to proactively inspect a dynamic road network and gather critical information for system management. This problem simultaneously requires understanding the complex spatio-temporal evolution and making decisions with partial observations. In this work, we focus on active sensing in a large-scale urban road network with utilities grounded in dynamic traffic states, while prior work has rarely considered these factors jointly. We propose \emph{SenseAlign}, a Reinforcement Learning-based (RL) framework that learns decision-aligned predictive representations for coordinating an urban sensing drone fleet. SenseAlign first trains a privileged teacher agent that exploits future ground-truth traffic for optimal sensing choices. The student agent has an auxiliary branch that learns to predict future traffic with partial observations, in addition to the RL-trained actor and critic branches. During student learning, our framework matches the action distributions of the teacher under ground-truth and student-predicted future traffic, while keeping the teacher's observations unchanged. Such a design shapes the latent space for decision-making instead of prediction alone. At inference time, the student agent has no overhead as all this learning is done in training. We conduct comprehensive experiments with the real road network of central Barcelona containing 1570 road segments, and demonstrate that our method consistently outperforms the baselines on multiple utility formulations. The codebase will be made publicly available upon paper acceptance.

---


### 192. [Loss-Guided Tsetlin Machines: Making the Learning Objective Explicit](https://arxiv.org/abs/2611.26114)

**<font color=#1a73e8>作者：</font>** Mayur Shende, Runar Helin, Ole-Christoffer Granmo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Tsetlin Machine (TM) has no explicit notion of a loss function. Its learning signal is fixed to an implicit, margin-based update rule (MBUR), with no way to choose an objective function suited to a specific task. This paper introduces Loss-Guided TM, which replaces MBUR with an explicit and swappable loss function. In our proposed method, clause feedback and weight updates are driven by the loss, while keeping the Tsetlin Automaton and clause logic unchanged. The approach incorporates cross entropy (CE), symmetric cross entropy (SCE), and asymmetric loss (ASL). We evaluate Loss-Guided TM across six datasets that span multiclass, multilabel, and binary classification tasks. With a suitable loss, Loss-Guided TM matches or improves accuracy and F1 over MBUR on five of the six datasets. The gains are greatest for the imbalanced multilabel datasets, where ASL improves macro F1 by up to 9 percentage points. With CE, Loss-Guided TM is also significantly better calibrated than MBUR on all six datasets, reducing calibration error by a factor of 3 to 11. A qualitative inspection shows that the clause-based global interpretability, examined at the per-class level on image and text data, is preserved when using the Loss-Guided mechanism. These results show that our explicit TM learning objective allows direct targeting of uncertainty calibration, data imbalance, and task structure, opening the TM to the broader literature on loss functions.

---


### 193. [Learning Reconstruction Errors as Spatiotemporal Evidence for AI-Generated Video Detection](https://arxiv.org/abs/2611.26116)

**<font color=#1a73e8>作者：</font>** Jiahua Jiang, Jinglai Li, Jianru Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The proliferation of AI-generated videos has raised growing concerns about misinformation, fraud, and potential societal risks, creating an urgent need for detection. Reconstruction-error-based methods have shown strong empirical performance for AI-generated image detection by exploiting discrepancies between an input and its reconstructed version. Their extension to video detection, however, faces two challenges: (i) a fixed reconstructor is not optimized for the detection objective and may yield weak discriminative signals; and (ii) an additional raw-video feature stream is often introduced to model temporal dependencies, increasing architectural overhead. To address these challenges, we develop a detector that learns and exploits reconstruction errors as a unified source of spatiotemporal evidence. First, we jointly optimize a reconstructor and the downstream classifier to produce reconstruction errors that are more informative for detecting AI-generated videos. Second, we show that consecutive reconstruction errors alone carry temporal evidence, and thus a 3D convolution over them captures spatiotemporal evidence without a raw-video stream. Extensive experiments on over 30 existing AI-video generators demonstrate competitive performance against baselines.

---


### 194. [CryoGaussian: Heterogeneous Cryo-EM Reconstruction Made Explicit with Gaussian Splatting](https://arxiv.org/abs/2611.26128)

**<font color=#1a73e8>作者：</font>** Ziwen Wang, Jiajun Fan, Chaoran Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-particle cryo-electron microscopy (cryo-EM) determines macromolecular structures from noisy particle images. However, rare, transient compositional states and subtle, continuous conformational variation are difficult to resolve. We present CryoGaussian, a Gaussian splatting method for heterogeneous cryo-EM reconstruction that fits an explicit Gaussian density representation directly to the particle images through a differentiable rasterizer rendering orthographic line integrals modulated by the contrast transfer function. The Gaussians are initialized randomly, with their number derived from the estimated spatial support of the molecular density and their minimum size bounded by the Nyquist frequency of the particle images. To capture the compositional and conformational variation across particle images, we learn particle-image and per-Gaussian latents that jointly modulate the base position, amplitude, and scale of each Gaussian. Each structural state is then reconstructed by fitting the Gaussians conditioned on its inferred latent. On CryoBench, CryoGaussian achieves state-of-the-art reconstruction accuracy for both compositional and conformational heterogeneity. On experimental data, it resolves a rare compositional state of the 50S ribosomal subunit (class C4, 1.3% of particles) with rRNA helix 68 docked in the absence of the central protuberance, and continuous conformational motion of the SF3b and helicase subcomplexes of the pre-catalytic spliceosome. We further optimize the rasterizer for additive cryo-EM projection, reducing training time by 12.8-28.0$\times$.

---


### 195. [Sage-Evolve-Preview:Adaptive Observation for Post-Training Self-Improvement](https://arxiv.org/abs/2611.26132)

**<font color=#1a73e8>作者：</font>** Yinhao Tang, Youqing Fang, Yanan Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training recursive self-improvement (RSI) iteratively improves a target capability, operationalized by a fixed anchor benchmark, through repeated intervention, training, and evaluation. Yet most loops use the anchor's aggregate score as their sole observation, so early gains give way to stalled progress and repetitive exploration. When this anchor-only feedback ceases to reveal actionable gaps, a plateau may reflect an exhausted observation rather than an exhausted capability. We introduce adaptive observation (AdaObs), an observation-side mechanism of harness evolution that keeps the anchor objective fixed while adapting the active observation. At a plateau, a controller refines diagnostic granularity, escalates difficulty, and adds related tasks; validated increments are fused back into training, while every checkpoint remains evaluated against the anchor. Across eight independently optimized anchors in long-context reading comprehension and instruction following, AdaObs raises the mean score from $66.4$ to $73.7$ under a matched data budget, outperforming FixedObs, the anchor-only baseline. The evolved harness further improves the seven-task average on the independent PostTrainBench across two agent backends. These results identify observation adaptation as a missing mechanism of harness evolution for sustaining post-training RSI.

---


### 196. [Public-Private Cooperation in the Port of Rotterdam: An Agent-Based Toy Model of Cooperative Efforts Against Cocaine Trafficking](https://arxiv.org/abs/2611.26154)

**<font color=#1a73e8>作者：</font>** Frederike Oetker, Charlotte Geertman  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Cocaine trafficking poses a persistent governance challenge in the Port of Rotterdam (PoR), requiring cooperation between public and private actors. This paper develops an Agent-Based toy Model (ABM) coupled with a Causal Loop Diagram (CLD) to explore interactions between trust, cooperation, competition, pressure, enforcement, and actor skills in public-private cooperation (PPC). Based on empirical data of PPC in the PoR, we explore responses to parameter shocks across different initial configurations. In this model, effectiveness of PPC is strongly state-dependent and measures institutional, relational, behavioral, and resource readiness. The toy model demonstrates that isolated, single-track measures yield limited long-term gains modelled over 5 years due to structural system inertia, whereas coordinated multi-parameter strategies produce substantial improvements. Specifically, combining trust-building, cooperation, and moderate pressure with reduced regulatory enforcement friction raises effectiveness by 25% from a baseline effectiveness, compared to just 13% for an isolated increase in cooperation. Acknowledging the exploratory nature of the model, these findings offer exploratory hypotheses on port security governance. Future work should validate the model against test cases and additional expert input.

---


### 197. [StreamEgo: Streaming Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2611.26165)

**<font color=#1a73e8>作者：</font>** Tianyi Xu, Boyang Lyu, Yunkai Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Exocentric-to-egocentric (Exo2Ego) video generation transforms third-person recordings into first-person viewpoints, unlocking immersive AR/VR experiences and scalable demonstration synthesis for embodied robotics. Extending it to a streaming setting is expected to further enable live applications. However, existing methods suffer from degraded manipulation regions, overfitting and confinement to fixed-length clips with prohibitive latency. To address these limitations, we present StreamEgo, a real-time framework for unbounded, generalizable Exo2Ego video generation. To resolve intricate manipulation dynamics while supporting the streaming pipeline, a streaming dual-branch prior provides pixel-aligned guidance for translating appearance and skeletal kinematics. We also introduce a region-aware loss curriculum to improve generalization and stabilize multi-objective diffusion training. Furthermore, we distill the model into a chunk-wise autoregressive model, augmented with a region-aware corruption mechanism and a first-chunk curriculum, enabling high-quality, generalizable real-time streaming Exo2Ego generation at 24.3 FPS on a single H100 GPU.

---


### 198. [FlexVSR: Continuous-Scale Super-Resolution for Streaming Video Generation](https://arxiv.org/abs/2611.26178)

**<font color=#1a73e8>作者：</font>** Ji Wang, Haonan An, Jiasheng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time streaming video generation has gained rapid momentum in live content creation and interactive media. Deploying such systems in practice requires flexible scaling factors to accommodate diverse source resolutions, target displays, and computational budgets. However, extending fixed-scale generative video super-resolution (VSR) to varying target scales poses two challenges: downsampling from a larger fixed scale incurs redundant cost, while re-optimizing the diffusion transformer (DiT) is costly and alters the shared generative prior. To address both, we propose FlexVSR, a decoupled framework for continuous-scale streaming generative VSR with supervision at only a few scales. Our key insight is that naively resampling fixed-scale latents onto a new target grid induces scale-dependent input mismatch, which can be effectively addressed through parameter-efficient, scale-aware adaptation of the latent interface without updating the DiT. To this end, FlexVSR introduces ReLSA (Refined Latent Scale Adaptation), a lightweight latent adapter that constructs and refines target-grid latents before they enter the DiT, enabling a shared frozen VSR prior to generalize across continuous scales with only 0.274M trainable parameters and an adaptation cost of 7.3 H100 GPU-hours, while introducing no additional temporal dependencies and preserving the native causal streaming protocol. Extensive experiments demonstrate competitive or superior reconstruction and temporal quality, lower latency than most native-scale streaming baselines and offline methods, and effective generalization to unseen continuous scales, filling the continuous-scale gap in real-time streaming generative VSR.

---


### 199. [Thermodynamically Consistent Neural Networks for a Universal Fluid Gibbs Free Energy Equation of State](https://arxiv.org/abs/2611.26183)

**<font color=#1a73e8>作者：</font>** Xurui Li, Zhiguo Gan, Jiaming Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Over the past three centuries, many thermodynamics researchers have worked to develop fluid equations of state with both high accuracy and broad applicability, proposing various theoretical frameworks and models. Building on these efforts, this study uses Gibbs free energy as the starting point and introduces thermodynamically consistent neural networks to construct a fluid equation of state based on Gibbs free energy (GEoS). This approach establishes a novel machine learning framework that provides a unified representation of fluid states. GEoS performs well on the vapor- and liquid-phase density test sets, with average absolute relative deviations (AARDs) of 5.25% and 3.96%, respectively. It outperforms conventional volume-translated cubic equations of state and existing machine learning models, demonstrating its effectiveness. Further analysis using the UMAP dimensionality reduction method shows that most molecules in the test set belong to extrapolation systems, confirming the strong generalization ability of the model. Finally, the test results show that the PC-SAFT equation fitted using GEoS maintains high predictive accuracy, providing a reliable basis for its practical application in industry.

---


### 200. [Invertible Transport Between Sample-Only Distributions via Projected Characteristic Functions](https://arxiv.org/abs/2611.26187)

**<font color=#1a73e8>作者：</font>** Juan Gutiérrez, Victor Gutiérrez-García, José Luis Blanco-Murillo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many useful latent distributions can be sampled but do not have a tractable density. Such distributions may be represented by empirical collections of real-world observations or generated by scientific simulators and black-box generative models. These sample-only priors cannot be used directly in likelihood-based normalizing flows, which require evaluating the prior density. We propose Projected Characteristic-Function matching (PCF), a density-free framework for learning an invertible map between a data distribution and a prior specified only through samples.
Our method aligns distributions using projected empirical characteristic functions, eliminating the need for density estimation, adversarial training, or paired observations. To address the non-uniqueness of the transport map, we introduce an optional transport regularizer that selects lower-displacement transformations while preserving endpoint alignment.
We benchmark PCF on controlled transports, sample-efficiency studies, and high-dimensional alignment tasks. PCF matches the accuracy of kernel MMD on the controlled benchmark and on raw-pixel MNIST--USPS at a cost linear in the batch size, and it is more sample-efficient, achieving lower endpoint error than MMD in 13 of 15 paired runs across library sizes. By avoiding pairwise kernel evaluation, it reduces discrepancy memory by 29.8% and trains at batch sizes where kernel MMD exceeds GPU memory. These results show that PCF provides accurate and efficient invertible transport, particularly in sample- and memory-limited settings.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-265](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

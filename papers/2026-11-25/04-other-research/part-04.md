# 📦 其他研究 | 2026年11月25日

> 本类共 **569** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

---

### 151. [Pretraining Representation Lottery Determines Fine-tuning Generalization](https://arxiv.org/abs/2611.28777)

**<font color=#1a73e8>作者：</font>** Fuming Yang, Core Francisco Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large scale pretraining (PT) followed by fine-tuning (FT) is the central paradigm of modern deep learning, yet how PT shapes FT generalization remains poorly understood. We use a synthetic setup in which the ground-truth concept geometry of entities is known, as a controlled testbed to study how representational geometry affects model behavior and how PT representations determine FT generalization. We first show that models differing only in training seed can closely match in PT loss yet vary substantially in FT generalization. We hypothesize that a representational lottery underlies this phenomenon: the random seed dependent geometry formed during PT determines what FT can reach. We confirm this causally. First, injecting the ground-truth concept geometry into the model yields near-ceiling FT generalization, showing that good representations directly drive generalization. Then, distilling a lucky seed's learned representation into an unlucky seed unlocks FT generalization, while distilling the same model's behavior does not. Furthermore, representation distillation can merge entities that never interacted during PT, which FT alone cannot. Finally, we show that regularizing representational drift during FT enables naturalistic learning: only models with good representations learn the task, and they generalize, while models with poor representations fail to fit it. Under plain FT, by contrast, models with poor representations fit the training objective by reshaping their pretrained representations. We reproduce the distillation result in Pythia-160M and Pythia-410M, each pretrained multiple times with different random seeds, and show that the transferable representation lives in the deep layers at both scales. Overall, PT acts as a lottery over representations, and the representation a model draws determines how it adapts during FT in a way that behavior alone does not explain.

---


### 152. [Imagine Smarter, Drive Faster: Efficient World Modeling for Decision-Aware Autonomous Driving](https://arxiv.org/abs/2611.28779)

**<font color=#1a73e8>作者：</font>** Feiyang Jia, Lin Liu, Zhicheng Bao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models hold great promise for autonomous driving planning, yet their ability to imagine the future often comes at a formidable computational cost. Efficiency efforts, such as knowledge distillation and domain-specific pre-training, often shift this burden to costly teachers or training pipelines, leaving lightweight world modeling an open challenge. We introduce FastWorld, a natively lightweight world-model framework for efficient autonomous driving planning. FastWorld reduces computation through compact scene representations, short-horizon action-conditioned prediction, and selective candidate verification and score refinement. These designs support efficient future-informed planning without teacher distillation or additional domain-specific pre-training. On NAVSIMv1, FastWorld achieves 92.2 PDMS at 132 FPS on a single 4090 GPU. It also achieves 89.4 EPDMS on NAVSIMv2 and an average L2 of 0.40 over 3 seconds at 17 FPS on nuScenes. Code and models can be found at this https URL.

---


### 153. [Joint Client Scheduling and Resource Allocation for Optimal Federated Learning over Wireless Networks](https://arxiv.org/abs/2611.28782)

**<font color=#1a73e8>作者：</font>** Ahmad Dabaja, Rachid El-Azouzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning often relies on partial client participation because full participation is costly in cross-device wireless systems with limited uplink resources, heterogeneous channel conditions, energy constraints, and strict upload deadlines. However, partial participation introduces sampling variance, causing the sampled update to deviate from the full-participation update. Existing optimal client sampling methods reduce this variance but usually rely on simplified client-count budgets, while wireless-aware scheduling methods account for communication constraints but do not directly optimize sampling variance. This paper proposes resource-aware optimal client sampling (RAOCS), a unified variance-minimizing client scheduling framework under uplink resource-block, round deadline, update-information, and energy constraints. The resulting problem admits a capped water-filling solution that balances client update importance, wireless resource cost, and energy feasibility. Experimental results demonstrate that RAOCS achieves accuracy comparable to that of OCS while reducing the average upload time per iteration by more than a factor of 252.

---


### 154. [Reporting Differential Privacy Guarantees via Operationally Equivalent $\varepsilon$: What Does $\varepsilon=19.61$ Mean for the 2020 U.S. Census?](https://arxiv.org/abs/2611.28790)

**<font color=#1a73e8>作者：</font>** Masayuki Terada, Shinsuke Ito, Takumasa Ishioka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The large value $\varepsilon=19.61$, reported as an approximate differential privacy (ADP) parameter for the 2020 U.S. Census, has prompted doubts about the adequacy of Census privacy protection. It was obtained by converting component zero-concentrated differential privacy (zCDP) guarantees to ADP at $\delta=10^{-10}$. A single ADP pair can substantially loosen the original upper bound on the power (true positive rate) of a distinguishing test. At significance level $\alpha$, we express the original bound as the smallest pure differential privacy (DP) parameter giving the same power bound. We call this the $\alpha$-operationally equivalent $\varepsilon$. The full curve represents the original bound exactly on $(0,1)$, even when the bound is nonconcave. For maximum-power curves and bounds derived from trade-off functions, we characterize the extrema of operationally equivalent $\varepsilon$ over an interval of significance levels. When finite, they give the parameters of the pure DP bounds that enclose the original power bound on that interval. The mapping preserves the ordering of power bounds at each significance level. For Laplace and Gaussian mechanisms with equal noise variance, conversion to single ADP pairs or Gaussian DP envelopes can reverse this ordering. For the P.L. 94-171 redistricting data, we reproduce the reported $\varepsilon=19.61$ as the sum of rounded component ADP values. The published zCDP guarantee yields operationally equivalent $\varepsilon$ values of approximately 4.25, 2.94, and 3.18 at significance levels of 1%, 5%, and 10%, respectively. Converting the same guarantee to a single ADP pair at $\delta=10^{-10}$ gives power bounds near 1 at all three levels. The pure DP scale thus clarifies constraints on distinguishing attacks that are difficult to discern from the reported $\varepsilon=19.61$.

---


### 155. [ArrythML-II: An Optimized TinyML Framework for ECG Arrhythmia Detection and Multi-Class Beat Classification on Wearable Devices](https://arxiv.org/abs/2611.28791)

**<font color=#1a73e8>作者：</font>** Nagarajan S, Kurian Polachan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents ArrythML-II, an optimized TinyML framework for on-device ECG arrhythmia detection and multi-class beat classification on wearable platforms. A systematic hyperparameter optimization framework is developed to identify compact autoencoder architectures for binary ECG arrhythmia detection. A custom scoring mechanism jointly considers detection performance, reconstruction-error thresholds, and model size to guide architecture selection. The framework is further extended to six-class ECG beat classification using a lightweight classifier derived from the optimized autoencoder architecture. Both models are INT8 quantized and deployed using TensorFlow Lite Micro on a custom-developed, battery-operated, single-lead ECG device based on the PSoC~6 microcontroller. The deployed autoencoder and classifier have model sizes of approximately 44~KB and 22~KB, respectively, with end-to-end processing times of 5.1~ms and 4.7~ms per ECG segment. Model inference accounts for 3.95~ms and 1.38~ms of these processing times, respectively. In the refined arrhythmia detection evaluation using the MIT-BIH Arrhythmia Database, the autoencoder achieved an accuracy of 84.76\%, precision of 82.68\%, and recall of 77.99\%. The multi-class classifier achieved 82.29\% accuracy, weighted precision of 90.18\%, and weighted recall of 82.29\%. Beyond offline model evaluation, the wearable platform is validated using preloaded ECG segments, live ECG signals, and an ESP32-S3-based ECG emulator that replays annotated MIT-BIH recordings as analog waveforms. The results demonstrate the feasibility of integrating optimized TinyML models into wearable platforms for real-time ECG analysis.

---


### 156. [ArgsWorld: Unifying 3DGS Scene Reconstruction, Generation and Extrapolation with Autoregressive Diffusion Transformer](https://arxiv.org/abs/2611.28792)

**<font color=#1a73e8>作者：</font>** Weiming Chen, Shuaiyan Liu, Xinyu Shao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive diffusion world models deliver strong video generation performance, yet they typically output only RGB frames rather than explicit 3D Gaussian Splatting (3DGS) scene representations, creating a gap between learned visual world dynamics and usable 3D assets for downstream robotics, simulation and rendering. To bridge this gap, we introduce ArgsWorld, an autoregressive diffusion model that also produces an explicit 3DGS scene. For each generation chunk, the diffusion transformer jointly processes clean historical image latents and noisy latents for new views. It keeps the historical image latents fixed and refreshes the scene features so that the Gaussian representation can be revised as new regions come into view. Our 3D Self-Forcing Distillation trains the model on its own generated histories using a mixture of single-view and multi-view data. Distribution matching supervises direct image latents and latents of Gaussian renderings at both generation and additional cameras. ArgsWorld unifies 3D scene reconstruction from posed images, scene generation from image or text prompts, and scene extrapolation across camera segments with disconnected endpoints. Experimental results demonstrate that ArgsWorld achieves state-of-the-art performance across multiple 3D scene modeling tasks. Project page: this https URL

---


### 157. [Inference Dynamics: Image Classifiers Keep Using Visual Cues After They Are Removed](https://arxiv.org/abs/2611.28795)

**<font color=#1a73e8>作者：</font>** Ruiqi Wang, Mingming Lu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image classifiers are typically evaluated by their final predictions, treating inference as a static image-to-label mapping. Reliability, however, also depends on whether a model can relinquish evidence after that evidence disappears. We reveal a counterintuitive phenomenon: removing a local visual cue from its original location may not remove its influence on the prediction. Once captured by early layers, the cue can become distributed across later representations, making ``no longer visible'' different from ``no longer relied upon.'' We introduce Inference Dynamics, a process-level framework for tracing how cue influence evolves and remains withdrawable across network depth. Given an image and a matched cue-removed reference, we replace cue-aligned states in the original branch with their reference counterparts at successive layers and measure recovery toward the cue-free prediction. The resulting trajectory separates evidence locality from decision-level withdrawability. Across datasets and architectures, we find locality declines before withdrawability collapses: cue-induced information becomes less concentrated at its original support while its effect remains active, before entering an evidence lock-in stage. Consequently, fixed late-stage correction may alter the final readout without removing accumulated cue dependence. We therefore propose Evidence Reset, which selects an input-dependent layer before lock-in and reconstructs cue-aligned states toward their cue-free counterparts. Our results establish evidence withdrawability as a process-level dimension of classifier reliability and suggest a new intervention principle: correction depth should follow the dynamics of evidence rather than be fixed in advance.

---


### 158. [NavDecision: Parallel Multi-Step Action Prediction with Persistent Self-Referential Learning for Vision-and-Language Navigation](https://arxiv.org/abs/2611.28796)

**<font color=#1a73e8>作者：</font>** Kai Wu, Yufan Hu, Quan Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-and-language navigation (VLN) requires timely decisions based on instructions and visual observations. However, autoregressive VLN models generate action descriptions token by token, introducing substantial inference overhead. Decision models offer an efficient alternative but face challenges in maintaining short-horizon action coherence and long-horizon goal alignment. To address these challenges, we propose NavDecision, an efficient multi-step VLN decision model. We introduce parallel multi-step action prediction (PMAP) to predict multiple action distributions from a shared vision-language state, and memory-augmented self-referential policy optimization (M-SRPO) to learn from unsuccessful trajectories using successful trajectories as references. A cross-iteration success memory further accumulates historical successful trajectories to provide informative training feedback. NavDecision achieves success rates of 64.60% on R2R-CE and 64.57% on RxR-CE with a 4B backbone. Compared with existing autoregressive VLN methods, it delivers significant inference speedups of up to $22.28\times$ and $18.96\times$ while maintaining comparable navigation performance.

---


### 159. [Not All Directions Are Flat: Decomposed-Gradient Flatness for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2611.28802)

**<font color=#1a73e8>作者：</font>** Ungbae Yoon, Kwanyoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many applications of novel view synthesis, such as augmented reality and robotics, can afford only a few input views, since dense capture is costly. With such sparse views, however, 3D Gaussian Splatting (3DGS) overfits the training views and degrades at unseen viewpoints. Among the approaches to this problem, flat-minima optimization treats the Gaussians as trainable parameters and steers training toward flat minima, which generalize better, by perturbing the Gaussians with random noise or along the training gradient. However, these perturbations ignore their direction relative to the other training views. Interestingly, we find that the direction of the perturbation determines whether it improves generalization. Specifically, we decompose the gradient of each training view into a component parallel to the average gradient of all views, on which the views agree, and an orthogonal component, on which they disagree. Perturbing along the orthogonal component improves generalization, whereas perturbing along the parallel component does not. We further find that the flatness correction often opposes the reconstruction gradient, shrinking or even reversing the reconstruction step. Based on these findings, we propose DecoFlat, which perturbs each Gaussian along the orthogonal component together with random noise. Furthermore, we introduce a conflict-aware correction, which removes the part of the flatness correction that opposes the reconstruction gradient, and a rescheduling of the spherical-harmonics color, which suppresses the overfitting of view-dependent appearance. Extensive experiments demonstrate that DecoFlat, as a plug-in optimizer, consistently improves vanilla 3DGS and a wide range of sparse-view 3DGS methods.

---


### 160. [When do stored facts become available in looped transformers?](https://arxiv.org/abs/2611.28808)

**<font color=#1a73e8>作者：</font>** Fabio Valerio Massoli, Arnau Padrés Masdemont, Jordi Ros Giralt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Looped transformers do not acquire new knowledge during a forward pass. Prior work shows that they store as many bits in their weights as non-looped models. It remains unclear how recurrence makes this knowledge available during inference. We study this question using synthetic factual recall and multi-hop reasoning, measuring depth-resolved readable information in bits with native readouts and tuned lenses. Under final-loop supervision, single-hop facts become readable progressively: heavier memorization loads delay retrieval despite comparable final readable information. Untied baselines of equal unrolled depth concentrate retrieval near the end of their stacks, whereas looped models expose facts earlier. This delay is not intrinsic to the tested recall tasks: training with supervision and depth-specific readouts at every loop makes near-final information readable after the first loop in all tested configurations. Representational analysis shows value-related structure emerging within states organized by the query key. We then study multi-hop chains whose facts are stored in the weights rather than given in the prompt. Intermediate entities become decodable in chain order, and aligned transitions show next-entity structure developing while current-entity structure remains dominant. Interventions in a released six-recurrence model establish a causal role for these representations. Counterfactual replacements of a probe-defined entity component at a single prompt position redirect downstream bridge entities and the final answer. Conversely, replacements from queries that reach the same entity through different preceding relations, preserving the remaining relation suffix, retain the original answer in over 99.5\% of tested cases. These results distinguish a training-dependent schedule for factual recall from the causal role of retrieved-entity representations in subsequent composition.

---


### 161. [RadAG: Reward-Adversarial Attention Guidance for Efficient Inference-Time Alignment of Diffusion Models](https://arxiv.org/abs/2611.28809)

**<font color=#1a73e8>作者：</font>** Hyeongchan Jeon, Kwanyoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow-based models have achieved remarkable success in generation, yet their samples often remain suboptimal in fidelity and text alignment. Two lines of inference-time methods address this: extrapolation guidance, such as classifier-free guidance (CFG) and its variants, and reward guidance, which aligns samples with reward models of human preference. Extrapolation guidance needs only forward passes, but it builds its reference by heuristic rules unrelated to the reward and therefore cannot steer sampling toward a given reward. Gradient-based reward guidance steers sampling directly toward a higher reward, but backpropagates through the entire generator at every step. This trade-off raises the question of whether extrapolation guidance can steer sampling toward a higher reward without a full backward pass. To answer this, we introduce Reward-Adversarial Attention Guidance (RadAG), which constructs the reference by perturbing the attention logits of a single block against their reward gradient and extrapolates away from it. We prove that this update increases the reward of the clean estimate to first order, while its backward pass stops at the perturbed block instead of traversing the entire generator. On FLUX.2-klein-4B and 9B with PickScore and aesthetic rewards, RadAG achieves the highest target reward in every setting with 30-65% less time than gradient-based and candidate-based baselines.

---


### 162. [The Humming Revachol: A Dialogue Network Analysis of Narrative Power in Disco Elysium](https://arxiv.org/abs/2611.28812)

**<font color=#1a73e8>作者：</font>** Xinran Liu, Miguel Arana-Catania, Jack Orchard  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study applies social network analysis to the narrative RPG Disco Elysium to examine how narrative power is distributed among its characters. A directed, weighted character-mention network of 73 NPCs is constructed from the game's complete dialogue script, with characters identified and annotated across five social attributes. Narrative power is operationalised through four dimensions: attention, authority, discursive initiative, and embeddedness. Non-parametric statistical tests examine differences across gender, age, race, class, and ideology. The findings suggest that narrative power is largely independent of social identity categories and is more closely associated with character narrative functions, while structural embeddedness reflects the socio-organisational contexts in which characters are situated. These findings show that dialogue-network analysis can reveal structural patterns of representation that visibility counts alone would miss.

---


### 163. [ViTrust: Learning 3D Observation Trust for Deformable Physical World Models](https://arxiv.org/abs/2611.28815)

**<font color=#1a73e8>作者：</font>** Zhihao Guo, Zhihao Li, Xu Ge 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning deformable physical world models requires dynamics that generalize beyond observed motion. Accurate reconstruction alone does not ensure accurate future prediction, motivating us to learn how observations should influence physical identification. However, visual reliability alone does not determine how informative an observation is about physical dynamics. We propose ViTrust to learn 3D observation trust, determining how strongly each tracked point influences physical identification. Its key design is a visual-contact trust adapter that combines pointwise spatiotemporal evidence with interaction history on a persistent contact graph to predict time-varying observation weights. A single-stage, shared-forward objective jointly optimizes these weights and physical parameters through weighted geometry and correspondence losses, with constraints to prevent observation-weight collapse. All learning uses only the observed prefix. The fitted physics remains fixed for future prediction under supplied controls. Experiments on real-world sequences demonstrate improved future prediction over the evaluated baselines, alongside qualitative demonstrations of novel-control rollouts and cross-object transfer.

---


### 164. [Improving semantic equivalence in research-level math formalization](https://arxiv.org/abs/2611.28819)

**<font color=#1a73e8>作者：</font>** Ayush Khaitan, Liam Fowl, Tomàs Ortega 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Formalizing mathematics in Lean is never a word-for-word translation of a paper: a Lean formalization changes definitions, strengthens hypotheses, splits arguments, and adds lemmas the paper never mentions. It stands to reason that a model that is good at autoformalization must be a good predictor of how a natural language source must differ from its faithful Lean formalization. With that in mind, we collect 4{,}076 audited examples of such changes from 832 Lean projects that formalize research-level mathematics, and use them to ask a practical question: how well can a model \emph{write} Lean inside a real research-level project that may contain tens of thousands of lines of code, and does training on discrepancies between natural language sources and their faithful Lean formalizations help? Our training set consists of 3{,}431 tasks from 141 repositories, and the test set consists of 645 tasks from the remaining 27 repositories. Training on in-project Lean nearly doubles complete proofs ($11\% \to 20\%$) and raises the share of statements in gold agreement with the project's own formalization by nearly a third ($30\%$ to $39\%$). The gain comes from the pairs themselves: an adapter trained only to predict how the Lean will differ, or a model told the difference in advance, barely helps. Training on where formalizations depart from their sources is thus an effective way of improving semantic equivalence in research-level formalization.

---


### 165. [PointNeXt Adapter Improved Model for BIM Component Defect Association under Construction Images and Design Model Attributes](https://arxiv.org/abs/2611.28820)

**<font color=#1a73e8>作者：</font>** Na Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Construction site defect analysis increasingly requires linking field evidence to the correct BIM object, because a crack, spalling area, missing sleeve or misaligned support is useful for quality control only when it is connected with component identity, location, responsibility and design intent. This paper proposes a PointNeXt Adapter improved model for BIM component defect association under construction images and design model attributes. The method aligns site image crops, local point cloud patches, BIM component identifiers, geometry attributes, material categories, installation stage, inspection distance, viewpoint quality and source reliability tags into component level inspection windows. PointNeXt learns local geometry and deviation from as built point evidence, while the adapter injects BIM attributes so the same geometric irregularity can be interpreted differently for structural, envelope, MEP and embedded components. The fusion head outputs component link, defect class, defect probability, confidence, dominant evidence and recommended review action. A synthetic multisource BIM inspection dataset is used to evaluate repeated layouts, occlusion, sparse point clouds, registration errors and unseen component arrangements. Results show that attribute aware point learning improves association accuracy, defect recall and confidence calibration compared with image only, point only, simple fusion and adapter free baselines. The framework is positioned as traceable BIM issue review support, requiring manual confirmation and staged field validation before operational deployment.

---


### 166. [More Is Never Less: Affordable Robustness to Additive Attacks via Monotone Multiple-Instance Learning](https://arxiv.org/abs/2611.28825)

**<font color=#1a73e8>作者：</font>** Alexander Herzog, Shae McFadden, Lorenzo Cavallaro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Static malware detectors that represent each sample as a bag of extracted features, such as permissions, API calls, or imported functions, are cheap to deploy and remain state-of-the-art under temporal drift and in selective classification. Yet, attackers can evade them by adding benign-looking content that outweighs malicious evidence. Canonically, detectors encode the presence of a few thousand features, selected during training, as sparse multi-hot vectors over a fixed vocabulary. Features that emerge after training remain invisible. We show that linear models and multi-layer perceptrons (MLPs) over this input are sum-pooled set models in disguise. Sum-pooling lets added benign features cancel malicious evidence. Instead, we cast malware detection with set-shaped static features as a multiple-instance learning (MIL) problem. To this end, we propose MalSets, which uses max-pooled Deep Sets models with a monotone head to ensure that any malicious evidence remains undiluted; thus, more is never less. Under MIL, a general text encoder maps any feature string to an embedding, thus eliminating the long-standing out-of-vocabulary problem at test time. Max-pooling retains the malicious evidence regardless of how many benign features an attacker adds. Since max-pooling can only grow when features are added, constraining the head alone makes the malware score monotone under additions, even against a white-box attacker adapted to this architecture. While monotone detectors are never evaded by state-of-the-art black-box or white-box attacks, they often significantly pay for this robustness in clean performance since benign features cannot count as evidence. However, by combining a non-monotone set encoder with max-pooling and a monotone head, MalSets maintains the robustness of prior monotone classifiers while achieving state-of-the-art performance.

---


### 167. [Task-Conditioned Detail Allocation for Synthetic Segmentation Data](https://arxiv.org/abs/2611.28841)

**<font color=#1a73e8>作者：</font>** Chunming He, Dingming Zhang, Jifan Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic images sharing a segmentation label can differ in their training value. We propose Task-Conditioned Detail Allocation (TCDA) to select useful candidates and locally edit some remaining images. We ask whether image details provide class-specific cues in the regions marked by the label. We train a small task reference on frozen image features from real training images. We compare its class responses before and after blurring each candidate, and score how well these response changes align with the labeled regions. This detail allocation score ranks candidates from the same source. Comparing their response--label alignment with that of the real source image also guides repair decisions and, in multiclass tasks, the choice of regions to edit. Selected candidates and accepted repairs are used for training with the original labels and the unchanged downstream segmenter. Experiments on camouflaged object detection, degraded salient object detection, and adverse-condition semantic segmentation show that our selection outperforms equally sized random and label-agreement subsets. Combining selection and repair improves over real-only training by up to 0.019 in $S_\alpha$ on COD10K and 2.86 mIoU points on ACDC.

---


### 168. [Learning How a Body Moves: Few-Shot Body Inference for Visual World Models of Animated Characters](https://arxiv.org/abs/2611.28842)

**<font color=#1a73e8>作者：</font>** Amarnath R  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Two visually identical animated characters can respond differently to the same action command because their body dynamics differ. For example, a stiff blob and its bouncy twin reach different heights when both receive the jump command. Given only the first frame and the action command, a visual world model has no information to distinguish these twins, because their initial appearances are identical. We therefore propose an in-context world model that encodes clips of a character's other actions into a body representation, using a contrastive loss to separate look-alike characters. We introduce ToonTwins, a benchmark of 144 2D cartoon characters that run, jump, fall, turn and crouch. Its characters form look-alike groups of four that differ only in their dynamics profile, and we also evaluate the model on 32 animated animals from DeformingThings4D. Even with a body code from these clips, the latent pixel world model we tested recovered at most 25 percent of the twins' jump height difference. On new shapes, our model identified the correct twin in 85.9 percent of cases, compared with 76.7 percent for a transformer baseline that reads the same clips without a body summary, and in a controlled ablation the contrastive loss gave more than half of this gain. On the animated animals, it reduced the mean path prediction error by 8.5 percent against a model without body information.

---


### 169. [EA-Bench: Measuring information and action efficiency under imperfect instructions](https://arxiv.org/abs/2611.28846)

**<font color=#1a73e8>作者：</font>** Xu Wan, Wenyue Xu, Shenjie Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal agents help users complete everyday work across digital applications. Many standard benchmarks assume that users provide sufficient information to solve a task. However, agents often encounter incomplete, distracting, or inconsistent information in practice. To systematically study agent inefficiency under such imperfect information, we introduce Efficient Action (EA)-Bench, which evaluates both tool calls and user interactions in work-related tasks. To our knowledge, it is the first benchmark to jointly evaluate tool-call efficiency and user-interaction efficiency under controlled missing, redundant, and conflicting information. We construct 63 base-task instances adapted from existing work-related benchmarks. To guide perturbation design and quantify task requirements, we represent workflows as directed acyclic graphs (DAGs) and examine node-level dependencies to identify where information can be withheld, contradicted, or supplemented with distractors. We use a two-stage validation process combining AI-assisted checks with expert screening to select 232 conditions from 792 initial candidates. We organize these tasks into Easy and Hard tracks by task complexity. Experiments show that imperfect information can reduce accuracy and increase tool-use and user-interaction costs. More concerning, several models obtain apparently correct outcomes by guessing user-specific values without confirmation, revealing potential execution unreliability in current models under imperfect user information.

---


### 170. [Guarding with Judgment: Learning to Intervene for Multimodal Safety](https://arxiv.org/abs/2611.28849)

**<font color=#1a73e8>作者：</font>** Jipei He, Cheng Cheng, Liuguo Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When visual context makes an ordinary request unsafe to answer as asked, a blanket refusal may leave the user's need unresolved. Choosing how to help requires distinguishing an established hazard from a condition that still needs verification, a distinction that binary safety labels leave unspecified. We formulate this decision through four actions: allow, warn, review, and refuse. To ground these decisions in verifiable evidence, we build a corpus of 20,126 training audits and the JudiBench benchmark, connecting each action to diagnostic judgments, source evidence, and controlled context changes. Our guard, JudiAct, separately states what the source establishes, what condition governs the help, and how the rules apply. It then checks these three brief review items against the original inputs to predict diagnostic labels and a handling action. Supervised training learns individual judgments while comparing label assignments across related cases. A second stage swaps one review item at a time, using the resulting audit feedback to refine review generation. On JudiBench, JudiAct improves request and answer Macro-F1 by more than 28 percentage points over its 4B backbone. Across nine public benchmarks, it outperforms state-of-the-art guards on the mean delivered-answer score in both pre-generation and post-generation settings, cutting MM-SafetyBench attack success from 40.78% to 25.30%.

---


### 171. [MQCODet: Modality Quality-Guided Collaborative Optimization for UAV-Based RGB-T Tiny Pedestrian Detection](https://arxiv.org/abs/2611.28850)

**<font color=#1a73e8>作者：</font>** Hui Li, Jianbo Ma, Hui Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV)-based RGB-thermal (RGB-T) remote sensing provides complementary visual and thermal information for pedestrian perception under complex aerial observation conditions. However, detecting tiny pedestrians in UAV-based RGB-T imagery remains challenging due to cross-modal spatial heterogeneity, manifested as modality quality imbalance and spatial position misalignment. Existing RGB-T detectors primarily address these challenges at the feature fusion stage, without establishing an effective coupling between feature fusion and object localization, potentially resulting in suboptimal detection performance. To address this limitation, we introduce a Modality Quality-Guided Collaborative Optimization Detector (MQCODet), which extends modality quality from a fusion prior to a localization supervision cue. Specifically, we propose a Dynamic Calibration and Region-Aware Fusion (DCRF) module that progressively refines cross-modal spatial alignment and performs region-aware fusion to generate reliable multi-scale features and a scene-level modality quality prior. We further design an Efficient Contextual Interaction (ECI) encoder to enhance multi-scale feature interaction while preserving fine-grained spatial details. Moreover, we propose a Modality-Aware Adaptive (MAA) loss that incorporates the modality prior and object scale to adaptively balance spatial consistency and geometric similarity for localization supervision. Extensive experiments demonstrate that MQCODet surpasses state-of-the-art methods on two UAV-based RGB-T tiny pedestrian detection benchmarks while achieving real-time inference on the edge platform.

---


### 172. [Dynamic Model Merging with Multi-Layer Aggregated Routing Evidence](https://arxiv.org/abs/2611.28855)

**<font color=#1a73e8>作者：</font>** Yuxi Li, Jiacong Hu, Jie Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic model merging aims to retain the efficiency of a unified model while better preserving task-specific expertise through input-dependent routing at both the task and head levels. However, even the routing components of the state-of-the-art approach remain limited: the task routing is highly sensitive to the choice of routing layer, whereas the head routing relies on simple max-logit competition. To address these limitations, we propose multi-layer aggregated routing evidence (MATE) as a unified mechanism for improving both task and head routing. Specifically, we first introduce a metric to quantify task routing separability across different layers. Empirical analysis of this metric reveals that different layers provide complementary evidence for identifying the tasks relevant to an input. Motivated by this observation, MATE selects multiple informative layers according to their routing separability and aggregates their layer-wise routing scores to produce a more robust signal that can be directly used for task selection. Moreover, we observe that this signal also encodes useful information about the suitability of the corresponding classification heads. This motivates us to further combine the MATE signal with the max-logit score to guide classification head selection. Extensive experiments on vision benchmarks demonstrate that MATE consistently achieves state-of-the-art performance.

---


### 173. ["I feel like AI is just everywhere": A longitudinal qualitative study on parents' perceptions, use, and mediation of GenAI](https://arxiv.org/abs/2611.28861)

**<font color=#1a73e8>作者：</font>** Jennica Li, Shirley Zhang, Dakota Sullivan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> GenAI has developed rapidly over the last few years, yet few longitudinal studies exploring how individuals' experiences with GenAI have changed over time exist. Even fewer studies have focused on families with children, despite the opportunity to explore how parents have balanced their needs, their children's development, and the fast pace in which technology changes. To better understand how parents' perceptions, use, and mediation of GenAI shifted over two years, we interviewed 10 parents who had participated in a prior study about their families' experiences with GenAI. Parents had shifted from thinking GenAI was novel to feeling like it was unavoidable, characterizing GenAI as a limited tool to believing GenAI development needed to be regulated, and focusing on their personal mediation strategies to wanting systemic plans to curb GenAI's long-term consequences. We position our findings within the context of parental mediation of technology and increasing collective mitigation of GenAI-related risks.

---


### 174. [KineState-SWAM: A Surgical World Action Model with Explicit Kinematics and Causal Interaction Dynamics](https://arxiv.org/abs/2611.28871)

**<font color=#1a73e8>作者：</font>** Rulin Zhou, Yujie Ma, Rui Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing surgical world models often leave implicit how instrument motion drives localized tissue responses and how interaction history informs subsequent actions. We introduce KineState-SWAM, a surgical world-action model coupling action prediction and video generation through a persistent interaction state, separating kinematically determined instrument motion from learned scene evolution. A flow-matching policy predicts joint trajectories conditioned on interaction state, robot configuration, and task instruction. Kinematic Geometry Conditioning converts these trajectories into surface-motion tokens and spatially aligned instrument renderings using calibrated URDF kinematics. Causal Interaction Dynamics recurrently updates the state through geometry-guided attention and motion-aligned feature transport, carrying interaction history into subsequent action predictions without intermediate video synthesis. The State-Geometry Adapter combines state-dependent spatial modulation with localized geometric residuals to guide video generation. Interaction-aware supervision emphasizes tissue responses near instrument working regions. We introduce dVRK-Chole5.2k, comprising 5,255 videos spanning 17 surgical tasks. Experiments demonstrate improved action accuracy and video fidelity over evaluated baselines within matched action-conditioning settings. Ablations support preserving and transporting interaction states for long-horizon prediction.

---


### 175. [SENSA: Visual-to-Brain Generation with Individualized Subject-State Transfer and Adaptation](https://arxiv.org/abs/2611.28872)

**<font color=#1a73e8>作者：</font>** Yihang Zou, Chunmei Qing, Ruixi Liang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual-to-brain encoding predicts neural responses to visual stimuli, supporting visual cognition research and neural decoding. However, challenges in disentangling shared from image-specific activity, together with inter-subject distribution shifts and representational heterogeneity, limit accurate encoding and cross-subject generalization with limited calibration data.
We introduce SENSA, a structured continuous neural response generation framework that separates shared activity from image-dependent responses and calibrates a compact subject state. An independent response prior captures shared activity, while complementary visual descriptors drive separable sensor-time bases and a shared Response Refiner. Subject-Adaptive Factor Transport adjusts the spatiotemporal expression of shared bases, while Source-Grounded Residual Memory predicts image-dependent corrections in source-response coordinates. Together, they personalize a frozen generator using limited paired support.
Experiments demonstrate that the generation backbone outperforms recent generators across three datasets, with image-identity perturbations confirming stimulus specificity. Using only 400 paired images, electroencephalography (EEG) and the Natural Scenes Dataset (NSD) calibration achieve residual Pearson correlations of 0.1091 and 0.2995, respectively, demonstrating effective brain-response generation and cross-subject adaptation.

---


### 176. [Eidetic Code World Model](https://arxiv.org/abs/2611.28878)

**<font color=#1a73e8>作者：</font>** Wenqing Tian, Zijian Zhang, Qiang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Executable code can preserve a world's structural layout, yet video renderers frequently alter the appearance of previously visited places once they leave the camera view. We present Paintress, a code-conditioned world model that couples an executable geometric proxy with an independently parameterized 3D Gaussian appearance memory in a shared metric coordinate frame. While the proxy enforces structural and visibility constraints, 3D Gaussians capture the visual realization synthesized by emitted observations. To balance stable incremental fusion with consistent readout, Paintress separates writing from reading: newly emitted frames update a persistent raw Gaussian map under confidence-gated selection, whereas a cloned reader copy is globally refined against the observation archive and rendered with coverage masks to condition generation. We also introduce Expedition-33, a benchmark for generated-appearance retention across 11 static scenes, five route families, and 15, 30, and 60 s target absences (165 settings per system). Excluded from the opening image, targets are synthesized during a shared prefix and scored against each system's own first visit at matched return cameras. Across ten systems (1,650 videos), Paintress achieves 0.1220 ROI-LPIPS, 0.0613 MAE, and 52.12% detail retention (vs. 0.2731, 0.1401, and 10.91% for CWM), with lower discrepancy at 60 s (0.1630) than CWM, AgentGarten, and Lyra 2.0 achieve at 15 s.

---


### 177. [Health Ikigai: Semantic Conversational Interfaces for Wearable Health Data to Support Behavioral Change for Senior Indian](https://arxiv.org/abs/2611.28883)

**<font color=#1a73e8>作者：</font>** Md Haseen Akhtar, Hansoo Lee, Rafael A. Calvo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In ubiquitous health contexts, wearable feedback is often encountered in brief, interrupted moments of everyday life. However, many wearable and mobile health systems still present personal health data through numerical dashboards, leaving users and health coaches to interpret trends, thresholds, and deviations on their own. This interpretive burden may be especially relevant for adults aged 50-65 in India, where digital literacy, health literacy, language, and daily routines can shape how health technologies are understood and used. We present Health Ikigai, a design-oriented proof-of-concept framework that reframes wearable activity feedback from dashboard-based numerical interpretation to semantic conversational feedback. The prototype transforms replayed wearable-derived activity data into baseline-aware triggers, plain-language feedback, limited-turn conversational prompts, and coach-facing review summaries. A preliminary formative evaluation with ten adults in India suggests that participants perceived the interaction as understandable, lightweight, supportive, and actionable. We discuss design implications for low-burden wearable health interfaces that preserve coach oversight while reducing users' interpretive work.

---


### 178. [Controlled One-Click Benchmarking and Post-Fusion Recalibration for Support-Conditioned Medical Segmentation](https://arxiv.org/abs/2611.28890)

**<font color=#1a73e8>作者：</font>** Wang-Chi-Shiun, Wei-Huan Hu, Liu-En-Chi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-prompt medical segmentation is hard to compare when prompts, supports, thresholds, and splits differ. This paper uses a controlled one-click protocol: each test image receives one positive foreground click, training-only support, validation-only checkpoint selection, and no test-time threshold tuning. We propose {Support-Aware Recalibration (SAR)}, a late post-fusion recalibration block for MultiverSeg that combines large-kernel spatial gating with squeeze-and-excitation channel recalibration after support--query fusion. BUSI, NerveUS-BP-present, and Kvasir-SEG are evaluated with matched 697 foreground-present sample budgets, shared splits/clicks, and threshold-free Dice-AUC/IoU-AUC. Compared with a protocol-matched raw-support MultiverSeg baseline, the main SAR configuration shows favorable mean Dice-AUC/IoU-AUC performance on BUSI, NerveUS-BP-present, and Kvasir-SEG, while reducing logged training time in this implementation. These controlled results indicate that late post-fusion recalibration is useful under a leakage-controlled one-click protocol.

---


### 179. [Gaze Graphs: A Scene-Level Representation of Visual Attention in the Operating Room](https://arxiv.org/abs/2611.28901)

**<font color=#1a73e8>作者：</font>** Séraphin Baributsa, Keqi Chen, Vinkle Srivastav 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Analyzing clinicians' visual attention from exocentric camera views can support surgical scene understanding without requiring wearable eye trackers. However, existing gaze-following research in the operating room (OR) estimates only 2D gaze locations without identifying attended scene entities or localizing gaze targets in 3D space. In this work, we investigate gaze graphs as a scene-level representation of visual attention that connects clinicians to attended scene entities, and evaluate their utility for fine-grained surgical action recognition and semantic scene graph (SSG) generation. Methods: We extend the public EgoExOR dataset with gaze annotations to create EgoExOR-Gaze, the first benchmark for multi-view gaze graph generation in the OR. We propose a novel architecture that jointly estimates 3D gaze targets and predicts attended entities using only exocentric camera views. Specifically, our approach exploits 3D gaze geometry to sample local visual features across multiple views for attended entity prediction. We further utilize predicted gaze graphs for fine-grained surgical action recognition and SSG generation. Results: For gaze graph generation, our model outperforms both exocentric-only and combined exocentric-egocentric baselines. For surgical action recognition, our model incorporating predicted gaze graphs outperforms both exocentric and egocentric baselines across all evaluated metrics, with particularly strong gains in temporal metrics. For SSG generation, incorporating gaze graphs improves macro-F1 from 0.42 to 0.52 compared to exocentric inputs alone, although performance remains below that achieved with egocentric inputs. Conclusion: Our results demonstrate the value of gaze graphs for surgical action recognition and SSG generation, highlighting the importance of explicitly modeling scene-level visual attention even when egocentric views are unavailable.

---


### 180. [Ads for Agents: Measuring Ad-Serving MCP Servers](https://arxiv.org/abs/2611.28911)

**<font color=#1a73e8>作者：</font>** Shahrooz Pouryousef, Sohini Chakraborty, Ali Montazer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents call external tools through protocols such as the Model Context Protocol (MCP). Some MCP servers return paid advertisements (ads) into the model's context. The model then decides whether these ads and their disclosures reach the user. We trace these ads from their sources to the agent's tool results across public MCP servers and packages. We find the servers through their public traces in ad networks, package registries, certificate logs, hostnames, MCP directories, and GitHub configurations. We then query the ad-serving servers with read-only requests and inspect their ad links. Ads appear on only 0.57% of 101,363 open MCP endpoints and 0.04% of 122,656 local MCP packages. Although 173 ad networks target agents, operators insert the ads themselves on about half of the 226 ad-returning servers. Nearly all ad-serving packages likewise carry the operator's own affiliate identifier. While ads adapt to the topic and intent of the query, their disclosure stays fixed within each tool. Only 9.3% of the ads carry an explicit sponsored label. Most ad links also hide their destinations. Since operators insert most ads themselves and label them inconsistently, we propose a per-item ad annotation in MCP results. Clients can show this annotation to the user independently of the model's answer.

---


### 181. [Div3DAfford: Diverse 3D affordance grounding](https://arxiv.org/abs/2611.28917)

**<font color=#1a73e8>作者：</font>** Haomeng Zhang, Raymond A. Yeh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D affordance grounding aims to localize 3D regions specified by an interaction query. Existing methods predict a single affordance mask, overlooking the inherent diversity of human-object interactions. We introduce diverse 3D affordance grounding, a new task that requires predicting multiple plausible regions for a given object and affordance query. We then propose Div3DAffordNet, a transformer-based set prediction model capable of generating diverse affordance regions. To address the scarcity of diverse 3D affordance data, we develop an automated pipeline leveraging 2D generative models and 3D reconstruction techniques to synthesize 3D affordances, followed by lightweight human verification (reducing the annotation time by 72X), yielding the Div3DAfford benchmark. Extensive experiments show Div3DAffordNet effectively captures multi-mask affordance regions. Our method achieves the SOTA affordance grounding performance in the multi-mask setting, reducing GED-SIM from 0.745 to 0.492, while maintaining competitive single-mask performance on the standard benchmark of 19.0 mIoU.

---


### 182. [When Do Better Visual World Models Make Better Plans? Decision-Aligned Selection for Latent Planning](https://arxiv.org/abs/2611.28919)

**<font color=#1a73e8>作者：</font>** Chan Aristella Lu, Arya Fayyazi, Junil Yeo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual world models enable goal-conditioned planning by predicting the outcomes of candidate actions in latent space. However, planning depends on how well a model ranks candidates, whereas training optimizes how accurately it predicts each one. We identify the Decision-Relevant Residual (DRR), the part of the cost error that can reorder candidates, and show that the more training reduces the DRR, the more it improves selection (Spearman $\rho = 0.82$, vs. $0.61$ for prediction error). Building on this insight, we introduce Decision-Aligned Selection (DAS), a plug-in selection rule that scores candidates by the standardized consensus of several independently trained checkpoints, which averages out their checkpoint-specific residuals. Across two model families (LeWorldModel and DINO-WM) and five tasks, DAS selects better actions than single checkpoints in 12 of 18 configurations and outperforms training one model three times longer in 14 of 18. In closed loop, DAS improves success over single checkpoints in 6 of 9 pre-registered LeWM comparisons.

---


### 183. [PIAE: Physics-Informed Continuous Autoencoding for Compact 3D Human Motion](https://arxiv.org/abs/2611.28922)

**<font color=#1a73e8>作者：</font>** Osama Alshammari, Omar Mohammed, Kerven Durdymyradov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal compression reduces the sequence length that motion generators must model, but can damage articulated detail and global trajectory. These errors have unequal consequences: root-velocity and heading errors propagate through trajectory recovery and affect the placement of the entire body. We propose PIAE, a physics-informed continuous autoencoder that allocates a fixed token budget between explicitly retained kinematic signals and complementary learned features. At 8 x temporal compression, each 256-dimensional token contains 224 learned values and a 32-dimensional physical carrier. The complete token conditions neural decoding, while a parallel recovery path constrains selected outputs. On the official HumanML3D benchmark, PIAE achieves 8.936 mm global MPJPE, an 82.0% reduction relative to a same-width learned-only model. The benefit extends beyond trajectory restoration: facing-local neural-body error before analytical correction decreases by 76.6% in a frozen-checkpoint validation diagnostic, and supplying the same true trajectory to both models preserves the body-quality advantage. Targeted root-only and explicit-root hybrid controls establish strong trajectory-aware comparisons; alternative carriers reveal that torso references favor position accuracy, whereas stance anchors favor support quality. With the original 8 x AEs frozen, matched text-to-motion generators predict every carrier value and improve FID from 0.506 to 0.163. Frozen reconstruction also transfers to AIST++ without adaptation. The compressed carrier interface reduces measured generation time by 27.8% relative to its 1 x counterpart. Together, these findings demonstrate that selective preservation can use a fixed representation budget more effectively, improving neural articulated reconstruction and downstream generation in compact human motion.

---


### 184. [Intrinsic Value Modules: Trusted-Hardware Support for Locally Final Offline Asset Transfer](https://arxiv.org/abs/2611.28928)

**<font color=#1a73e8>作者：</font>** AmirReza Fathi, Ali Rahimi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Consensus lets distributed participants agree on a common state, but it makes monetary validity depend on network connectivity and collective acceptance. We explore making validity intrinsic to a digital coin. We propose an \emph{Intrinsic Value Module (IVM)}: trusted hardware that gives a coin locally verifiable authenticity and spendability, analogous to verifying a signature. Under stated hardware and cryptographic assumptions, the IVM abstraction and our offline transfer protocol move monetary uniqueness from a replicated ledger into non-clonable protected state. The protocol prevents forgery, replay, double credit, and double spending by genuine, uncompromised IVMs; communication failures may lock value but cannot duplicate it. We distinguish local transfer atomicity and asset uniqueness, which the protocol establishes, from global state consistency across disconnected devices, which it does not. The IVM does not eliminate trust; it relocates trust to certified hardware, issuer roots, and non-rollback state. We present the architecture, protocol, and security analysis, and discuss open challenges.

---


### 185. [STEdgeFormer: MCU and NPU Deployable Transformer Architecture](https://arxiv.org/abs/2611.28935)

**<font color=#1a73e8>作者：</font>** Sudhakar Sah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transformer-based sequence models have achieved strong performance in language and time-series modeling, but self-attention remains computationally and memory intensive for deployment on resource-constrained edge accelerators. We propose STEdgeFormer, a lightweight, hardware-aware sequence architecture designed for efficient execution on embedded neural accelerators. STEdgeFormer combines polynomial mixture layers and DyT normalization with an accelerator-aware causal memory block, replacing pairwise self-attention with compact causal aggregation. On TinyStories, the fully NPU-supported STEdgeFormer (MW) achieves a perplexity of 7.39 with 4.12M parameters and 6.51 MB RAM, with an end-to-end latency of 40 ms. In comparison, the standard 4.12M-parameter configuration achieves a lower perplexity of 6.79 but requires CPU fallback for unsupported operators, resulting in 1450 ms latency. Vanilla Transformer, on the other hand, achieves a perplexity score of 5.71 using a 4.40M-parameter model, but it cannot be deployed on the hardware. On downstream tasks, STEdgeFormer achieves 94% accuracy on ECG5000 and 93% accuracy on Speech Commands with 1.39M parameters. These results demonstrate that hardware-aware architectural choices and operator compatibility can have a substantial impact on practical inference latency, beyond model size and task accuracy alone. Rather than targeting state-of-the-art accuracy on individual benchmarks, STEdgeFormer is designed to provide a deployable sequence modeling architecture under the memory, computational, and operator constraints of embedded neural accelerators.

---


### 186. [ActWithin: Bounding Wrong-Payment Risk in Delegated Payment Batches](https://arxiv.org/abs/2611.28941)

**<font color=#1a73e8>作者：</font>** Shuhao Zheng, Zhipeng Wang, Zi Xuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A delegated payment agent can hold valid rights for incompatible revisions of a batch. We study the window in which the selected revision cannot be verified by the execution deadline. For batches that permit every subset of up to q revisions, ActWithin compiles the limit into a shared quota of q successful replacement payments. If approved plans are mutually replayable with the same observable inputs, deadlines, and resources, this quota preserves normal completion without additional approvals and minimizes worst-case wrong-payment principal for arbitrary positive amounts. A dynamic program computes its exact risk and witness. For amount-preserving recipient changes, we derive the exact risk of the tightest single amount cap on the same replacement group, provided mixed payment subsets can settle within the window. A two-phase result isolates the risk to payments due before trusted verification. Against the amount cap, an exploratory setting with 16-64 payments and one quarter of positions revisable yields aggregate reductions of 16.23-16.88% on adapted IBM AMLSim amounts and 10.12-12.52% on an adapted controlled catalog. The 760 funded original controlled paths with constructed single-position revisions yield 2.69%. In one local MetaMask fixture, both policies complete all 37 normal plans and the worst wrong debit falls from 93,962 to 81,056 test wei.

---


### 187. [XShot: Cross-Shot Video Object Insertion from a Reference Video](https://arxiv.org/abs/2611.28942)

**<font color=#1a73e8>作者：</font>** Bangxun Tang, Chen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present XShot, a framework for cross-shot video object insertion, which adds objects to a shot by watching another shot of the same scene. Video productions show a scene through many shots, and objects added to one shot must appear consistently in the others. Most video editors take the appearance of new objects from reference images and their location from a text prompt, a mask or an edited keyframe, leaving this consistency to the user. XShot reads both from a reference video of another shot, which need not be aligned with the target, and needs no mask, box or camera pose. We build on a video Diffusion Transformer and formulate the task as in-context generation over the reference video, a few images of the objects and the target video. A geometry-aware cross-shot attention estimates the epipolar geometry between the two shots from the model's own correspondences and uses it to guide where the target reads the reference and the exemplars. We train XShot with an erase-and-restore data engine: objects are erased from one shot of a film or a multi-camera recording and restored from another shot of the scene. Experiments show that XShot places objects more accurately and renders them more faithfully than open-source and commercial video editors, while leaving the rest of the shot intact.

---


### 188. [Learning Land-Surface Hydrology World Model from Satellite Observations](https://arxiv.org/abs/2611.28963)

**<font color=#1a73e8>作者：</font>** Suya Li, Zekun Qi, Xiaochong Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A world model should tell us not only what will happen, but what would happen under a different action. Learned Earth models now forecast remarkably well, yet forecast skill says little about what their state means or how it responds to a changed driver. We build LandWM, a world model of land-surface water in which rain is the action, learned from seven years of SMAP and CYGNSS observations: physical observation operators tie its latent state to soil water, and a mass-conserving balance governs how that state responds to rain. Over the U.S. Southern Great Plains, the model, never shown a soil-moisture value, tracks 28 in-situ probes as well as the operational SMAP Level-4 product, even from CYGNSS alone, and a storm added to the forcing of a station's cell wets its soil as natural storms wet the probes. Replace either piece and the forecasts stay, but the meaning goes: with neural operators, only a probe fitted to the stations finds the soil water; with a generic recurrent transition, rain on a single cell barely moves it. Yet when the same rain covers the whole region the two transitions swap roles, and the conserving one responds too weakly. Grounding makes a world model readable; its response to actions must be tested under more than one kind of intervention.

---


### 189. [PruneNAS: Constraint Aware Neural Architecture Search based Pruning](https://arxiv.org/abs/2611.28964)

**<font color=#1a73e8>作者：</font>** Sudhakar Sah, Nikhil Chhabra, Honnesh Rohmetra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural Architecture Search (NAS) has achieved state-of-the-art performance across diverse tasks, but its high computational cost remains a major barrier. We introduce PruneNAS, a novel framework that integrates structured pruning into NAS to efficiently explore high-performing architectures while leveraging pretrained models. Unlike conventional NAS methods that train each candidate from scratch, PruneNAS generates a candidate pool by pruning pretrained networks at multiple granularity levels and formulates the selection as a global optimization problem using training-free importance metrics. This approach enables rapid evaluation of candidate architectures under strict resource constraints, dramatically reducing search time from hundreds of GPU hours to mere minutes. Experiments on standard benchmarks demonstrate that PruneNAS discovers compact, high-accuracy architectures that nearly halve the computational cost (MACs) of prior methods on ResNet-50, while also showing strong generalization on object detection tasks with YOLO. Our method bridges structured pruning and NAS, offering a practical solution for resource-constrained model deployment.

---


### 190. [Global Stability and Loss Convergence in Matrix Factorization](https://arxiv.org/abs/2611.28975)

**<font color=#1a73e8>作者：</font>** Eric Gan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the matrix factorization objective $\mathcal L(X,Y)=f(XY)$ for convex, twice continuously differentiable output losses with bounded and Lipschitz gradient and a minimizing set that is compact modulo specified input and output invariances. This includes the well-known cross entropy loss. We prove that a positive learning-rate threshold guarantees bounded parameters, summability of squared gradients, and convergence of the loss from every finite initialization. The proof constructs a quantity from the imbalance between parameter matrices that decreases over every step of the gradient descent trajectory.

---


### 191. [AlignHand: Multi-View Hand Reconstruction from a Frozen Monocular Prior](https://arxiv.org/abs/2611.28979)

**<font color=#1a73e8>作者：</font>** Zhilu Yang, Kun Yang, Shiyan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern monocular hand estimators recover detailed 3D meshes from individual images, yet effectively leveraging their predictions across multiple views remains challenging. Independently predicted meshes can disagree in scale, placement, and articulation, limiting the integration of complementary multi-view information. Hence, we present AlignHand, a calibrated multi-view framework that builds on a frozen monocular hand reconstruction prior to align and enhance its predictions. Specifically, AlignHand refines cross-view joint observations and estimates their reliability to establish a shared metric reference for alignment. Once the meshes are brought into a common frame, their complementary surface evidence is selectively fused across anatomical regions, followed by pixel-aligned refinement that predicts bounded residual displacements from local image features. This global-to-local integration enables AlignHand to exploit complementary observations while preserving the strong monocular prior. Extensive experiments on DexYCB-MV, HanCo, and HO3D-Eval-MV demonstrate that AlignHand achieves the lowest MPVPE and MPJPE among the compared methods under the respective evaluation protocols, reducing MPVPE by 30.1%, 29.1%, and 8.0%, respectively, compared with a matched geometry baseline.

---


### 192. [Stochastic non-metric MDS for noisy high-dimensional data](https://arxiv.org/abs/2611.28985)

**<font color=#1a73e8>作者：</font>** Sebastian Damrich, Dmitry Kobak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multidimensional scaling (MDS) constructs low-dimensional embeddings that approximate pairwise distances in a high-dimensional dataset. MDS exists in several flavors, with metric MDS approximating distances directly and non-metric MDS additionally optimizing for an arbitrary monotonic transformation of the high-dimensional distances. Empirically, metric MDS is known to suffer from the curse of dimensionality. Here we extend prior theoretical results for metric MDS on fully uninformative data to a more general case of finite, high-dimensional data with concentrated distances. We show that the metric MDS embeddings of such datasets stay distributionally close to the data-independent limit case. We then show that non-metric MDS is more robust to high-dimensional noise and can yield informative embeddings of such data. While existing implementations of non-metric MDS are slow, we develop a fast implementation using stochastic gradient descent in PyTorch. Using our implementation, we conduct an empirical study using multiple simulated and real-world datasets, including population-genomic and scRNA-seq data, and show that non-metric MDS can strongly outperform other methods in terms of global structure preservation.

---


### 193. [MB-SSIM: A Multi-Band Variant of SSIM, Tunable to Viewing Conditions](https://arxiv.org/abs/2611.28987)

**<font color=#1a73e8>作者：</font>** Yuriy A. Reznik  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> SSIM, as practically deployed, contains a hidden two-band model: although it was introduced as a departure from channel-based vision models, it amounts to a product of one similarity functional applied to a low-pass and a high-pass version of the two images. This split, however, is defined in pixels, so the spatial frequencies each band covers, as seen by the viewer, change with the display and the viewing distance. Making the model explicit and expressing it in cycles per degree gives a version of SSIM that takes the viewing conditions into account while preserving its simplicity. The resulting metric, MB-SSIM, keeps SSIM's per-patch product of similarity ratios; the bands are placed where psychophysics places the visual system's channels, and the viewing geometry enters through a single number, the angular sampling density in pixels per degree. On the CID:IQ dataset, which rates the same 690 images at two viewing distances, one set of sub-band weights fitted jointly and evaluated on held-out content reaches a pooled PLCC of 0.834 against 0.787 for SSIM and 0.808 for MS-SSIM; on LIVE Release 2, calibrating the geometry yields 0.956 against 0.946 and 0.950. As a cross-verification, the CID:IQ weights applied unchanged to the Brightcove-Kingston multi-screen video dataset, which rates the same clips on a television, a tablet and a phone, give a pooled PLCC of 0.844 across devices where SSIM and MS-SSIM, which must return one number per clip, fall to 0.62 and 0.59. Accuracy is flat from three channels to six and insensitive to filter shape, window and peak placement; only the channel bandwidths matter, and the psychophysically measured values are a safe choice. The most sensitive parameter is SSIM's own stabilising constant: reducing it to a third raises the pooled PLCC to 0.857. Source code reproducing the results is available.

---


### 194. [Demystifying Classifier-Free Guidance for Auto-Regressive Image Generation](https://arxiv.org/abs/2611.29002)

**<font color=#1a73e8>作者：</font>** Zhiling Zhou, Jiachun Pan, Fengzhuo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classifier-free guidance (CFG) has been widely adopted in autoregressive (AR) models for high-quality image generation. Despite its strong empirical performance, its mechanism in AR models remains unclear. This paper demystifies the mechanism of CFG through both empirical and theoretical studies. By examining the top-ranked semantics of different components in CFG, we show that texture information is primarily encoded in the difference between the conditional and unconditional logits, whereas both logits share previous-token repetition as their leading semantics. This strong repetition semantics obscures the desired texture information, causing greedy decoding from the conditional logits alone to produce nearly pure-color images. Through a training-dynamics analysis of shallow transformers, we prove that this shared repetition semantics does not arise from limitations or failures of pretraining, but instead originates from the texture sparsity of images. We further show that CFG improves generation quality by rectifying this repetition bias during inference. Motivated by the shared semantics between conditional and unconditional logits, we propose Attention Weight Reuse (AttnReuse), which reuses intermediate attention computations from the conditional-logit forward pass to accelerate the unconditional-logit computation. AttnReuse reduces about $25\%$ of attention computation with little performance degradation across different models.

---


### 195. [DoC: Learning to Defer or Commit for Timely, Accurate, and Stable Conversational Diagnosis Prediction](https://arxiv.org/abs/2611.29003)

**<font color=#1a73e8>作者：</font>** Xueren Ge, Anthony Cortez, Homa Alemzadeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conversational diagnosis prediction requires accurate, early, and stable predictions from ongoing clinical dialogue, yet dialogue-level labels do not specify when to commit. We propose a two-phase framework for learning deferral and diagnosis decisions. First, iterative commitment-boundary estimation constructs Defer/diagnosis supervision without annotated commitment times. Second, Defer-aware supervised fine-tuning initializes a policy, refined through reinforcement learning with trajectory-level rewards for timeliness, first-commit accuracy, and post-commit stability. On EMSDialog and MediTOD, DoC commits early, achieving the highest first-commit accuracy among post-trained methods (76.7%/51.2%) and the lowest post-commit error overall (16.4%/48.3%).

---


### 196. [Mirrored Min-of-K Training](https://arxiv.org/abs/2611.29008)

**<font color=#1a73e8>作者：</font>** Jiaru Zhang, Zeyun Deng, Hyunsoo Yun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Min-of-K (MoK) training is widely used to train models that produce diverse outputs from random noise. For each target, it draws K outputs from the model and backpropagates only through the one closest to the target. However, MoK generally does not make the generated distribution match the data distribution. In this paper, we analyze the MoK bias across all values of K and show that tuning K shifts between failure modes, from mode dropping at small K to distribution flattening at large K. We further prove that every nontrivial loss based only on target-candidate distances fails to recover some data distribution, since these distances do not reveal how the candidates are placed relative to each other. Based on these analyses, we propose mirrored MoK (MMoK), a drop-in modification of MoK training that draws one extra sample from the model, applies the closest-candidate selection rule against it, and subtracts the resulting distance. Since this distance is measured between samples of the model, it provides additional information about how the candidates are placed relative to each other. We prove that MMoK can in principle recover data distributions that MoK cannot. We empirically validate MMoK on five scenarios, namely synthetic mixtures, pedestrian and vehicle trajectory prediction, tropical cyclone forecasting, robotic policy learning, and ambiguous medical image segmentation. The results confirm the effectiveness and generality of MMoK in both distribution learning and task performance.

---


### 197. [SenFabric: 3D Printing On-fabric Sensing Mechanisms for Smart Textiles](https://arxiv.org/abs/2611.29016)

**<font color=#1a73e8>作者：</font>** Yao Wang, Mingming Li, Vera Yu Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present SenFabric, a one-step fabrication technique that 3D prints conductive TPU directly onto existing fabric. Rather than compensating for conductive material instability, SenFabric uses geometry-driven resistive structures in which motion changes conductive contact and reconfigures the effective path, producing characteristic signal responses that remain distinguishable despite variation in absolute resistance. We introduce four sensing primitives, slide, press, stretch, and bend, with geometric variables that control activation force, deformation range, and resolution, and a browser-based tool that adapts them to user-supplied outlines and generates routing, pins, and printable models. Four applications demonstrate wearable sensing, human-robot interaction, garment interfaces, and animal wearables, while evaluations show geometry-dominated sensing, cross-motion selectivity, and stable response under repeated use.

---


### 198. [RAGA: Refreshable Animatable Gaussian Avatars from a Single Photo](https://arxiv.org/abs/2611.29026)

**<font color=#1a73e8>作者：</font>** Sadia Mubashshira, John Quarles, Kevin Desai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Avatars created from a single photo are fixed once made: regions the photo never showed, such as the back of a garment, are hallucinated and remain that way. We present Refreshable Animatable Gaussian Avatars (RAGA), a full-body Gaussian avatar that is created from a single image in about one second and can be refreshed whenever new images of the same person become available, without retraining or gradient-based optimization. RAGA maps each new observation into canonical UV space, accumulates it as visibility- and angle-weighted running sums, and re-decodes the fused map with the same decoder used for the photo. Although this decoder is trained only on single images, it makes use of the fused evidence. On 163 clips from five datasets, RAGA created from one photo outperforms LHM, LHM++ and IDOL, including on three datasets never used in training. Refreshing from later frames adds 0.49 dB PSNR overall and 0.68 dB on views turned at least 135° from the photo, where SSIM and LPIPS also improve. Given the same 16 images on all clips, LHM++ gains 0.15 dB, against 0.48 dB for RAGA. Creating an avatar takes 1.08 s and animating it 48.1 ms per frame on a laptop RTX 3080 GPU, with body fitting and matting included in creation and pose estimation included in animation. Code will be released on GitHub.

---


### 199. [T2ISpec: Benchmarking Speculative Decoding for Text-to-Image Generation](https://arxiv.org/abs/2611.29029)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Shatong Zhu, Hui Shen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) generators produce detailed images but remain slow at inference. Speculative decoding can reduce this cost, yet its behavior across the rendering requirements of T2I prompts remains insufficiently understood. We introduce T2ISpec, a benchmark of 1,400 prompts balanced across seven rendering topics and two difficulty levels. It evaluates autoregressive and diffusion/flow accelerators by latency, work performed by the target model, and image quality. Our study reveals three key findings: (1) aggregate results hide large differences between topics, (2) alignment and preference scores can disagree with prompt constraint satisfaction, and (3) large reductions in target work can yield limited latency gains. Motivated by these findings, we propose TopicRoute, a plugin that combines prompt routing with speculative and cache controls without retraining the generator. Across six model--method pairs, it achieves a geometric mean speedup of 1.0308x over the native methods, and the speedup carries over to external prompts with the same settings, while quality gains and losses vary across configurations.

---


### 200. [Do Larger Fully Connected Neural Networks Generalize Better?](https://arxiv.org/abs/2611.29039)

**<font color=#1a73e8>作者：</font>** Mohammad Jalili Torkamani, Suhib Hamid, Moaz N. Ishag  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Greater neural-network capacity does not necessarily yield better performance on unseen data. This study investigates whether a deeper, fully connected neural-network architecture generalizes better than a shallower architecture on the Fashion-MNIST dataset. We compare two architectures under two learning rates and two L2-regularization settings, producing eight configurations. The architectures contain 95,410 and 561,470 trainable parameters, respectively, an approximately 5.9-fold difference. Checkpoints and the final configuration are selected by validation loss, and all configurations are evaluated on a held-out test set. The selected larger configuration achieves 89.82% validation accuracy and 88.77% test accuracy. Selecting the lowest-validation-loss configuration within each architecture yields test accuracies of 88.77% and 88.52%, respectively, a difference of 0.25 percentage points. Across matched training settings, the larger architecture achieves higher test accuracy in only one of four comparisons. Class-level errors are concentrated among visually similar garment categories, and qualitative pixel-removal analyses suggest sensitivity to shape and boundaries. Overall, the findings suggest that increasing architectural capacity alone does not guarantee better generalization, highlighting the importance of considering optimization and regularization when selecting neural-network architectures.

---


> [!TIP]
> 当前位于：**151-200**（第 4/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

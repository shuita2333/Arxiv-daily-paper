# 📦 其他研究 | 2026年10月20日

> 本类共 **213** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-213](./part-05.md)

---

### 151. [Predictable Scaling: Efficient Model Exploration via Scaling-Law Prediction](https://arxiv.org/abs/2610.23453)

**<font color=#1a73e8>作者：</font>** Aishwarya Wesanekar, Sheng-Tao Yang, Jiawei Zhang 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating candidate changes (hypotheses) to recommendation models requires full-scale training runs consuming thousands of GPU-hours, severely limiting the hypothesis space engineers can feasibly explore. We introduce Predictable Scaling (PS), a systematic framework that exploits empirically verified regularity conditions to predict full-scale model performance from small-scale proxies. PS constructs scaled-down variants via composable scaling functions along distinct resource axes, and projects metrics to the target scale via curve fitting with calibrated uncertainty estimates. We compare three prediction strategies of increasing expressiveness: even the simplest (raw proxy) achieves prediction error within the empirical noise floor of repeated-run variance; the most expressive (Gaussian Process) provides an indicative 15% relative MAE improvement and calibrated uncertainty. Evaluation on two ranking models of increasing complexity---a task-specific model and a foundation model---demonstrates that PS correctly ranks actionable hypotheses across diverse hypothesis types at 79-88% compute reductions.

---


### 152. [TriINR: Unsupervised Atmospheric Turbulence Mitigation with Triple Implicit Neural Representations](https://arxiv.org/abs/2610.23454)

**<font color=#1a73e8>作者：</font>** Yuka Ogino, Rikuto Otsuka, Yuho Shoji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Atmospheric turbulence degrades image quality in long-range imaging. The degradation is generally modeled with two spatio-temporally varying components, tilt and blur. Recent unsupervised turbulence mitigation methods have demonstrated the effectiveness of representing a sharp image as an implicit neural representation (INR). However, their tilt and blur representations remain frame-dependent, and the number of optimization parameters grows with the number of input frames. To address this limitation, we propose TriINR, an unsupervised turbulence mitigation method that recovers a sharp image from multiple degraded frames. TriINR represents the sharp image, tilt, and blur as three implicit neural representations. By modeling tilt and blur as spatio-temporal INRs, TriINR achieves frame-count-independent degradation representation and memory-efficient optimization. We further incorporate physical and statistical properties of atmospheric turbulence as constraints on the INRs to improve restoration accuracy. Experiments on synthesized turbulence data with three degradation strengths show that TriINR restores images more robustly across varying turbulence strengths than prior TM methods and achieves the highest accuracy among the evaluated unsupervised methods. Our method also demonstrates robustness on real long-range scenes containing additional non-ideal motion.

---


### 153. [A low-dimensional dynamical basis for tongue shape control](https://arxiv.org/abs/2610.23456)

**<font color=#1a73e8>作者：</font>** Sam Kirkham, Patrycja Strycharczuk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech production involves the control of a high-dimensional articulatory system with many degrees-of-freedom, but a widespread hypothesis is that speakers navigate this complexity using a set of lower-dimensional control variables. Common candidates for these control variables include individual articulators (e.g. tongue body) and abstract tract variables (e.g. tongue body constriction location), but identifying the most appropriate coordinate system for articulatory control remains an open question. In this study, we advance a model in which holistic tongue shape modes represent a potential low-dimensional control basis for a simple dynamical law. We first discover empirical tongue shape modes in a cross-speaker coordinate space and then fit the model to ultrasound data on monophthongal vowels from 36 speakers of British English. A three-dimensional linear point attractor fitted to these time-varying modes recovers the dynamics of tongue shape with a high degree of accuracy. This suggests that complex tongue movement can arise from independent modes that linearly combine under simple dynamical laws, thereby relocating some complexity from the control signal to the coordinate system. We show that this framing explains why one-dimensional articulatory measures can exhibit observable nonlinearities, and hypothesize that shape modes are a plausible kinematic expression of underlying muscle synergies.

---


### 154. [TAN: A Size- and Form-Adaptive Masked-Convolution Encoder for Tissue Graphs](https://arxiv.org/abs/2610.23475)

**<font color=#1a73e8>作者：</font>** Jan Herschel, Anselm von Gladiss  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tissue graphs represent histology images as graphs over tissue-conforming superpixels, which keeps homogeneous tissue regions intact instead of cutting them into rectangular patches. To embed superpixels, current encoders crop them to bounding boxes and then pad, resize, or mask them, so background or fill values can leak into the node features. This matters in practice, and especially in medical imaging, where a prediction should depend on the tissue and not on an arbitrary preprocessing choice: on BACH, changing only the fill of the masked region shifts the accuracy of frozen encoders by up to 6 percentage points, larger than the differences among the four best encoders under mean fill, and the preferred fill differs between datasets, so it cannot be fixed once and for all. We present TAN (Tissue-Aware Network), a compact convolutional encoder (0.41M parameters) that processes each superpixel at its native shape and extent and excludes background from every operation, which makes its embeddings exactly invariant to the fill by construction. Under identical masks and an identical graph classifier, TAN's accuracy on BACH is not significantly different from that of the 303M-parameter foundation model UNI (81.1% vs. 80.7-82.6%, depending on the fill), with ~740x fewer parameters, ~1,190x fewer FLOPs, and no pretraining. On BRACS, TAN is close to a ResNet18 trained under the same protocol and trails the histopathology foundation models. An ablation with TAN's architecture but standard processing of fill-padded crops shows that masking keeps accuracy similar (nominally higher on BACH, lower on BRACS, within noise) at less than half the FLOPs.

---


### 155. [A Topological Signature of Learning under Noisy Labels](https://arxiv.org/abs/2610.23491)

**<font color=#1a73e8>作者：</font>** Zhongtian Sun, Fan Mo, Prayag Tiwari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How does noisy supervision change the representations learned by a neural network? Training accuracy measures agreement with training labels but provides little information about representation geometry. We use persistent homology to track loop structure across distance thresholds in neural activations. Experiments span image classification, text classification, and modular arithmetic. On a fixed CIFAR-10/ResNet-18 training probe, equally sized clean-label and corrupted-label subsets show no detectable persistence difference at epoch 10, whereas corrupted-label subsets have higher persistence at epoch 50. The contrast survives uniform-scale controls, even though predictions match the assigned noisy labels for only 7-11% of corrupted probe examples at that checkpoint. Normalisation preserves the crossover between clean and noisy training trajectories on CIFAR-10/ResNet-18, whereas CIFAR-100/ResNet-18 shows no crossover under any of the five evaluated constructions. In a separate noise-rate calibration comparison across five pipelines, mean activation norm achieves a higher mean in-sample R2 than raw persistence (0.936 versus 0.908). These findings show that noisy supervision leaves a measurable geometric signature even when agreement with corrupted labels is low. Comparing persistence under scale controls with label-fitting measurements offers a way to study how representations respond to label corruption beyond what training accuracy reveals.

---


### 156. [Uncertainty-aware AI-enabled framework for predicting hydrogen dispersion in confined spaces to enhance operator situational awareness](https://arxiv.org/abs/2610.23515)

**<font color=#1a73e8>作者：</font>** Niclas Flehmig, Mary Ann Lundteigen, Shen Yin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a two-stage AI-enabled framework for enhancing operator situational awareness during compressed hydrogen bunkering in maritime confined spaces. In the event of a leak, the framework first estimates the unknown leakage rate from early sensor readings and then forecasts how the hydrogen cloud will disperse over the next time steps, providing operators with a predicted concentration map together with confidence bounds. The framework is based on two independent AI models building one AI system. The AI system is designed as a decision-support tool. It augments sensor readings, and thus enhances operator situational awareness and supports decision-making. This enables preventive safety barriers to be deployed before hazardous concentrations are reached, while an independent emergency shutdown system remains the ultimate safety layer. The system design incorporates safeguards to ensure the AI system operates within its competence envelope. Trained and tested on an open dataset of confined-space hydrogen releases, the framework achieves a mean absolute error of $0.052$~g/s in leakage-rate estimation and $\approx0.018$ in hydrogen-concentration prediction, approaching the sensor precision bound of $\pm0.01$. The hydrogen-concentration prediction provides well-calibrated uncertainty estimates that allow operators to judge the reliability of each forecast. These results suggest that the framework may provide early information about hazardous concentration build-up, potentially supporting preventive actions by operators.

---


### 157. [PONDER: Learning to Generate in the Right Order](https://arxiv.org/abs/2610.23531)

**<font color=#1a73e8>作者：</font>** Julius Erbach, Dominik Narnhofer, Bernt Schiele 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce PONDER, a method that learns in which order an image generator should fill in content and which of its earlier predictions to revise. Masked generative models construct a sample by repeatedly filling in subsets of missing variables. The order of these partial predictions determines the context available in subsequent steps and therefore affects the quality of the final sample. Common strategies are to choose the order randomly or based on local confidence estimates. Conditioned on the partially generated sample and the generator's features, our policy chooses which positions to fill next and/or which previously filled positions to mask for later regeneration, a mechanism we call rethinking. In this way, the generation process is able to adapt to the evolving context and also to revise earlier predictions. We optimize the policy using group-relative policy gradients, with rewards that measure constraint satisfaction, human preference, or distribution quality. For the latter, we introduce FIDgrad, an image-level reward derived from the (first-order) change in Fréchet Inception Distance caused by adding a generated sample to the current feature distribution. With the generators frozen, learned ordering reduces MAR-B ImageNet FID from 4.09 to 2.78 and raises the accuracy on hard visual Sudokus from 3.9\% to 56.6\%, surpassing uncertainty-based greedy ordering (38.7\%). Rethinking further improves these results to 2.70 FID and 96.7\% accuracy, while increasing the rethinking budget of a fixed policy yields continued improvements at inference time.

---


### 158. [ReVision: Reprogramming Image Generators for Dense Visual Perception](https://arxiv.org/abs/2610.23533)

**<font color=#1a73e8>作者：</font>** Yitong Yang, Yinglin Wang, Xuexin Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent image generators exhibit rich visual priors that can support dense visual perception. However, existing approaches typically encode multiple perception tasks into a shared parameterization, making joint training sensitive to the mixture and weighting of heterogeneous data and prone to cross-task interference. To address this issue, we introduce ReVision, an instruction-conditioned parameter generation framework built on a frozen multimodal understanding model and a frozen image generator. Given an image and a free-form instruction, the understanding model jointly encodes them into a multimodal image--instruction representation, which a trainable parameter generator maps to transient low-rank updates for the generator. Each image--instruction pair induces a distinct set of transient prediction parameters, enabling instance-specific adaptation while both pretrained backbones remain unchanged. ReVision requires no task-specific heads, explicit task identifiers, or stored adapters. A shared RGB output interface unifies segmentation, depth estimation, and surface-normal prediction. Across diverse dense prediction benchmarks, ReVision achieves competitive performance with state-of-the-art methods while supporting flexible task specification through natural-language instructions. Our analysis further reveals substantial gradient disagreement across tasks, highlighting the conflict introduced when heterogeneous objectives share a single parameterization. Meanwhile, the generated updates exhibit structured task- and input-dependent organization in weight space, further validating instance-level parameter generation for multi-task perception.

---


### 159. [PreciseEdit: Strong Yet Stable Semantic Transport for One-Step Image Editing](https://arxiv.org/abs/2610.23535)

**<font color=#1a73e8>作者：</font>** Jingyi Wang, Xiao Lu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent one-step text-to-image (T2I) models enable efficient image synthesis, opening up new possibilities for interactive Web-based image editing. However, existing one-step editing methods often construct a global transport field through simple vector operations between conditional predictions. While such strong transport can effectively drive the image toward the target semantics, it may be released along unreliable directions or over non-edited regions, leading to structural distortions within the editing region and background drift elsewhere. More importantly, stabilizing the editing process through global smoothing or uniformly weakening the transport field often makes large semantic changes overly conservative. In this work, we revisit one-step image editing from the perspective of the tension between semantic strength and transport stability, and identify a key insight: strong semantic transport is not inherently unstable. What matters is whether it is applied along reliable directions and at reliable spatial locations. Motivated by this insight, we introduce PreciseEdit, a model-agnostic, training-free and inversion-free one-step editing framework that strengthens target-semantic alignment while preserving background fidelity and structural consistency. We further propose a dual-noise-scale role decomposition strategy: a higher-noise scale produces the strong target-directed transport used for actual editing, whereas a lower-noise scale jointly serves as a probe for directional agreement and spatial structure. Extensive experiments on PIE-Bench demonstrate that PreciseEdit achieves state-of-the-art performance and effectiveness on various editing tasks.

---


### 160. [PanoBench: A Panoptic Occupancy Prediction Benchmark for Autonomous Driving](https://arxiv.org/abs/2610.23537)

**<font color=#1a73e8>作者：</font>** Yi Feng, Zizhan Guo, Junwu E 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoptic occupancy unifies 3D geometry, semantics, and instance identities, but its development is limited by scarce instance-aware annotations. Existing benchmarks mainly provide semantic labels reconstructed from incomplete sensor observations, while panoptic datasets have limited domain coverage or annotation completeness. We introduce PanoBench, a camera-centric panoptic occupancy prediction benchmark spanning synthetic and real-world driving scenes. It combines PanoBench-CarlaOcc, PanoBench-nuScenes, and PanoBench-KITTI360 through canonical data interfaces and unified evaluation protocols, providing multi-resolution annotations with persistent instance identities. The synthetic branch derives complete panoptic geometry from simulated meshes. For real-world data, a new pipeline reconstructs backgrounds using geometric priors and topology constraints, generates foreground mesh assets from multi-frame multi-view images, and fuses them into sparse panoptic voxels. A unified valid-mask protocol evaluates complete thing instances supported by temporal observations while scoring stuff regions at the voxel level. Analyses of observation fidelity, geometric completeness, spatial continuity, and temporal consistency demonstrate the benefits of the resulting annotations over existing occupancy benchmarks. We benchmark representative methods on semantic occupancy prediction, panoptic occupancy prediction, and 4D occupancy forecasting, and study voxel resolution, synthetic-to-real transfer, and storage efficiency. These results reveal complementary strengths of volumetric and ray-based metrics and persistent challenges in real-world instance-aware prediction. PanoBench is available at this https URL.

---


### 161. [Execution Before Memory: Diagnosing Memory Failures in Video World Models](https://arxiv.org/abs/2610.23542)

**<font color=#1a73e8>作者：</font>** Weiyang Jin, Jiwen Yu, Sihan Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A memory test for a video world model should say whether the scene was set, whether the asked change was carried out, and whether the last frame shows the result. Current tests fold these into one number, so a low score is easy to read as forgetting. When the change is not carried out, the hidden state transition cannot appear, so the test is not really a test of memory. We introduce MIST, an evaluation that separates the change from the memory it should leave behind. The model first sets the scene while the change stays hidden, and only later is asked to show it, with leakage before that point kept under control. This separation locates the bottleneck: the model sets the scene but does not carry out the instructed change. The same gap appears in general memory evaluations. On that basis we propose M3-Agent (Make the Missing Move), which recursively revises the details of the input instruction so that the model successfully carries out the requested instruction. Relative to the baseline, it more than triples the MIST reveal score. On the benchmarks, WRBench's score T rises by 26.1% and MBench-T's score U by 52.7%. The method meets the problem from the execution side: it shows what the frozen model can do once the move is stated, and it sets a stricter baseline.

---


### 162. [LiveSync: Iterative Self-Training for Lip-Sync Generation](https://arxiv.org/abs/2610.23558)

**<font color=#1a73e8>作者：</font>** Huaishao Luo, Huan Zhang, Guanbo Bao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-driven lip synchronization aims to match target speech through localized mouth and jaw articulation while preserving subject identity, head pose, and surrounding facial context. Naturally recorded videos provide synchronized reconstruction targets but rarely offer pairs that are matched in identity and pose yet differ primarily in speech-related articulation. Mask-based training enables reconstruction from these videos, but random-reference inputs differ from the aligned self-reference used at inference. We present LiveSync, an iterative self-training framework in which a single mask-based model generates pseudo pairs and is refined for deployment. The model is first trained on a curated real-video corpus augmented with externally generated clips covering under-represented visual conditions. A frozen checkpoint then uses independently sampled audio to generate mouth-edited references from real-video frames, copying pixels outside the edit mask from each source frame. After confidence filtering, these references are paired with aligned masked inputs and original real-frame targets. The retained pseudo pairs are mixed with real training data to refine the same model from its current weights, updating training supervision without adding inference stages. Although we instantiate the framework with a single-pass GAN-based model, the self-training strategy could in principle also be adapted to diffusion-based models. Experimental results show that LiveSync achieves leading synchronization performance on HDTF and competitive performance compared with the baselines on the AIGC-LipSync subset, while maintaining low inference latency.

---


### 163. [Beyond Expected Values: Risk-Sensitive Planning with Distributional Monte-Carlo Tree Search](https://arxiv.org/abs/2610.23565)

**<font color=#1a73e8>作者：</font>** Quynh Trinh, Trung Nguyen, Nam Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monte-Carlo Tree Search (MCTS) typically stores only scalar mean estimates, which makes it poorly suited for tail-risk objectives such as conditional value-at-risk (CVaR). We introduce Categorical Thompson Sampling with Optimism (CATSO) and Particle Thompson Sampling with Optimism (PATSO), two distributional MCTS algorithms that maintain finite-support empirical backup laws at Q-edges. CATSO represents Q-edge laws with categorical atoms and Dirichlet Thompson sampling, while PATSO represents them with adaptive particles. Both algorithms select actions using the CVaR of a Thompson-sampled Q-edge law plus a polynomial optimism bonus, and propagate scalar continuation values through visit-weighted averages of child Q-edge CVaR scores. For the finite-depth nested CVaR planning target, we prove an $O(n^{-1/2})$ bound on the root value error after $n$ rollouts, which upper-bounds the risk-sensitive simple regret. CATSO adds a fixed-grid discretization bias, while capped PATSO adds a tunable Wasserstein compression bias. Experiments on stochastic planning benchmarks show that distributional Q-edges improve lower-tail return and reduce catastrophic outcomes when mean-optimal and risk-sensitive behavior differ.

---


### 164. [From Adult Renal Masses to Pediatric Wilms Tumors: Evaluating Cross-Domain Generalization of Kidney Lesion Segmentation on MRI](https://arxiv.org/abs/2610.23568)

**<font color=#1a73e8>作者：</font>** Sarah de Boer, Myrthe A. D. Buser, Hartmut Häntze 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning segmentation models for pediatric oncology are often trained on small, single-center cohorts, whereas much larger datasets exist for adult diseases, such as kidney cancer. Whether models trained on adult renal lesions generalize to pediatric Wilms tumors remains unclear. We trained a segmentation model on single-sequence T1- or T2-weighted adult kidney MRI and evaluated it on a held-out adult test set and a pediatric Wilms tumor cohort, where it was compared with a pediatric-specific nnU-Net. Segmentation performance was quantified using the Dice similarity coefficient (DSC) and 95th-percentile Hausdorff distance. On the adult test set, the model achieved a median DSC of 0.86 for renal lesions. On the pediatric cohort, the adult-trained model achieved a median DSC of 0.85 compared with 0.90 for the pediatric-specific model. Despite differences in age, anatomy, and tumor type, the adult-trained model showed promising performance on pediatric Wilms tumors, with only a modest difference in median DSC compared with the pediatric-specific model. However, non-inferiority could not be shown, highlighting the value of pediatric training data. In future work, a fine-tuning strategy could be explored.

---


### 165. [CLEAR: Cooperative Latent Flow for Visual Counterfactual Explanations with Accurate Region Preservation](https://arxiv.org/abs/2610.23577)

**<font color=#1a73e8>作者：</font>** Yan Zeng, Changlu Guo, Oskar Kristoffersen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual counterfactual explanations (VCEs) should alter a classifier's prediction while remaining realistic and preserving decision-irrelevant content. Image-space methods provide high-quality counterfactuals but are computationally costly, whereas latent-space methods are more efficient but often less faithful. We identify two sources responsible for this gap. First, latent generation recovers a natural sample from a perturbed representation, whereas classifier guidance pushes it toward a target class, so their update directions may oppose. Second, VAE reconstruction can alter regions that should remain unchanged. We introduce CLEAR, a latent Flow Matching framework for VCEs. CLEAR uses Flow Matching's explicit instantaneous velocity as a reference for the generative direction to decompose classifier guidance into cooperative and conflicting components. It preserves the cooperative component and adaptively attenuates only the conflicting one according to conflict strength. We further analyze conflict frequency and strength throughout generation to reveal how classifier guidance interacts with the generative process. CLEAR also dynamically identifies editable regions, constrains latent modifications, and directly preserves factual content outside them to reduce VAE-induced changes. Across five bidirectional tasks on two datasets, CLEAR retains latent-space efficiency while achieving counterfactual quality comparable to or better than strong image-space baselines, with a 2.5x speedup over the strongest baseline. Project page: this https URL

---


### 166. [SemPurify: Semantics-Aware Data Purification for Black-box Backdoor Defense](https://arxiv.org/abs/2610.23589)

**<font color=#1a73e8>作者：</font>** Jiawei Yu, Syed Irfan Ali Meerza, Yi Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks have emerged as a critical security threat in machine learning, where adversaries embed triggers within poisoned training samples to manipulate a model's predictions on targeted inputs while leaving its general behavior unaffected. This stealthy nature makes backdoor attacks difficult to detect, as the model functions normally until activated by a specific malicious trigger. Current purification-based defenses use image transformations (e.g., blurring) to disrupt trigger patterns but often degrade image quality. Even with advanced restoration techniques like diffusion models, these approaches can still alter visual or semantic information, reducing utility for downstream tasks. To address this, we propose the first semantics-aware data purification framework for black-box backdoor defense, SemPurify, which explicitly incorporates multi-level semantics (i.e., low-level semantic embeddings and high-level image tags) within a text-to-image (T2I) framework to guide image restoration during purification. Using this semantic information, the T2I model subsequently refines the transformed samples, helping preserve visual details and semantic information during restoration. Extensive experiments spanning multiple backdoor scenarios, i.e., classification models, CLIP-style encoders, and generative models, demonstrate that SemPurify reliably removes backdoors while effectively preserving semantic information for downstream tasks.

---


### 167. [Learning to Discriminate Scene Structures Makes Self-Supervised Depth Learning Scalable](https://arxiv.org/abs/2610.23600)

**<font color=#1a73e8>作者：</font>** Mengtan Zhang, Yuchuan Cui, Yu Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised monocular depth estimation is appealing for its potential to scale with unlabeled data, yet existing methods often degrade when trained on diverse scenes. This study finds that, under self-supervision, models tend to encode dataset-specific structural biases rather than transferable scene geometry, leading to cross-domain optimization conflicts. To address this issue, this study proposes the MaSS framework, aiming to make self-supervised depth learning scalable to diverse data. MaSS introduces a dedicated structural representation pathway explicitly decoupled from contextual features, which is guided by a novel scene-structure discrimination objective to learn generalized, layout-aware structural representations for depth decoding. Trained and evaluated on four diverse datasets, both individually and jointly, MaSS substantially outperforms prior self-supervised methods and is the first to consistently benefit from mixed-domain training. Zero-shot evaluation on eight additional datasets further demonstrates its remarkable generalizability, particularly on those entirely out-of-distribution scenes. The source code is publicly available at this https URL.

---


### 168. [When Magnitude Suffices: Reconstructing Time-Domain-Gated Microwave Signals Without Phase on a Thoracic Phantom](https://arxiv.org/abs/2610.23608)

**<font color=#1a73e8>作者：</font>** Maciej Cichoń, Patrycja Gołaś, Maksymilian Bartosik 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-domain gating separates the arrivals that form a microwave S-parameter measurement. It requires the measurement of complex values, so this application almost always uses a vector network analyzer (VNA). We show that, on one calibrated measurement configuration, the gated magnitude the VNA would give can be reconstructed from a magnitude-only sweep of a spectrum analyzer with a tracking generator (SA). We select the gate center for separability of the measured states, correct each instrument once by a per-bin subtraction of a reference state, and train a fully connected network on sweeps from both instruments. The test object is a torso phantom with lung-shaped compartments whose filling takes eleven dielectric states, each held out in turn. On $S_{11}$ the reconstruction from SA input reaches a shape error of 0.08 dB$^2$ with a state ordering of 0.81. This matches the reconstruction from VNA input. On $S_{21}$ it reaches 0.82 dB$^2$ and keeps the ordered groups of the states. An explicit phase prediction performs much worse, because gating needs the phase to about 0.2 rad RMS. Across eleven measurement configurations the dependence of phase on magnitude is strong for reflection and weak for transmission. This explains the difference between $S_{11}$ and $S_{21}$. Where the magnitude carries enough of the phase, a scalar instrument gives the gated response without any phase measurement after installation. On the open UM-BMID breast data set, with whole phantoms held out, the shape error of the network is 30 percent lower than that of a per-bin linear map.

---


### 169. [ADA 2025: A Multimodal Dataset for Water-Deficit Stress Detection in Sugar Beets](https://arxiv.org/abs/2610.23609)

**<font color=#1a73e8>作者：</font>** Piper Powell, Robert Franz, Amos Smith 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Research and development into artificial intelligence (AI) and machine learning (ML) applications in crop management are hindered by a lack of suitable public datasets. Whereas applications in disease and pest detection benefit from a comparatively higher amount of available data, applications like water-deficit stress detection often have very few if any public datasets available. Moreover, most datasets that are available are single-modality and frequently RGB-only, leaving the early detection and enhanced performance offered by other methods, and particularly by multimodal approaches, out of reach. Datasets with accurate metadata, higher numbers of plants, and smaller intervals between data points are also scarce. To address this, we publicly release ADA 2025, a >500 GB comprehensive multimodal dataset of young sugar beet plants under healthy and water-deficit conditions combining thermal, hyperspectral, RGB, and depth imagery along with relevant environmental and metadata and both relative water content (RWC) and leaf thickness as ground truth sources. Exemplary results showcase the dataset's validity in terms of differences detectable between stressed and healthy plants.

---


### 170. [How Many, but How Sure? Class Competition as a Confidence Proxy in Multi-Class Density-Based Counting](https://arxiv.org/abs/2610.23611)

**<font color=#1a73e8>作者：</font>** Villanelle O'Reilly, Georgios Leontidis, Marc Hanheide  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-class density estimators can count objects in crowded scenes, but their class-wise outputs offer no indication of how reliably density mass has been allocated. We introduce a training-free confidence proxy based on local competition between the strongest class channels. The resulting prominence measure requires only the predicted density maps, with no retraining or access to model internals. We test whether residual competition is diagnostic of cross-class leakage by attenuating contested density at inference time. On DSACA predictions for the Hicks et al. dataset, this reduces overall MAE from 0.920 to 0.846, suggesting that class competition contains useful information about count reliability.

---


### 171. [Trajectory-Triggered Sparse Collaborative Decoding](https://arxiv.org/abs/2610.23613)

**<font color=#1a73e8>作者：</font>** Amit Ranjan Trivedi, Sruthikesh Surineni, Kyong Ho Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dense assistance methods such as speculative decoding repeatedly verify draft tokens with a target model, keeping target computation coupled to generation. We study sparse collaborative decoding, where a draft model generates most tokens and a target model is invoked only for short corrective segments. The key problem is deciding when to call the target. We show that local uncertainty is a weak trigger: entropy, negative log-likelihood, logit margin, top-$k$ mass, and velocity features give near-chance failure prediction, with AUC 0.50-0.53. In contrast, aggregate trajectory-shape features over the draft confidence path reach AUC 0.86 using a lightweight logistic predictor trained only from draft correctness labels. This induces a trigger-timing tradeoff: early calls have more leverage but weaker evidence, while later calls have stronger evidence but less ability to redirect the trajectory. Used online, learned sparse collaborative decoding improves over the best open-loop schedule by +5.3 to +20.0 accuracy points across five GSM8K draft-target pairs. On MATH-500, it gains 7.0-13.5 points when early prediction and target competence align, but loses when either is weak. On StrategyQA, it improves over open-loop by 5.0-8.3 points, showing transfer beyond arithmetics.

---


### 172. [The Sign Code: The Hidden Binary Nature of Deep Networks](https://arxiv.org/abs/2610.23616)

**<font color=#1a73e8>作者：</font>** Niclas Göring, Shuofeng Zhang, Roi Holtzman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every neuron in a trained network outputs a number that can be separated into its sign (positive or negative) and its magnitude (absolute size). We call the set of all neuron signs the \textit{sign code}. This raises a key question: does classification depend more on the sign code or on the magnitudes? For overparameterized vision classifiers with sign-preserving activations, the answer is overwhelmingly the sign code. A $k$-nearest neighbor classifier operating only on this binary sign code achieves accuracy comparable to the full model across different architectures, activation functions, and datasets. Moreover, replacing all magnitudes in every layer with random noise while keeping the original signs barely changes residual network performance. In contrast, flipping just 20\% of the signs reduces accuracy to chance. Models generalize well when same-class inputs share similar sign codes. When this overlap is disrupted by a regularizer, training accuracy remains high, but test performance collapses. A margin decomposition helps explain these results: the sign-only contribution to each logit grows as $\sqrt{d}$ in network width, dominating the magnitude residual. The natural unit of analysis for these networks may not be through their continuous weight space but instead through their discrete sign codes.

---


### 173. [GEMS: Molecular Structure Elucidation as Learned Search over Isomer Graphs](https://arxiv.org/abs/2610.23617)

**<font color=#1a73e8>作者：</font>** Utku Umur Acikalin, Yingheng Wang, Goncalo J. Gouveia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Identifying small-molecule structures from molecular formulas and tandem mass spectra remains a bottleneck in untargeted metabolomics and natural-product discovery. Even when database retrieval or de novo prediction misses the exact structure, the resulting candidates can provide starting points for exploring nearby structures through a few bond edits. We introduce GEMS (Guided Editing of Molecular Structures), which refines candidates through learned 2-switch bond edits that preserve the molecular formula and each atom's total valence. GEMS uses MIST, a pretrained spectrum-to-fingerprint model, to predict fingerprint probabilities once per spectrum. A neural policy compares each candidate's fingerprint with these predictions, links present features to the atoms and bonds that generate them, and scores all valid edits in one forward pass. The policy is trained on shortest edit paths between structures, so it can be pretrained on PubChem isomers without spectra and then fine-tuned with spectrum-predicted fingerprints. At inference, GEMS searches from multiple initial candidates matching the supplied molecular formula and ranks candidates by fingerprint agreement and multi-start consensus. With the target structure excluded from PubChem initialization, three edit rounds achieve Hit@1/Hit@10 of 29.64%/50.81% on NPLIB1 and 30.22%/41.33% on MassSpecGym, exceeding published baselines under comparable settings. On NPLIB1, GEMS achieves higher identification accuracy in about 3.3 minutes end to end, compared with 26.2 hours for our FRIGID run. GEMS also improves identification from generated candidates, including those refined by FRIGID. Experiments with exact target fingerprints identify fingerprint prediction error as a bottleneck in target recovery and final ranking. Deeper search recovers additional targets without retraining, with larger gains from weaker initial candidates.

---


### 174. [GRAFT-EEG: Gauge-Aware Physical Field Transport for Cross-Dataset Motor-Imagery EEG](https://arxiv.org/abs/2610.23620)

**<font color=#1a73e8>作者：</font>** Ying Zhou, Mengting Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-dataset EEG decoding often treats montage, reference, and active-sensor changes as representation shift, although they also alter the observation operator. We study target-statistics-blind transfer: fitting receives no target signal, label, or empirical statistic, and electrode coordinates only instantiate a fixed prediction operator. method removes the active-set common-reference gauge and transports each native mask through a template motor leadfield. A source-fitted spectral classifier anchors the decision; a bounded state-space-model (SSM) residual is secondary. We establish restricted identifiability and an operator-perturbation bound. Across five leave-one-dataset-out targets (253 participants), dynamic method achieved 60.865% equal-target balanced accuracy versus 52.684% for strict-clean 5/5 BIOT (hierarchical difference +8.182 points; 95% CI +6.382 to +10.196; positive in every target). On four EEGPT-clean targets, the descriptive means were 61.520% and 59.057%. In four post-hoc exact same-parent tests, FULL exceeded coordinate-basis, matched-spectrum, row-shuffled, and wrong-anatomy controls by 9.959, 9.698, 11.241, and 3.985 points, respectively (all 95% CIs excluded zero; Holm-adjusted P<0.001). A separate 60-participant same-paradigm evaluation retained a positive physical-operator contrast (+4.029 points; +2.338 to +5.773), whereas dynamic--static was inconclusive; its preregistered status is partial confirmation rather than unrestricted external validation. The SSM added +1.059 points (+0.013 to +1.892). Claims remain bounded to five binary motor-imagery domains and the tested operators.

---


### 175. [Stereo LWIR-RGB Automatic Labeling for Low-Light Camera-Based VRU Detection](https://arxiv.org/abs/2610.23621)

**<font color=#1a73e8>作者：</font>** Dimitrios Bouzoulas, Pyry Jäppinen, Pejman Habibiroudkenar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> VRU detection in low-light conditions is a key component in ensuring VRU safety during the most collision prone time of the day. Currently, advances in low-light detection are limited due to the lack of large scale datasets and automated labeling methods. Most autolabeling methods use RGB detections as their labels source, which cannot be replicated in low-light conditions. To fill this gap in this paper we present an automated pipeline for low-light VRU labeling. We use LWIR-RGB image pairs and source our labels from LWIR as VRUs differentiate from the background due to their body temperature. Unlike our previous work that relied on a complex hardware setup to align the two modalities, we perform this experiment using a LWIR-RGB stereo setup, lowering hardware complexity and cost, making the pipeline easier to reproduce. We evaluate method end-to-end on a dataset collected in the capital region of Finland. Models trained on our generated labels beat both off-the-shelf baselines and models fine tuned on a hand labeled subset on F1, mAP@50 and LAMR metrics when tested on a manually labeled dataset, and the result holds for two different LWIR detectors. This shows that low-light VRU autolabeling can be made both accessible and effective without specialized alignment hardware.

---


### 176. [Deconstructing Multi-Task Active Learning: The Paradox of Gradient Conflict and Orthogonal Decomposition](https://arxiv.org/abs/2610.23623)

**<font color=#1a73e8>作者：</font>** Juho Jung, Seongjae Kang, Jinyoung Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing multi-task active learning (MTL-AL) methods predominantly rely on linear scalarization of heterogeneous objectives such as uncertainty, diversity, and gradient conflict. We argue that this entangled formulation is fundamentally limited, as linear combination fails to capture Pareto-optimal trade-offs under conflicting objectives. We propose a shift from combination to deconstruction and introduce a principled framework that rethinks MTL-AL along three orthogonal dimensions. First, we identify the Conflict Paradox: although the optimization literature treats gradient conflict as interference to be suppressed, penalizing conflict when ranking candidates is measurably worse than not scoring it at all. We therefore decouple the two concerns: the acquisition function does not score conflict, and the resulting interference is resolved by gradient surgery during training. Second, we introduce Orthogonal Decomposition, separating acquisition into Informativeness and Exploration. This two-stage process, informativeness filtering followed by coverage maximization, prevents "diversity dilution" by excluding uninformative outliers before enforcing diversity. Third, we propose Cross-Task Mutual Information (CTMI), a covariance-based statistic of cross-task dependency computed from MC-dropout task entropies. Extensive experiments on COCO, Cityscapes, and NYUv2, including comparisons against recent MTL-AL and data-selection baselines, demonstrate consistent improvements over state-of-the-art methods, highlighting that structural rethinking of acquisition yields larger gains than incremental heuristic design. Code is available at this https URL.

---


### 177. [No-Regret Language Generation](https://arxiv.org/abs/2610.23641)

**<font color=#1a73e8>作者：</font>** Jiaxun Li, Vinod Raman, Ambuj Tewari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce no-regret generation, which requires a generator to make a sublinear number of mistakes uniformly over all demonstration sequences and compatible target languages. We also formulate an agnostic variant that allows arbitrary demonstrations that may not be compatible with any languages. For both settings, we introduce tree-based mistake-forcing dimensions that exactly characterize finite-horizon minimax complexity and establish necessary and sufficient conditions for no-regret generation. Our characterizations reveal a rich spectrum of generation rates: up to constant rescaling, every admissible nondecreasing profile is attainable in both the realizable and agnostic settings. Finally, we connect generation complexity to online prediction: for language classes of finite Littlestone dimension \(d\), we obtain realizable mistake bounds of \(O(d\log(1+T/d))\) and agnostic regret bounds of \(O(\sqrt{dT\log(1+T/d)})\). The realizable bound is optimal up to universal constants.

---


### 178. [Diversity Without Labels: Task-Agnostic Coreset Selection Across Perception and Action](https://arxiv.org/abs/2610.23642)

**<font color=#1a73e8>作者：</font>** Julia Hindel, Benjamin Ramtoula, Kyuhwan Yeon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While data collection for model training is relatively easy, curating high-quality datasets from large collections is inherently challenging. Coreset estimation methods address this problem by identifying the best data subsets to train models on. However, existing approaches often require proxy model training, extensive annotations, or task-specific tailoring. Unsupervised alternatives typically exploit geometric properties in foundation model feature spaces, but are limited to pairwise image-to-image comparisons or comparisons against a fixed subset. We introduce CoreDNA, an unsupervised, task-agnostic coreset estimation approach that pools neuron activations from vision foundation models into per-image and per-dataset distributions. By comparing each image's distribution to the dataset-level distribution, CoreDNA can capture both low-level visual structure and high-level semantic information across layers. We find that high-quality samples concentrate in the tails of the last layer's activation statistics, which we validate by relating them to training-based coreset methods. Building on these findings, we develop a computationally efficient selection mechanism to construct task-agnostic, high-quality coresets for selective annotation and model training. Across image classification, semantic segmentation, depth estimation, and imitation learning for end-to-end driving and mobile manipulation, CoreDNA matches or outperforms the state of the art, demonstrating unprecedented generalization across perception and action tasks. These results highlight the effectiveness of compact activation-based representations for data selection.

---


### 179. [JAXtari: High-Throughput and Easy-to-Modify Arcade Learning Environment](https://arxiv.org/abs/2610.23650)

**<font color=#1a73e8>作者：</font>** Quentin Delfosse, Raban Emunds, Paul Seitz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Arcade Learning Environment (ALE) has been a cornerstone of Deep Reinforcement Learning research, providing a standardized benchmark for evaluating general agents. However, its lack of native support for object-extraction and environment modification restricts research into evaluating whether agents learn robust causal models or rely on brittle visual heuristics. Furthermore, the ALE's dependence on CPU-based emulation creates a significant bottleneck in modern GPU-accelerated training pipelines, limiting both experimental scale and iteration frequency. In this work, we introduce JAXtari, an open-source, high-performance reimplementation of Atari 2600 environments. By leveraging massive GPU parallelization, JAXtari allows PPO agents to finish training on 100M environment steps on a single A100-GPU in under an hour. Beyond speed, it provides object-centric observations and a flexible modification system, allowing researchers to, e.g. develop neuro-symbolic methods or discover novel shortcuts and subsequently train and adapt their agents rapidly, sometimes in only minutes.

---


### 180. [In Human Memories. Technology, Creativity and Self-Determination: An Ethical Proposal](https://arxiv.org/abs/2610.23651)

**<font color=#1a73e8>作者：</font>** Francesco Vitucci, Giuseppe Silvi, Francesco Abbrescia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This research investigates the role of artificial intelligence (AI) in modern compositional practices, with a particular focus on two case studies: Convergence (2020/21) by Alexander Schubert, for String Ensemble and AI System, and In Human Memories (2024) by Francesco Vitucci, for four cellos and one electroacoustic player, whose installation was created by the Electronic Music School of the "N. Piccinni" Conservatory of Bari. The initial historical survey traces the evolving use of technology in composition, revealing how the search for new expressive possibilities has driven the development of technological tools through experimentation. The appearance of AI marks a fundamental shift: no longer just a tool, AI now poses questions and challenges to the composer. Engaging with AI becomes an exploration of an unknown entity, whose full capabilities are still largely undiscovered. This new interaction leads composers to confront AI not merely as a passive resource but as a participant in the creative process, outlining an ethical path to reclaim technology as a creative tool. In Human Memories reflects this dynamic, demonstrating how AI can serve as both inspiration and a driving force in shaping contemporary music.

---


### 181. [ABF-Bench: A Verifiable Benchmark for Agentic Blockchain Forensics](https://arxiv.org/abs/2610.23656)

**<font color=#1a73e8>作者：</font>** Xiaohang Yu, Hejia Geng, William Knottenbelt  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchain forensics is adversarial and open-ended: money launderers split, swap, and bridge funds, cut their trail at mixers or custodial services, and change tactics from one incident to the next. Investigators must keep adapting their tracing in response. Yet the immutability of public ledgers preserves every recorded movement in public view, making much of the investigation independently verifiable. We introduce ABF-Bench, an interactive benchmark that makes evidence-backed fund tracing a verifiable agent task, in which every claimed movement must cite ledger records the agent retrieved. A case-to-task pipeline builds well-posed tasks across ledgers: conservative rules halt tracing wherever the records leave a continuation unresolved, and each task's reference graph is the answer those rules determine. Built from real laundering activity, the tasks combine multi-hop transfers, DeFi exchanges, cross-chain round trips, custodial and mixer deposits, and address poisoning. We also propose the ABF agent harness, built around a working memory, and evaluate it alongside general-purpose agents and fixed-order tracers. The harness reaches 75% edge recall, against 47% for Codex with the same model and 10% for Claude Code, which loses recall to overconfidence: it cites records it left unretrieved. Compared with fixed-order tracers, the harness acquires evidence faster than the best of them early in the budget and recognizes undisclosed custodial services that they walk past (89% vs. 0%), with 98% fidelity. However, agents tend to stop early and lose recall on larger tasks, which holds their final recall below the best tracer. Beyond exposing these gaps, ABF-Bench opens blockchain forensics to LLM agents as a verifiable domain, where the verdicts that score agents also offer potential training signals.

---


### 182. [An Efficient Approach to Beetle Damage Detection of Banana Using Deep Learning](https://arxiv.org/abs/2610.23661)

**<font color=#1a73e8>作者：</font>** Md. Mehedi Hasan Naeem, Ishtiyak Ahmmad Araf, Md. Arefin Haque Mahir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible surface damage of banana fruits by Basilepta subcostata (the banana fruit scarring beetle) can reduce their market value. Here, manual inspection of Banana fruits is subjective and difficult to scale. This study presents a lightweight framework based on YOLOv8n deep learning model for locating individual bananas and classifying their visible surface condition as healthy or unhealthy. The term beetle damage in the paper title is used operationally for the locally observed scar-like surface condition; the model does not identify a specific beetle species or biological cause. A custom dataset of 2,473 images containing 5,827 annotated banana instances was prepared from local-market imagery in Bangladesh. The reported experiment used an 80/20 protocol with 1,982 training images and 491 test images. A pretrained YOLOv8n model was trained at 640x640 resolution for 50 epochs with a batch size of 4. On the test partition, it achieved 81.36% precision, 74.30% recall, 77.67% F1-score, 87.04% mAP@0.50 and 59.33% mAP@0.50:0.95. A YOLOv8s comparison gave slightly lower F1 and mAP while using a substantially larger checkpoint. The YOLOv8n checkpoint occupied 5.96 MB and required 6.54 ms/image for inference on an NVIDIA Tesla T4. The results support YOLOv8n as a compact baseline for instance-level banana surface inspection within the studied acquisition conditions.

---


### 183. [PCDFusion: Proposal-Context-Detail Bayesian Rendering for Infrared-Visible Image Fusion](https://arxiv.org/abs/2610.23663)

**<font color=#1a73e8>作者：</font>** Rui Liu, Lin Gu, Hesong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared-visible image fusion (IVIF) aims to combine visible and thermal infrared observations for human perception and downstream vision tasks. Visible and thermal infrared observations are physically complementary but unreliable in different ways. Existing deep IVIF methods mainly improve feature interaction and reconstruction, but often lack an explicit local rule for deciding when visible appearance should dominate and when thermal responses should contribute. To address this issue, we reformulate IVIF as local Bayesian posterior rendering, where fusion is controlled by posterior action weights rather than direct modality mixing. In this paper, we propose Proposal-Context-Detail Fusion (PCDFusion), a visible-anchored framework that implements this formulation through three rendering stages. PCDFusion preserves potentially useful thermal responses, updates exposure-degraded visible regions, and renders reliable band-limited infrared structures into the final luminance. Extensive experiments on public IVIF benchmarks show that PCDFusion improves fusion quality, target recovery, and downstream detection and segmentation performance under challenging illumination. The code is available at this https URL.

---


### 184. [TriRouter: Sparse-to-Dense Electrode-Space Routing for Robust EEG Motor Imagery Decoding](https://arxiv.org/abs/2610.23665)

**<font color=#1a73e8>作者：</font>** Ying Zhou, Yaoxin, Mengting Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motor imagery brain-computer interfaces require reliable decoding from multichannel EEG, but practical acquisition often yields sparse or corrupted electrode montages. We propose TriRouter, an electrode-space routing framework with discriminative-preservation, mask-robustness, and latent-compensation paths. A validation-calibrated router uses observable channel availability to allocate path contributions, preserving complete-channel discrimination while increasing representation recovery under severe missingness. In BNCI2014-001, TriRouter outperforms standard public backbones and a dynamic-spatial-filtering corrupted-EEG baseline. It improves accuracy over the strongest corrupted-EEG baseline by 3.68, 4.02, and 6.46 percentage points at nominal 25%, 50%, and 75% missing settings, and remains effective under structured regional missingness and additional low-channel dataset evaluation.

---


### 185. [TUPLE-Bench: Evaluating and Mitigating Privacy-Utility Trade-offs in Typed Decision Models](https://arxiv.org/abs/2610.23668)

**<font color=#1a73e8>作者：</font>** Yiqu Yang, Qiaoyuan Zheng, Yang Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Typed decision models often return more than a selected category. They also expose probabilities for each candidate and, sometimes, a separate confidence score. These fields support downstream decisions but may reveal information beyond a recipient's authorization. We introduce TUPLE-Bench (Typed decision models' Utility and Privacy Leakage Evaluation Benchmark), a benchmark of paired synthetic cases in which recipients may learn a coarse operational category but not its fine-grained cause. Across nine models, instructions to withhold the cause fail to protect it: 91.88%-99.93% of responses reveal the cause through direct selection or residual scores. Even when causes are excluded from the candidate set, full outputs enable 62.85%-75.35% recovery on held-out cases, compared with 51.04%-57.64% using only the selected category (50% chance). Full outputs also reduce mean downstream cost in all 27 model-task comparisons. However, confidence fields increase leakage without consistently reducing cost. We further introduce workflow-constrained privacy quantization (WCPQ), which reduces secret recovery while preserving the behavior and cost of specified downstream workflows. Our findings highlight the need to audit decision interfaces field by field and workflow by workflow.

---


### 186. [Equivalence testing and run-count design for stochastic machine-learning experiments](https://arxiv.org/abs/2610.23700)

**<font color=#1a73e8>作者：</font>** Dmytro Knopov, Nadiya Shvai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Claims that two training methods perform equally well often rest on a non-significant difference between two or three runs per method. We develop a protocol, with its power theory, for certifying practical equivalence in per-run metrics such as the AUROC (area under the receiver operating characteristic curve). It rests on a two-level (seed x item) variance model separating between-run dispersion from item-level noise. Equivalence within a pre-specified margin is tested by two one-sided tests (TOST), equivalently by a confidence interval inside the margin; a two-level bootstrap covers composite statistics. A closed-form formula converts a margin and a target power into runs per method; its shifted-t refinement is calibrated against the realised two-level process. Simulations on a 270-cell grid and under non-Gaussian seed laws confirm the formula within its design-relevant range, from five runs per method. For four published runs of a joint energy-based model, the failure to certify equivalence was largely decided by design: with the variance calibrated to those runs, two per method certify with probability near three per cent, whereas certifying 0.01 AUROC at 80 per cent power needs twelve even under exact equality. A second case study on a thousand-seed CIFAR-10 zoo and the MultiBERTs checks the formula against real seed laws (within 0.05 in that range) and resolves comparisons that two or three runs leave undecided. In a two-stage design (pilot, then formula), our experiments suggest that an upper confidence bound on the pilot variance substantially reduces the undersizing seen with its point estimate.

---


### 187. [Blitz: Accelerating the Diffusion Modules of AlphaFold3 and Boltz-2](https://arxiv.org/abs/2610.23703)

**<font color=#1a73e8>作者：</font>** Vinay Saji Mathew, Soundar Kumara, Gretta Kellogg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-based protein structure prediction models produce all-atom structures in about 200 denoising steps, and that cost has driven a number of few-step samplers. We present Blitz, a few-step distillation framework that uses a geometric noise schedule to distribute steps more evenly across noise scales, then learns those updates through multistep consistency training. Physical steering and target-free candidate selection help reduce the remaining geometric defects at inference. We apply Blitz to AlphaFold 3 and Boltz-2, reducing denoising from 200 steps to eight. Because published few-step results use different benchmarks and scoring procedures, we compare both distilled models with their teachers and other few-step methods under a common evaluation protocol covering structural accuracy, interface quality, ligand placement, and stereochemical validity. Blitz retains teacher-level structural accuracy, with AF3-Blitz outperforming all evaluated few-step baselines and exceeding its teacher on several accuracy metrics.

---


### 188. ["To Boldly Go Where No One Has Gone Before" What Has AI Let Developers Unlock?](https://arxiv.org/abs/2610.23708)

**<font color=#1a73e8>作者：</font>** Rudrajit Choudhuri, Jenna L. Butler, Christian Bird 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Measuring AI by how much faster developers work is like judging electricity by how much faster it spun a steam-era factory. A fuller measure asks what new work becomes possible. We surveyed 331 software developers at Microsoft about what AI lets them do that they could not do before and analyzed their answers using reflexive thematic analysis with a human-in-the-loop, multi-model AI council. Developers described doing familiar work faster (Faster, 45%), undertaking work previously beyond their reach (Further, 36.9%), and taking on new kinds of work centered on building for and directing AI agents (Afresh, 12.4%). Across these accounts, learning and scaffolding ran in both directions: developers learned new skills with AI while externalizing their tacit knowledge as the context and standards that guide AI's work. Drawing on Vygotsky's zone of proximal development, we frame developers and AI as joint learners whose zones meet at the skill-judgment nexus: AI can supply skill faster than it can reliably judge its own work, and developers must continuously bridge that gap. Whether they do sets them on one of two paths. On one, developers' judgment grows alongside AI's skill, and they codify what they learn so the loop keeps turning. On the other, they become hollow orchestrators, approving work they can no longer judge and losing the identity and meaning they once drew from it. Based on our findings, we offer a two-way scaffolding playbook to help developers, teams, and tool builders take the first path.

---


### 189. [Neural Expansion: A Unified Mechanism for How Deep Neural Networks Generalize](https://arxiv.org/abs/2610.23716)

**<font color=#1a73e8>作者：</font>** Chashi Mahiul Islam, Samuel Jacob Chacko, Mao Nishino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks demonstrate remarkable generalization despite being highly over-parameterized, challenging traditional statistical learning theories. While several theoretical paradigms such as margin-based bounds, PAC-Bayesian analyses, and neural tangent kernels provide global explanations, they often lack mechanistic insight into how generalization emerges from training dynamics. We introduce Neural Expansion, a unified geometric framework that characterizes generalization through the expansion of directionally-selective ray coverage in the input space. Using Generalization Intervals (GIs), we quantify direction-specific regions around training samples where the model's predictions remain stable. Our extensive empirical studies across diverse architectures and datasets reveal that training leads to progressive expansion of ray coverage, particularly along directions with low Jacobian singular values. This mechanism helps explain a large fraction of correctly classified test inputs, adversarial examples, and even mislabeled or out-of-distribution samples through the geometry of ray coverage rather than instance-level memorization. By connecting input-space curvature to predictive behavior, our framework provides a mechanistic foundation that complements existing global theories of deep learning.

---


### 190. [Escaping Parameter Space: Tight Generalization Bounds via Representation Quality](https://arxiv.org/abs/2610.23729)

**<font color=#1a73e8>作者：</font>** Niclas Göring, Shuofeng Zhang, Branton DeMoss 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We derive a tight generalization bound for deterministic neural We derive a tight generalization bound for deterministic neural networks based on their last hidden layer representations. By evaluating representation quality with a parameter-free $k$-nearest-neighbor ($k$-NN) classifier, our certificate avoids traditional parameter-space complexity measures, KL divergences to a posterior, weight norms, and compression. The bound is tight: trained from scratch, it reaches an 8.0 percentage point gap to test error on CIFAR-10 (ResNet-18) and yields the first non-vacuous certificates we are aware of on CIFAR-100; with frozen DINOv2 representations, it certifies at 1.4\% on CIFAR-10 and 23.1\% on 1,000-class ImageNet. It decomposes additively into three empirical, independently measurable quantities: local class geometry ($k$-NN decoder error), decoder-network agreement, and training stability. This allows the bound to act as a diagnostic tool: we demonstrate that actively destroying local class geometry eliminates generalization while leaving dataset memorization intact, identifying class geometry as a causally relevant mechanism for generalization. Finally, we show that learned representations are significantly less sensitive to weight noise than linear readouts, suggesting why parameter-space certificates often struggle to remain tight.

---


### 191. [Synthetic Image Oversampling for Rare-Class Representation Learning in Deep Facial Phenotyping](https://arxiv.org/abs/2610.23730)

**<font color=#1a73e8>作者：</font>** Miles Liao, Zhanliang Wang, Hongzhuo Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent deep facial phenotyping methods can support the recognition of genetic syndromes, but patient images are often scarce and unevenly distributed across disorders. Synthetic facial images offer a way to supplement the training data without collecting additional patient photographs. Their usefulness, however, depends on whether they improve recognition of real patients: generated images may introduce artifacts or repeat features already represented in the training set. It is therefore necessary to examine both how much synthetic augmentation to use and which disorders benefit. We investigate disease-specific synthetic oversampling using images from the Phenotypic Disease Image Database to augment a subset of the GestaltMatcher Database. We compare increasing augmentation levels in an image-based model, GestaltMatcher-Arc, and a multimodal model, GestaltMML, while keeping the real training and patient-disjoint evaluation partitions fixed. Repeated training runs assess overall and disease-specific accuracy, and an exploratory embedding analysis examines changes in class compactness and separation. Augmentation improves mean recognition accuracy in both training setups, although gains remain modest in GestaltMatcher-Arc and continue across the tested levels in GestaltMML. These aggregate improvements are accompanied by uneven disease-level responses, including reduced accuracy for some disorders. In the embedding analysis, disorders with fewer real training images tend to gain more class separation, but geometric changes do not consistently track classification performance. Together, the findings support synthetic oversampling for limited-data facial phenotyping and emphasize the need to assess its amount and benefit for individual disorders within each training setup.

---


### 192. [ESC: Escaping 2D Diffusion Ambiguity with Geometric Constraints for Consistent Novel View Synthesis](https://arxiv.org/abs/2610.23732)

**<font color=#1a73e8>作者：</font>** Ge Ya Luo, Daniel Severo, Brian Karrer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating 3D-consistent novel views from 2D diffusion models remains a fundamental challenge in computer vision. In this work, we introduce a framework that enhances geometric alignment for monocular view synthesis under drastic camera changes by jointly generating a target view and its corresponding depth map. By conditioning the diffusion pipeline on the single source image, source depth, and target camera rays, our approach forces the model to inherently reason in 3D space even under extreme viewpoint shifts. To guarantee spatial fidelity, we propose a novel per-pixel depth consistency constraint, which verifies and enforces 3D consistency across generated views. Our framework establishes a robust pipeline for geometrically consistent view synthesis, yielding superior visual accuracy and spatial alignment compared to current state-of-the-art methods. With this work, we pave the road towards robust 3D world models capable of understanding complex environments from a single view image.

---


### 193. [Material and Defocus Cues for Occluded Object Localization in Single Hyperspectral Images: An Exploratory Study](https://arxiv.org/abs/2610.23733)

**<font color=#1a73e8>作者：</font>** Ali Zia, Jun Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Partial occlusion makes object detection difficult when visible regions have weak texture or similar appearance. Hyperspectral imaging provides material-dependent spectra and wavelength-dependent optical blur, which offer complementary evidence for separating objects. We investigate a pipeline that combines nonnegative-matrix-factorization-based material grouping, divergence-based optical cues, and graph Laplacian propagation. The propagated scores support region extraction and bounding-box localization without requiring a separate depth sensor at inference. A collection of 30 indoor and six outdoor hyperspectral scenes acquired using two camera systems provides qualitative examples spanning different materials, depth arrangements, and partial occlusions. The examples illustrate how material information can support separation when optical cues are weak, and how optical cues can distinguish some surfaces with similar material properties. Objects sharing both material and depth remain challenging. This exploratory study establishes the sensing rationale and mathematical formulation, while identifying the quantitative evaluation and implementation details needed to assess detection performance systematically.

---


### 194. [LagNet: Lag-Structured Operators for Long-Term Time Series Forecasting](https://arxiv.org/abs/2610.23735)

**<font color=#1a73e8>作者：</font>** Zhenan Yu, Guangxin Jiang, Jiuyun Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term time series forecasting maps a finite history window to an extended future horizon. Many existing models focus primarily on the design of input representations and model structures, while paying less attention to the structural form of the history-to-future forecasting operator itself. We examine this operator directly and find that, across model families, sensitivity matrices exhibit recurring diagonal patterns whose diagonals correspond to relative temporal lags. Motivated by this observation, we develop a framework for direct multi-step forecasting based on lag-structured temporal operators. Its basic building block, LagLayer, constructs a Toeplitz matrix by tying history-to-future connections with the same relative lag and incorporates horizon-wise and history-wise scaling coefficients to relax exact sharing. This design enables LagLayer to serve as an effective replacement for temporal linear layers in existing forecasting models. Stacking LagLayer modules with activations and multiple feature maps yields LagNet. Experiments on long-term time series forecasting benchmarks show that our method is competitive with strong baselines, while sensitivity matrix diagnostics and limited-data experiments demonstrate that LagLayer provides an effective and sample-efficient alternative to a linear layer.

---


### 195. [Beyond Multi-Stage Pipelines: A Label-Correlation Ensemble for Multi-Label Retinal Fundus Disease Classification](https://arxiv.org/abs/2610.23747)

**<font color=#1a73e8>作者：</font>** Md Asif Uddin, Jannatul Ferdous, Asif Islam 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retinal fundus images frequently carry more than one disease, and public fundus datasets are heterogeneous and severely long-tailed. Clinical triage suggests a staged design, in which a screening gate, a disease-group router and group-specific classifiers operate in sequence, but it is unclear whether this hierarchy earns its complexity. We present a controlled comparison of three architectures on a unified 39-target label space built from RFMiD 1.0, RFMiD 2.0 and ODIR-5K (12,652 images): (i) a three-stage gated cascade of eight models, (ii) a flat model with 39 independent sigmoid outputs, and (iii) a label-correlation model that replaces the flat linear head with 39 learned label queries and a two-layer transformer decoder. All three share one Swin-V2-B backbone, one preprocessing pipeline and one training protocol, so differences are attributable to the architecture. Staging offers no consistent advantage: tracing every missed disease instance to the stage that lost it shows that the two coarse gates discard 34.2% of true instances while the fine-grained classifiers lose only 6.7%, and the gates' hard zeros depress the cascade's macro-AUC to 0.747. Label-correlation modeling gives the largest single gain, raising the detection rate from 0.621 to 0.682 (0.689 with test-time augmentation). Blending the flat and label-correlation models under four-view test-time augmentation is the best configuration on six of eight metrics (exact match 0.694, micro-F1 0.678, macro-F1 0.456, macro-AUC 0.972). On definition-matched class subsets it matches or exceeds four recent studies on macro- and micro-F1, most clearly on low-support pathologies. We also show that ensembling a gated cascade with continuous-output models is harmful, and that per-source negative sampling is needed to remove a dataset shortcut that otherwise yields a spurious AUC of 1.000.

---


### 196. [A Paired RGB-Sonar Dataset for Fish Monitoring with Consumer Sonar](https://arxiv.org/abs/2610.23759)

**<font color=#1a73e8>作者：</font>** Mourad Derbedrosian, Michael Hobley, Pietro Perona  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Imaging sonar enables underwater observation in conditions where optical imaging is ineffective due to darkness and turbid water. However, imaging-sonar systems previously used for ecological monitoring have typically been expensive, limiting their accessibility. Consumer forward-looking sonar has the potential to make fish monitoring more accessible, but its noisy imagery makes annotation and the development of automated methods challenging. We introduce the Huntington and Caltech Koi RGB and Sonar dataset (HaCKRS), which pairs Garmin LiveScope imaging-sonar recordings with top-down RGB video of koi carp. The dataset contains more than 105,000 temporally matched frame pairs, spanning approximately 3.3 hours of recordings across four range and orientation configurations. We provide frame-wise metadata, sonar geometry and coordinate information, synchronization data for all four configurations, and planar registration for the three horizontal configurations. The release focuses on paired observations and calibration rather than task-specific fish annotations. We intend HaCKRS to support annotation and the development of fish detection, tracking, and counting methods, and investigations into the potential of consumer sonar for ecological monitoring.

---


### 197. [Universal Semantic Enhancement for Weakly Supervised Anomaly Detection](https://arxiv.org/abs/2610.23765)

**<font color=#1a73e8>作者：</font>** Siyu Zhou, Yuqin Xie, Hao Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weakly supervised anomaly detection on tabular data is an essential task in many label-scarce applications, since tabular data is widely encountered and it is commonly observed in practice that only a limited number of labeled anomalies are available alongside abundant unlabeled samples. Most existing methods try to learn features that capture the inherent distribution patterns in the target domain. However, such features often struggle to provide a complete description of possible abnormal characteristics and are highly susceptible to overfitting the extremely scarce labels. To address this challenge, we propose a weakly supervised anomaly detection method based on universal semantic enhancement for tabular data, which fuses the universal knowledge from a pre-trained tabular foundation model with the domain-specific knowledge learned on the target dataset. The two types of knowledge are naturally complementary: universal semantics describe the common patterns of tabular data across domains, while the domain-specific features capture the inherent distributions of normal and anomalous behaviors in the target dataset. A prototype-conditioned modulation mechanism is then designed to effectively integrate the two types of features, allowing them to reinforce each other for improved anomaly detection. Extensive experiments on public datasets show that the proposed method outperforms competitive methods when only eight labeled anomalies are available in the training procedure.

---


### 198. [Logic-Guided Graph Denoising Diffusion Models](https://arxiv.org/abs/2610.23766)

**<font color=#1a73e8>作者：</font>** Samuel Cognolato, Luciano Serafini, Alessandro Sperduti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph diffusion models are competitive approaches for generating complex graph-structured data. However, when such distributions have strict structural constraints, diffusion models may fail to capture them exactly, resulting in the generation of invalid graphs. In this paper, we propose a method for grounding graph diffusion models in domain-specific knowledge via First Order Logic (FOL), leveraging its expressive and interpretable formalism to impose structural constraints on the generative process. We incorporate domain knowledge using classifier guidance, a technique that conditions the diffusion model's distribution on external variables to exert control over the sampled data. During the generative process, classifier guidance steers the denoising trajectory to optimize an objective function, which we define as a fuzzy and differentiable relaxation of the logical rules. Our methodology requires only the specification of constraints in FOL, whose satisfaction is encouraged at inference time to guide a pre-trained generative model. We evaluate our approach by comparing the unconditional generation of knowledge graphs with our logic-guided framework, which incorporates domain ontologies as structural constraints during inference. This approach significantly increases the proportion of generated graphs that satisfy the ontological constraints.

---


### 199. [Video Diffusion Avatars: Taming Video Diffusion Models into Controllable 3D Avatars](https://arxiv.org/abs/2610.23772)

**<font color=#1a73e8>作者：</font>** Simon Giebenhain, Tobias Kirschstein, Liam Schoneveld 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models (VDMs) trained on internet-scale data encode a rich prior on appearance, motion, and physics that is difficult to replicate with explicit 3D rendering and costly 3D data capture. We introduce Video Diffusion Avatars (VDAs), a method that creates photo-realistic, multi-view consistent avatars from a single image by fine-tuning a VDM for precise control over camera viewpoint, facial expression, and upper-body pose. Departing from 3D morphable models (3DMMs), VDAs use a learned expression space that lifts the expressiveness ceiling of 3DMMs, e.g., for the tongue and mouth interior. However, learned expression codes exhibit heavy viewpoint bias, as our DISTRACT benchmark reveals. We show that this bias can be removed through disentanglement, enabling their use as driving signals for multi-view consistent avatars. Camera and upper-body pose are controlled jointly via proxy-mesh renderings, giving independent control over expression, pose, and viewpoint. A camera-triplet training strategy makes the approach efficient: our models train for 34 hours on a single A100 using only public multi-view data. VDAs outperform state-of-the-art single-image 3D avatars on novel-view reenactment, reducing face LPIPS by 29% and improving perceptual quality (JOD) by 66% on BecomingLit. A static 3DGS reconstruction probe further confirms that our generations are the most multi-view consistent. Built on a video prior, VDAs produce effects beyond the reach of explicit renderers, including physically plausible hair dynamics, shadows, reflections, and refractions.

---


### 200. [The Collection of a Real-World, Large-Scale Dataset for Automated Skill Evaluation in Central Line Dressing Change](https://arxiv.org/abs/2610.23789)

**<font color=#1a73e8>作者：</font>** Ummey Tanin, Shannan K. Hamlin, Hsin-Mei Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Central line-associated bloodstream infections (CLABSIs) remain a major source of preventable morbidity and mortality in healthcare settings. Proper execution of the central line dressing change (CLDC) procedure is essential for infection prevention, yet current approaches to competency assessment rely primarily on manual ob- servation by clinical educators, making evaluation time-intensive, difficult to scale, and limited in consistency and granularity. These challenges highlight the need for AI-assisted skill evaluation methods that can support more objective, reproducible, and scalable assessment of clinical performance. However, progress in this area has been constrained by the lack of broad-scale, clinically grounded datasets for developing and evaluating such methods. In this work, we present the collection process of a large-scale video dataset for CLDC skill evaluation, comprising 365 recordings of registered nurses collected during the 2026 annual competency exam at Houston Methodist Hospital. Each video is paired with subtask-level temporal annotations and clinical performance assessments spanning 17 subtasks of the procedure. We describe the data collection and curation pipeline, including pilot testing of record- ing configurations, annotation protocol design, and post-collection processing. We further establish the feasibility of video-based skill assessment through benchmark experiments with spatiotemporal deep learning models. This dataset provides a foundation for future research on automated clinical skill assessment, feedback generation, and AI-assisted training in nursing education.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-213](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

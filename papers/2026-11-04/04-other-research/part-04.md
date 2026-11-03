# 📦 其他研究 | 2026年11月04日

> 本类共 **633** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

---

### 151. [The Tangled Web They Weave: Exploring Neural Representations with Directed Simplicial Complexes](https://arxiv.org/abs/2611.00786)

**<font color=#1a73e8>作者：</font>** Michael Bleher  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how artificial neural networks (ANNs) represent and combine features internally is a central challenge in mechanistic interpretability. Existing neural circuit-discovery methods represent neuron interactions as pairwise edges in a graph. But distributed neural representations consist of large groups of neurons that are inherently linked by higher-order causal dependencies: suppressing a subgroup of neurons in concert may shift the activation of other neurons in the feature representation. We propose a method to construct filtered directed simplicial complexes (DSCs) that give a topological representation of such dependencies, built from the activation profiles of an ANN on a given set of inputs. Our approach treats ANNs as structural causal models and uses counterfactual ablations to test for causal links between groups of internal neurons within specific input contexts. As a proof of concept, we apply the approach to a pair of small multilayer perceptron (MLP) architectures in a synthetic two-dimensional quadrant classification task. In these examples, DSCs recover the designed feature pathways and coordinated class transitions, and the complexes of trained networks are higher-dimensional than those of their handcrafted references. As validation, we compare our method with graph-based circuit-discovery baselines and find that their 1-skeletons agree within the relations that a weight graph can represent. These results support DSCs as context-dependent descriptions of multi-neuron computation and may thus provide a novel, orthogonal framework to study the phenomenon of distributed feature representations and polysemanticity.

---


### 152. [Tight Stochastic Sequential Covers for General VC Classes with Unknown i.i.d. Features](https://arxiv.org/abs/2611.00788)

**<font color=#1a73e8>作者：</font>** Changlong Wu, Wojciech Szpankowski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study hybrid online learning with stochastic features and adversarial labels when the feature distribution is unknown. Prior work gave stochastic sequential covers of log-size $O(d\log^2 T)$ for a general VC class and logarithmic bounds only under stronger star-type structure. We show that finite VC dimension alone is enough: every binary class of VC dimension $d$ admits a distribution-blind exact cover with log-size $O(d\log T+\log(1/\delta))$, matching the worst-case $\Omega(d\log(T/d))$ dependence on the horizon. The key ingredient is a new local cube weight that counts Boolean subcubes incident to each realizable trace. Unlike the equal splits used in earlier constructions, we split mass unevenly according to these cube weights; a coordinate-deletion inequality shows that VC dimension controls the total cost of these splits. This yields, to our knowledge, the first tight $O((d+1)\log T)$ expected worst-case log-loss regret for general VC partitions with unknown i.i.d. features, and an exact polynomial-time implementation for planar affine halfspaces. We also show that the binary phenomenon does not extend from VC dimension to pseudo-dimension: a fixed pseudo-dimension-one sigmoid class requires $\Omega(\log^2 T)$ bits for uniform sequential approximation at accuracy $1/T$.

---


### 153. [Crop Mapping Evaluation under Sampling Bias](https://arxiv.org/abs/2611.00794)

**<font color=#1a73e8>作者：</font>** Akram Zaytar, Kemunto Ochwang'i, Caleb Robinson 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Government agencies use crop maps to estimate production, monitor food security, and set agricultural policy. These crop maps are usually validated against field labels, but these labels are rarely a random sample of the area the map covers. Field teams tend to label parcels near roads and skip ones that are small or hard to reach, so performance measured on held-out labels mainly describes the places they visited. We call the difference between this reported performance and performance over the whole mapped region the deployment performance gap. To estimate performance over the whole region, we use a weighted form of prediction-powered inference (PPI). The classifier's predictions on unlabeled points across the region give a first estimate, and its errors on the labeled points correct that estimate, with more weight on labels from under-sampled conditions. We test this in five European regions where crop registers label every declared parcel, so the true performance is known. Simulating six documented collection practices there produces gaps of up to 0.20 macro-F1. On the collection rule that creates the largest gap in each region, 5 km block cross-validation still overestimates macro-F1 by as much as 0.18, while PPI with weights estimated from satellite embeddings reduces the largest error across regions to 0.07. Importance-weighted cross-validation with the same weights does almost as well, so most of the improvement comes from the weights themselves. We also apply the method to three Kenyan datasets that have no region-wide reference labels. For a roadside dataset collected with helmet-mounted cameras, the estimated macro-F1 falls from 0.93 under random cross-validation to 0.61, although the correction relies on a small number of heavily weighted labels. Our code is available at this https URL.

---


### 154. [BridgeDock: Taming Generative Co-Folding Prior for Molecular Docking with Diffusion Bridge](https://arxiv.org/abs/2611.00795)

**<font color=#1a73e8>作者：</font>** Shikun Feng, Zipeng Yang, Qiuyi Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Molecular docking aims to predict the three-dimensional structure of a protein-ligand complex; in the conventional structure-based setting, it is conditioned on an input protein structure and ligand, often starting from an apo receptor in flexible docking or a holo receptor in rigid docking. Recent co-folding models exemplified by AlphaFold 3 achieve strong accuracy in protein-ligand complex prediction, but they typically generate complexes from sequence-derived inputs and therefore do not directly use apo structures as structural priors in docking, leading to a larger conformational search space and weaker robustness in difficult or few-step settings. We present BridgeDock, a framework that adapts pretrained co-folding backbones to flexible docking by modeling the apo-to-holo transition as a diffusion bridge, allowing generation from the initial protein-ligand state rather than from Gaussian noise. To make this bridge formulation compatible with pretrained denoisers, we introduce an alignment mechanism that maps bridge states to the original denoising schedule of the pretrained model. Experiments on standard flexible docking benchmarks show that BridgeDock consistently outperforms strong co-folding baselines. Moreover, BridgeDock is computationally efficient at inference time and remains effective even with very few denoising steps.

---


### 155. [Private Uniform Language Generation](https://arxiv.org/abs/2611.00797)

**<font color=#1a73e8>作者：</font>** Di Wang, Peng Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study uniform language generation under approximate differential privacy. Given a uniformly bounded number of distinct examples from an unknown target language, a generator must produce infinitely many new examples from that language with probability one while protecting the privacy of its input. We introduce a new combinatorial dimension termed the nested branching dimension and prove that a language class is privately uniformly generatable if and only if both its closure dimension and nested branching dimension are finite. Previous work characterizes non-private uniform generation by the finiteness of the closure dimension alone. Our results therefore identify an additional combinatorial obstruction imposed by privacy.

---


### 156. [A Discrete-Time Variational Objective for Degenerate Diffusion and Equivalence to Flow Matching](https://arxiv.org/abs/2611.00800)

**<font color=#1a73e8>作者：</font>** Rares Dolga, Harshad Dahake, David Barber  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion models and more recently Flow models have widespread application. In this work we consider degenerate Diffusion models in which the per-step generator is deterministic. We construct a modified variational framework and show a formal equivalence between Flow models and Degenerate Diffusion models. For our discrete-time variational objective we show that the optimal degenerate generator recovers the data distribution in the limit of an infinite number of generator steps. Our work therefore provides a unified perspective, showing that discrete-time implementations of flow matching and the discrete-time Degenerate Diffusion model can be considered within the same simple variational framework, removing the need for the continuous-time machinery normally used to justify flow matching models.

---


### 157. [Training-free Conditional Object Composition for Multi-object Image Generation with Diffusion Models](https://arxiv.org/abs/2611.00804)

**<font color=#1a73e8>作者：</font>** Hsuan-Fu Wang, Hsuan-Tien Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object image generation in text-to-image diffusion models remains challenging, as existing approaches struggle to reliably generate all objects specified in a prompt. Compositional approaches that generate objects independently often fail to capture the interactions among them, whereas joint generation methods tend to suffer from inter-object interference. In this work, we propose a training-free framework, termed conditional object composition, that relaxes joint generation methods by taking one step back toward compositional approaches. Our framework decomposes the generation of $N$ objects into two stages: it first generates a subset of $N-1$ objects and then composes the remaining object conditioned on the generated content. To enable effective composition, we adopt an inpainting-based formulation with layout guidance to preserve existing regions and encourage spatially coherent placement. To address the challenge of selecting which objects to generate separately, we introduce an attention-based scoring mechanism based on cross-attention maps and further explore the use of off-the-shelf object detectors. We evaluate our method on multi-object image generation using the widely adopted MS COCO dataset. Experimental results show that our approach achieves competitive or improved performance compared to existing methods, particularly as the number of objects increases. Further studies highlight the importance of the proposed design choices. The source code is available at this https URL

---


### 158. [Streaming Virtual Metrology via Lightweight Adaptation under Temporal Distribution Shifts](https://arxiv.org/abs/2611.00806)

**<font color=#1a73e8>作者：</font>** Doyun Choi, Cheonwoo Lee, Younghyun Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Virtual metrology (VM) aims to estimate costly or delayed metrology variables from heterogeneous sensor signals and in-line measurements, and it acts as a critical component of semiconductor manufacturing. While recent data-driven models have improved VM accuracy, most are trained in batch settings and assume stationary data distributions. In practice, however, production environments evolve continuously due to equipment degradation, process adjustments, and maintenance events, making conventional batch-trained VM models difficult to maintain under temporal distribution shifts. In this work, we propose GRAPE (Global Regression with Adaptive Prediction Enhancement), a practical online learning framework for VM in evolving wafer-processing environments. GRAPE integrates a stable global predictor based on interpretable representations with two lightweight streaming adapters that correct feature-level and environment-level shifts through online updates. Experiments on two real-world semiconductor manufacturing datasets, including chronologically held-out blind-test streams, show that GRAPE improves robustness and generalization under real temporal drift compared with both conventional batch-learning methods and existing online learning baselines.

---


### 159. [UniCaMo: Unified Camera and Motion Control for Video Diffusion Models](https://arxiv.org/abs/2611.00810)

**<font color=#1a73e8>作者：</font>** Long Vu, Tan Ngo, Animesh Karnewar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present \textbf{UniCaMo}, an unified framework for joint control of camera and object motion in image-and-text-to-video diffusion models. Given a reference image, text prompt, sparse 3D object trajectories, and a 3D camera trajectory, UniCaMo constructs motion-consistent input noise that directly encodes the desired motion. Our 3D-grounded noise construction combines reference-derived noise propagation with a spherical Gaussian noise representation for newly revealed regions, providing a simple and effective motion prior without requiring reconstruction of unseen scene geometry. UniCaMo requires no architectural modifications or dedicated control modules and can be adapted using lightweight LoRA fine-tuning with low training data volume. Experiments on standard controllable video generation benchmarks demonstrate state-of-the-art motion controllability and high visual quality with minimal inference overhead.

---


### 160. [ODC: Orthogonal Drift Correction for Improved Text-to-Image Semantic Alignment at Inference](https://arxiv.org/abs/2611.00819)

**<font color=#1a73e8>作者：</font>** Kasra Kamali, Basim Azam, Tuan Duong Trinh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image models have achieved remarkable success in generating high-quality images from textual descriptions. However, they often struggle with "semantic drift," where the generated output fails to precisely align with complex or nuanced text prompts. While recent approaches have attempted to address semantic errors regarding attribute binding or object presence, there remains a gap for a more holistic method that addresses these issues by directly refining the text embeddings of the initial user prompt. In this work, we introduce Orthogonal Drift Correction (ODC), an inference-time guidance method designed to mitigate semantic drift without requiring model retraining or additional user inputs. ODC guides image generation through a two-stage process. In the first stage, it identifies the semantic drift by evaluating the initially generated image against the user prompt in a shared vision-language embedding space. It then isolates the component of this drift vector that is orthogonal to the prompt's direction and translates it back into text via a vocabulary-based surrogate mechanism. In the second stage, it produces refined text conditioning for a second generation pass by feeding both the initial text embedding and the re-embedded drift representation into an adaptive rank-reduced concept removal module. Our experiments demonstrate that ODC consistently improves prompt-image alignment, increasing CLIP scores by up to 5.4% over the baseline on the COALBench-300 and PartiPrompts benchmarks. Furthermore, on the T2I-CompBench complex subset, ODC improves the average 3-in-1 score by 4.5% over the competing methods. As a plug-and-play module, ODC offers a practical and efficient method for improving the reliability of text-to-image models. Code is available at this https URL.

---


### 161. [Beyond Temporal Overlap: Consumer-Aware Evaluation of Sign-Language Segmentation across Three Corpora](https://arxiv.org/abs/2611.00823)

**<font color=#1a73e8>作者：</font>** Guohou Zhang, Kalin Stefanov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign-language segmentation divides continuous signing into clips. In this study, the downstream consumer is a frozen recognizer that assigns one sign label to each predicted clip. Existing metrics instead compare predicted clips with manually annotated boundaries. They do not directly measure whether a clip preserves the visual evidence needed by the recognizer or whether the segmenter produces too many clips. We therefore ask whether overlap metrics and this consumer prefer the same segmenter. We evaluate 27 outputs from three segmentation architectures, three random seeds, and three corpora. Controlled boundary edits separate the effect of removing sign evidence from that of adding surrounding context. Overlap predicts recognition on average, but it does not always determine model choice. At the same intersection-over-union, different recognizers can prefer the shorter or the longer clip. The real outputs reveal two operating regimes. On DGS, overlap, recognition, and sequence error select the same model. On BSL, recognition-based selection recovers and recognizes more reference signs but increases word error rate (WER). Dicta-Sign shows the reverse trade-off: WER selection reduces in-vocabulary WER by 31.17 points but misses more recognizable signs. Segmenters should therefore be evaluated on four axes: temporal agreement, reference recovery, clip recognition, and sequence error, rather than on overlap alone.

---


### 162. [Intent-Bound Authorization for Cryptocurrency Withdrawals Under Backend Compromise](https://arxiv.org/abs/2611.00839)

**<font color=#1a73e8>作者：</font>** Toqeer Ali Syed, Asadullah Abdullah Khan, Ali Akrama  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Binance's preliminary account of its October 2026 attack raises a custody question that key protection alone cannot answer: how can a provider prevent unauthorized withdrawals when an attacker controls a service permitted to request signatures? We propose the Intent-Bound Withdrawal Authorization Protocol (IWAP). Before signing, independent enforcement checks customer intent, exact transaction effects, fresh workload evidence, and a committed single-use spending reservation. Administrative actions use a separate authorization path. We specify the protocol's trust assumptions and give conditional arguments for intent preservation, replay resistance, and a fixed-epoch exposure bound. A Python reference monitor authenticates synthetic records with Ed25519 and serializes reservations with SQLite. It rejects 1,200 negative requests, accepts 3,000 valid synthetic requests, and preserves a 100-unit budget under 64 concurrent attempts in each of 20 trials. When the intent authority is deliberately compromised, malicious requests pass, but the independent budget still limits admitted exposure. The study evaluates a normalized policy model, not Binance's infrastructure or a deployed custody platform. Its contribution is an explicit authorization boundary and reproducible tests of that boundary.

---


### 163. [Running a 20B Video Diffusion Transformer on Consumer Hardware: A Deployment and Measurement Report for MiniMax H3 on Apple Silicon](https://arxiv.org/abs/2611.00843)

**<font color=#1a73e8>作者：</font>** Luke Shi, Steven Shi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We report the end-to-end deployment and measurement of MiniMax H3, a 20.38-billion-parameter video diffusion transformer (DiT) - the count measured from the safetensors headers of the Q8 checkpoint as deployed locally (Section 3.2) - running entirely on consumer Apple Silicon hardware: an Apple Mac mini with M5 Pro chip and 64 GiB of unified memory. Using the official bf16-to-Q8 (8-bit, group size 64) quantization path executed locally on the machine, we produced a working text-to-video pipeline with no cloud dependency. We document the full deployment procedure, including two non-trivial blockers and their fixes, and report measured figures for build time, peak memory, and per-clip render latency across four resolution tiers (Draft 384x640 through Native 768x1344). A 15.08-second 576x1024 clip rendered in 4838.49 seconds with a measured MLX peak of 27.467 GiB. We further operated the system as an unattended production pipeline, completing 17 clips in 26.49 hours with zero render failures. A blind human review of the 17 production clips (generation prompts withheld) averaged 3.12, 3.18, and 2.94 out of 5 for structural integrity, temporal consistency, and visible artifacts. All figures in this report are our own measurements except where explicitly labeled as third-party data. This is a systems/empirical report; we make no claim of model innovation.

---


### 164. [Wave Forcing: Towards Speed-of-Light Streaming Video Generation](https://arxiv.org/abs/2611.00859)

**<font color=#1a73e8>作者：</font>** Yijie Jin, Yuxuan Liu, Jiajun Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time long-video generation requires continuous output with consistent appearance and natural motion. Existing chunk-wise autoregressive methods face challenges in both generation efficiency and long-video quality: serialized denoising and history-cache refresh require two forward passes even with one-step denoising, and longer rollouts can degrade quality and cause camera drift. We propose Wave Forcing (WF), which co-designs generation, training, and execution for continuous video output with multi-step denoising. WF uses chunk-wise causal attention to access earlier, cleaner chunks before their denoising is complete, and distributes staggered denoising and cache-refresh stages across full-model replicas to achieve 1F1C: one output chunk per concurrent forward round after pipeline fill. To adapt the model to this continuous generation process, we develop a three-stage training procedure that successively introduces mixed-noise denoising, motion supervision, and causal adaptation using self-generated history. To execute this process efficiently, Wave Runtime (WaveRT) uses Wave Parallelism (WP) for early K/V delivery and communication-computation overlap, together with optimized kernels and pipelined VAE decoding. Experiments on Wan2.1-T2V-1.3B show that 5-step WF maintains overall quality comparable to Rolling Forcing while achieving higher Dynamic Degree on both short and long videos. Our system efficiency experiments show that 4-step WF achieves 147.6 DiT FPS and 134.8 end-to-end FPS on eight H200 GPUs, yielding 7.07x the single-GPU end-to-end throughput. In DiT-only tests with matched SageAttention+W8A8 backends, denoising steps, and GPU counts, WP delivers up to 2.53x the throughput of the faster of the Ulysses and Ring context-parallel baselines across six model scales (1.3B-14B).

---


### 165. [HamFormer: A Hamiltonian Flow-based SE(3)-Transformer for Conformation Optimization](https://arxiv.org/abs/2611.00875)

**<font color=#1a73e8>作者：</font>** Minjie Cheng, Zhenghao Liu, Yitian Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Transformer architecture plays a central role in modern deep learning, and its SE(3)-equivariant variants have been widely applied to molecular conformation modeling and optimization. Given its importance, many methods attempt to interpret and improve the Transformer through the lens of dynamics. However, they mainly focus on a single attention head rather than the full Transformer architecture and seldom consider SE(3)-equivariance in their proposed models. In this study, we propose an improved SE(3)-Transformer architecture, called HamFormer, which revisits the design of SE(3)-Transformer through the lens of Hamiltonian flow. In particular, we define a parametrized Hamiltonian flow in the phase space of position and velocity, corresponding to optimizing an energy functional that combines an optimal transport-based potential with a damped momentum. The Lie-Trotter splitting framework of the Hamiltonian flow leads to the proposed HamFormer architecture, whose feedforward computation achieves the optimization step of the proposed energy functional. Furthermore, we combine HamFormer with Equivariant Graph Neural Network (EGNN), build a new model for molecular conformation optimization. Extensive experiments on molecular ground-state conformation prediction show that HamFormer provides a strong and physically interpretable surrogate for classic SE(3)-Transformer and generally outperforms state-of-the-art competitors.

---


### 166. [FilmTogether: Cinematic Video Generation from Low-Cost Inputs](https://arxiv.org/abs/2611.00899)

**<font color=#1a73e8>作者：</font>** Shiying Zhang, Xiaobin Hu, Qianchi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of mobile devices has democratized video recording, but a stark aesthetic divide persists between casual, low-cost captures and high-cost cinematic productions. Bridging this gap requires upgrading heterogeneous production elements, such as lighting, specialized costumes, and materials, without altering the core layout, identity, and temporal motion of the original footage. However, this task is heavily bottlenecked by two important challenges: 1) Lacking a high-quality paired training data specifically designed to handle complex low-to-high appearance shifts. 2) Ignoring the capacity of current video editing models to perceive and enhance the multiple low-cost compositions. To address these issues, we present CineCraft-120K, a large-scale dataset of aligned low- and high-cost video pairs annotated with pair-aware editing prompts. CineCraft-120K features a diverse, high-resolution and high-cost Cinematic Crafting bank spanning decades of media production, meticulously taxonomized into 5 broad domains and 23 fine-grained sub-categories. It also provides element-level mapping between low- and high-cost counterparts, offering pair-aware rich textual prompts that precisely detail the required aesthetic transformations while anchoring structural layout. Architecturally, we propose a simple yet effective dual-memory feature adapter, where a text-memory expands semantic capacity for low2high appearance changes, and a hint memory supplies layer-wise visual feature corrections of high-cost element before context injection. Extensive experiments and ablation studies demonstrate the superiority of CineCraft-120K for low-to-high-cost video editing, alongside the effectiveness of our dual-memory adapter.

---


### 167. [Foresight: Learning Twisted SMC for Rare Events from Reversed Relaxations](https://arxiv.org/abs/2611.00903)

**<font color=#1a73e8>作者：</font>** Ziyi Fan, Yuxuan Qiu, Haibo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the probability that a reversible Markov chain started in a set $A$ is in a rare set $B$ after a fixed horizon, a quantity often needed for many start laws, down to single states. Twisted sequential Monte Carlo (SMC) estimates such probabilities without bias, with small variance when its proposal and twist approximate the dynamics conditioned on reaching $B$, but these components are usually learned from forward simulations, which contain almost no successful paths when the event is rare. We introduce Foresight-SMC, which learns both components from the target side: under reversibility, relaxations started in $B$ that return to $A$ are, read backwards, exact samples of the conditioned paths, and their number is governed by the return probability rather than by the rare probability. Extending this reversal to the recorded propose--accept decisions of a Metropolis-adjusted sampler, we fit a controlled Langevin proposal with exact likelihood ratios by maximum likelihood, together with a classifier twist; the resulting estimator is unbiased for any start law. A variance analysis shows that resampling reduces the variance when the importance weights degenerate, as they do over long horizons. On an Allen--Cahn field, the learned proposal alone suffices, and one trained model is more accurate than splitting at equal cost. On alanine tripeptide, resampling with the learned twist is necessary, and Foresight-SMC needs less computation per query than adaptive multilevel splitting on localized start sets.

---


### 168. [Benchmarking Machine-Learning Classifiers for Neoantigen Immunogenicity Prediction and the Limits of SHAP Interpretability](https://arxiv.org/abs/2611.00907)

**<font color=#1a73e8>作者：</font>** Ramon Gonzalez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized cancer vaccines require prioritizing, among hundreds of candidate mutant peptides, the few that will induce a T-cell response. This study asks what general-purpose machine learning achieves on that task, and whether the features such models identify as important can be trusted.
We make three contributions. The first is a benchmark of sixty models: twelve supervised classifier families, each in five configurations, evaluated on the Immunogenic Tumor Specific Neoantigen database (ITSNdb; 199 experimentally validated neoantigens, 129 immunogenic and 70 non-immunogenic). All sixty are compared under one stratified k-fold cross-validation protocol, in which the data used to choose a configuration are never the data used to score it. The second is an interpretability study that combines SHAP with feature ablation. The third is a shuffled-label control that tests whether a SHAP value has been earned.
Two results follow, and both run against current practice. First, the classical linear models lead the ranking. The gradient-boosted ensembles and neural networks that dominate recent work bring no advantage. Second, SHAP can fail on high-cardinality categorical features. Ablation establishes the presenting HLA allele as the dominant input and the source gene as dispensable. SHAP reports the opposite, assigning 68.7% to 81.7% of its total value to the source gene in every model that gives each gene its own weight. Shuffling the gene labels at random among the peptides resolves the contradiction: the meaningless column earns the same SHAP value as the real one. That value measures only that ITSNdb contains 173 genes for 199 peptides. We therefore recommend that SHAP values for high-cardinality categorical annotations in cohorts of this size always be reported against such a shuffled-label control, and we describe one in full.

---


### 169. [ZOPGA-KD: Zeroth Order PGA Guided Data Free Knowledge Distillation](https://arxiv.org/abs/2611.00908)

**<font color=#1a73e8>作者：</font>** Tuhin Subhra Mukherjee, Tiya Rose Pulikunnel, Vaidhav Adit 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) enables the transfer of learned representations from a large teacher network to a small student network. In foundational KD, the student network uses the original training data of the teacher model to accomplish this task. However, due to privacy concerns, the original training data is often not available. To overcome this reliance on original training data, several data-free knowledge distillation methods have been developed. Some of these methods operate in the white-box setting, and a few methods generate synthetic data by training a generator network. White-box methods use the teacher model's parameters to obtain a synthetic dataset. To avoid relying on teacher parameters, some methods use computationally expensive generative approaches to obtain such a dataset. There also exist certain black-box methods that generate the synthetic data without accessing teacher parameters. These methods are also computationally intensive. We propose a data-free knowledge distillation method that utilizes just the teacher's output logits and does not require access to its architecture, parameters, or gradients. We generate synthetic data via Projected Gradient Ascent (PGA) starting from smooth random noise signals. Required gradients are obtained through zeroth-order gradient estimation rather than backpropagating through the teacher's parameters. The student is then trained on these synthetically generated samples. We evaluate the proposed method on several benchmark datasets and show that the distillation performance is comparable with approaches that have access to the teacher model parameters.

---


### 170. [Benchmarking Classical Machine Learning Models for Shading-Fault Detection in Rooftop Photovoltaic Systems Using Real Sensor Data](https://arxiv.org/abs/2611.00917)

**<font color=#1a73e8>作者：</font>** Zablon Ombiro, Bernard Shibwabo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most published comparisons of machine-learning classifiers for photovoltaic (PV) fault detection are validated on simulated faults. We compare seven classical and ensemble-tree classifiers on the Réunion dataset, a 4 kW domestic rooftop plant on which shading faults were physically staged and logged. Readings within a staged episode are near-duplicates, so every train/test split is grouped by episode. A 20,800-row subsample that retains all 17 fault episodes was evaluated with three repeats of five-fold group-aware nested cross-validation, with synthetic minority oversampling (SMOTE) applied inside the training folds. Random Forest and XGBoost gave the highest mean accuracy (0.838 and 0.831) and Matthews correlation coefficient (MCC; 0.526 and 0.522). After Holm correction across the 21 pairwise Wilcoxon tests, only Random Forest's accuracy advantage over k-nearest neighbours and the multi-layer perceptron remained significant. Logistic Regression and the Decision Tree (accuracy 0.820) could be separated neither from the ensembles nor from the weakest models. SMOTE lowered binary MCC for six of the seven classifiers. Errors were concentrated in whole episodes: the Random Forest almost entirely missed four of the 17 fault episodes, including one of two uniform-shading and two of five intermittent-shading episodes. A post-hoc diagnostic shows that the no-fault rows were sampled over a wider range of times of day and output levels than the fault rows. Clock time alone reaches an MCC of 0.44, and PV-side voltage alone 0.72. The reported scores therefore reflect operating-condition differences as well as shading signatures. We release the pipeline and the diagnostics, and identify matched no-fault sampling as the step needed before the classifier ranking can be generalised.

---


### 171. [TreePIN$^{2}$: Tree-Prior Initialized Neural Networks](https://arxiv.org/abs/2611.00919)

**<font color=#1a73e8>作者：</font>** Yanrong Wang, Qiming Sun, Haoyang Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fitted decision trees provide predictive knowledge for neural network initialization. We present Tree-Prior Initialized Neural Networks (TreePIN$^{2}$), a method that translates split rules, decision paths and leaf predictions into initial network weights and biases for classification and regression. Sigmoid units encode split responses, hidden units combine them along decision paths, and leaf predictions initialize the output layer. We calibrate split softness using local training margins, sample support and impurity reduction, relating the initial responses to the data at each node. All weights and biases remain trainable, allowing gradient-based optimization to refine the transferred decisions and their combinations. Across six classification and six regression tasks with twenty paired seeds, TreePIN$^{2}$ improves mean initial and early validation performance over initialization baselines on most tasks. After fifty epochs, it achieves the best or tied-best mean validation performance among the six compared methods on ten tasks. Paired ablations show how split calibration and leaf-informed output initialization contribute to the starting predictor and its subsequent learning.

---


### 172. [What matters in classical machine learning for non-intrusive load monitoring? A factorial benchmark on REFIT with validation on unseen houses](https://arxiv.org/abs/2611.00920)

**<font color=#1a73e8>作者：</font>** Zablon Ombiro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Published classical machine-learning results for appliance ON/OFF classification in nonintrusive load monitoring (NILM) range from F1-type scores of 0.53 to 0.98, and the sources of this spread have not been separated. This study separates them with a factorial benchmark on REFIT: seven models, two feature sets and four class-imbalance strategies for five appliances (270 fitted configurations), each evaluated by pooled nested cross-validation and on houses unseen during training, with robustness checks. An analysis of variance shows that the appliance explains 38% of the variance in F1, the feature set 13% and the model only 8%. Engineered rolling-window features raised the mean F1 score by 52% under both protocols. Other conclusions changed on unseen houses: the support-weighted F1 score of the best pooled configurations fell from 0.548 to 0.447, the differences between the models selected by pooled validation were no longer significant, and the benefit of class weighting over no correction rose from 32% to 69%. In a nested comparison, house-grouped selection on the training houses improved F1 on unseen houses for three of five appliances, by up to 0.110, and was within 0.007 for the other two. These findings held across four house partitions and without the solar-affected houses. A same-protocol convolutional network reached a weighted F1 score of 0.50, about 0.05 above the classical models (0.45) and far below the published deep-learning scores of 0.78 to 0.91, which were obtained under a different protocol. The results support low-cost appliance monitoring in buildings and yield a NILM reporting checklist.

---


### 173. [What Helps Denoising Can Hurt Memory: Rethinking History in Long Video Generation](https://arxiv.org/abs/2611.00937)

**<font color=#1a73e8>作者：</font>** Yubin Jing, Ziyang Zhang, Meng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video generators produce long videos block by block, using historical context to maintain temporal consistency. After denoising, a committing pass encodes each clean block into keys and values (KV) that later blocks read, and the same clean block can be encoded into different KV depending on the history it reads. We therefore study historical context not only as a condition for denoising but also as an input to committing. Older historical context that supports denoising can harm subsequent generation when read during committing. At fixed context size and temporal positions, older historical context lowers mean clip-to-clip Subject Consistency. Across 5 generator configurations supporting longer contexts, consistency rises, plateaus, and then declines as committing context expands. Motivated by these findings, we propose Commit Forcing, a training-free rule that organizes committing into a chain. During committing, each block reads only the preceding block's stored KV, so older historical context reaches new entries only through the chain. We apply this rule to 6 pretrained generators. On 60-second VBench, Commit Forcing improves Quality and Total on all 6 generators, by up to 1.27 Quality points and 1.10 Total points. Long-range consistency gains extend to 240-second videos. In a blinded comparison on 120-second LongLive videos, Commit Forcing achieves win rates of 83.5% for subject and scene consistency and 82.9% for overall preference against the base generator, excluding ties.

---


### 174. [Reformulation and Equivalence of Bock's Algorithm for Exact Dependency Parsing](https://arxiv.org/abs/2611.00939)

**<font color=#1a73e8>作者：</font>** Yuxi Wang, Jungyeul Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bock's algorithm provides a matrix-based alternative to Chu--Liu/Edmonds (CL/E) for exact dependency parsing. We present a reformulation that retains original node and arc identities through component labels, column adjustments, and star-and-bar transfers. In exact arithmetic, we prove operational equivalence to original Bock under matching scan and tie rules, and establish correspondence with corrected Tarjan under a prescribed component schedule. A separate analysis establishes optimal-value equivalence with Dozat-derived CL/E under the stated score and single-root conventions. We integrate reformulated Bock into a biaffine dependency parser and evaluate decoding and structured training on the Penn Treebank and Chinese Treebank. These results establish Bock as an alternative exact oracle for dependency parsing and structured training, while distinguishing equality of optimal values from identity of returned trees and training trajectories.

---


### 175. [MarkovTS: Pretrained State-Transition Representations for Zero-Shot Time Series Generation](https://arxiv.org/abs/2611.00941)

**<font color=#1a73e8>作者：</font>** Yujie Li, Zezhi Shao, Jingbo Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Across heterogeneous real-world domains, time-series generation supports simulation, model development, and data augmentation by generating sequences that preserve target-domain statistics and temporal dependencies when real observations are scarce or costly. However, existing methods predominantly address in-domain generation, limiting their reuse in unseen domains. We study reference-conditioned zero-shot time series generation: target domains are unseen during pretraining, generation uses a single target-domain reference sequence, and no model parameters are updated. MarkovTS characterizes sequence evolution through local morphologies and their ordered transitions at multiple temporal scales. Its pretrained encoder quantizes normalized time-series patches into multiscale morphological states with a state codebook, while a transition codebook encodes contextual transitions between adjacent intervals. These transferable state-transition representations condition a pretrained flow-matching model. At generation, the frozen model combines a reference-derived condition with independent Gaussian noise to produce stochastic samples that retain the reference's temporal organization. Across 12 unseen target datasets, MarkovTS outperforms strong baselines in most distributional comparisons and generates diverse, reference-consistent sequences. As downstream augmentation, its samples yield overall gains across forecasting, classification, and anomaly detection benchmarks and diverse model families. Our code is available at this https URL.

---


### 176. [PSF-Informed Reconstruction: An Enhanced 2D Directional Filtered Backprojection Method for Cone-Beam Rotary Computed Laminography](https://arxiv.org/abs/2611.00953)

**<font color=#1a73e8>作者：</font>** Chengxiang Wang, Wei Yu, Baodong Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cone-beam rotary computed laminography (CL) presents a viable alternative to cone-beam CT for imaging objects with high aspect ratios. Conventional reconstruction techniques, such as CL-FBP and CL-FDK, often yield suboptimal results charac?terized by pronounced superimposition artifacts, reduced contrast,and blurred edges, primarily due to their reliance on 1D row-wise filtering along detector rows. To address these limitations and improve reconstruction quality, we proposed a novel 2D directional filtered backprojection (DFBP) method based on the point spread function (PSF). First, an exact expression for the projection process is derived by establishing the relationship between a reconstructed pixel and its corresponding projection point on the detector. Second, a revised backprojection process incorporating two weighting factors is introduced to counteract the nonlinearity inherent in conventional backprojection, leading to a simplified PSF formulation. Third, to circumvent the computational burden of 3D image space filtering,an approximate method by linearizing the coordinate relationship in Fourier space under some assumptions is developed that transfers the 3D filtering operation to the 2D projection space. This approach facilitates the derivation of a formally simple yet effective 2D direc?tional filter, which integrates a 2D von Hann window and a 2D sinc window. Experimental results demonstrate that the proposed method produces reconstructions with superior contrast, sharper boundaries,and fewer superimposition artifacts compared to CL-FBP and CL?FDK. Moreover, it enables more accurate recovery of internal structures, such as bubble defects and electronic components.

---


### 177. [4K Image Super-Resolution on Mobile NPUs: Mobile AI 2026 Challenge Report](https://arxiv.org/abs/2611.00963)

**<font color=#1a73e8>作者：</font>** Andrey Ignatov, Georgy Perevozchikov, Radu Timofte 等 46 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image super-resolution is widely used on mobile devices for upscaling various types of image data. This creates a need for efficient deep learning-based models that are not only performant but can also be deployed on neural processing units (NPUs) present in the majority of mobile and IoT chipsets. In this Mobile AI challenge, we address this problem and propose the participants to design fast solutions that can upsample images from Full HD to 4K resolution while running on popular mobile NPUs from Qualcomm and MediaTek. For this, the participants were provided with the DIV2K dataset and trained models to do an efficient 3X image upscaling. The competition had two tracks: in the first track, the models had to be fully quantized (INT8), and the runtime of all models was evaluated on the Qualcomm Snapdragon 8 Elite Gen 5 NPU. In the second track, the participants were developing floating-point solutions that were evaluated on the MediaTek Dimensity 9500 NPU. Top solutions proposed in this challenge are able to reconstruct 4K images under 5 milliseconds while reaching a PSNR score of 30 dB. A comprehensive description of the models developed in the challenge is provided in this paper.

---


### 178. [E-UDE: A Scientific Machine Learning Model for Malware Propagation Dynamics](https://arxiv.org/abs/2611.00971)

**<font color=#1a73e8>作者：</font>** Vineet Kumar, Samiran Ghosh, V Anil Kumar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Understanding the malware propagation dynamics over the Internet is crucial for effectively controlling its spread. Existing mechanistic and data-driven models in the context of malware propagation dynamics, have some issues with either interpretability or predictive accuracy. This study presents an Enhanced Universal Differential Equation (E-UDE) framework that explicitly incorporates more detailed key factors that influence malware propagation. Evaluation on real-world malware propagation data shows that the E-UDE achieves the best overall performance, attaining an overall RMSE of 783.70 and MAE of 421.65. Compared with the Classical ODE and the UDE models, the proposed approach reduces RMSE by approximately 66 percent and 39 percent, respectively. Its robustness to predictive capability is further evaluated. In this experiment, the E-UDE achieves a Test RMSE of 634.6, a Test MAE of 419.3, and a Test Correlation of 0.964. The E-UDE maintains relatively stable prediction performance as the noise level increases, showing limited degradation compared with the baseline models. Furthermore, this E-UDE model enables us to perform several scenario analyses under different cybersecurity scenarios, providing a useful framework for better understanding the effective control factors. To study the wide applicability of the E-UDE framework, the model performance is assessed by two different datasets, namely, Code Red dataset and Witty Worm dataset.

---


### 179. [Efficient Image Denoising on Smartphone GPUs: Mobile AI 2026 Challenge Report](https://arxiv.org/abs/2611.00974)

**<font color=#1a73e8>作者：</font>** Andrey Ignatov, Georgy Perevozchikov, Radu Timofte 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image denoising is a fundamental problem in mobile photography. Despite a large number of solutions proposed for this task, the majority of them are trained on synthetically produced noisy images, and are additionally too computationally heavy for processing full-resolution images on mobile devices. This creates a need for efficient deep learning-based models that are not only performant but can also be deployed on constrained mobile hardware. In this Mobile AI challenge, we address this problem and propose the participants to design fast solutions that can denoise Full HD resolution photos while running on popular smartphone GPUs from Qualcomm and Arm. For this, the participants were provided with a large-scale dataset consisting of noisy-clean image pairs captured in the wild. The runtime of all models was evaluated on the Snapdragon 8 Elite Gen 5 and Dimensity 9500 chipsets with the Adreno and Mali GPUs, respectively. Top solutions proposed in this challenge are able to perform high-quality image denoising under 100 milliseconds on both platforms while reaching a PSNR score of over 37 dB. A comprehensive description of the models developed in the challenge is provided in this paper.

---


### 180. [HALO: Hierarchical Evidence Selection and Reinforcement Learning for Allocating Budgeted Label Optimization from Longitudinal Clinical Records](https://arxiv.org/abs/2611.00986)

**<font color=#1a73e8>作者：</font>** Huaiyuan Ying, Feiqing Huang, Ryumei Nakada 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Learning from extensive longitudinal clinical records--spanning repeated encounters, evolving conditions, and heterogeneous documentation--under a finite labeling budget requires solving two coupled problems: deciding what evidence to keep and deciding which patients deserve higher-fidelity labels. Prior work on active learning and multi-fidelity label acquisition mainly addresses the second problem, while treating the evidence presented to the acquisition policy as fixed. We present HALO, a Hierarchical Evidence Selection and Reinforcement Learning pipeline for Allocating Budgeted Label Optimization from Longitudinal Clinical Records. This framework jointly learns what to read and what label source to acquire under budget. HALO first selects informative evidence from longitudinal records and then uses a budget-aware policy to allocate free-, silver-, and gold-fidelity label sources. For frozen policies, our theory characterizes asymmetric acquired-label channels and gives a budget-constrained finite-sample gold-risk bound for a common downstream logistic model. In a heart-failure case study, HALO attained the highest MedAlign acquired-label F1 at six of eight target budgets. A downstream classifier trained on HALO-acquired labels attained the highest external MGB F1 at budgets 15-60 and remained within 0.01 of the best comparator at budgets 75-120.

---


### 181. [ISBC: Interpretable Sparse Binary Coding of Pretrained Text Embeddings](https://arxiv.org/abs/2611.00999)

**<font color=#1a73e8>作者：</font>** Stefano Maria Iacus, Haodong Qi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained text embeddings encode semantic structure in high-dimensional continuous spaces whose coordinates are difficult to interpret. We introduce Interpretable Sparse Binary Coding (ISBC), which learns a small set of binary dimensions from frozen embeddings without taxonomy labels or downstream outcomes. A trainable encoder and affine decoder combine reconstruction with controls on activity, factor utilization, dependence, and activation uncertainty. Individual bits and their conjunctions select overlapping document groups; complete activation profiles provide finer contexts for conditional comparisons. We evaluate these representations across corpora, backbones, and code configurations through reconstruction, geometry, predictive probes, and document inspection. Empirical cases identify both distinctions within existing categories and shared content across their boundaries. In a mixed-domain corpus, the most frequent profiles predominantly identify source collections, while selected within-source comparisons reveal sentiment and migration contrasts. Selected associations persist in additional documents encoded without refitting. In an engagement application, bits alone improve prediction of log-transformed outcomes over a constant reference, while their combinations identify within-event content contrasts associated with engagement. The results support using binary coordinates and their combinations for empirical interpretation, with complete profiles providing a fine, partly initialization-dependent description rather than a unique discrete taxonomy.

---


### 182. [IJev: Order-Invariant Decisions via Iterated Cyclic Reordering](https://arxiv.org/abs/2611.01015)

**<font color=#1a73e8>作者：</font>** Youzhi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> System One decision models answer a choice question in one forward pass, but their answer depends on the order in which options are listed, and their probabilities carry a prior over answer labels. An invariant ordering operator is any fixed function that returns the same ordered option list for every input order of a fixed option set. Starting from any such order and averaging a listwise readout over its K cyclic shifts removes the input order, but the decision still depends on the chosen cyclic class: those $K$ shifts are only one of the (K-1)! classes, and different invariant operators can select different classes. We propose IJev, which repeatedly reorders the options by the cyclic-averaged, label-prior-corrected distribution and runs another cyclic average. Every iterate is exactly input-order-invariant. When the iteration does not converge, we average the round distributions rather than return the last round. On five benchmarks and five models, IJev has flip rate zero in every cell. The default uniform average over T=20 rounds substantially improves calibration over a single cyclic average, and its accuracy is comparable. A descriptive choice of horizon and averaging rule is best or tied-best for accuracy in all 25 settings.

---


### 183. [Robust Pixel-wise Digital Image Correlation under Large Motions and Illumination Variations via a Global-to-Local Hybrid Neural Field](https://arxiv.org/abs/2611.01018)

**<font color=#1a73e8>作者：</font>** Xianglong Guo, Jianyang Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital image correlation (DIC) is a widely used non-contact technique for full-field displacement measurement. Data-driven deep-learning DIC offers rapid inference but may generalize poorly to unseen speckle patterns, deformation modes, noise levels, and illumination conditions. Classical optimization-based DIC and recent image-constrained neural formulations avoid labeled displacement data, yet their convergence and accuracy remain vulnerable to initialization, large rigid-body motion, fine non-uniform deformation, and gray-value disturbances. This paper presents a global-to-local hybrid neural DIC framework for robust pixelwise measurement. Stage 1 estimates a dominant in-plane rigid transformation through coarse rotation search, phase correlation, and masked refinement, providing a reliable initialization under large translation and rotation. Stage 2 represents the residual displacement with a hybrid Kolmogorov-Arnold network (KAN) and multilayer perceptron (MLP), and optimizes it using a valid-overlap, illumination-robust structural loss. The local gray-value model explicitly accommodates multiplicative and additive intensity changes. Simulated and real experiments demonstrate accurate and stable displacement recovery under noise, non-uniform deformation, large rotation, illumination variation, and degraded imaging conditions.

---


### 184. [Hierarchical Asynchronous Federated Learning over Space-Air-Ground Integrated Networks](https://arxiv.org/abs/2611.01025)

**<font color=#1a73e8>作者：</font>** Kai Wang, Chee Wei Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the emerging 6G paradigm where AI services operate over decentralized and resource-constrained edge infrastructure, performance of distributed learning algorithms remains a significant challenge. This paper proposes HAFL, a Low Earth Orbit (LEO) satellite-assisted hierarchical asynchronous Federated Learning (FL) framework, enabling resource-limited terrestrial clients to collaborate via Ground-Satellite Links (GSLs). Within this framework, LEO satellites serve multiple roles: as edge servers aggregating and broadcasting models, as clients accelerating training, and as high-throughput relays managing inter-satellite routing through Inter-Satellite Links (ISLs). Unlike conventional synchronous Jacobian-type updates, HAFL employs asynchronous Gauss-Seidel-type updates to enhance convergence speed. We provide theoretical convergences for convex, strongly convex, and nonconvex objectives, respectively, and formulate optimization problems to jointly determine optimal hyperparameters to minimize global training latency. Evaluations demonstrate that HAFL achieves faster initial convergence and comparable final performance for benchmark DNNs and datasets, offering promising FL systems across remote areas with 6G technologies, but much less global rounds and communication cost.

---


### 185. [Trouble With Time: Compile Timestamps and First-Seen Date Regression in EMBER2024](https://arxiv.org/abs/2611.01031)

**<font color=#1a73e8>作者：</font>** Edward Raff, Aditya Kapoor  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reliable first-seen dates are important for constructing temporal malware evaluation splits, but this information often comes from external services that are not equally accessible to all researchers. We investigate whether machine learning can instead estimate an executable's first-seen date or determine when its PE/COFF compilation timestamp is unreliable. Using EMBER2024, we evaluate feature-based and raw-byte models across classification, regression, ranking, and latent-reliability formulations. Direct first-seen regression produces errors comparable to a substantial portion of the dataset's collection window, and none of the evaluated scores provides a useful chronological ordering of files. Current models therefore cannot replace externally sourced first-seen metadata. In contrast, classifiers can identify timestamps that fall within specified tolerances of first seen and can detect clearly implausible timestamps with high discrimination. We also find substantial timestamp disagreement among both benign and malicious executables, indicating that unreliable timestamps are not exclusively a product of malicious manipulation. These results establish baselines and identify timestamp reliability as a distinct direction for future security-ML research.

---


### 186. [ParaBlock++: Communication-Computation Parallel Blockwise Hierarchical Federated Learning](https://arxiv.org/abs/2611.01040)

**<font color=#1a73e8>作者：</font>** Kai Wang, Chee Wei Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the emerging 6G paradigm, where AI-driven services operate over decentralized and resource-constrained infrastructures, the convergence of distributed learning algorithms remains a significant challenge. This paper introduces $\mathrm{ParaBlock}$++, a low Earth orbit (LEO) satellite-assisted hierarchical federated learning (HFL) framework, enabling resource-limited terrestrial clients to collaboratively engage in federated learning (FL) via ground-satellite links (GSLs) supported by LEO satellite megaconstellations. Within this architecture, LEO satellites serve multiple roles: as edge servers aggregating and broadcasting models, as clients accelerating training, and as high-throughput relays managing inter-satellite routing through inter-satellite links (ISLs). Departing from conventional synchronous Jacobian-type updates, $\mathrm{ParaBlock}$++ employs asynchronous BCD-type updates to enhance convergence speed. We provide theoretical convergence guarantees for convex, strongly convex, and non-convex objectives, and formulate optimization problems to determine optimal cluster resource allocation and model partitioning for minimizing global training latency. Experimental evaluations demonstrate that $\mathrm{ParaBlock}$++ achieves faster initial convergence and comparable final performance for deep neural networks (DNNs) such as ResNet-18, offering promising directions for federated learning across geographically remote areas enabled by 6G technologies, but much less global rounds and communication cost.

---


### 187. [Entropy-Regularized Reinforcement Learning for the Regime-Switching Consumption-Investment Problem](https://arxiv.org/abs/2611.01046)

**<font color=#1a73e8>作者：</font>** Congde Hu, Danping Li, Xun Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper establishes an entropy-regularized reinforcement learning (ERRL) framework for the continuous-time consumption-investment problem under a regime-switching market model with general utility functions. By incorporating randomized exploratory policies and Shannon entropy regularization into the stochastic optimal control formulation, we derive closed-form representations for the optimal exploratory consumption and investment strategies. Specifically, the optimal investment strategy follows a multivariate Gaussian distribution, whereas the optimal consumption strategy takes the form of a Gibbs measure---which specializes to a Gamma distribution under logarithmic utility and a non-standard exponential distribution under power utility. Crucially, our theoretical analysis reveals that the classical deterministic optimal decisions correspond to the mode---rather than the mean---of these exploratory distributions. Furthermore, we establish the convergence of the exploratory value function to its classical unregularized counterpart as the temperature parameter vanishes. For algorithmic design, we develop a continuous-time q-learning framework grounded in a novel continuous-time q-function, prove the policy improvement theorem, and establish martingale characterizations for both on-policy and off-policy learning. We find that parameterizing the actor network based on theoretical distribution families can help accelerate convergence and enhance numerical stability. Furthermore, numerical experiments across regime-switching environments provide empirical support for our theoretical findings, demonstrating stable loss convergence as well as the monotonicity and concavity of the learned value functions.

---


### 188. [Infinite Worlds from One Example: What Local Generators Must Share](https://arxiv.org/abs/2611.01048)

**<font color=#1a73e8>作者：</font>** Amin Najafgholizadeh, Mohsen Afsharchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Seeded noise lets games generate any region of an unbounded world on demand. We ask what such a generator needs when every small window must come from one example, the constraint behind Wave Function Collapse. The difficulty is that local constraints can require agreement over arbitrary distances: in a brick wall, each row keeps its place between the mortar lines. We study local generators, each cell a fixed function of the randomness near it. When the constraints carry a quantity that varies across the example, no generator that applies one rule, ignoring position, to independent randomness at every cell can be both exactly valid and faithful to the example's statistics, however far each cell reads. At radius r, staying faithful forces forbidden windows at a density of at least order 1/r, and a construction attains this order. To vary the quantity between exactly valid worlds, a generator needs randomness shared along its direction. We give a finitely checkable condition under which row types drawn from the seed and the position modulo a fixed period suffice for exact validity without learning. A search over the example's patches certifies these quantities and names the input each needs. Across 52 public examples of Wave Function Collapse and 27 from other implementations, it certifies only examples where a learned generator on independent randomness stays far from valid after repair. Given that input, a neural cellular automaton and a diffusion model become valid on 10 and 8 of the 12 certified examples that receive one, and on none from independent randomness. Valid means at most one forbidden window in a thousand after repair. With octaves of seeded noise elsewhere, the automaton is valid on 45 of the 52 public examples and 21 of the 27 from other implementations, and repair keeps random access.

---


### 189. [Efficient Conformal Calibration for Paired Recommendation Decisions](https://arxiv.org/abs/2611.01053)

**<font color=#1a73e8>作者：</font>** Xinyu Qiao, Yichen Lin, Zhewen Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Risk control can suppress useful changes to a frozen recommendation rule. We study how to recover valid activation from the same observed fractional losses. Two specified internal calibrators can lose efficiency by compressing losses into their sum or clipping auxiliary inverse counts before averaging. We propose Averaged Conformal Risk Calibration, or ACRC, which averages before clipping. A product identity proves expected-risk validity, while pointwise bounds characterize the additional activation. For fixed populations sampled without replacement, we connect activation to signed utility under heterogeneous users and switching constraints. Near the budgets, positive population mean gain and the stated nondegeneracy conditions give positive leading-order utility increments despite sampling dependence. Across six datasets, changing only calibration improves discounted net utility by $0.010226$ over raw and $0.008337$ over RB. A separately frozen Jester confirmation gives $0.011025 \pm 0.001082$ over raw with the rule and filter fixed, using a five-seed approximate 95 percent paired interval. Against information-matched SCoRE selecting risk or reward scores, the mean utility difference is $+0.015934 \pm 0.001440$. These gains use more mean realized risk within the declared budgets. Upstream failures delimit the benefit: efficient calibration releases useful modifications when the proposals themselves have value.

---


### 190. [Appointed-Time Fault-Tolerant Fast Terminal Sliding Control for UAVs with a Tracking Error-Based Disturbance Observer](https://arxiv.org/abs/2611.01061)

**<font color=#1a73e8>作者：</font>** Jinfa Li, Sheng Xu, Yanjie Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper addresses the critical challenge of high-performance fault-tolerant tracking control for quadrotor UAVs under complex conditions including external disturbances, parameter uncertainties, and actuator faults. A synergistic control framework is proposed by decoupling the system into position and attitude loops, each governed by the following three innovations. First, an Appointed-Time Prescribed Performance Function (AT-PPF) is developed to strictly constrain the tracking error within a predefined funnel boundary, ensuring convergence within a fixed time regardless of initial conditions. Second, a Tracking Error-Based Fixed-Time Composite Disturbance Observer (TFxTCDO) is developed to enable fast and accurate estimation of lumped disturbances without requiring full-state information or precise system modeling. This observer directly couples disturbance estimation with the control objective, thereby enhancing robustness and convergence. Third, a Fast Second-Order Terminal Sliding Mode Controller (NFSO-TSMC) is designed to achieve faster convergence and effective chattering mitigation. Simulation results demonstrate that the proposed control strategy significantly outperforms conventional methods in terms of tracking accuracy, fault recovery speed, and robustness against uncertainties.

---


### 191. [Robust Reward Machine Learning and Execution in Noisy Environments](https://arxiv.org/abs/2611.01063)

**<font color=#1a73e8>作者：</font>** Roko Parac, Lorenzo Nodari, Daniel Furelos-Blanco 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background: Reward machines (RMs) represent non-Markovian reward functions as finite-state machines over high-level propositional events. Traditionally, these events are generated by a deterministic labelling function that maps environment states to proposition sets. However, real-world labelling functions are inherently noisy.
Objectives: Design and implement a method that learns RMs in the presence of noisy labelling functions and exploits them for policy learning in both discrete and continuous environments.
Methods: We propose Prob-IRM, a method that learns RMs from noisy proposition histories using inductive logic programming (ILP) and exploits them for policy learning. Noisy proposition histories are represented as training examples for ILP, which learns an RM that maximises coverage of low-uncertainty histories. RM learning is interleaved with policy optimisation. Prob-IRM uses a belief over RM states to determine when to relearn the RM and to provide additional guiding rewards.
Results: Prob-IRM is evaluated on environments with discrete and continuous state spaces under varying levels of labelling noise. Prob-IRM performs comparably to baselines using handcrafted RMs and outperforms approaches that use recurrent neural networks to encode history, despite operating with noisy labels.
Conclusions: Prob-IRM represents a step towards deploying reward machines in noisy, real-world environments.

---


### 192. [Label Smoothing in Disguise? Gated Knowledge Distillation for Low-Resource Bangla Generation](https://arxiv.org/abs/2611.01065)

**<font color=#1a73e8>作者：</font>** Dipto Sumit, Zobeida Zaman Chowdhury, Syeda Fabiayee Jahan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gated knowledge distillation (KD) weights teacher signals per token or example, aiming to trust an imperfect teacher only where it seems reliable. We test two gates: EWAD (entropy-weighted agreement-aware distillation), which gates tokens by teacher confidence, and CHAD (counterfactual harm-aware distillation), which gates examples by gradient alignment with validation data. Across six Bangla-centric tasks, three student models (60M to about 2B parameters), and two teacher families, no gate significantly improves plain KD in 45 comparisons. KD also fails to beat cross-entropy (CE) fine-tuning on gold outputs in 40 single-seed comparisons or three-seed runs on four tasks; CE leads on every summarisation metric. The main benefit of KD is regularisation: over ten fixed epochs, CE students lose 0.030 to 0.044 token-F1 from their early-stopped checkpoint, versus 0.005 to 0.025 for distilled students. Teacher-free label smoothing closes most of this gap. In one comparison, a teacher 0.29 token-F1 worse yields students at most 0.009 worse. Thus, gating may change regularisation strength but has little teacher knowledge to select. Findings are limited to Bangla-centric tasks and small students. We will release code, data splits, predictions, and scores.

---


### 193. [On Sparse Graph Limits for Neural Combinatorial Optimization](https://arxiv.org/abs/2611.01069)

**<font color=#1a73e8>作者：</font>** Thien Le, Melanie Weber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks are often trained on small graphs and deployed on larger ones, raising the question of which graph information must be preserved for combinatorial optimization values to transfer across sizes. We establish size-transfer guarantees for normalized graph optimization values using finite collections of energy features. For affine objectives, including MAX-CUT, coloring defect, and independent-set density, differences in task value are controlled by discrepancies in normalized scalar energy probes on all bounded-degree graphs. For general Lipschitz objectives, such as those with balance penalties, an additional representation error appears; this error vanishes on hyperfinite graph families but can remain bounded away from zero on expanders. Thus, at fixed degree bound, state space, Lipschitz constant, and target accuracy, a finite energy representation independent of graph size suffices universally for affine tasks and asymptotically for general Lipschitz tasks on hyperfinite families. These results yield prediction guarantees under explicit conditions on encoder accuracy, readout stability, and representation coverage, together with statistical generalization bounds. Theoretically, we prove Shapley-Folkman bounds with sharp parameter dependence, including a dimension-free $\ell_2$ regime, and realize the resulting energy features with a fixed-weight message-passing network using random node initialization on bounded-treewidth graphs. Experiments with exact solvers and trained models test the resulting transfer guarantees.

---


### 194. [Synergetic Autonomous Intelligence: Three Axioms for Recursive Semi-Closed Learning](https://arxiv.org/abs/2611.01070)

**<font color=#1a73e8>作者：</font>** Dongxu Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Synergetic Autonomous Intelligence (SAI), a theory and design program for learning systems that form, preserve, revise, and compose relations while continuing to learn. SAI is built on three axioms: consequential distinctions must not become orphaned (U); identity is determined by future-faithful continuation under a declared contract (I); and unresolved defects are repaired by the least lawful local completion at the lowest admitted grade (L). We model a model, agent, tool, team, or environment boundary as a recursive semi-closed system with a Kernel-Ring representation, a Compile-Open-Participate cycle, and a typed residual comparing actual with claimed continuation. Under explicit finite or affine contracts, we establish relative consistency and conditional non-redundancy of U/I/L, characterize a contract-relative semantic quotient, construct an exact joint stochastic refinement, derive a constrained residual contraction, prove finite-horizon continued-service viability, and give an executed-intervention identification result with an observational-confounding boundary. We define GRC-Close as the generative and repair schema for this contract. The framework also gives finite contracts for action-effect-feedback loop re-entry, partial failure, duplicate-effect idempotency, replay, concurrent delivery, causal uncertainty, and threshold-radix state representation. KREIT, the Kernel-Ring Equilibrium Information Theory layer, treats information as a typed, resource-bounded distinction; the control layer authorizes, executes, audits, and updates actions across cloud-edge-end scales. These results establish a common contract-level vocabulary for representation, relation, memory, action, communication, explanation, coordination, and growth, while marking the assumptions and open boundaries required for later generalization.

---


### 195. [Grounding Across Views: Cross-View Referring Reasoning for Visual Grounding](https://arxiv.org/abs/2611.01074)

**<font color=#1a73e8>作者：</font>** Hao Gan, Liuqian Wang, Shuang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view object geo-localization (CVOGL) aims to localize a target in a satellite image from an observation captured under another viewpoint. Existing methods typically specify the query with a click point or bounding box, marking the target region but underusing the semantic attributes and relations conveyed by natural language. Moreover, referring expressions are often viewpoint-dependent, making query-view descriptions difficult to ground directly in the satellite image. In this paper, we formulate cross-view visual grounding (CVVG), extending conventional point- or box-prompted CVOGL to instance grounding jointly guided by a referring expression and a visual exemplar. We present GAV (Grounding Across Views), a view-aware framework for selectively transferring visual and linguistic evidence across views. Its core is view-aware referring reasoning: target-centered descriptions are derived from the marked query image, checked for target-category consistency, and augmented with a direction-free role cue. Exemplar prompting, cross-view alignment, and scene-level discrimination ground this semantic evidence in a satellite instance. GAV achieves a new state of the art on MoP-UAV with 62.55% Acc@0.5. We also introduce CVOGL-Text, a benchmark for text-guided grounding from street- and drone-view queries to satellite images. GAV outperforms the click-point baseline by 7.09 and 6.79 Acc@0.25 points on the street- and drone-view splits, respectively, demonstrating robustness to larger viewpoint gaps. The code and annotations will be publicly released.

---


### 196. [Change the Funnel, Not Who May Submit: Engineering Peer Review for the Flood](https://arxiv.org/abs/2611.01076)

**<font color=#1a73e8>作者：</font>** Mikhail L. Arbuzov, Lee Mosbacker, Sisong Bei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every reviewer knows the feeling: more papers each cycle, three full reviews for each of them, and a suspicion that near the accept line the outcome is luck. The numbers bear it out. NeurIPS received 30,709 submissions in 2026, more than three times as many as in 2021, and reviewing them took some 184,000 expert hours, or 92 years of researchers' time. Three-quarters of those hours went to papers that were rejected. And when NeurIPS twice had the same papers reviewed by two committees, the second rejected half of what the first accepted.
Conferences are responding by limiting who may submit. We simulated that answer, and an alternative, in a model calibrated to the NeurIPS experiments. The limits save little and select no better, and those based on a past acceptance fall mostly on new authors. The alternative changes how papers are judged, spending full reads only where a decision turns on them. In a staged funnel, an automated quality check first turns back papers that are not ready. The rest are ranked by their value, from short summaries, by readers that each submission brings. Only the finalists get a full read, which checks their claims and settles the final ranking. The staged funnel needs a little over half of today's expert hours, accepts 95.5% of papers in the top 3-10% (against 74% today), and makes nearly every top-0.5% paper a spotlight or oral. And because every paper brings its own reader, the funnel keeps pace with the flood.

---


### 197. [CuPH: Parallel Cubical Persistent Homology via Level-Synchronous Component Tracking](https://arxiv.org/abs/2611.01078)

**<font color=#1a73e8>作者：</font>** Guangyu Meng, Pengfei Gu, Erin Wolf Chambers 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Persistent homology (PH) is a mathematically principled multi-scale topological descriptor of shape and connectivity in data. It is widely applied in image classification, segmentation, and shape analysis across medical and aerial imaging, providing structural information that pixel-wise deep learning may overlook. Standard cubical PH decomposes an image into cubical cells (vertices, edges, and squares) and reduces them sequentially in filtration order. This sequential reduction has $\Theta(n)$ parallel depth for an $n$-pixel image, limiting within-image GPU parallelism and constraining its use in topology-aware deep learning. We introduce CuPH, a GPU-based parallel algorithm for computing cubical PH on 2D images that operates directly on pixels rather than cubical cells. CuPH buckets pixels by filtration values, activates them with a level-synchronous sweep, and tracks connected components with a lock-free union-find method. We prove that CuPH produces persistence diagrams identical to standard cubical PH on integer inputs, with a stability bound for floating-point inputs. CuPH reduces parallel depth from $\Theta(n)$ to $O(L\log n)$ for an image with $L$ intensity levels. We implement the level sweep as a single CUDA kernel, eliminating cross-level kernel-launch overhead. Empirically, CuPH is $18.6$--$99.6\times$ faster than the existing GPU baseline (CMP). As a drop-in PH backend, CuPH accelerates topology-aware classification ($4.2$--$16.7\times$) and segmentation ($8.3$--$44\times$) while preserving accuracy. It also enables computing full-image PH losses on high-resolution images, improving segmentation Dice by $2.2$--$4.6$ points over patch-local PH baselines and accelerating training by $25$--$31\times$.

---


### 198. [VeilFL: Two-Stage Accountability for Anonymous Federated Learning](https://arxiv.org/abs/2611.01082)

**<font color=#1a73e8>作者：</font>** Varesh Mishra, Aysajan Abidin, Bart Preneel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Anonymous credentials can hide which registered client participates in federated learning, but their unlinkability also makes repeated misconduct difficult to associate. We present VeilFL, a two-aggregator protocol that adds staged accountability to PINE (USENIX Security '24). Each submission binds two private PINE messages, a round-specific pseudonym, and a tracing pair to the same hidden credential secret. This design enables detection of duplicate submissions within a round without introducing a persistent identifier for normal participation. VeilFL implements accountability in two stages. After a confirmed duplicate or joint PINE rejection, a threshold tracing committee reveals a stable handle that links faults associated with the same credential. The client's registered identity is recoverable only after the public log records the requisite number of linked faults and a separate threshold committee authorizes identification. Accepted and unopened submissions remain unlinkable under the stated assumptions. This work establishes submission binding and duplicate detection, anonymity, fault non-frameability, controlled two-stage opening, and preservation of PINE's privacy and validity guarantees. In the prototype implementation, creating a submission requires a median of 2.11 ms, while verification requires 3.01 ms. Batch verification reduces the cost to 1.86 ms per submission for a batch of 1,000. The public part of each submission is 608 bytes, with 1,248 bytes of additional VeilFL protocol data across the two aggregator submissions. Each opening stage completes within 4.3 ms for the different committee configurations.

---


### 199. [QVR3D: Query-Guided Visual Reasoning for Training-Free 3D Grounding](https://arxiv.org/abs/2611.01084)

**<font color=#1a73e8>作者：</font>** Jung-Hao Kao, Jing-En Huang, Jia-Wei Liao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D visual grounding localizes objects in 3D scenes from natural language descriptions, requiring reasoning over semantics, spatial relationships, and multi-view observations. Training-free approaches avoid costly annotations but often rely on explicit scene transformation or scene-level frame selection, which may waste limited visual capacity on query-irrelevant regions. We observe that effective grounding should prioritize observations that provide evidence for the query rather than uniformly represent the entire scene. Based on this insight, we introduce QVR3D, a query-guided visual reasoning framework that operates on RGB-D observations using off-the-shelf foundation models. QVR3D combines Query-Guided Maximum Coverage (QGMC) for selecting complementary query-relevant views with Grounding Probability Estimation (GPE) that integrates instance confidence, attribute consistency, and relationship consistency. The framework supports both single- and multi-object grounding without task-specific adaptation. Experiments on ScanRefer and Nr3D achieve state-of-the-art zero-shot performance, while QGMC also improves frame efficiency across multiple 3D vision-language tasks. Our code is available at this https URL.

---


### 200. [Pop Goes the Verifier: Phoneme-Targeted Data Poisoning of Voice Liveness Detection](https://arxiv.org/abs/2611.01095)

**<font color=#1a73e8>作者：</font>** Eshaq Jamdar, Amith Kamath Belman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Many Automated Speaker Verification Systems (ASVs) commonly employ liveliness detection techniques, such as VoicePop, which identify genuine speech by analyzing low- frequency pop bursts from plosive phonemes using Gammatone Frequency Cepstral Coefficients (GFCC) and an SVM classifier. While effective against traditional replay attacks, such systems are vulnerable to data poisoning techniques. Prior work shows that broadly applied SyntheticPop attacks can collapse model to accuracy to as low as 14.01% using only 20% poisoned samples, but the resulting artifacts are easily detectable when visualizing the waveform energies. This paper introduces Pop Goes the Verifier, a stealthier phoneme injection poisoning attack. By leveraging FastSpeech 2 (FS2) with a modified HiFi-GAN vocoder, we inject localized pop bursts at plosive phoneme locations and overlay subtle Gaussian noise to reduce the visibility of injected artifacts in waveform and spectrogram analysis. Using the ASVSpoof 2019 as the dataset, we observe that the approach achieves a moderate poisoning attack while providing greater resistance to signal-level inspection than the original SyntheticPop attack.

---


> [!TIP]
> 当前位于：**151-200**（第 4/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

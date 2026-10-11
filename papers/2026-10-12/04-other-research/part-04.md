# 📦 其他研究 | 2026年10月12日

> 本类共 **329** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-329](./part-07.md)

---

### 151. [Why machines will still not rule the world](https://arxiv.org/abs/2610.11424)

**<font color=#1a73e8>作者：</font>** Jobst Landgrebe, Barry Smith  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In our book Why machines will never rule the world [13, 14] we argue that arti- ficial general intelligence is mathematically impossible. This is because the human beings and the processes which exhibit intelligence are complex systems whose be- haviour cannot be captured by the kinds of models that we can generate with or without computers. Proponents of contemporary machine intelligence respond with two lines of argument: a theoretical one, grounded in the universal approximation theorems for neural networks and the Church-Turing-Deutsch principle; and an em- pirical one, grounded in rapidly rising scores on standardized benchmarks. In this communication we examine and reject both responses. First, we show serious issues in the physicalist counter-argument based on the Church-Turing-Deutsch principle. Second, we review recent evidence to the effect that prominent benchmarks are compromised by training-data contamination, flawed test construction, and strate- gic optimization. Our central argument remains: That models required to perform cognitive behaviour in open-ended, thermodynamically complex and non-ergodic environments are not and will not become achievable.

---


### 152. [EchoDiST: Self-distillation-based joint learning for diffusion-conditioned echocardiographic myocardial motion estimation](https://arxiv.org/abs/2610.11431)

**<font color=#1a73e8>作者：</font>** Feiyue Qi, Xingyue Wei, Jianwen Luo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion estimation in echocardiography is essential for quantitative assessment of cardiac function and myocardial mechanics, but remains challenging due to image artifacts, limited image information, speckle decorrelation, and the scarcity of ground-truth displacement fields. Anatomy-guided approaches can provide structural information, yet often rely on expert-labeled myocardial segmentations. We propose EchoDiST, a framework for unsupervised echocardiographic myocardial motion estimation that integrates self-distillation-based joint learning with a diffusion-conditioned motion estimation network. Here, unsupervised motion estimation refers to learning without ground-truth displacement fields. The self-distillation strategy jointly optimizes anatomical segmentation and myocardial motion estimation under limited anatomical annotations. Diffusion-based conditioning is used during training with stochastic perturbations, while inference requires only a single deterministic forward pass without iterative reverse-diffusion sampling. EchoDiST was evaluated on three echocardiographic datasets, including two external test datasets under cross-view and cross-dataset settings. Compared with seven representative learning-based methods, EchoDiST consistently improved anatomical alignment, myocardial strain assessment, and motion-derived functional and cardiac-phase assessment. These gains were statistically significant across the evaluated tasks and datasets. Overall, EchoDiST provides an effective approach for reliable myocardial motion estimation under limited anatomical supervision and supports downstream quantitative assessment of cardiac function.

---


### 153. [On-Chain Archaeology of Bitcoin Oracles: Evidence of Use under Limited Observability](https://arxiv.org/abs/2610.11439)

**<font color=#1a73e8>作者：</font>** Giulio Caldarelli  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Before Ethereum made the "oracle problem" a household term, Bitcoin already had oracles serving as feeds, key-release services, federated signers, and arbiters that carried real value on the main chain. This study traces their use and the changing evidence of oracle activity from early days through July 2026. We combine a complete census of Counterparty betting (1,149 bets), analysis of the full Bitcoin chain through block 958,628, and searches for documented keys from Reality Keys, Orisi, Bitrated, and Oraclize in an 854-million-row public-key index. We also recover DLC oracle records from an archived explorer and live Nostr relays. Two results emerge. First, early contracts remain on-chain, but many event descriptions have disappeared, and protocol encoding and API limitations complicate access to the surviving record. However, for modern DLCs, public oracle announcements can survive even when the contracts using them cannot be identified on-chain. In the script classes examined, the share of spends that reveal no script peaks at 81.9% in 2024 after excluding spends containing inscription data. Second, public registries can give a misleading picture of oracle use. In Counterparty, 95% of pre-2018 sources declaring an oracle fee were never bet on. In Bitrated, 0.1% of archived keys appear on-chain overall, compared with 10 of 19 keys captured in 2014. Sport dominates Counterparty's matched volume, while a daily price series dominates the archived DLC announcements. These findings show how protocol design and data preservation shape the historical record of Bitcoin oracle use.

---


### 154. [MotiveMob: Motivation as Semantic Action for Closed-Loop Human Mobility Generation](https://arxiv.org/abs/2610.11442)

**<font color=#1a73e8>作者：</font>** Mengkun Gao, Zengqing Wu, Renhe Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human mobility generation, an important task in urban research, synthesizes trajectory data for urban planning and transportation management. Human mobility can be characterized as a "why-where-when" decision process: people form an intention to move and then determine where and when the corresponding activity will take place. Trajectory generation under user-level and temporal distribution shifts may benefit from explicitly modeling this decision structure. However, many existing human mobility generation methods either represent behavioral intent at a coarse granularity, such as a daily plan or a trajectory-level description, or directly predict future locations without explicitly reasoning about a possible motivation for each movement step. We introduce MotiveMob, a motivation-driven autoregressive framework for human mobility generation that first forms a hypothesis about why the next movement may occur and then jointly generates where and when it may occur. At each step, a motivation predictor conditions on the current mobility state, a long-term behavioral report, and the mobility history to infer a plausible motivation or determine whether the trajectory should terminate. Given the hypothesized motivation, a state predictor grounds it in a candidate next location and arrival time. The candidate then undergoes speed-feasibility and repetition checks before being fed back for the next decision. We evaluate MotiveMob under distribution shifts involving unseen users and unseen temporal periods, including seasonal changes and the substantial behavioral disruption caused by the COVID-19 pandemic. Experiments show that MotiveMob consistently achieves better distributional fidelity than competitive pretraining-based and prompting-based methods under user-level and temporal distribution shifts, demonstrating robust generalization to out-of-distribution mobility patterns.

---


### 155. [Learning to Retrieve: Internalizing Memory Retrieval for Video World Models](https://arxiv.org/abs/2610.11444)

**<font color=#1a73e8>作者：</font>** JiaKui Hu, Tailai Chen, Yuqi Pan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models aim to generate explorable, 3D-consistent scene videos conditioned on camera trajectories. Existing approaches often rely on external memory systems that explicitly retrieve previously observed content to mitigate scene drift during long-horizon generation. However, these auxiliary memory pathways operate outside the model's internal generative dynamics, preventing the model from intrinsically learning when and what historical information should be retrieved. We propose to internalize memory retrieval into the generation process, allowing retrieval to emerge as an intrinsic behavior of the video world model rather than relying on an external memory system. Based on this principle, we introduce \textbf{Learning-to-Retrieve (L2R)}, which repurposes the model's persistent internal state as a memory for historical context. A camera-conditioned retrieval gate selectively accesses relevant historical information from this state, determining \textit{what to retrieve}, while a retrieval trigger determines \textit{when to retrieve}. We further supervise the trigger with a 3D re-visibility signal, activating retrieval when previously observed content re-enters the current view while otherwise preserving the existing context. Together, these components enable the model to intrinsically acquire memory retrieval behavior and incorporate relevant historical observations into generation without a separate retrieval pathway. Across multiple base models and camera-revisit benchmarks, L2R improves long-term scene consistency while eliminating the need for an external memory bank or 3D conditions. this https URL

---


### 156. [Zatom-2: Multitask Pretraining on Atomistic Data for Generative Modeling across Domains](https://arxiv.org/abs/2610.11454)

**<font color=#1a73e8>作者：</font>** Miruna Cretu, Alex Abrudan, Antonia Panescu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unified atomistic modeling has the potential to accelerate discovery in chemistry, materials science, and biology by bridging data-rich chemical domains and data-scarce biological contexts. However, existing generative approaches to atomistic modeling remain highly specialized to scientific disciplines (chemistry vs. biology) or do not leverage both high-volume organic (molecule) and inorganic (material) data for general-purpose pretraining. To this end, we introduce Zatom-2, an atomistic generative model pretrained on approximately five million structures from the OMol25 and OMat24 electronic structure datasets. Zatom-2 features a multiscale Transformer architecture coupled with conditional flow matching that supports force conditioning and foundational pretraining tasks such as generation, structure prediction, and prediction of molecular and material energies and forces. Empirically, Zatom-2 achieves better molecular distribution fidelity than Zatom-1 and achieves strong performance on existing molecule and material generation benchmarks. Zatom-2 demonstrates the ability to control sample generation across low- and high-force regimes, and enhances protein generation in a low-data setting through joint generative-predictive pretraining and transfer learning, increasing protein backbone designability in a length extrapolation setting from 67.8% without pretraining to 74.8% after finetuning on 2,000 protein domains.

---


### 157. [SpikeSSL: A Universal Spike Inference Framework with Dynamics-Informed State-Space Layers](https://arxiv.org/abs/2610.11456)

**<font color=#1a73e8>作者：</font>** Chenghao Yue, Siming Xing, Shuran Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Two-photon calcium imaging is a standard tool for recording large neural populations in vivo, yet inferring spikes accurately across the growing diversity of calcium indicators remains an open problem. Existing supervised methods achieve reasonable in-domain accuracy but generalize poorly to unseen indicators, because different indicators induce distinct fluorescence kinetics and signal statistics while existing architectures remain relatively simple generic temporal regressors without dynamics-matched inductive bias. We propose SpikeSSL, a universal spike inference framework whose temporal backbone is a bank of bidirectional IIR state-space layers broadly motivated by calcium dynamics. A multi-modal conditioning encoder maps indicator identity, sampling rate, and trace-level signal statistics into a global conditioning vector that modulates the backbone via Adaptive Layer Normalization, while a heteroscedastic variance head provides calibrated per-frame uncertainty. On a benchmark with five fixed evaluation splits built from 33 public ground-truth datasets, SpikeSSL achieves state-of-the-art performance in both in-domain and zero-shot leave-one-indicator-out settings. We also develop a biophysical simulation pipeline capable of generating paired fluorescence-spike traces with systematically varied kinetic parameters, spike statistics, response nonlinearities, baseline drift, and noise. Using this pipeline, we synthesize approximately 11,000 simulated traces. Augmenting training with these data effectively closes the cross-indicator domain gap and improves zero-shot generalization. Code is publicly available at this https URL.

---


### 158. [ProtoSemImage: Image-Valued Prototypes with Deformable Row Alignment for Interpretable Document Classification](https://arxiv.org/abs/2610.11460)

**<font color=#1a73e8>作者：</font>** Mohammad Zare, Pirooz Shamsinejadbabaki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prototypes in classification models are almost always vectors, and a vector has no readable form. This paper asks what happens when a prototype is an image. Documents give the question a natural form, because a document can be rendered as a multi-channel image in which every token becomes a pixel, so a class representative can take the same shape and the same channel semantics as the inputs it stands for. ProtoSemImage represents each class by one or more visual archetypes: prototype images in a four-channel HSV space whose channels carry named linguistic factors. A Skip-Gram objective learns that color space end to end through a four-dimensional bottleneck, discourse boundary rows become differentiable typed difference rows, and classification reduces to 2D visual template matching: a deformable row alignment between a document image and the archetype bank, in the spirit of dynamic time warping. Because the match is a spatial pattern comparison rather than a linear readout, the model reports where an input departs from its archetype and along which channel, and a generative head decodes each archetype back into text. The image representation works: it beats an otherwise identical model with vector prototypes in all three paired seeds, by between 4.3 and 11.8 points on a ten-class task. The distance-based matching does not. A diagnostic that keeps the representation fixed and swaps only the classifier recovers the sequence baselines, which locates a 20.6-point shortfall in the matching rather than in the color compression, and a benchmark built so that a pair of documents shares a bag of words and differs only in arrangement confirms the layout-preservation it was designed for. We report both directions, because for a representation whose whole purpose is inspect ability, the failure modes are as informative as the gains.

---


### 159. [SpheriColor: Colormaps for Spherical Geospatial Input Topographies](https://arxiv.org/abs/2610.11470)

**<font color=#1a73e8>作者：</font>** Julius Rauscher, Johannes Fuchs, Daniel A. Keim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multivariate geospatial data visualization often relies on multiple coordinated views, where color can be used to either link views or encode data attributes. Encoding spatial locations through color can reveal patterns in non-spatial visualizations, yet most applications of colormaps focus on high-dimensional attribute encodings instead. While 2D colormaps have been studied extensively, color encodings designed for spherical geospatial data have received much less attention, even though all locations lie on a sphere. To address this, we propose SpheriColor, a colormap generation approach for mapping geospatial references guided by the design goals of distance preservation and colorspace exploitation. We project a geospatial distance function into a perceptually linear colorspace, followed by two different gamut-constrained optimization strategies. We perform a quantitative evaluation using both real-world and synthetic datasets, demonstrating superior performance over 2D colormaps and HSLuv double cone encodings. The simplex-based optimization excels at distance preservation, whereas the ray-based approach provides better colorspace exploitation.

---


### 160. [A Survey of Security Research for Operating Systems](https://arxiv.org/abs/2610.11471)

**<font color=#1a73e8>作者：</font>** Masaki Hashimoto, Ruo Ando, Toshiyuki Maeda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In recent years, information systems have become the social infrastructure, so that their security must be improved urgently. In this paper, we introduce the results of the survey of virtualization, operating system verification and access control technologies in association with the design requirements of the reference monitor. Additionally, we show the prospects and challenges for each technology.

---


### 161. [Rare Gate Disagreements Can Limit Plasticity: When Gradient Flow Mispredicts Finite-Batch SGD](https://arxiv.org/abs/2610.11475)

**<font color=#1a73e8>作者：</font>** Ruoyu Zhao, Mingxuan Zhang, Jianbo Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Population gradient flow is a common tool for reasoning about how neural networks adapt, including after pretraining. We show that it can mispredict finite-batch stochastic gradient descent (SGD) qualitatively, and we trace the discrepancy to a specific mechanism. In a two-unit ReLU regression, a source task drives the two neurons toward positive proportionality and a target task rewards separating them. After source training for time $T$, gradient flow recovers on the target in time linear in $T$. Online SGD with batch size $b$ and step size $\eta$ in both phases instead fails with high probability throughout a horizon of order $e^{c/\eta}$ once $T \gtrsim \log(b/\eta)$, uniformly on an explicit set of initializations with Gaussian probability above one percent. For each fixed $T$, small-step SGD still recovers, so the failure requires the joint limit of small steps and long pretraining. At the target clone, the population instability is carried entirely by inputs on which the two ReLU gates disagree. For units at angle $\delta$ these inputs form a wedge of probability $\delta/\pi$, and weight decay shrinks the angle exponentially during pretraining. On every other input both units receive the same random linear update, which contracts their separation in conditional expectation. Bounding the cumulative probability of sampling the wedge along the exact online recursion, without a diffusion approximation, shows that recovery with fixed probability from an identical source-gradient-flow checkpoint, within $e^{c/\eta}$ updates, requires $Nb \gtrsim e^{\lambda T}$ target samples and batch size $b \gtrsim \eta e^{\lambda T}$, where $N$ counts updates and $\lambda$ is the weight decay. In simulations, recovery is approximately a function of the disagreement budget $b\delta/\eta$ and saturates in the horizon.

---


### 162. [Conditional Residual Prediction: Improving Autoregressive Video Diffusion without a Bidirectional Teacher](https://arxiv.org/abs/2610.11479)

**<font color=#1a73e8>作者：</font>** Bowen Zheng, Zhiguang Liu, Jiarong Ou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Causal video diffusion models generate video autoregressively, which suits streaming, interactive, and long-video generation. Under standard training, however, they often yield lower generation quality than bidirectional models of the same size. Many existing approaches address this gap by initializing from or distilling a pretrained bidirectional teacher. We instead train a causal model from an image-model initialization, with no bidirectional video model at any stage. Because this path requires neither a large bidirectional teacher nor a complex distillation pipeline, it is simpler and more scalable. On this path, we find that a causal model trained on ground-truth history becomes strongly dependent on it, so that at inference errors in its own generated history propagate forward. We hypothesize that much of this dependence is unnecessary, because the current input already determines much of what the history provides. We propose Conditional Residual Prediction (CRP), a simple recipe for reducing a model's reliance on a condition: the model first predicts the target without the condition, and the condition may only add a residual on top of this prediction. Applied to history, CRP makes the model predict each chunk from the present as far as it can and use the past only for what the present cannot supply. In controlled experiments, CRP nearly closes the 6.14-point gap to a bidirectional model trained under the same setup. Scaling this recipe, we train Optica, a 2B-parameter causal video model that autoregressively generates 5-second 480p videos and reaches 82.78 on VBench with only about 15M training videos.

---


### 163. [BridgeGuard: Explicit Safety Drift for Diffusion-based Autonomous Driving](https://arxiv.org/abs/2610.11483)

**<font color=#1a73e8>作者：</font>** Zhenjun Qiu, Jianing Huang, Dongang Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion-based driving planners capture diverse behaviors but can generate unsafe trajectories under distribution shift. We propose BridgeGuard, a safety-constrained diffusion planning method that progressively strengthens a constraint term during denoising to drive intermediate trajectories toward a scene-dependent safety domain. Corrections operate in a low-dimensional curve space, promoting geometric coherence. A learned module, DistanceFieldNet, predicts a time-dependent distance field from bird's-eye-view features. Value and spatial-gradient supervision at queries sampled beyond expert trajectories teaches this field about both safe and unsafe regions. The learned field supplies the constraint term through safety injection while the pretrained perception backbone and planner remain frozen. We further establish sufficient conditions for terminal safety in an idealized continuous-time bridge. On Bench2Drive, BridgeGuard improves driving score/success rate from 87.99/74.99% to 90.88/76.36% for BridgeDrive and from 80.79/58.18% to 90.46/74.09% for $\text{DiffusionDrive}^{\text{geo}}$, demonstrating cross-model generalization.

---


### 164. [MARC: Multi-Bit Watermarking for Autoregressive Audio Generation against Codec Attacks](https://arxiv.org/abs/2610.11488)

**<font color=#1a73e8>作者：</font>** Liaoran Xu, Weizhi Liu, Zhaoxia Yin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generated audio is now used in a range of applications, creating a need to verify its origin after distribution and signal processing. This task is particularly challenging for autoregressive audio generation because codec processing can alter the token sequence recovered from the waveform. Such changes reduce the reliability of watermark detection and payload decoding. Existing methods construct token groups using either intrinsic token representations or substitution patterns caused by transformations. As a result, intrinsic token relationships and codec induced substitutions are modeled separately. In addition, most methods support only zero bit detection. They can determine whether a watermark is present but cannot distinguish individual generated outputs. We propose \textbf{MARC}, a multi-bit generative watermarking method for autoregressive audio generation. MARC integrates intrinsic token representations with confusion patterns obtained through retokenization and multiple codecs, forming a codec-aware token-cluster space. Within this space, payload-driven cluster scheduling is used to embed a multi-bit watermark, while detection and payload decoding are performed on retokenized observations. Experiments on speech, dialogue, and music generation show that MARC achieves an average of 97.3\% bit extraction accuracy on unmodified watermarked audio and the watermark can still be extracted under diverse codec attacks. MARC also demonstrates robustness to overwriting attacks.

---


### 165. [Beyond Resolution: Object-to-Image Ratio Mismatch in Instance Retrieval](https://arxiv.org/abs/2610.11489)

**<font color=#1a73e8>作者：</font>** Boaz Meivar, Ofir Kedem, Amit Edenzon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual instance retrieval often fails when the same object appears at different apparent sizes in the query and gallery. We show that the dominant cause is usually not resolution loss but object-to-image (O2I) ratio mismatch: the object occupies different fractions of the two images. On a controlled benchmark of 3,021 Objaverse objects rendered at five camera distances, more than 80% of the cross-distance degradation is attributable to O2I mismatch rather than resolution for 9 of 12 pretrained backbones; multi-scale architectures cut the resolution-only effect to single digits yet remain equally susceptible. The failure is also asymmetric: tight queries retrieve more reliably against wide gallery images than the reverse. Guided by this analysis, query-side scale augmentation and an OWLv2 crop reranker reach state of the art on ILIAS 100M (29.2 mAP@1000 before reranking, 42.0 after) without training or modifying the precomputed gallery index, and a LoRA fine-tune matches the query-side gains at a single forward pass, showing that O2I robustness is learnable.

---


### 166. [A Zero-Knowledge Signature Framework for Efficient Post-Quantum Message Authentication in Cooperative Automated Driving](https://arxiv.org/abs/2610.11490)

**<font color=#1a73e8>作者：</font>** Takahito Yoshizawa, Aysajan Abidin, Edoardo Pena-Gonzalez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Connected and Automated Vehicles (CAV) rely on authenticated Vehicle-to-Everything (V2X) communications to exchange safety-critical information among vehicles and roadside infrastructure. As the automotive industry transitions toward post-quantum cryptography (PQC), the significantly larger public keys and signatures of standardized PQC digital signature algorithms introduce substantial communication overhead, which challenges the scalability of certificate-based V2X authentication, particularly for high-frequency cooperative awareness messages (CAM). This paper presents ZKS-PQC, a zero-knowledge signature framework that enables communication-efficient post-quantum message authentication for cooperative V2X systems. Instead of transmitting complete post-quantum public keys and signatures, the proposed framework replaces this authentication material with a compact Zero-Knowledge Proof (ZKP) while preserving compatibility with existing certificate-based trust architectures. This approach supports incremental migration and backward compatibility with the legacy ECDSA. The framework is implemented using the Open Quantum Safe (liboqs) and ZKP (Bulletproofs) libraries, and we evaluated the performance of standardized NIST PQC signature algorithms and additional candidate algorithms. Experimental validation on both a Linux platform and a commercial On-Board Unit (OBU) demonstrates substantial reductions in message size exceeding 95% for all algorithms, while limiting additional processing overhead by staying within the order of milliseconds at both sender and receiver in many algorithms, consistent with the latency requirements of real-time V2X operation. By decoupling communication overhead from the size characteristics of post-quantum signature algorithms, ZKS-PQC offers a practical migration strategy for scalable, quantum-resilient message authentication in future CAV systems.

---


### 167. [Stop My Dancing! Understanding, Detecting and Attributing Motion-Aware Deepfake Videos](https://arxiv.org/abs/2610.11496)

**<font color=#1a73e8>作者：</font>** Fazhong Liu, Yan Meng, Tian Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pose-guided diffusion models can now synthesize entire human figures in motion, spawning a new class of deepfakes: Motion Aware Deepfake (MAD) that have already reached hundreds of millions of viewers. To better understand this emerging threat, we construct the first MAD-specific benchmark and measurement framework, containing over 1.5 million frames that mix 1,363 real and 30,122 synthetic videos from six controllable generators, with realistic perturbations and open-world evaluation splits. Then, we dissect MAD and discover that, despite their global coherence, these videos betray faint yet reliable cues: because the model relies on limited input frames for motion synthesis, it must predict and simulate coherent movement at motion boundaries, thereby producing high-frequency artifacts along with model-specific spectral fingerprints. Based on the observations obtained from analysis on dataset, we propose MoDA, the first defense framework tailored to detect and attribute MAD videos. MoDA couples spatial semantics with steganalysis-rich frequency features via cross-domain alignment and multi-scale aggregation, achieving 94.8% in-distribution and 89.1% cross-dataset detection accuracy gains of 10% to 25% over prior work and 91.5% model attribution accuracy. MoDA achieves 81.94% accuracy on 200 clips produced by two unseen commercial MAD platforms, indicating promising zero-shot transfer, and 78.13% detection accuracy on 1,200 unseen MAD video clips (55k frames in total) collected from the open Internet. Under white-box, gray-box, and black-box adaptive attacks, MoDA maintains relatively stable detection and attribution performance while the accuracies of the baselines drop rapidly.

---


### 168. [Parametric Trajectory Distillation for Few-Step Video Generation](https://arxiv.org/abs/2610.11498)

**<font color=#1a73e8>作者：</font>** Lan Feng, Peter Karkus, Maximilian Igl 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion and flow models require many sequential evaluations, making generation computationally expensive. Few-step distillation reduces this cost but poses a capacity allocation problem: a student must match the teacher's iterative generation with far less sequential computation. Existing trajectory methods ask the student to reproduce teacher transitions that are highly curved at high noise, which can exceed its capacity and degrade fine detail. We introduce Parametric Trajectory Distillation (PTD), which lets the student parameterize teacher trajectory segments as polynomials and learn from teacher guidance along its own predicted path. PTD is designed to let the learned curvature adapt to the backbone's predictive capacity, preserving motion and diversity. The curvature head is used only in training; inference keeps the original backbone architecture. On Wan2.1-14B, four-step PTD sets a new state of the art for trajectory distillation, significantly improving dynamic quality and naturalness over PDD, the best-performing trajectory-only method on this model, under the same training setting. On the 33B audio-video MiniMax-H3, LoRA-trained PTD significantly improves diversity and naturalness over the state-of-the-art LightX2V Turbo. Blinded human votes give PTD 55.1% and 63.4% preference shares against PDD and LightX2V Turbo. Project page: this https URL.

---


### 169. [The Operator Mismatch Problem: Deploying BEV Perception with Portable GPU Compute](https://arxiv.org/abs/2610.11504)

**<font color=#1a73e8>作者：</font>** Rohit Verma, Anand V Bodas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern autonomous driving systems rely on bird's-eye-view (BEV) perception models that fuse camera and LiDAR inputs to detect objects in 3D space. These models are accurate, but they cannot be deployed through standard inference runtimes. The reason is an operator mismatch between dense convolutions (which runtimes handle well), sparse 3D convolutions (which runtimes cannot represent), and geometric scatter operations (which runtimes have no vocabulary for). Today, every sparse convolution library is CUDA-only and PyTorch-coupled, locking BEV deployment to a single vendor's hardware and a single execution framework.
We present BEVPIPE, a framework for deploying multimodal BEV perception pipelines using portable GPU compute APIs and integrating them with production inference runtimes. BEVPIPE partitions the model into runtime-managed dense subgraphs and three external operator extensions (voxelizer, sparse encoder, BEV projector), connected through a shared GPU memory space. BEVPIPE achieves a 19.5x end-to-end speedup over conventional deployments while retaining 98.5% of reference mAP. We also showcase that BEVPIPE is portable across different GPU backends.

---


### 170. [Compactness and Consistency: A Conjoint Framework for Deep Graph Clustering](https://arxiv.org/abs/2610.11506)

**<font color=#1a73e8>作者：</font>** Wei Ju, Siyu Yi, Kangjie Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph clustering is a fundamental task in data analysis, aiming at grouping nodes with similar characteristics in the graph into clusters. This problem has been widely explored using graph neural networks (GNNs) due to their ability to leverage node attributes and graph topology for effective cluster assignments. However, representations learned through GNNs typically struggle to capture global relationships between nodes via local message-passing mechanisms. Moreover, the redundancy and noise inherently present in graph data may easily result in node representations lacking compactness and robustness. To address these issues, we propose a conjoint framework CoCo, which captures compactness and consistency in the learned node representations for deep graph clustering. Technically, our CoCo leverages graph convolutional filters to learn robust node representations from both local and global views, and then encodes them into low-rank compact embeddings, thus effectively removing the redundancy and noise as well as uncovering the intrinsic underlying structure. To further enrich the node semantics, we develop a consistency learning strategy based on compact embeddings to facilitate knowledge transfer from the two perspectives. Our experimental results indicate that our CoCo outperforms state-of-the-art counterparts on various datasets.

---


### 171. [EIFL: Efficiently Protecting Global Model Privacy and Integrity Against an Untrusted Server in Federated Learning](https://arxiv.org/abs/2610.11511)

**<font color=#1a73e8>作者：</font>** Zehui Liao, Qiang Li, Binghui Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) typically adopts a server-client architecture, where the server aggregates clients' local models (i.e., the input) and returns the aggregated global model (i.e., the output) to clients. An untrusted server may return a tampered global model to compromise the output integrity. Some existing schemes focus on verifying the output integrity. However, these schemes mostly rely on clients pre-negotiating a set of identical auxiliary information among themselves and keeping it confidential from the server. This dependency creates a verification vulnerability: if the auxiliary information is leaked, the verification method may be circumvented. Additionally, in some privacy-sensitive scenarios (e.g., commercial federated learning), the global model may need to be kept confidential from an untrusted server. However, only a few works achieve the output privacy while addressing verification vulnerability, at the cost of prohibitive computation and communication overhead. To address these challenges simultaneously, we propose a novel provably privacy-preserving FL method called EIFL. Specifically, we adopt a two-stage aggregation and combine it with symmetric encryption to protect the output privacy. To address the verification vulnerability, we propose an efficient verification method based on vector inner product for output integrity, and a random vector generation method for clients to agree on auxiliary information. EIFL innovatively binds the auxiliary information to the output integrity, and eliminates the need to keep the auxiliary information confidential from the server. Moreover, EIFL is robust against client dropout during the verification phase through a simple resending operation. Evaluation results validate the advantages of EIFL over state-of-the-art schemes in terms of computation and communication overhead.

---


### 172. [Certifying Hidden Paths: Scalable Topology Assurance for QKD Networks](https://arxiv.org/abs/2610.11513)

**<font color=#1a73e8>作者：</font>** Alessandro Colombo, Margherita Cozzolino, Stephan Krenn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large-scale Quantum Key Distribution (QKD) networks rely on trusted repeaters, making the security properties of the selected communication path an essential part of end-to-end assurance. At the same time, network operators may be unwilling to disclose their internal topology. We present a topology-certification mechanism that lets a provider prove in zero knowledge that policy-compliant routes between two endpoints exist, without disclosing the routes in an individual presentation. Our main idea is to certify nodes and edges independently using multi-message signatures, rather than signing the complete graph as one object. For a route chosen in advance, proof size and cryptographic proving and verification work depend on its positions and attributes, independently of the overall network size, whereas route discovery and certification have separate graph-dependent costs. The construction hides the actual route length up to a public bound and sketches extensions to node-disjoint routes and monotonic additions within a graph epoch. We give a formal security model and conditional proofs of unforgeability and graph hiding for a generic construction. For a BBS-based construction, presentation-size estimates remain below $300$\,KiB at $\ell=m=n=50$, and measured generation and verification times remain below $400$\,ms at $\ell=64$ and $m=n=8$.

---


### 173. [When Can You Prune Your Network? A Study of Intermediate Neurons in Multilingual Speech Parsing](https://arxiv.org/abs/2610.11520)

**<font color=#1a73e8>作者：</font>** Minnie Kabra, Benjamin Lecouteux, Maximin Coavoux  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> End-to-end speech parsing, a task recently proposed, consists in predicting both the transcription and the syntactic tree for a spoken utterance. Existing architectures for speech parsing often utilise intermediate neural networks. In this work, we examine the effectiveness of intermediate neural networks (NN) for parsing, and, specifically, what role do they play. We introduce a simpler end-to-end architecture for speech parsing, where we remove these intermediate NN units, reducing the parameters by 12%, while achieving comparable or better performance than prior method on both automatic speech recognition (ASR) and parsing. We demonstrate that intermediate NN units help reduce the representational gap when the pre-trained encoder is frozen. We do a comprehensive evaluation of speech parsing on French, and medium-low resource languages Slovenian and Naija. We further investigate the impact of the training data size and intermediate layers of the pretrained speech encoder on speech parsing.

---


### 174. [When to Intervene? State-Aware Sparse Manipulation in Federated Reinforcement Learning](https://arxiv.org/abs/2610.11523)

**<font color=#1a73e8>作者：</font>** Shutong Zheng, Sijia Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated reinforcement learning (FRL) enables distributed agents to collaboratively train decision-making policies, but its decentralized training process also exposes global policy learning to Byzantine manipulation. Existing poisoning attacks primarily focus on how to construct malicious updates, while trajectory-level intervention timing remains largely implicit. In sequential decision making, however, where an intervention is applied can alter subsequent trajectories and learning signals. Through controlled experiments, we find that changing the selected trajectory states materially alters attack efficacy even when the malicious-update construction is fixed. We therefore identify when as a distinct attack dimension and introduce the Viability-constrained Behavioral Steering Attack (V-BSA), which uses local policy uncertainty to select sparse intervention states and applies envelope-constrained behavioral steering. Across discrete-action benchmarks, V-BSA achieves substantial degradation against robust aggregators and ensemble defenses with only a fraction of the interventions used by dense poisoning, while revealing task- and aggregation-dependent boundaries. Overall, our results highlight intervention timing as a distinct dimension of sequential robustness in FRL. The code is available at this https URL

---


### 175. [MSGAT: Multi-Head Spiking Graph Attention with Similarity-Space Fusion for Image-Text Retrieval](https://arxiv.org/abs/2610.11526)

**<font color=#1a73e8>作者：</font>** Xintao Zong, Wenxuan Liu, Jianhao Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks (SNNs) offer an energy-efficient computing paradigm through sparse event-driven computation, showing great potential for efficient multimodal learning. However, applying SNNs to high-level multimodal tasks, such as image-text retrieval (ITR), remains challenging, since sparse spike representations make it difficult to capture semantic structures required for cross-modal alignment. Existing spiking ITR methods rely on local alignment and additional soft-label supervision during training, while lacking awareness of structural and multi-granularity relationships. To address these issues, we propose a Multi-head Spiking Graph Attention Network (\textbf{MSGAT}) for structural modeling and equip it with dynamic attention heads to capture complementary relational patterns and enable spike-driven graph reasoning and aggregation. However, within a two-branch multi-granularity fusion framework, the fine-grained spike representations generated by MSGAT are sparse and discrete, whereas the global representations are continuous, making conventional feature-level fusion susceptible to interference across heterogeneous representations. Therefore, we introduce \textbf{Sim-Fuse}, a similarity-space fusion alignment strategy integrating coarse- and fine-grained matching relations while avoiding direct fusion of heterogeneous representations. Experiments on Flickr30K and MSCOCO show our method outperforms ANN methods under matched settings and existing SNN retrieval baselines. Moreover, with only two time steps, our SNN achieves comparable or superior performance to its ANN counterpart while reducing theoretical module-level energy by 55\%. The code is provided in the Supplementary Materials.

---


### 176. [AtomWorld-Mirror: Macro-Step World Modeling of Critical Evolution Backbones for Materials Dynamics](https://arxiv.org/abs/2610.11527)

**<font color=#1a73e8>作者：</font>** Ziming Pan, Ruge Zhang, Haozhi Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Atomistic simulation is a fundamental tool for studying long-term materials evolution, from diffusion and defect dynamics to interfacial reactions and fracture. Yet conventional simulators typically advance at microscopic resolution, spending substantial computation on low-impact local updates before reaching structurally consequential states, an evolutionary-resolution bottleneck that limits long-horizon simulation. We propose AtomWorld-Mirror, a time-aware macro-step world model for the critical evolution backbone of atomic systems. For Step-Wise atomistic simulation, AtomWorld-Mirror distills short micro-event segments into physically reachable transitions between key states, jointly predicting sparse structural edits and accumulated physical time through latent macro-step dynamics. Local reachability, inventory conservation, and continuous-time consistency constrain each transition. By amortizing local atomic physics into a reusable latent macro model and replacing explicit micro-event replay with macro-step inference, this formulation provides a path toward substantially faster prediction of long-term materials evolution while preserving structural validity and time semantics. Across five atomic systems, spanning Cu-rich RPV steel irradiation aging, Cu-Zr metallic glass, and Li$_3$N-based anti-perovskite solid electrolyte, macro-step inference delivers a speed up of $10^3$ to $10^4$ times over event-by-event simulation.

---


### 177. [HAND: A Biologically-Inspired Activation Function that Improves Generalisation and Sample Efficiency in Image Classification](https://arxiv.org/abs/2610.11534)

**<font color=#1a73e8>作者：</font>** Michael W. Spratling, Heiko H. Schütt  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> DNNs exhibit robustness and generalisation issues not seen in humans. They are also far less data-efficient learners, requiring considerably more training samples to accurately classify novel exemplars. Inductive bias could help with these issues by providing in-built mechanisms to improve generalisation, and hence, reduce reliance on learning from data. We incorporate a biologically-inspired inductive bias into a new activation function, HAND (Homeostasis, Accelerating Nonlinearity, and Divisive-nomalisation), and show its effectiveness with CNNs trained on image classification. Using HAND a ConvNeXt-tiny required 25 training epochs to reach the same accuracy on ImageNet1k as the unmodified model achieved after 200 epochs. Consistent with the effects of an inductive bias, the performance gap reduced with training time and increased data augmentation. When the volume of training data was reduced and unevenly distributed between classes (Long-tailed ImageNet) the improvements in accuracy were even larger and did not reduce with increased training time. Generalisation performance with the common-corruptions data, and the ability to reject samples from unknown classes, were unaffected or improved by HAND. Results generalised across CNN architectures and training data-sets. HAND can, therefore, reduce the required training time and/or the required volume and variety of training data, helping to improve sample efficiency.

---


### 178. [OX-NeRF: 3D X-ray Tomography Reconstruction from Sparse Views Using Implicit Neural Representation](https://arxiv.org/abs/2610.11547)

**<font color=#1a73e8>作者：</font>** Thomas Welsch, Min-Hsin Tu, David J. Chapman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> NeRF and Gaussian splatting methods have been successfully applied on X-ray scenes where the views are too sparse for 3D reconstruction via classical methods. Ultra-sparse scenes with 10 or fewer views such as those with high-rate or low-dose acquisition still, however, present a significant challenge. To address this problem we present a new framework, Optimised X-ray Neural Radiance Fields (OX-NeRF), that combines cross-scene feature learning with scene-specific optimisation to reconstruct sets of related scenes. OX-NeRF employs a convolutional neural network (CNN) to identify cross-scene features while maintaining scene-specific multi-resolution hash grids of spatial features. The paired representations are fused and passed to a multilayer perceptron (MLP); the CNN, hash grids and MLP are then jointly optimised end-to-end. Benchmarking on parallel-beam and cone-beam X-ray datasets shows OX-NeRF provides significantly higher reconstruction accuracy on ultra-sparse scenes compared to existing radiance field methods.

---


### 179. [$C_4$-Equivariant Flow Matching on Anisotropic Power-Diagram Graphs for Microstructure Generation](https://arxiv.org/abs/2610.11549)

**<font color=#1a73e8>作者：</font>** Dawid Lipinski, Jixiang Qing, Henry Moss  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Acquiring realistic microstructure data through Electron Backscatter Diffraction (EBSD) is costly and time consuming, often relying on specialised equipment. As microstructures strongly influence material properties, generating realistic samples is essential for modelling the behaviour of polycrystalline materials. We introduce a generative model for synthesising realistic polycrystalline microstructures using flow matching and graph neural networks. By representing microstructures as anisotropic power diagrams, our model learns a compact geometric parametrisation and can render generated samples at arbitrary pixel resolution. A $C_4$-equivariant architecture incorporates rotational symmetry directly into the model, ensuring that rotations of the input noise produce corresponding rotations of the generated microstructure. We also demonstrate how training-free guidance can be used to generate complex microstructures, based on user defined objective function. In particular, we generate microstructures resembling a copper weld, cast metal slab, 3D-printed stainless steel and heterogeneous lamella titanium.

---


### 180. [New Lower Bound and Upper Bounds on the Regret for Online Sparse Linear Regression](https://arxiv.org/abs/2610.11551)

**<font color=#1a73e8>作者：</font>** Xiaofeng Cao, Junfan Li, Langzhang Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online sparse linear regression (OSLR) where any algorithm is restricted to accessing only $b$ out of $d$ attributes per instance for prediction and $b_0\geq 0$ additional attributes after prediction, which was proved to be NP-hard. Previous work focused on designing computationally efficient algorithms under regularity assumptions, but did not characterize its information theoretic complexity. In this work, we give the first lower bound on the minimax regret of OSLR and design algorithms with better upper bounds without regularity assumptions. We characterize how minimax regret scales with problem-dependent parameters, capturing the information theoretic complexity of OSLR.

---


### 181. [Best of Both Worlds in Federated LSA: Speedup When Possible, Personalization Always](https://arxiv.org/abs/2610.11555)

**<font color=#1a73e8>作者：</font>** Safwan Labbi, Paul Mangold, Eric Moulines  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study personalized federated linear stochastic approximation (LSA), a framework which notably encompass personalized temporal difference learning. In this setting, heterogeneous agents collaborate to solve distinct linear fixed-point equations, each corresponding to an agent-specific learning problem. A central open question in personalized learning is whether a single method can adapt to an unknown level of heterogeneity by converging to each agent's personalized solution in all regimes while achieving a linear speedup in the number of agents when their learning problems are sufficiently similar. We answer this question affirmatively by introducing PF-LSA, a minimalist algorithm that mixes each agent's local stochastic update with the average update across agents, at no additional computational cost relative to standard federated methods. We prove that PF-LSA, achieves best-of-both-worlds guarantees without any prior knowledge on the level of heterogeneity. Our analysis is based on a sharp decomposition of the error into consensus and disagreement components. The consensus error decays rapidly, whereas the disagreement error decays more slowly but becomes negligible in low-heterogeneity regimes.

---


### 182. [Hankel Subspace Self-Supervised Learning for Parallel MRI Reconstruction](https://arxiv.org/abs/2610.11560)

**<font color=#1a73e8>作者：</font>** Mingyu Hu, Siquan Zhu, Xijun Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parallel magnetic resonance imaging reconstruction is an ill-posed inverse problem under undersampling. Multi-coil acquisition and Hankel lifting expose complementary repeated information: observations of the same anatomy across coils and repeated local k-space neighborhoods in overlapping windows. These dependencies guide recovery of missing k-space data. However, splitting lifted Hankel entries for self-supervision can place the original sample in both input and target, causing data leakage. We propose Hankel Subspace Self-Supervised Reconstruction (HSSRecon), a scan-specific reconstruction framework for parallel magnetic resonance imaging. HSSRecon partitions data by physical acquisition units before Hankel lifting and applies multiplicity normalization to repeated Hankel copies in overlapping windows. Rather than learning a mapping that directly predicts missing data, the network learns a compact complex-valued Hankel subspace operator. Reconstruction is performed over the original k-space variables using a conjugategradient solver with hard data consistency. This design separates structural learning in the Hankel domain from data consistency in the physical domain: the former exploits multi-coil and local Hankel correlations, while the latter solves over unacquired degrees of freedom. We provide theoretical analyses of physicalgroup splitting and multiplicity normalization, and establish positive definiteness, uniqueness, hard data consistency, and a finite-step conjugate-gradient error bound for the system. On fastMRI brain data with three contrasts and three sampling masks, HSSRecon achieves competitive peak signal-to-noise ratio, structural similarity, and normalized mean squared error across six aggregated conditions.

---


### 183. [Incremental Open-Ended Deep Research with Structured Harness](https://arxiv.org/abs/2610.11566)

**<font color=#1a73e8>作者：</font>** Meilin Chen, Hongyuan Bao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing Open-Ended Deep Research (OEDR) systems primarily generate reports from scratch, making them inefficient for scenarios where research reports need to be continuously maintained as new information emerges. We introduce \textbf{Incremental Open-Ended Deep Research (Incremental-OEDR)}, a research setting that treats a report as an evolving research state and incrementally updates it by preserving valid knowledge, revising outdated or incomplete content, and incorporating newly available information. To support this setting, we propose \textbf{Structured Harness}, which represents reports as structured collections of outlines, sections, and supporting evidence, and provides structured retrieval, a persistent structured evidence pool, and structured generation for selective report updating and evidence reuse. We further establish a temporal evaluation framework spanning ten years, with \emph{Single-Step Task} and \emph{Long-Chain Task} to evaluate incremental updates over both individual transitions and long-term update chains. Extensive Experiments on DeepResearch Bench and DeepConsult under both the Open-source Configuration (OC) and Proprietary Configuration (PC) show that Incremental-OEDR maintains competitive report quality while substantially improving report continuity and reducing research costs. As shown in Figure~\ref{fig:profile}, it achieves up to 0.51 higher content-level ROUGE-L F1, 0.63 higher outline-level EM F1, 33\% lower token consumption, and 61\% fewer search calls than OEDR on DeepResearch Bench. For more details, please refer to our project page: this https URL.

---


### 184. [Scaling to Tens of Thousands of Test-Time Iterations with Loop-Native Attention Residuals](https://arxiv.org/abs/2610.11570)

**<font color=#1a73e8>作者：</font>** Pengxiang Li, Dilxat Muhtar, Di He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we argue that looped Transformers need their own residual connections to prevent performance degradation as the number of iterations grows. We observe that increasing loop iterations can reduce reasoning accuracy: noisy state updates overwrite correct intermediate deductions and even undo completed solutions. This leaves subsequent iterations to recover lost information from an already degraded representation: once an error arises in an earlier loop, often as a result of long-range propagation through the recurrence, later loops find it difficult to correct. In this paper, we introduce InfiLoop, a loop-native residual connection that learns which past computations to retain and how much to accept from each new update. InfiLoop combines content-based weighting with learned temporal decay to maintain a running summary of recurrent states. An exact streaming recurrence keeps its persistent aggregation memory constant as the loop count grows. The resulting adaptive update suppresses unreliable proposals and preserves useful intermediate states. Across extensive reasoning tasks, a 7M-parameter InfiLoop model outperforms existing recursive architectures, reaching 97.9% exact accuracy on Sudoku-Extreme, and 13.6% pass@2 on ARC-AGI-2. Notably, on Sudoku-Extreme, InfiLoop continues to improve with test-time looping beyond 20,000 effective steps, showing that added depth translates directly into stronger reasoning. Our code is available at this https URL.

---


### 185. [PAM-ToD: Plug-and-Play Appearance Modeling for Cross-Time-of-Day 3D Gaussian Splatting](https://arxiv.org/abs/2610.11572)

**<font color=#1a73e8>作者：</font>** Kota Shimomura, Sungho Moon, Tsubasa Hirakawa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting a pre-trained 3D Gaussian Splatting (3DGS) road scene to a new time of day requires learning appearance changes from a few anchor images while preserving consistent, real-time rendering. We propose PAM-ToD, a lightweight plug-in that learns color corrections while keeping the pre-trained 3DGS parameters fixed. PAM-ToD scales each Gaussian's existing color to model illumination changes and uses an additive term for additional brightness, such as when street lamps turn on at night. Under a simplified image formation model, unchanged surface albedo can be eliminated from the relation between source and target appearances, allowing us to learn these corrections without separately estimating albedo and illumination. The model corrects colors across the scene while allowing the corrections to vary by location and by Gaussian. To guide learning from a few anchor images, it discourages abrupt spatial changes in these corrections. We also introduce CARLA-ToD, a benchmark with matching geometry, camera poses, and moving-object trajectories across three times of day. A few target-time anchor images are used to train each plug-in, while separate views are used for evaluation. Across the static and dynamic settings, PAM-ToD achieves higher PSNR and lower LPIPS than the baselines, even when the anchor images come from a single synchronized capture across multiple cameras.

---


### 186. [SV-TAD: Native Sparse Convs for Efficient Temporal Action Detection](https://arxiv.org/abs/2610.11579)

**<font color=#1a73e8>作者：</font>** Ricardo Pizarro, Roberto Valle, José M. Buenaposada 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To adapt billion-parameter Vision Transformers for long-video understanding, recent methods freeze the backbone and train lightweight convolutional modules. While effective for parameter-efficient training, existing adapters do not reduce inference-time computation, leaving scalability with respect to video length largely unaddressed. Token selection can reduce attention cost by pruning redundant tokens, but it breaks the spatial grid structure required by convolutional adapters. This forces an expensive dense reconstruction, nullifying much of the potential speedup. We address this by introducing native sparse 2D convolutions, a primitive that allows these adapters, for the first time, to operate directly and efficiently on dynamically pruned token sets. We integrate this primitive into SV-TAD, an adapter framework for temporal action detection, reducing VideoMAEv2-L computation by up to 64% and achieving 2.2x faster inference, while maintaining state-of-the-art accuracy on THUMOS-14 and ActivityNet-1.3. When scaled to InternVideoNext-L, our approach surpasses the previous state of the art at roughly half its computational cost. Moreover, the sparse formulation naturally supports auxiliary task tokens, which improves fine-grained assembly detection on ATTACH.

---


### 187. [Uncertainty-Aware Optimization for Physics-Aware Highway Trajectory Prediction](https://arxiv.org/abs/2610.11580)

**<font color=#1a73e8>作者：</font>** Aanchal Rajesh Chugh, Sebastian Dorn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate trajectory forecasting and well-defined predictive uncertainty are crucial for reliable, safety-critical applications such as autonomous driving. Most trajectory prediction approaches provide point estimates only, while uncertainty-aware approaches typically quantify uncertainty only in the trajectory space. In physics-aware approaches, uncertainty in the predicted motion variables should be explicitly modeled and propagated through the vehicle dynamics. Otherwise, the resulting trajectory-space uncertainty may not fully reflect the variability introduced by the underlying motion prediction. Therefore, in this work, uncertainty-aware extensions of X-TRACK (X-TRACK-DE and X-TRACK-MCD), a physics-aware trajectory prediction framework, are proposed. The proposed framework predicts future vehicle motion variables and models both aleatoric and epistemic uncertainties by propagating motion space uncertainty to trajectory space. Additionally, conformal prediction is applied to the trajectory space predictive covariance to construct uncertainty regions targeting a desired marginal coverage level. Evaluation on the highD dataset shows that X-TRACK-DE improves trajectory prediction accuracy over the deterministic baseline, while both uncertainty-aware variants provide predictive uncertainty that can be conformally calibrated to the desired marginal coverage level.

---


### 188. [S$^3$Geo: Structure-Semantic Synergistic Learning for Cross-View Geo-Localization](https://arxiv.org/abs/2610.11608)

**<font color=#1a73e8>作者：</font>** Ziqian Mo, Hill Zhang, Haosheng Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view geo-localization (CVGL) aims to estimate geographic locations by matching images captured from different viewpoints, such as drone and satellite views. Existing methods mainly rely on visual representations, but often fail to jointly model fine-grained structural correspondences and semantic priors, making them prone to confusion between visually similar but semantically different regions, and thus limiting robustness under large viewpoint variations. To address these challenges, we propose \textbf{S$^3$Geo}, a structure-semantic synergistic learning framework for cross-view matching. Specifically, we first introduce a Decoupled Query Pooling (DQP) module to extract a compact set of region-aware features from dense tokens, enabling explicit modeling of local structural patterns. We then design a query-level contrastive learning scheme with an optimal transport (OT)-based formulation to establish soft correspondences under cross-view spatial misalignment. Furthermore, we incorporate a Semantic Knowledge Distillation (SKD) strategy from a frozen CLIP teacher to transfer semantic priors and relational structures, thereby improving discrimination on hard negatives. By operating synergistically, the semantic priors provide robust contextual filtering, which guides the structural module to establish precise spatial alignments. Experiments on the University-1652 and SUES-200 datasets demonstrate that \textbf{S$^3$Geo} consistently outperforms state-of-the-art approaches without increasing inference complexity, validating the effectiveness of jointly modeling structural and semantic information for CVGL.

---


### 189. [PointVGGT: Zero-Shot Multiview RGB-D Point Cloud Registration with Visual Geometry Foundation Priors](https://arxiv.org/abs/2610.11612)

**<font color=#1a73e8>作者：</font>** Haobo Jiang, Liang Yu, Jianmin Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses multiview RGB-D point cloud registration, aiming to estimate global rigid poses for unordered RGB-D scans and align them in a metrically consistent coordinate frame. The conventional pairwise-then-global paradigm suffers from locally optimized pairwise registration, severe error propagation and high computational burden. In particular, existing methods typically treat RGB data as a mere auxiliary matching cue and overlook the holistic geometric priors (e.g., camera poses and 3D models) encoded across image sequences. This paper introduces PointVGGT, a zero-shot framework built upon a novel \emph{foundation-then-refinement} paradigm that systematically leverages visual geometry foundation models (e.g., VGGT) as the computational backbone for robust, training-free multiview RGB-D registration. In the foundation stage, we directly recover metrically consistent global poses (without any pairwise estimation) by grounding the scale-ambiguous pose predictions of the foundation model against metric depth observations. In the refinement stage, we introduce an efficient voxelized spatial hashing mechanism that exploits the globally coherent 3D reconstruction (induced by the foundation model) as a shared spatial anchor, enabling dense multiview correspondences in near-linear time. On top of this, an IRLS-based robust motion-only bundle adjustment is performed using a conjugate gradient solver to jointly minimize the correspondence and reprojection residuals for multiview pose refinement. Extensive experiments on indoor/object-centric/outdoor datasets verify the outstanding zero-shot registration accuracy and computational efficiency of our proposed method.

---


### 190. [AgentEvolver: System-Wide Self-Evolution Through Task Execution](https://arxiv.org/abs/2610.11613)

**<font color=#1a73e8>作者：</font>** Wentao Zhang, Fuchao Yang, Yilei Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent can complete a task without improving how it works. Turning task experience into reusable capability requires connecting the changed component to its evaluation and subsequent use. We present AgentEvolver, a system for developing capabilities during task execution while keeping the foundation model fixed. Eight entity families expose reusable operations, methods, agents, control flow, interfaces, and supporting state to revision through a common versioned lifecycle. A shared Runtime coordinates ongoing work, while persistent planning and recoverable context preserve task direction and supporting evidence. We evaluate task outcomes on SWE-bench Pro Public and examine capability changes in six application cases. The team reports an 82.08\% resolution rate with evolution, exceeding its reported baseline without evolution. The cases show retained capabilities entering later website, game, and research work, while also documenting incomplete objectives and an unsuccessful strategy. These findings distinguish improvement in a reusable component from success on the final task. AgentEvolver provides a concrete basis for studying capability accumulation through execution; independent-task transfer and total development cost remain open questions.

---


### 191. [TAM: Task-Aware Memory Distillation for Efficient Spatiotemporal Prediction](https://arxiv.org/abs/2610.11617)

**<font color=#1a73e8>作者：</font>** Yuqi Li, Xiaoqin Feng, Fan Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation enables efficient spatiotemporal prediction by transferring knowledge from an accurate teacher to a compact student. However, matching outputs or features independently for each sample leaves cross-sample predictive structure underused. Exploiting this structure requires representations and historical references that reflect the dynamics of each task. We propose TAM, a Task-Aware Memory Distillation framework that organizes a frozen teacher's knowledge into a bounded, retrievable history. Memory entries encode latent features, forecast changes, or flow residuals, while task-specific selection rules identify relevant historical references. The student either matches the teacher's similarity distribution over shared references or regresses observation-conditioned residual prototypes. These objectives complement supervised prediction and conventional distillation. The teacher, memory, and auxiliary adapters are used only during training, leaving student inference unchanged. We evaluate TAM on video prediction, weather forecasting, and traffic flow prediction across multiple teacher-student configurations. Averaged over four paired runs, adding TAM improves SSIM on all six video datasets and reduces MSE on five relative to the corresponding KD baselines. Mean paired MSE reductions reach 1.86% on KittiCaltech, 1.93% on WeatherBench with a gSTA teacher, and 1.01% on TaxiBJ. These results demonstrate the utility of historical teacher supervision across distinct forecasting tasks without additional student inference cost.

---


### 192. [Constructing Structured Decision Sources for Consensus-Based Pseudo-Label Learning](https://arxiv.org/abs/2610.11621)

**<font color=#1a73e8>作者：</font>** Long Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Consensus can make pseudo-label learning more reliable, but only when its predictors contribute genuinely different evidence. Multiple models that repeat the same boundary provide additional votes without additional information. We address this problem by con structing decision sources through controlled changes to within-class structure. Starting from a shared graph representation, we vary center granularity and neighborhood mixing, reproduce each resulting source to test its stability, and select a complementary subset using node pair coassignment. Unanimous predictions from the selected sources are then ranked for student training. On the public fixed splits of Cora, CiteSeer, and PubMed, evaluated with five random seeds, the constructed sources improve fixed-budget training pseudo-label precision by 1.19 to 4.39 percentage points over three conventionally initialized GCN sources. Under matched structural filters, three-source consensus is more precise than each constituent source in all 45 dataset slot eed comparisons. The gains are strongest in pseudo-label quality: downstream accuracy remains competitive but does not lead on every dataset. These results identify source construction rather than model count alone as an important design problem for consensus-based pseudo-label learning.

---


### 193. [Beyond Action Entropy: Quotient-Space Exploration for Genome-Scale Metabolic Model Repair](https://arxiv.org/abs/2610.11627)

**<font color=#1a73e8>作者：</font>** Xuan Gong, Hanbo Huang, Wenbin Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Repairing scientific models from functional observations differs fundamentally from supervised prediction: feedback may certify a solution without revealing which structural correction is responsible. We study this setting for genome-scale metabolic model (GEM) repair, where multiple reaction edits can explain the same phenotypes and many apparently distinct edits correspond to the same biological mechanism. This many-to-one structure creates a hidden failure mode for conventional exploration: diversity in the output space need not translate into diversity of scientific hypotheses. We introduce QuotientPO, which collapses equivalent repairs into canonical mechanisms and optimizes exploration directly over the resulting quotient space. To make quotient exploration informative under finite rollouts, we derive a kernelized Rényi estimator that resolves graded crowding among distinct repair cores beyond coarse exact-match counts. On 2,212 held-out GEMs, QuotientPO improves Success@32 from 17.93% to 20.10% (+12.1% relative) while consistently increasing distinct successful-core discovery under the same sampling budget. These results establish quotient-space exploration as a principled approach to mechanism-level discovery under verifier-induced equivalence.

---


### 194. [UXBench Pro: Benchmarking Personalized User Experience in Multi-Turn Dialogue Interactions](https://arxiv.org/abs/2610.11638)

**<font color=#1a73e8>作者：</font>** Mengze Hong, Zeyang Lei, Wenbo Shang 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating user experience (UX) with automated computational methods has gained increasing attention, supported by empirical evidence from UXBench. However, binary preference prediction provides limited insight, while relying on a single user-agnostic reward model overlooks the inherent heterogeneity of users, whose expectations can differ substantially. In this paper, we present UXBench Pro, comprising 1{,}000 test instances derived from real user interactions across 12 task scenarios and 82 domains. Each instance is paired with a FACTORS user profile that characterizes the user through seven interpretable behavioral facets, differentiating user groups. To provide richer evaluation insights, we introduce a dual-perspective paradigm that combines a personalized User Reward Model (URM) for third-person judgment with Sim4Eval, a user simulator that enables multi-turn interactions and provides first-person evaluation across four cognitive state dimensions. To assess the reliability of these based evaluators, we further introduce two meta-benchmarks, URMBench and USimBench, that evaluate how faithfully they reproduce real human preferences and behaviors. Extensive experiments reveal seven key findings that highlight the importance of user modeling and multi-perspective evaluation, offering a fresh perspective on user-centric benchmarking and motivating personalized model optimization.

---


### 195. [Host Attack Graph for Botnet Propagation](https://arxiv.org/abs/2610.11640)

**<font color=#1a73e8>作者：</font>** Andrei Neagu, Mara-Cristina Sterian, Paul Irofti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Botnets represent the backbone of most modern cybersecurity attacks through which botmasters deploy distributed denial of service and advanced persistent threats against legitimate computer networks. In this paper we introduce the Host Attack Graph model and propose two botnet propagation strategies which we study across network topologies, target selection, and attack strategies together with their effectiveness in time. While strategy and botnet size are important for propagation, our study and simulations show that network topology and target selection should not be easily discarded. Implementation and benchmarks are available at this https URL.

---


### 196. [Revisiting Handcrafted Minutiae Detection: A Simple and Effective Open Source Baseline for Modern Fingerprint Workflows](https://arxiv.org/abs/2610.11641)

**<font color=#1a73e8>作者：</font>** Raffaele Cappelli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handcrafted minutiae detection algorithms remain fundamental to biometric science and forensic practice due to their full auditability, adherence to international standards, and operational independence from training datasets or GPU hardware. However, current open-source traditional baselines are severely outdated, relying almost exclusively on legacy C/C++ codebases that lack seamless integration with modern scientific software ecosystems. To bridge this gap, the present work introduces SBMEX (Skeleton-Based Minutiae EXtraction), a fast and deterministic minutiae detection method integrated into the open source \texttt{pyfing} package. SBMEX achieves high computational throughput by employing a dual Look-Up Table architecture that replaces runtime neighborhood scanning during Crossing Number computation and skeleton tracking. Additionally, it incorporates a continuous quality scoring framework driven by tracking path length, dual ridge-valley skeleton fusion, and spatial density decay. Rigorous evaluation on NIST SD302 datasets demonstrates that SBMEX delivers feature extraction accuracy comparable to or outperforming traditional open-source baselines without fine-tuning, while achieving a drastic reduction in minutiae detection latency relative to classical Crossing Number Python implementations.

---


### 197. [Phonologically Informed Tokenization for German Speech Recognition: A Cross-Domain Study](https://arxiv.org/abs/2610.11646)

**<font color=#1a73e8>作者：</font>** Christopher Witzl, Tobias Bocklet, Korbinian Riedhammer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> German is a morphologically rich language whose syllable structure is exceptionally well-predicted by the Knuth--Liang hyphenation algorithm. We ask whether phonologically informed tokenization can serve as a competitive target for end-to-end speech recognition. We compare three tokenizer families on the Omnilingual ASR wav2vec 2.0 backbone fine-tuned with CTC: the pretrained multilingual character inventory, a data-driven Byte-Pair Encoding (BPE) over orthography, and phonologically informed units from Pyphen syllabification and grapheme-to-phoneme conversion. Across 40 fine-tunes, we evaluate on three German test sets spanning orthogonal shifts: in-domain read speech, dialectal spontaneous speech, and standard-German spontaneous speech. In-domain, all phonologically informed tokenizers match BPE and the multilingual character baseline on both WER and CER. Under domain shift the picture splits along vocabulary size rather than the linguistic axis of variation: at small vocabularies, syllable-aware tokenization improves on dialectal speech, where phonetic surface forms vary but syllable structure is preserved, and stays ahead on spontaneous speech, where new word-forms violate vocabulary closure. A phoneme-level confusion analysis further shows that all tokenizers commit the same canonical function-word errors, indicating that the acoustic encoder, not the tokenizer, dominates the error topology. Our findings suggest that tokenizer choice may depend on the vocabulary budget as much as on the distribution shift expected at deployment rather than reducing to a single universal optimum.

---


### 198. [DisFace3DNet: Explainable Facial Attractiveness Prediction via 3D Component Disentanglement](https://arxiv.org/abs/2610.11656)

**<font color=#1a73e8>作者：</font>** Fenggui Rao, Yan Luximon, Jie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial attractiveness prediction usually assigns one overall rating, leaving the roles of shape, appearance, and viewing conditions implicit. We propose DisFace3DNet, which uses 3D component disentanglement to learn seven component reference scores from overall ratings with auxiliary weak semantic supervision, without human-labeled component targets. Designated 3D representations and image cues feed jointly learned routes for identity, skin, hair, light, background, expression, and pose. A constrained fit then combines five static and two signed dynamic scores into the overall rating, exposing each component's numerical contribution and supporting component-specific comparisons across images. On SCUT-FBP5500, DisFace3DNet achieves a Pearson correlation of $0.8904\pm0.0063$ (mean $\pm$ standard deviation across five folds) with average human ratings; its component terms reconstruct every held-out prediction to numerical precision. Skin, hair, and facial shape account for the largest component-wise prediction variation. Human evaluation supports the score directions for facial shape, skin, and hair; expression agreement is weaker. DisFace3DNet thus connects overall prediction to quantitative analysis of the facial and contextual cues entering each estimate.

---


### 199. [Lamarck's Driving School: Discovering Autonomous Driving Training Strategies through Evolutionary Competition](https://arxiv.org/abs/2610.11662)

**<font color=#1a73e8>作者：</font>** Yichun Ye, He Zhang, Ye Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous driving capabilities depend strongly on the distribution of scenarios encountered during training. Existing methods commonly construct or dynamically adapt training scenario distributions using surrogate criteria such as realism, difficulty, or risk. However, these predefined surrogates may misrepresent training value, leading to inefficient use of training resources. To address this limitation, we propose a Lamarckian evolutionary framework that replaces surrogate-based guidance with competition among candidate distributions. We formulate training strategy discovery as a multi-stage bilevel optimization problem and use Lamarckian evolution algorithm to approximate its solution. At the outer level, Darwinian crossover, mutation, and selection explore the scenario distribution space; at the inner level, policy learning acquires new capabilities, and Lamarckian inheritance transfers them to subsequent stages, allowing scenario distributions and policy capabilities to co-evolve. The resulting evolutionary trajectories reveal recurring stage-wise regularities among high-value distributions, characterized by capability accumulation through stage-wise challenge rotation. We further distill these regularities into a lightweight, reusable Lamarckian Training Strategy. Experiments show that, compared with the baseline, the complete framework reduces performance loss by up to 25.07%, while the lightweight strategy still achieves a 19.13% reduction. These results demonstrate that evolutionary competition can both discover effective training strategies and reveal reusable stage-wise patterns in how the value of training distributions changes with policy capability. Code is available on GitHub.

---


### 200. [Constrained Command-Conditioned Reinforcement Learning with Bandit Strategy Selection in Real-Time Strategy Games](https://arxiv.org/abs/2610.11663)

**<font color=#1a73e8>作者：</font>** Nick Leenders, Roy Lindelauf, Joost van Oijen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning agents reach strong performance in real-time strategy games but can be brittle against opponents outside their training distribution. Separating strategic command selection from learned unit control allows different strategies to be selected for different opponents while reusing the same execution policy. This requires an executor that can follow different commands and measurable criteria for assessing whether it does so. We introduce a constrained command-conditioned Proximal Policy Optimization (PPO) policy, the executor, for MicroRTS, a real-time strategy environment. Discrete commands specify strategic objectives and behavioral requirements for economy, army composition, military posture, and worker policy over multiple environment steps; the executor determines the unit-level actions used to fulfill them. A Thompson-sampling bandit acts as the strategist, selecting command tuples from an estimate of the opponent's strategy built from in-game observations rather than opponent identity. In a controlled comparison with a flat PPO baseline trained with the same architecture, budget, curriculum and self-play league, the strategist-executor system wins significantly more often against three of the four strongest opponents on a training map, including the two strongest held-out ones (0.55 to 0.97 and 0.01 to 0.34), with no significant difference against the others.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-329](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

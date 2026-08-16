# 📦 其他研究 | 2026年08月17日

> 本类共 **199** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-199**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-199**

---

### 151. [GeoCache: Training-Free Acceleration of Multi-View Texture Diffusion via Geometric Delta Transport](https://arxiv.org/abs/2608.13255)

**<font color=#1a73e8>作者：</font>** Haotang Li, Zhenyu Qi, Shaohan Henry Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometry-conditioned multi-view diffusion enables high-quality 3D texture generation, but its repeated per-view denoiser evaluations introduce substantial computational cost. Existing training-free accelerators primarily exploit temporal redundancy by reusing computation across denoising steps. In multi-view texturing, however, skipping a step also removes the cross-view interaction that continually aligns different observations of the same surface, leading to rapidly degraded consistency and fidelity. Our analysis identifies a complementary source of redundancy: although intermediate features remain view-specific, geometrically corresponding surface points exhibit transferable evolution in their predicted clean signals. Based on this observation, we introduce \gc{}, a training-free plugin that evaluates a rotating subset of anchor views and transports their geometry-aligned per-step $\xz$ updates to the remaining views. Periodic full-view computation controls accumulated error, while sampler-consistent reconstruction preserves the denoising trajectory. \gc{} requires neither retraining nor architectural modification and uses the position maps already available in geometry-conditioned texturing pipelines. Across Hunyuan3D-2.1, SyncMVD, and MVPainter, \gc{} achieves a stronger speed--fidelity trade-off than temporal caches and step reduction at operating points above $2\times$. On Hunyuan3D-2.1, it delivers a $2.21\times$ denoiser-loop speedup with an MV-LPIPS of 0.0293 and an MV-PSNR of 33.60 dB, providing the best fidelity among all tested methods above $2\times$. The same transferred configuration reaches the highest speedup and lowest FLOPs on SyncMVD, while \gc{} achieves the lowest FLOPs and best fidelity among the accelerated methods on MVPainter. These results establish cross-view geometry as an effective acceleration axis for multi-view texture diffusion.

---


### 152. [Novel Knowledge-Guided Generative Methods for Synthetic Transcriptomic Data](https://arxiv.org/abs/2608.13256)

**<font color=#1a73e8>作者：</font>** Francesca Pia Panaccione, Sofia Mongardi, Marco Masseroli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As biomedical research increasingly relies on data-intensive tools, the quality and utility of datasets are critical. Challenges such as imbalances, biases, and ethical or legal constraints often limit access to high-quality data. Synthetic data generation can help overcome these limitations. Here, we present a comparative analysis of generative models for transcriptomic data, investigating strategies to incorporate prior biological knowledge via gene graphs. This ensures that synthetic data capture real-world gene patterns, maintaining their usefulness for downstream tasks. In particular, we introduce and benchmark three variants of the Generative Adversarial Network. Among the alternatives, MK-TGAN - an innovative multi-kernel, Graph Neural Network-based model - stands out for its performance in terms of both the realism and utility of the generated data. Unlike other methods, MK-TGAN leverages prior knowledge graphs by exploiting graph neural networks. Our results show that prior knowledge integration strategies improve performance, and that MK-TGAN consistently produces synthetic samples with superior realism and biological plausibility.

---


### 153. [Virtual Temperature Sensors in Power Transformers Using Neural Ordinary Differential Equations](https://arxiv.org/abs/2608.13260)

**<font color=#1a73e8>作者：</font>** Berk Hadzhamolla, Alexander Johannes Stasik, Signe Riemer-Sørensen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate modeling and forecasting of power transformer thermal behavior are critical for reliability, asset lifetime, and optimized power system operation. Numerical approaches such as finite element methods (FEM) and computational fluid dynamics (CFD) offer high fidelity but are computationally expensive, require complex mesh generation, and are often impractical for real-time or large-scale applications, particularly when transformer geometries are unknown. Lumped-parameter thermal models are more practical but depend on transformer-specific thermal constants and may fail to capture dynamic responses under varying operating and environmental conditions. Purely data-driven machine learning methods, including artificial neural networks, convolutional neural networks, and long short-term memory (LSTM) networks, have shown success in forecasting transformer temperatures but typically require large volumes of high-quality training data and may produce physically inconsistent or uninterpretable results. This paper develops a physics-aware Neural Ordinary Differential Equation (Neural ODE) framework for forecasting transformer thermal behavior from real-world time-series data. Neural ODEs model system dynamics in continuous time, providing smooth trajectory prediction and a natural representation of continuously evolving thermal dynamics. A key contribution is the integration of simplified heat-transfer equations directly into the Neural ODE formulation. The model is evaluated across datasets from fifteen transformers in different regions of Norway with varying designs and cooling mechanisms. The results demonstrate that the developed Neural ODE framework provides a standardized, physics-aware, and robust forecasting approach for heterogeneous transformer units.

---


### 154. [Slow and Steady: Preventing MEV with Verifiable Delays](https://arxiv.org/abs/2608.13271)

**<font color=#1a73e8>作者：</font>** Zeta Avarikioti, Dimitris Karakostas, Karl Kreder 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Our work presents a defense mechanism against Maximal Extractable Value (MEV) opportunities in distributed ledgers. The mechanism relies on the idea of enforcing a verifiable delay when generating transactions, such that a block creator cannot react to the appearance of a MEV opportunity without breaking liveness. We present positive results both in the Byzantine setting and in a game theoretic model of rational participants. We additionally present negative bounds that outline the limitations of this line of defense. Finally, we explore real-world implementation details of verifiable delays and show that, based on historical MEV data, our mechanism could realistically help prevent most existing MEV threats.

---


### 155. [Sovereign by necessity? Frontier AI export controls, cyber security, and the limits of national AI capability](https://arxiv.org/abs/2608.13272)

**<font color=#1a73e8>作者：</font>** Alan Woodward, Andrew Rogoyski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A small number of firms based in two states produce the most capable frontier AI models. The governments of those states have shown both the legal power and the political will to decide which other countries may use these systems. In June 2026 the United States required a leading developer to obtain licences before releasing its most advanced models to any foreign person, including foreign nationals resident in the United States. The affected models were withdrawn worldwide at short notice, partly because the restriction proved impractical to administer. This followed within months of the first documented case of a largely autonomous, AI-run cyber espionage campaign, and coincided with mounting evidence that frontier models alter the economics of both cyber attack and cyber defence. This article examines how these two developments interact, and situates them within the unusual market dynamics now driving large-scale AI development. It argues that access to frontier AI is becoming part of national cyber defence, that such access can be revoked, and that the obvious remedy of sovereign capability remains only partly feasible for all but a handful of states. Drawing on evidence about training costs, the concentration of computing power and the support offered by national AI programmes, it asks what sovereignty can realistically mean for small and middle powers, and for large powers as well. The article proposes a layered strategy: negotiated access guarantees, sovereignty at the level of inference, hedging with open-weight models, pooled regional capability, sustained talent development and continued investment in basic cyber resilience. The open-weight hedge proves at once more capable and more politically exposed than is commonly assumed. Much of the near-term risk lies in how capable models are deployed and contained rather than in their apparent performance.

---


### 156. [Print&Fold: Printing and Folding Shape-accurate 3D Models](https://arxiv.org/abs/2608.13279)

**<font color=#1a73e8>作者：</font>** Archit Kumar, Zachary Grimm, Mingsheng Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper introduces Print&Fold, a tool to allow FDM 3D printing of complex models with less time and material while preserving shape accuracy. Key to this work is a folding algorithm that planarizes foldable faces internal to the 3D model. While folding techniques typically discretize a target model's surface, thereby fabricating low fidelity counterparts, our method preserves the surface features in the physical print. Our design tool allows users to unfold 3D models to be FDM-printed flat before manually folding these into their target shapes. We showcase a variety of applications and evaluate the material and time savings across a range of 3D models.

---


### 157. [Towards Context-Aware Clinical Motion Understanding in Daily Living at Home: Freezing of Gait Detection with Egocentric Vision](https://arxiv.org/abs/2608.13283)

**<font color=#1a73e8>作者：</font>** Vayalet Stefanova, Diwas Lamsal, Margot Genbrugge 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding motion in daily living requires context beyond kinematics, because similar inertial patterns during activities of daily living (ADLs) can reflect intentional stopping, object interaction, or pathological movement impairment. Egocentric vision provides task-related context that may help disambiguate these cases. We investigate this challenge through freezing of gait (FOG) detection in Parkinson's disease (PD), a symptom strongly influenced by contextual factors during ADLs. Using synchronized egocentric video, wearable IMUs, and expert-annotated FOG labels collected from 13 PD participants in their homes, we evaluate frozen representations from pretrained ego-video and time-series foundation models, alongside an IMU-based TCN trained from scratch, under leave-one-subject-out evaluation. The IMU-based TCN achieved the strongest event-detection performance, reaching 42.3 F1 and 83.0 AUROC, compared with 32.6 F1 and 77.2 AUROC for V-JEPA2 ego-video features. Although ego-video alone did not outperform IMU-based sensing, it showed above-chance discrimination, and qualitative analyses suggest that egocentric vision may capture FOG-relevant information independent of IMUs. Together, these results support the use of pretrained ego-video representations to add contextual information to wearable-sensor-based clinical motion understanding in daily living.

---


### 158. [EEG Decoding Using CNN and LSTM Network](https://arxiv.org/abs/2608.13285)

**<font color=#1a73e8>作者：</font>** Athanasios Karagounis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motor imagery (MI) brain--computer interfaces (BCIs) have emerged as a promising approach for establishing flexible communication pathways between the human brain and external devices , particularly for individuals affected by stroke or neurodegenerative disorders. Reliable decoding of motor-imagery electroencephalography (MI-EEG) remains challenging because EEG recordings contain substantial noise and exhibit complex, weakly informative relationships with the underlying brain activity. Although deep learning provides an effective means of learning representations directly from EEG signals, its application to MI-EEG feature learning remains comparatively limited. This study introduces a hybrid deep-learning architecture that integrates a convolutional neural network (CNN) with a bidirectional long short-term memory (bi-LSTM) network. The CNN is used to learn high-level spatial and temporal representations directly from raw MI-EEG recordings, whereas the bi-LSTM models temporal dependencies and relationships among the extracted features. The proposed approach is evaluated using both a publicly available dataset and a privately acquired dataset obtained with an EEG acquisition system. The experimental results indicate that the CNN\&bi-LSTM architecture provides robust performance for both two- and three-class motor-imagery classification and demonstrates promising subject-independent decoding capability across the evaluated methods.

---


### 159. [VR-Themis: A Scalable Framework for Virtual Reality Application Clone Detection](https://arxiv.org/abs/2608.13290)

**<font color=#1a73e8>作者：</font>** Gengyang Xu, Hanyang Guo, Hong-Ning Dai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Repackaging of mobile applications (aka app cloning) not only threatens the security and privacy of mobile users but also infringes upon the copyright of the original app developers. However, existing detection methods that primarily focus on mobile platforms (such as Android) fail to capture the essential features of virtual reality (VR). Consequently, they are inadequate for effectively detecting cloned VR apps, which have often been targeted by illegal users in the VR market. Considering the unique features of VR apps, this paper proposes a two-stage app clone detection framework, namely VR-Themis, based on \emph{Hierarchy-Object-Behaviour} (HOB). Firstly, VR-Themis exploits the coarse-grained stage to cluster apps based on their retrievable statistical features, making this tool scalable to large-scale VR app datasets. Then, in the fine-grained stage, VR-Themis performs in-depth analysis of the suspicious apps (identified in the first stage) by calculating similarity using our defined \emph{HOB metrics}. Our extensive experiments indicate that VR-Themis successfully detects 307 suspected clone apps from the collected 4,277 VR apps without false positives, demonstrating its effectiveness and scalability.

---


### 160. [NAS-Driven Hardware Accelerator Exploration for Edge AI and Quantization Effects on the Pareto Space](https://arxiv.org/abs/2608.13293)

**<font color=#1a73e8>作者：</font>** Eleftherios Mylonas, Angelos Kouprizas, Michael Birbas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Edge AI deployment demands neural architectures that are simultaneously accurate, computationally efficient, and hardware-deployable - a challenge addressed by hardware-aware Neural Architecture Search (NAS). While recent works incorporate quantization directly into the NAS loop, these approaches expand search complexity and tightly couple architecture and quantization design. The simpler post-search quantization strategy has received little analytical attention: the effects of Post-Training Quantization (PTQ) on the NAS-discovered Pareto structure remain uncharacterised, and no framework combines quantized architecture mapping onto reconfigurable accelerators with automated hardware exploration. This paper addresses both gaps. First, a three-stage pipeline is proposed: a hardware-agnostic Pareto rank surrogate frontend on NAS-Bench-201, a quantization bridge with Pareto-aware filtering and feedback control, and an evolutionary Domain Space Exploration (DSE) backend on CGRA4ML for optimal hardware mapping. Second, an empirical study characterises how INT4 PTQ perturbs the NAS-Bench-201 Pareto space through formal stability metrics on ground-truth data for all 15,625 architectures, and demonstrates that an FP32 zero-shot surrogate outperforms a dedicated INT4-trained surrogate in Pareto space coverage across two standard search strategies.

---


### 161. [More Than 63% of IEEE VIS Research Liable to be Retracted?! Ethics Approval Statements Protect Participants (and Researchers!)](https://arxiv.org/abs/2608.13295)

**<font color=#1a73e8>作者：</font>** Lonni Besançon, Tobias Isenberg  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We analyzed the ethics reporting in 255 IEEE VIS papers from 2024 and 2025, as published in TVCG. This analysis arose from our experience as readers and reviewers of IEEE VIS papers that such reporting is frequently incomplete or missing, as well as from investigations in which we ourselves had to answer challenges regarding ethics approval in our own work. Visualization research naturally often involves human participants, yet ethics approval and informed-consent procedures are not always explicitly reported. In our corpus, 189 papers (74.1%) reported on work involving human participants. Only 6 of them (3.2%) reported to have obtained ethics approval, an approval identifier, and having received informed consent from the participants, while 26 (13.8%) reported at least ethics approval and informed consent. These omissions do not imply that the empirical work was unethical or lacked approval. They rather show that current reporting practices make ethical approval difficult to assess. Beyond our alarming - yet true - paper title, we wish to raise awareness on how authors themselves may eventually be at risk for not properly reporting ethics. We argue that VIS should adopt clearer and more standardized ethics-reporting practices to protect participants, authors, reviewers, and editors.

---


### 162. [Large-scale Testing Global Optimization Methods with Black-box Adversarial Attacks](https://arxiv.org/abs/2608.13296)

**<font color=#1a73e8>作者：</font>** Wojciech Zarzecki, Jarosław Arabas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing global optimization benchmark suites are of a moderate size and are based on a small number of analytical functions that date back even to the 1970s. This causes a risk of biasing the development of global optimization methods. We argue that the tasks related to the black-box adversarial attack (BBAA) can serve as valuable global optimization benchmark in many-dimensional space. We demonstrate the efficiency of several types of evolutionary algorithms and other metaheuristics in solving example BBAA problems. Thus, we take a step towards convergence of global optimization methods to the challenges and needs that arise in the modern machine learning field.

---


### 163. [The Time Value of Evolution](https://arxiv.org/abs/2608.13297)

**<font color=#1a73e8>作者：</font>** Matthew Siper, Ahmed Khalifa, Julian Togelius  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In evolutionary search, a weak child can be a valuable ancestor that makes high-fitness regions reachable. Immediate-return control is blind to this delayed utility, penalizing mutations through their immediate offspring even when they open productive future lineages. We formalize this hidden dynamic as the time value of evolution within a finite-horizon Markov decision process. To exploit it, we introduce Lineage-Value Policy Gradients (LVPG), a long-horizon actor-critic framework for automated trading policy discovery. Our architecture decouples search control into specialized policy heads over a shared generative backbone: a bootstrapped critic head estimates the value of finite-horizon lineage potential from multi-step mutation trees, while an actor head dynamically modulates mutation intensity over the remaining search budget. We isolate the impact of long-horizon credit assignment against immediate-return optimization across 90 paired runs under matched operators, lineage supervision, folds, seeds, and budgets. Path-based credit assignment substantially accelerates finite-budget search, increasing validation best-so-far AUC by 0.394 Sharpe units. LVPG also produces fewer temporary regressions than immediate-return optimization and recovers from them more often. Finite-horizon lineage value yields more selective non-monotonic search and stronger policies within identical resource constraints.

---


### 164. [A Probe Direction Is a Property of Its Prompt](https://arxiv.org/abs/2608.13329)

**<font color=#1a73e8>作者：</font>** Valentin Noël  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A model that behaves differently when it senses it is being tested would undermine the evaluations we rely on, so recent work has sought to read that sense directly from a model's activations. The standard instrument contrasts activations on prompts that announce an evaluation against prompts that do not, and reports how well the resulting direction separates held-out cases. That number is then compared across models and correlated with scale. We observe that the instrument has a free parameter its readings do not disclose: "a prompt that announces an evaluation" is not a prompt but a choice among many, and nothing in the method fixes which. Holding the task text fixed and varying only that choice, we find that the reported score, and even the direction in which it trends with model size, follows the prompt rather than the model; two published studies that disagree about the sign of that trend are both reproducible from a single design, by choice of prompt alone. Treating the prompt as a facet of a measurement design rather than an implementation detail, we find the model under study accounts for a small share of the variance in the number reported about it, and most of the rest lies in how each model responds to each prompt: collecting more evaluation items cannot repair the measurement, while varying prompts can. A further check finds that the split these probes are scored on is largely separable from surface form alone, so a direction carrying no information about evaluation at all still reproduces a substantial fraction of each published score. We conclude that a single-prompt design cannot support comparison between models, and we give the number of prompts a defensible comparison requires.

---


### 165. [Neural Quadratic Forms: A Unified Minimal Model for Sudden Learning and Scaling Laws](https://arxiv.org/abs/2608.13335)

**<font color=#1a73e8>作者：</font>** Liu Ziyin, Yizhou Xu, Tomaso Poggio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks trained by gradient descent on a smooth cost function can nevertheless learn in steps: the cost holds on long plateaus and then drops abruptly. Meanwhile, training losses instead follow smooth power laws. Variants of both behaviors occur in architectures with very different microscopic structures, which is the signature of a few relevant collective variables. We show that a symmetry fixes what those variables are: a network layer is a sum over interchangeable units, so relabeling the units leaves it unchanged; given smoothness and the condition that a unit's gradient vanish at the origin, symmetry then enforces a universal leading form for the expansion about the near-zero weights present at the start of training, the quadratic $\Tr[WW^{\top}A(x)]$, in which every architectural detail is confined to a single ``structure matrix" $A(x)$ that we compute for each architecture. Perceptrons, attention layers, mixtures of experts, and convolutions become one model at different $A$. Its training dynamics then close on the ``order parameter" $M=WW^{\top}$ and, whenever the data matrices share an eigenbasis, reduce to a Lotka--Volterra equation whose modes switch on one after another. The smaller the initial weights, the further apart the switch-on times, and the plateaus appear as a singular limit of a smooth flow; when many modes are unresolved the same events merge into a power law in training time whose exponent the theory predicts. We confirm both numerically across training methods and architectures.

---


### 166. [Simulation-to-real transfer learning for infrared spectroscopic chemical sensing and analysis from molecules to complex samples](https://arxiv.org/abs/2608.13341)

**<font color=#1a73e8>作者：</font>** Yusen Tan, Yixuan Chen, Zheng Fang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Infrared (IR) spectroscopy is widely used for chemical sensing, but extracting reliable chemical information from spectra remains challenging. Conventional interpretation is labor-intensive, relies on prior knowledge and reference spectra, and is difficult to scale, whereas most machine-learning methods are tailored to individual tasks or datasets, require large labeled training sets, and transfer poorly across analytical objectives and experimental datasets. Here we introduce UltraIR, a foundation model for IR spectroscopy with more than 100 million parameters that enables simulation-to-real transfer learning for chemical sensing and analysis from molecules to complex samples. UltraIR is pretrained on approximately 60 million simulated IR spectra using spectral reconstruction, molecular fingerprint similarity alignment, and functional-group prediction, then adapted to downstream objectives with task-specific labels or targets. Across functional-group prediction, molecular structure elucidation, physicochemical property prediction, mixture-component identification and quantification, bacterial classification, medicinal-herb geographic origin traceability and constituent quantification, microplastics classification, and soil property prediction, UltraIR outperforms conventional machine-learning and task-specific deep-learning baselines. It performs strongly with limited labeled experimental spectra and in zero-shot inference for the same analytical task across Fourier-transform infrared spectrometers and laboratories, providing a route to adaptable, data-efficient chemical sensing from complex real-world samples.

---


### 167. [When Local Variance Optimality Is Not Enough: RoPE-Aligned Q/K Rotations for Dynamic 4-Bit Quantisation](https://arxiv.org/abs/2608.13365)

**<font color=#1a73e8>作者：</font>** Shuhan Wang, Yilin Luo, Nan Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rotation-based post-training quantisation commonly applies an orthogonal transform across an entire attention head to reduce outlier-induced error. RoPE instead partitions each head into two-dimensional frequency pairs, raising the question of whether a transform respecting this decomposition can improve on full-head mixing. Prior work has established the per-pair rotations that commute with RoPE. We state the converse result that, for distinct frequencies, no other single-head orthogonal map commutes with RoPE. For the head-shared parameterisation used in our experiments, we then derive the rotation angle that minimises the larger channel variance under a pooled-covariance, position-averaged surrogate and verify that the implementation attains its analytic minimum. The evaluated head-shared pairwise configuration does not improve accuracy in the tested dynamic W4A4KV4 setting. Across four checkpoints, replacing the full-head Hadamard with this configuration increases perplexity at both short and long context lengths. Composing the pairwise rotation with the Hadamard satisfies the selected $\pm0.05$-PPL interval criterion under the default estimator. Estimating the shared angle from K alone improves pairwise-only on every checkpoint but does not close its gap to full-head mixing. The analytic objective controls a position-averaged second moment of a pooled calibration covariance, whereas the dynamic quantiser sets its step from a tokenwise group range. The pairwise transform also has only two-channel mixing support. Along a controlled interpolation from two-channel to full-head mixing, K range, relative quantisation error, and perplexity degradation decrease as support increases. These results show that optimality for a structured surrogate need not reduce quantisation error when the surrogate and mixing support are misaligned with the quantiser's scale-setting statistic.

---


### 168. [Sign Language Video Synthesis via Loss-Guided Multi-Expert GANs](https://arxiv.org/abs/2608.13368)

**<font color=#1a73e8>作者：</font>** Dingzhan Nong, Zhihao Ren, Ziqi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This preliminary technical report presents a framework for sign language video synthesis using a loss-guided multi-expert Generative Adversarial Network (GAN) to enhance communication for individuals with hearing impairments. Three specialized discriminators -- global, hand, and head -- each guide a corresponding expert branch in the generator toward a distinct visual region, enabling implicit feature specialization without explicit diversity losses. To stabilize this multi-discriminator system, whose early-phase training otherwise exhibits chaotic dynamics, we introduce a United Loss consensus mechanism that regularizes each discriminator toward the ensemble average at a 10% weight. Each branch further adopts a dual-pathway convolutional-transformer design with learnable AdaptiveFeatureFusion, balancing the stability of convolutions against the detail of windowed self-attention. The generator is trained using an alternating three-mode schedule (discriminator, holistic generation, branch-specialized generation). On a custom 156GB dataset with a filtered test set that removes easy and repetitive samples, our 0.2B-parameter variant achieves 29.8 PSNR and the 1.3B-parameter variant achieves 30.7 PSNR, with inference VRAM footprints of 1.5 GB and 8 GB respectively, enabling deployment on consumer-grade hardware. Full ablation studies remain ongoing due to the 2-3 month training cycle on a single GPU. The system was showcased at the 2025 Hong Kong Frontier Technology Summit.

---


### 169. [Reconstructing Historical Manuscripts through MSI: The Potential of Contrast in Assessing Image Quality and Legibility](https://arxiv.org/abs/2608.13381)

**<font color=#1a73e8>作者：</font>** Anna Breger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital restoration of historical manuscript images aims to improve readability while preserving the authenticity of cultural heritage documents. However, evaluating quality of restored manuscripts remains challenging, where readability is often subjective and expert annotations are scarce. This study investigates the suitability of contrast-based image quality measures to assess quality and legibility of reconstructed manuscript images from multi-spectral imaging. Two experiments were conducted with publicly-available data sets, facilitating manual quality scores by experts and full-reference image quality measures as reference evaluations. The results show that potential contrast achieves the highest correlation with expert ratings, while contrast-to-noise ratio demonstrates the strongest agreement with full-reference quality measures. Overall, contrast-based measures consistently outperform general image quality measures, demonstrating their potential as objective indicators of manuscript legibility and reconstruction quality.

---


### 170. [TopoIntent: Compiling Security Intent into Executable, Compliance-Checked Network Topologies](https://arxiv.org/abs/2608.13389)

**<font color=#1a73e8>作者：</font>** Xiaokang Qu, Jianliang Ma, Zao Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise security topology design requires translating business intent, regulatory requirements, and risk assumptions into zones, boundary devices, inter-zone paths, and access-control policies. Existing NetOps automation tools mainly operate after this design is fixed, providing limited support for generating structured security topologies from underspecified natural-language requirements. We present TopoIntent, a system that compiles security intent into executable, compliance-checked network topologies. It uses a schema contract to constrain generation, retrieves reference architectures from a curated template library via dense-vector search, and applies staged fusion for intent-template alignment and security completion. The generated topology is checked against CIS Controls v8.1.2 safeguards visible at the topology layer, while unresolved cases are marked for manual review. Structural gaps are repaired through additive schema-preserving edits. The final topology is exported to Mininet scripts with kernel-level iptables ACLs, enabling executable reachability and allow/deny tests. Because no public benchmark exists for this requirement-to-topology task, we construct an evaluation set from reference security architecture diagrams. The retrieval set contains 22 templates and 44 synthetic intents across five scenarios, while the held-out set contains 7 templates and 14 intents from finance and government scenarios excluded from retrieval. On the held-out set, additive repair improves topology-visible CIS satisfaction from 0.78 to 1.00 in fewer than 1.5 rounds on average, and one feedback round raises the post-ACL policy pass rate from 0.78 to 0.88.

---


### 171. [TeleGapper: On the (un)reliability of Privacy Policies in Telegram Mini apps](https://arxiv.org/abs/2608.13390)

**<font color=#1a73e8>作者：</font>** Luca Ferrari, Mariano Ceccato, Luca Verderame  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Telegram Mini Apps are Web applications embedded within the Telegram client, forming an ecosystem of third-party services within one of the world's most widely used messaging platforms. Despite their growing adoption and access to Telegram-provided context, their privacy properties remain largely unexplored. Unlike ecosystems such as WeChat, which rely on tightly controlled, proprietary execution frameworks, Telegram adopts a different model: Mini Apps run inside a WebView, combining platform-provided context with standard Web capabilities and unrestricted outbound networking. This enables applications to transmit sensitive information to analytics, advertising, tracking, or other third parties through ordinary Web requests, often with limited visibility.
Privacy disclosures are therefore critical for transparency. Telegram allows Mini Apps either to define an application-specific privacy policy or to rely on a platform-provided default policy. While the latter reduces the developer's disclosure burden, it may lead to generic statements that do not accurately capture actual data practices of individual Mini Apps.
In this paper, we present TeleGapper, a black-box dynamic analysis framework to assess the privacy posture of Mini Apps by capturing runtime network traffic, identifying third-party communications, and comparing observed data flows against disclosed privacy information. We evaluate 278 working Mini Apps collected from tApps Center, a community-driven catalogue for discovering third-party applications in Telegram. We find that 59.4% contact at least one undisclosed third party, 78.8% rely exclusively on Telegram's default privacy policy, and none provides a consent or opt-out mechanism. These findings expose a substantial transparency and compliance gap in a widely used yet understudied ecosystem.

---


### 172. [Context-Matched Distillation: Teacher Causality for Autoregressive Video Distillation](https://arxiv.org/abs/2608.13391)

**<font color=#1a73e8>作者：</font>** Hmrishav Bandyopadhyay, Xuanchi Ren, Zijian Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive autoregressive video generation demands both low-latency rollouts and precise online control. Few-step distillation accelerates generation by reducing denoising steps, while online control imposes a causal constraint: frames and blocks should depend on history and controls available during generation. Existing video distribution matching distillation (DMD) pipelines, however, often supervise causal few-step students using bidirectional teachers that score complete clips. The score for a target can therefore depend on future frames and controls that were unavailable when the student generated it, misaligning teacher supervision with the student's causal information set. We introduce Context-Matched Distillation (CMD), a causal DMD framework that aligns teacher supervision with the information available when each target is generated. CMD replaces bidirectional full-clip scoring with a causal teacher that evaluates each target without access to future frames or controls. The same causal teacher initializes the few-step student, establishing a consistent causal formulation across teacher training, student distillation, and inference. Beyond aligning the temporal information boundary, Prefix Scoring matches supervision to the student's realized rollout context by evaluating each target under the cached student-generated prefix that produced it. Prefix Corruption further stabilizes training by perturbing unreliable prefixes produced early in training while preserving this target-context alignment. With a simple causal formulation, CMD naturally extends to frame-wise and chunk-wise generation, long video distillation, and camera-conditioned distillation. Experiments demonstrate state-of-the-art aggregate performance among autoregressive methods on both short- and long-video benchmarks, together with substantially improved adherence to time-varying camera controls.

---


### 173. [Jointly Predicting Courses and Grades Using a Transformer-Based Model](https://arxiv.org/abs/2608.13409)

**<font color=#1a73e8>作者：</font>** Paul Savala  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing predictive models in learning analytics often treat student academic history as a simple sequence, overlooking the concurrent nature of courses taken within a semester. This simplification can lead to inaccurate performance predictions, particularly for students with heavy or challenging course loads. This paper introduces a TRansformer for Academic Course-grade Estimation (TRACE) that addresses this limitation by jointly predicting both the set of courses a student will take and their corresponding grades for an upcoming semester. Our approach encodes courses on a per-semester basis to capture the effects of course concurrency and utilizes a novel loss function combining course-set prediction with grade prediction. We demonstrate that predicting courses taken in addition to the grades in those courses leads to significant improvements in prediction quality. Trained on ten years of institutional data, our joint prediction model reduces mean absolute error by nearly 50% compared to an identical architecture that predicts grades alone. The model also outperforms traditional LSTM-based sequential models, as well as graph neural network-based approaches, and offers natural ways to incorporate student attribute data. This work demonstrates the utility of modern neural architectures for creating interpretable models that can be adapted to new institutions via retraining and recalibration, as well as the importance of key techniques, such as predicting courses taken during training. We discuss how this model could be incorporated into early detection systems at institutions of higher education.

---


### 174. [Sensorimotor Stickies: A Reconfigurable On-Body Platform for Closed-Loop Sensorimotor Training](https://arxiv.org/abs/2608.13412)

**<font color=#1a73e8>作者：</font>** Tianhong Catherine Yu, Jiwei Zheng, Chi-Jung Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Closed-loop sensorimotor training systems can improve learning by sensing movement and delivering real-time feedback, yet most are built as fixed implementations tied to a single task, even though the core technology (inertial and tactile sensing, vibrotactile cueing, rule-based logic) remains the same. We present Sensorimotor Stickies, a reconfigurable on-body platform that treats sensing and vibrotactile feedback as modular stickies that can be patched onto the body as needed. The platform includes miniaturized adhesive modules for IMU sensing, optional tactile sensing, and vibrotactile actuation; low-power firmware and BLE infrastructure for raw streaming and motor control without task-specific rewrites; and a companion mobile app that provides a shared body-centered model for placement, calibration, and feedback authoring. Together, these components enable reconfiguration across training scenarios, user needs, and feedback setups. We evaluate the platform through technical characterization, configured application demonstration, practitioner-mediated configuration sessions, and an end-user study, demonstrating technical feasibility, reconfiguration breadth, and end-user configurability for first-time setup, calibration, and within-task feedback reconfiguration.

---


### 175. [Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Research and Development](https://arxiv.org/abs/2608.13417)

**<font color=#1a73e8>作者：</font>** Yiwei Li, Wanli Yang, Hexiang Tan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents are increasingly capable of improving models, systems, and other technical artifacts through long-horizon experimentation. To understand the current state of this capability, however, evaluation must go beyond final scores, which neither reveal where progress is gained or lost nor indicate whether accumulated experience improves later decisions. We therefore present a systematic evaluation of seven frontier models on 36 long-horizon tasks based on a new framework that uses rule-based metrics to characterize within-run behavior through Solution Framing, Execution, and Feedback Control and controlled comparisons to assess experience reuse within and across tasks. The results show that current agents operate more like engineering optimizers than fully autonomous researchers: they can formulate and implement practical solutions, but their performance varies substantially across runs, their strongest solutions mainly adapt or combine established techniques, and genuine methodological novelty remains rare. Detailed analysis reveals that observed performance is shaped by multiple factors, including distinct process bottlenecks behind similar final outcomes, experience reuse that can help or mislead subsequent decisions, and harness designs that affect performance stability. These findings suggest concrete directions for improving model training, inference-time strategies, experience management, and harness design.

---


### 176. [Motor, Cognitive, or Corpus? What Survives Cross-Lingual Transfer in Speech-Based Parkinsons Disease Detection](https://arxiv.org/abs/2608.13425)

**<font color=#1a73e8>作者：</font>** Serli Kopar, Sam Gijsen, Abner Hernandez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) speech representations achieve strong performance for Parkinson's disease (PD) detection within individual corpora. However, it remains unclear whether these models capture disease-related characteristics or exploit dataset-specific confounds, particularly since most SSL backbones are pretrained exclusively on healthy speech. To investigate this question, we perform a layer-wise analysis of nine SSL speech backbones using a low-capacity logistic regression probe across three languages. We structure the evaluation as multiple scenarios that progressively introduce distribution shifts in participant identity, recording conditions, language, and pathology. Our results reveal two key findings. First, layer selection is highly corpus-dependent: the optimal representation layer is determined primarily by the source dataset rather than by the SSL architecture itself. Second, the transferred discriminative signal lacks pathological specificity: classifiers trained to detect PD assign similarly high probabilities to both PD and dementia speech in the target corpus. These results highlight critical limitations that must be addressed before speech-based pathology recognition models can be reliably deployed in clinical settings.

---


### 177. [Academic League of Artificial Intelligence - An Integrative Perspective of Teaching, Research, and Extension](https://arxiv.org/abs/2608.13447)

**<font color=#1a73e8>作者：</font>** Alison R. Panisson, Maria Eduarda W. M. Vianna, Italo Firmino da Silva 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Academic leagues have become important mechanisms for promoting extracurricular education and strengthening the integration between universities and society. This paper presents the organizational framework adopted by the Academic League of Artificial Intelligence (LIA) at the Federal University of Santa Catarina (UFSC), designed to integrate teaching, research, and university extension through a student-centered, project-based approach. The framework combines democratic governance, collaborative learning, and dynamic project organization to foster both technical and transversal competencies. The framework is illustrated through representative initiatives, including competition teams, study groups, open lectures, knowledge repositories, and AI-powered applications with social impact. These projects demonstrate how diverse educational, scientific, and extension activities can be developed within a common organizational structure while promoting leadership, scientific production, community engagement, and knowledge preservation. The reported experience indicates that the proposed framework provides a flexible and replicable model for integrating the three university pillars into engineering and computing education, offering practical guidance for academic leagues and similar student organizations.

---


### 178. [A Unifying Perspective on Causal World Models: From Observations to Representations to Structure](https://arxiv.org/abs/2608.13456)

**<font color=#1a73e8>作者：</font>** Avinash Kori, Fabrizio Russo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World Models (WM) are increasingly seen as a foundation for intelligent agents that can predict, plan, and act beyond their training distribution. In this paper, we study WMs from a causal perspective across multiple levels of abstraction, ranging from perceptual observations to building a conceptual representation of the structure governing the environment dynamics. We argue that useful WMs must go beyond generative capabilities alone: they should also capture entity properties, entity-to-entity interactions, and entity-to-environment interactions that determine and explain the dynamics of a system. We provide a formal definition of Causal WMs (CWMs) grounded in the tasks they are intended to support, connecting world modelling with existing work in causal representation learning, object-centric learning, causal discovery, structural causal models, and model-based decision-making. Finally, we relate CWMs to the literature on identifiability, clarifying when the components of a WM can be recovered from data and up to which equivalence. With this, we ground WMs in representations and structures that support causal reasoning and informed decision-making.

---


### 179. [Symmetry-Breaking De Novo Crystal Generation via Markovian Jump Diffusion](https://arxiv.org/abs/2608.13457)

**<font color=#1a73e8>作者：</font>** Van Khoa Nguyen, Alexandros Kalousis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating crystals has recently attracted significant interest due to their broad applications in materials science. However, existing generative models struggle to produce complete crystallographic specifications, limiting their ability to capture global symmetry and structural dependencies. In particular, current state-of-the-art approaches generate crystals only up to site symmetries and rely on sampling space groups from empirical distributions during generation. Inspired by \emph{spontaneous symmetry breaking} in physics, where crystals break symmetries under external conditions, we propose a novel diffusion-based framework that generates full structure specifications by reversing from the lowest-symmetry priors. Our method leverages a Markovian jump-diffusion process to model these symmetry-breaking dynamics, enabling it to traverse different space groups in a physically motivated manner. Our model, dubbed \emph{Symmetry-breaking Crystal Diffusion} (SbCD), introduces a principled approach to explicitly incorporate inter-space-group transitions into the generative process. In de novo generation experiments on MP20 and MPTS-52, SbCD outperforms its symmetry-preserving counterpart by a substantial margin, offering a promising perspective for generative modeling of crystalline materials.

---


### 180. [SNM-VFI: Symmetric Nonlinear Motion-Guided Generative Video Frame Interpolation](https://arxiv.org/abs/2608.13460)

**<font color=#1a73e8>作者：</font>** Jisoo Jeong, Hong Cai, Jamie Menjay Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Symmetric Nonlinear Motion-guided Generative Video Frame Interpolation (SNM-VFI), a training-free framework for motion-controllable generative video frame interpolation with pre-trained optical flow and video diffusion models. Unlike conventional diffusion-based VFI methods that synthesize intermediate frames from random noise, SNM-VFI guides the generative process with correspondence-aware frames produced by a symmetric nonlinear motion model. Specifically, we first utilize a pre-trained optical flow model to construct multi-frame nonlinear flow-based intermediate frames and confidence maps. These flow-guided frames are then encoded as latent priors to initialize and iteratively guide a pre-trained Video Diffusion model, enabling the diffusion model to preserve dense motion correspondence while improving perceptual realism. To further enhance output quality, we employ confidence maps to fuse structurally reliable flow-based predictions with diffusion-generated details in uncertain regions such as occlusions and object boundaries. Extensive evaluations on challenging benchmarks, including DAVIS, Sintel, and KITTI, demonstrate that SNM-VFI achieves strong perceptual quality, competitive reconstruction accuracy, and robust temporal coherence across diverse motion scenarios.

---


### 181. [Doubly Robust Estimation of Causal Effect on CVR with Targeted Regularization](https://arxiv.org/abs/2608.13461)

**<font color=#1a73e8>作者：</font>** Jiayi Dan, Bo Li, Lu Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-click conversion rate (CVR) is a key metric in various scenarios including e-commerce and advertising, reflecting the efficiency and user experience in the second stage of the conversion process. Estimating the causal effect on CVR is therefore of great practical importance. However, directly applying existing causal inference methods to clicked samples introduces sample selection bias and increased variance due to the exclusion of non-click data. Recent studies on CVR prediction introduce "ideal loss", which optimizes model parameters using an unbiased estimate of the loss over the full sample. Nevertheless, there is no guarantee that unbiasedness of the loss implies unbiasedness of the final estimator.
We revisit this challenge from the perspective of semiparametric theory. Specifically, we develop a new doubly robust causal effect estimator for chain-structured outcomes such as CVR, and derive its theoretical properties in detail. It achieves a faster convergence rate compared to nuisance parameters estimation and is therefore more robust when using flexible nonparametric estimators, including neural networks. Based on these theoretical findings, we further design a framework based on targeted regularization to improve numerical stability and practical applicability.
Extensive experiments on synthetic and real-world data demonstrate the effectiveness and robustness of our method. In addition, we find that naively combining loss debiasing with standard causal estimators underperforms our method, highlighting the necessity of developing the new estimator tailored to this CVR-style objective with solid theoretical guarantees.

---


### 182. [Concept Drift Detection and Adaptive Retraining of Malware Classification Models](https://arxiv.org/abs/2608.13465)

**<font color=#1a73e8>作者：</font>** Christofer Washington Berruz Chungata, Martin Jurecek, Katerina Potika 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept drift refers to changes over time in the statistical properties of data, as compared to the data that was used to train a learning model. Machine learning models for malware detection or classification are particularly susceptible to performance degradation caused by concept drift, as attackers constantly modify existing malware. In this chapter, we analyze two machine learning-based approaches to automated concept drift detection-a novel approach based on One-Class Support Vector Machines (OCSVM) and a previously-studied technique based on Minibatch K-Means (MK-Means). For comparison we also consider Maximum Mean Discrepancy (MMD), a statistical technique for detecting changes in multidimensional data. We conduct an extensive series of experiments comparing the effectiveness of four learning models, namely, Multilayer Perceptron, Random Forest, Support Vector Machines, and eXtreme Gradient Boosting. For each of these models, we consider three distinct scenarios: A static scenario where no model retraining occurs, a periodic scenario where models are constantly retrained irrespective of concept drift, and a drift-aware scenario where models are only retrained when concept drift is detected. Under the drift-aware scenario, we analyze the tradeoff between accuracy and training efficiency using Pareto Front analysis. We find that all three concept drift detection techniques achieve classification accuracy comparable to periodic retraining, while offering substantially greater efficiency in terms of the number of models that must be retrained. In addition, drift-aware retraining based on our OCSVM technique generally outperforms the MK-Means and MMD approaches. Overall, these results provide strong evidence that we can accurately detect concept drift in malware classification models.

---


### 183. [Active-Trace Complexity Bounds for Moreau--Yosida Unadjusted Langevin Sampling](https://arxiv.org/abs/2608.13467)

**<font color=#1a73e8>作者：</font>** Yuchen Xin, Zhihua Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the Moreau--Yosida unadjusted Langevin algorithm (MYULA) for the nonsmooth composite target \[ \pi(dx)\propto \exp\{-f(x)-g(x)\}\,dx, \qquad x\in\mathbb R^d, \] where \(f\) is \(m\)-strongly convex with \(L_f\)-Lipschitz gradient and \(g\) is convex and \(G\)-Lipschitz. Let \(g_\lambda\) be the Moreau envelope of \(g\), \(\pi_\lambda\) the corresponding smoothed target, and \(a_\lambda=\operatorname{tr}H_\lambda\), where \(H_\lambda\) is the a.e./weak Hessian of \(g_\lambda\). We show that the leading MYULA discretization error is controlled by the reference active trace \(B_{\mathrm{ref}}\), the average of \(a_\lambda\) along the heat substep of one MYULA update started from \(\pi_\lambda\), rather than by the global curvature bound \(d/\lambda\). If \(M_\lambda\) is an a.e. upper bound for \(a_\lambda\), then, up to logarithmic factors, \[ N \lesssim \frac{1}{m} \left[ L_f + \frac{ \tau_f+G^2+B_{\mathrm{ref}} }{ \varepsilon_{\mathrm{alg}}^2 } + \frac{M_\lambda}{\varepsilon_{\mathrm{alg}}} \right], \qquad \tau_f:= \sup_x\operatorname{tr}\nabla^2 f(x), \] iterations suffice to ensure \(\sqrt m\,W_2(\mu_N,\pi_\lambda)\leq\varepsilon_{\mathrm{alg}}\), where \(\mu_N\) is the law of the \(N\)-th iterate and \(W_2\) is the quadratic Wasserstein distance. We also prove the Moreau-bias bound \[ \sqrt m\,W_2(\pi_\lambda,\pi) \leq \frac{G^2\lambda}{4}. \] Thus, choosing \(\lambda\asymp\varepsilon/G^2\) gives an end-to-end guarantee for \(\pi\). The universal estimate \(B_{\mathrm{ref}}\leq d/\lambda\) yields \(\widetilde O(\varepsilon^{-3})\) accuracy dependence. For the structured piecewise-linear, lasso-type, group, and total-variation penalties considered here, curvature--tube estimates make \(B_{\mathrm{ref}}\) independent of \(\lambda\), yielding \(\widetilde O(\varepsilon^{-2})\) for the same classical MYULA kernel.

---


### 184. [MapRoute++: Surrogate-Guided Semantic Routing for Visual Concept Unlearning](https://arxiv.org/abs/2608.13478)

**<font color=#1a73e8>作者：</font>** Ashok Urlana, L. D. M. S. Sai Teja, Vivek Hruday Kavuri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present our submission to Task 3 of the Gen$\mu$ 2.0 Challenge on visual concept unlearning. Building on MapRoute, we introduce task-specific training objectives, richer concept representations, and semantic routing for concept-specific mapper selection. Our approach improves robust concept removal while preserving unrelated and semantically adjacent concepts. On the official benchmark, evaluated using the Erasing-Retention-Robustness (ERR) metric on Stable Diffusion v1.4, our method outperforms the state-of-the-art baseline by 12.1\% on average across the five concept categories, achieving substantial gains.

---


### 185. [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489)

**<font color=#1a73e8>作者：</font>** DreamX Team, Rui Chen, Xiangxiang Chu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present \textbf{DreamX-Phi 1.0}, an action-conditioned video world model for robotic manipulation that, given an observed frame, a language instruction, and a prescribed action sequence comprising end-effector poses and gripper states, predicts the resulting future observations. Yet realism alone does not guarantee faithfulness: a convincing rollout can still move the wrong arm or lose the manipulated object. To ensure the prediction respects each arm's commanded path, we inject per-arm $\mathrm{SE}(3)$ transformations into attention via \textbf{PRoPE-style geometric encoding}, preserving arm identity and rigid-motion structure. Action control alone does not fully constrain scene geometry or the evolution of small manipulated objects. We therefore add a lightweight \textbf{depth branch} for scene-level geometry and use \textbf{SAM3 masks} with a frozen \textbf{V-JEPA teacher} to maintain object consistency throughout grasping. We further distill the multi-step generator into a few-step student via distribution-matching distillation for efficient deployment. At the time of writing, \model{} achieves first place on Track~1 and second place on Track~2 of the WorldArena~2.0 Challenge. Our model and code will be publicly available.

---


### 186. [AlayaWorld: Interactive Long-Horizon World Modeling - Full Technical Report (v1.1)](https://arxiv.org/abs/2608.13492)

**<font color=#1a73e8>作者：</font>** AlayaWorld Team, Kaipeng Zhang, Chuanhao Li 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This report presents an improved version of AlayaWorld. While the backbone architecture, chunk-wise autoregressive generation scheme, and training data remain unchanged from the previous release, we substantially revise how conditioning signals are represented and integrated into the model. The new design is guided by a simple principle: conditioning signals should match the generated content as closely as possible in both latent representation and temporal structure. To this end, we make two major changes. First, we replace the previous depth-warping-based spatial memory with a streaming 3D point-cache renderer. Second, we redesign the conditioning pipeline so that visual conditions are encoded in the same causal-VAE latent space, with temporal statistics consistent with those of the generated video. Concretely, the new version introduces six modifications: (1) replacing static-frame image conditioning with motion-aware latent conditioning; (2) causally encoding re-rendered spatial memory as a continuous sequence; (3) aligning the temporal-memory window in pixel space; (4) adopting hard memory dropout that removes memory tokens rather than zeroing them; (5) unifying the VAE encoding and decoding protocol across training and inference; and (6) removing the camera AdaLN branch, such that viewpoint control is provided entirely through the re-rendered spatial condition.

---


### 187. [GS$^{2}$CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via Large Vision Model Priors](https://arxiv.org/abs/2608.13502)

**<font color=#1a73e8>作者：</font>** Yanming Yang, Chenxi Song, Ping Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Snapshot Compressive Imaging (SCI) offers an efficient solution for high-speed video acquisition and, under exposure-time camera--scene relative motion, multi-view scene capture by compressing temporal or spatial information into a single 2D measurement. While recent studies have explored SCI for 3D scene reconstruction, existing methods struggle with significant challenges due to information loss, limited viewpoint diversity, and the computational burden of jointly optimizing 3D representations and camera poses. In this work, we propose a novel framework that reconstructs high-quality 3D scenes from a single SCI measurement by leveraging 3D Gaussian Splatting (3DGS) and the powerful priors of large-scale vision foundation models (VFMs). Our primary reconstruction combines measurement-derived 3D VFM initialization with SCI-aware Gaussian optimization. After coarse-stage convergence, an auxiliary 2D VFM provides pseudo-view supervision at synthesized viewpoints for local appearance refinement. To further address the instability caused by ambiguous SCI supervision during 3DGS optimization, we introduce Opacity-Guided Splitting and Growth Regulation (OSGR), an SCI-specific densification strategy that augments split candidates using local opacity statistics, discourages loss-compensating opacity inflation through mean-opacity regulation, and bounds representation growth with explicit candidate-ratio and Gaussian-count constraints. Extensive experiments across multiple benchmarks demonstrate that our method achieves the strongest overall performance, combining leading reconstruction quality and robustness to viewpoint variation with competitive computational efficiency.

---


### 188. [Sparse Orthogonal Regression Technique: A Spectral Framework for Equation Discovery, Approximation, and Integration](https://arxiv.org/abs/2608.13504)

**<font color=#1a73e8>作者：</font>** Sabin Roman, Ljupco Todorovski, Saso Dzeroski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop the Sparse Orthogonal Regression Technique (SORT), a sparse spectral framework for learning orthonormal-basis expansions from noisy and irregularly sampled data. SORT estimates expansion coefficients directly from observations using L1-regularized regression, avoiding explicit quadrature or analytic inner-product evaluation. The central application is data-driven discovery of ordinary differential equations: vector fields are represented in chosen orthogonal bases and learned as sparse coefficient expansions. This provides a complementary route to symbolic regression, grammar-based discovery, and SINDy-style sparse identification by first recovering a compact spectral representation, which can later guide searches for simpler analytic forms. Across the dynamical-system experiments, SORT matches or improves upon library-based sparse-regression baselines when the basis is well adapted to the problem, and shows more stable degradation under sparse sampling, noisy derivative estimates, and representation mismatch. Specific examples illustrate why this representation is useful: if a finite library misses the problem-specific nonlinearity, the resulting model can fail. SORT is not immune to mismatch, but it shifts the problem away from brittle selection among generic terms to basis design adapted to the problem domain. The experiments also show that dominant low-order coefficients persist as model order increases, supporting order-consistent model growth. Beyond equation discovery, the same learned expansion supports nonlinear approximation and estimation of complex, high-dimensional integrals by coefficient readout. Overall, SORT provides a reusable intermediate representation for system identification, approximation, and integration, while making basis design an explicit part of the scientific modeling problem.

---


### 189. [TabSOM: A tabular-to-image encoding method based on self-organizing maps](https://arxiv.org/abs/2608.13513)

**<font color=#1a73e8>作者：</font>** David Chushig-Muzo, María Ángeles Rodríguez de Cara, Eva Milara 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tabular-to-image methods have emerged as novel approaches to leverage the high predictive performance of convolutional neural networks and vision transformers. They convert tabular data into image representations, mapping each feature at a fixed pixel location derived from a dimensionality-reduction method (e.g., t-SNE, UMAP, PCA). However, they encode only the marginal value of each feature and discard information about feature relationships. We propose TabSOM, a tabular-to-image encoding built on the Self-Organizing Map (SOM), which provides: (i) a spatial layout in which every input feature occupies a fixed canvas position derived from its component plane via collision-free Hungarian assignment; and (ii) a graph that captures pairwise feature relationships derived from the SOM component planes. The resulting image stacks two multi-scale node channels: one encodes feature values at fixed scales, while the other encodes pairwise feature interactions as spatial connections between related features. Two SOM-derived interpretability approaches are introduced: a prototype-inspired partial dependence plot and a class--separation importance score. Benchmarked against twelve existing tabular-to-image methods across public binary-classification datasets, TabSOM ranks first or second on every dataset and achieves the lowest variance of any method evaluated. Interpretability obtained with TabSOM was validated against Random Forest, XGBoost, and SHAP, the class-separation score shows reasonable agreement with established baselines on the top-ranked features while capturing complementary structural information from input data. These results demonstrate that TabSOM provides an effective and interpretable approach for applying deep learning architectures to tabular data, bridging the performance--interpretability gap in this domain.

---


### 190. [Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology](https://arxiv.org/abs/2608.13518)

**<font color=#1a73e8>作者：</font>** Yunsung Chung, Yingshuo Liu, Abboud F. Hassan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many clinical prediction models treat post-intervention outcomes as a one-step mapping from baseline measurements to a future endpoint. However, recovery after a procedure often unfolds as an irregular trajectory: clinical observations, medication changes, repeat interventions, and physiological measurements are recorded asynchronously and can change risk assessment over time. We propose an intervention-aware clinical world model that represents each patient with a structured latent state and evolves it through time-ordered post-intervention events. The model first encodes baseline imaging into a 3D spatial latent state. It then updates this state using procedural context, static covariates, elapsed time, and peri-event physiological embeddings. Follow-up imaging provides training-only supervision through a latent forecasting objective. We apply the framework to atrial fibrillation ablation. During the 90-day recovery window, irregular post-procedure records provide clinically meaningful evidence for long-term recurrence risk. In repeated internal cross-validation on DECAAF-II, our model achieves AUROC 0.756 and AUPRC 0.777 for recurrence prediction. It also achieves a scar-extent MAE of 2.971 percentage points without requiring follow-up MRI intensities at inference. The learned state supports recurrence-risk queries at different horizons and retrospective input editing of blanking-period records.

---


### 191. [The data geometry of masking diffusion: Certified-optimal schedules via unmasking growth complexity](https://arxiv.org/abs/2608.13520)

**<font color=#1a73e8>作者：</font>** Martin J. Wainwright  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study masking diffusion for discrete sampling and introduce a path-resolved measure of data geometry called the \emph{unmasking growth complexity} ({\textsf{UGC}\xspace}). Its local increments directly control Kullback--Leibler (KL) discretization error, yielding a unified analysis of Bernoulli-subset and fixed-cardinality unmasking schemes. In log-reveal-odds coordinates, this structure yields optimized single-block and multi-block schedules, and quantifies the gains from adapting computational effort to data geometry. Crucially, we show how {\textsf{UGC}\xspace} increments can be estimated from samples via KL increments along coupled reveal trajectories. This leads to \emph{certified-optimal} samplers that achieve a prescribed KL error with high probability and iteration complexity within a constant factor of the corresponding oracle procedure. Collapsing the \ugc path yields the aggregate {\textsf{UGC}\xspace} mass, which connects to classical multivariate dependence measures and complexity measures from previous analyses of discrete diffusion. In the fine-partition limit, the squared integral of the square-root {\textsf{UGC}\xspace} density determines the sharp leading-order optimal Euler discretization error. Examples exhibit substantial dimension-dependent gains over coarse schedules, including $\widetilde{\Omega}(\sqrt{d})$ improvements achievable with a constant number of adaptively placed blocks.

---


### 192. [Safety vs. Social Image: Co-Designing Protection Mechanisms Against Ableist Harassment with People with Disabilities in Social Virtual Reality](https://arxiv.org/abs/2608.13532)

**<font color=#1a73e8>作者：</font>** Kexin Zhang, Daniel Killough, Xinran Adeline Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People with disabilities (PWD) increasingly use avatars to express disability identities in social virtual reality (VR), but greater visibility also invites targeted harassment. Existing safety features are often insufficient, overlooking PWD's experiences and needs. To address this gap, we co-designed protection mechanisms with 11 PWD to reveal their values and needs. Our research employed a social lens to interpret harassment behaviors and protection mechanisms. Inspired by Hall's Proxemics Theory that interpersonal distances indicate social intent and boundaries, we divided social VR spaces into four proxemic zones (Intimate, Personal, Social, and Public) and used them to structure our protection mechanism co-design. We also provided different protection mechanism probes (Inform, Educate, Consent, and Combat) to elicit participant preferences. Our study highlighted the role of social proximity in shaping PWD's harassment perception and protection preferences and revealing PWD's unique social values and needs (e.g., managing harassment with optimism and resilience, prioritizing social image over safety). We proposed design recommendations for protection mechanisms that protect PWD while maintaining their desired social images.

---


### 193. [SCULPT: Subtractive Composition for 3D Part Generation](https://arxiv.org/abs/2608.13541)

**<font color=#1a73e8>作者：</font>** Sikuang Li, Chen Yang, Jiemin Fang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Part-aware 3D generation aims to create digital assets that are coherent as complete objects while exposing structural parts for editing, material assignment, animation, and reuse. Existing methods impose this structure outside the native generation loop: segmentation-based methods partition an already generated shape, while additive methods synthesize parts from predefined layouts, boxes, or tokens and then reconcile them into a whole. The former preserves the generated geometry but fixes the object before part boundaries are determined; the latter exposes part cardinality but often leaves shared boundaries vulnerable to gaps, interpenetrations, and material discontinuities. In this paper, we propose SCULPT, a framework that addresses these challenges through subtractive composition. Given a complete object represented in a structured 3D latent space, SCULPT iteratively applies a joint split predictor to generate one extracted part together with the remaining object. The predictor performs a coupled denoising process conditioned on both the image and the current 3D state, so the extracted part and updated remainder are generated together rather than reconciled after generation. The joint split predictor processes both outputs on the union of their native sparse 3D supports, allowing neighboring supports to overlap rather than imposing a disjoint voxel partition. The rollout ends when the remainder support becomes empty or reaches a fixed safety cap, allowing the number of generated parts to adapt to each object within that bound. Extensive experiments demonstrate state-of-the-art geometry on PartObjaverse while preserving strong complete-object reconstruction after part assembly. Results on four dataset images, one text-to-image-generated input, and one real-world photograph further show fine-grained textured part decomposition beyond the benchmark.

---


### 194. [Alaya-EVOKE: From Linear-Scaling Supervision to Endless World](https://arxiv.org/abs/2608.13546)

**<font color=#1a73e8>作者：</font>** Yuanyang Yin, Gongxuan Wang, Yifan Zhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive world models must support persistent memory, responsive interaction, and long-horizon generation, yet these requirements place conflicting demands on the model. Maintaining history in the denoiser context or key-value cache incurs growing cost, forcing a trade-off between session length and retained memory, while low-latency interaction relies on few-step generation whose capabilities are bounded by its teacher. Evoke addresses both limitations by externalizing persistent world state and redesigning the teacher for long-horizon interactive generation. Scene geometry is maintained in an external, camera-indexed world state bank, from which only view-relevant information is retrieved, keeping the denoiser context bounded as the session grows. Rather than treating the teacher as a fixed generator, we design it for long-horizon supervision: its sparse attention combines chunk-wise grouping, retrieval of selected distant frames, and a linear-attention global state, yielding linear growth in memory and compute while enabling supervision over long horizons. Such supervision exposes content drift that stays locally plausible within short windows, while per-chunk conditioning enables prompt changes and event control throughout the sequence. A 30-second distribution-matching objective, applied under self-forced rollouts, transfers both capabilities to a three-step student that uses no classifier-free guidance, improving resistance to long-term drift while preserving responsive conditioning. With bounded context and recurrent external memory, Evoke supports open-ended, continuously evolving generation; on a single H200 at $384\times 640$, each $1.5\,\mathrm{s}$ chunk is generated in $2.11\,\mathrm{s}$. As a three-step world model, Evoke achieves state-of-the-art performance on WBench while remaining competitive on VBench-Long and VBench-2.0.

---


### 195. [Exponential Convex Calibration Dimension for the Multi-Label Jaccard Measure](https://arxiv.org/abs/2608.13549)

**<font color=#1a73e8>作者：</font>** Mingyuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The per-instance Jaccard score, or intersection over union (IoU), is standard in multi-label classification and binary segmentation. With $s$ labels, its loss matrix has $2^s$ outcomes and reports. Under the convention $\mathrm{Jac}(\varnothing,\varnothing)=1$, we prove that the Jaccard score, shifted-loss, and ordinary loss matrices are nonsingular and that the loss columns have affine dimension $2^s-1$. The proof combines a finite MinHash Gram representation with Boolean Möbius inversion. For exact calibration, we prove $2^{s-1} \leq \mathrm{CCdim}(L^{\mathrm{Jac}}) \leq 2^s-1$. The lower bound uses a factorially weighted distribution with $2^{s-1}+1$ supported outcomes and Bayes-optimal reports. Consequently, every exactly calibrated convex surrogate requires exponentially many prediction coordinates. We also give two polynomial-dimensional approximation guarantees with explicit regret transfers. A new $F_1$-to-Jaccard transfer turns an existing $(s^2+1)$-dimensional $F_1$ surrogate into a polynomial-time rule with asymptotic Jaccard regret at most $3-2\sqrt{2}$. For any $\alpha>0$ and $0<\rho<1$, a MinHash square-loss surrogate attains Jaccard-regret floor $\alpha$ uniformly over arbitrary conditional label distributions. With probability at least $1-\rho$, the direct construction has dimension $O((s^2+s\log(1/\rho))/\alpha^2)$, while a signed variant has dimension $O((s+\log(1/\rho))/\alpha^2)$. Thus zero-regret calibration requires exponential dimension, whereas every fixed additive regret tolerance admits polynomial prediction dimension.

---


### 196. [PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives](https://arxiv.org/abs/2608.13552)

**<font color=#1a73e8>作者：</font>** Kaixin Ding, Xi Chen, Minghong Cai 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models simulate future states conditioned on current observations and user actions. Recent systems have demonstrated impressive video consistency and action controllability over long sequences. However, fairly comparing these interactive models remains challenging. In practice, a human player typically evaluates a world model by pursuing long-horizon objectives through interaction. For example, a user may turn around 360 degrees to see whether the environment remains consistent, or walk into the water and inspect whether realistic water ripples are generated. The action sequence required to achieve the same objective may vary substantially between models, making fixed action-conditioned evaluation unsuitable for cross-model comparison. To address this, we employ multi-modal Agent Players to interact with world models toward specified long-horizon objectives. Building on this paradigm, we introduce PlayWorld, a benchmark providing 171 scenarios, each with a specified objective. To evaluate performance thoroughly, we assess models along four core dimensions: geometry consistency, interaction fidelity, out-of-sight evolution, and insight evolution. In addition, we incorporate basic ability metrics for video quality and controllability. Experiments across nine state-of-the-art world models reveal that current models remain unreliable on long-horizon interactive objectives, particularly in maintaining spatial consistency and persistent state evolution. Code and data are available at this https URL.

---


### 197. [Defensive Boosting for Online Probabilistic Forecasting](https://arxiv.org/abs/2608.13554)

**<font color=#1a73e8>作者：</font>** Georgy Noarov, Aaron Roth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online probabilistic forecasting of binary outcomes chosen by an adaptive adversary. Given an online learning algorithm for a weak hypothesis class $H$, we would like to efficiently obtain two incomparable guarantees that existing online boosting techniques provide separately. Online gradient boosting competes in Brier score with the best predictor induced by the span of $H$ on every sequence, but promises nothing when the span does not contain an accurate predictor. Online weak-to-strong boosting drives classification error to zero under a weak-learning condition, but promises little when that condition fails.
We give a simple defensive forecasting algorithm, the Defensive Booster, that obtains both guarantees. On every adaptive sequence, its Brier score is competitive with the best prediction induced by the span of $H$ at the same rate as online gradient boosting; simultaneously, whenever the realized transcript satisfies the smooth weak-learning condition, its Brier score and randomized classification error satisfy the same rate guarantee as online classification boosting. This is achieved by operationalizing the "dual view" of boosting: When the algorithm's randomized classification error is persistently high, its mistake weights form a smooth reweighting on which every weak hypothesis has low edge, yielding an ex-post hard-core certificate that the weak-learning condition fails. We also develop a strongly adaptive variant, which satisfies both guarantees on every time interval. The Defensive Booster is very efficient: it accesses just one weak-class learner, whereas the prior online boosting methods we compare against maintain large weak-learner ensembles. Experiments on synthetic and real data streams demonstrate its strong predictive performance (sometimes substantially improving over all prior baselines) coupled with orders-of-magnitude faster runtime.

---


### 198. [V-RAE: Rethinking Video Latent Spaces for Generation](https://arxiv.org/abs/2608.13556)

**<font color=#1a73e8>作者：</font>** Minghui Guo, Shengqiong Wu, Hao Fei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent video generation relies on autoencoders to define a compact space in which generative models operate. Although video autoencoder architectures have evolved substantially, their latent spaces are still optimized primarily for pixel-level reconstruction and provide limited high-level semantic organization. A reconstruction-optimal latent space, however, need not be well suited to generative modeling. We propose V-RAE, a video representation autoencoder that builds compact generative latents on top of frozen vision foundation model representations. A lightweight temporal pooling module removes temporal redundancy while preserving semantic structure, and a video decoder reconstructs continuous motion from the compressed features. We evaluate V-RAE with four representative frozen encoders on video reconstruction, semantic probing, and class-conditional generation. V-RAE achieves 2.13 rFVD on K600, outperforming all evaluated large-scale pretrained video VAEs. Its latents retain substantially more semantic information than conventional video tokenizer latents. Under matched generation settings, our best variant achieves gFVD scores of 117.86 and 19.16 on UCF101 and K600, respectively, while converging up to 6x faster}. We further show that reconstruction quality alone is insufficient to characterize generative utility and introduce tFVD, a temporal-coherence diagnostic that correlates more reliably with downstream generation quality. Beyond video generation, V-RAE also improves future video prediction on Cityscapes over the Wan 2.2 VAE latent space under matched prediction settings. Taken together, the experiments show that frozen semantic representations can support video reconstruction, generation, and predictive modeling. The project page: this https URL.

---


### 199. [OmniScientist: An Omni-Modal Omni-Discipline AI Scientist](https://arxiv.org/abs/2608.13558)

**<font color=#1a73e8>作者：</font>** Bobo Li, Hao Fei, Tianjie Ju 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workflow coverage alone does not provide access to the full evidence on which scientific discovery depends. Existing systems typically reason over text, code, labels, or precomputed summaries, leaving scientifically decisive spatial, temporal, cross-channel, and procedural relations unavailable to the agent. We introduce OmniScientist, an end-to-end, omni-modal AI scientist that conducts multidisciplinary research directly from heterogeneous raw evidence. A perception layer and 3 autonomous agents for ideation, experiment, and writeup operate within a deterministic pipeline, allowing observations to shape research questions, experimental decisions, and final claims throughout the research lifecycle. By running idea, rigour, and claim checks in code, the system enforces novelty screening, statistical validity, execution provenance, and numerical traceability. We evaluate OmniScientist on 36 real-data cases spanning 5 discipline families, 4 families of scientific evidence, and modalities including images, signals, audio, video, 3-D structures, trajectories, tables, formulae, and graphs. The system completes the full path from raw data to a compiled manuscript in all 36 cases and achieves a mean overall paper score of 6.3 with the reference reasoning backbone. In paired comparisons against a blind variant that receives only precomputed scalar features, direct perception improves all 7 evaluation dimensions and wins 85% of head-to-head judgments. These results show that lifecycle-wide perception is essential for evidence-grounded scientific discovery and provides a practical path toward broadly capable AI scientists.

---


> [!TIP]
> 当前位于：**151-199**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-199**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

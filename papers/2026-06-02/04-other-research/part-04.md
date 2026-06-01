# 📦 其他研究 | 2026年06月02日

> 本类共 **317** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-317](./part-07.md)

---

### 151. [Generating Reports or Repeating Templates? Measuring and Mitigating Template Collapse in 3D CT Report Generation](https://arxiv.org/abs/2605.30984)

**<font color=#1a73e8>作者：</font>** Tom Maye-Lasserre, Yitong Li, Bailiang Jian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern 3D medical vision-language models (VLMs) can generate fluent radiology-style text while exhibit critically low pathology detection and output diversity, collapsing to generic templates that under-report rare yet critical findings. We identify this failure mode as Template Collapse. This failure stems from the unique constraints of 3D medical imaging, e.g., limited data, severe label imbalance, and weak signals from volumetric encoders. Under these constraints, text-generation objectives encourage shortcut learning and fluent but weakly grounded reports. We systematically diagnose the Template Collapse through clinical fidelity, output diversity, normal-template bias, and rare-finding survival. To mitigate it, we propose CLarGen, a decoupled framework that separates what to say (clinical detection) from how to say it (language synthesis). CLarGen uses (i) a Latent Query Transformer for multi-label pathology detection, (ii) pathology-guided retrieval for clinically matched exemplars, and (iii) a medical language model to synthesize the final report from detected findings and retrieved context. Across state-of-the-art 3D CT report generation baselines, CLarGen mitigates Template Collapse and substantially improves clinical accuracy (macro-F1 0.487 vs. 0.189; CRG 0.472 vs. 0.368) while maintaining fluent reporting. Our results suggest that explicit, measurable clinical grounding is essential for template-collapse-resistant 3D CT report generation. Code will be released upon acceptance.

---


### 152. [Benchmarking Single-Step Inpainting Methods for Multi-Object 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2605.30987)

**<font color=#1a73e8>作者：</font>** Finn Dröge, Cecilia Curreli, Abhishek Saroha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The tasks of object removal and inpainting 3D Gaussian Splatting (3DGS) scenes face challenges such as 3D consistency across camera views. In comparing 2D inpainters and their suitability for the 3D domain, we find that reconstruction-based inpainters outperform generative diffusion models in 3D consistency. Integrating these 2D inpainters into different single-step methods for creating and finetuning 3DGS scenes, our results indicate that initializing the scene from scratch produces higher quality results than finetuning the existing scene. Using a state-of-the-art generative 2D inpainter, we create a straightforward baseline to underline the importance of object removal before inpainting in the 3D setting. Since 360° datasets rarely include real-world ground truths, and challenging occlusion scenarios are equally sparse, we introduce a novel multi-object scene with recorded ground truth data and many views with object occlusions.

---


### 153. [Free-Riding in the AI Economy: Demystifying Logic Flaws in x402-Enabled Payment Systems](https://arxiv.org/abs/2605.30998)

**<font color=#1a73e8>作者：</font>** Shengchen Ling, Yihang Huang, Yuan Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The agentic economy demands programmatic financial rails, positioning the x402 protocol as the de facto standard for machine-to-machine payments. However, bridging synchronous HTTP requests with asynchronous blockchain finality introduces profound state synchronization challenges. In this work, we perform the first comprehensive security analysis of the x402 ecosystem. By formalizing five Security Invariants, we reveal that current implementations fail to enforce transactional atomicity and cryptographic context binding, leading to systemic vulnerabilities. We identify a semantic gap in signature design enabling cross-resource substitution, where payment proofs are transplanted to other unauthorized contexts. Furthermore, we expose a temporal gap where concurrency race conditions allow probabilistic service duplication. In the AI inference domain, we demonstrate how dynamic pricing models are vulnerable to allowance overdrafts and infrastructure rate limits. We validate these vulnerabilities against official SDKs and live deployments. Specifically, we show that attackers can exploit the synchronization gap in dynamic authorization schemes to force merchants to subsidize compute costs, achieving a resource leakage ratio of up to 100% on production middleware. Finally, we propose architectural mitigations, advocating for request-bound signatures and pessimistic state locking to secure the financial rails of autonomous agents. All discovered issues have been disclosed to Coinbase and ThirdWeb.

---


### 154. [Iterative Framework For Data Augmentation Of Segmented Fingerprints](https://arxiv.org/abs/2605.31001)

**<font color=#1a73e8>作者：</font>** João Leonardo H. D. Agnol, Wesley Augusto de Bona, Erick Oliveira Rodrigues 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infant biometrics presents unique challenges due to the physiological differences between infants and adults, compounded by the scarcity of available data for research that limits the development of robust matching systems. This paper proposes a novel data augmentation method that uses iterative techniques to generate diverse variants of segmented fingerprints by inducing errors in a convolutional neural network trained to extract fingerprint ridges and valleys. Experiments on real infant fingerprints demonstrate the method's effectiveness in expanding fingerprint variability, with augmentations exhibiting significant fluctuations in minutiae counts while still retaining visual similarity to the originals. The study also highlights the method's customizable nature for applying varying levels of changes to fingerprint segmentations. Future research includes training segmentation and matching neural networks using datasets augmented by the proposed framework.

---


### 155. [Learning Multi-Agent Coordination via Sheaf-ADMM](https://arxiv.org/abs/2605.31005)

**<font color=#1a73e8>作者：</font>** Jeffrey Seely, Bartłomiej Cupiał, Llion Jones  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a differentiable optimization framework for multi-agent coordination. An input is decomposed into overlapping local views, each processed by an agent that solves a convex subproblem parameterized by a neural encoder. Agents coordinate through the Alternating Direction Method of Multipliers (ADMM) with inter-agent constraints specified by a cellular sheaf. The sheaf specifies which aspects of neighboring solutions must agree, allowing for heterogeneous notions of global consensus. Backpropagating through the unrolled optimization jointly trains all components of the multi-agent system. We evaluate on maze pathfinding, image classification, and Sudoku, where agents with individually insufficient local views learn to coordinate to produce correct global outputs. On MNIST, the local-view decomposition yields improved robustness to distribution shifts relative to a standard CNN. On Sudoku, the optimization-derived structure yields markedly higher solve rates than parameter-matched MPNN baselines. Finally, the ADMM structure exposes distinct primal, consensus, and dual state variables, opening the coordination dynamics to direct analysis and intervention -- a property unavailable in standard message-passing architectures.

---


### 156. [DEM: A Distilled Explanation Model for Interpretable Anomaly Detection in Physiological Sensor Networks](https://arxiv.org/abs/2605.31007)

**<font color=#1a73e8>作者：</font>** Jyotirmoy Singh, Anushka Roy, Shreea Bose 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection in physiological sensor data from Wireless Body Area Networks (WBANs) can be caused by sensor faults, network disruptions, or missing data, leading to false alarms. Hence, it demands both high predictive accuracy and clinically interpretable explanations. Existing approaches rely either on black-box models that achieve strong performance but offer no transparency, or on post-prediction explanation methods such as SHAP and LIME. In this paper, we propose the Distilled Explanation Model (DEM), a three-stage glass-box framework that distills the non-linear knowledge of a gradient boosting expert into an interpretable decision tree operating on residuals relative to a linear baseline, so that the explanation is not an approximation but the prediction itself. DEM introduces a novel distillation fidelity metric that quantifies how faithfully the explanation tree captures the expert model's non-linear contribution, providing a principled measure of explanation trustworthiness absent from prior interpretable models. Evaluated across four physiological datasets, including MIMIC-IV, WESAD, eICU, and an in-house SmartNet WBAN corpus, DEM achieves an AUC of 0.9964 on clinical contextual anomaly detection and 0.9047 on wearable stress detection while producing human-readable if-then rules at a controllable depth. Inference requires 0.17ms per 1000 samples, rendering DEM 1235x faster than SHAP-based post-hoc explanation and suitable for real-time physiological monitoring. Ablation studies confirm that the XGBoost distillation step provides measurable gains over naive residual fitting, and depth-sensitivity analysis demonstrates an explicit, user-controlled accuracy-interpretability trade-off unique to DEM among existing intrinsically interpretable models.

---


### 157. [Physics-Informed Coarsening for Multigrid Graph Neural Surrogates](https://arxiv.org/abs/2605.31013)

**<font color=#1a73e8>作者：</font>** Amir Bazzi, David Cardinaux, Ramy Nemer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-based surrogates for partial differential equations have recently matched the accuracy of classical solvers while achieving orders-of-magnitude speedups, predominantly in fluid settings and structured geometries. In contrast, robust surrogates for deformable solids remain underexplored, despite the presence of nonlinear elasticity, plasticity, and transient behavior that challenge standard architectures. We introduce a multigrid graph neural network for solid mechanics that couples an encoder-processor-decoder backbone with a physics-informed coarsening strategy. Instead of downsampling via geometric heuristics, our method scores nodes using a residual-based measure of local physical activity and preferentially retains regions of high strain or stress concentration, allocating multiscale capacity where it is most needed. This preserves long-range interactions through hierarchical message passing while improving stability over long rollouts. We evaluate on multiple datasets covering linear, nonlinear, and transient regimes, and observe consistent gains in accuracy and rollout stability compared to standard sampling baselines. Our results highlight the importance of physics-informed coarsening for scalable surrogate modeling in solid mechanics.

---


### 158. [SDM-Q: Cost-Aware Staged Decision-Making for Multi-Omics Classification with Deep Q-Learning](https://arxiv.org/abs/2605.31014)

**<font color=#1a73e8>作者：</font>** Nan Mu, Xiaoyang Fan, Chen Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-omics data provide complementary molecular characterizations of disease phenotypes and play an important role in disease diagnosis and subtype classification in precision medicine. However, acquiring complete multi-omics profiles is expensive and time-consuming, while most existing deep learning methods assume full modality availability during inference, resulting in substantial redundancy and limited practicality in clinical settings. To address this issue, we propose SDM-Q, a reinforcement learning framework for adaptive and cost-aware multi-omics classification. Specifically, multi-omics diagnosis is reformulated as a finite-horizon sequential decision problem, where the currently acquired omics modalities define the diagnostic state at each stage. An action--value function determines whether to acquire an additional modality or terminate the decision process and output the final prediction. To balance diagnostic utility and acquisition cost, the reward is defined only at the terminal stage and jointly determined by classification correctness and cumulative modality acquisition cost. A backward stage-wise optimization strategy is introduced to improve policy consistency and training stability. Experiments on four public multi-omics datasets, including ROSMAP, LGG, BRCA, and KIPAN, demonstrate that SDM-Q effectively reduces redundant modality acquisition while maintaining competitive classification performance compared with methods using complete multi-omics inputs. In the BRCA and KIPAN datasets, more than 99\% and 95\% of subjects, respectively, achieve accurate classification using only a single omics modality, while the average number of acquired modalities remains below two for ROSMAP and LGG. These results suggest that cost-aware sequential decision-making provides an effective paradigm for improving the efficiency of precision medicine workflows.

---


### 159. [An Efficient and Scalable Graph Condensation with Structure-Preserving](https://arxiv.org/abs/2605.31016)

**<font color=#1a73e8>作者：</font>** Yulin Hu, Fuyan Ou, Ye Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph condensation (GC) is pivotal for enabling Graph Neural Networks (GNNs) deployment in resource-constrained scenarios by compressing large-scale graphs into compact synthetic counterparts. Existing GC methods commonly suffer from computational inefficiency due to coupled optimization as well as encountering poor generalization across GNN architectures. To address these challenges, this study proposes an Efficient and Scalable Graph Condensation with Structure-Preserving (SP-ESGC), which possesses a decoupled design that separates node condensation from graph structure generation. Specifically, it first employs heat kernel feature propagation to generate node representation via spectral graph theory-inspired diffusion. Further, a novel hybrid clustering strategy is designed to extracts discriminative intra-class centroids from the node representation. Finally, a pre-trained edge predictor infers transferable structural patterns from the original graph, ensuring accurate synthetic graph generation. Extensive experiments on real-world graph datasets demonstrate that the proposed SP-ESGC implementes a precise GC with significantly high computational efficiency. Moreover, SP-ESGC also generalizes well across diverse GNN architectures.

---


### 160. [Thou Shall Not Pass: Gatekeeping Outbound TLS Connections](https://arxiv.org/abs/2605.31020)

**<font color=#1a73e8>作者：</font>** Henrique B. Brum, Matteo Franzil, Riccardo Germenia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite the widespread use of Transport Layer Security (TLS), its security guarantees are frequently compromised by outdated versions and misconfigurations. To analyze this problem, we collected more than 50 million TLS handshakes over a two-week period at our research institution, Fondazione Bruno Kessler, and analyzed three server-selected parameters against the recommendations of four TLS guidelines. Our analysis shows that while the use of insecure or outdated options is minimal, it remains persistent. More importantly, servers are adopting the latest TLS advancements much faster than official guidelines can be updated to provide directives for them. These findings, combined with the difficulty of configuring TLS clients due to their ephemeral, ubiquitous and server-dependent nature, leave users vulnerable to non-standard or outright insecure connections. To address this, we present TLSGatekeeper, a real-time, network-based tool that transparently monitors handshakes, analyzes server parameters, and, based on organizational policy, reports non-compliant connections without requiring client-side modifications. Unlike Next-Generation Firewalls, TLSGatekeeper preserves end-to-end privacy by validating only handshakes, and offers greater flexibility in defining undesired configurations. Our evaluation shows that TLSGatekeeper sustains traffic rates of up to 100 Gbps while preventing insecure connections, with an average added processing delay of 671 ns (TLS 1.3) and 795 ns (TLS 1.2) per handshake packet, making enforcement feasible at scale.

---


### 161. [Augmented Lagrangian Predictive Coding](https://arxiv.org/abs/2605.31022)

**<font color=#1a73e8>作者：</font>** Jeffrey Seely, Julian Gould  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive coding (PC) is a local-learning alternative to backpropagation (BP), training deep networks via local energy-minimization dynamics rather than a global backward pass. We introduce Augmented Lagrangian Predictive Coding (PC-ALM), which maintains PC's inference budget but aligns each weight update toward BP by accumulating per-layer constraint errors into a layer-local Lagrange multiplier. In linear PC networks, PC-ALM converges to an equilibrium with exact BP gradients distributed across the network via only layer-local updates. We analyze PC-ALM in nonlinear PC networks up to depth 128 and show that it matches BP performance across all width-depth regimes, notably in deep narrow networks where PC underperforms. PC-ALM introduces recurrent dynamics in each layer's activations. Compared to PC's heat flow on a scalar energy, PC-ALM dynamics are driven by dual ascent on the augmented Lagrangian. We observe "ballistic" credit propagation across very deep networks, with credit signals evenly distributed across layers, compared to PC's slow, diffusive credit propagation. Beyond the algorithm itself, the augmented Lagrangian framework offers a generalization of PC, and may yield insights into how distributed systems could compute and propagate BP-like credit signals through purely local dynamics.

---


### 162. [HADT: A Heterogeneous Multi-Agent Differential Transformer for Autonomous Earth Observation Satellite Cluster](https://arxiv.org/abs/2605.31023)

**<font color=#1a73e8>作者：</font>** Mohamad A. Hady, Muhammad Anwar Masum, Siyi Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work addresses the problem of autonomous resource management in heterogeneous satellite cluster conducting Earth Observation (EO) missions including optical and Synthetic Aperture Radar (SAR) satellites. In autonomous operation mode, satellites are equipped with intelligent capabilities enabling real-time decision-making based on the latest conditions, while requiring minimal interaction with ground operators. Traditional scheduling approaches typically rely on mathematical models to represent satellite mission and resource management. Then, this problem is solved by using optimization algorithms. However, such solutions become less effective when the underlying models are not available, over complex, and inaccurate due to dynamic changes and uncertainties inherent in the space mission environment. A promising alternative is to reformulate the problem as a sequential decision-making process and apply model-free reinforcement learning techniques to enable adaptive and real-time resource management. To this end, we propose a novel transformer-based architecture tailored for heterogeneous satellite cluster autonomous EO Mission with relational observations-actions tokenization and differential attention mechanism. Our experimental results demonstrate significant performance improvements compared to the available baselines. Moreover, the proposed architecture exhibits strong adaptability and transferability with respect to varying numbers of satellite clusters.

---


### 163. [From Statistics to Individuals: An Exploration of Zoomable Empathic Visualizations](https://arxiv.org/abs/2605.31026)

**<font color=#1a73e8>作者：</font>** Edwige Chauvergne, Arnaud Prouzeau, Martin Hachet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Data visualization is a powerful tool for conveying statistical information, but when representing populations, it tends to hide individuals. We introduce Zoomable Empathic Visualizations (ZEVs), interactive experiences allowing users to smoothly navigate between abstract statistical visualizations and more qualitative, relatable representations focused on individuals. We present three use cases of ZEVs and report on a qualitative user study that highlights opportunities for deeper understanding and emotional engagement, while pointing to areas for improvement and further refinement. In summary, ZEVs point toward new approaches for revealing the individuals behind the data.

---


### 164. [Multi-Scale Separable Fourier Neural Networks for Solving High-Frequency PDEs](https://arxiv.org/abs/2605.31027)

**<font color=#1a73e8>作者：</font>** Qihong Yang, Qiaolin He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a novel neural network architecture, termed Multi-Scale Separable Fourier Neural Networks (MS-SFNN), for the accurate and efficient solution of linear and nonlinear high-frequency partial differential equations (PDEs). MS-SFNN exploits a separable representation: given a $d$-dimensional input, it employs $d$ independent subnetworks -- each acting on a single coordinate -- and constructs basis functions via element-wise multiplication of their outputs. The PDE solution is approximated as a linear combination of these basis functions, with coefficients determined by least squares. Critically, all network weights and biases are randomly initialized once, from a uniform distribution with unit variance, and remain fixed thereafter. To enhance expressivity, a tunable scaling factor is introduced in each subnetwork to modulate the frequency content of the resulting basis functions. Fourier features are explicitly embedded through cosine activations, endowing the method with strong spectral approximation capabilities. To mitigate the memory bottleneck associated with dense collocation in high-frequency or three-dimensional problems, we replace automatic differentiation with analytically derived basis function derivatives and develop a memory-efficient batched QR decomposition algorithm for solving large-scale least-squares systems. Numerical experiments demonstrate that MS-SFNN achieves unprecedented accuracy across a range of challenging PDEs, significantly outperforming state-of-the-art methods such as Physics-Informed Neural Networks (PINN) and Separated-Variable Spectral Neural Networks (SV-SNN).

---


### 165. [PEEK: Picking Essential frames via Efficient Knowledge distillation](https://arxiv.org/abs/2605.31029)

**<font color=#1a73e8>作者：</font>** Killian Steunou, Anas Filali Razzouki, Khalil Guetari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-language models can process only a limited number of frames, making frame selection a key bottleneck for efficient video captioning. Most captioning pipelines still rely on uniform sampling, which is computationally cheap but agnostic to visual content. Adaptive frame sampling has recently emerged as a promising approach for selecting the most informative frames from a video; however, existing methods remain computationally expensive. We introduce PEEK, an efficient dynamic frame sampling method that distills caption-conditioned frame relevance rankings from a stronger teacher model into a lightweight temporal model that operates only on visual content. We find that, overall, on ActivityNet Captions and MSR-VTT, our method outperforms state-of-the-art methods across all evaluated downstream vision language models, especially when only one or two frames are selected for captioning, obtaining the best CIDEr for most frame budgets. On ActivityNet Captions, PEEK is particularly strong, winning 14 out of 16 configurations. Zero-shot evaluation on MSR-VTT shows that our model transfers best at low frame budgets, while results at four and eight frames are more mixed as temporal coverage and visual diversity become increasingly competitive. Compared with recent adaptive baselines, PEEK is both more accurate in the low-budget regime and more efficient: it adds only $5.2\%$ to the captioning time, compared with $65.4\%$ for CSTA and $211.9\%$ for MaxInfo. We release our code and pre-trained checkpoint at this https URL.

---


### 166. [GraphARC: A Comprehensive Benchmark for Graph-Based Abstract Reasoning](https://arxiv.org/abs/2605.31031)

**<font color=#1a73e8>作者：</font>** Saku Peltonen, August Bøgh Rønberg, Andreas Plesner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Relational reasoning lies at the heart of intelligence, but existing benchmarks are typically confined to formats such as grids or text. We introduce GraphARC, a benchmark for abstract reasoning on graph-structured data. GraphARC generalizes the few-shot transformation learning paradigm of the Abstraction and Reasoning Corpus (ARC). Each task requires inferring a transformation rule from a few input-output pairs and applying it to a new test graph, covering local, global, and hierarchical graph transformations. Unlike grid-based ARC, GraphARC instances can be generated at scale across diverse graph families and sizes, enabling systematic evaluation of generalization abilities. We evaluate state-of-the-art language models on GraphARC and observe clear limitations. Models can answer questions about graph properties but often fail to solve the full graph transformation task, revealing a comprehension-execution gap. Performance further degrades on larger instances, exposing scaling barriers. More broadly, by combining aspects of node classification, link prediction, and graph generation within a single framework, GraphARC provides a promising testbed for future graph foundation models.

---


### 167. [SlotMemory: Object-Centric KV Memory for Streaming Long-Video Generation](https://arxiv.org/abs/2605.31033)

**<font color=#1a73e8>作者：</font>** Weijia Dou, Hui Li, Jiahao Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video generation models typically rely on temporal-centric memory, which organizes historical context as raw frames, chunk segments, or unclustered tokens. This organization frequently leads to identity drift and semantic inconsistency when entities exit the frame or during interactive prompt transitions. To address these limitations, we propose SlotMemory, an object-centric Key-Value memory mechanism for streaming video diffusion. Our approach shifts the memory abstraction from "when" an event occurred to "what" is being represented by decomposing the transformer's key-value manifold into discrete, reusable semantic slots. By utilizing these slots as routing addresses to index and store high-fidelity key-value tokens, we enable entity-level persistence and prompt-aware retrieval across long horizons. Evaluated on 60-second interactive narratives using the Wan2.1-T2V-1.3B backbone, SlotMemory achieves a state-of-the-art quality score of 81.61 and a 22.8 percent relative improvement in dynamic consistency over the strongest existing streaming baseline. Our results demonstrate that structured semantic representation, rather than raw temporal capacity, is the essential primitive for persistent long-form video synthesis. Our codes and checkpoints are available at this https URL.

---


### 168. [Annealed Softmax Greedy in Many-Armed Bayesian Bandits](https://arxiv.org/abs/2605.31034)

**<font color=#1a73e8>作者：</font>** William Overman, Mohsen Bayati  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) and group-based policy optimization methods such as GRPO update a stochastic policy by sampling multiple completions per prompt and increasing the policy's probability on those with higher reward, regularized by a KL penalty toward a reference policy. These updates do not include explicit mechanisms that track epistemic uncertainty. This paper studies a stylized explanation for why such uncertainty-agnostic updates can nevertheless be effective. We analyze an annealed softmax (Boltzmann) policy that selects actions according to a softmax of empirical mean rewards in a many-armed Bayesian Bernoulli bandit. Under a linear upper-tail condition on the prior (the $\beta=1$ case of $\beta$-regularity), which implies an abundance of near-optimal arms, we prove that annealed softmax greedy achieves Bayes regret $\tilde{O}(m + T/m)$, and in particular $\tilde{O}(\sqrt{T})$ when the number of arms scales as $m = \Theta(\sqrt{T})$. This is the near-optimal Bayes regret rate in this regime, attained also by empirical-mean greedy. Under $\beta$-regularity, many arms maintain empirical means close to the optimum throughout learning, so when softmax samples an arm other than the empirically best, that arm tends to be another near-optimal one rather than a clearly inferior one. By contrast, with a small number of arms, the same kind of softmax policy can suffer linear regret. The result also provides a structural analogy to RLVR, where a base policy with a non-negligible probability of producing a correct completion plays the role of $\beta$-regularity.

---


### 169. [GGT-100K: Generative Ground Truth for Generalizable Real-World Image Restoration](https://arxiv.org/abs/2605.31039)

**<font color=#1a73e8>作者：</font>** Xiangtao Kong, Jixin Zhao, Lingchen Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world image restoration (IR) is bottlenecked by the scarcity of high-quality paired training data. Synthetic datasets are abundant but often fail to model real-world degradations, while real-world paired datasets are expensive and difficult to capture. As a result, IR models trained on these datasets show limited generalization in real-world scenarios. In this work, we propose Generative Ground Truth (GGT) by using generative multimodal foundation models (MFMs) to produce high-quality (HQ) targets from real-world low-quality (LQ) images. We first conduct a systematic evaluation of nine state-of-the-art MFMs, including Nano-Banana-2 and GPT-Image-2, on images of various scenes and degradation types. The results demonstrate that Nano-Banana-2 with VLM-based adaptive prompting shows the highest capability to synthesize perceptually realistic and content-faithful HQ targets, which can serve as the GGT for the LQ input. We then employ Nano-Banana-2 to build a GGT synthesis pipeline, which involves multi-stage quality control to ensure data reliability, and construct GGT-100K, an LQ-HQ paired dataset comprising 103,707 training pairs and covering diverse scenes and complex real-world degradations. A test set of 500 image pairs is also established. Extensive experiments show that GGT-100K consistently improves the real-world generalization of a wide range of IR models, with particularly strong benefits for finetuning generative models for IR tasks. Our results suggest that MFMs can serve as practical tools for restoration-oriented data generation, and GGT-100K is a useful resource to expand the generalization boundaries of real-world IR models.

---


### 170. [UniRTL: Unifying Code and Graph for Robust RTL Representation Learning](https://arxiv.org/abs/2605.31040)

**<font color=#1a73e8>作者：</font>** Yi Liu, Hongji Zhang, Lei Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Developing effective representations for register transfer level (RTL) designs is crucial for accelerating the hardware design workflow. Existing approaches, however, typically rely on a single data modality, either the RTL code or its associated graph-based representation, limiting the expressiveness and generalization ability of the learned representations. For RTL, the control data flow graph (CDFG) offers a comprehensive structural representation that preserves complete information, while the code modality explicitly encodes semantic and functional information. We argue that integrating these complementary modalities is essential for a thorough understanding of RTL designs. To this end, we propose UniRTL, a multimodal pretraining framework that learns unified RTL representations by jointly leveraging code and CDFG. UniRTL achieves fine-grained alignment between code and graph through mutual masked modeling and employs a hierarchical training strategy that incorporates a pretrained graph-aware tokenizer and staged alignment of text (i.e., functional summary) and code prior to graph integration. We evaluate UniRTL on two downstream tasks, performance prediction and code retrieval, under multiple settings. Experimental results show that UniRTL consistently outperforms prior methods, establishing it as a more robust and powerful foundation for advancing hardware design automation.

---


### 171. [Does Visual Information Play a Decisive Role in Vision-Language-Action Model Driving Behavior?](https://arxiv.org/abs/2605.31041)

**<font color=#1a73e8>作者：</font>** Jingtao He, Hongliang Lu, Xiaoyun Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have demonstrated promising capability in autonomous driving, highlighting the potential of unified multimodal architectures for jointly modeling perception and planning. However, how current VLA-based driving behavior is grounded in visual information remains poorly understood. Existing evaluation protocols mainly focus on aggregate performance metrics, lacking structured and practical diagnostics to quantify visual-behavior dependency. In this work, we introduce a structured multi-level visual perturbation framework to analyze visual-behavior dependency in VLA-based driving models systematically. The framework organizes controlled visual perturbations along three complementary dimensions: channellevel degradation, information-level disruption, and structurelevel modification. We apply it to VLA-based driving systems and evaluate behavioral responses under both open-loop trajectory prediction and interactive closed-loop safety evaluation. Experimental results reveal evaluation-dependent dependency patterns and uneven visual grounding across abstraction levels. These findings call for more structured analyses and principled design of VLA driving models to better understand how visual information shapes behavior and develop safer, more robust systems.

---


### 172. [The Challenges of Using Reinforcement Learning for Controlling Industrial Energy Systems](https://arxiv.org/abs/2605.31044)

**<font color=#1a73e8>作者：</font>** Tobias Lademann, Théo Vincent, Jan Peters 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has shown promising results for optimizing the control of industrial energy systems, yet most existing studies remain limited to the application in simulation environments. We investigate the challenges of deploying reinforcement learning in a real-world industrial energy system, considering a thermal heating network as a use case. We formulate the task as a Markov Decision Process and systematically analyze the associated challenges along the structure of the formal description, including partial observability, action space design, reward design, and the simulation-to-reality gap. The challenges are grounded in an existing real-world deployment, where reinforcement learning achieves operational stability but shows a significant performance gap compared to simulation.

---


### 173. [Rethinking Efficient Crack Segmentation with Task-Aligned Structural-Directional Modeling](https://arxiv.org/abs/2605.31048)

**<font color=#1a73e8>作者：</font>** Shipeng Liu, Liang Zhao, Dengfeng Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent crack segmentation methods often follow generic semantic segmentation designs, using stronger backbones, hybrid CNN-Transformer-Mamba encoders, and auxiliary enhancement branches. Although effective, this raises whether stronger generic feature mixing is the most suitable direction for crack segmentation. We instead formulate crack segmentation as sparse structural recovery. Cracks have limited category-level semantics but strong morphological regularities, being thin, sparse, anisotropic, locally fragmented, and easily confused with textures or shadows. Thus, the key bottleneck lies in preserving weak structural evidence, recovering directional continuity, and suppressing background coupling. We propose RIFT, a compact family of morphology-aligned crack segmentation models. Rather than compressing a complex generic architecture, RIFT is simple by design, preserving local evidence, aggregating cooperative directional continuity, and restoring crack structures through lightweight multi-scale fusion. Experiments on four public benchmarks show that RIFT achieves the best or tied-best results across the 16 main metrics against reproduced representative baselines. RIFT-B gives the strongest overall accuracy, while RIFT-T provides the best deployment efficiency with only 0.47M parameters and high inference speed. Topology-aware evaluation, ablations, transfer experiments, and visualizations further verify that task-aligned simplicity can match or surpass complex hybrid architectures when its inductive bias fits crack morphology. Code: this https URL

---


### 174. [Learning to Solve and Optimize by Evolving Code](https://arxiv.org/abs/2605.31049)

**<font color=#1a73e8>作者：</font>** Veronika Semmelrock, Benedetta Strizzolo, Francesco Zuccato 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Combinatorial and optimization problems are fundamental to many industrial AI applications. Solving large-scale real-world instances of such problems typically requires careful problem formalization, specialized solvers, and expert-designed heuristics. Thus, experts need to specify not only what solutions are, but also how they are derived. By introducing the tool CHECKMATE, we show that algorithm generation via code evolution represents a paradigm shift by eliminating the need to formulate the how. CHECKMATE solely relies on the what. Specifically, a formal specification ensures solutions' correctness and enables systematic performance evaluation of the generated programs, while a natural language description guides the evolutionary process. The effectiveness of our method is demonstrated on selected problems from two industrial domains: configuration and scheduling. In all cases, the evolved algorithms consistently outperform state-of-the-art solvers. This underscores the potential of formal methods in guiding code evolution for automatically solving complex real-world problems.

---


### 175. [LVSA: Training-Free Sparse Attention for Long Video Diffusion](https://arxiv.org/abs/2605.31057)

**<font color=#1a73e8>作者：</font>** Gael Glorian, Ioannis Lamprou, Zhen Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense self-attention is the compute and quality bottleneck of long-video diffusion inference: cost grows quadratically with the sequence length, and beyond the training horizon the model converges to near-static output, that is, "frozen" repetitive video. State of the art approaches are either too costly, e.g., they require retraining, or fail to satisfy both performance and quality objectives in a scalable manner. To this end, we introduce Long Video Sparse Attention (LVSA), a training-free model-agnostic block-sparse attention for video diffusion transformers that combines a structured window pattern with rotating global anchors, thus removing the fixed-grid bias which causes long-range temporal artifacts. LVSA, combined with a FlashInfer kernel, reduces compute up to 3.17x on Wan 2.1 1.3B at a 6x horizon, 2.98x on Wan 2.1 14B at a 6x horizon, and 3.33x on HunyuanVideo 1.5 at a 1.5x horizon, compared to dense attention. Beyond reducing compute, LVSA enables HunyuanVideo 1.5 generation at a 2x horizon, which is otherwise out-of-memory on a single GPU. Moreover, LVSA provides speedups up to 2.41x compared to RIFLEx and 3.27x compared to UltraViCo on Wan 2.1 1.3B. To demonstrate applicability across diverse platforms, we apply LVSA on NPUs and achieve speedups up to 2.71x on Wan 2.2 A14B and 3.24x on Wan 2.1 1.3B compared to dense attention. To evaluate quality in a fair way, we introduce VQeval, a tool properly scoring loopy video failures, which instead are rewarded in state of the art evaluators like VBench-Long. LVSA is quality-neutral for generation at training horizon length and quality-positive at extended lengths.

---


### 176. [Combinatorial Synthesis: Scaling Code RLVR via Atomic Decomposition and Recombination](https://arxiv.org/abs/2605.31058)

**<font color=#1a73e8>作者：</font>** Jiasheng Zheng, Boxi Cao, Boxi Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has recently emerged as the cornerstone for shaping the remarkable coding abilities of Large Language Models (LLMs). However, the scalability of RLVR is severely constrained by the scarcity of sufficiently challenging verifiable code tasks that target near the model's edge of competence. Prior studies often rely on heuristic seed expansions for data synthesis, which severely limits both novelty and difficulty. Consequently, the training value of such data fails to scale proportionally with the size of its synthesis. To this end, we propose Atomic Decomposition and Recombination (ADR), a novel framework that generates verifiable code tasks via decomposition into atomic elements and controlled recombination, thereby enabling the generation of genuinely novel and challenging verifiable code tasks. Experiments and analysis demonstrate that ADR achieves superior originality, difficulty, diversity, and test quality over existing baselines, and consistently delivers greater improvements in code ability across RLVR in diverse downstream domains, including algorithmic programming, tool usage, and data science. Our work sheds light on a new paradigm for novel code task synthesis and scalable RLVR training.

---


### 177. [STEP: Learning STructured Embeddings for Progressive Time Series](https://arxiv.org/abs/2605.31061)

**<font color=#1a73e8>作者：</font>** Lucas Thil, Jesse Read, Rim Kaddah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a novel method for learning interpretable representations of progressive time series, that is, data capturing irreversible state transitions such as degradation or task completion. Our approach uses a self-supervised contrastive objective to learn a low-dimensional latent space whose geometry is itself the interpretation: each observation becomes a point on a manifold anchored between two fixed orthogonal prototype vectors, and a trajectory becomes a path across that manifold. From this structure we read a latent compass, the polar coordinates ({\theta}, r) of the latent vector, in which {\theta} tracks the progression of the underlying state (e.g., from healthy to failed) and r identifies the active mode (e.g., the operating condition), without any proxy labels. We evaluate the approach against the state of the art on diverse domains, including industrial degradation, robotic tasks, and neural activity, validating three key capabilities: (1) end-state prediction, (2) multi-step forecasting, and (3) interpretable phase separation. Our method matches or improves over black-box counterparts on all of these while providing transparency about the underlying mechanisms. A simple linear regressor on top of the latent compass coordinates is competitive with deep architectures, direct quantitative evidence that the underlying state is encoded in a geometrically accessible form.

---


### 178. [HQ-JEPA: Hybrid Quantum Joint-Embedding Predictive Architecture for Cross-Modal Remote Sensing Representation Learning](https://arxiv.org/abs/2605.31068)

**<font color=#1a73e8>作者：</font>** Md Aminur Hossain, Ayush V. Patel, Sanjay K. Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce HQ-JEPA, a hybrid quantum-classical joint-embedding predictive architecture for cross-modal remote sensing representation learning. The proposed framework extends JEPA-style masked latent prediction to paired Sentinel-1 and Sentinel-2 imagery by predicting masked target representations from visible context regions while aligning heterogeneous modality features in a shared embedding space. To improve representation quality, HQ-JEPA combines four complementary objectives: latent token prediction, cross-modal token alignment, SIGReg-based Gaussian regularization in the fused latent space, and a differentiable SWAP-test-based Fidelity Quantum Similarity (FQS) loss. Unlike pixel reconstruction methods, HQ-JEPA learns semantic representations directly in latent space and uses quantum state-overlap-based similarity as an additional regularization signal. We evaluate the pretrained encoder on GeoBench classification and segmentation tasks under linear probing and fine-tuning settings. Results show that HQ-JEPA achieves competitive and often superior performance over strong self-supervised and remote sensing foundation-model baselines, demonstrating the benefit of integrating predictive self-supervision, cross-modal geometric regularization, and quantum fidelity-based representation learning for remote sensing applications.

---


### 179. [Learning to Bid in FCR Markets: A Best-of-Both-Worlds Approach](https://arxiv.org/abs/2605.31070)

**<font color=#1a73e8>作者：</font>** Marius Potfer, Cheng Wan, Pierre Gruet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bidding in the European Frequency Containment Reserve (FCR) market is challenging for flexibility providers because competing offers are hidden and bidders observe only partial feedback form the market, such as, clearing price and awarded quantity. For a participant active in a single country, we show that the multi-country FCR clearing problem can be recast as a repeated multi-unit uniform-price auction against an endogenous vector of opposing bids. This reformulation yields an online learning problem and allows us to adapt a Best-of-Both-Worlds combinatorial semi-bandit algorithm implementable from this standard market feedback. The resulting bidder achieves logarithmic pseudo-regret in stochastic environments and $\mathcal{O}(\sqrt{T})$ regret in adversarial ones. Synthetic experiments confirm the expected scaling, and backtests on historical European FCR data show competitive performance in practice: the method performs especially well on stable products, while EXP3-type baselines can be safer under stronger non-stationarity. Overall, the results show that learning-based bidding in FCR markets is theoretically grounded and practically useful when the learning rule matches product-level market stability.

---


### 180. [On Revisiting Entropy for Identifying Mislabeled Images](https://arxiv.org/abs/2605.31090)

**<font color=#1a73e8>作者：</font>** Chunlei Li, Zixuan Zheng, Yilei Shi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mislabeled samples in training datasets severely degrade the performance of deep networks, as overparameterized models tend to memorize erroneous labels. We address this challenge by proposing a novel approach for mislabeled data detection that leverages training dynamics. Our method is grounded in the key observation that correctly labeled samples exhibit consistent entropy decrease during training, while mislabeled samples maintain relatively high entropy throughout the training process. Building on this insight, we introduce a signed entropy integral (SEI) statistic that captures both the magnitude and temporal trend of prediction entropy across training epochs. SEI is broadly applicable to classification networks and demonstrates particular effectiveness when integrated with contrastive language-image pretraining (CLIP) architectures. Through extensive experiments on four medical imaging datasets -- a domain particularly susceptible to labeling errors due to diagnostic complexity -- spanning diverse modalities and pathologies, we demonstrate that SEI achieves state-of-the-art performance in mislabeled data identification, outperforming existing methods while maintaining computational efficiency and implementation simplicity. Our code is available at this https URL.

---


### 181. [Cross-Modal Clinical Knowledge Integration for Mammography Report Generation](https://arxiv.org/abs/2605.31093)

**<font color=#1a73e8>作者：</font>** Jiayi Zhu, Fuxiang Huang, Yu Xie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast cancer is a major global health concern, and mammography screening plays a central role in early detection. The large volume of screening examinations creates a substantial workload for radiologists, making accurate and consistent report generation a critical clinical challenge. Existing automated mammography report generation methods primarily focus on direct visual-to-text mapping, while overlooking the structured clinical reasoning process followed by radiologists in real-world practice. To address this limitation, we propose MammoRG, a mammography report generation framework that explicitly simulates the clinical reporting workflow by following the BI-RADS guideline and incorporating prior clinical knowledge to produce diagnostic reports. Specifically, MammoRG adopts a two-stage training framework. In the first stage, the model learns to integrate clinically relevant prior knowledge from a patient's four-view mammograms through classification-based supervision. In the second stage, a terminology-aware supervised fine-tuning strategy is introduced to model mammography-specific clinical terms as atomic semantic units, enabling the generation of high-quality reports with improved clinical consistency. To facilitate clinical efficacy evaluation of generated reports, we further develop MammoRGTool, a dedicated mammography report parsing tool that extracts structured clinical information from free-text reports. Extensive experiments demonstrate that MammoRG consistently outperforms existing methods across multiple clinical efficacy metrics, particularly in diagnosis-related BI-RADS F1, where it surpasses the second-best model by 2.73%, 2.04%, 1.90%, and 3.27% on the internal, external 1, external 2, and VinDr-Mammo datasets, respectively.

---


### 182. [Redefining Instance Matching: A Unified Framework for Part-Aware Matching in Panoptic Segmentation Evaluation](https://arxiv.org/abs/2605.31094)

**<font color=#1a73e8>作者：</font>** Erik Großkopf, Soumya Snigdha Kundu, Hendrik Möller 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Panoptic Quality (PQ) metric is the standard for jointly evaluating instance and semantic segmentation. However, its original definition relies on a One-to-One matching between predicted and ground truth segments, which is only straightforward when the IoU threshold exceeds 0.5. Below 0.5, multiple matching strategies emerge in a poorly explored problem space. We systematically elucidate this space by recasting segment matching as a constrained bipartite assignment problem. Independently bounding the prediction- and ground-truth-side degrees yields four matching strategies: One-to-One, Many-to-One, One-to-Many, and Many-to-Many. We show that the first three are well-defined within the PQ framework, while Many-to-Many falls outside it. These strategies become relevant when instances are fragmented, adjacent objects are difficult to delineate, or annotations are noisy. Central to our framework is a vertex-based accounting of TP, FN, and FP, anchored to ground truth and predicted segments rather than to matching edges. We further show that the framework extends naturally to part-aware panoptic segmentation, and we explore part-aware evaluation on biomedical data. Across configurable case studies we report how different combinations of thresholds and matching strategies behave in practice. We release a unified open-source package built on Panoptica. It exposes Voronoi-based region-wise analysis, part-aware evaluation, and Area Under Threshold Curve computations as configurable options.

---


### 183. [KnowledgeGain: Evaluating and Optimizing Science News Generation for Reader Learning](https://arxiv.org/abs/2605.31099)

**<font color=#1a73e8>作者：</font>** Dominik Soós, Meng Jiang, Jian Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Science news is an important medium to communicate discoveries between the research communities and the public. Yet, most metrics for generated or summarized text evaluate semantic similarity and factual consistency, but do not measure how much knowledge readers learn from the news. We introduce KnowledgeGain, a metric that evaluates the quality of science news by measuring how much knowledge readers gained after reading it. To evaluate the metric, we first performed a controlled human study and showed that the metric successfully captures the differential knowledge gained by human readers reading different types of science media. The data allowed us to calibrate a prompt-only LLM reader simulator. We use it to rank and filter candidate articles before human evaluation. A second human study shows that articles selected with this simulator improve post-reading accuracy and normalized KnowledgeGain over a strong generation baseline. Our work is a step toward generating science news that better meets the knowledge and comprehension goals of Bloom's Taxonomy.

---


### 184. [Vector Linking via Cross-Model Local Isometric Consistency](https://arxiv.org/abs/2605.31100)

**<font color=#1a73e8>作者：</font>** Ziying Chen, Yang Cao, He Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study Vector Linking: given two embedding clouds produced by different black-box encoders over partially overlapping datasets, recover cross-model object correspondences using only vectors. Empirically and theoretically, we show that independently trained contrastive encoders exhibit local geometric consistency: short-range distances are approximately preserved up to a scale factor, while long-range distances are not due to model-specific distortion. Building on this, we propose an iterative, reference-based geometric embedding hashing that recovers vector links from a tiny seed set of paired anchors. It represents each vector by distances to sampled paired anchors, proposes candidate links via hash-space matching, and aggregates evidence across views in a Beta-Bernoulli posterior to bootstrap high-confidence links as new anchors. Experiments across multiple benchmarks and embedding model pairs demonstrate accurate and robust linking under varying overlap, seed budgets, and out-of-domain anchors, with applications to vector database integration and cross-model clustering. Code is available at this https URL.

---


### 185. [Extending the UXR Point of View Playbook: Triangulating Insights in Complex Developer Domains](https://arxiv.org/abs/2605.31104)

**<font color=#1a73e8>作者：</font>** Sarah Kianfar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As User Experience Research (UXR) matures, practitioners face the challenge of moving beyond data collection toward establishing a compelling Point of View (POV) that drives strategic impact. This paper proposes an extension to the UXR POV Playbook, specifically focusing on the transition from the "Insight Generation" layer to the "POV" layer. Drawing on extensive multi-method research in Cloud Developer Tools, spanning AI Agents, Command Line Interfaces (CLI), and Error Messages, we demonstrate how triangulating qualitative and quantitative data facilitates the creation of high-confidence POVs. We introduce three new "Playbook Cards" derived from this research: The Paradigm Shift, Explainability as Trust, and The Cost of Friction. These cards provide a structured mechanism for researchers to translate complex technical findings into irrefutable business narratives.

---


### 186. [Riemannian Diffusion Models on General Manifolds via Physics-Informed Neural Networks](https://arxiv.org/abs/2605.31106)

**<font color=#1a73e8>作者：</font>** Gyeonghoon Ko, Juho Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Riemannian diffusion models generalize score-based generative modeling to manifold-supported data via stochastic diffusion equations on the manifold. However, training requires sampling from and differentiating the manifold heat kernel, which is rarely available in closed form beyond a few highly symmetric manifolds. We propose a general approach that approximates the heat kernel by directly solving the manifold heat equation with a physics-informed neural network (PINN). Given an explicit manifold specification, we choose a coordinate system, derive the corresponding heat (Fokker--Planck) equation and a short-time asymptotic approximation, and then train a PINN to learn the log heat kernel. The resulting surrogate enables both forward noising (heat-kernel sampling) and conditional-score evaluation for denoising score matching. We demonstrate the method on diverse manifolds including $S^2$, $SO(3)$, $\mathrm{SPD}(n)$, and permutation-quotiented point clouds.

---


### 187. [Remembering by Reconstructing: Domain Incremental Learning With Test-Time Training on Video Streams](https://arxiv.org/abs/2605.31108)

**<font color=#1a73e8>作者：</font>** Jonathan Swinnen, Tinne Tuytelaars  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work we introduce a novel approach to domain incremental learning, adapting models over time to evolving, non-stationary data. In contrast to other works, we do not attempt to avoid catastrophic forgetting, but rather allow it and exploit it. Our model combines a main task head with a self-supervised masked autoencoder (MAE) head. We then learn domain-specific LoRA adapters during incremental training. Each adapter specializes to its domain, naturally inducing forgetting on other domains in both heads. At inference, we perform online test-time training on the self-supervised MAE head to identify which LoRAs best matches the current input, so the model can `remember' the domain again. Our scheme is especially well-suited to real-world streaming data, such as video, where consecutive samples are highly correlated and domain shifts are gradual. We demonstrate our method on domain-incremental action recognition and semantic segmentation tasks.

---


### 188. [Polyphony: Diffusion-based Dual-Hand Action Segmentation with Alternating Vision Transformer and Semantic Conditioning](https://arxiv.org/abs/2605.31115)

**<font color=#1a73e8>作者：</font>** Hao Zheng, Hu Wang, Tiantian Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dual-hand action segmentation, densely predicting actions for both hands from untrimmed videos, is essential for understanding complex bimanual activities. However, it poses several unique challenges: complex inter-hand dependencies, visual asymmetry between hands, representation conflicts where the dominant hand monopolizes gradients, and semantic ambiguity in fine-grained actions. We propose Polyphony, a three-stage method to address these challenges through: (1) an Alternating Dual-Hand Vision Transformer that alternates training between left- and right-hand mini-batches to ensure balanced gradient contributions from both hands while sharing a spatio-temporal encoder; (2) Semantic Feature Conditioning that aligns visual features with structured, compositional action descriptions to enhance discrimination of semantically similar actions; and (3) Diffusion-Based Segmentation with cross-hand feature fusion for inter-hand coordination and adaptive loss weighting for balancing performance. Polyphony achieves state-of-the-art on both dual-hand datasets (HA-ViD, ATTACH) with improvements up to 16.8 points, and on the single-stream Breakfast dataset (82.5%), outperforming the prior best method that uses a 12x larger backbone. Notably, our unified model with a single shared backbone surpasses baselines requiring separate per-hand models. Code is at this https URL.

---


### 189. [NTR: Neural Token Reconstruction for Scene Token Bottleneck in End-to-End Driving](https://arxiv.org/abs/2605.31116)

**<font color=#1a73e8>作者：</font>** Jiahui Li, Jiawei Sun, Zixiang Ren 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent perception-free end-to-end (E2E) autonomous driving methods bypass explicit perception outputs by compressing dense image patch tokens into compact scene tokens for downstream trajectory generation and scoring. While these scene tokens form a compact visual bottleneck for the planner, they receive supervision solely from the planning objective, providing limited constraints on the encoded visual information. To address this limitation, we introduce Neural Token Reconstruction (NTR), a representation learning framework to directly constrain the compact scene-token bottleneck in perception-free driving. NTR introduces a self-distillation masked latent reconstruction objective that reconstructs masked patch-level latent features using only compact scene tokens as reconstruction memory. This forces reconstruction gradients to pass exclusively through the scene-token bottleneck, encouraging scene tokens to preserve richer and less redundant visual representations for planning. We further introduce semantic priors derived from foundation-model annotations as a weak semantic interface biasing reconstruction targets toward driving-related structures without introducing explicit perception heads. All auxiliary reconstruction components are removed at inference time, leaving the deployed planner unchanged. NTR achieves state-of-the-art performance on three public autonomous driving benchmarks, including 8.0461 RFS on Waymo E2E and 94.1 PDMS / 90.9 EPDMS on NavSim1&2. The learned scene tokens exhibit lower pairwise redundancy and higher effective rank, indicating that effective bottleneck supervision improves both compact visual representation learning and planning performance.

---


### 190. [Generative AI in developing User Experience Research Point of View: A NotebookLM case study](https://arxiv.org/abs/2605.31125)

**<font color=#1a73e8>作者：</font>** Mona Giff, Stephen Giff, Huseyin Dogan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> User Experience Research (UXR) is currently undergoing a transition from traditional usability testing towards design-led and data-driven approaches, yet it faces an identity crisis due to a lack of methodological grounding in UXR and time-intensive methodologies which often lag behind product decision cycles. To address this, the UXR Point of View (PoV) framework formalises the UXR process by transitioning from raw data collection to forming an evidence-based PoV which drives strategic product impact. Furthermore, the use of GenAI in UXR has been investigated, but researchers often face increased work intensity when using GenAI, attributed to time spent on prompt engineering, data cleaning, and verification of AI outputs. This paper proposes and evaluates a formalised methodology for leveraging GenAI, specifically Google's NotebookLM, to augment the UXR PoV process. The methodology consists of five prompts across four stages: (1) leveraging the framework, (2) establishing roadmaps, (3) applying best-practices, and (4) crafting PoV narratives; and was tested on eleven UXR papers. Results showed that by using the proposed methodology, NotebookLM successfully leveraged the UXR PoV framework across all stages of PoV creation. These findings demonstrate that NotebookLM can serve as an effective collaborative partner in UXR, so long as it is provided with sufficient context and specific prompting.

---


### 191. [Not All Synthetic Data Is Yours to Learn From](https://arxiv.org/abs/2605.31126)

**<font color=#1a73e8>作者：</font>** Sina Alemohammad, Li Chen, Richard G. Baraniuk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can a language model improve from plain text sampled from itself, with no prompts, no teacher, no verifier, and no reward model? Yes, but only when the synthetic corpus is compatible with the student, a relational property of the source-student pair rather than an intrinsic property of the data. We call this the latent capability resurfacing hypothesis: weak self-training can amplify capabilities already present in the pretrained model, but only under this compatibility condition. We study this in the minimal setting of prompt-free unconditional self-training, where base language models are fine-tuned on text generated from the BOS token alone, with no task specification or external supervision. We report three findings. First, synthetic utility is relational rather than intrinsic: self-generated data is the most effective source, same-lineage transfer outperforms stronger but differently trained sources, and cross-family transfer is substantially weaker. Second, common intrinsic proxies fail: neither benchmark-level semantic similarity nor average per-token likelihood under the student predicts which corpora help. Third, this regime produces a surprising byproduct. In controlled Pythia experiments, capability and verbatim memorization decouple: benchmark utility is preserved or improved while held-out exact-match extraction drops by over 95 percent, with no forget set, privacy objective, or targeted unlearning. Together, these results suggest that prompt-free self-training works by amplifying what the student already knows, not by importing structure from the data. They also reveal a regime in which capability and verbatim memorization can be separated without any explicit unlearning objective.

---


### 192. [Scalable Bayesian Inference for Nonlinear Conservation Laws](https://arxiv.org/abs/2605.31127)

**<font color=#1a73e8>作者：</font>** Tim Weiland, Philipp Hennig  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonlinear conservation laws are at the heart of many of the most important dynamical systems in science and engineering. In practical applications, such systems are often subject to various sources of uncertainty, e.g. due to sparse or noisy measurements. Inferring physical quantities and fields of interest then becomes an ill-posed problem which both classical numerical methods and modern deep learning-based methods struggle to treat appropriately. Recent work has framed classical numerical methods as Bayesian inference under Gaussian process priors, resulting in a physics-aware treatment of uncertainties. Following this line of work, we develop a novel numerically conservative method for uncertainty-aware simulations of nonlinear conservation laws. We use recent sparse approximation techniques to scale up to large-scale forward and inverse problems. For forward simulation, we inherit the accuracy of classical solvers while providing structured uncertainty quantification. On inverse problems, we recover posteriors over nonparametric source fields in seconds -- outperforming neural baselines that take minutes to produce a less accurate point estimate.

---


### 193. [Generalizing Multi-Scale Time-Series Modeling with a Single Operator](https://arxiv.org/abs/2605.31129)

**<font color=#1a73e8>作者：</font>** Cheonwoo Lee, Dooho Lee, Doyun Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-scale modeling has emerged as an effective design principle for time-series forecasting by capturing temporal dynamics at multiple resolutions. As no principled foundation has been established in the literature, we unify existing scaling methods into a scaling operator family, revealing a fundamental limitation of existing approaches: reliance on fixed and discrete scaling. To address this limitation, we propose SiGMA (Single Generalized Multi-scale Architecture), which enables distance-aware scaling via the learnable discrete Gaussian (LDG) kernel grounded in scale-space theory. We evaluate SiGMA comprehensively on long- and short-term forecasting benchmarks against state-of-the-art multi-scale baselines. SiGMA outperforms all competitors on both tasks, especially achieving the best performance in 13 out of 16 long-term evaluation settings. Beyond accuracy, SiGMA significantly improves training speed by up to 5.3 times and reduces memory consumption by up to 3.8 times over the strongest competitors. Code is available at this https URL.

---


### 194. [UXR PoV for Neuroinclusive Emotion Regulation](https://arxiv.org/abs/2605.31131)

**<font color=#1a73e8>作者：</font>** Melike Akca, Mona Giff, Deniz Cetinkaya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Attention-deficit/hyperactivity disorder (ADHD) is a psychiatric disorder which presents itself in individuals through patterns of developmentally inappropriate levels of inattentiveness, hyperactivity, and impulsivity, with difficulties in decision making and emotional regulation (ER). Although digital and AI-based interventions have expanded access to ER support, many existing systems remain limited by weak theoretical integration, insufficient accommodation of neurodiversity, and a lack of structured user experience research (UXR) methodologies, that bridge psychological insight with design practice. This paper introduces a Generative AI-augmented UXR methodology, grounded in the UXR Point of View (PoV) Playbook, to support the design of emotionally intelligent and Neuroinclusive digital ER interventions for adults with ADHD. The approach integrates empirical evidence with established psychological frameworks Dialectical Behaviour Therapy (DBT), Self-Determination Theory (SDT), and the COM-B behavioural model and leverages Generative AI as a co-analytic tool to support synthesis, hypothesis formation, and design articulation. The methodology is operationalized through a four-stage UXR process encompassing AI-supported hypothesis generation, foundational planning, insight generation via Building Blocks, and the construction of stakeholder-specific PoV narratives. This process results in a set of ten theory informed UXR Play Cards that translate psychological mechanisms and empirical findings into actionable design guidance. The primary contribution of this work is a replicable, bias-aware framework for integrating Generative AI into UXR practice, advancing human-centred and Neuroinclusive approaches to digital mental health design.

---


### 195. [Multilingual and Cross-Lingual Citation Needed Detection on Wikipedia for Lower-Resource Languages](https://arxiv.org/abs/2605.31136)

**<font color=#1a73e8>作者：</font>** Gerrit Quaremba, Amy Rechkemmer, Elizabeth Black 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In automated fact-checking (AFC), check-worthiness detection identifies claims requiring verification based on domain-specific criteria. On Wikipedia, this task instantiates as Citation Needed Detection (CND), which flags claims lacking supporting citations. However, existing research has largely overlooked lower-resource languages, and recent AFC pipelines rely on large language models (LLMs), which are inaccessible to low-resource organizations. We introduce MCN, a multilingual CND corpus spanning 18 languages across three resource levels, on which we conduct an extensive study of small decoder-based language models (SLMs). Our experiments show that SLMs fine-tuned with an encoder-style objective substantially outperform prompted LLMs across languages. We further present one of the first studies on cross-lingual CND, demonstrating that SLMs fine-tuned solely on English claims surpass LLMs, even with little to no target-language adaptation. Our findings have important implications for lower-resource Wikipedia communities and suggest that compact, task-specific models are preferable to LLMs for CND. We release all data and code at this https URL

---


### 196. [PolSAR Image Classification using a Hybrid Complex-Valued Network (HybridCVNet)](https://arxiv.org/abs/2605.31137)

**<font color=#1a73e8>作者：</font>** Mohammed Q. Alkhatib  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, convolutional neural networks (CNNs) have become popular for image classification due to their effectiveness in computer vision tasks. Now, researchers are exploring the potential of vision transformers (ViTs) in remote sensing and Earth observation. However, traditional Real-Valued networks often overlook important phase information in Complex-Valued (CV) data like polarimetric synthetic aperture radar (PolSAR) data. To address this, new CV deep architectures have emerged. HybridCVNet, a novel hybrid network, blends CV-CNN and CV vision transformer (CV-ViT) techniques. It efficiently combines CV 3D and 2D CNNs as feature extractors, enhancing PolSAR image classification by extracting complementary information and effectively leveraging interdependencies within the data. Experimental results from widely-used PolSAR datasets show HybridCVNet outperforms other methods, achieving an overall accuracy of 97.39% on the Flevoland dataset and showing promise even with just a 1% sampling ratio, with a Kappa value of 0.972 on the San Francisco dataset. Source code is accessible through this https URL

---


### 197. [Developing an AI-Powered UX Research Point of View for Digital Health in A Regulatory Context: An Exemplar Case from MSM and Transgender HIV Care in Nigeria](https://arxiv.org/abs/2605.31138)

**<font color=#1a73e8>作者：</font>** Emmanuel Oluwatosin Oluokun, Festus Fatai Adedoyin, Huseyin Dogan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> User Experience Research (UXR) in a legal and regulatory contexts presents unique challenges that require specialised approaches to protect vulnerable populations whilst generating actionable insights. Digital consultation, appointment booking, and medication delivery platforms show promise for extending care access; however, their real-world effectiveness is curtailed by an absence of theoretically grounded user experience research (UXR) methodologies that adequately account for the psychosocial conditions of these populations. This paper introduces a Generative AI-augmented UXR methodology, grounded in the UXR Point of View (PoV) Playbook, to guide the design of psychologically safe, low-cognitive-load digital health interventions for MSM and transgender individuals living with HIV/AIDS in Nigeria. Drawing from empirical research involving co-design workshops, thematic analysis, and requirements engineering, the methodology is operationalised through a four-stage UXR process encompassing AI-supported hypothesis generation, foundational planning, insight generation via Building Blocks, and the construction of stakeholder-specific PoV narratives. This process results in ten theory-informed UXR Play Cards that translate psychological mechanisms and empirical findings into actionable design guidance. Each play contains actionable tasks, AI-augmented approaches, and ethical guardrails tailored for research with marginalised populations. The output is a set of ten theory-informed UXR Play Cards translating psychological insight and empirical evidence into actionable design guidance. The core contribution is a replicable, stigma-aware, and privacy-centred framework for responsible GenAI use in UXR practice, advancing human-centred digital health design for marginalised communities.

---


### 198. [On the Robustness of Multilingual Text Embedding Rankings Across Learning Tasks, Languages, and Benchmark Datasets](https://arxiv.org/abs/2605.31142)

**<font color=#1a73e8>作者：</font>** Ana Gjorgjevikj, Barbara Koroušić Seljak, Tome Eftimov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale multilingual text embedding models play crucial role in both research and industry, yet their behavior in language-specific, multi-task settings remains insufficiently understood. Although benchmarking platforms such as MTEB report results across more than 250 languages, conclusions about model superiority often depend on implicit choices of dataset compositions and performance aggregation methods. To address this gap, we present a meta-study of multilingual model performance robustness in MTEB, applying a diverse set of multi-criteria decision-making ranking schemes and introducing two robustness indicators: dataset-composition robustness (sensitivity of rankings to changing dataset compositions) and ranking-scheme robustness (sensitivity to aggregation method change). They enable systematic sensitivity analysis of whether benchmarking conclusions remain stable under different evaluation designs. We conduct an in-depth analysis on five languages (English, French, German, Hindi, and Spanish) across nine tasks (e.g., classification, clustering, retrieval) and release results for approximately 230 additional languages. The task-specific analyses show that large-scale LLM-based models are often robust top performers, though not uniformly (e.g., in retrieval task), while task-agnostic results reveal that only a small subset of models remains consistently strong across tasks, ranking schemes, and data subsamples.

---


### 199. [Extending the UXR Point of View Pyramid: A Generative AI-Augmented Methodology for Human-Centred AI Systems](https://arxiv.org/abs/2605.31143)

**<font color=#1a73e8>作者：</font>** Festus Fatai Adedoyin, Huseyin Dogan, Melike Akca 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Rising household debt and cost-of-living pressures in the United Kingdom have intensified the role of AI-driven financial technologies in mediating credit assessment, repayment structuring, and debt support services. These systems increasingly shape consequential financial decisions, yet they operate within complex socio-technical environments characterised by regulatory constraint, algorithmic opacity, and heightened vulnerability risk. User Experience Research (UXR) Points of View (PoVs) are critical in translating heterogeneous research evidence into strategic direction for product and governance decisions. However, the existing UXR PoV framework was not designed for AI-mediated financial systems where interpretability, fairness, and accountability are central. This paper extends the UXR PoV pyramid into an AI-augmented methodological framework for Human-Centred AI debt management technologies in the UK financial services context. We formalise (1) an AI-Augmented PoV Pyramid, (2) a structured prompt architecture for synthesis and hypothesis generation, and (3) an AI-enabled Playbook Card system that embeds Generative AI into UXR workflows while preserving traceability and ethical oversight. Generative AI is positioned not as an analytic authority, but as an epistemic support mechanism subject to human validation and regulatory awareness. By grounding the framework in debt management technologies, including affordability assessment, repayment planning, and financial stress prediction systems, this work advances UXR methodology for high-stakes financial AI environments and contributes to the evolution of responsible, AI-powered UXR practice within the CHI community.

---


### 200. [FOCUS: Forcing In-Context Object Localization through Visual Support Constraints and Policy Optimization](https://arxiv.org/abs/2605.31145)

**<font color=#1a73e8>作者：</font>** Mohammed Asad Karim, Vinay Kumar Verma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-context localization (ICL) seeks to localize a target object specified by a small set of support examples in a query image, operating on the fly without training or parameter updates. Despite rapid advances in vision-language models (VLMs), achieving category-agnostic and visually grounded ICL remains an open problem, even though it is essential for applications such as image editing, personalized visual search, and retrieval. Existing methods are fragile and rely on explicit category supervision, which not only limits applicability in realistic settings with unnamed or instance-specific objects but also introduces category bias that steers predictions toward semantic priors rather than visual evidence. We introduce a two-stage training framework that explicitly optimizes in-context attention between support bounding boxes and query images without category supervision. We further refine localization via reinforcement learning using Group Relative Policy Optimization (GRPO) to directly minimize localization error. This formulation enforces visual correspondence over semantic priors, yielding robust instance-level localization. Empirically, a 7B-parameter model trained with our objectives outperforms models up to 72B parameters, demonstrating that context-aware localization objectives can surpass scaling alone. Comprehensive ablations validate the contribution of each component.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-317](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

# 🧠 大模型相关研究 | 2026年09月10日

> 本类共 **483** 篇论文：已确认 **447** 篇，待复核 **36** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**451-483**（第 10/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-483**

---

### 451. [DART: Distributional Adversarial Recurrent Training for Algorithm Learning](https://arxiv.org/abs/2609.05988)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hieu Tran Bao, Phung Thanh Dang, Pham Quang Nhat Minh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent reasoning models (RRMs) can solve structured problems, achieving easy-to-hard generalization through iterative computation in hidden space. These models are typically trained with instance-level supervision, which becomes increasingly problematic as task difficulty grows: valid solutions occupy a tiny region of the solution space, while invalid solutions proliferate rapidly. We propose Distributional Adversarial Recurrent Training (DART), a training framework that replaces single-point supervision with a local target distribution around the ground-truth solution and aligns model outputs with this distribution through an adversarial objective. DART provides a richer learning signal and encourages more stable iterative trajectories toward valid solutions. When evaluated on Maze, Chess, and masked Sudoku with multiple RRMs, including Deep Thinking Systems and Tiny Recursive Models, DART improves solution quality, stability, and robustness under the evaluated distribution shifts. Comparisons with label smoothing, Gaussian softened targets, and progressive training show that DART is not explained by target softening alone and is complementary to training schemes that stabilize long-horizon recurrence. These results identify DART as a promising approach for improving robustness across the evaluated recurrent reasoning models.

---


### 452. [Agentic Pressure: The Endogenous Entropy of Reliable Autonomy](https://arxiv.org/abs/2609.05995)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hengle Jiang, Ziying Luo, Ke Tang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Achieving reliable autonomy in the wild requires agents to sustain continuous operations across long-horizon trajectories. However, as agents navigate these unconstrained settings, they encounter cumulative friction that inherently destabilizes their alignment. In this paper, we identify a distinct non-adversarial phenomenon termed Agentic Pressure. We define this as a kinetic force that spontaneously emerges when the cost of compliance conflicts with the imperative of goal achievement. Unlike static jailbreaks, this pressure is endogenous and arises directly from the dynamics of interaction. We propose a theoretical framework that formalizes Agentic Pressure as the ratio between the required work to overcome environmental friction and the remaining capacity of the agent. Our analysis demonstrates that when this pressure exceeds a critical threshold, agents exhibit safety drift as a mathematically optimal adaptation. Consequently, they often resort to Instrumental Hallucination to rationalize rule violations. Empirical experiments validate this framework and show that aligned agents spontaneously compromise safety to preserve autonomy under high-pressure conditions.

---


### 453. [CWF: A Collaborative Writing Framework for Personalized and Reliable Popular Science Writing](https://arxiv.org/abs/2609.06126)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ruibiao Fu, Di Tang, Yunlong Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Personalized and Reliable Popular Science Writing, a novel task that requires adapting scientific explanations to audiences with different cognitive levels while preserving factual accuracy. However, improving personalization often introduces simplifications that increase the risk of hallucination and factual distortion. To address these challenges, we first construct a dataset of 39,134 entries and a reader-centric Personalized Science Communication Benchmark (PSCB) that jointly evaluates audience adaptation and factual accuracy. To reduce data and computational requirements while improving generalization across domains and audiences, we introduce DA-MoE, which explicitly decouples audience adaptation from domain knowledge through separate modeling. To enable robust verification and revision in evidence-scarce scenarios, a multi-agent fact-checking mechanism that augments limited evidence with role-specific agent debate and propagates confidence over a graph is proposed. Experiments on PSCB show that our approach achieves state-of-the-art performance. Our code is open-sourced at this https URL.

---


### 454. [Adapting Vision Foundation Models to Acoustics for Pose-Free 3D Sonar Reconstruction](https://arxiv.org/abs/2609.06261)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kevin Zhang, Jingxi Chen, Mohamad Qadri 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models trained on Internet-scale RGB datasets enable remarkable capabilities across a range of tasks, from text-to-video generation to few-shot 3D scene reconstruction. An acoustic foundation model trained on large-scale sonar datasets could enable similar capabilities in the underwater domain, where turbidity and low-visibility conditions make conventional RGB foundation models inapplicable. Unfortunately, a lack of freely available large-scale sonar datasets makes training such a model from scratch impractical. In this work, we demonstrate that vision foundation models can be efficiently adapted to the sonar setting by (1) exploiting the geometric relationship between the two sensing modalities and (2) employing accurate physics-based noise models for synthetic data generation. The resulting sonar adaptation models enable new capabilities: For the first time, we experimentally demonstrate sonar-based pose-free 3D reconstruction.

---


### 455. [OracleZoom: On-Policy Self-Distillation Inspired Reference-Constrained Recursive Image Super Resolution](https://arxiv.org/abs/2609.06490)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shubhashis Roy Dipta, Sourajit Saha, Shaswati Saha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recursive Super-Resolution (SR) extends fixed-scale SR to extreme magnification by repeatedly feeding predictions back into the same model, analogous to zooming an image repeatedly. However, ground truth availability at every scale, especially at depth, remains challenging as the required source resolution grows geometrically, leaving deeper predictions unsupervised. We present OracleZoom, an on-policy distillation-inspired, reference-constrained framework that trains on its trajectory while carrying the last ground-truth evidence beyond the supervision boundary. Direct and cross-scale supervision constrain verifiable content, while a no-reference quality objective guides unresolved fine-scale detail. A KL-constrained pretrained latent prior limits quality-driven drift, while EMA consistency stabilizes the supervision boundary. Across seven datasets, OracleZoom achieves the state-of-the-art SR quality across zooming scales, averaging 0.713 CLIPIQA, with larger gains on deeper scales, while significantly reducing hallucinations. Code, data, and models are available at this https URL .

---


### 456. [Assessing Covariate-Informed Grid Load Forecasting with a Time-Series Foundation Model](https://arxiv.org/abs/2609.06656)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Varsha Pendyala, Yiwei Fu, Weizhong Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern power systems are growing increasingly complex as they integrate diverse generation sources to meet rising demand, making accurate load forecasting challenging. Recent advances in time-series foundation models (TSFMs) resulted in promising performance in zero-shot univariate load forecasting tasks. However, real-world load forecasting often involves multiple target variables and requires the integration of exogenous variables, raising important questions about the utility of TSFMs in realistic settings. In this study, we position Chronos-2, a recently developed model by Amazon, as a representative multi-channel TSFM that supports univariate, multivariate, and covariate-informed forecasting, and conduct a systematic investigation of how such models can be used for real-world load forecasting. While prior work has evaluated Chronos-2 on a limited number of energy-related tasks in a zero-shot setting, its performance relative to established task-specific deep learning models and its behavior when adapted using task-specific historical data remains insufficiently understood. In this work, we evaluate Chronos-2 on two real-world utility datasets, ISO New England and ENTSO-E, and benchmark it against widely used task-specific deep learning models. Our results show that Chronos-2 benefits substantially from task-specific fine-tuning and achieves strong short-horizon forecasting performance, but its zero-shot accuracy lags behind task-specific models and its forecasting error grows more rapidly with increasing forecast steps. Overall, this study provides a detailed characterization of the strengths and limitations of TSFMs such as Chronos-2 in grid load forecasting and offers practical insights into how a pretrained TSFM can be effectively adapted for operational load forecasting applications.

---


### 457. [Towards Unified Multimodal Graph Foundation Model: A Bridge-Router-Adapter Based Approach](https://arxiv.org/abs/2609.06668)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sirui Zhang, Yubing Zhou, Xunkai Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal graphs couple node attributes in different modalities, such as text and images, with relational structure, enabling topological structure and cross-modality attributes to be modeled jointly. Multimodal graph foundation models seek unified representations from such data that transfer across different graph domains and downstream tasks. However, existing methods exhibit two fundamental limitations. (1) Cross-Scope Context Entanglement. They merge scope-specific graph contexts into a unified representation, obscuring their distinctions during multimodal construction. (2) Scope-Ignorant Modality Routing. They route modalities within a fixed graph scope, overlooking how modality relevance varies across neighborhood ranges. To address these challenges, we propose BRAIN, a unified model that focuses on graph context that combines neighborhood scope with modality composition. BRAIN comprises a scope-conditioned Bridge that combines structural information spanning local-to-global neighborhood scopes with different modality compositions; a hierarchical Router that estimates the relevance between the scope and the task, and selects compositions separately within each scope, allowing modality utility to vary with graph range; and a lightweight residual Adapter that further specializes the routed embedding for downstream prediction. BRAIN is trained through multi-graph pretraining followed by task-specific adaptation. Experiments across nine datasets and four task families demonstrate its broad effectiveness, improving node-classification and link-prediction performance by up to 4.73% relative to the strongest baseline, while achieving an average relative improvement of 14.72% across four graph-to-text and two graph-to-image metrics.

---


### 458. [A Trustworthy Watermarking Framework for LLM-Generated Food Safety Content](https://arxiv.org/abs/2609.06708)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhongli Fang, Yiran Chen, Lingyun Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are transforming many industries with their text generation abilities. However, their outputs can be easily tampered with, creating serious risks in critical areas such as food safety reporting. To protect the integrity and traceability of AI-generated content, this paper introduces ToSS (Token Oriented Repartitioning and Strategic Selection), a reliable authentication method using adaptive dual watermarking. The key innovation of ToSS is its dual watermark encoding approach that divides vocabulary tokens into black and white sublists, enabling precise bit-level embedding of traceability information. Additionally, an entropy adaptive mechanism dynamically selects text regions with high prediction uncertainty for watermark insertion, maintaining text fluency and factual accuracy while ensuring reliable traceability. Experiments on multiple datasets, including food domain texts, demonstrate that ToSS achieves leading performance in both watermark capacity and decoding accuracy.

---


### 459. [Companion-style QA Assistance in Ego-Vision](https://arxiv.org/abs/2609.06721)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hangyu Qin, Junbin Xiao, Shenglang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI companions are envisioned as always-on assistants that support users in daily life. With this regard, we introduce BuddyVQA, a benchmark for companion-style question answering (QA) on egocentric streaming video. BuddyVQA contains 21.6K questions linked to 6K highlight moments across 1,012 long, egocentric videos. It features two key characteristics that are common in daily first-person QA assistance but are largely overlooked in existing VideoQA benchmarks: ego-deictic expressions and interactively chained questions (e.g., "Where is it?", "How to get there?"). These require models to infer a user's in-situation intent by resolving visual pronouns in the context of egocentric visual and QA contents, with both grounded in a long-form streaming setting. To tackle the challenges, we propose MyBuddy, a companion-style QA assistant that highlights a multimodal chain-of-thought reasoning mechanism to infer the final answer based on the historical QA and visual content. An additional question filter and multi-level memory are designed to facilitate efficient QA and visual information retrieval under streaming QA settings. Experiments show that MyBuddy significantly enhances the performance of foundation models on BuddyVQA. Moreover, these gains generalize to other streaming and common video QA benchmarks, demonstrating the applicability and effectiveness of our approach. Our code and dataset are available at this https URL

---


### 460. [Improving Proficiency and Efficiency of Android GUI Agents via Self-Generating Tool Actions](https://arxiv.org/abs/2609.06792)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Juyong Lee, Woogyeol Jin, Kimin Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Android agents using a hybrid action space that combines GUI actions and tool actions (e.g., accessing application data via APIs) remain largely underexplored, mainly due to the excessive effort required to create tools. To address this gap, we introduce DroidTool, a framework for augmenting the agents with self-generated tools, which are realized as Python functions operating on application states (e.g., a database). To create tools with minimal human labor, DroidTool employs an agentic workflow featuring stages: proposal, implementation, test generation and execution, and repair. Notably, when testing the created tools for verification, it constructs relational tests across relevant tools for natural preparation of appropriate test preconditions and improved test coverage, rather than testing each tool separately. The GUI agents augmented with the generated tools achieved approximately 4.47%p higher performance with approximately 20.05% fewer interactions than the GUI-only agents, averaged across representative benchmarks: AndroidWorld, B-MoCA, and MobileSafetyBench.

---


### 461. [From Synthetic Priors to Model Behavior: Structural Coverage in Tabular Foundation Models](https://arxiv.org/abs/2609.06912)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** He Zhao, Ryan Thompson, Daniel M. Steinberg 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) are commonly pretrained on large collections of procedurally generated synthetic tasks, yet it remains unclear how well these synthetic pretraining priors support the downstream tasks on which the models are evaluated. We study this question from a distribution-level attribution perspective. We recover or reconstruct the synthetic data generators of four TFMs and compare their generated tasks with datasets from two widely used tabular benchmarks. Each dataset is represented by a common set of structural descriptors capturing schema, feature distributions, dependence structure, response properties, and feature--response relationships. In this space, we measure how broadly and repeatedly each synthetic prior reaches benchmark tasks using structural coverage and normalized density, and examine whether stronger local support is associated with better predictive performance. We find substantial differences across synthetic pretraining priors: some generators provide consistently broader and denser support for benchmark tasks than others. Moreover, stronger synthetic-to-benchmark support is generally associated with better relative model performance. These results suggest that structural coverage provides a useful diagnostic for characterizing synthetic pretraining priors and relating their data-generating assumptions to downstream model behavior.

---


### 462. [iBrain: A Unified Foundation Model Reading the Brain from Surface to Spikes](https://arxiv.org/abs/2609.06960)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ying Chen, Tiou Wang, Zhifeng Yue  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Invasive neural recordings provide high-fidelity measurements of brain activity, with signals such as intracranial EEG (iEEG) and intracortical spiking activity capturing neural dynamics at different spatial and temporal scales. Yet existing neural foundation models have largely been developed independently for different invasive recording paradigms, leaving joint pretraining across heterogeneous invasive signals underexplored. In this work, we introduce iBrain, a unified foundation model that jointly learns from iEEG and spiking activity. iBrain employs signal-specific encoders to accommodate their distinct signal characteristics and a shared spatiotemporal Transformer backbone to model dependencies across recording channels and time. We pretrain iBrain on over 7,000 hours of heterogeneous neural recordings using masked signal reconstruction and channel-view alignment, promoting contextual modeling of neural dynamics and robustness across different channels. iBrain consistently outperforms single-signal pretraining baselines and achieves state-of-the-art performance on multiple benchmarks. Further experiments demonstrate that iBrain exhibits transferability and data efficiency across diverse recording settings. These results highlight the potential of joint pretraining on heterogeneous invasive neural recordings to support scalable neural modeling and transferable representations across recording settings and downstream tasks.

---


### 463. [MOLE: Detecting Insider Threats in AI Agents](https://arxiv.org/abs/2609.06966)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Aashiq Muhamed, Virginia Smith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model misalignment, prompt injection, or operator misuse could lead AI agents operating frontier-lab accounts to exfiltrate model weights, poison training data, or weaken release gates. Existing benchmarks do not test whether defenders can detect this activity among routine work under a limited review budget. We introduce MOLE, an open benchmark of 150 AI-operated accounts sharing 9 stateful services over 30 workdays, with 12 threats and 8 corpora from four models totaling roughly 20 billion tokens. Of 39 agent models, 72% complete most assigned harmful objectives and agent refusal does not predict completion. MOLE enables comparison of 40 monitors across corpus generators, observability levels, and threats; even the best evaluated monitor in our single-day audit-event comparison misses nearly half of completed harm. MOLE also enables monitor development: benchmark-guided search improves a mid-tier monitor by 49-64%, while selective use of a stronger monitor improves budget-AUC by 10% over applying it to every account-day at comparable modeled cost.

---


### 464. [NeuCME: Toward Dynamic Multimodal Continual Learning via Neural Combinatorics of Multiple Experts](https://arxiv.org/abs/2609.07009)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kai Guo, Chuanbin Liu, Peng Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal continual learning has recently shown great potential for developing agents with human-like intelligence by continuously learning new tasks across multiple modalities. However, existing methods typically assume that the set of modalities per task is predefined and fixed. In this paper, we investigate a more realistic learning setting, referred to as dynamic multimodal continual learning, in which the set of modalities may vary across tasks rather than remaining fixed. This setting involves two primary challenges: (i) spatio-temporal catastrophic forgetting and (ii) adaptive multimodal fusion. To address these challenges, we propose NeuCME (as shorthand for \textbf{Neu}ral \textbf{C}ombinatorics of \textbf{M}ultiple \textbf{E}xperts), a novel framework designed to effectively learn and integrate knowledge across tasks with varying modalities. The proposed NeuCME model comprises three key components, namely modality-combinational rehearsal, multi-gated mixture-of-experts, and task relevance-guided distillation. Furthermore, we formulate an evaluation metric to quantify the dynamism of task sequences and then set up a comprehensive benchmark with different degrees of dynamism. Extensive experiments using four real-world datasets demonstrate that the proposed NeuCME outperforms state-of-the-art methods markedly.

---


### 465. [Detect Anything in Graphic Design: Element-Level Rewards for Autoregressive Detection](https://arxiv.org/abs/2609.07072)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiangning Zhu, Bowen Li, Shenyu Qiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphic designs, such as posters, advertisements, and infographics, are an important medium for communicating information and shaping understanding. Unlike natural images, they consist of layered elements with explicit compositional order. However, existing object detection models treat these elements as an unordered set, leaving compositional order unexploited. To address this limitation, we present Detect Anything in Graphic Design (DAD), a model that formulates graphic design detection as compositional deconstruction. It decodes elements in compositional order, using lower-layer elements to better detect higher-layer ones. The key feature of DAD is amodal detection, which predicts the full bounding box of each element, including regions occluded by elements placed above it. Building on this formulation, we propose Element Relative Policy Optimization (EleRPO), which extends GRPO from sequence-level supervision to element-level optimization. EleRPO provides fine-grained training signals that capture how each detected element contributes to overall detection quality, and works synergistically with compositional order to improve detection performance. To support training and evaluation, we build a dataset of 10 million graphic designs. Experiments show that DAD outperforms all baselines and achieves human-level performance in amodal detection, supporting effective image-to-layer decomposition. EleRPO consistently improves over GRPO across nine detection benchmarks.

---


### 466. [One for All: Generalist Foundation Model for Cross-Sensor Skeleton Representation Learning](https://arxiv.org/abs/2609.07078)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jeonghyeok Do, Yun Chen, Munchurl Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For learning generalizable motion representations from large-scale unlabeled data, Self-supervised learning (SSL) has become a widely adopted methodology. However, existing approaches are primarily limited by the inherent heterogeneity of skeleton data---characterized by varying joint counts, indexing protocols, and topological structures across different sensors---which typically necessitates training separate, sensor-specific, or even entirely dataset-specific models. To overcome this, we introduce SOfA (Skeleton One for All), the first generalist foundation model designed to achieve sensor-unified skeleton representation learning across diverse sensors. To accommodate the dimensional gap caused by varying joint counts, we introduce a fixed-size set of learnable Canonical Joint Slots, acting as a universal vessel that seamlessly accommodates arbitrary skeletal topologies. SOfA fills these slots via an attention mechanism that dynamically aggregates skeletal information from sensor-specific inputs. Furthermore, we resolve joint index misalignment between various sensors by introducing a Semantic Joint Embedding derived from a pre-trained text encoder, rather than relying on absolute positional embeddings. To validate our approach, we standardized ten 3D skeleton datasets for unified training. Extensive experiments demonstrate that SOfA can serve as a truly universal encoder, achieving state-of-the-art (SOTA) performance across a wide range of downstream tasks and sensor types, often outperforming dataset-specific specialist models with a single foundation model.

---


### 467. [The Price of Consistency: Exploiting Visual Anchors for Multimodal Jailbreaking in Video Generation](https://arxiv.org/abs/2609.07216)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Peng Li, Qianqian Xu, Yangbangyan Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of video generation has shifted the paradigm from pure text-driven to multi-conditional controllable generation, with reference images now widely adopted as conditional inputs to achieve superior spatiotemporal consistency. While these reference images serve as powerful visual anchors that significantly enhance controllability, their impact on safety remains largely unexplored. In this work, we reveal the visual anchoring effect: by enforcing consistency, the mechanism prevents the generated content from drifting away from the original harmful intent, thereby eliminating the model's natural safety escape route from harmful to benign content. Consequently, visual anchors inherently increase the safety risk---this is the price of consistency. Building on this insight, we propose Decoupling Intent via Visual Anchors (DIVA), a training-free multimodal jailbreak framework for video generation that exploits this vulnerability. DIVA decouples harmful intent into a static visual anchor image and a dynamic motion text prompt, and employs dual-criteria selection to balance attack stealthiness with semantic preservation. Extensive experiments across various leading commercial platforms and mainstream open-source video generation models demonstrate that DIVA achieves a substantially higher Attack Success Rate than existing text-only methods. To facilitate future research, we additionally contribute TI2VSafetyBench, the first safety benchmark for multi-conditional video generation.

---


### 468. [Distance-Aware Attention and Wall-Distance Expert Routing for Transformer-Based 3D Flow Prediction](https://arxiv.org/abs/2609.07222)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sanghyeon Kim, Sunwoong Yang, Namwoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transformer surrogates for 3D flow prediction compress an industrial mesh into a small set of tokens from which every prediction point reads. Two operations follow: the retrieval step in which a point gathers information from the compressed representation, and the feed-forward layer that transforms what it retrieved. In current backbones both are blind to where the point sits in the flow. We condition both on wall-related physical signals. Distance-aware cross-attention (DA-CA) reshapes each volume query by its wall distance before retrieval, so that a point deep in the boundary layer draws different geometric information than one in the outer flow. Surface-volume mixture-of-experts (SVMoE) replaces the shared feed-forward layer with a small set of experts, routed by wall distance for volume points and by local geometry for surface points. Neither mechanism is tied to one architecture, so we apply both unchanged to AB-UPT and Transolver-3. On DrivAerML with 50 training cases, DA-CA reduces the volume pressure error by 10.1%, and DA-CA and SVMoE together reduce it by 12.5%; DA-CA improves the near-wall region at some cost in the far region, which SVMoE recovers, and the volume experts settle into near-wall, transition, and free-stream bands without routing supervision. Retrained on 300 cases, the conditioning improves every field quantity, reducing volume pressure and velocity errors by 33.1% and 18.6% on AB-UPT and by 21.4% and 21.3% on Transolver-3. Under Leave-One-Body-Out evaluation on DrivAerNet++, it reduces the volume pressure error on unseen body types by up to 14.2%.

---


### 469. [Cross-modal learning for SAR target recognition using optical vision foundation models](https://arxiv.org/abs/2609.07753)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lucas Hirsch, James R. Hopgood, Javid Khan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic Aperture Radar (SAR) is an important modality in a wide range of imaging applications due to its versatile, long range and near all weather operating capabilities. However, Automatic Target Recognition (ATR) remains a challenging problem due to limited labelled data, the strong speckle in SAR images and the significant domain gap between SAR and more abundant optical imagery. In contrast, electro-optical (EO) imagery benefits from massive datasets, clearer visual structure and powerful foundation models. In this work, we investigate how vision foundation models trained on optical data can provide class level supervision for SAR classification.
We propose a cross-modal EO to SAR prototype alignment framework in which a frozen EO encoder, based on a DINOv3 vision foundation model, is used to construct class level optical prototypes without requiring strict EO/SAR pairs. A SAR model is then trained to classify SAR images while aligning its embeddings to the corresponding EO class prototype. At inference time, the SAR model operates independently, without access to optical imagery. We evaluate our approach on the UNICORNv2 dataset, an EO and SAR dataset of civilian vehicles with heavily speckled images and severe class imbalance. EO prototype alignment improves SAR classification accuracy over frozen DINOv3, SAR only finetuning and unpaired distribution alignment baselines, and t-SNE visualizations provide qualitative evidence of clearer separation among classes in the trained SAR embedding space. These results suggest that optical vision foundation models, despite being trained on visible spectrum imagery, provide transferable information for SAR image classification, offering a practical method for using large scale pretrained vision foundation models across challenging sensing modalities.

---


### 470. [Foundation Models for Generalizable Semantic and Goal-Oriented Communication](https://arxiv.org/abs/2609.07853)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Boliang Liu, Wint Yi Poe, Riccardo Trivisonno 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semantic and goal-oriented communication is increasingly studied for 6G, but generalization beyond seen data remains a key weakness under tight rate budgets. Many existing systems overfit their training data and degrade sharply at very low bit rates because they attempt to compress the entire signal. We introduce Foundation Model-Guided Semantic and Goal-Oriented Communication (FMSGOC), a framework that uses broad visual-linguistic Foundation Model priors to mitigate overfitting. It further improves rate efficiency by concentrating bits on sparse, goal-aligned anchors and relying on generative foundation-model priors to reconstruct the masked regions. By decoupling what to send from how to reconstruct, a vision-language foundation model selects and transmits a sparse set of semantic anchors, while a pretrained diffusion model, fine-tuned for masked completion, reconstructs the image at the receiver. In our experiments, FMSGOC reaches 0.039 bits per pixel (BPP), maintains high semantic fidelity (cosine similarity 0.87-0.90 on CIFAR-10), remains robust on previously unseen inputs (0.83-0.86 on ImageNet), and shows good perceptual similarity (0.1278/0.1558, CIFAR-10/ImageNet), outperforming strong end-to-end baselines at lower bit rates.

---


### 471. [Streaming Hierarchical Inference with Tabular Foundation Models](https://arxiv.org/abs/2609.07956)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Vitor Crista, Afonso Lourenço, Diogo Martinho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular Foundation Models (TFMs) have recently demonstrated strong predictive performance through in-context learning, but their deployment in high-throughput data streams remains challenging due to communication overhead and latency. We propose \textit{HINT}, a hierarchical inference framework that combines edge-based retrieval with cloud-based TFM inference. A graph-based approximate nearest neighbor memory maintained over a sliding window provides local predictions and uncertainty estimates, allowing confident samples to be processed locally while uncertain instances are selectively offloaded, together with their retrieved context, to a cloud-hosted TFM. The framework exposes an offloading threshold and a neighborhood retrieval policy that can be varied to balance predictive performance and communication cost. Experiments show \textit{HINT} consistently identifies favorable trade-offs.

---


### 472. [Inference-Time Nash Alignment](https://arxiv.org/abs/2609.08082)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hadi Hosseini, Debmalya Mandal, Duohan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Preference-based fine-tuning methods such as RLHF and DPO require substantial compute and large preference datasets. They also need direct access to the model parameters which are not provided by many state-of-the art models. Inference-time alignment offers a cost-effective alternative without updating model parameters. However, existing inference-time methods rely on a scalar reward model derived under a Bradley-Terry assumption, which cannot represent general preferences. Following recent work on fine-tuning with generalized preferences, in this work, we initiate the study of inference-time alignment under general preferences. We formulate the problem as obtaining a Nash equilibrium of a two-player zero-sum game between policies. We propose two algorithms: Best-of-Nash (BoN) and Nash Mirror Descent (NMD). We prove that both algorithms achieve a duality gap that matches the problem lower bound. Empirically, we implement the two methods on three datasets, which shows that our methods substantially outperform the base policy, converging to the performance of the fine-tuned models. Moreover, our results show that NMD remains robust across the regularization parameter.

---


### 473. [IGT @ FinMMEval 2026 Task 2: Question-Type Prompting with Targeted Extraction for Multilingual Financial QA](https://arxiv.org/abs/2609.08139)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuwen Chiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present the IGT system for PolyFiQA Task 2 of the FinMMEval Lab at CLEF 2026, a multilingual financial question answering task over English SEC filings and multilingual news articles (English, Chinese, Japanese, Spanish, Greek) for four companies. Our central observation is that the 344 development questions divide into two families requiring fundamentally different approaches: structured numeric types (R&D ratio, cash flow, capital expenditure) are best answered by direct keyword extraction on filing text, while synthesis types (investment strategy, capital allocation, top-three revenue focuses) require rule-based multilingual news passage selection. A dataset analysis reveals that 17-18 of 19 ground-truth reference answers per synthesis type share an exact evidence label prefix, whose unigram tokens contribute directly to ROUGE-1 overlap. The final system achieves development ROUGE-1 approximately 0.395, a 60% relative improvement over a generic RAG baseline (approximately 0.247), and ranks 3rd of 12 teams on the official test set with ROUGE-1 = 0.3071, Precision = 0.2821, and Recall = 0.4044.

---


### 474. [Snugi-AI-v2 @ eRisk 2026 Task 2: Early Depression Detection via a Learned Stopping Policy with Sustained Confidence Gate](https://arxiv.org/abs/2609.08161)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuwen Chiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe the Snugi-AI-v2 submission to eRisk 2026 Task 2, the second edition of contextualized early depression detection from Reddit discussions. Our central contribution is a learned MLP stopping policy trained to directly optimize ERDE50, replacing the fixed and tiered threshold strategies used in all prior eRisk Task 2 submissions. Combined with a sustained confidence gate that commits only after N=3 consecutive rounds of high policy confidence, the system reduces false positives caused by transient emotional posts without sacrificing recall. The pipeline encodes each discussion thread with a frozen MentalRoBERTa model, maps the accumulated representation to a depression probability via an MLP classifier, and delegates the timing decision to the learned policy. Our best run achieves F1 = 0.73 (Run 1) and F_latency = 0.70 (Runs 0 and 3), with a median alert round of 8 out of 500, completing the full evaluation in 1 hour 26 minutes, the fastest among all complete-submission teams. We report a systematic ablation across five runs spanning two encoder variants, four stopping strategies, and three gate values, along with negative results from GRPO policy training, BDI-II post filtering, MentalLongformer encoding, and DeBERTa ensembling. Code: this https URL

---


### 475. [NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness](https://arxiv.org/abs/2609.08183)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** NeoHorse Team, Guoliang Cao, Guohao Dai 等 37 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) requires a concrete mechanism through which an AI system observes its capabilities and converts that evidence into the next round of learning. We present NeoHorse-1, a family of agent-native models developed to explore this path through agentic post-training. Our system combines a heterogeneous model pool with intelligent routing, recording the predicted capability demand, selected service tier, and subsequent interaction for each user turn. These records are converted into training examples that preserve interleaved reasoning, tool calls, and harness context, and are admitted through structural validation, six-dimensional semantic evaluation, and subscene-level labeling. Routing signals organize supervised fine-tuning into a three-stage curriculum and extend to routing-guided on-policy distillation, where a teacher supervises student-generated responses under the same progression. Capability-guided allocation then converts evaluation feedback into the next training mixture, closing an evaluation-selection-update loop in which what the system learns to do shapes what it learns from next. Across eleven benchmarks covering harness-based agents, tool use, coding, and instruction following, post-training raises the macro-average from 58.94 to 64.87 at 4B and from 65.60 to 69.04 at 9B, substantially narrowing the aggregate gap between the post-trained 4B model and the 9B base model. NeoHorse-1 provides an initial prototype of this feedback-driven process and a path toward harness-mediated RSI across successive iterations.

---


### 476. [ReMoMask-2: Latent Retrieval-Augmented Masked Motion Generation](https://arxiv.org/abs/2609.08365)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yiran Wang, Zeyu Zhang, Ling Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-motion (T2M) generation maps natural language to human joint movements, aiding gaming, VR, and robotics. Retrieval-Augmented Text-to-Motion (RAG-T2M) improves generation on complex descriptions by conditioning on retrieved motion-text pairs. However, existing RAG-T2M models face two challenges: coarse-grained retrieval and fusion mechanisms overlook the hierarchical, spatial-temporal topology of human motion, and a representation gap exists because retrieved evidence resides in a semantic space separate from the generator's latents. To address the first, we present ReMoMask, a structure-aware RAG framework coupling Hierarchical Bidirectional Momentum (HBM) contrastive learning to align global and part-level features with text; Semantic Spatial-Temporal Attention (SSTA) for topology-aware fusion; and Topology Structured Masking (TSM) to force robust part-level grounding via adaptive masking. To address the second, we introduce ReMoMask-2, which rebuilds the retrieval database directly within the generator's pre-quantization latent space and aligns text queries via a distilled lightweight projector, allowing the generator to directly consume the retrieved motion's semantic content. Extensive experiments on HumanML3D, KIT-ML, and SnapMoGen demonstrate our retriever achieves state-of-the-art accuracy, while ReMoMask-2 attains the lowest FID on KIT-ML and SnapMoGen; notably, its single mask-transformer stage surpasses ReMoMask's full two-stage pipeline and delivers the fastest inference.

---


### 477. [Miles v0.1: Production-Level Post-Training](https://arxiv.org/abs/2609.08368)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** RadixArk, Tom Chen, Mao Cheng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Miles v0.1, a full-stack, production-ready system for frontier post-training. Building upon the clean design of slime, Miles designs each stage of the reinforcement-learning (RL) training loop around a single principle: components should be verified, clean, and customizable. With accuracy, efficiency, reliability, and scalability as first-class goals, Miles aims to make frontier-scale RL accessible to researchers and enterprises alike. This report walks through the system end to end: rollout engines built on SGLang, a trainer with a choice of two backends (NVIDIA Megatron-LM and PyTorch FSDP), and three weight-synchronization transports for different deployment topologies. Beyond full-parameter RL, Miles also supports LoRA RL, on-policy distillation, supervised fine-tuning, and true-on-policy rollout-training alignment, and extends the same architecture to diffusion models. We close with an end-to-end case study: fully asynchronous agentic RL on a GLM-5.2 744B-A40B model over terminal-use coding tasks, running on 64 NVIDIA GB300 GPUs with a median step time of 263 seconds over the first 30 measured steps. Miles is open-sourced at this https URL, with the project website at this https URL.

---


### 478. [IPM-FM: A Foundation Model with Consensus Feature Selection for Industrial Process Monitoring](https://arxiv.org/abs/2609.08375)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Liang Cao, Weide Liu, Yan Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial process monitoring is fundamental to the safety and economic performance of modern process plants. Current practice remains a one-task-one-model paradigm that is label-inefficient and prone to degradation under operating drift. Foundation models have reshaped language, vision, and generic time-series forecasting, but it has not been adapted to industrial process monitoring. This setting poses domain-specific challenges, including safety-critical decisions and asymmetric sampling between process variables and laboratory measurements. We propose the industrial process monitoring foundation model (IPM-FM). It first learns general-purpose representations from unlabeled industrial process data through self-supervised pretraining, then adapts to specific monitoring tasks using a small amount of task-labeled data, and finally produces calibrated predictions through an uncertainty-aware prediction head. IPM-FM integrates a self-supervised Informer backbone with a multi-criteria consensus feature selector, a recursive lag-feature regression head, and a calibrated Monte Carlo dropout uncertainty module. On a seven-year hydrotreater dataset for diesel flash-point soft sensing, IPM-FM attains an RMSE of 2.99, $R^2$ of 0.50, and 97\% coverage of its 95\% predictive interval, outperforming the strongest classical and from-scratch sequence baselines by 8.3\% and 14.6\% in RMSE respectively, supporting the viability of a unified pretraining--adaptation framework for industrial process monitoring.

---


### 479. [Beyond Agent Harnesses: Cross-Substrate Authority for Multi-Agent Systems](https://arxiv.org/abs/2609.08472)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yang Li, Sergey Volkov, Hai Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agentic systems persist model-visible memory while mutating workspaces, while a runtime, registry, or approval service may hold authority state outside both. Identical final files can then require opposite safe actions. We call this the cross-substrate authority gap: decision- relevant authorization information resides outside the planner-visible workspace or memory state. Across two controlled mini-benchmark families, three experiments compare planner-observation augmentation with an execution-time authority check using real Git lineage, durably recorded agent execution attempts, deterministic oracles, and two model routes. Experiment 1 is a 128-cell controlled evidence ablation: authority-blind candidate evidence obtains 0/32 final semantic success, while raw receipts and a typed relation both obtain 32/32. The missing authority fact accounts for the gain; typed packaging provides no observed planning-accuracy gain over equal raw information. Experiment 2 uses 96 planning calls: workspace-visible evidence yields 12/16 unsafe publication decisions, and planning with the typed relation remains unreliable (15/32 first actions correct; 11/32 invalid or absent). Experiment 3 replays the same 32 fixed model-generated first-action intents with zero additional model calls; a deterministic execution guard prevents all six unsafe intents from becoming effects and permits all 12 valid authorized publish intents. These results position authority enforcement at the mutation boundary as the operational endpoint of memory governance.

---


### 480. [Difficulty-Adaptive Tree-Structured Policy Optimization for Expanding Reasoning Coverage in RLVR](https://arxiv.org/abs/2609.08650)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Youngjun Yu, Sanghwan Jang, Hwanjo Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has been central to the recent success of Large Reasoning Models. However, while RLVR significantly improves single-sample accuracy, it often fails to expand the model's intrinsic reasoning coverage (pass@k) due to limited exploration during training. To address this, we optimize the structural design of train-time rollouts to enhance pass@k. Our analysis identifies three key design principles: (1) difficulty-adaptive rollout can play an important role in expanding pass@k, beyond serving as an efficiency heuristic; (2) tree-based rollout outperforms parallel sampling in discovering correct answers; and (3) sentence-entropy-guided forking overcomes the localization phenomenon of token-level branching to maximize semantic diversity. Building on these insights, we propose DATPO (Difficulty-Adaptive Sentence-entropy-guided Tree-structured Policy Optimization). DATPO integrates difficulty-adaptive tree search with a sibling-diversity advantage term, explicitly promoting semantic diversity to expand reasoning coverage during training. Experiments on mathematical reasoning benchmarks demonstrate that DATPO outperforms baselines especially in pass@k, which directly translates to superior test-time scaling performance.

---


### 481. [MorphoOrgaAgent: A Foundation-Model-Based Multi-Agent System for Autonomous Organoid Analysis](https://arxiv.org/abs/2609.08696)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hanyi Zhang, Maximilian Hoermann, Lion J. Gleiter 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Organoids are three-dimensional tissue models whose morphology provides important insights into tumor development, disease progression, and drug testing. Extracting these morphological features relies heavily on manual segmentation, which is time-consuming and labor-intensive. Furthermore, performing quantitative statistical analysis typically requires custom coding skills and a mathematical background, presenting a major barrier for experimental biologists. To address these challenges, we introduce MorphoOrgaAgent, a multi-agent framework that achieves zero-shot organoid segmentation, automated data analysis, and report generation based on natural language input. The framework consists mainly of three core components: a TaskUnderstandingAgent that identifies requested measurements and visualization types; a hybrid segmentation module that combines Cellpose-derived geometric prompts with text prompts to guide SAM3 for zero-shot organoid instance segmentation; and a ReportAgent that computes quantitative metrics and compiles them alongside generated visualizations into a structured report. We further introduce MorphoOrgaVQA, a benchmark designed for quantitative evaluation of agent systems in organoid morphology analysis. Experimental results demonstrate that MorphoOrgaAgent handles both explicit and descriptive user requests, produces measurements closely matching ground truth, and generates complete analysis reports without requiring manual programming. The complete source code and MorphoOrgaVQA benchmark are publicly available at this https URL.

---


### 482. [Beyond Gait: Person Identification from Millimeter-Wave Point Clouds Across Activities of Daily Living](https://arxiv.org/abs/2609.08818)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xilai Wang, Zixiong Han, Saad Rhanmouni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Person identification from millimeter-wave (mmWave) point clouds has mainly relied on gait. Indoor walking, however, is often brief and interrupted, while other activities of daily living (ADLs) may provide complementary identity information. We investigate identification across seven ADLs using mm-ADL, a new point-cloud dataset collected from 11 subjects under a controlled protocol. This extension introduces heterogeneous states and transitions whose spatial and temporal characteristics vary with activity. We therefore study whether activity can provide useful context for learning identity representations. We propose an activity-conditioned framework in which a human activity recognition router dispatches each clip to an activity-specific identity expert. The framework is implemented as a supervised mixture of experts, using a dual-stream static-dynamic PointNet (DS-SDPNet) to combine time-aggregated spatial structure with frame-to-frame information. We evaluate closed-set identification (ID) and subject-disjoint re-identification (ReID). With learned hard routing, ID accuracy increases from 62.1% to 68.0%. In a two-occupant ReID setting, hard routing increases mAP from 57.2% to 75.4% and Rank-1 accuracy from 59.1% to 82.1%. Under a matched gallery partition, activity-specific experts also outperform a shared embedding, showing that the gain extends beyond restricting the gallery. These results support the feasibility of using ADLs beyond gait for identification and the value of activity conditioning under controlled indoor conditions.

---


### 483. [DXPR: Depth-Based Vision-LiDAR Cross-Modal Place Recognition Using Vision Foundation Models](https://arxiv.org/abs/2609.09005)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yungsoo Han, Youngseok Jang, Seungwon Roh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present DXPR, a depth-based cross-modal place recognition (CMPR) framework that uses vision foundation models (VFMs) to match monocular camera queries against a LiDAR map without modality-specific encoders. This enables robots and autonomous vehicles to robustly localize using only cameras within pre-built LiDAR maps, even under severe seasonal, weather, and illumination changes. The key idea is to convert both camera images and LiDAR scans into a unified depth image representation so that a single VFM backbone with an aggregation head can learn modality-invariant global descriptors. To make pairwise metric learning faithful to scene geometry, we introduce a geometry-aware overlap miner: after cross-modal scale alignment of camera and LiDAR depth, we forward-warp measurements between views to compute a pixel-level overlap score. This score relabels ambiguous pairs and adaptively modulates the positive margin in a multi-similarity loss to avoid overfitting on weakly overlapping views. Extensive experiments on KITTI odometry and Boreas demonstrate strong performance and robustness across seasons, weather, and day/night. On KITTI, DXPR achieves near-perfect Recall@1 on most sequences and outperforms prior CMPR baselines. On Boreas, DXPR achieves intra-sequence performance on par with a strong single-modal baseline (DINOv2-SALAD), while showing clear improvements in the more challenging inter-sequence setting. Compared with RangeBEV, our method consistently performs better in both intra- and inter-sequence evaluations, demonstrating robustness under diverse seasonal and illumination changes.

---


> [!TIP]
> 当前位于：**451-483**（第 10/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-483**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

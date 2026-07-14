# 📦 其他研究 | 2026年07月15日

> 本类共 **420** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-420**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-420**

---

### 401. [HiFi-LLP: High-Fidelity, Low-Cost Latency Predictors with Confidence for Robust HW-NAS](https://arxiv.org/abs/2607.11746)

**<font color=#1a73e8>作者：</font>** Shambhavi Balamuthu Sampath, Behzad Shomali, Nael Fasfous 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With deep neural networks (DNNs) increasingly deployed on edge devices, hardware (HW)-aware optimization techniques--such as HW-aware compression and HW-aware neural architecture search (HW-NAS)--have become essential. These methods rely on real feedback from the target hardware to tailor DNN architectures for efficient deployment. While the search can be parallelized, latency measurements via hardware-in-the-loop (HIL) remain a bottleneck due to their sequential nature. Recent approaches use latency predictors to replace costly HIL feedback, but challenges persist: (1) platform-specific predictors often require tens of thousands of samples, and (2) inaccurate predictions can mislead the NAS process. To address this, we introduce HiFi-LLP, a high-fidelity, low-cost latency predictor based on graph attention networks, augmented with a confidence metric. HiFi-LLP outperforms prior platform-specific predictors by up to 9 percentage points (p.p.) in the 10% accuracy bound and achieves a Spearman's rank correlation of up to 0.996 across six devices in the LatBench dataset. We further propose a hybrid NAS framework that routes low-confidence predictions to HIL, achieving up to 8.6$\times$ speedup compared to typical NAS while maintaining a competitive Pareto front.

---


### 402. [When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems](https://arxiv.org/abs/2607.11751)

**<font color=#1a73e8>作者：</font>** Yibo Hu, Ren Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As multi-agent, tool-using LLM systems are deployed, a common safety net is a runtime monitor that checks each message, tool call, or step on its own. We show this net has a fundamental hole. A distributed backdoor splits a harmful payload across agents, so every local check passes while the assembled object is the attack. The monitor can be right on every step and still miss the attack. The problem is not splitting itself: split fragments can still leak suspicious tokens or provenance edges. The hard case is \emph{local benignness}. No fragment carries the harm, and what is left looks like ordinary benign traffic. We formalize this as an \emph{observability boundary}: a monitor catches only what its view can tell apart from benign traffic. We prove that once the fragments look benign in the monitored view, no detector on that view can catch them, however strong it is. Across a controlled testbed, an external benchmark, and end-to-end agent runs, local monitors lose the signal exactly as local evidence disappears, and it returns only when the monitor sees the assembled object. A monitor trained only on benign traffic recovers the attack's code structure across held-out encodings (0.874 mean AUROC). A decoded-view gate, given the encoding family, blocks every tested attack. But seeing more is not enough: full-trace monitors and decoders still fail unless they reach the representation where the payload is exposed. Local safety is not global safety when harm is compositional, and the open problem is finding that representation.

---


### 403. [Higher-Order Cell Tracking Transformer](https://arxiv.org/abs/2607.11754)

**<font color=#1a73e8>作者：</font>** Jordão Bragantini, Ilan Theodoro, Loïc A. Royer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing lineages from live-imaging microscopy requires linking cell detections across time, including through cell divisions. A common approach is to construct a candidate graph and associate cell segmentations (nodes) across frames. However, these and other existing methods overlook two structural obstacles in candidate tracking graphs: (i) cell divisions entangle distinct lineage paths in the node embedding space, and (ii) edges sharing a node have near-random label agreement, so the candidate-graph topology carries no useful information for graph neural networks to aggregate. We propose the \textbf{Higher-Order Cell Tracking Transformer} (HOCT), an edge-centric architecture in which candidate cell links attend to one another under a 3D geometric prior, resolving both issues. Evaluated on the Cell Tracking Challenge and a bacteria division benchmark, HOCT achieves state-of-the-art results without deep pre-trained image encoders. Moreover, the proposed approach is easier to fine-tune, quickly reducing tracking errors by 59% with 400 annotations in a human-in-the-loop setting, outperforming LoRA fine-tuning of competing transformer baselines (6.75% improvement).

---


### 404. [From Global to Factor-Wise Expert Composition in Discrete Diffusion Models](https://arxiv.org/abs/2607.11758)

**<font color=#1a73e8>作者：</font>** Haozhe Huang, Yudong Xu, Abhijoy Mandal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models offer a powerful framework for solving complex reasoning tasks, particularly through compositional generation, which combines multiple pre-trained experts to generalize beyond their individual training data. Recent theoretical corrections introduce time-dependent mixing weights to better align composed diffusion dynamics with the intended target. However, these methods are fundamentally limited by working on a per-sample basis, treating each generated state monolithically and ignoring the potential spatial or functional specializations of different experts. In this work, we address this limitation by proposing FactorDiff - a factor-wise composition framework for diffusion models. We posit that samples can be further decomposed into smaller factors, and propose a sampling process that dynamically routes each factor to the most relevant expert. We instantiate this framework with spatial/pixel-level compositions and validate it on the ARC-AGI benchmark, demonstrating that simple factor-specific routing consistently outperforms complex global scalar weighting schemes on tasks that require logical consistency and spatial disentanglement.

---


### 405. [From Expressivity to Sample Complexity: Narrow Teachers for Transformers via C-RASP](https://arxiv.org/abs/2607.11760)

**<font color=#1a73e8>作者：</font>** Michael Rizvi-Martel, Satwik Bhattamishra, Guillaume Rabusseau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A theoretical understanding of Transformers is crucial to better understand the capacities and limitations of large language models (LLMs). There is much work analyzing the expressivity of attention-based models. By proposing handcrafted weights or using computational complexity arguments, a large amount of past theoretical works have sought to characterize which tasks are and which are not in the hypothesis class of Transformer models. However, little work investigates the learnability of such solutions. In this work, we make progress towards this goal. Inspired by recent loss landscape analysis work, we propose preliminary sample complexity bounds for learning C-RASP constructions with Transformers.

---


### 406. [An Exact Instrument for State Usage in Selective State-Space Models, and the Input-Driven Migration It Reveals](https://arxiv.org/abs/2607.11796)

**<font color=#1a73e8>作者：</font>** Raktim Bhattacharya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selective state-space models such as Mamba route information through a bank of first-order modes whose input coupling is set by a learned selection mechanism. We give an exact instrument for measuring how a trained model uses these modes. Because the state matrix is diagonal, each channel's output decomposes exactly into per-mode contributions, and a per-(layer, channel, window) Gram tensor yields the exact output error of dropping any subset of modes, offline, at any budget. Validated against the reference implementation to a relative error of $2.3\times10^{-7}$ on the Mamba-1 family where it is exact, the instrument predicts a layer's deployed pruning error to a median relative deviation of $5\times10^{-7}$ over $4{,}464$ configurations, its floor set by the reconstruction. Applying the instrument across the Mamba-1 family (130M--2.8B), the deployed 7B Falcon-Mamba, and Mamba-2, we find that trained models re-allocate their state space with the input: which modes carry the signal migrates across contexts, and at the most affected layers a per-input oracle roughly halves the output error of a fixed mode set. Frozen-signal counterfactuals attribute the migration primarily to the input-dependent write map $B_t$; the timestep usually identified with selectivity carries almost none of it. Input-scheduled mode pruning on this measurement outperforms static, Hankel-based, and layer-adaptive rankings at every scale from 130M to the deployed 7B Falcon-Mamba, and at half the state budget it matches the unpruned model. Because the scheduler reads each window's mode usage from a first pass, this demonstrates realizable headroom; we claim no deployed compute or memory saving.

---


### 407. [StoryTeller: Training-Free Narrative Grounding for Long-Form Audio Description](https://arxiv.org/abs/2607.11798)

**<font color=#1a73e8>作者：</font>** Seung Hyun Hahm, Minh T. Dinh, SouYoung Jin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-form audio description (AD) requires more than describing visible actions: it must preserve characters, events, relationships, and story context across scenes so that blind and low-vision (BLV) audiences can follow a film. Modern video-language models (VLMs) are effective on short clips, but they often treat each moment independently, producing descriptions that miss who characters are, why events matter, and how the current scene connects to earlier narrative context. We propose StoryTeller, a training-free framework for story-aware long-form AD. Instead of relying only on local visual cues, StoryTeller maintains a verified narrative memory that carries forward story-relevant information across scenes, enabling later descriptions to remain coherent, grounded, and contextually informative. Given only raw video and a movie title, StoryTeller can optionally retrieve public movie metadata to resolve names and story context, while accepting only facts that are supported by the video through semantic filtering and VLM verification. The method requires no subtitles, scripts, AD transcripts, aligned captions, character banks, precomputed face identities, or task-specific fine-tuning. To evaluate whether generated AD preserves narrative information, we introduce StoryAD-QA, a question-answering benchmark that tests whether a language model can answer story-context questions using only the generated descriptions. Experiments on standard AD benchmarks and diverse long-form videos show that StoryTeller consistently improves narrative coherence, factual grounding, and story comprehension over strong baselines in automatic, QA-based, and human evaluations.

---


### 408. ["We are all in big trouble! *Shock Emoji": Personal Narratives in Expressing Emotions, Opinions, and Data Regarding Climate Change in TikTok Short Videos](https://arxiv.org/abs/2607.11803)

**<font color=#1a73e8>作者：</font>** Chu Zhang, Simai Huang, Shaohua Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Climate change is a source of anxiety about the future. Understanding how people express themselves about climate change enables us to address such concerns. To study climate change expression on social media, we analyzed 200 TikTok videos tagged with #climatechange, identifying four categories of content: expression-feelings, views-appeals, news-information, and trend-hijacking. We found that creators use humor to package sharp critiques, avoiding direct confrontation. They replace complex discussions with life stories, such as adopting a vegetarian lifestyle or deleting emails. They borrow from news media to present fragmented information as scientific interpretations, creating a perception of scientific credibility, balancing scientific accuracy with emotionality. Analysis of viewer responses showed they engaged empathetically, reshaping interpretations of videos. These interactions risk reinforcing existing views but help build community on TikTok, which lacks community structure. This study reveals how creators may retell news on science using personal narratives, highlighting how short-form videos enable climate communication.

---


### 409. [HandPad: A Bimanual Hand Interface for Fluid Window Interactions in VR](https://arxiv.org/abs/2607.11807)

**<font color=#1a73e8>作者：</font>** Wen Ying, Adil Rahman, Erzhen Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Virtual Reality (VR) offers potential for productivity work by creating expansive displays anywhere, yet current systems often rely on external input devices that limit the on-the-go use of mobile VR. We introduce HandPad, a suite of bare-hand interaction techniques that leverage the benefits of asymmetric bimanual coordination and self-haptic support. HandPad assigns the non-dominant hand (NDH) to establish spatial frames and interaction contexts, while the dominant hand (DH) performs fine-grained manipulation. Users can use NDH gestures as an input modifier to change the mode and target of DH interactions, including multi-window navigation, in-window content interaction, and window management. The palm surface of the NDH also serves as a physical touch surface, providing passive haptic feedback for effective DH touch interaction. Both hands and their interactions are spatially remapped to the window surface, enabling comfortable and direct interaction with virtual content. An exploratory study showed that HandPad enables efficient and ergonomic interaction, demonstrating its potential as a device-free approach for knowledge work in VR.

---


### 410. [Introducing Human-Centeredness in AI-Assisted Lexicography](https://arxiv.org/abs/2607.11808)

**<font color=#1a73e8>作者：</font>** Antonio San Martin, Catherine Trekker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper proposes a human-centered artificial intelligence (HCAI) framework for AI-assisted lexicography. While generative AI offers significant opportunities to enhance lexicographic work, it also raises concerns regarding the future role of lexicographers and the preservation of linguistic and cultural diversity. Drawing on HCAI principles and previous applications in other language professions, the paper identifies four interrelated dimensions through which AI integration in lexicography can be understood and critically examined: the augmented lexicographer, the sociotechnical context of AI integration, bias, and the design of AI-powered lexicographic tools. The framework argues that AI should augment rather than replace lexicographers, combining high levels of automation with meaningful human control. It further emphasizes the importance of preserving professional agency, mitigating AI-generated biases, and designing tools around the needs of lexicographers. By doing so, the paper provides a foundation for future research and the beneficial integration of AI into lexicographic workflows.

---


### 411. [Relaxing Faithfulness with Intervention-Only Causal Discovery](https://arxiv.org/abs/2607.11816)

**<font color=#1a73e8>作者：</font>** Bijan Mazaheri, Jiaqi Zhang, Caroline Uhler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery algorithms learn a network that describes the causal dependencies among random variables. A common workflow involves first utilizing conditional independence properties on observational data to determine partially directed causal relationships, then applying interventions to orient the unknown causal directions. A critical assumption for the first step is faithfulness: a requirement that causally linked variables exhibit statistical dependence. Many natural systems include buffering and stabilizing pathways that cancel out to achieve systemic robustness. This cancellation of pathways violates faithfulness, leading causal discovery algorithms to incorrectly remove causal dependencies. In this paper, we argue that hard interventions contain information about the presence/absence of causal linkage that is overlooked in the first stage of structure discovery. We show that a mild assumption -- called intervention-immediacy faithfulness -- that allows cancellations, is sufficient to nonparametrically identify causal structures with hard interventions. These results position interventions as the primary carriers of information about causal structure, which should take precedence over conditional independence testing. To flip the paradigm, we also specify equivalence classes when the identification criteria are not met due to limitations in the scope of interventions.

---


### 412. [MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents](https://arxiv.org/abs/2607.11818)

**<font color=#1a73e8>作者：</font>** Kaixin Ma, Di Feng, Alexander Metz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce MM-ToolSandBox, a benchmark and evaluation framework for visually grounded tool-calling agents. The framework provides a stateful execution environment spanning 500+ tools across 16 application domains, supporting multi-image, multi-turn tasks where agents must ground progressively arriving visual inputs into executable tool calls while handling realistic conversational phenomena (goal revisions, error corrections, state mutations). An automated scenario generation pipeline produces diverse, visually grounded scenarios through information-flow-guided planning and multi-stage quality filtering, yielding 258 human-verified nominal scenarios and 50 variants targeting interactive UI applications. Evaluating 12 state-of-the-art models, from 4B open-weight to frontier proprietary systems, shows that current models still lack robust visual tool-calling capability: even the best model achieves below 50% success rate. Our failure analysis further reveals that visual precision, not only planning, is a primary bottleneck for capable models: 53% of failures stem from incorrect information extraction from images despite otherwise correct task workflows. A planning-to-precision crossover emerges with scale: smaller models fail at deciding what to do, while larger models fail at perceiving what they see, suggesting fundamentally different research directions for improving models at different capability levels. The framework and the benchmark are publicly available at this https URL

---


### 413. [Transformer-Guided Swarm Intelligence for Frugal Neural Architecture Search](https://arxiv.org/abs/2607.11826)

**<font color=#1a73e8>作者：</font>** Romain Amigon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Architecture Search (NAS) has automated the design of deep learning models but traditionally requires massive computational resources, often measured in thousands of GPU-days. In this paper, we propose a frugal and memetic NAS framework designed to democratize architecture design on consumer-grade hardware. Our approach combines the global macro-search capabilities of an autoregressive Transformer controller, trained via Reinforcement Learning (RL), with the local micro-exploitation of an Artificial Bee Colony (ABC) algorithm. To prevent premature convergence during the RL phase, we introduce a dynamic entropy mechanism that forces topological exploration upon detection of performance stagnation. Evaluated on a standard GPU (NVIDIA RTX 3060), our hybrid method effectively resolves the "cold-start" problem inherent in metaheuristics. By algorithmically penalizing network depth, our framework actively mitigates model bloat: on the CIFAR-10 dataset, it discovers an efficient architecture reaching 84.85% accuracy with only $\sim$174,000 parameters (significantly smaller than standard baselines like ResNet-20) in 3 hours of search time. Furthermore, we demonstrate the framework's flexibility by applying it to credit card fraud detection, directly optimizing the F1-Score on highly imbalanced tabular data to reach a F1-Score of 0.71 with a compact network of $\sim$4,600 parameters. These results suggest that our approach can yield tailored, accessible, and highly parameter-efficient deep learning models suitable for edge deployment.

---


### 414. [MicroCharNet: Less is More for License Plate Character Detection](https://arxiv.org/abs/2607.11830)

**<font color=#1a73e8>作者：</font>** Huy Che, Dinh-Duy Phan, Duc-Lung Vu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> License plate character detection is a crucial component of intelligent transportation systems, where high accuracy and computational efficiency are required for real-time deployment. Although recent deep learning-based methods have substantially improved detection performance, many high-accuracy models rely on large-scale architectures that incur substantial computational overhead, limiting their applicability to resource-constrained devices. In this paper, we propose MicroCharNet, an ultra-lightweight model specifically designed for license plate character detection. The proposed architecture employs a compact backbone composed of C2f blocks, integrated with CoordAtt module to enhance feature extraction while preserving spatial information. A lightweight C3k2-based neck fuses multi-level features, followed by a single-level anchor-free detection head that enables end-to-end prediction. Experiments conducted on the UFPR-ALPR dataset demonstrate that MicroCharNet achieves competitive detection accuracy with only 0.08M parameters and 0.096 GFLOPs, while outperforming several recent YOLO-based baselines. Hardware-level evaluations further confirm its efficiency for real-time deployment on edge devices. These results indicate that carefully designed ultra-lightweight architectures can effectively balance accuracy and efficiency in license plate character detection. The source code is available at this https URL.

---


### 415. [FIERO: Empowering Creative Writing Through Collaborative Game Play](https://arxiv.org/abs/2607.11837)

**<font color=#1a73e8>作者：</font>** Chu Zhang, XiaoKe Zeng, Jin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Creativity often flourishes in collaboration, such as when designers brainstorm a new app together, or storytellers collectively build a world with elements of each person's narrative. However, collaborative storytelling can have challenges for its participants, such as when they disagree about the plot proposed, or when different ideas become fragmented when voiced individually. While current tools for creative collaboration focus on synchronous online text sharing, they often neglect the social dynamics of in-person collaboration critical to creative synergy. To address this, we created FIERO, a multiplayer web-based card game. Physical cards provide tangible scaffolding and social interaction, while the digital interface generates contextual visuals, facilitate group decisions, ensure narrative coherence, and synthesize different idea contributions using generative AI. Compared against online collaborative writing alone, the game significantly enhanced intuitive stimulation, idea fluency, and novelty generation, and also improved the content of the stories produced, leading to greater plot coherence (N=60). The cards provided creative structure and social engagement, while the interface provided contextualized augmentation without affecting player agency. This work shows how collaborative play can be utilized to foster creative support.

---


### 416. [HASTE: A Platform for Rapid Post-Disaster Building Damage Assessment](https://arxiv.org/abs/2607.11838)

**<font color=#1a73e8>作者：</font>** Caleb Robinson, Anthony Ortiz, Simone Fobi Nsutezo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a large disaster strikes, responders need a map of which buildings are damaged within hours. The models that do well on public benchmarks assume matched before-and-after imagery and a training set drawn from similar past events, and neither is usually available for a new disaster in its first day. We present HASTE (High-speed Assessment and Satellite Tracking for Emergencies), a no-code web platform that lets analysts who are not machine learning engineers produce per-building damage maps from post-disaster satellite imagery. HASTE implements two methods that share one interface. The first requires the user to label polygons over the post-disaster scene, trains a small semantic segmentation model on that single scene, runs it over the whole image, and joins the per-pixel output to existing building footprints. The second embeds every footprint with a pretrained vision model, requires the user to label a handful of buildings, and fits a logistic regression in the browser that scores the rest of the scene in seconds. We describe the platform, both methods, and the engineering that supports them. We also report preliminary experiments on xBD showing that foundation-model embeddings pooled over footprints separate damaged from intact buildings using post-disaster imagery alone, matching a fully supervised ResNet-50 baseline with a twentieth of its labels. HASTE and its predecessors have supported more than thirty real-world disaster responses since 2023, spanning earthquakes, hurricanes, cyclones, floods, wildfires, and tornadoes, delivering results to humanitarian partners within hours to days of imagery becoming available. We close with the directions we think are most promising, including vision-language assessment, active learning, and damage models for roads and other infrastructure. HASTE is open source at this https URL.

---


### 417. [A Durability and Cross-Language Transfer Benchmark for a Validated Teaching-Feedback Classification Protocol](https://arxiv.org/abs/2607.11873)

**<font color=#1a73e8>作者：</font>** Esteban U. Vega Barajas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Institutions collect far more open-ended teaching-evaluation feedback than they read. A prior study introduced a validated protocol for classifying such comments by thematic category and sentiment, built from a documented annotation guide, an intra-annotator reliability measurement, stratified cross-validation, and a held-out evaluation on a Spanish institutional corpus with a frozen-encoder design. Two questions limit its reuse: whether a protocol fixed to 2019-era frozen embeddings stays competitive as representation methods advance, and whether it transfers to a second language. We re-run it on the original Spanish data across three representation generations, sparse lexical features, frozen transformer embeddings, and prompted large language models, and transfer its sentiment task to English with a balanced 45,000-comment corpus checked against an aspect-labeled education dataset. Treating paired comparisons as descriptive, we find the protocol durable: a 2026 frontier model posts the highest thematic F1 on the hardest Spanish task, yet shows no sentiment advantage over a cheap model and no descriptive separation from it on English, so model choice is a deployment decision, not a property of the method.

---


### 418. [Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks](https://arxiv.org/abs/2607.11875)

**<font color=#1a73e8>作者：</font>** Tiberiu Musat, Tiago Pimentel, Nicholas Zucchet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a theoretical framework to explain the emergence of inductive reasoning abilities in Transformer language models. While previous works on Transformer learning dynamics have so far been mostly tied to specific tasks, we study a generalized class of inductive tasks that unifies several synthetic tasks known in the literature, including in-context n-grams and multi-hop reasoning. In this class, we theoretically prove that the training dynamics of attention models can be confined to a highly interpretable, low-dimensional invariant manifold. On this manifold, the learning dynamics are captured by a handful of interpretable coordinates rather than millions of parameters, making both theoretical and empirical analysis more tractable. Using this framework, we characterize how data statistics govern the competition between in-context and in-weights learning, we study how random initializations determine the `winning' circuit when multiple solutions are possible, and we demonstrate that the coordinate frame associated with the manifold can be used to automatically detect which circuits have been learned in trained models. By casting circuit formation as a low-dimensional dynamical phenomenon, we take a step toward a predictive theory of how Transformers learn.

---


### 419. [Requential Coding: Pushing the Limits of Model Compression with Self-Generated Training Data](https://arxiv.org/abs/2607.11883)

**<font color=#1a73e8>作者：</font>** Shikai Qiu, Marc Finzi, Yujia Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compression is fundamental to intelligence. A model that can represent its training data as a short code has discovered regularities that enable generalization. Large neural networks may learn functions far simpler than their parameter counts suggest, but it is challenging to construct codes that realize this simplicity. Parameter-based methods such as quantization produce code lengths that scale with model size, insensitive to how much information the parameters store. Prequential coding bypasses this issue by compressing the training trajectory, but codes the exact data sequence regardless of how much the model learns, yielding large codes when the data has high entropy. We introduce requential coding, where a teacher model selects training samples drawn from the student's own distribution. The student's code records only these selections, which cost bits only where teacher and student disagree. The resulting code length is independent of parameter count and data entropy, and often orders of magnitude shorter than the prequential counterpart, with an advantage that grows with scale. This compression sheds light on phenomena inaccessible to prior compressors. Holding loss fixed, larger models and ensembles compress to much smaller sizes despite more parameters. Plugged into a PAC-Bayes bound, the requential code yields state-of-the-art generalization guarantees for billion-parameter LLMs, outperforming bounds built on aggressive post-training quantization even granted zero error. The bound tightens with scale in the compute-optimal regime, as models become increasingly compressible relative to dataset size. The same code predicts that models gradually overfit when trained for multiple epochs. It also isolates the learnable information in a dataset from its unpredictable, random content, revealing that lower-entropy text holds far more learnable structure than higher-entropy image data.

---


### 420. [Latent-Identity Tuning in Text-to-Image Personalization Models](https://arxiv.org/abs/2607.11885)

**<font color=#1a73e8>作者：</font>** Daniel Garibi, Ronen Kamenetsky, Hadar Averbuch-Elor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating and editing a person's face demands high precision, as even minor modifications can significantly alter a subject's perceived identity. Current personalization and editing methods built on general-purpose text-to-image models, however, often lack the precision required for fine-grained facial edits. We present a method for fine-grained identity tuning in text-to-image personalization models. Unlike standard image editing, which operates on a given image, identity tuning modifies the latent representation of a specific identity, enabling the generation of diverse images that consistently depict the same edited identity. To enable fine-grained latent identity tuning, we explore the latent space of a pre-trained, frozen encoder for text-to-image personalization. Our approach requires no additional training. Instead, it leverages the existing architecture of a frozen encoder to uncover latent semantic directions. This space consists of a set of latent tokens that play distinct roles in capturing different aspects of an identity and often correspond to specific spatial or semantic facial regions. We show that meaningful directions can be identified within this space and within subspaces defined by selected tokens, enabling localized, fine-grained, and semantically coherent edits. We validate our approach through qualitative and quantitative experiments that demonstrate diverse localized facial edits while preserving cross-image identity consistency. Project page at: this https URL

---


> [!TIP]
> 当前位于：**401-420**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-420**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

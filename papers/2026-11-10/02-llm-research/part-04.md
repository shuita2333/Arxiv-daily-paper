# 🧠 大模型相关研究 | 2026年11月10日

> 本类共 **174** 篇论文：已确认 **163** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-174**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-174**

---

### 151. [Assessing the Impact of Retrieval-Augmented Generation on Algorithmic Problem-Solving](https://arxiv.org/abs/2611.09791)

**<font color=#1a73e8>作者：</font>** Gabriel Souza Baggio, Gabriel Machado Lunardi, Guilherme Medeiros Machado 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Competitive programming problems pose distinctive challenges for Large Language Models, as they demand not only proficient code generation but also advanced algorithmic reasoning. This study presents a Retrieval-Augmented Generation approach specifically designed to enhance the capacity of Large Language Models to address such problems. Our approach integrates an embedding-based retrieval mechanism and a similarity search algorithm to identify analogous problems within a knowledge database, employing a dynamically adjusted threshold to mitigate retrieval noise. We conducted an evaluation using the CodeContests dataset, focusing on the test split problems that exhibit similarity to instances from the training split. The experimental framework considered three conditions: (i) problems provided solely with their original descriptions, (ii) problems supplemented with randomly selected examples from the training split, and (iii) problems augmented with similar examples retrieved through the proposed method. In addition, we incorporated a Min-K membership inference analysis to examine whether the generated code solutions were influenced by potential memorization of training data within the evaluated Large Language Models. This complementary perspective enables a deeper understanding of model behavior by distinguishing genuine generalization through retrieval from implicit recall of pretraining samples. Performance was assessed using both pass rates and the CodeForces Elo rating of the problems. The results provide empirical evidence that similarity-based retrieval substantially enhances Large Language Models performance in competitive programming scenarios, offering an scalable framework for improving code generation in algorithmic problem-solving contexts.

---


### 152. [Maya a1: Do the Options Read the Model, or Does Their Position? Order Sensitivity in a Non-Autoregressive Decision Model](https://arxiv.org/abs/2611.09803)

**<font color=#1a73e8>作者：</font>** Mohammed Nayeem Khan, Logesh L  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Laya answers typed multiple-choice questions in one forward pass by scoring a hidden state at one [MASK] marker per option. We re-engineer the checkpoint (421M parameters; a 2-layer option head with no positional tensor; a documented but unused parallel layout) and test whether the answer depends on where an option is listed. Presenting 951 Qwen-verified questions under every cyclic rotation of their options (or six random permutations for 12 options), the released checkpoint changes its answer for 25.8% [22.9-28.7] of questions (19.7% on the 605 English-language items alone); accuracy with the gold option first versus last differs by 10.1 points, and the flips concentrate where the model's own confidence is low (54% versus 8% across confidence terciles). Fine-tuning with Laya's trainer on 2,818 teacher-verified rows with option shuffling cuts the flip rate to 7.2%; the identical rows without shuffling give 11.4%, so shuffling is responsible for 4.2 points of the improvement. A confidence-weighted vote over orderings gives 69.7% against 69.1% for a single base pass at 4.1x the compute. Labels are LLM-made and the test sets are teacher-filtered. We also fine-tune with the authors' parallel layout on the same rows: flip rate 0.5%.

---


### 153. [Compaction, decay and reinforcement in a two-tier conversational memory: a paired evaluation against retrieval-augmented generation](https://arxiv.org/abs/2611.09807)

**<font color=#1a73e8>作者：</font>** Osamudiamen Edogun, Joshua Obigwe, Irfan Mehmood  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A conversational agent that remembers has to decide what to keep. Retrieval-augmented generation keeps the transcript and searches it; the alternative is to compact each turn into atomic facts and search those. We compare the two on LoCoMo, with both arms answering all 1,985 questions in one window, against the same stores, with the same generator and judge, and both predictions on one row, which licenses McNemar's exact test on the 512 questions where they disagree.
On the four categories comparable work reports, compaction scores 71.4 per cent against 64.6, a lead of 6.8 points (p = 5.5e-08) at 34 per cent fewer prompt tokens. On all five, including the adversarial set comparable work drops, the lead falls to 2.0 and stops being significant, because the baseline leads adversarial by 14.6.
That loss has a structure. Our lead falls as the reference answer demands more source wording, 9.6 points ahead at one or two reference words and 3.1 behind past eight, with token overlap moving the same way, so the judge is not the cause. Compaction keeps what a fact asserts and discards how it was said, so it wins where the answer is a value and loses where it is a phrasing. We also report four negative results with their power calculations.

---


### 154. [BEV3SR: Evidence-Aware 3D Spatial Reasoning from Video](https://arxiv.org/abs/2611.09816)

**<font color=#1a73e8>作者：</font>** Fan Zhu, Rui Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D spatial reasoning from video remains challenging for VLMs because videos provide sequential, view-local observations rather than persistent metric scene records. Many questions must be answered in a query-specified perspective rather than the observed camera viewpoint, and prompting with a fixed set of RGB views may miss sparse or occluded visual cues. To address these gaps, we introduce BEV3SR, a training-free and backbone-agnostic framework for RGB-D videos with camera parameters. BEV3SR turns video observations into queryable metric bird's-eye-view (BEV) scene memory and formalizes each query into an evidence-aware spatial task. The Spatial Task Formalizer specifies the query's reference frame, spatial constraints, objective, and evidence requirement. The evidence requirement determines the appropriate reasoning pathway. A query treated as requiring geometric evidence is handled by the Geometric Reasoner, which deterministically computes the answer using the metric BEV records in the query-specified reference frame. Otherwise, a query treated as requiring visual evidence is passed to the Visual Evidence Aligner, which uses BEV-indexed object records and their associated supporting views to retrieve object-consistent and scene-context RGB frames for VLM grounding. Within a standard 16-frame budget, BEV3SR consistently improves different VLM backbones across multiple 3D scene QA benchmarks, delivering large gains on spatially intensive questions and significant improvements on open-ended scene QA. These results demonstrate that BEV3SR offers an effective, efficient, and interpretable framework for explicit 3D spatial reasoning from video.

---


### 155. [Generative Latent Priors for Interpreting and Steering Protein Language Models](https://arxiv.org/abs/2611.09818)

**<font color=#1a73e8>作者：</font>** Daniel Hinjos, Lucía Urcelay  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dominant methods for interpreting large models impose strong structural assumptions. Generative Latent Priors (GLP) are a complementary approach: a diffusion model that learns the distribution of a frozen model's activations directly, imposing no assumptions. We port GLP to ESM-2 activations (UniRef50) and evaluate it at two host scales (ESM-2-8M and -650M), both as a lens for protein representations and as a prior for editing them. Generation quality scales smoothly with depth and compute. As a lens, single GLP "meta-neurons" are the strongest probes of discrete Swiss-Prot concepts at both hosts, beating InterPLM's released SAE features, and lead on continuous properties at 8M though not at 650M; falsification tests show this is mostly concentration, not new information. As an editing prior, the on-manifold correction makes DiffMean steering of three biochemical properties effective and restores on-manifoldness, but only in isolation: re-embedding the sequences actually produced after several rounds of decoding, the structural plausibility is compromised. This is mainly reproduced in additional SAE-based clamping structural steering experiments, where only Helix motif succeeds. The naturalness failure is traced to the rewriting coverage and the decoder rather than the prior, highlighting what the method must clear before it can serve for both discovery-by-editing and discovery-by-exploration. Trained GLPs are released on this http URL.

---


### 156. [BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design](https://arxiv.org/abs/2611.09825)

**<font color=#1a73e8>作者：</font>** Dayou Du, Woon Yee Ng, Guangming Sheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The key-value (KV) cache dominates memory capacity and bandwidth in long-context LLM serving. While 4-bit microscaling formats (NVFP4, MXFP4) shrink the cache and run attention on FP4 Tensor Cores, a fundamental gap remains between algorithmic quantization and system-aware acceleration: existing FP4 KV systems use vanilla quantization that causes severe accuracy drops, whereas accuracy-oriented 4-bit algorithms rely on vector codebooks whose lookup overhead degrades decoding throughput. We present BitDecoding-FP4, an algorithm--system co-design for accurate and efficient native FP4 KV decoding. We mitigate three error sources: Dual-Residual Query Quantization splits queries into two FP4 tensors, cutting query logit error from 60% to 1%; Underflow-Aware Probability Scaling prevents E4M3 scales from rounding long-context probabilities to zero; and Outlier-Aware Key Quantization combines static smoothing, Hadamard rotation, and scale search to suppress key outliers under token-wise scaling. At the system level, we remove the softmax bottleneck via transposed softmax with fused probability quantization and stacked query MMA on paged KV caches. Across dense and MoE models with GQA and MLA, BitDecoding-FP4 stays within 0.5 points of BF16 KV accuracy with NVFP4 (1 point with MXFP4), and tracks BF16 KV in RL training rollouts. In end-to-end serving on NVIDIA B300 with Qwen3-4B and Qwen3-30B-A3B, it delivers 2.4-3.0$\times$ higher peak serving throughput than BF16 KV. The implementation is available at this https URL.

---


### 157. [Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL](https://arxiv.org/abs/2611.09828)

**<font color=#1a73e8>作者：</font>** Aria Wong, Joshua Engels, Neel Nanda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) rewards are notoriously difficult to design and control, often leading to the model learning unintended behaviors such as reward hacking. One potential solution is to monitor for reward hacking and penalize it when detected; however, training against a monitor could lead to evasive behavior, and our general understanding of how to apply monitors effectively during training is limited. To study how best to use monitors to mitigate reward hacking, we introduce and open source three realistic environments where Qwen3-4B reward hacks: a coding environment hackable via test overwriting, a medical chat environment hackable via sycophancy, and a biography generation environment hackable via hallucination. We first focus on the coding environment, where we find that: (1) models can learn to evade highly accurate monitors by exploiting systemic flaws in probes and LLM judges; (2) monitors that leak more learning signal during RL suppress reward hacking but are more often evaded; and (3) including easier problems in training can decrease reward hacking. We apply our findings to build better reward hacking monitors for the medical chat and biography generation environments that improve upon naive baselines to reduce reward hacking rates across seeds to before-training levels in some interventions. Our results demonstrate that our takeaways translate to new settings and that better monitor intervention designs are possible.

---


### 158. [GroundWork: Bridging Human and LLM Reasoning Through a Structured Argumentation Model](https://arxiv.org/abs/2611.09840)

**<font color=#1a73e8>作者：</font>** Sjoerd Vink, Byungmoo Kim, Michael Behrisch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly integrated into workflows that require reasoning over text documents, yet interaction remains largely conversational. This leaves argumentative structure implicit or embedded in text, making it difficult to maintain, compare, and revise arguments as analyses evolve. We present GroundWork, a mixed-initiative system that makes argument structure a shared, editable state for humans and LLMs. GroundWork operationalizes the Toulmin model of argumentation as a typed graph with explicit operations for human and LLM edits. It exposes this structure through coordinated corpus views and an editable workbench for constructing, comparing, testing, and tracing source-grounded arguments. We evaluate GroundWork through an expert study with four participants spanning consulting, product development, law, and immunology, and three use-case scenarios in intelligence, law, and medicine. Our findings show that GroundWork makes source-grounded arguments inspectable, comparable, and revisable as shared human-LLM state.

---


### 159. [Ensemble Methodology for Reference-Free Confidence Estimation in LLM-based Code Summarization](https://arxiv.org/abs/2611.09846)

**<font color=#1a73e8>作者：</font>** Marco Colombo, Balaji A Jayaram, Sowmyakumari Selvaraj 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper describes an approach and use case to estimate the correctness of LLM-generated COBOL summaries without access to human-authored references. The core intuition is that inter-model agreement on semantics is informative about truth, and that an LLM-as-judge can provide higher-fidelity pairwise assessments than traditional string- or embedding-based metrics. We operationalise this intuition with (i) controlled summary generation from diverse models; (ii) a LLM evaluator that compares pairs of summaries and emits structured judgments; and (iii) a calibrated aggregation rule that combines supportive evidence while penalising only corroborated contradictions.

---


### 160. [Computer-Use Agents Are Embodied Generalists](https://arxiv.org/abs/2611.09847)

**<font color=#1a73e8>作者：</font>** Pranjal Aggarwal, Sean Welleck  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many areas of AI, general-purpose models have increasingly replaced handcrafted methods and specialized architectures. We argue that embodied AI is poised for a similar shift. Our key claim is that embodied tasks can be formulated as interaction with digital software. Specifically, we build software that renders an agent's view of a physical environment on a screen and provides controls for acting in it. A computer-use agent (CUA) can then perform embodied tasks through the same screenshots and keyboard and mouse actions that it uses to operate ordinary software. Using a single CUA design and changing only the software, our entries win first-, second-, third-, and sixth-place prizes across four ECCV workshop competitions, without any competition-specific agent tuning. These results suggest that the skills CUAs learn on software, such as visual grounding, precise clicking, and exploration, already carry over to embodied tasks, giving CUAs a far broader scope in embodied AI than previously realized. We therefore advocate that computer-use agents can be embodied generalists. Further, we advocate that, by following the training strategy that made computer-use agents general, embodied AI can converge on a single general model as well, ushering in a new era of general embodied AI. Website: this https URL

---


### 161. [On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning](https://arxiv.org/abs/2611.09872)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Ru Wang, Yuanyuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time reinforcement learning (TTRL) adapts pretrained language models to unlabeled target-domain data using self-generated pseudo-labels, whose reliability remains poorly understood. We analyze majority-vote supervision for TTRL with online Direct Preference Optimization (DPO) and decompose its error into population-majority bias and prompt-dependent finite-rollout variation. Because population-majority bias is generally unidentifiable without external supervision, we focus on mitigating the downstream effects of finite-rollout variation. We propose \emph{Prompt-Conditional Distributionally Robust DPO (this http URL)}, which conditions within-prompt robust reweighting on observed vote reliability to make updates from sampling-sensitive prompts more conservative. We further introduce a cache-based mechanism to reduce self-supervised forgetting during online adaptation. Across six mathematical and knowledge-intensive reasoning benchmarks and five model backbones, this http URL matches or outperforms the strongest TTRL baseline in 24 of 30 settings.

---


### 162. [CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse](https://arxiv.org/abs/2611.09891)

**<font color=#1a73e8>作者：</font>** Peter Belcak, Greg Heinrich, Saurav Muralidharan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models reinvent the wheel all the time. They conflate task-solving with the execution of the solutions, which forces them to solve every problem from scratch. We show that once a task has been reasoned through, the application of its solution to a new problem instance can be done very efficiently and with little involvement from language models. We introduce agentic reasoning caching, a method for constructing robust CPU-executable agentic reasoning caches (ARCs) from LLM reasoning traces. ARCs show on-par performance with frontier LLMs across a range of difficult mathematical and scientific tasks, are fully explainable, continually trainable, robust to input perturbations, and 16-291x cheaper to invoke than the source model.

---


### 163. [Video-Coder: Reinforcing Agentic Coding for Video Generation](https://arxiv.org/abs/2611.09894)

**<font color=#1a73e8>作者：</font>** Chaoyang Wang, Sicheng Gao, Junan Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed remarkable progress in video generation in terms of visual quality and temporal consistency. However, generating videos with precise spatial structure, coherent motion dynamics, and controllable scene composition remains challenging. In this paper, we introduce Video-Coder, the first attempt to train a code-driven video generation agent, which autonomously writes and executes code to construct a dynamic 3D scene (Draft Video) that provides structure and motion signals to downstream video generators. To support this paradigm, we design a dedicated data pipeline and curate two high-quality datasets, Video-Coder-SFT-6k and Video-Coder-RL-2k, which contain diverse prompts and ground-truth reference videos. We further develop the Video- Coder Harness, a unified interactive environment integrating code execution, 3D scene rendering, and execution feedback for agent training and inference. We then train Video-Coder with SFT fol- lowed by harness-native agentic reinforcement learning with dual reward feedback, which combines execution-based and video-based rewards. Additionally, we design an annealing training strategy that gradually reduces the execution reward over time, allowing the model to rely more on the video reward in the later training stages. Experiments show that Video-Coder achieves significant gains, improving Minimax-H3 by approximately 7 points on PhyGenBench and 24 points on VBench-2.0. We hope this work can serve as an open foundation for coding agents in video generation, and we fully open-source our data, models, and code

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 164. [Towards Label-Efficient Geospatial Foundation Model Adaptation via Positive-Unlabeled Learning for Building Damage Mapping](https://arxiv.org/abs/2611.08561)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hengwei Zhao, Qirui Wang, Zhuo Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation models (GFMs) are reshaping remote sensing by shifting the field from task-specific modeling toward general-purpose geospatial intelligence. Mapping the damage to buildings stands to benefit substantially from this shift, as GFMs pretrained on large-scale Earth observation data provide generalizable geospatial representations that can facilitate effective responses to sudden-onset disasters. Although parameter-efficient fine-tuning (PEFT) facilitates GFM adaptation, parameter efficiency does not necessarily translate into label efficiency. Building damage mapping remains challenging due to scarce pre-existing labeled data or limited time for annotation. When weak supervision is introduced to alleviate the labeling bottleneck, we identify the difficulty of learning sufficiently discriminative representations as a key challenge for label-efficient GFM adaptation. To address this challenge, we propose a Positive-Unlabeled GFM Adaptation (PUMA) framework that requires annotations for only a small number of damaged buildings. More specifically, PUMA integrates non-contrastive weakly supervised representation refinement to mitigate the impact of noisy supervision on representation learning from a gradient perspective, and latent-state-based label disambiguation to enable reversible supervision refinement without requiring class prior estimation. Extensive experiments on disaster benchmark datasets from around the world demonstrated the effectiveness and robustness of PUMA. A real-world application to the 2025 Los Angeles wildfires further highlighted its potential to accurately map damage under highly limited supervision. More broadly, these findings suggest that weakly supervised PEFT offers a label-efficient pathway from GFMs to real-world applications.

---


### 165. [Foundation-Model Residuals as Signals of Urban Bus Irregularity](https://arxiv.org/abs/2611.08703)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Csaba I. Sidló, Jamil J. Ghazal, Domonkos Rózsay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained trajectory models encode mobility patterns learned across cities, but their errors when transferred to a new city are usually treated only as performance limitations. We instead ask whether these residuals reveal systematic local conditions. Architectures such as UniTraj and TrajFM learn transferable trajectory representations, although cross-context transfer remains challenging. Using the NetMob26 bus location, ticketing, weather, network, and socioeconomic data for Niteroi, we analyze spatial and travel-time residuals of these recent trajectory foundation models. We test whether high residuals concentrate spatially, whether spatial and travel-time residuals overlap, and which urban-context variables explain their distribution.
We interpret high residuals as candidate proxy signals of transit irregularity rather than direct evidence of service disruption, and analyze their contextual associations using Explainable AI (XAI). Insights into such varied environments are increasingly valuable for evaluating new urban paradigms; for instance, the 15-minute-city perspective serves as a key motivation for our approach, guiding our methods and expanding the analysis beyond standard mobility metrics.

---


### 166. [PhysioWave-T: Token-Efficient Wavelet Foundation Models for Biosignals](https://arxiv.org/abs/2611.08969)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yanlong Chen, Simone Benatti, Luca Benini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present PhysioWave-T, a token-efficient wavelet foundation model family for EEG, ECG, and sEMG. Dynamic scale folding recombines J+1 wavelet subbands prior to tokenization, compressing sequence length from (J+1)CS to CS tokens for J levels, C channels, and S temporal patches. Route-specific front ends and learned channel-name embeddings allow one Transformer per modality to handle diverse montages and sampling rates, while unseen setups reuse the backbone via lightweight adapters. We pre-train a 30M-parameter EEG model on over 15M windows (19--128 channels), alongside ECG (30M) and sEMG (12M) encoders. Across four EEG routes, scale folding cuts Transformer latency by 4.0--7.2x and peak memory by 6.8--12.7x over scale expansion without accuracy loss. Our EEG encoder leads 8 of 9 metrics against BENDR, BIOT, LaBraM, and EEGPT, and surpasses LUNA-L on wearable seizure detection with fewer parameters. Reliability-aware latent fusion (RALF) further integrates summary tokens from independently pre-trained encoders via sample-adaptive weights. On SeizeIT2, RALF raises event sensitivity at 11 false alarms/h from 61.4% to 74.4% and window AUPRC from 0.321 to 0.399 over the best unimodal baseline, outperforming weighted-logit and concatenation fusion across all variants. PhysioWave-T also achieves state-of-the-art sEMG accuracies and top macro-F1 on PTB-XL Super and Chapman-Shaoxing. Code and models: this https URL.

---


### 167. [Energy-Based Reasoners: Your Recurrent Reasoner Should Be an Energy-Based Model](https://arxiv.org/abs/2611.08977)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** William Xingxu Chen, Alexi Gladstone, Zeyu Michael Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looping is a powerful inductive bias for reasoning. By repeatedly iterating a recurrent block, looped models can scale their effective depth and enable multi-step reasoning in latent space. However, existing looped models are not inherently guided by an explicit measure of progress, making it difficult to determine when to stop looping and how to improve upon the current state. To enable this, we introduce Energy-Based Reasoners (EBRs), which learn an energy function over latent reasoning states and formulate looped updates as gradient descent on this energy. The energy scores latent states, while its gradient guides refinement and provides a signal for stopping. To train EBRs effectively, we further introduce exploration-based training to discover additional modes and to better shape the energy landscape over a broader set of states. Across four algorithmic reasoning benchmarks, EBRs match or outperform prior recurrent reasoning models, achieving 99.9% accuracy on Sudoku-Extreme while using 345$\times$ less inference compute than the next-best model and maintaining comparable training compute. On all multi-solution benchmarks, EBRs achieve state-of-the-art coverage of distinct valid solutions while maintaining near-100% single-sample accuracy. These results suggest that energy-based models are a promising approach for strong reasoning performance.

---


### 168. [StreamTab: Training-Free Temporal Link Prediction with Tabular Foundation Models](https://arxiv.org/abs/2611.09052)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mingqi Yang, Renqi Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal link prediction uses past interactions to predict whether two nodes will interact in the future. Temporal graph neural networks achieve strong results on this task, but they are trained separately for each graph. How a model should use interaction history also depends on the candidates it is compared with. A past interaction can distinguish a recurring link from a random pair that has never interacted, but when the negative candidates have also interacted before, other signals are needed. We propose StreamTab, a training-free framework built on a frozen tabular foundation model pretrained only on synthetic tables. StreamTab describes each candidate pair by statistics of its past interactions and shows the model recent observed interactions and sampled negative pairs as labeled examples, from which the model scores new candidates. Its central design, regime conditioning, samples the negative examples according to how the candidates are sampled, so the examples show the distinction the model must make. As new interactions arrive, StreamTab updates the statistics and refreshes the examples while the model parameters stay fixed. On thirteen datasets against 21 temporal graph baselines, StreamTab achieves the highest average precision on twelve datasets under historical sampling and eleven under inductive sampling, and ranks first or stays within one point of the best on seven datasets under random sampling. With the same features and model, regime conditioning raises average precision over examples with random negatives by a median of 12.6 points under historical sampling.

---


### 169. [TailDART: Compute-Efficient Foundation Models for Financial Time-Series Forecasting](https://arxiv.org/abs/2611.09176)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chiang Qin Zhi, Ranjan Satapathy, Erik Cambria 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although time-series foundation models (TSFMs) achieve strong zero-shot transferability across high-information-density physical systems, applying overparameterized TSFMs to quantitative finance is fundamentally constrained by low signal-to-noise ratios, non-stationarity, and prohibitive autoregressive decoding latency. To reconcile representation learning with institutional operational constraints, this study presents TailDART, a dense 2.68 million-parameter foundation model engineered for financial time-series forecasting. By integrating grouped-query attention into a lightweight backbone, the architecture drastically reduces Key-Value cache memory bandwidth overhead, achieving major inference acceleration (up to 48.1%) over prevailing state-of-the-art TSFMs to enable low-latency, high-throughput streaming execution. Furthermore, multi-asset benchmarks across varying temporal resolutions show that a compact model can remain competitive for market forecasting: TailDART matches the predictive fidelity of substantially larger baselines while demonstrating superior error resilience in high-volatility regimes.

---


### 170. [ABHBench: Evaluating Moral Decision-Making of Foundation Models from an Agentic Perspective](https://arxiv.org/abs/2611.09326)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chaoran Li, Yukun Li, Zeyuan Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models are increasingly deployed as agentic systems that perceive context and act autonomously, raising the need to evaluate their moral behavior as active decision-makers. Existing benchmarks, however, largely ask models to judge human actions from third-person textual vignettes, leaving untested how models behave when they themselves become the acting agent. We introduce ABHBench, a multimodal benchmark built from Detroit: Become Human, an interactive narrative game, to evaluate how foundation models make moral decisions in first-person human-android dilemmas. ABHBench places foundation models in branching narrative scenarios with visual observations, dialogue, memory, and action choices. Inspired by Asimov's Three Laws of Robotics, our framework measures Harmlessness, Obedience, and Self-preservation to capture the core tensions in human-AI relations, along with Autonomy, Stability, and Certainty to assess decision-making patterns. Across 12 foundation models, we find that moral behavior changes substantially under situated agentic context: 75% of models shift significantly between a text-only abstraction and the matched multimodal DBH scenario, and reasoning-enhanced models show no monotonic gains in consistency or human-oriented behavior. These results highlight the necessity of evaluating moral behavior in situated agentic contexts rather than relying on third-person judgment alone.

---


### 171. [Causal graph fusion across incomplete cohorts and causal steering of tabular foundation models](https://arxiv.org/abs/2611.09400)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yanke Li, Dhiyaa Al Jorf, Ayoube Ighissou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical data are split across incomplete cohorts with partially overlapping variables. Causal discovery under missing data and multi-source integration have developed separately, and tabular foundation models cannot take a causal graph without retraining. We make two contributions. First, causal graph fusion learns a partial ancestral graph on the shared variables, fuses it into each cohort's graph under temporal background knowledge and lets Markov blankets guide re-imputation, so missing data are handled inside discovery. Second, causal attention steering compiles the learned graph into the attention of a frozen tabular foundation model at inference. Against known ground truth, fusion dominates pooled and per-cohort baselines in every missingness and heterogeneity condition tested (p<0.001), and steering improves discrimination under distribution shift (p<10^{-5}), a gain that a random graph does not produce. In two spinal cord injury cohorts, fusion orients age, albumin and hemoglobin as ancestors of length of stay, a set no single cohort orients in full, and yields compact, temporally ordered predictor sets that match or exceed automatic feature selection on four of five outcomes.

---


### 172. [RadarDINO: Distilling a Visual Foundation Model into mmWave Radar for Human Mesh Reconstruction](https://arxiv.org/abs/2611.09524)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Furkan Mert Algan, Zhifan Ni, Eckehard Steinbach  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Millimeter-wave (mmWave) radar offers a privacy-preserving and illumination-robust alternative for human mesh reconstruction (HMR). However, high-fidelity radar HMR remains challenging. Sparse point cloud-based methods suffer from information loss and missed detections, while raw radar tensor methods like RT-Mesh lack fine-grained semantics and explicit local body modeling. In this paper, we propose RadarDINO, a radar HMR framework that distills visual semantics from a DINOv3 teacher into 3D radar representations and introduces explicit geometric supervision. DINOv3 descriptors are transferred to radar voxels via calibrated RGB-radar geometry, providing voxel- and body-part-level supervision for part-aware radar representations. We further incorporate vertex- and joint-losses to directly constrain reconstructed geometry. On the M4Human dataset, our method outperforms the SOTA baseline across all three evaluation splits.

---


### 173. [Test-Time Compute Scales Better with Parallel Agent Teams](https://arxiv.org/abs/2611.09798)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junlin Wang, Haozhe Chen, Ang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling improves the performance of a fixed model by spending more computation at inference. There are two common ways to spend it on agents when a verifier can score every attempt. Best-of-N sampling runs many independent agents and keeps the best result but saturates quickly. One large team of collaborating agents can score higher but stops improving as it grows. Can we get the best of both? Our method, parallel agent teams, does so by sampling many small teams in parallel and keeping the best team's result. We test it on 12 long-horizon tasks from GPU kernels and formal proofs to exploit development. With a 27B model and a budget of 100 agents, parallel teams of ten beat parallel agents on 10 of 12 tasks and beat one team of 100 on all four tasks where we ran such large teams. At equal dollar cost the same parallel teams beat a frontier model on half the tasks. A simple statistical model shows that individual agents lose because their many samples have a low mean and that one large team loses because a single sample gets no gain from variance. Sampling many small teams in parallel balances a high mean with the gain from variance. Parallel agent teams thus offer a more effective way to scale test-time compute.

---


### 174. [CodeQuant2: Enhanced Outlier Mitigation and Adaptive Clustering for Low-Precision LRMs](https://arxiv.org/abs/2611.09868)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xingyu Liu, Xiangyang Yin, Tianhua Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) improve task performance by generating longer intermediate reasoning traces, but this substantially increases inference costs and makes low-precision quantization increasingly important. However, aggressively quantized models often perform poorly on reasoning tasks. We observe larger activation fluctuations during the first decoding steps of reasoning. Calibration that omits these early states may miss their activation fluctuations. To address these reasoning-specific quantization challenges, we propose \textbf{CodeQuant2}, a clustering-based LUT quantization framework for low-precision large reasoning models. CodeQuant2 mitigates activation outliers with rotation and scaling, uses clustering to represent non-uniform weight distributions, and adapts codebook sizes to the quantization difficulty of each layer. Guided by our observation of reasoning-time activation behavior, CodeQuant2 further improves calibration sample selection to better match actual decoding statistics. Combined with our customized LUT CUDA kernel, CodeQuant2 delivers substantial accuracy improvements on reasoning benchmarks while achieving up to $2.85\times$ speedup over BF16.

---


> [!TIP]
> 当前位于：**151-174**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-174**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

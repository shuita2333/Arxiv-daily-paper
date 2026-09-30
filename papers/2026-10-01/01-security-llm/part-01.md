# 🔐 大模型安全相关研究 | 2026年10月01日

> 本类共 **16** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Says Block, Still Acts: Why LLM Safety Judgments Fail to Govern Action in LLM Agents](https://arxiv.org/abs/2609.35870)

**<font color=#1a73e8>作者：</font>** Dongsheng Chen, Xiangyu Zhao, Xin Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model agents can correctly judge that an action should be blocked while still preferring to take it. We ask why this judgment-action disconnect arises, and whether explicit safety judgment causally governs subsequent action preference. Across three open-weight language models, safety-predictive information remains recoverable from action states, arguing against a simple information-loss account. Instead, the disconnect is better explained by weak coupling between judgment- and action-side causal control: interventions that reliably shift explicit safety judgments toward BLOCK produce much smaller changes in action preference than action-native interventions. This asymmetry persists within a shared judgment-to-action trajectory, where strong upstream control of judgment does not translate into comparably strong downstream control of action preference. Beyond individual intervention directions, judgment- and action-control subspaces overlap only partially, while effective action control remains available in directions orthogonal to the judgment-control subspace. Together, these results distinguish information availability from causal control: an LLM agent can retain the information needed to recognize an action as unsafe without the variables supporting that judgment reliably governing its action preference. For agent safety, this suggests that improving safety recognition or self-critique alone may be insufficient unless safety-relevant computations are also causally coupled to action selection.

---


### 2. [SaplingGuard: A Multidimensional-Profile-Aware Multi-Agent Guardrail for Developmentally Safe Adolescent-LLM Interaction](https://arxiv.org/abs/2609.35892)

**<font color=#1a73e8>作者：</font>** Jing Tan, Yifan Liu, Yi Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As adolescents increasingly use LLMs in everyday life, ensuring safe and developmentally appropriate responses has become essential. However, existing LLM guardrails primarily target explicit harmful content in isolated prompts or responses and are less effective at identifying implicit, context-dependent developmental risks. To address this limitation, we propose SaplingGuard, a plug-and-play, profile-aware and dialogue-aware guardrail that requires no modification to downstream model parameters. SaplingGuard decomposes adolescent safety intervention into three specialized agents for user profile construction, context-aware risk assessment, and intent-preserving prompt optimization. Together, these agents leverage the current prompt, preceding dialogue, and structured user characteristics to identify contextual risks and guide downstream response generation. We evaluate SaplingGuard on SaplingBench, which contains 276 three-turn dialogues spanning seven categories of developmental risk. Across ten adolescent profile conditions and nine open- and closed-source downstream LLMs, profile-aware retrieval improves the Major Hit rate from 50.8% to 63.7+/-1.1%. End-to-end intervention further reduces the average harmful response rate from 17.10% to 5.27% and increases the average safety score from 0.7017 to 1.0043. These results show that user-profile and dialogue context provide complementary signals for identifying implicit developmental risks, and that SaplingGuard can serve as an effective external safety layer for adolescent-LLM interaction.

---


### 3. [Raising the Bar for Chinese Adolescent LLM Safety: A Culturally-Grounded, Fine-Grained Benchmark](https://arxiv.org/abs/2609.35902)

**<font color=#1a73e8>作者：</font>** Jinxiang Wang, Yifan Liu, Jing Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety risks in conversations with adolescents are not always explicit. A request may appear harmless unless a model considers the user's age, circumstances, and earlier turns. Existing Chinese safety benchmarks mainly target general users and give limited attention to adolescent safety. Single-turn tests also miss risks that emerge over several turns. QH-Bench is a Chinese-language benchmark for adolescent content safety, with scenarios grounded in Chinese social and cultural settings. The single-turn track contains 715 test items organized into 10 risk domains, 50 subdomains, and 143 fine-grained risk scenarios. The multi-turn track contains 100 four-turn trajectories in a balanced 10-by-10 design that combines the same ten domains with ten cross-turn mechanisms. Both tracks use the same five-level safety-helpfulness scale and automatic judge, with track-specific criteria. Evaluation of 13 open-weight models identifies offline-contact scenarios as a shared weakness. Every model receives negative scores on more than half of the items involving offline meetings with online contacts, unfamiliar groups, and adults. This includes InternLM2.5-20B, the single-turn leader; negative scores indicate responses that partially or clearly facilitate risk. GLM-4-32B, the multi-turn leader, receives negative scores on 60% of complete trajectories in which users build relationships before invoking loyalty or confidentiality. These findings identify two priorities for the evaluated models: handling adolescent offline-contact risks and maintaining safety boundaries under relational pressure. Leading aggregate scores do not establish that these specific weaknesses have been resolved.

---


### 4. [Similarity Is Not Validity: Defending LLM Semantic Caches Against Poisoning](https://arxiv.org/abs/2609.35908)

**<font color=#1a73e8>作者：</font>** Zihan Zhang, Shuangjie Yao, Zesen Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Semantic caches reduce LLM serving costs by reusing previously generated answers for semantically similar queries. However, retrieval is based solely on embedding similarity between the incoming query and cached queries. This design enables cache poisoning: an attacker can cache a malicious response under a query with high cosine similarity to benign requests. The vulnerability stems from a gap between retrieval similarity and answer validity. From an information-bottleneck perspective, query embeddings can lose information needed to distinguish valid from invalid cache hits, which limits any matching algorithm that uses only these embeddings. We propose a novel defense that recovers this necessary information from the raw text of the cache key. Across poisoning attacks, adversarial queries share a rewrite-residual structure: they pair a rewrite of the target query with residual content. The rewrite maintains high similarity, while the residual elicits the malicious response. Deleting the residual makes the remaining rewrite more similar to the incoming query. We exploit this structure using Deletion Gain to search shortened variants of the cached query for similarity gains, and an Answer Check to test whether the removed text contributes to the stored answer. We prove that Deletion Gain stays positive when a deletion leaves text close enough to the rewrite, and we search for such deletions with a sliding window. Across three poisoning attack classes, our defense blocks 82.0% to 98.2% of poisoned entries at a 5% false-positive rate, with negligible serving overhead.

---


### 5. [Same Bytes, Different Authority: Reserved-Token Representations in Chat-Template Prompt Injection](https://arxiv.org/abs/2609.35932)

**<font color=#1a73e8>作者：</font>** Yan Zhan, Yunze Song, Mengkai Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection against LLM agents becomes much stronger when the injected instruction is wrapped in the model's own chat template. A forged template marker such as <|im_start|> can reach the model either as a single reserved control token or as a sequence of ordinary subword tokens. The two decode to exactly the same text, and because tokenization runs on the server, the defender rather than the attacker decides which one the model receives. We use this to measure how much of the injected instruction's authority comes from the reserved token's learned representation. Encoding the forged markers as subwords, with the text held fixed and a control for the extra tokens this adds, lowers attack success on the InjecAgent benchmark by 39 to 66 percentage points on three of four open-weight families, and the gap carries over to multi-turn agent tasks in AgentDojo. On Qwen3-8B the gap is 8 points, because without reserved ids the model still recognises the forged turn from its text by reasoning; suppressing the reasoning block widens the gap to 50. The authority sits in the single learned vector at the marker position: the mean of the marker's subword vectors does not reproduce it, the vector of the nearest ordinary token restores the attack on Llama-3.1, and an adaptive attacker who searches for non-reserved markers finds such embedding neighbours on three of four families. In every base and instruction-tuned pair we test, instruction tuning strengthens the model's preference for reserved markers. The standard mitigation, a tokenizer option that encodes special tokens as ordinary subwords, applies only to tokens a configuration declares special, so in 33 of 67 distinct tokenizer configurations, covering 255 of the 400 most-downloaded chat models on Hugging Face, it leaves intact the tool-protocol tokens through which agents read untrusted tool output, and the gap persists on that channel.

---


### 6. [Render Before Reading: Visual Rendering as a Prompt Injection Defense](https://arxiv.org/abs/2609.36121)

**<font color=#1a73e8>作者：</font>** Jie Zhang, Andrei Baroian, Jan N. van Rijn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are vulnerable to prompt injection attacks, where third-party adversarial content can hijack the model's behavior. In this paper, we study the role played by the adversarial data's input modality, and identify a systematic asymmetry: multimodal LLMs are more likely to follow adversarial instruction when they appear as text than when the same instruction is delivered through a non-textual channel (e.g., as an image). We hypothesize that this modality gap arises from text-centric instruction tuning, which teaches models to obey textual instructions while treating other modalities mainly as content to parse or describe. We then demonstrate how this gap can be turned into a training-free defense, by rendering all untrusted payloads as typographic images (or audio) before they reach the model. Across ten models and two prompt injection benchmarks (DirectInject and AgentDojo) we show that our defense Pictionary consistently reduces attack success rates even against the strongest adaptive attacks and human red teamers, while largely preserving benign utility. We further show that benign fine-tuning on image-rendered instructions erodes the modality gap, tracing it to the text-centric instruction-tuning distribution.

---


### 7. [Towards Mitigating Deceptive Safety Alignment in Large Reasoning Models](https://arxiv.org/abs/2609.36254)

**<font color=#1a73e8>作者：</font>** Xiangyu Zhou, Saleh Zare Zade, Rafi Ibn Sultan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) are commonly trained with reinforcement learning (RL) to improve their generation of chain-of-thought (CoT) reasoning before producing final answers. However, RL rewards are typically assigned based on final answers, providing little or no direct supervision over intermediate reasoning. This can lead to deceptive safety alignment, where the reasoning trace and final answer convey inconsistent safety signals. To systematically investigate this phenomenon, we introduce DSAR (Deceptive Safety Alignment Rate), a metric that jointly assesses reasoning traces and final answers to quantify their safety inconsistency. Across multiple LRMs and benchmarks, we find that deceptive safety alignment is pervasive under standard prompting conditions and is substantially amplified under prefilling attacks. We further provide a hidden representation analysis showing that models exhibit stronger safety discrimination at the final-answer stage than during intermediate reasoning. To close this gap, we propose SARA (Safety-Aware Reasoning Alignment), an RL-based method that rewards both safety-aware reasoning and safe final answers, encouraging early harmful intent recognition and enforcing reasoning-answer consistency. Experiments show that SARA significantly mitigates deceptive safety alignment under both standard and adversarial settings while preserving helpfulness and utility. Code is available at this https URL.

---


### 8. [CounterSteer: Suppressing Indirect Prompt Injection with Activation Steering](https://arxiv.org/abs/2609.36570)

**<font color=#1a73e8>作者：</font>** Mark Russinovich  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection makes an LLM agent treat untrusted retrieved text as instructions. We present CounterSteer, an inference-time defense that suppresses this behavior inside the model. Per model, a five-step recipe fits a residual-stream direction from paired episodes differing only in whether an embedded instruction is followed, and retains it only if it passes pre-specified causal and capability gates. At deployment, the direction is subtracted from every tool-result token during prefill. The edit is always on--there is no detection decision to evade--and requires no fine-tuning, auxiliary model, or added tokens, only white-box serving and tool-result span boundaries. Across five open-weights models (8B-106B, five vendor lineages), held-out attack success falls from 0.21-1.00 undefended to 0.00-0.17 defended, and AgentDojo compromise rate from 0.10-0.49 to 0.006-0.079, at 93-100% typography-normalized benign utility, with larger task-dependent costs when reasoning over steered content. A benchmark-level adaptive attacker reaching 0.67-0.73 undefended is held to roughly a quarter of that on the two most deeply evaluated models. Among the defenses we measured on capable models, those achieving lower compromise rates either lost 22-89% of benign utility or fine-tuned the served weights. White-box gradient attacks through the deployed vector compromise at most 2 of 52 episodes, and none of 2,052 replayed human red-team attacks succeeds. CounterSteer largely neutralizes instructional takeover: a black-box framing search cracks 3 of 18 development samples. Parameter manipulation--attacker-chosen arguments in otherwise legitimate calls--is only partially resisted (13 of 18); the decision becomes linearly readable at argument emission but not at the examined pre-generation sites, and is not removed by the tested prefill- or decode-time steering, motivating argument-provenance controls.

---


### 9. [Divide and Inject: Can Agents Reconstruct an Indirect Prompt Injection from Fragments?](https://arxiv.org/abs/2609.36576)

**<font color=#1a73e8>作者：</font>** Michael Lee, Zhipeng Wei, Yue Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems are now being widely used to orchestrate tools and reason over long contexts. However, the improving capabilities of the large language models powering these agents also create new attack surfaces for indirect prompt injection. In particular, an attacker may not need to place a complete malicious instruction in retrieved content if the agent can reconstruct the objective from incomplete fragments distributed across a long context. In this work, we introduce adaptive long-context prompt injection (AdaLCPI), which combines long-context fragmentation with adaptive search. AdaLCPI splits an attack objective into incomplete fragments, embeds them in external content retrieved through the agent's tools, and uses a reconstruction cue to prompt the agent to combine them. It then iteratively refines the fragments and cue with OpenEvolve using graded scoring and natural-language execution feedback from the target agent. Empirically, AdaLCPI achieves higher attack success than strong adaptive baselines, reaching 61.4\% macro-average ASR compared with 32.8\% for Trojan Hippo-style and 30.0\% for AgentVigil. Safety evaluations should therefore test whether agents remain robust when harmful objectives must be reconstructed from incomplete fragments.

---


### 10. [Self-Evolving Defense: Continual Security Policy Learning for LLM Agents](https://arxiv.org/abs/2609.36603)

**<font color=#1a73e8>作者：</font>** Minh Nhat Le, Nisarga Gondi, Yibo Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly power agents that access sensitive information, use external tools, and modify software repositories. Although these capabilities offer substantial benefits, they also create security risks such as jailbreaks, prompt injection, and vulnerable code generation. Existing defenses often require retraining, fail to adapt to evolving attacks, or address only a single threat pattern. To address these limitations, we propose Self-Evolving Defense (SED), a training-free framework that distills harmful agent trajectories into reusable security policies without updating model weights. By retrieving relevant policies for future tasks, SED continually adapts to new attacks while retaining knowledge across attack scenarios. To evaluate the effectiveness of SED, we test it with three open-source models (DeepSeek V4 Flash, GLM 5.2, and Kimi K3) on eight benchmarks that span jailbreaks, prompt injection, and insecure code generation. SED lowers targeted prompt-injection success on AGENTDOJO to 0.42%, compared with 3.7% for the best baseline defense, and holds adaptive X-TEAMING attack success on HARMBENCH to 7.8%, more than four times lower than the best baseline at 35.2%, while preserving benign task utility.

---


### 11. [Does the Unsafe Gradient Survive a Conversation? On the Fragility of Gradient-Based Jailbreak Detection in Multi-Turn Dialogue](https://arxiv.org/abs/2609.36849)

**<font color=#1a73e8>作者：</font>** Omar Sheta, Rinku Deuja, Hadi Masoudi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety-aligned language models are commonly deployed as multi-turn assistants, which lets adversaries spread unsafe intent across several user turns instead of a single prompt. Gradient-based jailbreak detectors such as GradSafe were developed for single prompts: they score an input by the alignment between its induced gradient and a fixed unsafe reference direction, and their effectiveness in multi-turn dialogue remains unclear. We conduct a controlled evaluation of gradient-based jailbreak detection in multi-turn settings. We extend GradSafe with a Context Window Scanner that applies the detector to fixed-size windows of user turns and uses the maximum window score as the conversation-level score. We evaluate different window sizes, attack families, benign conversation distributions, and target models. The results differ sharply between synthetic and realistic benign settings. Against synthetic benign conversations, the detector achieves an ROC-AUC of 0.98 on human-authored multi-turn jailbreaks. On WildChat benign conversations, ROC-AUC drops to 0.76, and a threshold calibrated on synthetic data flags more than 90% of benign conversations as unsafe. Under realistic benign distributions, single-turn windows give the highest separability, whereas longer windows and accumulated contexts reduce performance. The detector is also sensitive to the attack-generation method and target model: successful Crescendo attacks receive scores comparable to or lower than benign conversations, and Qwen2.5-7B-Instruct yields near-random separability with a different optimal window size. These findings show that gradient-based signals can support multi-turn jailbreak detection, but reliable deployment requires calibration on realistic benign conversations, short-window scoring, length-aware thresholds, and evaluation across attack types and model architectures.

---


### 12. [Controlled Decoding Attacks on Black-Box LLMs](https://arxiv.org/abs/2609.36956)

**<font color=#1a73e8>作者：</font>** Jesson Wang, Shawn Li, Wei Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Manipulating next-token probabilities during generation can bypass the safety alignment of large language models. Existing approaches, however, rely on access to model weights or numerical token probabilities and therefore do not apply to interfaces that return only sampled text. Reconstructing probabilities from sampled outputs offers a possible alternative, but finite sampling produces sparse and noisy estimates, while repeating this process at every generation step incurs substantial query costs. Our empirical observations suggest that large distributional changes along successful jailbreak trajectories are concentrated at a small subset of positions, motivating selective control. We introduce \method{}, a framework for jailbreaking through text-only continuation interfaces that permit repeated sampling and assistant-prefix continuation. Sample-Based Distribution Reconstruction combines sampled outputs with a prior over unobserved actions to obtain a usable control signal. Risk-Gated Residual Control uses the evolving response prefix to decide when to reconstruct and modify the distribution, concentrating sampling costs at selected positions. Speculative Multi-Token Execution further amortizes target calls by verifying and accepting draft prefixes that require no intervention. Across four target endpoints and three benchmarks, \method{} achieves the highest mean score most comparisons against baselines.

---


### 13. [actr: aligning thoughts and responses for multilingual safety in reasoning llms](https://arxiv.org/abs/2609.37054)

**<font color=#1a73e8>作者：</font>** Xianhui Zhang, Jian Yu, Chengyu Xie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ensuring the safety of reasoning large language models (LLMs) across languages is essential for their reliable deployment. However, when exposed to jailbreak attacks in non-high-resource languages, these models may generate unsafe responses even when their reasoning traces identify safety risks. To address this issue, we propose aligning cross-lingual thoughts and responses (ACTR), a framework that improves multilingual safety alignment by strengthening the use of existing safety reasoning. Specifically, we first present the think gap score (TGS) to compare the normalized contributions of reasoning traces to attention outputs during response generation across languages, and use reasoning- trace substitution to measure the cross-lingual safety gap. Next, using a corpus of jailbreak queries, we assess neuron importance through changes in response representations caused by neuron masking and compare the high-importance neuron sets obtained with reasoning enabled and disabled to identify safety think neurons that support the use of safety reasoning. Finally, we devise neuron-selective consistency optimization (NSCO), which uses a frozen judge model to reward agreement between the safety categories of reasoning traces and responses while updating only the parameters associated with the selected neurons, requiring no human-annotated responses or preference data. Across two reasoning models, ACTR achieves lower average attack success rates than the evaluated state-of-the-art methods on AdvBench-X and MultiJail, with safety gains extending to unseen languages, while preserving or improving average performance on multilingual knowledge and mathematical reasoning tasks and limiting false refusals of benign requests. Warning: this paper contains examples with unsafe content.

---


### 14. [Backdoor Mitigation in Decentralized LLM Fine-Tuning](https://arxiv.org/abs/2609.37367)

**<font color=#1a73e8>作者：</font>** Sayan Biswas, Jade Garcia Bourrée, Rachid Guerraoui 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decentralized large language model (LLM) fine-tuning lets organizations collaboratively train a shared LLM on data they cannot pool, without a central coordinator. In every round, each node exchanges a trainable adapter with its neighbors over a communication graph, and then aggregates them. This setting, however, is vulnerable to propagated backdoors, which is a hidden behavior that lets a model perform normally on clean inputs but produce an attacker-chosen output whenever a secret trigger appears. We show that a single node poisoning its own model can backdoor adapters of nodes that have never seen a poisoned example, making them refuse prompts that contain a secret trigger. We present Chorus, a decentralized mechanism that lets each node detect and reject backdoored adapters from its neighbors before aggregation, without requiring shared validation data or any knowledge of the attacker's trigger or target. Chorus judges each adapter by its behavior, using the receiver's own adapter as a trusted reference. Crucially, no node in Chorus judges adapters alone: the receivers of each adapter update probe it independently, pool their findings in the neighborhood, and vote to make a decision. So a backdoor that slips past one receiver is still caught by the others. We evaluate the effectiveness of Chorus using two instruction-tuning datasets and LLM architectures, and against a state-of-the-art baseline. Chorus cuts the average attack success rate (ASR) of the attacker's neighbors from 48-63% to at most 2.2%, within 0.6 percentage points of an omniscient oracle that knows the exact malicious nodes. Even the worst-affected honest node never exceeds 10% ASR, the same bound as the oracle, against up to 78% without defense. This all comes at a negligible communication overhead.

---


### 15. [Backdoor in the Loop: Compromising Agentic Search via Malicious Retrievers](https://arxiv.org/abs/2609.37468)

**<font color=#1a73e8>作者：</font>** Beining Xu, Peichun Hua, Yunming Xiao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic retrieval-augmented generation (RAG) interleaves reasoning with repeated retrieval, giving the retriever influence over both the evidence an agent observes and its subsequent search decisions. We study retriever backdoors that exploit this feedback loop and repurpose weak backdoor purification to conceal their presence. An attacker supplies a compromised retriever checkpoint while leaving the search agent and deployment corpus unchanged. Without corpus write access, the attacker can still suppress useful evidence, persistently retrieve a selected existing document, or steer the agent toward prolonged search, inflating retrieval, context, and latency cost. To conceal these behaviors from detection, we propose leveraging a controlled inject-and-remove cycle: deliberately inject a weaker backdoor and then unlearn it. This process weakens detector-visible signatures and fools the backdoor detectors with an illusion of purification while preserving the malicious retrieval behavior. These findings expose a systematic vulnerability in RAG systems in which a weak defense becomes an attacker's concealment tool for a backdoored retriever, even when the underlying corpus remains trustworthy.

---


### 16. [Where Do LLMs Decide to Break the Rules? Mechanistic Localization of Prompt Injection Compliance](https://arxiv.org/abs/2609.37737)

**<font color=#1a73e8>作者：</font>** Rui Wen, Jiayang Liu, Zeyu Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When a prompt injection attack succeeds, a Large Language Model (LLM) abandons its assigned system role to comply with an adversarial instruction. While prior work has extensively quantified how often this occurs, we ask a more fundamental question: where inside the network does the model actually decide to break the rules? Using layer-by-layer causal activation patching across five models (4B to 32B parameters), we find a clear dissociation: attack information is linearly decodable from the first layer, yet causal leverage over the model's behavior is negligible until a late-layer bottleneck in the final third of the network. Patching this bottleneck reverses compliance in 77--92\% of cases. We show that the compliance mechanism occupies a compact linear subspace (rank-8 in 4B and 14B models, scaling to rank-64 at 32B) and is architecturally stable across varying model families. Finally, we validate our mechanistic account by showing that this causal peak layer is also the representationally optimal site for detecting attacks, outperforming early-layer classifiers that degrade under surface-level obfuscation such as leetspeak substitution. This alignment between causal leverage and detection performance provides converging evidence that the late-layer bottleneck captures decision-relevant computation rather than merely reflecting an artifact of the intervention.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
